# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 451. [Representing and Detecting Label Ambiguity in IMU-Based Exercise Evaluation](https://arxiv.org/abs/2607.04842)

**<font color=#1a73e8>作者：</font>** Andreas Spilz, Heiko Oppel, Michael Munz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Home-based physiotherapy is performed without supervision, which leads to incorrect execution and motivates systems that assess movement automatically from inertial measurement units (IMUs). Such systems assign each repetition to a category, yet a relevant share of repetitions falls near a class boundary, where even trained raters disagree. Classifiers trained with one-hot labels collapse these borderline repetitions onto a single class and discard this ambiguity. We address this with a method that automatically generates a label distribution per repetition without a large rater pool. We train a network to reproduce the full distribution with a Kullback-Leibler objective, the ambiguity approach, and compare it against a one-hot cross-entropy baseline on four IMU exercise datasets. From the network output we further determine whether a repetition is ambiguous and which classes are relevant to it. The ambiguity approach matched or exceeded the baseline classification on all four datasets, and detected ambiguity and the relevant classes more reliably. Representing the label distribution in the training target therefore adds information about ambiguity at no cost to classification.

---


### 452. [Framework for Grouping Local Process Models](https://arxiv.org/abs/2607.04856)

**<font color=#1a73e8>作者：</font>** Viki Peeva, Wil M. P. van der Aalst  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local Process Models (LPMs) are an underexplored concept in process mining. LPMs describe patterns in event data considering sequence, choice, concurrency, and loop. In recent years, process mining has proved successful in the analysis and improvement of operational processes. More often than not, surprising findings are found when one does not consider the full process, making LPMs and their discovery highly valuable. However, similar to other pattern mining approaches, LPM discovery algorithms face the problems of model explosion and model repetition, i.e., the algorithms may create hundreds if not thousands of LPMs, and subsets of them are close in structure or behavior. Practically, no analyst would be able to comb through thousands of LPMs leading to using a sample of LPMs that are easily accessible. The current sentiment is that the top-scoring LPMs form the optimal sample to be presented. However, different applications should demand a different optimal sample. With this work, we show that if the goal of the mined LPMs is to understand a process, using the top-scoring LPMs as an optimal sample is a poor choice because of high repetition. We propose a framework for grouping LPMs and creating an optimal sample by taking one representative LPM for each group. We measure similarity between models via established process model similarity measures or by comparing the context in which an LPM appears. The context is formed using data attributes available in the underlying event logs. We demonstrate the usefulness of grouping on multiple event logs by comparing repetition and coverage between samples comprised of the top-scoring models and the representatives of discovered groups.

---


### 453. [PAGE: Towards Practical Human-level Gaze Target Estimation](https://arxiv.org/abs/2607.04860)

**<font color=#1a73e8>作者：</font>** Zhoutong Ye, Chengwen Zhang, Zhaibin Cui 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaze target estimation, the task of predicting where a person is looking in a scene, is crucial to understanding human attention and intent. It is a challenging task that combines high-level understanding of global scene semantics and precise spatial reasoning using human appearance (e.g. pose, eye orientation). As a result, human-level performance remains elusive for existing models, limiting their practical application. To this end, we propose PaGE (Practical Gaze Estimator), a gaze estimation model that explicitly models the complex interaction between scene and head features. Using a PaGE model with a large ViT-H+ backbone as the teacher, we further distill student models with lighter backbones on a much larger and more diverse unlabeled dataset. The architectural improvements and novel training recipe allow PaGE to achieve state-of-the-art performance on several gaze estimation tasks, outperforming humans in 7 out of 9 metrics while reducing the human-AI gap by at least 60% in the remaining 2. The distilled student models retain most of the teacher's performance while being lightweight enough for practical deployment on robots and consumer devices. The code and model checkpoints are available at our project page.

---


### 454. [Enhancing the Forecasting Capability of Multi-Model Blending Algorithms for Extreme Precipitation via Joint Use of Station and Gridded Observations](https://arxiv.org/abs/2607.04862)

**<font color=#1a73e8>作者：</font>** Yu Wang, Yong Cao, Kan Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate extreme precipitation forecasting is critical for disaster mitigation but remains challenging for numerical weather prediction (NWP) models due to systemic intensity underestimation and spatial displacement. Traditional precipitation multi-model blending algorithms perform pixel-by-pixel blending on the forecast field based on weights, which may lead to the expansion of precipitation areas and the smoothing of extreme values. This study proposes an U-Net based two-stage framework: probability classification followed by value reconstruction, to blend forecasts from six major NWP models. A novel station-grid joint supervision mechanism is introduced by integrating observations from 2411 national meteorological stations in China into the loss function, simultaneously constraining spatial structures and peak intensities. Evaluations using independent samples from the 2025 flood season demonstrate that our model significantly outperforms both individual NWPs and current operational products. For rainstorms (>=50 mm), the Threat Score (TS) improved by 38.4% compared to the best NWP. Notably, for extreme events (>=100 mm) driven by extratropical cyclones and the subtropical high, the model successfully elevated the TS to above 0.1, transforming forecasts from having negligible reference value into those with certain operational utility. Furthermore, the model exhibits data-driven spatial correction capabilities, effectively realigning systematic rainbelt displacements with actual precipitation centers. The inclusion of station observations specifically enhanced the TS for rainstorms by 10.4% and effectively balanced the Bias. These results highlight the efficacy of multi-source joint supervision in enhancing the capture of extreme precipitation events.

---


### 455. [Active Learning on Adversarially Corrupted Graphs](https://arxiv.org/abs/2607.04869)

**<font color=#1a73e8>作者：</font>** Marco Bressan, Nicolò Cesa-Bianchi, Tommaso d`Orsi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by real-world scenarios where malicious entities tamper with existing networks, we define a model where an adversary seeks to hide a set of \emph{corrupted vertices} inside a graph $G^*$. To this end, the adversary can add edges between the corrupted vertices, as well as edges between the corrupted vertices and $G^*$, and its power is then measured by the size of the \emph{neighborhood} of the corrupted vertices in $G^*$. Our goal is to design an active learning algorithm that efficiently finds the subset of corrupted vertices using a small number of label queries. We devise an efficient algorithm that approximately recovers the corrupted vertices with a query complexity that depends polynomially on both the power of the adversary and the \emph{vertex expansion} of $G^*$, a fundamental measure of graph connectivity. At the heart of this result is a polynomial-time algorithm, obtained by carefully adapting sum-of-squares algorithms for approximating minimum expansion, that finds a set with small vertex expansion subject to cardinality constraints. To the best of our knowledge, this is the first time that the vertex expansion is shown to play a key role in determining the query complexity of active learning algorithms robust to structural adversarial attacks.

---


### 456. [EventCoT: Event-centric Video Chain-of-thought for Reasoning Temporal Localization](https://arxiv.org/abs/2607.04872)

**<font color=#1a73e8>作者：</font>** Youngkil Song, Yoonjae Baek, Dongwon Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning temporal localization (RTL) requires a model to generate an answer that itself contains the time interval supporting it, so high-level reasoning and precise temporal grounding must be produced jointly in a single response. To tackle this challenging task, we propose the first event-centric video chain-of-thought framework, dubbed EventCoT. EventCoT first performs event-centric tokenization of the input video to convert it into compact event tokens, enabling efficient identification of question-relevant events. It then reasons within the identified events to generate the answer, grounding the time interval via embedding matching that aligns placeholder tokens with visual embeddings. EventCoT achieves state-of-the-art results on ActivityNet-RTL for reasoning temporal localization while using substantially fewer visual tokens than previous work. To verify its general performance, we further evaluate EventCoT on the grounded video question answering benchmark ReXTime, where it attains strong zero-shot results.

---


### 457. [Unsupervised Detection of Underground Tunnels in Ground-Penetrating Radar Using Depth-Restricted Reconstruction Scoring](https://arxiv.org/abs/2607.04882)

