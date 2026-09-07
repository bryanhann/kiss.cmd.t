from __my__ import my

def _test_remote():
    repo = my.repo.remote
    repo.destroy()
    assert not repo.exists()
    repo.create()
    assert repo.exists()
    repo.destroy()
    assert not repo.exists()

def test_local():
    my.repo.remote.create()
    repo = my.repo.local
    repo.destroy()
    assert not repo.exists()
    repo.create()
    assert repo.exists()
    repo.destroy()
    assert not repo.exists()
