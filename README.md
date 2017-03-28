# iNaturalist Competition 
Please open an issue if you have questions or problems with the dataset.

# 2017 Competition
The 2017 competition is part of the [FGVC^4 workshop](fgvc.org) at [CVPR](http://cvpr2017.thecvf.com/). 

## Details

There are a total of 5,089 categories in the dataset, with 411,326 training images and 263,844 validation images. The distribution of images per category follows the observation frequecy of that category by the iNaturalist community. Therefore, there is a non-uniform distribution of images per category. 


| Super Category |	Species Count	| Train Images |	Val Images |
|------|---------------|-------------|---------------|
|Animalia|77|5228|1362|
|Actinopterygii|53|1982|637|
|Chromista|9|398|144|
|Mollusca|93|7536|1841|
|Fungi|121|5826|1780|
|Reptilia|289|35201|5680|
|Mammalia|186|29333|3490|
|Amphibia|115|15318|2385|
|Protozoa|4|308|73|
|Aves|964|214295|21226|
|Insecta|1021|100479|18076|
|Arachnida|56|4873|1086|
|Plantae|2101|158407|38206|
|||||
|Total|13|579184|95986|


## Evalutation
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.642109pt height=21.60213pt/>, an algorithm will produce 5 labels <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/655bedbaf4a65f397b5041d0fdecde4c.svg?invert_in_darkmode" align=middle width=15.601905pt height=22.74591pt/>, <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/6d0aa77223bd2246e5cdd2a422d9e584.svg?invert_in_darkmode" align=middle width=82.4274pt height=21.60213pt/>. We allow 5 labels because some categories are distinguished with additional data provided by the observer, such as latitude, longitude and date. It might also be the case that multiple categories occur in an image (e.g. a photo of a bee on a flower). For this competition each image has one ground truth label <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/681a37b53b66acbc455e39ca3e6f1c41.svg?invert_in_darkmode" align=middle width=12.444795pt height=14.10255pt/>, and the error for that image is:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/svgs/7a42826f81c53c77e0fef3c827238d25.svg?invert_in_darkmode" align=middle width=123.403665pt height=24.865665pt/></p>
Where
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/svgs/1b5971b5eaf03547d39e224e9cb8bd43.svg?invert_in_darkmode" align=middle width=190.2021pt height=49.13139pt/></p>

The overall error score for an algorithm is the average error over all <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.94405pt height=22.38192pt/> test images:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/svgs/444adcac0c7cbb4a8419ee1484625349.svg?invert_in_darkmode" align=middle width=118.05123pt height=41.069655pt/></p>

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


# Terms of Use

By downloading this dataset you agree to the following terms:

1. You will abide by the [iNaturalist Terms of Service](https://www.inaturalist.org/pages/terms)
2. You will use the data only for non-commercial research and educational purposes.
3. You will NOT distribute the above images.
4. The Califonia Insitute of Technology makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
5. You accept full responsibility for your use of the data and shall defend and indemnify the Califonia Insitute of Technology, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.