**<font color=#1a73e8>作者：</font>** Muhammad Junaid, Shoab A. Khan, Nisar Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clandestine tunneling beneath oil and gas pipelines enables fuel theft, smuggling, and sabotage, yet conventional monitoring detects damage only after a pipeline has been compromised. Ground-penetrating radar (GPR) can image such tunnels non-invasively, but manual radargram interpretation does not scale to continuous corridor surveillance, and supervised detectors require tunnel examples that are scarce in practice. We present a fully unsupervised detection pipeline trained exclusively on normal subsurface radargrams collected at a purpose-built field site containing three buried tunnels at 1.5-3 m depth. A denoising convolutional autoencoder learns the structure of anomaly-free ground; at inference, tunnels are flagged by reconstruction error. Our central contribution is a depth-restricted top-k anomaly score, which pools the highest reconstruction errors only within the depth band where tunnels can physically occur. This physically motivated rule raises AUC from 0.986 to 0.994 and cuts missed detections from 74 to 17 of 634 tunnel windows, relative to whole-image scoring, without any retraining or labels. We further show that the optimal top-k fraction interacts with the depth restriction - 1% pooling is best on full images, 5% once scoring is depth-restricted - and that spatial voting across overlapping survey windows helps weak per-image detectors but offers no benefit once the scoring rule is strong. The final system attains AUC 0.994, F1 0.975, recall 0.973, and precision 0.976 on 1,600 field test windows spanning 55 survey lines, at a 1.6% false-alarm rate, using no tunnel labels for training, scoring, or threshold calibration.

---


### 458. [ProCon: Projection-Consistency Memory for Training-Free Anomaly Detection](https://arxiv.org/abs/2607.04894)

**<font color=#1a73e8>作者：</font>** Joongwon Chae, Lihui Luo, Yang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memory-based anomaly detection is attractive because it localizes defects from normal images without training a decoder or synthesizing pseudo anomalies. However, most memory methods still use the memory bank as a nearest-neighbor lookup table: a test patch is treated as normal if it has one nearby normal anchor. This hard retrieval view is vulnerable to false-normal matches and does not test whether the patch is consistently supported by a local normal neighborhood. We propose ProCon, a training-free framework that turns memory retrieval into decoder-free reconstruction. ProCon softly projects each test patch onto nearby normal memory vectors and uses the projection residual as anomaly evidence. To stabilize this residual, it constructs seed-perturbed layer-wise memories, aggregates bank residuals by a median, and fuses depth-specific residual maps by layer consensus. ProCon requires no decoder training, backbone fine-tuning, learned fusion weights, or pseudo-anomaly supervision. Across MVTec-AD, VisA, and Real-IAD under the single-category evaluation protocol, ProCon achieves strong image- and pixel-level performance under seven standard metrics, including image AUROC scores of 99.8%, 99.2%, and 93.2%, respectively. Ablations show that the gains come from replacing hard retrieval with soft normal projection and stabilizing the residuals through memory and depth consensus. The code is available at this https URL

---


### 459. [Ossetic-COT: Designing a morphologically annotated corpus and morphological analyzer for Ossetic](https://arxiv.org/abs/2607.04895)

**<font color=#1a73e8>作者：</font>** Anna Shatskikh, Alexey Sorokin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this work we present the first morphologically annotated corpus for Iron Ossetic that conforms to the Universal Dependencies schema. The corpus includes 5454 manually annotated sentences from the Iron Ossetic Corpus of Oral Texts, containing 74032 tokens. We use this corpus to train a BERT-based morphological analyzer. The analyzer achieves tag accuracy of 95.60%.

---


### 460. [3DMPE: 3D Multi-Perspective Embedding](https://arxiv.org/abs/2607.04898)

**<font color=#1a73e8>作者：</font>** Vahan Huroyan, Md Rahat-uz-Zaman, Stephen Kobourov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study 3D point cloud reconstruction from multiple partially observed 2D projections. Given two or more projections of an unknown 3D point cloud, together with cross-view point correspondences and visibility information, our goal is to recover a consistent 3D configuration when different views contain different subsets of points. We propose 3D Multi-Perspective Embedding (3DMPE), an optimization-based, training-free method that reconstructs the 3D point cloud and, in the variable-projection setting, jointly estimates the projection maps. 3DMPE extends Multi-Perspective Simultaneous Embedding to accommodate missing points and incomplete pairwise distance information across views. We consider both fixed-projection and variable-projection settings. Unlike learning-based reconstruction methods that infer shape from raw images and often depend on training data, 3DMPE operates on geometric observations with established correspondences and does not require category-specific training. Experiments on ShapeNet and Pix3D evaluate reconstruction quality using Chamfer Distance, Earth Mover Distance, and RMSE-Optimize-Align (ROA), and examine the effects of initialization, the number of views, point visibility, and several noise regimes, including noisy distances and erroneous correspondences. The results demonstrate that 3DMPE can effectively reconstruct point clouds from partial multi-view geometric observations.

---


### 461. [RL-Ballast: Ship Ballast Water Path Planning and Clog Prediction via Reinforcement Learning](https://arxiv.org/abs/2607.04906)

**<font color=#1a73e8>作者：</font>** Ming-Kuan Lin, Yi-Chung Lai, Ming-Hsin Chiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Under the Shipping 4.0 paradigm, autonomous and reduced-crew vessels require intelligent internal systems to maintain operational safety and structural stability. Ballast-water control is essential for ship trim and integrity, but conventional rule-based or manual approaches have limited adaptability to hydraulic anomalies such as valve failures and pipe blockages, and often depend on dense pressure or flow sensors for diagnosis. To address these limitations, this paper proposes RL-Ballast, a graph-based deep reinforcement learning framework for adaptive ballast-water path planning and sensor-frugal blockage candidate scoring. The valve-permutation problem is transformed into 54 feasible fluid-transfer routes generated using graph theory and depth-first search. The partially observable ballast environment is approximated with frame-stacked tank levels and action outcomes, allowing the agent to infer hidden blockage effects without explicitly modeling a high-dimensional POMDP. During deterministic inference, episode-level failed-action memory and dynamic action masking prevent repeated ineffective actions and support immediate rerouting. Failed transfer histories are further accumulated to rank suspicious valves or pipe segments without dense instrumentation. Monte Carlo simulations show that RL-Ballast completes all unexpected single-blockage scenarios and reduces average decision steps from 61.0 to 41.5 compared with a Dijkstra rule-based baseline. For diagnostic support, the failure-history scoring scheme achieves a 100% Top-3 hit rate, a 66.7% strict Top-1 hit rate, and an 83.3% Top-1 tie-hit rate under serially indistinguishable blockage conditions. These results suggest that RL-Ballast enables adaptive rerouting and maintenance-oriented blockage diagnosis under limited sensing conditions.

---


### 462. [Graph Representation Learning of Longitudinal Medical Imaging Trajectories for Treatment Response Prediction](https://arxiv.org/abs/2607.04912)

**<font color=#1a73e8>作者：</font>** Johannes Kiechle, Richard Osuala, Daniel M. Lang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In patients with breast cancer, pathological complete response (pCR) has been established as a clinically meaningful surrogate marker for long-term outcomes. While commonly treated with neoadjuvant chemotherapy (NACT), effective treatment decision-making remains challenging, as therapeutic response can vary substantially across patients, calling for predictive models capable of accurately estimating individualized treatment response. To address this, we propose an imaging-based 3D spatio-temporal framework for treatment response prediction that integrates a state-of-the-art graph neural network with relational modeling of temporal interactions across timepoints alongside three novel complementary self-supervised treatment trajectory representation learning objectives. Experiments across a cohort of 585 patients from the public ISPY-2 dataset demonstrate that our method substantially outperforms both vision and self-supervised learning baselines across several classification metrics. Alongside establishing a breast cancer pCR prediction benchmark, we include a principled ablation of our method and further introduce and empirically assess the impact of the available number of DCE-MRI timepoints per patient trajectory and the inclusion of inter-scan time-differences. Overall, our study substantiates the utility of clinically meaningful longitudinal medical imagaging modeling for predicting NACT-induced pCR. We will publicly share our code repository and a user-friendly PyPI library for dataset curation upon publication, effectively promoting reproducible open-source research.

---


### 463. [Efficient Perception in Automotive Detection and Tracking Using Neuromorphic Computing](https://arxiv.org/abs/2607.04921)

**<font color=#1a73e8>作者：</font>** Manish Kolachalam, Rani Malhotra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning algorithms are notorious for their high carbon footprint and computational demands that limit their deployment on edge devices and raise concerns about their long-term sustainability. Neuromorphic computing and Spiking Neural Networks (SNNs) offer a promising alternative to traditional Von Neumann architectures, providing energy-efficient performance, massively parallel computation, and on-chip learning capabilities. Autonomous machines represent a critical application domain where these advantages are particularly valuable. We present the first comprehensive evaluation of SNNs for real-world automotive multi-object detection and tracking. Using transfer learning with the SpikeYOLO architecture, we achieve mean Average Precision of 0.937 on the KITTI dataset and 0.771 on BDD100K MOT2020 dataset for object detection and a Higher Order Tracking Accuracy score of 0.701 (KITTI) and 0.445 (BDD100K MOT2020) for object tracking--results competitive with conventional deep learning methods. Our results demonstrate that SNNs can deliver high-performance object detection and tracking in an energy efficient manner, establishing their viability for perception in real-world autonomous systems.

