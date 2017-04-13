![Banner](https://rawgit.com/visipedia/inat_comp/master/assets/banner.jpg)

# iNaturalist Competition 
Please open an issue if you have questions or problems with the dataset.

# 2017 Competition
The 2017 competition, sponsored by Google, is part of the [FGVC^4 workshop](http://fgvc.org) at [CVPR](http://cvpr2017.thecvf.com/). 

## Dates
|||
|------|---------------|
Data Released|April 5, 2017|
Submission Server Open |June 2017|
Submission Deadline|June 30, 2017|
Winners Announced|July 21, 2017|

## Details

There are a total of 5,089 categories in the dataset, with 579,184 training images and 95,986 validation images. For the training set, the distribution of images per category follows the observation frequency of that category by the iNaturalist community. Therefore, there is a non-uniform distribution of images per category. 


| Super Category |	Category Count	| Train Images |	Val Images |
|------|---------------|-------------|---------------|
Plantae|2,101|158,407|38,206|
Insecta|1,021|100,479|18,076|
Aves|964|214,295|21,226|
Reptilia|289|35,201|5,680|
Mammalia|186|29,333|3,490|
Fungi|121|5,826|1,780|
Amphibia|115|15,318|2,385|
Mollusca|93|7,536|1,841|
Animalia|77|5,228|1,362|
Arachnida|56|4,873|1,086|
Actinopterygii|53|1,982|637|
Chromista|9|398|144|
Protozoa|4|308|73|
|||||
|Total|5,089|579,184|95,986|


## Evaluation
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.642109pt height=21.60213pt/>, an algorithm will produce 5 labels <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/655bedbaf4a65f397b5041d0fdecde4c.svg?invert_in_darkmode" align=middle width=15.601905pt height=22.74591pt/>, <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/6d0aa77223bd2246e5cdd2a422d9e584.svg?invert_in_darkmode" align=middle width=82.4274pt height=21.60213pt/>. We allow 5 labels because some categories are disambiguated with additional data provided by the observer, such as latitude, longitude and date. It might also be the case that multiple categories occur in an image (e.g. a photo of a bee on a flower). For this competition each image has one ground truth label <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/681a37b53b66acbc455e39ca3e6f1c41.svg?invert_in_darkmode" align=middle width=12.444795pt height=14.10255pt/>, and the error for that image is:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/svgs/7a42826f81c53c77e0fef3c827238d25.svg?invert_in_darkmode" align=middle width=123.403665pt height=24.865665pt/></p>
Where
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/svgs/1b5971b5eaf03547d39e224e9cb8bd43.svg?invert_in_darkmode" align=middle width=190.2021pt height=49.13139pt/></p>

The overall error score for an algorithm is the average error over all <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.94405pt height=22.38192pt/> test images:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/svgs/444adcac0c7cbb4a8419ee1484625349.svg?invert_in_darkmode" align=middle width=118.05123pt height=41.069655pt/></p>

## Guidelines

Participants are restricted to train their algorithms on iNaturalist 2017 train and validation sets. Pretrained models may be used to construct the algorithms (e.g. ImageNet pretrained models) as long as participants do not actively collect additional data for the target categories of the iNaturalist 2017 competition. Please specify any and all external data used for training when uploading results.

The general rule is that we want participants to use only the provided training and validation images to train a model to classify the test images. We do not want participants crawling the web in search of additional data for the target categories. Participants should be in the mindset that this is the only data available for those categories.

Participants are allowed to collect additional annotations (e.g. bounding boxes) on the provided training and validation sets. Teams should specify that they collected additional annotations when submitting results. 

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
*TBD*
The submission format is still being determined. It may look similar to:
```
[{
  "image_id" : int,
  "category_id" : int,
  "score" : float
}]
```

## Terms of Use

By downloading this dataset you agree to the following terms:

1. You will abide by the [iNaturalist Terms of Service](https://www.inaturalist.org/pages/terms)
2. You will use the data only for non-commercial research and educational purposes.
3. You will NOT distribute the above images.
4. The California Institute of Technology makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
5. You accept full responsibility for your use of the data and shall defend and indemnify the California Institute of Technology, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.

## Data

Download the dataset files here:
  * [Training and validation images [186GB]](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc4_competition/train_val_images.tar.gz)
      * An alternate (potentially faster) download link is available [here [186GB]](https://s3-us-west-2.amazonaws.com/inaturalist-fgvc-competition-2017/train_val_images.tar.gz).
      * Running `md5sum` on the tar.gz file should produce `7c784ea5e424efaec655bd392f87301f  train_val_images.tar.gz`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `train_val_images/super category/category/image.jpg`. This may take a while.
  * [Training and validation annotations [26MB]](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc4_competition/train_val2017.zip)
  
  * [Sample images [1.2GB]](https://s3-us-west-2.amazonaws.com/inaturalist-fgvc-competition-2017/train_val_images_mini.tar.gz)
     * This is a subset of the category images that you can download for easy viewing. Contains 3 sample categories for each of the 13 super categories.
