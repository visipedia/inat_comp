![Banner](https://rawgit.com/visipedia/inat_comp/master/assets/banner2019.gif)

# iNaturalist 2019 Competition
The 2019 competition is part of the [FGVC^6 workshop](https://sites.google.com/view/fgvc6/home) at [CVPR](http://cvpr2019.thecvf.com/).

Please open an issue if you have questions or problems with the dataset.

## Updates
August 6th, 2019: 
  * Un-obfuscated names are released. Simply replace the `categories` list in the dataset files with the list found in this [file](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc6_competition/categories.json.tar.gz).

  * Thanks to everyone who attended and participated in the [FGVC6 workshop](https://sites.google.com/view/fgvc6/home)! Slides from the competition overview can be found [here](https://drive.google.com/file/d/1Ah5haDF6kFioQzy45-HKTsxZCqGwondf/view).

## Kaggle
We are using Kaggle to host the leaderboard. Checkout the competition page [here](https://www.kaggle.com/c/inaturalist-2019-fgvc6).

## Dates
|||
|------|---------------|
Data Released|March, 2019|
Submission Server Open |March, 2019|
Submission Deadline|June, 2019|
Winners Announced|June, 2019|

## Details
There are a total of 1,010 species in the dataset, spanning 72 genera, with a combined training and validation set of 268,243 images. The dataset was constructed such that each genera contains at least 10 species, making the dataset inherently fine-grained. 

![Train Val Distribution](https://rawgit.com/visipedia/inat_comp/master/assets/train_val_distribution2019.png)


## Evaluation
This competition employs average top-1 error. For each image <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.642109000000004pt height=21.602129999999985pt/>, an algorithm will produce 1 label <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/bb29cf3d0decad4c2df62b08fbcb2d23.svg?invert_in_darkmode" align=middle width=9.520170000000002pt height=22.745910000000016pt/>. Each image has one ground truth label <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/681a37b53b66acbc455e39ca3e6f1c41.svg?invert_in_darkmode" align=middle width=12.444795000000004pt height=14.102549999999994pt/>, and the error for that image is:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/svgs/d04cfdb4d46bd80e8835a37572804c82.svg?invert_in_darkmode" align=middle width=87.16207499999999pt height=16.376943pt/></p>
Where
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/svgs/7a45c501d5042bd031a267f008fa2ae6.svg?invert_in_darkmode" align=middle width=190.2021pt height=49.131389999999996pt/></p>

The overall error score for an algorithm is the average error over all <img src="https://rawgit.com/visipedia/inat_comp/master/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.944050000000002pt height=22.381919999999983pt/> test images:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/master/svgs/444adcac0c7cbb4a8419ee1484625349.svg?invert_in_darkmode" align=middle width=118.05122999999999pt height=41.069655pt/></p>

## Differences from iNaturalist 2018 Competition
The primary difference between the 2019 competition and the [2018 Competition](2018/README.md) is the way species were selected for the dataset. For the 2019 dataset, we filtered out all species that had insufficient observations. From this reduced set, we filtered out all species that were not members of genera with at least 10 species remaining. This produced a dataset of 72 genera, each with at least 10 species, for a total of 1,010 species. Our aim was to produce a collection of fine-grained problems that are representative of the natural world. We made the evalue metric more strict in 2019, going to top-1 error as opposed to top-3. 





## Guidelines

Participants are welcome to use the [iNaturalist 2018](2018/README.md) and [iNaturalist 2017](2017/README.md) competition datasets as an additional data source. There is an overlap between the 2017 & 2018 species and the 2019 species, however we do not provide a mapping. Besides using the 2017 and 2018 datasets, participants are restricted from collecting additional natural world data for the 2019 competition. Pretrained models may be used to construct the algorithms (e.g. ImageNet pretrained models, or iNaturalist 2017 pretrained models). Please specify any and all external data used for training when uploading results.

The general rule is that participants should only use the provided training and validation images (with the exception of the allowed pretrained models) to train a model to classify the test images. We do not want participants crawling the web in search of additional data for the target categories. Participants should be in the mindset that this is the only data available for these categories.

Participants are allowed to collect additional annotations (e.g. bounding boxes, keypoints) on the provided training and validation sets. Teams should specify that they collected additional annotations when submitting results.

## Annotation Format
We follow the annotation format of the [COCO dataset](http://mscoco.org/dataset/#download) and add additional fields. The annotations are stored in the [JSON format](http://www.json.org/) and are organized as follows:
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
  "kingdom" : str,
  "phylum" : str,
  "class" : str,
  "order" : str,
  "family" : str,
  "genus" : str
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
12345,0
67890,83
```
The `id` column corresponds to the test image id. The `predicted` column corresponds to the predicted category ids. You should have one row for each test image.

## Terms of Use

By downloading this dataset you agree to the following terms:

1. You will abide by the [iNaturalist Terms of Service](https://www.inaturalist.org/pages/terms)
2. You will use the data only for non-commercial research and educational purposes.
3. You will NOT distribute the above images.
4. The California Institute of Technology makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
5. You accept full responsibility for your use of the data and shall defend and indemnify the California Institute of Technology, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.

## Data

Kaggle is hosting the dataset and can be downloaded by joining the [competition](https://www.kaggle.com/c/inaturalist-2019-fgvc6) and going to the [Data page](https://www.kaggle.com/c/inaturalist-2019-fgvc6/data). We also provide posterity links via Caltech servers. Downloading the data from Kaggle will be faster. 

### Caltech Links:
  * All training and validation images [74GB]
      * [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc6_competition/train_val2019.tar.gz). Warning this will be slow.
      * Running `md5sum train_val2019.tar.gz` should produce `c60a6e2962c9b8ccbd458d12c8582644`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `train_val2019/super category/category/image.jpg`. This may take a while.
  * Training annotations [13MB]
      * [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc6_competition/train2019.json.tar.gz)
      * Running `md5sum train2019.json.tar.gz` should produce `b06a6683537867c0d5c7a45f407a306d`
  * Validation annotations [156KB]
      * [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc6_competition/val2019.json.tar.gz)
      * Running `md5sum val2019.json.tar.gz` should produce `5cc5509b0fe495f1c8c1362612448497`
  * Test images [8.6GB]
      * [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc6_competition/test2019.tar.gz). Warning this will be slow.
      * Running `md5sum test2019.tar.gz` should produce `6966703cc589a877689dc8993bb3e55e`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `test2019/image.jpg`.
  * Test image info [1.3MB]
      * [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc6_competition/test2019.json.tar.gz)
      * Running `md5sum test2019.json.tar.gz` should produce `f3208996d9f675462cb00d2f18cbb28c`

## Previous Competitions
* [2018 Competition](2018/README.md)
* [2017 Competition](2017/README.md)