---


### 464. [UniSpine-GS: An Efficient Physics-Aware Gaussian Framework for Cross-Modality Multi-view Spine Image Synthesis](https://arxiv.org/abs/2607.04923)

**<font color=#1a73e8>作者：</font>** Qiuhua Chen, Changning Yu, Na Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The diagnosis of spinal diseases is often assisted by 3D imaging techniques in clinical practice. However, precise 3D spinal assessment is limited by the high costs of 3D imaging hardware and the challenges posed by the physical differences between imaging modalities, which hinder the generalizability of models. To address these issues, we propose UniSpine-GS, an efficient, physics-aware Gaussian framework designed for novel-view projection rendering in multi-view spine imaging via a 3D-aware representation. Instead of performing explicit 3D reconstruction, our approach learns a geometry-aware Gaussian representation that ensures anatomical consistency across different views. We introduce SPWM, a structure-guided loss reweighting strategy to improve boundary fidelity and local details. We evaluate our method on the CTSpine3D dataset and a newly constructed 3D fetal ultrasound dataset, FeSpine3D. Our results demonstrate that UniSpine-GS significantly outperforms existing methods across all metrics, offering a practical and cost-effective solution for unified multi-view medical imaging. Our code is publicly available at this https URL.

---


### 465. [Input Pathways Shape Few-Shot, Not Zero-Shot, Binding in Tiny Transformers: A Fully-Enumerable Study](https://arxiv.org/abs/2607.04926)

**<font color=#1a73e8>作者：</font>** Yoshiyuki Ootani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How does the way information reaches a transformer -- as symbolic tokens, a clean per-factor "oracle" code, or an entangled perceptual vector -- shape whether it binds that information compositionally? We study ~6-10K-parameter transformers on finite factored worlds enumerated exhaustively, so every measurement covers the whole input space (zero sampling variance) and the informative routes are information-matched (exact Bayes ceiling 1.0). We report four findings. (1) Endpoint invariance: on held-out binding queries no informative route reaches converged zero-shot composition -- each ends at or below chance despite a ceiling of 1.0, so within a bounded sweep the failure reflects inductive bias under a lookup-sufficient objective, not missing information. (2) A two-factor account of few-shot binding: sample efficiency is best explained by input-pathway parameter sharing and code readability; a dimension-matched control and a graded readability sweep isolate readability from input dimension, and the clean oracle is not the most sample-efficient readable route. (3) A double dissociation: early in training, distributed -- but not index-like -- codes pass through a transient above-chance phase (tracking code format), while few-shot efficiency tracks pathway sharing. (4) Failure anatomy: symbolic routes lose the answer at the readout; index routes mis-bind (the answer stays decodable, yet an input intervention shows the output tracks the wrong slot); entangled routes inherit their input's readability. The central claim is the two-factor account; the endpoint and anatomy results are diagnostic constraints. All code, manifests, and per-seed logs are released for exact reproduction.

---


### 466. [MemPose: Category-level Object Pose Estimation with Memory](https://arxiv.org/abs/2607.04930)

**<font color=#1a73e8>作者：</font>** Xiao Lin, Minghao Zhu, Yun Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the pursuit of robust and generalizable category-level object pose estimation, most existing methods adopt parametric formulations that learn effective representations from data, yet they primarily encode category-level patterns into fixed shape priors or static parameter weights, which limits their scalability to highly diverse instances. In this paper, we rethink category-level pose estimation from a memory-centric perspective and present MemPose, a memory-augmented framework that explicitly incorporates category-level geometric memory into the pose estimation pipeline. We introduce an external memory buffer that stores and dynamically updates structural representations from previously observed instances, enabling the model to leverage accumulated experience to support current perception. Extensive experiments on four challenging benchmarks (REAL275, CAMERA25, Housecat6D and Wild6D) demonstrate the superiority of our proposed method over previous state-of-the-art approaches.

---


### 467. [Lightweight ML-Based Automatic Sleep Staging Framework with Constrained CNN and Mamba for Small-Sample EEG Datasets](https://arxiv.org/abs/2607.04934)

**<font color=#1a73e8>作者：</font>** Zihao Wei, Yulin Gong, Yudan Lv  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic sleep staging is a key technology for precise diagnosis and treatment of sleep disorders as well as long-term home sleep monitoring. Portable electroencephalogram (EEG) devices have become the focus of research due to their convenience in data collection. However, current methods still face three major challenges: large parameter sizes that easily lead to overfitting on small datasets, low accuracy in classifying difficult stages such as N1 and REM, unclear optimal training dataset size, and difficulty in deployment. This paper proposes GamSleepNet, a lightweight and low-latency automatic sleep staging framework for single-channel EEG. The framework features the FEB module, which combines improved Gabor kernels with learnable filters for feature extraction, uses the Mamba architecture to build a temporal classification network, introduces a novel contrastive loss and a two-stage training strategy, and experimentally validates the optimal dataset size for single-channel EEG sleep staging models. On the Sleepedf dataset, this model achieves an overall accuracy of 87.86 percent with only 30.86 thousand parameters, with all metrics reaching SOTA levels and significantly improving the identification accuracy of challenging sleep stages.

---


### 468. [Sensitivity Sampling with Predictions for k-Means Clustering](https://arxiv.org/abs/2607.04949)

**<font color=#1a73e8>作者：</font>** Cristian Boldrin, Fabio Vandin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of k-means clustering on large datasets. The state-of-the-art for the problem is given by coresets-based approaches, which build small weighted summaries of the input and derive approximate solutions with rigorous quality guarantees from them. One of the most popular and advanced approaches to derive coresets for k-means is sensitivity sampling. However, sensitivity sampling requires to compute the importance of each input point with respect to the whole dataset over all possible choices of centers. Since the exact computation of such quantities is unfeasible, current approaches work by approximating the sensitivity values. Nevertheless, the runtime of such approaches is still impractical for large datasets.
In this work, we propose to reduce the runtime of sensitivity-based approaches for k-means by leveraging predictions to approximate the importance of input points. We first formally prove that current theoretical results on coresets construction via sensitivity sampling hold for coarser approximations of sensitivities compared to the one required by existing approaches. This implies that even fairly noisy predictors can be leveraged for sensitivity-sampling approaches. We then propose a natural predictor, which applies to the common scenario where clustering is performed (over time) on a sequence of datasets from the same problem. We prove that when the datasets in the sequence come from the same (unknown) distribution, centers resulting in a low error on one dataset can be used as predictions for sensitivity sampling in subsequent datasets, with guarantees on their quality. We perform an extensive experimental evaluation showing that our approach significantly improves, in terms of clustering cost vs runtime, over uniform sampling and state-of-the-art sensitivity sampling approaches when applied to sequences of datasets.

---


### 469. [Who's Behind It? Annotating and Extracting Conspiratorial Actors from German Telegram Posts](https://arxiv.org/abs/2607.04962)

**<font color=#1a73e8>作者：</font>** Helena Mihaljević, Jolanda Beer, Mareike Lisker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conspiracy theories commonly attribute important events to the actions of powerful and secretive actors. While computational research has largely focused on document-level analyses of conspiracy theories, less attention has been paid to identifying the actors that drive such narratives. We develop annotation guidelines for conspiratorial actors, present a span-annotated corpus of German Telegram posts, and investigate their automatic extraction using transformer-based models. We further apply the resulting model to the \textit{Schwurbelarchiv}, a large-scale archive of German conspiracy-related Telegram channels. Our results demonstrate that conspiratorial actors can be annotated with meaningful agreement and extracted with reasonable accuracy despite the linguistic complexity of conspiracy discourse, enabling large-scale analyses of actor representations in conspiracy narratives.

---


### 470. [Measuring Healthcare Data Leaks and Security Flaws at Internet Scale](https://arxiv.org/abs/2607.04965)

