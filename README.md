![Banner](https://rawgit.com/visipedia/inat_comp/2018/assets/banner2018.jpg)

# iNaturalist 2018 Competition
The 2018 competition is part of the [FGVC^5 workshop](http://fgvc.org) at [CVPR](http://cvpr2018.thecvf.com/).

Please open an issue if you have questions or problems with the dataset.

## Kaggle
We are using Kaggle to host the leaderboard. Checkout the competition page [here]().

## Dates
|||
|------|---------------|
Data Released|February, 2018|
Submission Server Open |February, 2018|
Submission Deadline|June, 2018|
Winners Announced|June, 2018|

## Details
There are a total of 8,142 species in the dataset, with 437,513 training and 24,426 validation images.

| Super Category |	Category Count	| Train Images |	Val Images |
|------|---------------|-------------|---------------|
Plantae|2,917|118,800|8,751|
Insecta|2,031|87,192|6,093|
Aves|1,258|143,950|3,774|
Actinopterygii|369|7,835|1,107|
Fungi|321|6,864|963|
Reptilia|284|22,754|852|
Mollusca|262|8,007|786|
Mammalia|234|20,104|702|
Animalia|178|5,966|534|
Amphibia|144|11,156|432|
Arachnida|114|4,037|342|
Chromista|25|621|75|
Protozoa|4|211|12|
Bacteria|1|16|3|
|||||
Total|8,142|437,513|24,426|

![Train Val Distribution](https://rawgit.com/visipedia/inat_comp/2018/assets/train_val_distribution.png)

## Evaluation
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image <img src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.642109pt height=21.60213pt/>, an algorithm will produce 3 labels <img src="svgs/655bedbaf4a65f397b5041d0fdecde4c.svg?invert_in_darkmode" align=middle width=15.601905pt height=22.74591pt/>, <img src="svgs/946e592e2b2753a9272767ae3dd5b9a9.svg?invert_in_darkmode" align=middle width=82.4274pt height=21.60213pt/>. We allow 3 labels because some categories are disambiguated with additional data provided by the observer, such as latitude, longitude and date. It might also be the case that multiple categories occur in an image (e.g. a photo of a bee on a flower). For this competition each image has one ground truth label <img src="svgs/681a37b53b66acbc455e39ca3e6f1c41.svg?invert_in_darkmode" align=middle width=12.444795pt height=14.10255pt/>, and the error for that image is:
<p align="center"><img src="svgs/7a42826f81c53c77e0fef3c827238d25.svg?invert_in_darkmode" align=middle width=123.403665pt height=24.865665pt/></p>
Where
<p align="center"><img src="svgs/7a45c501d5042bd031a267f008fa2ae6.svg?invert_in_darkmode" align=middle width=190.2021pt height=49.13139pt/></p>

The overall error score for an algorithm is the average error over all <img src="svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.94405pt height=22.38192pt/> test images:
<p align="center"><img src="svgs/444adcac0c7cbb4a8419ee1484625349.svg?invert_in_darkmode" align=middle width=118.05123pt height=41.069655pt/></p>

## Differences from iNaturalist 2017 Competition
The 2018 competition differs from the [2017 Competition](2017/README.md) in several ways:

### Species Only
The 2017 dataset categories contained mostly species, but also had a few additional taxonomic ranks (e.g. genus, subspecies, and variety). The 2018 categories are all species.

### Taxonomy Information & Obfuscation
The 2018 dataset contains kingdom, phylum, class, order, family, and genus taxonomic information for all species. However, we have obfuscated all taxonomic names to hinder participants from constructing web search terms to collect additional data.

### Data Overlap
The 2018 dataset contains some species and images that are found in the 2017 dataset. However, we will not provide a mapping between the two datasets.

## Guidelines

Participants are welcome to use the [iNaturalist 2017 Competition dataset](2017/README.md) as an additional data source. There is an overlap between the 2017 species and the 2018 species, however we do not provide a mapping between the two datasets. Besides using the 2017 dataset, participants are restricted from collecting additional natural world data for the 2018 competition. Pretrained models may be used to construct the algorithms (e.g. ImageNet pretrained models, or iNaturalist 2017 pretrained models). Please specify any and all external data used for training when uploading results.

The general rule is that participants should only use the provided training and validation images to train a model to classify the test images. We do not want participants crawling the web in search of additional data for the target categories. Participants should be in the mindset that this is the only data available for these categories.

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
  "supercategory" : str,
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
12345,0 78 23
67890,83 13 42
```
The `id` column corresponds to the test image id. The `predicted` column corresponds to 3 category ids, separated by spaces. You should have one row for each test image. Please sort your predictions from most confident to least, this will allow us to study top-1, top-2, and top-3 accuracy.

## Terms of Use

By downloading this dataset you agree to the following terms:

1. You will abide by the [iNaturalist Terms of Service](https://www.inaturalist.org/pages/terms)
2. You will use the data only for non-commercial research and educational purposes.
3. You will NOT distribute the above images.
4. The California Institute of Technology makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
5. You accept full responsibility for your use of the data and shall defend and indemnify the California Institute of Technology, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.

## Data

Download the dataset files here:
  * All training and validation images [120GB]
      * Links for different parts of the world:
          * [North America]()
          * [Asia]()
          * [Europe]()
      * Posterity [Caltech link](). Warning this will be slow.
      * Running `md5sum train_val2018.tar.gz` should produce `b1c6952ce38f31868cc50ea72d066cc3`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `train_val2018/super category/category/image.jpg`. This may take a while.
  * Training annotations [26MB]
      * Links for different parts of the world:
          * [North America]()
          * [Asia]()
          * [Europe]()
      * Posterity [Caltech link]()
      * Running `md5sum train2018.json.tar.gz` should produce `blah`
  * Validation annotations [26MB]
      * Links for different parts of the world:
          * [North America]()
          * [Asia]()
          * [Europe]()
      * Posterity [Caltech link]()
      * Running `md5sum val2018.json.tar.gz` should produce `blah`
  * Test images [40GB]
      * Links for different parts of the world:
          * [North America]()
          * [Asia]()
          * [Europe]()
      * Posterity [Caltech link](). Warning this will be slow.
      * Running `md5sum test2018.tar.gz` should produce `4b71d44d73e27475eefea68886c7d1b1`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `test2018/image.jpg`.
  * Test image info [6.3MB]
      * Links for different parts of the world:
          * [North America]()
          * [Asia]()
          * [Europe]()
      * Posterity [Caltech link]()
      * Running `md5sum test2018.json.tar.gz` should produce `blah`
