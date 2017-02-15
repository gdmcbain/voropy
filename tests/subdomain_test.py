# -*- coding: utf-8 -*-
#
import fetch_data
import voropy


def test_get_edges():
    filename = fetch_data.download_mesh(
            'pacman.msh',
            '2da8ff96537f844a95a83abb48471b6a'
            )
    mesh, _, _, _ = voropy.read(filename)
    mesh.create_edges()
    mesh.mark_default_subdomains()
    edges = mesh.get_edges('everywhere')
    assert len(edges) == 1276
    return


def test_mark_subdomain():
    filename = fetch_data.download_mesh(
            'pacman.msh',
            '2da8ff96537f844a95a83abb48471b6a'
            )
    mesh, _, _, _ = voropy.read(filename)

    class Subdomain(object):
        def __init__(self):
            self.is_boundary_only = True
            return

        def is_inside(self, x):
            return x[0] < 0.0

    sd = Subdomain()
    mesh.mark_subdomain(sd)
    assert len(mesh.subdomains[sd]['vertices']) == 27
    return