**<font color=#1a73e8>作者：</font>** Nico Brüggemann, Lukas Schmidt, Marvin Dölzer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Systems that process medical data should be meticulously secured. Yet, network services in healthcare environments often fail to implement basic security measures. For example, previous studies showed that network segmentation flaws led to DICOM systems leaking millions of patient records.
In addition to DICOM, healthcare facilities rely heavily on the HL7 and FHIR protocols to transmit data. For nine months, we operated a low-interaction honeypot for medical protocols. We found it was regularly scanned for DICOM but never for HL7 or FHIR, indicating that despite their widespread use and importance for patient data security, the security of these services remains underexplored.
In this paper, we present the first large-scale study on HL7 and FHIR services and expand previous work on DICOM. Our large-scale Internet scans, covering the three major healthcare protocols across IPv4 and IPv6 address spaces, identify healthcare systems and uncover data leaks due to authentication flaws. Additionally, we scanned for deficiencies in TLS configurations of these services and known insecure healthcare software.
In total, we found \TotalEndpointsAuthFlaws ~healthcare services with authentication flaws. \NonTLSPercentage{}\% of all exposed systems do not support transport encryption, and \AllServerCVE{} systems have known software vulnerabilities, including those with potential for system takeover and CVSS scores up to 9.8. Overall, our study reveals an alarming state of cybersecurity in healthcare deployments, for which we discuss potential reasons and countermeasures. Finally, we report on the coordinated disclosure campaign we initiated to improve the security of patient data.

---


### 471. [Geometry-Aware Bayesian Quantification via Compositional Data Analysis](https://arxiv.org/abs/2607.04977)

**<font color=#1a73e8>作者：</font>** Alejandro Moreo, Pablo González, Juan José del Coz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately estimating the unknown target label distribution is the critical first step for adapting to label shift. This task, widely known as quantification or class prevalence estimation, has recently seen significant advances through continuous KDE-based methods which model the density of multiclass classifier posteriors. Posterior vectors might be regarded as compositional data, since they lie on the probability simplex. However, existing KDE-based quantifiers typically rely on Euclidean Gaussian kernels, which ignore simplex geometry and incorrectly assign probability mass outside its boundaries. We introduce a geometry-aware KDE model for multiclass quantification based on log-ratio representations and Aitchison geometry, together with a shrinkage regularization that improves robustness near the simplex boundary. Combined with a maximum-likelihood interpretation of KDE-based quantification, we derive both point-estimation and Bayesian inference procedures for class prevalences. Experiments on 42 datasets across tabular, text, and image domains show that the proposed method is competitive with state-of-the-art quantifiers, often improving over standard KDE-based baselines, while also yielding strong results among Bayesian quantification methods.

---


### 472. [Qantara: Bridge-Flow Training for Multi-Paradigm JEPA Control](https://arxiv.org/abs/2607.04978)

**<font color=#1a73e8>作者：</font>** Ruslan Rakhimov, George Bredis, Yuriy Maksyuta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) underpin a growing family of latent world models for control from raw pixels, but every existing JEPA world model commits at training time to a single inference paradigm: either trajectory optimisation in a learned dynamics model, or direct behaviour cloning. A single checkpoint that serves both would defer this choice to inference, when deployment constraints (rollout cost, observation accessibility) determine which path wins. We present Qantara, an end-to-end JEPA whose joint training objective pairs a Brownian-bridge interpolant between consecutive clean latents on the state axis with noise-to-data flow matching on the action axis. The same checkpoint serves three inference paradigms without retraining: latent planning, behaviour-cloning action sampling, and inverse dynamics, which we query through a video-inverse composition that first predicts the next latent without action conditioning, then extracts the action. Training concentrates mass on the edges of the (action-time, state-time) noise square, where inference queries the predictor: replacing it with uniform interior sampling drops Push-T planning from 90.1 to 53.3 SR at matched compute. On the LeWM control suite, Qantara reaches a 91.2 SR three-train-seed average and sets new SOTA on OGBench-Cube (+7.7 SR over DINO-WM, +19.7 over LeWM). From the same weights, the behaviour-cloning and video-inverse paths reach 82-83 SR on Push-T and 71-73 SR on Cube. These results move JEPA world models from single-paradigm planners to multi-paradigm controllers.

---


### 473. [Virtual Category-Guided Continual Generalized Category Discovery](https://arxiv.org/abs/2607.04984)

**<font color=#1a73e8>作者：</font>** Jiahui Xiong, Qiuxia Lai, Hongsong Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual Generalized Category Discovery (C-GCD) aims to incrementally identify novel categories from sequential unlabeled data while preserving recognition of known classes, which is an essential capability for open-world visual learning. A major bottleneck lies in ambiguous unlabeled samples that cannot be confidently assigned to known classes nor reliably grouped as novel ones, making pseudo-labeling brittle and often biasing learning toward familiar categories. In this work, we introduce Virtual Category-Guided Continual Generalized Category Discovery by adapting Virtual Category Learning (VCL) to the continual setting. Our method identifies uncertain samples and assigns them to temporary virtual categories, enabling safe and informative learning from unlabeled streams without injecting noisy labels, while improving unlabeled data utilization and mitigating prediction bias. To further stabilize discovery across sessions and enhance class separation, we augment VCL with Expanded Neighborhood Contrastive Learning (ENCL), which exploits extended neighborhood relations and an adaptive margin to learn more discriminative and well-separated representations for both old and emerging classes. Extensive experiments on CIFAR-100, Tiny ImageNet, and ImageNet-100 demonstrate that our approach consistently outperforms state-of-the-art methods, establishing a scalable and effective solution for C-GCD.

---


### 474. [The syntax of wh-agreement in Yemeni Ibbi Arabic](https://arxiv.org/abs/2607.04986)

**<font color=#1a73e8>作者：</font>** Ashraf Naji, Mohammed Q. Shormani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This article tackles an important phenomenon in the syntax of Yemeni Ibbi Arabic (YIA), viz., wh-agreement, a phenomenon common to several languages including Greek, Indonesian, Lubukusu, Irish, etc. In YIA, wh-agreement manifests itself via agreement inflections on the Wh-Op, C, T/V, v. To account for this phenomenon, we propose an Agree across phases (AAP) approach anchored in the mechanism of Feature Inheritance (FI) in which Agree as MATCHING (AM) is a bit separated from feature valuation (FV). AM concerns Cs/vs, but FV Ts/Vs. Analyzing the agreement patterns observed between Wh-Op(erators), functional heads (precisely C, (T), v), and verbal complexes, we argue that the suffixes -eh, -uh, -nen, -um, having undergone grammaticalization process from Stannard Arabic (SA) third person pronouns, function as morphological marking of wh-agreement. Findings indicate that YIA data offer a unique empirical contribution to generative syntax, specifically concerning wh-agreement in this dialect operating via MATCHING mechanism. Our proposal straightforwardly accounts for wh-agreement cross-linguistically. This study provides further evidence that incorporating under-investigated typology provides further support for the universality of Universal Grammar (UG) by revealing how specific I-language operations reflect deeper, invariant principles of human language architecture. It concludes that the wh-agreement mechanism in YIA is more morphosyntactically robust than in languages such as Greek, Indonesian, Palauan, and Irish, providing compelling evidence for AAP as a UG approach to long-distance dependencies.

---


### 475. [Data-Driven Soft Labeling Scales DNA Read Classification to Whole-Body Cell-Type Deconvolution](https://arxiv.org/abs/2607.04987)

**<font color=#1a73e8>作者：</font>** Dmytro Rizdvanetskyi, Nathan Ross, Pavlo Lutsik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cell-type deconvolution, the task of estimating the proportions of constituent cell types in a heterogeneous biological sample, is a core problem in computational biology. Methods that rely on epigenetic marks such as DNA methylation typically operate on aggregated methylation estimates, discarding the pattern-level information carried by individual DNA reads. Existing read-level approaches that exploit this information are scarce, and all remain restricted to few-class settings; scaling them further is an open problem because, at scale, non-discriminative reads dominate and hard labels conflict with the many-to-many mapping between methylation patterns and cell types, preventing classifier convergence. To overcome this, we propose data-driven soft labels that estimate the conditional cell-type distribution for each read, and integrate this scheme into Syto, a new modular framework for read-level classification-based deconvolution. On a whole-body atlas of 39 human cell types, Syto reduces MSE by 2.56$\times$ over SoTA, with gains transferring to an out-of-distribution dataset spanning 16 tissues. Syto lays the foundation for modeling increasingly large cell-type panels, with improved applications in biology and healthcare. The proposed soft-labeling scheme is further translatable to any setting with a many-to-many signal-to-label mapping.

