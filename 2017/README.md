![Banner](https://rawgit.com/visipedia/inat_comp/master/2017/assets/banner.jpg)

# iNaturalist Competition
Please open an issue if you have questions or problems with the dataset.

# 2017 Competition
The 2017 competition, sponsored by Google, is part of the [FGVC^4 workshop](http://fgvc.org) at [CVPR](http://cvpr2017.thecvf.com/).

## Updates
August 17th, 2020:
  * AWS S3 download links were created due to problems with the original Google and Caltech links. The dataset files are in a "requester pays" bucket, so you will need to download them through an AWS API. See the [Data](#Data) section below. 

August 16th, 2019: 
  * Additional metadata in the form of latitude, longitude, date, and user_id for each of images in the train and validation sets can be found [here](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc4_competition/inat2017_locations.zip).

## Kaggle
We are using Kaggle to host the leaderboard. Checkout the competition page [here](https://www.kaggle.com/c/inaturalist-challenge-at-fgvc-2017).

## Dates
|||
|------|---------------|
Data Released|April 5, 2017|
[Submission Server Open](https://www.kaggle.com/c/inaturalist-challenge-at-fgvc-2017) |June 1, 2017|
Submission Deadline|July 7, 2017|
Winners Announced|July 21, 2017|

## Details

There are a total of 5,089 categories in the dataset, with 579,184 training images and 95,986 validation images. For the training set, the distribution of images per category follows the observation frequency of that category by the iNaturalist community. Therefore, there is a non-uniform distribution of images per category. Example images, along with their unique [GBIF](http://www.gbif.org/) ID numbers (where available), can be viewed [here](https://docs.google.com/spreadsheets/d/1JHn6J_9HBYyN5kaVrH1qcc3VMyxOsV2II8BvSwufM54).


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
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image <img src="https://rawgit.com/visipedia/inat_comp/master/2017/svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.642109000000004pt height=21.602129999999985pt/>, an algorithm will produce 5 labels <img src="https://rawgit.com/visipedia/inat_comp/master/2017/svgs/655bedbaf4a65f397b5041d0fdecde4c.svg?invert_in_darkmode" align=middle width=15.601905000000002pt height=22.745910000000016pt/>, <img src="https://rawgit.com/visipedia/inat_comp/master/2017/svgs/6d0aa77223bd2246e5cdd2a422d9e584.svg?invert_in_darkmode" align=middle width=82.4274pt height=21.602129999999985pt/>. We allow 5 labels because some categories are disambiguated with additional data provided by the observer, such as latitude, longitude and date. It might also be the case that multiple categories occur in an image (e.g. a photo of a bee on a flower). For this competition each image has one ground truth label <img src="https://rawgit.com/visipedia/inat_comp/master/2017/svgs/681a37b53b66acbc455e39ca3e6f1c41.svg?invert_in_darkmode" align=middle width=12.444795000000004pt height=14.102549999999994pt/>, and the error for that image is:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/2017/svgs/7a42826f81c53c77e0fef3c827238d25.svg?invert_in_darkmode" align=middle width=123.40366499999999pt height=24.865665pt/></p>
Where
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/2017/svgs/7a45c501d5042bd031a267f008fa2ae6.svg?invert_in_darkmode" align=middle width=190.2021pt height=49.131389999999996pt/></p>

The overall error score for an algorithm is the average error over all <img src="https://rawgit.com/visipedia/inat_comp/master/2017/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.944050000000002pt height=22.381919999999983pt/> test images:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/2017/svgs/444adcac0c7cbb4a8419ee1484625349.svg?invert_in_darkmode" align=middle width=118.05122999999999pt height=41.069655pt/></p>

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

The submission format for the Kaggle competition is a csv file with the following format:
```
id,predicted
12345,0 78 23 3 42
67890,83 13 42 0 21
```
The `id` column corresponds to the test image id. The `predicted` column corresponds to 5 category ids, separated by spaces. You should have one row for each test image.

## Bounding Boxes

A *subset* of the dataset has been annotated with bounding boxes, please see the [paper](https://arxiv.org/abs/1707.06642) for the full details on how the boxes were collected. The following super categories were annotated: 

| Super Category | Train Boxes |	Val Boxes |
|------|---------------|-------------|
Insecta|106,304|16,732|
Aves|283,931|17,314|
Reptilia|36,476|5,480|
Mammalia|31,109|2,654|
Amphibia|15,812|2,280|
Mollusca|8,566|1,571|
Animalia|6,643|1,143|
Arachnida|4,752|1,051|
Actinopterygii|2,571|511|
|||||
|Total|496,164|48,736|

The bounding box format follows the COCO format:
```
annotation{
  "id" : int,
  "image_id" : int,
  "category_id" : int,
  "bbox" : [x, y, width, height],
  "area" : float,
  "iscrowd" : 0
}
``` 
The `bbox` units are in pixels, the origin is the upper left hand corner, and the `area` value is approximated as `(width * height) / 2.0` since we did not collect segmentation masks.

### Bounding Box Caveats:
  * Crowdworkers were asked to annotate at the *super category* level rather than the *category* level. Therefore, for images with multiple box annotations there is *no guarantee* that all instances actually belong to the same *category* even though they are labeled as being the same category (e.g. multiple bird species could be boxed in an image and labeled as the same species). Rather, the boxed instances will belong to the same *super category*. Due to this problem, the validation set is restricted to images with single instances so that we can be confident the category label is correct for the given box.    
  * `iscrowd` is hard coded to `0` for all annotations, although it is possible that a box is around a crowd of instances (such as barnacles or mussels).

## Terms of Use

By downloading this dataset you agree to the following terms:

1. You will abide by the [iNaturalist Terms of Service](https://www.inaturalist.org/pages/terms)
2. You will use the data only for non-commercial research and educational purposes.
3. You will NOT distribute the above images.
4. The California Institute of Technology makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
5. You accept full responsibility for your use of the data and shall defend and indemnify the California Institute of Technology, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.

## Data

Due to some issues with the original Google and Caltech links, we have made the dataset available via a "[requester pays](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)" bucket on AWS S3. To download the dataset files from S3 you must use an AWS API tool so that AWS knows who to charge for the data egress fees. Once you have an AWS account set up, the [s3cmd](https://s3tools.org/s3cmd) tool makes downloading the dataset very easy. 

AWS S3 Bucket Paths:
  * Training and validation images [186GB]
    * s3://inaturalist-datasets/2017/train_val_images.tar.gz
  * Training and validation annotations [26MB]
    * s3://inaturalist-datasets/2017/train_val2017.zip
  * Training bounding box annotations [22MB]
    * s3://inaturalist-datasets/2017/train_2017_bboxes.zip
  * Validation bounding box annotations [3MB]
    * s3://inaturalist-datasets/2017/val_2017_bboxes.zip
  * Location annotations (train and val) [12MB]
    * s3://inaturalist-datasets/2017/inat2017_locations.zip
  * Test images [53GB]
    * s3://inaturalist-datasets/2017/test2017.tar.gz
  * Test image info [6.3MB]
    * s3://inaturalist-datasets/2017/test2017.zip

Example s3cmd usage for downloading the training and validation images:
```
pip install s3cmd

s3cmd \
--access_key XXXXXXXXXXXXXXXXXXXX \
--secret_key XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
--requester-pays \
get s3://inaturalist-datasets/2017/train_val_images.tar.gz .
```

### **The following links are currently broken but the information is still relevant.**

Download the dataset files here:
  * [Training and validation images [186GB]](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc4_competition/train_val_images.tar.gz)
      * Alternate links for different parts of the world:
          * [North America [186GB]](https://storage.googleapis.com/us_inat_data/train_val/train_val_images.tar.gz)
          * [Asia [186GB]](https://storage.googleapis.com/asia_inat_data/train_val/train_val_images.tar.gz)
          * [Europe [186GB]](https://storage.googleapis.com/eu_inat_data/train_val/train_val_images.tar.gz)
      * Running `md5sum` on the tar.gz file should produce `7c784ea5e424efaec655bd392f87301f  train_val_images.tar.gz`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `train_val_images/super category/category/image.jpg`. This may take a while.
  * [Training and validation annotations [26MB]](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc4_competition/train_val2017.zip)
      * Alternate links for different parts of the world:
          * [North America [26MB]](https://storage.googleapis.com/us_inat_data/train_val/train_val2017.zip)
          * [Asia [26MB]](https://storage.googleapis.com/asia_inat_data/train_val/train_val2017.zip)
          * [Europe [26MB]](https://storage.googleapis.com/eu_inat_data/train_val/train_val2017.zip)
  * [Training bounding box annotations [22MB]](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc4_competition/train_2017_bboxes.zip)
  * [Validation bounding box annotations [3MB]](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc4_competition/val_2017_bboxes.zip)
  * Sample images
      * This is a subset of the category images that you can download for easy viewing. Contains 3 sample categories for each of the 13 super categories.
      * Links for different parts of the world:
          * [North America [1.2GB]](https://storage.googleapis.com/us_inat_data/train_val/train_val_images_mini.tar.gz)
          * [Asia [1.2GB]](https://storage.googleapis.com/asia_inat_data/train_val/train_val_images_mini.tar.gz)
          * [Europe [1.2GB]](https://storage.googleapis.com/eu_inat_data/train_val/train_val_images_mini.tar.gz)
  * [Location annotations (train and val) [12MB]](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc4_competition/inat2017_locations.zip)
      * Running `md5sum inat2017_locations.zip` should produce `afc1956f9a100b165b89f3923d040912`
  * [Test images [53GB]](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc4_competition/test2017.tar.gz)
      * Alternative links for different parts of the world:
          * [North America [53GB]](https://storage.googleapis.com/us_inat_data/test/test2017_images.tar.gz)
          * [Asia [53GB]](https://storage.googleapis.com/asia_inat_data/test/test2017_images.tar.gz)
          * [Europe [53GB]](https://storage.googleapis.com/eu_inat_data/test/test2017_images.tar.gz)
      * Running `md5sum` on the tar.gz file should produce `7d9b096fa1cd94d67a0fa779ea301234  test2017.tar.gz`
      * Images have a max dimension of 800px and have been converted to JPEG format
  * [Test image info [6.3MB]](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc4_competition/test2017.zip)
      * Alternative links for different parts of the world:
          * [North America [6.3MB]](https://storage.googleapis.com/us_inat_data/test/test2017.zip)
          * [Asia [6.3MB]](https://storage.googleapis.com/asia_inat_data/test/test2017.zip)
          * [Europe [6.3MB]](https://storage.googleapis.com/eu_inat_data/test/test2017.zip)
