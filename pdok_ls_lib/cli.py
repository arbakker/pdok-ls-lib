"""Console script for pdok_ls_lib."""
import argparse
import sys
import json
import click

from qgis.core import (
    QgsApplication,
    QgsProcessingFeedback,
    QgsVectorLayer,
    QgsField,
    QgsFields,
    QgsProperty,
    QgsProcessingFeatureSourceDefinition,
    QgsProcessingOutputLayerDefinition
)


import pdok_ls_lib.pdok_ls_lib as ls


def main():
    # start QGIS instance without GUI
    QgsApplication.setPrefixPath('/usr/share/qgis', True)
    myqgs = QgsApplication([], False)
    myqgs.initQgis()

    """Console script for pdok_ls_lib."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))

    locatie_server = ls.LocatieServer()

    # lookup
    # result = locatie_server.lookup_object(
    #     "wpl-f7e8b358f41a73d500713d08eed621b6", ls.Projection.EPSG_28992)

    # suggest
    # type_filter_query = ls.TypeFilterQuery(
    #     gemeente=False, woonplaats=True, weg=False, postcode=False, adres=False)
    # result = locatie_server.suggest_query(
    #     "Haarlem", type_filter_query)

    # free
    type_filter_query = ls.TypeFilterQuery(
        gemeente=False, woonplaats=False, weg=True, postcode=False, adres=False)
    result = locatie_server.free_query(
        "Ferdinand Bolstraat and Utrecht")
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