---


### 476. [Non-Convex Sparse Reinforcement Learning via Non-Monotone Inclusions](https://arxiv.org/abs/2607.04990)

**<font color=#1a73e8>作者：</font>** Kyohei Suzuki, onstantinos Slavakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work delivers two key contributions: one to efficient feature selection in reinforcement learning
(RL), the other to the theory of non-monotone inclusions. On the RL side, the estimation bias inherent
in conventional regularization schemes is addressed by augmenting classical least-squares
temporal-difference (LSTD) policy evaluation with the sparsity-inducing, non-convex projected minimax
concave (PMC) penalty. Because the PMC penalty is weakly convex, the resulting fixed-point problem is
no longer monotone; instead, it falls under a broader class of non-monotone inclusions involving the
sum of a monotone Lipschitz operator and a hypomonotone operator. On the theory side, novel convergence
conditions are developed for the forward-reflected-backward splitting (FRBS) method applied to this
broader class of non-monotone inclusion problems. Under mild conditions, Lyapunov stability and the
existence of a limit point of the sequence of FRBS iterates are established; alternatively, under the
weak Minty variational inequality assumption, exact convergence is guaranteed. Numerical tests on
benchmark datasets show that the proposed FRBS iterates, applied to the non-convexly regularized LSTD
problem, substantially outperform state-of-the-art feature-selection methods, especially when many
noisy features are present.

---


### 477. [The Map Behind the Flow: Finite-Step Gradient Descent as a Dynamical System](https://arxiv.org/abs/2607.04993)

**<font color=#1a73e8>作者：</font>** Thomas Hofmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many phenomena of deep learning are dynamical: they concern not only which minima exist, but how gradient descent reaches, avoids, or selects among them. Edge-of-stability behavior, sharpness oscillations, catapult phases, balancing, and movement toward flatter representations are effects of the training map itself, and are poorly captured by the small-step gradient-flow limit.
This paper studies fixed-step gradient descent as a discrete dynamical system in a hierarchy of exactly solvable models retaining basic structures of deep learning: depth, factorization, width, data coupling, activation, and stochasticity. The starting point is the balanced scalar reduction of a deep linear chain, giving a quartic loss and a cubic gradient map whose post-edge behavior is explicit. Under the natural large-depth scaling, this dynamics converges to a universal Ricker-type map. The edge of stability is therefore not a breakdown of optimization, but the first bifurcation of the training map.
Embedding the scalar dynamics back into factored models turns these regimes into learning phenomena. Finite steps break conservation laws of gradient flow and contract factorization imbalance; residual oscillations move parameters toward flatter, more balanced representations. Wider linear networks produce a ladder of spectral edges, so the optimal learning rate can lie beyond the first edge. Data coupling, nonlinear activations, and stochastic targets preserve the same organizing principle: finite-step oscillations drive alignment, balancing, and representation selection. Thus the learning rate is not merely a numerical stability parameter. It is a structural parameter of the training dynamics, determining its attractors and shaping the representations gradient descent selects.

---


### 478. [Geometry-aware Depth-guided Representation Learning for Structure-preserving Low-light Image Enhancement](https://arxiv.org/abs/2607.05005)

**<font color=#1a73e8>作者：</font>** Fang Gao, Jiongkai Qin, Jiabao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light degradation reduces image visibility and weakens structural cues that are important for visual representation and scene understanding. Existing low-light image enhancement methods mainly focus on appearance restoration, while insufficiently exploiting scene geometry to preserve structural consistency. To address this limitation, this paper proposes a Depth-guided Multi-scale Attention Network (DMSA-Net) for geometry-aware low-light image enhancement. DMSA-Net introduces depth-related structural priors into low-light representation learning through reflectance-geometry interaction. A Retinex-based decomposition module is first used to obtain illumination-invariant reflectance representations, from which depth cues are inferred to characterize scene structure under degraded illumination. A multi-scale depth-guided fusion strategy is then embedded into a hierarchical encoder-decoder architecture, where depth-aware attention adaptively integrates geometric and appearance features. Experiments on several benchmark datasets show that DMSA-Net achieves effective low-light restoration while improving structural preservation. Moreover, we construct LOL-D, a depth-augmented low-light dataset, to facilitate research on geometry-aware low-light vision.

---


### 479. [Unsupervised Pixel-Level Semantic Left-Right Understanding of In-the-Wild Images](https://arxiv.org/abs/2607.05006)

**<font color=#1a73e8>作者：</font>** Weikang Wang, Tobias Weißberg, Florian Bernard  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While various works address reflective symmetry understanding in 3D data and images, pixel-level semantic left-right prediction of in-the-wild images remains challenging, due to certain difficulties including the lack of 3D information, occlusion, object pose variation, partiality, etc. In this work, we propose an unsupervised learning framework to tackle this challenge. Leveraging recent advances in vertex-wise semantic left-right understanding of 3D data, our unsupervised learning method jointly utilises 3D shape and image datasets to infer pixel-wise semantic left-right predictions in single-view images. In particular, we show that a medium-scale 3D shape dataset comprising mainly of human- and quadruped animal-like shapes, combined with diverse in-the-wild image data, are sufficient to achieve high-quality semantic left-right prediction in images, even for entirely unseen 3D object categories, such as cars or trains. Overall, our approach achieves superior performance in dense pixel-wise semantic left-right predictions on both rendered and in-the-wild image datasets when compared to existing state-of-the-art methods.

---


### 480. [Quantum-Inspired Harmonic Decision Models: A Computational Framework for Music Generation](https://arxiv.org/abs/2607.05007)

**<font color=#1a73e8>作者：</font>** Josef Pavlíček, Petra Pavlíčková, Martin Molhanec  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces a quantum-inspired computational framework for harmonic decision-making in music. The proposed approach formulates harmonization as an optimization problem within a structured combinatorial space, where multiple candidate chord sequences are evaluated under interacting musical constraints. The model combines an interference-based harmonization stage with a classical optimization procedure grounded in tonal harmony. The quantum-inspired component enables the parallel consideration of multiple harmonic alternatives, while the classical stage refines the resulting sequences to ensure structural coherence and stylistic plausibility.
The framework is evaluated on selected musical examples, including Autumn Leaves and It's a Long Way to Tipperary. Quantitative analysis shows that the optimization stage significantly reduces chord density, increases harmonic stability, and improves functional organization. At the same time, expert evaluation highlights the importance of stylistic context, demonstrating that increased harmonic complexity is not always perceived as more natural. The results suggest that harmonic generation can be interpreted as a structured decision-making process in a constrained search space. The proposed approach provides a computational model that integrates domain-specific knowledge with an interference-based search mechanism.
Although preliminary, this work indicates that quantum-inspired methods may offer a useful framework for modeling complex decision processes in creative domains such as music. The proposed framework contributes to ongoing research on quantum-inspired models of cognition and decision-making in complex biological and creative systems.

---


### 481. [Comparison of Loss Functions for Robust Deep Learning-based Echocardiography Segmentation when Learning with Partially Labelled Data from Multiple Domains](https://arxiv.org/abs/2607.05008)

**<font color=#1a73e8>作者：</font>** Iman Islam, Esther Puyol-Antón, Bram Ruijsink 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Echocardiography is the first imaging modality used for assessing cardiac function, and accurate segmentation of cardiac structures is essential for deriving biomarkers. However, the development of effective automated segmentation models for multiple cardiac structures is challenged by the difficulty of training on datasets from different sources that are often partially-labelled. This study aims to address this challenge by evaluating the performance of three loss functions - adaptive categorical cross entropy (aCCE) loss, marginal loss, and the adaptive binary cross entropy (aBCE) loss - in handling partially-labelled data. We conduct a comprehensive comparison of these loss functions across multiple scenarios and network architectures: intra-domain and inter-domain tasks, with both single and multiple partial-labels, and varying proportions of fully-labelled to partially-labelled data.
Our experiments reveal that all three loss functions exhibit strong performance in intra-domain segmentation tasks, effectively handling label variations within the same domain. For inter-domain tasks, where models are trained on datasets with a domain shift, the aBCE and marginal losses show superior performance when dealing with the case of one label being missing from some training examples. In scenarios involving more than one label being missing, marginal loss outperforms the other methods, demonstrating its robustness in such complex conditions. These results highlight the strengths of each loss function depending on the labelling scenario, emphasizing the importance of selecting the appropriate loss function to optimize model performance. This study represents the first investigation of techniques for handling partially-labelled data from multiple different domains in echocardiography segmentation and provides a comprehensive comparison of loss-based solutions.

