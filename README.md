# iNaturalist Competition 
Please open an issue if you have questions or problems with the dataset.

# 2017 Competition
The 2017 competition is part of the [FGVC^4 workshop](fgvc.org) at [CVPR](http://cvpr2017.thecvf.com/). 

## Details

* Number of Species: X
* Number of Training Images: Y 
* Number of Validation Images: Z
* Number of Testing Images: W

Super Categories:

| Name | Species Count | Train + Val Image Count |
|------|---------------|-------------|
| Aves | 964 | 235521 | 
| Plantae | 2101 | 196613 |
| Insecta | 1021 | 118555 |
| Reptilia | 289 | 40881 |
| Mammalia | 186 | 32823 |
| Amphibia | 115 | 17703 |
| Mollusca | 93 | 9377 |
| Fungi | 121 | 7606 |
| Animalia | 77 | 6590 |
| Arachnida | 56 | 5959 |
| Actinopterygii | 53 | 2619 |
| Chromista | 9 | 542 |
| Protozoa | 4 | 381 |
| | | |
|Total| 5089 | 675170 |

## Evalutation
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image <img src="https://rawgit.com/visipedia/inat_comp/None/svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.642109pt height=21.60213pt/>, an algorithm will produce 5 labels <img src="https://rawgit.com/visipedia/inat_comp/None/svgs/655bedbaf4a65f397b5041d0fdecde4c.svg?invert_in_darkmode" align=middle width=15.601905pt height=22.74591pt/>, <img src="https://rawgit.com/visipedia/inat_comp/None/svgs/6d0aa77223bd2246e5cdd2a422d9e584.svg?invert_in_darkmode" align=middle width=82.4274pt height=21.60213pt/>. We allow 5 labels because some species are distinguished with additional data provided by the observer, such as latitude & longitude or date. Each image has one ground truth label <img src="https://rawgit.com/visipedia/inat_comp/None/svgs/681a37b53b66acbc455e39ca3e6f1c41.svg?invert_in_darkmode" align=middle width=12.444795pt height=14.10255pt/>, and the error for that image is:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/None/svgs/7a42826f81c53c77e0fef3c827238d25.svg?invert_in_darkmode" align=middle width=123.403665pt height=24.865665pt/></p>
Where
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/None/svgs/1b5971b5eaf03547d39e224e9cb8bd43.svg?invert_in_darkmode" align=middle width=190.2021pt height=49.13139pt/></p>

The overall error score for an algorithm is the average error over all <img src="https://rawgit.com/visipedia/inat_comp/None/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.94405pt height=22.38192pt/> test images:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/None/svgs/444adcac0c7cbb4a8419ee1484625349.svg?invert_in_darkmode" align=middle width=118.05123pt height=41.069655pt/></p>

## Annotation Format
We closely follow the annotation format of the [COCO dataset](http://mscoco.org/dataset/#download). The annotations are stored in the [JSON format](http://www.json.org/) and are organized as follows:
```
{
  "info" : info,
  "images" : [image],
  "categories" : [category],
  "annotations" : [annotation],
  "licenses" : [license]
}  

info{
  "year" : int,
  "version" : str,
  "description" : str,
  "contributor" : str,
  "url" : str,
  "date_created" : datetime,
}

image{
  "id" : int,
  "width" : int,
  "height" : int,
  "file_name" : str,
  "license" : int,
  "rights_holder" : str
}

category{
  "id" : int,
  "name" : str,
  "supercategory" : str,
}

annotation{
  "id" : int,
  "image_id" : int,
  "category_id" : int
}

license{
  "id" : int,
  "name" : str,
  "url" : str
}
```

## Submission Format
Depends on if we use Kaggle or not...
```
[{
  "image_id" : int,
  "category_id" : int,
  "score" : float
}]
```
