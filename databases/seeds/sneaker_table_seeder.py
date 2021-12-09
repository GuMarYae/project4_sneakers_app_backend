"""SneakerTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Sneaker import Sneaker


class SneakerTableSeeder(Seeder):
    def run(self):
        Sneaker.create({"brand": "Nike", "name": "Lebron 19", "cost": "$200", "year": "2021", "image": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/c2db773f-985f-4676-88ec-4674abf99594/lebron-19-basketball-shoe.png"})
        Sneaker.create({"brand": "Vans", "name": "Vans Sk8-Hi GORE-TEX MTE3 Shoes", "cost": "$165", "year": "2021", "image": "https://scene7.zumiez.com/is/image/zumiez/product_main_medium_2x/Vans-Sk8-Hi-Gore-Tex-MTE3-Tiger-Camo-%26-Black-shoes-_347861-front-US.jpg"})
        Sneaker.create({"brand": "Gianni Bini", "name": "Oliveen", "cost": "$140", "year": "2021", "image": "https://dimg.dillards.com/is/image/DillardsZoom/mainProduct/gianni-bini-oliveen-leather-buckle-detail-dress-booties/00000000_zi_3a2e4902-1b9d-4538-9022-92c912f90783.jpg"})
        Sneaker.create({"brand": "Gianni Bini", "name": "Bexxlie", "cost": "$100", "year": "2021", "image": "https://dimg.dillards.com/is/image/DillardsZoom/mainProduct/gianni-bini-bexxlie-strappy-leather-square-toe-sculptural-heel-dress-sandals/00000000_zi_28e46e82-c11f-4e81-911b-24ef7480ad21.jpg"})
        Sneaker.create({"brand": "Reebok", "name": "Yeezy 700 V3 Copperfade", "cost": "$200", "year": "2021", "image": "https://assets.adidas.com/images/w_840,h_840,q_auto:sensitive/48d6aadfd11d407da2caadef01542ccc_9366/GY4109_01_standard.jpg"})
        Sneaker.create({"brand": "Bottega Veneta", "name": "Loafers", "cost": "$1050", "year": "2021", "image": "https://bottega-veneta.dam.kering.com/m/22599fc512cb2d9d/Medium-651350V0G802113_A.jpg"})
        Sneaker.create({"brand": "Nike", "name": "Kobe 9 Christmas", "cost": "$225", "year": "2014", "image": "https://images.solecollector.com/complex/image/upload/ge0cbfgxigecwtcpsmpb.jpg"})