---


### 482. [ImputeECG: Deep Learning Reconstruction of Complete 12-Lead Electrocardiograms from Incomplete Recordings for Cardiac Assessment](https://arxiv.org/abs/2607.05009)

**<font color=#1a73e8>作者：</font>** Xiaocheng Fang, Haoyu Wang, Jieyi Cai 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complete digital 12-lead electrocardiograms (ECGs) are essential for AI-enabled cardiovascular assessment, yet many clinical ECG records, particularly those digitized from ECG images, remain incomplete because of short display formats, incomplete waveform digitization, lead loss, or signal corruption. We developed ImputeECG, a mask-conditioned one-dimensional Transformer autoencoder that completes 12-lead, 10-s ECGs while retaining all observed samples. The model was trained on PTB-XL and evaluated on PTB-XL and CPSC2018 under simulated incomplete settings, with additional real-world validation in a 43,633-record Kailuan clinical cohort after ECG image digitization. Metrics were computed over originally missing regions, with analyses of morphology and downstream diagnostic utility. On PTB-XL, ImputeECG reduced missing-region MAE by 41.7-51.0% and MSE by 54.0-63.7% versus the strongest baseline, with lower errors in R-peak timing, RR interval, QRS duration, QT interval, and P-wave, QRS-complex, and T-wave reconstruction. On CPSC2018, ImputeECG reduced MAE by 49.7-51.9%, supporting external generalization. In downstream multi-label classification, ImputeECG restored performance to 92.28% AUROC and 33.88% AUPRC in the most incomplete PTB-XL setting, approaching complete-ECG performance. On CPSC2018, completed ECGs achieved 94.75-95.89% AUROC and 78.83-81.86% AUPRC across settings. In Kailuan, ECG completion improved zero-shot sex prediction AUROC from 82.6% to 85.8% and reduced age prediction MAE from 10.72 to 9.87 years after image-based ECG digitization. These findings support ECG completion as a practical strategy for converting incomplete ECG records into AI-ready 12-lead, 10-s digital signals and extending the usable scope of ECG archives for digital cardiac assessment.

---


### 483. [Algorithmically Presented Numbers and Canonical Representations in Cryptographic Protocols](https://arxiv.org/abs/2607.05016)

**<font color=#1a73e8>作者：</font>** Arslan Brömme  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper develops a representation-theoretic perspective on cryptographic protocols. The focus is not solely on the computability of the abstract value as an extensional property, but on the algorithmic structure of its presentation in a representation system: for operational use in protocols, algorithmic accessibility of the value does not suffice; its fixed presentation is also decisive. We distinguish three representation-theoretic notions -- algorithmically approximable (A_app, the computable real numbers), finitely exactly describable in a system (A_fin(S)), and canonical normalizability of a system -- and show that there is no computable extensional canonicalizer that uniformly transforms arbitrary approximation programs of computable real numbers into unique finite value encodings. As the operational rational core presentation we use the rational system with its canonical encoding specification Sigma_Q (fixed rules for valid fraction descriptions, canonical codes, and normalization); the associated value set is A_ex = Q. The notion of a canonically serializable object class transfers this core idea to practical protocol objects (files as byte sequences, hash values, transaction IDs, and normatively serialized payloads). We illustrate the consequences for interoperability, well-definedness, and verification with fully worked toy examples from symmetric and asymmetric encryption and hashing, and with a real-world example, the snaproot hash-anchoring protocol for blockchain-based file integrity verification. The paper thereby shows that the mathematical determinacy of a value and its operational uniqueness as a protocol object are two different requirements. Once a normative representation specification has been fixed, byte-level correctness and well-definedness arguments can be carried out without further implementation-dependent serialization or rounding decisions.

---


### 484. [Hyperparameter Transfer in Graph Neural Networks](https://arxiv.org/abs/2607.05017)

**<font color=#1a73e8>作者：</font>** Gage DeZoort, Boris Hanin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The performance of deep learning models crucially depends on the settings of hyperparameters like learning rate, initialization scale, and weight decay. Hyperparameter transfer aims to make near-optimal hyperparameter settings consistent across model scale, so that large models can be optimized by proxy tuning their smaller, cheaper-to-optimize counterparts. While transfer principles are well-studied in the context of dense neural networks in language and vision tasks, they remain comparatively under-explored for graph neural networks (GNNs). We develop and validate a transfer parameterization for GNNs trained with SGD, Adam, and AdamW. Through theoretical scaling analyses and controlled experiments, we show that the proposed parameterization yields stable feature updates, learning rate transfer, and improved performance as width and depth increase. For SGD, we identify graph-dependent first-layer correction factors and show that their use can accelerate early training in graphs with sparse bag-of-words inputs. For Adam, we explore how different message passing normalizations affect early- and late-training transfer behavior, illustrating the importance of message passing normalization and advocating for an associated hyperparameter. For AdamW, we adapt a parameterization that allows for the joint transfer of weight decay and learning rate. Together, these results provide a practical recipe for scaling GNNs across a variety of learning tasks and training scenarios.

---


### 485. [Uncertainty-aware damage identification in short-span bridges via physics-informed variational autoencoder](https://arxiv.org/abs/2607.05025)

**<font color=#1a73e8>作者：</font>** Ana Fernandez Navamuel, A. Javier Omella, Diego Zamora-Sanchez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vibration-based damage identification in civil infrastructure is a challenging, ill-posed inverse problem due to measurement noise, sparse sensor arrays, and environmental variability. While deep learning is powerful for system identification, deterministic approaches lack reliable uncertainty quantification and can yield physically inconsistent results. This work proposes a robust probabilistic Scientific Machine Learning (SciML) framework: a physics-informed Gaussian copula variational autoencoder (PI-GCVAE) for structural health monitoring (SHM). First, we eliminate the need for data-driven surrogates by embedding a differentiable numerical eigenvalue solver directly into the VAE architecture. This ensures that latent space samples satisfy the governing equations of structural dynamics, reducing the trainable parameter space and improving generalization. Second, we replace the conventional independence assumption of latent variables with a Gaussian copula. This model captures complex, physics-dependent spatial cross-correlations between adjacent structural elements, defining feasible solutions while accounting for inherent system variability and measurement errors. Third, compared with alternatives such as Gaussian mixtures, our copula-based VAE provides an efficient distributional model for high-dimensional, strongly correlated latent spaces. We validate the approach using a synthetic dataset of a simply supported bridge subjected to various damage scenarios and corrupted with stochastic Gaussian noise. Synthetic data enables exhaustive validation against ground-truth stiffness values unavailable in practice. Results demonstrate that the PI-GCVAE accurately recovers the true posterior distribution, achieving 77.2% coverage. The proposed framework provides a reliable, scalable tool for early-stage damage diagnosis in operating bridges.

---


### 486. [RUFNet: Query-Guided Support Mask Refinement and Uncertainty Fusion based on Hybrid Mamba for Few-Shot Brain Tumor Segmentation](https://arxiv.org/abs/2607.05035)

**<font color=#1a73e8>作者：</font>** Dongyi He, Xiangkai Wang, Binbing Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot brain tumor segmentation remains challenging due to noisy support masks, inter-patient variations between support and query images, and the lack of pixel-wise confidence estimation. This study proposes RUFNet, a Hybrid Mamba-based few-shot framework that combines support mask refinement with uncertainty-aware posterior fusion. To preserve support-query dependencies with manageable cost, RUFNet adopts a Hybrid Mamba interaction backbone with linear complexity. To reduce support-mask noise, an Attention-Guided Mask Refinement module (AGMR) uses query features to recalibrate support masks and improve prototype consistency. To handle ambiguous predictions, an Uncertainty-Aware Posterior Fusion module (UAPF) estimates pixel-wise variance and adaptively balances few-shot predictions with query-aligned priors. On the Brain Tumor Segmentation Challenge (BraTS) 2020 dataset, RUFNet achieves Dice coefficients of 84.3% and 86.1% in the 1-way 1-shot and 1-way 5-shot settings, respectively, outperforming the compared state-of-the-art methods. These results suggest that Hybrid Mamba interaction, mask refinement and uncertainty modelling can improve the robustness of few-shot medical image segmentation. The official implementation code is available at this https URL.

---


