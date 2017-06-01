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
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image $i$, an algorithm will produce 5 labels $l_{ij}$, $j=1,\ldots,5$. We allow 5 labels because some categories are disambiguated with additional data provided by the observer, such as latitude, longitude and date. It might also be the case that multiple categories occur in an image (e.g. a photo of a bee on a flower). For this competition each image has one ground truth label $g_i$, and the error for that image is:
$$
e_i = \min_{j}d(l_{ij}, g_i)
$$
Where
$$
d(x, y) =
\begin{cases}
    0       & \quad \text{if } x = y \\
    1  & \quad \text{otherwise}\\
\end{cases}
$$

The overall error score for an algorithm is the average error over all $N$ test images:
$$
\text{score} = \frac{1}{N} \sum_{i} e_{i}
$$

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
  * Sample images
      * This is a subset of the category images that you can download for easy viewing. Contains 3 sample categories for each of the 13 super categories.
      * Links for different parts of the world:
          * [North America [1.2GB]](https://storage.googleapis.com/us_inat_data/train_val/train_val_images_mini.tar.gz)
          * [Asia [1.2GB]](https://storage.googleapis.com/asia_inat_data/train_val/train_val_images_mini.tar.gz)
          * [Europe [1.2GB]](https://storage.googleapis.com/eu_inat_data/train_val/train_val_images_mini.tar.gz)
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
