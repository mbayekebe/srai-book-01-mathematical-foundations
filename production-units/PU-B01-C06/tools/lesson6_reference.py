import numpy as np
def eigenpair_residual(a, eigenvalue, eigenvector):
    """Scale-aware residual; reject nonfinite, nonsquare and zero-vector inputs."""
    a=np.asarray(a, dtype=complex)
    v=np.asarray(eigenvector, dtype=complex)
    if a.ndim != 2 or a.shape[0] != a.shape[1] or a.shape[0] == 0:
        raise ValueError('A must be nonempty and square')
    if v.ndim != 1 or len(v) != len(a):
        raise ValueError('Vector dimensions do not agree')
    if not np.isfinite(a).all() or not np.isfinite(v).all() or not np.isfinite(eigenvalue):
        raise ValueError('Inputs must be finite')
    scale=np.max(np.abs(v))
    if scale == 0:
        raise ValueError('Zero vector is not an eigenvector')
    u=v/scale
    u=u/np.linalg.norm(u)
    numerator=np.linalg.norm(a@u-eigenvalue*u)
    denominator=np.linalg.norm(a, 2)+abs(eigenvalue)
    return float(numerator/denominator if denominator else numerator)

def residual_power_iteration(a, initial=None, tol=1e-10, max_iter=10000):
    """Real-matrix teaching implementation; reports residual and iteration count.

    A small residual certifies an approximate eigenpair, not dominance.
    Suitable spectral separation and an appropriate start are required.
    """
    if np.iscomplexobj(a) or (initial is not None and np.iscomplexobj(initial)):
        raise ValueError('This reference iteration accepts real inputs only')
    a=np.asarray(a, dtype=float)
    if a.ndim != 2 or a.shape[0] != a.shape[1] or len(a)==0 or not np.isfinite(a).all():
        raise ValueError('A must be finite, nonempty and square')
    if not np.isfinite(tol) or tol <= 0 or not isinstance(max_iter, int) or max_iter < 1:
        raise ValueError('Positive tolerance and integer iteration limit required')
    v=np.ones(len(a)) if initial is None else np.asarray(initial, dtype=float).copy()
    if v.shape != (len(a),) or not np.isfinite(v).all() or np.max(np.abs(v))==0:
        raise ValueError('Initial vector must be finite, nonzero and dimension-compatible')
    v=v/np.max(np.abs(v)); v=v/np.linalg.norm(v)
    a_scale=np.max(np.abs(a))
    if a_scale==0:
        return {'value':0., 'vector':v, 'iterations':0, 'residual':0.}
    scaled=a/a_scale
    for iteration in range(1,max_iter+1):
        w=scaled@v
        norm=np.linalg.norm(w)
        if norm==0 or not np.isfinite(norm):
            raise ValueError('Iteration reached zero/nonfinite vector; choose another start')
        v=w/norm
        value=float(v@a@v)
        residual=eigenpair_residual(a,value,v)
        if residual<=tol:
            return {'value':value, 'vector':v, 'iterations':iteration, 'residual':residual}
    raise RuntimeError('No residual convergence within max_iter; no eigenpair accepted')