### 487. [CollabEval: Statistically Efficient Collaborative Model Evaluation via Matrix Completion](https://arxiv.org/abs/2607.05046)

**<font color=#1a73e8>作者：</font>** Adam Fisch, Daniel Deutsch, Joshua Maynez 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating generative AI models is a routine, but resource-intensive, process that is conducted over and over again during the course of model development. In this work, we propose Collaborative Evaluation (CollabEval), a simple, effective, and principled method for exploiting dependencies between historical runs of different models on the same tasks to improve statistical efficiency. Specifically, our approach treats model evaluation as a matrix completion problem over an $M \times N$ matrix of evaluation scores, where $M$ is the total number of models and $N$ is the total number of evaluation prompts. We assume that a subset of these $M$ models are targeted for evaluation. For these target models only a small fraction, $p$, of prompts has been annotated with evaluation scores. Leveraging recent results in prediction-powered inference, we build a low-rank approximation of the score matrix, and use the reconstructed values as control variates in a manner that guarantees unbiased estimates of the true evaluation metric mean, in addition to statistically valid confidence intervals. Empirically, across a wide range of datasets, models, and sparsity levels $p$, we find that CollabEval substantially reduces the mean confidence interval size, and the mean squared error of the point estimate, compared to baseline methods at the same annotation budget.

---


### 488. [Beyond Independent Labels: Schwartz-Geometry Decoding for Human Value Detection](https://arxiv.org/abs/2607.05052)

**<font color=#1a73e8>作者：</font>** Víctor Yeste, Paolo Rosso  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human value detection is commonly formulated as sentence-level multi-label classification over the 19 refined Schwartz values, typically predicted as independent labels. Schwartz theory, however, describes them as a circular motivational continuum, in which adjacent values are compatible and opposing values are in tension. We ask whether this structure can be operationalized as an explicit output-space geometry and used as a soft bias rather than a hard constraint. On a DeBERTa-v3-base classifier, we compare two ways of injecting it: training-time geometry-aware objectives and a post-hoc Schwartz-aware energy decoder that scores whole label sets jointly. Across five seeds, training-time geometry gives only limited gains-no larger for the true continuum than for a random ordering-whereas the decoder makes label sets more coherent with the continuum-on theory-aware coherence metrics we introduce-at no cost to Macro-F1 or Micro-F1 (held fixed by its selection rule). The gain is specific to the true Schwartz ordering: it does not appear for a random permutation or an empirical co-occurrence graph through the identical decoder. A bounded Qwen2.5-72B-Instruct diagnostic shows that supplying the continuum at inference shifts behavior but does not match supervised structured prediction. Theory-aware decoding thus offers a lightweight, controllable way to make value detection faithful to its label space.

---


### 489. [Consistent and Editable: A Balanced Framework for Text-Guided Video Editing](https://arxiv.org/abs/2607.05056)

**<font color=#1a73e8>作者：</font>** Tao Jin, Li Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, diffusion models have achieved considerable success in the text-guided video editing domain. However, existing works often struggle to balance the trade-off between temporal consistency and editability in video editing, with consistency and editability typically being inversely related. To address this, we propose a high-quality video editing framework enhanced for consistency and editability, named EquiEdit, which improves coordinatively the temporal consistency and editability of the edited videos while achieving a balance between the two. In terms of temporal consistency, the proposed temporal Mamba module with a tailored temporal-aware scanning scans fused video sequences following four designed directions, effectively enhancing the inter-frame consistency of edited videos. For editability, we design a noise injection strategy based on the spectral transformation to increase editing flexibility, where the Fourier transform is used to preserve the hidden structure in the initial latent noise used for editing, ensuring inter-frame consistency of the edited video and fidelity to the input video. Extensive qualitative and quantitative experiments demonstrate the effectiveness of our method in terms of temporal consistency and editability, as well as its great fidelity to the input video itself.

---


### 490. [KVpop -- Key-Value Cache Compression with Predictive Online Pruning](https://arxiv.org/abs/2607.05061)

**<font color=#1a73e8>作者：</font>** Lukas Hauzenberger, Niklas Schmidinger, Anamaria-Roberta Hartl 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) cache growth is a major bottleneck in autoregressive decoding, as memory and bandwidth scale linearly with context length. Existing KV eviction methods often rely on static heuristics or proxy scores, which poorly track future token utility and cause brittle eviction as relevance shifts. To address this, we introduce KVpop, which learns a fixed-budget KV eviction policy by directly supervising the keep-or-drop decision. The scorer is trained against a novel future-attention target, computed efficiently without materializing dense attention maps. We further introduce a delayed memory-based scorer that, uniquely among learned eviction methods, defers scoring for a fixed number of steps to exploit near-future context. On AIME and HMMT mathematical reasoning, KVpop retains 98% of full-attention performance on Qwen3-4B at 75% KV cache compression and 97% at 88% compression, consistently outperforming established eviction baselines. Qwen3-8B shows even stronger results, reaching near-full teacher performance. These results show that supervising eviction with future-attention signals cuts memory costs while maintaining quality.

---


### 491. [Diffusion-Guided Uncertainty-Aware Delayed Policy Optimization](https://arxiv.org/abs/2607.05064)

**<font color=#1a73e8>作者：</font>** Junqi Tu, Zejiao Liu, Fangfei Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning in real world environments often suffers from severe performance degradation due to delayed feedback. Existing approaches typically mitigate performance degradation caused by observation delays by constructing augmented states or predicting the true states. However, these methods often overlook the inherent discrepancy between delayed state and true states induced by stochastic MDP. We theoretically prove the existence of such a discrepancy and show that it leads to the degradation of the optimal policy. To address this challenge, we propose Diffusion Guided Uncertainty Aware Delayed Policy Optimization (DUPO). Our method explicitly models the relationship between delayed state message and the current state using a diffusion model, and leverages the resulting discrepancy estimates to weight delayed policies. Extensive experiments on continuous robotic control tasks with multiple stochastic delays demonstrate that DUPO consistently outperforms existing methods and remains effective even under long and random delay scenarios.

---


### 492. [LangLoc: "Tell Me What You See"](https://arxiv.org/abs/2607.05077)

**<font color=#1a73e8>作者：</font>** Shaurya Kishore Panwar, Roham Zendehdel Nobari, Shirley Feng Yi Lau 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We tackle fine-grained indoor localization from natural language: given a free-form description of one's surroundings, estimate the observer's 2D position and heading within a known 3D environment. Language queries are lightweight, privacy-preserving, and need no camera - yet prior work stops at coarse scene retrieval and cannot resolve an intra-scene pose. We close this gap with LangLoc, a three-stage pipeline that (i) retrieves the correct scene via a dual-branch GATv2 encoder with CLIP semantic features, surpassing the previous best by 8 percentage points in Top-1 recall; (ii) estimates position and heading by scoring a dense floor grid through ray-cast object visibility, reaching a median error of 0.95 m; and (iii) resolves residual ambiguity through a Bayesian dialog module that asks targeted yes/no questions and updates a pose posterior until the location is pinpointed. To support this task we contribute a benchmark of $13{,}000{+}$ pose-indexed natural-language descriptions over $1{,}300{+}$ indoor 3D scans.

---


### 493. [Computing Monetary Risk Measures in Linear Time](https://arxiv.org/abs/2607.05078)

**<font color=#1a73e8>作者：</font>** Palash Agrawal, Gersi Doko, Maeve Burwell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monetary risk measures have gained popularity for expressing decision-makers' risk aversion. Value-at-Risk (VaR) and Conditional-Value-at-Risk (CVaR), in particular, are used commonly for this purpose. This paper proposes new efficient algorithms to compute these risk measures for a discrete random variable in expected linear time with respect to the size of its domain. First, we propose a QuickVaR algorithm that computes the VaR of a discrete random variable. Then, we leverage QuickVaR to propose QuickDivergence, an algorithm for computing a class of $\varphi$-divergence risk measures, including the popular CVaR risk measure. The QuickVaR algorithm adapts the well-known Quickselect algorithm, while QuickDivergence builds on polymatroid optimization algorithms. Numerical results show that our new algorithms offer an order-of-magnitude speedup for large domains, and a library implementation of the algorithms is available at this https URL.

---


### 494. [RADIANCE: Relative Adaptive Denoising with IP-Adapter for Novel Concept Enhancement](https://arxiv.org/abs/2607.05088)

