from river import stream

from . import base


class MovieLens100K(base.RemoteDataset):
    """MovieLens 100K dataset.

    MovieLens datasets were collected by the GroupLens Research Project at the University of
    Minnesota. This dataset consists of 100,000 ratings (1-5) from 943 users on 1682 movies. Each
    user has rated at least 20 movies. User and movie information are provided. The data was
    collected through the MovieLens web site (movielens.umn.edu) during the seven-month period from
    September 19th, 1997 through April 22nd, 1998.

    References
    ----------
    [^1]: [The MovieLens Datasets: History and Context](http://dx.doi.org/10.1145/2827872)

    """

    def __init__(self):
        super().__init__(
            n_samples=100_000,
            n_features=10,
            task=base.REG,
            url='https://maxhalford.github.io/files/datasets/ml_100k.zip',
            size=11057876,
            filename='ml_100k.csv'
        )

    def _iter(self):
        return stream.iter_csv(
            self.path,
            target='rating',
            converters={
                'timestamp': int,
                'release_date': int,
                'age': float,
                'rating': float
            },
            delimiter='\t'
        )