**<font color=#1a73e8>作者：</font>** Zi-Xiang Ni, Bo-Lun Huang, Teng-Fang Hsiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) diffusion models have achieved striking progress but still struggle to synthesize rare concepts involving unusual attribute-object pairings, often resulting in concept omission or semantic drift where a dominant entity overwhelms the generation. Tracing these failures to a lack of compositional balance during the denoising trajectory, we propose RADIANCE, a training-free framework that treats inference as a closed-loop feedback process. RADIANCE augments pretrained backbones with three modular components: (1) a Compositional Similarity Monitor (CSM) that tracks the emergence of objects and attributes in intermediate latents via CLIP-based feedback; (2) a Bidirectional Scale Controller (BSC) that applies a reactive "restoring force" using positive and negative IP-Adapter scales to rebalance biased trajectories; and (3) a Feedback Guidance Scheduler (FGS) that coordinates these updates across timesteps without additional training. We further extend the framework to multi-object prompts via Delayed Adapter Activation (DAA) and Layer-wise Alternating Guidance (LAG) to prevent premature concept fusion. By overlapping monitoring and denoising through pipelined execution, RADIANCE maintains competitive latency while significantly enhancing the per-sample success rate and effective throughput. Experiments on RareBench and T2I-CompBench demonstrate that RADIANCE consistently enhances compositional alignment and perceptual quality over state-of-the-art baselines.

---


### 495. [Be Indiscrete: The Benefits of Learning Continuous Spine Degeneration Severity Scores](https://arxiv.org/abs/2607.05090)

**<font color=#1a73e8>作者：</font>** Maria Monzon, Andrew Zisserman, Robin Y. Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lumbar spine degeneration is a major contributor to chronic low back pain and is routinely assessed on MRI using ordinal grading systems, e.g. normal, mild, moderate, severe. Consequently, most approaches to train models to grade these MRIs formulate grading as a multi-class classification problem, treating ordinal grades as categorical, ignoring differences in misclassification severity, and imposing hard decision boundaries on a continuous disease process. This work explores modeling spinal degeneration as a continuous severity ranking problem. We introduce SpineRankNet, a framework that learns scalar severity scores from lumbar spinal MRI, and compare it against multi-class classification and ordinal regression. Using multiple degeneration measures from the Genodisc dataset, we show that a model trained using a ranking loss to produce a continuous score enables fine-grained ordering of MRI scans. Furthermore, the ordinal grading classes can be recovered from the score with comparable accuracy to those from a model trained directly for classification. The score learned by ranking even improves discrimination between more distant classes. Source code is available at this https URL.

---


### 496. [Semantic Video Communication via Multi-Scale Convolution and Dynamic Routing for Next-Generation Networks](https://arxiv.org/abs/2607.05093)

**<font color=#1a73e8>作者：</font>** Gengtian Shi, Jinze Yu, Chenhao Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The exponential growth of video traffic demands novel semantic communication paradigms that transmit meaning rather than raw bits. We present a generative AI-enabled framework for semantic video communication addressing two critical challenges: efficient hierarchical temporal modeling for bandwidth-constrained transmission and robust semantic alignment between video content and natural language queries at network edge devices. Our approach introduces a multi-scale temporal convolutional encoder that captures motion patterns across different temporal granularities with O(T) complexity suitable for resource-constrained IoT deployments. We further propose a capsule-based dynamic routing mechanism that iteratively refines segment-query associations, enabling flexible modeling of non-monotonic semantic alignments essential for goal-oriented communication. These components are unified through a multi-task learning objective optimizing temporal boundary regression, cross-modal alignment, and capsule diversity. Experiments on ActivityNet Captions demonstrate significant improvements, achieving 42.9% Recall@0.5 and 41.1% mean IoU while maintaining computational efficiency critical for edge deployment.

---


### 497. [FAST: A Holistic Framework for Optimizing Memory-I/O, Computation, and Sampling in Temporal GNN Training](https://arxiv.org/abs/2607.05095)

**<font color=#1a73e8>作者：</font>** Yushu Cai, Qingrui Zhu, Lei Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal Graph Neural Networks (TGNNs) are widely used for learning from dynamic graphs in applications such as recommendation, social network analysis, and traffic forecasting. However, scaling TGNN training to large dynamic graphs remains challenging due to three intertwined bottlenecks: memory I/O, irregular computation, and temporal neighbor sampling. Existing systems often optimize these stages in isolation, leaving substantial performance headroom on the table. We present FAST, a holistic framework that accelerates end-to-end TGNN training by jointly optimizing sampling, memory I/O, and computation. FAST introduces SlimCache, which exploits within-batch compression and cross-batch caching to reduce host-device data movement under limited GPU memory budgets. It further designs thread-efficient graph operators tailored to sparse temporal subgraphs, improving GPU cache locality and reducing the latency of aggregation and edge softmax. In addition, FAST employs a topology-aware sampling strategy that improves CPU cache locality and accelerates temporal neighbor sampling. Extensive experiments on real-world large dynamic graphs show that FAST achieves an average of 2.1x (up to 4.7x) speedup over state-of-the-art systems without sacrificing model accuracy.

---


### 498. [Functional Bilevel Optimization for Predictive Fairness](https://arxiv.org/abs/2607.05098)

**<font color=#1a73e8>作者：</font>** Ieva Petrulionyte, Julien Mairal, Michael Arbel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When sensitive attributes are continuous and high-dimensional $-$ demographic score vectors, posteriors over attributes, age or income profiles $-$ enforcing full statistical independence is often too restrictive, and existing relaxations rely on indirect dependence penalties or adversarial schemes that do not directly target the fairness-accuracy trade-off. We instead consider mean demographic parity through DPVar, the variance of the conditional-mean prediction given the sensitive attribute, and show that optimizing it yields a functional bilevel problem. We propose two algorithms for this problem: FBO, which uses a closed-form adjoint we derive for the squared-loss case to obtain an exact hypergradient, and ITD, which differentiates through unrolled inner steps and extends beyond squared loss. On synthetic data and a new semi-synthetic benchmark built from 60 tabular regression datasets, both methods achieve the lowest or near-lowest aggregate fairness-accuracy regret, and consistently match or outperform strong HSIC, adversarial, linear-dependence, and generalized-DP baselines.

---


### 499. [Counterfactual Methods for Detecting Unfairness in Anti-Money Laundering Algorithms](https://arxiv.org/abs/2607.05101)

**<font color=#1a73e8>作者：</font>** Lea Multerer, Michele Inchingolo, David Kletz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The application of machine learning-based predictive algorithms to Anti-Money Laundering (AML) has grown rapidly, driven by the vast volume of financial transaction data available to banks. These algorithms are typically trained not only on transactional data but also on sensitive client information, which may raise fairness concerns. Despite this, AML detection systems remain largely underexplored from a fairness perspective, even though deeper analytical methods based on counterfactuals are now available. Such techniques enable the decomposition of the direct and indirect effects of potentially sensitive features on model predictions, thereby supporting the evaluation of whether their influence is acceptable from a fairness perspective. Closing this gap, we consider the synthetic IBM AMLSim transaction dataset and construct additional features of the country of an account and its average behaviour. This improves the predictive performance of diverse machine learning models, ranging from baseline decision trees to state-of-the-art graph neural networks. We assess the potential unfairness associated with these features through a counterfactual, path-specific effect analysis. This reveals that fairness violations tend to be more pronounced for models whose predictive performance benefits the most from the extended features. Such a finding highlights a concrete instance of the trade-off between predictive accuracy and fairness in AML applications, thus underscoring the urgency of a systematic fairness analysis in such critical domains.

---


### 500. [Choosing a parallel heterogeneous ensemble method for tabular classification](https://arxiv.org/abs/2607.05103)

**<font color=#1a73e8>作者：</font>** Vassili Maillet, Gustavo, Angulo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parallel ensemble methods were compared on $56$ small-to-medium tabular classification tasks drawn from OpenML CC18. A set of ``best practice'' recommendations on the use of ensemble methods was derived from these observations. It was later validated on 28 additional tasks using TabArena's precomputed data, where the recommendation set significantly outperformed Single Best and matched or exceeded individual ensemble methods.
Two key observations were made. First, Blending and Stacking are inconsistent, but their inconsistencies are independent and happen on different tasks. Second, while Hard Voting's probabilistic classification is rather weak, a consequence of using vote proportions as posterior estimates, Robust Soft Voting's probabilistic classification is particularly successful, especially in the multiclass case.

---


> [!TIP]
> 当前位于：**451-500**（第 10/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
