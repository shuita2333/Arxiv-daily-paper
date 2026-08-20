# 📦 其他研究 | 2026年08月21日

> 本类共 **184** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-184](./part-04.md)

---

### 101. [Multi-Class Electrical and Mechanical Fault Classification Using Random Convolutional Kernels](https://arxiv.org/abs/2608.18716)

**<font color=#1a73e8>作者：</font>** Mouhamadou Mansour Lo, Mouad Talbaoui, Gildas Morvan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diagnosing faults in rotating machinery is essential for ensuring the reliability of industrial processes. Random convolutional kernel-based Time Series Classification (TSC) methods, such as ROCKET and its variants, provide an attractive trade-off between predictive performance and computational efficiency. In this work, we evaluate SelF-Rocket for the multi-class diagnosis of both mechanical and electrical faults and introduce, as a new contribution, a multivariate extension of the original method. The proposed approach is compared with leading ROCKET-based methods on two public benchmark datasets, MaFaulDa (mechanical faults) and ITSC-UDG (stator inter-turn short circuits), under both univariate and multivariate settings. Experimental results show that SelF-Rocket achieves the best overall accuracy-latency trade-off among the evaluated methods, obtaining the highest classification performance on MaFaulDa while remaining highly competitive on the more challenging ITSC-UDG dataset.

---


### 102. [Model Literacy: An Extra Summative Evaluation Factor for Visual Analytics](https://arxiv.org/abs/2608.18721)

**<font color=#1a73e8>作者：</font>** Lei Xia, Siyu Wu, Haodian Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding and enhancing visual analytics (VA) performance is important for maximizing their impact. Existing studies have successfully applied well-established summative evaluation methods from information visualization to the VA context, yet the recent emphasis on an extra data analysis/modeling stage in the VA pipeline poses an additional challenge. Inspired by the modern concept of visualization literacy, this paper examines model literacy, namely users' knowledge of the analysis model used in a VA technique, as an additional factor for VA performance. Results from a controlled study on the visual analysis of multidimensional data with two dimensionality-reduction models indicate a positive correlation between model-task accuracy and VA-task accuracy. The study involves two common dimensionality-reduction models, PCA and t-SNE. The correlation is stronger for PCA than for t-SNE in the current task design, a pattern consistent with the possibility that VA effectiveness is more closely associated with model literacy when model outputs are less directly readable from the visualization. Completion-time evidence does not show a stable efficiency gain, suggesting that differences in model intuitiveness may help explain when model knowledge shortens task completion and when it involves additional interpretive effort. The findings of this study suggest ways to further enrich VA evaluation methods and provide directions for developing more rigorous model-literacy assessment instruments.

---


### 103. [Budget-First Tariff Recommendation (BFTR): A Complete Algorithmic Framework for Telecom Plan Recommendation without Overcharging](https://arxiv.org/abs/2608.18723)

**<font color=#1a73e8>作者：</font>** Ghislain Dorian Tchuente Mondjo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Telecom operators traditionally offer predefined tariff grids, forcing users to choose from a limited set of plans. This paper proposes BFTR (Budget-First Tariff Recommendation), a complete algorithmic framework integrating eight Budget-First strategies, including two original hybrid approaches: Recursive Hybrid (conditional interpolation) and Knapsack-First Hybrid (priority knapsack). Unlike existing approaches that adjust prices upward to guarantee a minimum margin, BFTR guarantees the absence of overcharging by systematically aligning the final price with the catalog reference price. We mathematically formalize each strategy, prove the existence of an offer for any positive budget, and prove that the price deviation (surcharge) is zero for all strategies that do not use interpolation with correction. A detailed comparative analysis confronts BFTR to ten main existing tariff models on ten dimensions. Experiments on a dataset of 974 customers inspired by the Nigerian MTN market show that: (i) Recursive Hybrid is optimal for the customer (100% budget used, 29.9 GB volume, utility 0.946, 0% overcharging), (ii) Piecewise offers the highest volume (39.7 GB) with 0% overcharging, (iii) Power Law provides an excellent compromise (99.9% budget, 38.1 GB, 0% overcharging). All strategies achieve a zero surcharge, confirming the theoretical guarantees. A sensitivity analysis on the weighting parameter alpha (0.2 - volume priority, 0.5 - balance, 0.8 - budget priority) shows that utility rankings evolve logically. Execution times (< 10 ms) and very low failure rates (0% for robust strategies) confirm the operational viability of the system. The formal proof of the absence of overcharging constitutes a major theoretical contribution.

---


### 104. [Visual-Aware Representation of Web Pages for Machine Learning Applications](https://arxiv.org/abs/2608.18727)

**<font color=#1a73e8>作者：</font>** Radek Burget, Radek Hranický  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Applying machine learning to web pages is challenging due to the need to interpret HTML together with associated resources and perform rendering to obtain a meaningful visual and layout-aware representation. As a result, machine learning over web content remains comparatively underexplored. In this paper, we present a platform for visual-aware representation and machine learning over web pages based on the open-source rendering tool FitLayout. The platform provides a server capable of rendering web pages, explicitly capturing their visual and structural properties in an RDF-based representation, and persisting the rendered documents in an integrated storage. The processing pipeline is controlled via a REST API, while SPARQL queries are used to retrieve structured data suitable as input for machine learning algorithms. By explicitly modeling rendered web pages, including fine-grained layout details, the platform enables dataset sharing and supports the reproducibility of experimental results. The architecture supports the complete dataset preparation workflow, from web page collection and rendering through preprocessing and annotation of content elements to downstream learning tasks. We further provide a Python client library that integrates the platform with standard machine learning workflows. As a demonstration, we show how rendered web pages can be transformed into graph-based representations and used to train graph neural networks for recognizing key content elements, illustrating both the applicability of the approach and the reproducibility of the results.

---


### 105. [A Few Cases Are All You Need: An Empirical Study of Annotation-Efficient LoRA Fine-Tuning of MedSAM3](https://arxiv.org/abs/2608.18731)

**<font color=#1a73e8>作者：</font>** Sachin Dudda Nagaraju, Bendik Skarre Abrahamsen, Ashkan Moradi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation is essential for clinical workflows such as treatment planning and disease assessment. While specialist tools like TotalSegmentator and MRSegmentator achieve strong performance, they require large annotated datasets for training. Medical foundation models offer a promising alternative through large-scale pretraining that reduces the annotation burden for new tasks, but zero-shot performance remains limited. Parameter-efficient adaptation via Low-Rank Adaptation (LoRA) enables efficient specialization with few trainable parameters, but a key question remains: how many expert-annotated cases are needed to achieve clinically useful segmentation performance? We address this by adapting MedSAM3 with LoRA for five abdominal organs (liver, kidneys, spleen, gallbladder, and pancreas) in CT and MRI using only 1, 2, 5, and 10 annotated cases, evaluating on AMOS22 dataset. With just 10 cases, models achieve performance competitive with specialist systems trained on orders of magnitude more data. Notably, this includes reliable gallbladder segmentation (Dice 0.68 CT, 0.59 MRI) where existing tools fail almost completely (Dice 0.0004), while remaining within 5--10% of MRSegmentator for liver, kidneys, and spleen using over 100 times fewer annotations. Furthermore, external validation on the Whole Heart Segmentation dataset shows that the approach extends to cardiac segmentation, a use case beyond the scope of TotalSegmentator (MRI) and MRSegmentator, achieving competitive left ventricle (LV) performance with only 10 annotated cases. Training requires only3--5,hours per organ on a single GPU, approximately 2--3 times faster than nnU-Net. These findings suggest that ten annotated cases are sufficient for clinically useful segmentation, effectively reducing bottlenecks for both image annotation and training time.

---


### 106. [Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditioned Objectives for MPC Planning](https://arxiv.org/abs/2608.18746)

**<font color=#1a73e8>作者：</font>** Jiawei Wang, Ke Rui, Yushen Zuo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> JEPA-style latent world models can use Euclidean distance to a goal latent as the cost for model-predictive control (MPC). Strong decoding of task variables, however, does not guarantee that this particular cost ranks candidate action sequences by real task progress. We call the latter property \emph{decision-metric alignment}. We introduce Plan-Real Spearman, which measures latent--real rank agreement on random plans, and CEM-stage Spearman, which measures the same agreement as cross-entropy-method (CEM) search concentrates its proposal. We analyze sufficient conditions under which latent distance preserves real-cost rankings, identifying encoder distortion, terminal rollout error, and candidate margins as the controlling quantities. Guided by the observed empirical alignment gap, DA-LeWM augments LeWM with inverse-dynamics and demonstration-conditioned goal-action heads. Across all our experiments, DA-LeWM accelerates convergence and achieves higher online success than LeWM, while probe scores remain similar. These results show that action-conditioned objectives improve the geometry used by Euclidean-cost, CEM-based latent MPC.

---


### 107. [Geometric Data Perturbation with Noisy-Anchor Alignment for Privacy-Preserving Collaborative Learning](https://arxiv.org/abs/2608.18749)

**<font color=#1a73e8>作者：</font>** Keiyu Nosaka, Yamato Suetake, Yuichi Takano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geometric Data Perturbation (GDP) enables one-shot, privacy-preserving collaborative learning: each participant applies a distance-preserving transformation to its private data and uploads only the resulting representation to a central analyst. We study GDP under analyst-participant collusion, in which the analyst combines all uploaded representations with the private data and transformations disclosed by colluding participants to recover a non-colluding participant's private data. Participant-specific independent transformations resist this attack but map participants' data into incompatible representation spaces, degrading downstream model performance. Shared-anchor alignment from Data Collaboration (DC) analysis restores compatibility and improves utility, but we show that disclosing the DC anchor matrix enables exact recovery of non-colluding participants' private data even in the presence of collusion. Adding noise directly to the private-data representations mitigates this vulnerability but substantially reduces utility. We propose adding noise to the anchor representations instead. Each participant independently transforms its private data and the shared anchor matrix, perturbs only the resulting anchor representation, and uploads both representations in a single round. Using the noisy anchor representations, the analyst aligns the private-data representations by solving a Generalized Orthogonal Procrustes Problem. We characterize alignment and recovery errors, specialize a conservative sufficient condition for convergence of the alignment to our setting, and analyze three recovery attacks. Experiments on MNIST and CelebA show that, across the evaluated attacks and deployment settings, anchor noise achieves higher learning accuracy than private-data noise at comparable measured leakage, yielding a more favorable privacy-utility trade-off under the specified collusion model.

---


### 108. [SED-FOD: Scattering-Aware Expert Decomposition for Few-Shot Cross-Sensor SAR Object Detection](https://arxiv.org/abs/2608.18755)

**<font color=#1a73e8>作者：</font>** Shu Yang, Zhen Chen, Zhiyu Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic aperture radar (SAR) object detection is an important part of remote sensing interpretation. However, because of variations in frequency band, resolution, background clutter, and target scattering responses, the performance of existing detectors often degrades when training and testing data are acquired from different SAR domains. Although domain adaptation methods offer a promising paradigm for solving this problem, most of them mainly pursue domain-invariant feature alignment and suppress sensor-dependent scattering characteristics that are useful for object detection. This problem becomes more challenging in few-shot scenarios, where only a few fully annotated target-domain SAR images are available. To address this issue, we propose a scattering-aware shared-specific feature decomposition framework for few-shot SAR domain adaptation object detection. We decompose detection features into a shared path and several soft-gated scattering-specific expert paths. The shared path learns transferable object structural information and is used for asymmetric domain alignment, while the scattering-specific experts adaptively compensate heterogeneous SAR responses. In addition, routing-domain auxiliary loss is introduced to encourage specific experts to capture sensor-dependent routing preferences, and an expert balancing loss is used to prevent routing collapse. Extensive experiments on four bidirectional heterogeneous SAR detection tasks between FARAD-X/FARAD-Ka and MiniSAR under different few-shot settings have been conducted and experimental results demonstrate that the proposed method achieves superior performance in both forward and reverse adaptation directions.

---


### 109. [Beyond Predictive Fairness: Quantifying Attribution Consistency Across Demographic Groups in Diabetic Retinopathy Screening](https://arxiv.org/abs/2608.18759)

**<font color=#1a73e8>作者：</font>** Kerol Djoumessi, Philipp Berens  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness in medical imaging is commonly evaluated through subgroup performance metrics, yet it remains unclear whether models rely on consistent visual evidence across demographic groups. This work introduces the Explanation Consistency Score (ECS), a fairness-aware metric based on Jensen-Shannon divergence that quantifies the similarity of attribution maps across subgroups. Using diabetic retinopathy screening as a case study, ECS is evaluated globally and within disease severity. Experiments reveal that while predictive performance differs across ethnic groups, explanation consistency remains relatively high and shows no significant association with performance disparities. These findings suggest that predictive fairness and explanation consistency capture complementary dimensions of model behavior, motivating fairness evaluations that extend beyond predictive performance.

---


### 110. [Enhancing Distance-Based Graph Autoencoders with Structural Penalties for Dynamic Graph Embedding](https://arxiv.org/abs/2608.18762)

**<font color=#1a73e8>作者：</font>** Aleksandar Tomčić, Miloš Savić, Miloš Radovanović  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph autoencoders (GAEs) are widely used for learning representations of dynamic graphs. However, their optimisation objectives typically do not take structural heterogeneity across nodes into account. We propose three distance-based GAE variants that incorporate structural penalties into the reconstruction loss. All variants share a two-layer Graph Convolutional Network encoder and a Euclidean-distance decoder trained with distance-based reconstruction objectives. We extend sparsity-corrected loss with two node-level regularization terms: (i) a hub penalty based on degree centrality, and (ii) a penalty based on Natural Community Local Intrinsic Dimensionality (NC-LID). The paper is motivated by prior evidence linking high NC-LID to reduced embedding quality. The proposed methods are designed to emphasize reconstruction errors for structurally ambiguous nodes. Experiments on multiple dynamic graph data sets show that incorporating NC-LID-based regularization consistently improves reconstruction performance over the baseline without structural regularization and the method using hub-aware regularization. These findings highlight NC-LID as a useful structural signal for enhancing distance-based graph autoencoders in dynamic settings.

---


### 111. [Learning Canonical Register Automata over Ordered Data Domains](https://arxiv.org/abs/2608.18765)

**<font color=#1a73e8>作者：</font>** Yong Li, Qiyi Tang, Di-De Yen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Register automata are finite automata equipped with memory that recognize data languages over infinite alphabets. In this work, we investigate active learning algorithms for deterministic register automata (DRAs) over ordered data domains--covering both dense domains, such as the rationals, and non-dense domains such as the integers. We show that the active learning problem for DRAs over both dense and non-dense ordered domains can be treated within a single unified framework. More specifically, we develop and implement a polynomial-time active learning procedure for DRAs over ordered domains, using oracles for membership, equivalence and memorability queries. The memorability queries were originally introduced for learning DRAs over domains with identity tests. Our unified framework also leads to a new consequence: minimization of DRAs over the non-dense ordered domain of integers is decidable, extending a result previously known only for dense domains. Finally, we give improved complexity bounds of several decision problems for DRAs over ordered domains that are closely related to the queries used in active learning.

---


### 112. [To Go Far, Go Together: Diverse Preferences Induce a Curriculum for Reward Optimization](https://arxiv.org/abs/2608.18770)

**<font color=#1a73e8>作者：</font>** Taehyung Kim, Jongeun Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning a reward model from human feedback and optimizing a policy against it is one approach to aligning AI systems with individual users. From a fairness perspective, existing work improves such alignment by developing data-efficient and accurate reward models that capture minority preferences despite scarce data. We push this line of inquiry one step further and argue that data-efficient and accurate per-user reward models are not sufficient: users whose reward models are difficult to \textit{optimize} at the policy level can become a new underserved group. We start from the observation that one user's reward model can be easy to optimize from the initial policy while another's is not. We argue that, given a sufficiently diverse user population, a curriculum naturally emerges between easy- and hard-to-optimize reward models. Building on this insight, we propose CurriPO, which grows a tree-structured curriculum to accommodate diverse user-specific objectives, covering the population in a single traversal. Specifically, CurriPO automatically constructs a curriculum over diverse user reward models, allowing it to branch from the existing curriculum and reuse reward models previously incorporated into the curriculum. To the best of our knowledge, this is the first work to explicitly exploit multi-user structure to address optimization in AI alignment. Extensive experiments on personalized continuous control in a simulated environment show that CurriPO achieves $1.2$--$2.1\times$ the population satisfaction of the strongest baseline while substantially reducing training time. Additional analysis attributes much of this improvement to the users left underserved by conventional optimization.

---


### 113. [MIFR: A Modality-Invariant and Fair Representation Framework for Skin Disease Classification](https://arxiv.org/abs/2608.18774)

**<font color=#1a73e8>作者：</font>** Asonyu Senge Njih, Yvan Guifo Fodjo, Vianney Kengne Tchendji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skin diseases represent a major global public health burden, yet machine learning tools developed to assist in their diagnosis suffer from two critical limitations: reliance on only one modality for diagnosis and systematic performance disparities across skin tones. While existing approaches address each challenge separately, this work proposes a modality-invariant framework with fair representation (MIFR) for skin disease classification. The architecture pairs clinical photographs with dermoscopic images using ViT-based encoders, projecting each input into a high-dimensional embedding space via modality-specific projection heads. The resulting model is trained with a five-component multi-objective loss including weighted cross-entropy for classification, confusion and skin-type classification losses for fairness, per-modality supervised contrastive loss for class alignment, and a modality-invariance loss for clinical and dermoscopic modality alignment. Experiments on the HIBA+Derm7pt paired dataset and the external PAD-UFES-20 and ISIC 2019 datasets showed that modality-invariant representation learning provides competitive predictive performance compare to relevant baseline models and competitive fairness on the internal dataset. t-SNE visualizations confirmed that clinical and dermoscopic embeddings of the same disease are geometrically aligned, validating the joint objectives.

---


### 114. [GraphK: Variable-Size Graph Generation with Efficient Edge Construction](https://arxiv.org/abs/2608.18777)

**<font color=#1a73e8>作者：</font>** Resul Tugay, Eren Oluğ, Elif Ak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph generation models have advanced significantly with deep learning, yet they remain limited in scalability, flexibility, and ability to model underlying structures. We present GraphK, a novel encoder-sampler-decoder framework for graph generation that overcomes these challenges through structural flexibility and computational efficiency. Unlike autoregressive approaches constrained by vocabulary size (i.e. number of nodes in graph generation), GraphK allows for both upscaling (generating graphs with more nodes than the input) and downscaling, providing a flexible control over output graph size. By learning permutation-invariant latent representations and sampling new node embeddings via maximum likelihood estimation, GraphK generalizes across graph sizes and structures. For edge generation, we employ edge prediction with a KDTree-based top-k neighbor search in the latent space, reducing computational cost. Based on the manifold smoothness assumption, our method effectively captures graph properties. Experiments on synthetic and real-world datasets show that GraphK outperforms existing methods, accurately learns graph structures, and generates synthetic graphs without explicit definitions.

---


### 115. [Engineering Psychological Safety in Autonomous Vehicles: A Systems-Theoretic Framework for Psychological Safety in Autonomous Vehicles and its Validation in Real-World Scenarios](https://arxiv.org/abs/2608.18778)

**<font color=#1a73e8>作者：</font>** Yandika Sirgabsou, Benjamin Hardin, François Leblanc 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite rapid technological advances, the societal acceptability of autonomous vehicles (AVs) remains limited by psychological barriers that extend beyond traditional concerns of physical safety. While factors such as trust and perceived safety are known to influence user acceptance, there is a lack of formalized mechanisms and engineering methods to systematically identify, assess, and mitigate psychological risks arising from human-AV interactions. To address this gap, this work proposes and validates a systems-theoretic framework for the assessment of psychological safety in autonomous vehicles. First, a comprehensive psychological safety risk model is defined, extending the Systems-Theoretic Accident Model and Processes (STAMP) to incorporate key psychological constructs such as trust, perceived control, predictability, and perceived support. Based on this model, a hazard analysis method (AV-PsySafe) is developed to systematically identify psychological hazards, unsafe control actions, and loss scenarios, while introducing a Psychological Safety Integrity Level (PsySIL) to support risk prioritization. Second, the applicability and relevance of the framework are evaluated through its deployment in realistic autonomous vehicle scenarios. A structured validation approach is implemented, including a methodological guide, standardized analysis templates, and the collection of analyst feedback. The results demonstrate that the framework can be consistently applied by practitioners, producing meaningful insights into psychological risks. Overall, this work establishes both the theoretical foundations and practical feasibility of a unified approach to co-assessing psychological and physical safety in autonomous systems, contributing to more human-centred and trustworthy AV development.

---


### 116. [A Real-Time Tsetlin Machine-based Non-intrusive Load Monitoring System on MCUs](https://arxiv.org/abs/2608.18780)

**<font color=#1a73e8>作者：</font>** Tianhang Tan, Han Wu, Tousif Rahman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-Intrusive Load Monitoring (NILM) systems estimate individual appliance energy consumption from a single aggregate meter, without requiring separate sensors for each device. By installing a single meter that measures a building's total electricity consumption, NILM algorithms can determine the active status of each appliance. However, traditional NILM systems use computationally intensive optimization algorithms to process offline data, limiting their capability for on-device deployment, where sensitive household data must be processed locally. This paper proposes a Tsetlin Machine (TM)-based NILM framework, targeting real-time applications on resource-constrained microcontrollers (MCUs), enabling privacy-preserving edge deployment. The problem is reformulated as a classification task, and the proposed approach achieves an average precision of 90% and recall of 96% for two-appliance classification, and 77% precision and 80% recall for four appliances on the REDD dataset. The trained model occupies only 18 KB of flash memory and achieves an inference latency of 0.43 ms on an ESP32, demonstrating its suitability for embedded NILM applications on MCUs.

---


### 117. [Scoring and Gamification to Encourage Sustainable Use of Compute Clusters](https://arxiv.org/abs/2608.18786)

**<font color=#1a73e8>作者：</font>** Maximilian MacDonald, Chris McCaig, Sean MacAvaney 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The environmental cost of computing continues to grow, yet behaviour change remains limited. We present a composite sustainability score integrating average carbon intensity, resource utilisation, and embodied emissions into a single 0-100 metric designed for gamified feedback. Each component rewards a different dimension of sustainable behaviour: carbon-aware workload shifting, high resource utilisation, and selecting hardware that is commonly underutilised. This scoring system is built into an existing cluster management interface and underpins three dashboard conditions: raw metrics, composite score, and a gamified tree visualisation, which we are planning to evaluate in a 12-week within-subjects study with approximately 35 researchers. Furthermore, we open the discussion on the challenge of defining computational work `goodness' in the context of sustainability scores.

---


### 118. [A revised framework for the assessment of psychological safety in autonomous vehicles](https://arxiv.org/abs/2608.18801)

**<font color=#1a73e8>作者：</font>** Yandika Sirgabsou, Benjamin Hardin, François Leblanc 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite recent technological progress in the development of autonomous vehicles (AVs), their societal acceptability remains a subject of debate as recent research findings point to psychological roadblocks. Concerns arise not only for physical safety but also for potential psychological risks resulting from human interaction with AVs. Psychological concepts such as trust, and perceived safety are well-studied in this context and are found to be determinant factors for the intention to use AVs. Unfortunately, there has been no formalization of the mechanism by which human interaction with AVs may lead to psychological hazards, threatening trust, perceived safety, and acceptability. Furthermore, there has been little prior research that conceptualizes the severity of psychological risk in AVs, and there are no clear guidelines for a systems designer on how to assess and address psychological risk in the AV development context. To address these limitations, this paper extends a theoretical framework for AV psychological safety risk assessment based on an early proposal. The proposed framework consists of an extended risk model for psychological safety including all the key concepts related to psychological safety in AVs, and an assessment method based on the Systems-Theoretic Accident Model and Processes (STAMP). We demonstrate the usefulness of the theoretical framework through a highly automated AV use case scenario, uncovering factors which may lead to psychological risk for an occupant. The use cases provide examples of how to use the framework to extensively evaluate psychological risk and determine vehicle behaviour that could lead to this risk. By developing a theoretical framework for AV psychological safety risk assessment, we provide a foundation and a method that were previously lacking to better enable responsible AV development regarding psychological safety.

---


### 119. [Forgetting, plasticity, and co-observation: a third facet of continual learning](https://arxiv.org/abs/2608.18803)

**<font color=#1a73e8>作者：</font>** Timm Hess, Abhishek Jha, Gido M. van de Ven 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient continual learning remains a fundamental challenge for deep neural networks. While catastrophic forgetting and loss of plasticity are widely considered the primary obstacles to overcome, we show that these two issues cannot fully explain the performance gap between naive sequential training and offline joint training. In this paper, we highlight data co-observation as a distinct factor influencing continual learning performance. By decoupling the constraints of separate data access from stability and plasticity, we systematically investigate the representational benefits gained by observing training data together. Empirically, we demonstrate a consistent performance difference between joint and separate training across both supervised and self-supervised paradigms in generic data-incremental "chunking" scenarios, whilst mitigating forgetting and controlling for plasticity. Our findings indicate that simultaneous observation of training data (co-observation) yields benefits to the learner's generalization that extend well beyond mere knowledge retention, and that this effect does not require a specific continual distribution shift. Furthermore, we contextualize prominent continual learning mechanisms through this lens: while distillation-based approaches act only as effective knowledge retention mechanisms, our results suggest that the empirical success of memory replay goes beyond the mitigation of forgetting, actively reintroducing the benefits of data co-observation into the learning process.

---


### 120. [Tensor Field Models](https://arxiv.org/abs/2608.18808)

**<font color=#1a73e8>作者：</font>** Alexander Strunk, Roland Assam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces Tensor Field Models (TFMs), realization-level Mathematical Structures in which a learned Operator maps a product of admissible component-section families to a prescribed family of time-dependent tangent sections on a Generative State Manifold. Analytic and dynamical restrictions are encoded through the choice of admissible families rather than imposed by the root definition. Constructed, component-separable, and Tensor Bundle TFMs provide structured refinements of this common object. In the conditional realizations considered here, a structured condition $c=(c_1,\ldots,c_n)$ is mapped componentwise to a reusable collection $\mathbf H_c=(H_{c_1}^{(1)},\ldots,H_{c_n}^{(n)})$. In the architectures evaluated here, the component representations remain distinct and are combined only by the Field Operator to produce the generated Vector Field. All learned models are trained using Flow Matching. Experiments show that TFMs can improve performance and that amortized sampling enabled by reusable condition representations can accelerate generation.

---


### 121. [Many Optimizers But Only One Training Path: Repeated Resampling for Adaptive Optimizer Selection](https://arxiv.org/abs/2608.18810)

**<font color=#1a73e8>作者：</font>** Ronald Richman, Mario V. Wüthrich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An optimizer is usually chosen before training a deep neural network and then kept fixed. Treating optimizer choice as a hyperparameter could boost performance, but it requires several complete training runs and discards all but the winner. Repeated Optimizer Resampling (ROR) instead searches during one evolving run. Every $b$ epochs, each candidate optimizer scouts from the current model weights for $s$ epochs. The best scout continues for the remaining $b-s$ epochs, and that completed segment becomes the new incumbent if it improves the validation objective. This design allows the preferred optimizer to change as training progresses.
We compare two variants of ROR on MNIST, Fashion-MNIST, and two motor insurance claim-count models. Nine fixed optimizers and both ROR variants are evaluated with the same ten seeds. One-epoch ROR uses 24\% to 35\% of the aggregate training needed to identify the best fixed optimizer exhaustively and remains close to that optimizer on all four tasks. These results support short scouting as a practical way to search over optimizers without completing every candidate run.

---


### 122. [A Unifying Relational Perspective on Expressive Lottery Tickets](https://arxiv.org/abs/2608.18819)

**<font color=#1a73e8>作者：</font>** Lorenz Kummer, Samir Moustafa, Anatol Ehrlich 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are widely used, but how parameter sparsity affects the expressivity of relational (RGNNs) and temporal (TGNNs) variants is poorly understood. The Strong Expressive Lottery Ticket Hypothesis (SELTH) posits the existence of sparse GNNs that preserve Weisfeiler-Leman (WL) expressivity on static graphs. We generalize this existence result to a probabilistic statement for multi-relational and temporal domains via the relational WL (RWL). We prove that sufficiently parameterized RGNNs contain sparse subnetworks that maintain 1-RWL expressivity and derive a lower bound on the probability that a random pruning yields such a subnetwork. We show that common TGNNs and cross-graph message passing schemes admit RGNN reformulations such that they inherit these guarantees and, moreover, that the expressivity of a sparse RGNN is connected to its optimization behavior under common update regimes. Experiments instantiate the bound, compare it to empirical probabilities on synthetic data, and study how pre-training expressivity relates to optimization and prediction quality metrics on temporal and molecular benchmarks.

---


### 123. [Pairwise Logical Selection of Enthymeme Completions under Semantic-Link Uncertainty](https://arxiv.org/abs/2608.18820)

**<font color=#1a73e8>作者：</font>** Xuyao Feng, Antonis Bikakis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Arguments often omit premises or claims, forming enthymemes. We study pairwise logical selection between two candidates for the omitted component. Existing natural language methods can identify or generate candidates but often do not expose how the selected candidate completes the inference, while logic-based approaches usually assume that the required formulae and background knowledge are available. We extend a prior neuro-symbolic pipeline from missing-premise to missing-claim selection and replace binary entailment outcomes with logical-resistance scores. Top-Link uses weighted Partial MaxSAT under a single configuration of highest-confidence semantic links. We then introduce Possible-World Atom-Link Formalization (PWAL), which keeps translated formulae fixed and marginalizes logical resistance over alternative cross-formula semantic-link configurations. We evaluate PWAL on five tasks: ARCT and a CDED-derived task for missing-premise selection, iDebate- and AAE2-derived tasks for missing-claim selection, and alphaNLI for abductive hypothesis selection. Relative to Top-Link, PWAL raises strict accuracy by 2.95-30.86 percentage points and reduces tie rates by 4.57-58.00 percentage points on all five tasks. When ties receive half credit, accuracy still increases by 0.45-6.04 percentage points. PWAL also records the translated formulae, sampled link configurations, and resistance components for every comparison, providing a transparent trace of each score.

---


### 124. [Understanding Multilingual Medical ASR Adaptation Through Layer-Wise Analysis](https://arxiv.org/abs/2608.18825)

**<font color=#1a73e8>作者：</font>** Souranil Kahali, Rituparna Bose, Abner Hernandez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical automatic speech recognition (MedASR) requires adaptation to specialised terminology, limited annotated clinical data, and multilingual use cases. Although large-scale pretrained ASR models such as Whisper achieve strong generalisation, their behaviour after medical and multilingual adaptation remains insufficiently understood beyond word error rate (WER). This paper investigates how multilingual medical adaptation reshapes the internal representations of Whisper models through layer-wise encoder analysis. We compare zero-shot decoding, English-only fine-tuning, German-only diagnostic fine-tuning, two-stage EN->EN+DE continuation, and direct EN+DE fine-tuning across Whisper model sizes. Fine-tuning substantially improves MedASR performance, but the best model depends on the adaptation setting: Whisper-Medium gives the lowest English WER (7.72%) and the lowest combined EN+DE WER under direct EN+DE training (26.30%); German-only Whisper-Large-v3 gives the lowest German WER (44.96%), but as a within-corpus diagnostic on 86 single-speaker training utterances rather than robust generalisation. Layer-wise analysis of the two-stage Whisper-Small trajectory shows that English medical fine-tuning produces the dominant encoder shift, whereas multilingual continuation largely preserves the adapted representation space. Domain and language information remain highly recoverable across layers, while linearly recoverable error-predictive cues weaken as WER improves.

---


### 125. [EfficientSync: Real-Time Lip Synchronization via Deformation-Based Reference Texture Mixing](https://arxiv.org/abs/2608.18832)

**<font color=#1a73e8>作者：</font>** Fa-Ting Hong, Runzhen Liu, Luchuan Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-driven lip synchronization manipulates the mouth region of a talking-face video to match the driving audio while preserving head pose, identity, and background. Although the task is inherently local editing, prevailing approaches reconstruct the entire lower face with heavy GAN- or diffusion-based decoders, incurring substantial latency and, more critically, hallucinating intra-oral details such as teeth and lip wrinkles instead of preserving authentic textures. We contend that the bottleneck in identity preservation is not the scarcity of reference frames, but the lack of a mechanism that faithfully transfers the genuine textures they already contain. We therefore present EfficientSync, a real-time deformation-based framework that retains reference textures rather than resynthesizing them. First, the Dynamic Texture Mixer reformulates multi-reference fusion as channel-wise selection, evaluating each spatially aligned reference in a global context and aggregating them by channel-wise weighted summation, preserving textural integrity at low cost. Second, Spatio-Temporal Shifted Adaptive Masking decomposes the source frame into lip-generation conditions and an independent background prior, suppressing lower-face leakage while blending the synthesized mouth seamlessly into the background. Third, STAR Sampling, a zero-overhead pre-processing step, retrieves the sharpest and most topologically diverse reference frames. Experiments on HDTF and VFHQ show state-of-the-art visual quality and identity preservation at 166 FPS on a single GPU. Video demos: this https URL.

---


### 126. [Multi-stage neural operator learning with application for convolutions](https://arxiv.org/abs/2608.18851)

**<font color=#1a73e8>作者：</font>** Zhiping Mao, Zhenye Wen, Yong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Convolution integrals widely exist in applications, and to enable fast and accurate computations, this paper introduces two general multi-stage neural operator learning frameworks. The first, Deep Collocation Neural Operator (DCNO), is a supervised approach that iteratively refines the operator approximation by learning residuals from input-output data pairs. The second, Deep Galerkin Neural Operator (DGNO), is an unsupervised framework applicable when the target operator can be represented by a PDE, leveraging the weak form of the PDE residual for training. Both methods progressively construct basis operators through multiple training stages to enrich the approximation space, leading to significantly improved accuracy over standard one-shot operator learning. We provide theoretical analysis for their approximation capabilities and implement them for learning convolutions. Extensive numerical experiments demonstrate that both DCNO and DGNO achieve high accuracy, approaching machine precision under single float for convolution problems, and offer substantial efficiency gains for numerous queries or parametric variations compared to traditional solvers. We also extend these frameworks to handle multi-input operator learning scenarios involving variations in both the density and kernel of a convolution.

---


### 127. [SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents](https://arxiv.org/abs/2608.18852)

**<font color=#1a73e8>作者：</font>** Qingyao Li, Wenxiang Jiao, Shuai Shao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent frameworks increasingly package procedural knowledge as skills: instruction files an agent reads on demand, while public libraries now hold thousands of them. Which skill to read has thus become a decision the policy itself makes in the middle of an episode, yet no existing signal trains it. We show that the default remedy, outcome-rewarded RL over the candidate slate, cannot teach it, for a structural reason we identify and name selector credit starvation: under a broadcast, sequence-level advantage, the few tokens that name the chosen skill carry a vanishing share of the loss, and the credit they inherit is increasingly wrong-signed as trajectories lengthen. A correct choice is punished whenever the execution after it fails, even though the choice itself is among the most valuable decisions in the trajectory. Auditing a completed run's own training artifacts confirms all three properties, each worsening monotonically with horizon. SkillGate removes the failure by construction: it partitions the token support into two disjoint credit channels, outcome credit reaching only execution tokens, and a separate action-local advantage reaching exactly the skill-naming tokens, positive only when a trajectory's single read is the correct one. On five agentic benchmarks under a 16-candidate slate, SkillGate lifts a 9B policy from 40.8% to 53.2% trial success, well ahead of the identical budget spent on outcome reward alone, while cutting exposure to misleading candidates by two thirds and reading fewer skills.

---


### 128. [RVLoss: Runoff Vote Loss for Self-Supervised LiDAR Scene Flow Estimation](https://arxiv.org/abs/2608.18864)

**<font color=#1a73e8>作者：</font>** Shiming Wang, Liangliang Nan, Julian Kooij 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR scene flow estimates point-wise motion between two consecutive scans, referred to as the source and target. Leading self-supervised methods typically minimize the Chamfer loss, the nearest neighbor distance between the flow-compensated source and the target. However, nearest-neighbor search does not enforce motion rigidity, often leading to inconsistent flows within object instances. Existing approaches address this issue with additional regularization terms, but flow consistency among points remains limited, especially for large objects. We propose RVLoss, a self-supervised loss that incorporates motion rigidity by design through a runoff vote mechanism. Our key observation is that the point-wise motion, calculated from nearest neighbor search, can often be grouped into a small set of dominant flow candidates by voting (top-k voting). Furthermore, when compensating the source by these candidates, the flow that best represents the underlying rigid motion often yields the highest consensus after a second voting (top-1 voting). Based on this insight, we incorporate the two-stage runoff vote into loss design and create cluster-wise rigid flows and free-form flows as pseudo-labels for self-supervised learning. RVLoss can be seamlessly integrated into existing feedforward architectures. Experiments on the Argoverse2 2026 Challenge show that models trained with RVLoss achieve state-of-the-art performance among self-supervised approaches, outperforming baseline models trained with alternative loss designs by 20%. Moreover, cross-dataset evaluations demonstrate consistent performance improvements across four additional datasets. Code will be released upon acceptance.

---


### 129. [CauSec: Unboxing the Causal Drivers of Static Vulnerability Analysis Performance](https://arxiv.org/abs/2608.18876)

**<font color=#1a73e8>作者：</font>** Md Akram Khan, Daniel Rodriguez-Cardenas, Alejandro Velasco Dimate 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static Application Security Testing (SAST) tools are widely used in both industry and academia. Such tools often make design choices that sacrifice detection to achieve higher performance, i.e., increased precision, decreased runtime, or increased scalability. These design choices rely on certain assumptions regarding the target code or the analysis technique itself. Hence, the assumptions directly impact the detection outcome through the design choices they influence. This motivates a key question: do the sacrifices in the detection capabilities actually help tools achieve the expected performance gains? That is, are the underlying assumptions valid?
This paper seeks to address this question by relying on a key observation that the assumptions made by these tools are generally of a causal nature. We propose CAUSEC, a causal analysis framework that makes SAST assumptions testable and explains why the performance changes given certain assumptions, beyond simple correlations. CAUSEC formalizes the assumptions of the SAST tool into the abstraction of a security assumption and combines assumption-driven causal modeling with effect estimation and validation to test its validity and investigate the factors affecting it. To understand what security assumptions generally entail, we perform a systematic literature review of SASTs that detect crypto-API misuse, leading to the discovery and qualitative analysis of 57 assumptions. We then demonstrate the utility and robustness of CAUSEC by testing a popular assumption in four highly relevant tools, using a manually labeled ground truth dataset consisting of 57,038 alerts. Our analysis leads to several key findings that represent insights regarding assumptions and causal effects, which we distill into 3 takeaways for future work.

---


### 130. [Graph-Based Approaches to Learning Epileptogenic Zone Localization Using Stereo-EEG Recordings](https://arxiv.org/abs/2608.18887)

**<font color=#1a73e8>作者：</font>** Daniel Wendelken, Brian Ervin, Ravindra Arya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The epileptogenic zone (EZ) is the brain region that generates seizures in an individual, and is the target of epilepsy surgery. Localizing the EZ from stereo-EEG (sEEG) recordings supports surgical planning, but manual interpretation is time-consuming and focuses on seizure recordings. Graphical learning models of resting-state functional connectivity among the recorded brain regions are an attractive alternative, but depend crucially on the network topology chosen for the model.
We present a controlled study of graph-based models to explore how graph topology affects EZ localization from resting-state sEEG in 40 patients. Using the same simple learnable model and leave-one-patient-out evaluation, we compare dense graphs, anatomy- and geometry-informed priors, budgeted sparsification methods, and learned sparsification, including the proposed Region-Bridge-$c$ topology. To compare graph constructions fairly, we control the number of incoming edges per node and vary graph sparsity.
At $\approx 30\%$ edge retention, Region-Bridge-$c$ achieves the highest observed mean PR-AUC ($0.371\pm0.015$; ROC-AUC $0.743\pm0.010$) while using $\approx 69\%$ fewer edges than Dense (PR-AUC $0.349\pm0.014$). Spatial-$k$ is competitive, whereas random pruning requires near-dense retention. Learned sparsification benefits from anatomical node metadata but, on average, does not surpass the best fixed prior. Across all topologies, the best choice varies by patient. These results suggest that graph construction should be evaluated explicitly rather than treated as fixed preprocessing.

---


### 131. [Syntactic Simplification of OWL Class Expressions](https://arxiv.org/abs/2608.18899)

**<font color=#1a73e8>作者：</font>** Alkid Baci, N'Dah Jean Kouagou, Caglar Demir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Class expression learning often produces complex OWL class expressions that are difficult to interpret and reason over. However, by following theoretically grounded simplification principles, this complexity can be reduced. In this paper, we propose Class Expression Simplifier (CES), a novel algorithm for the syntactic simplification of class expressions in Description Logics (DL). CES aims to preserve formal semantics while reducing representational complexity. It systematically applies rewriting rules to eliminate redundancies and identify simpler yet equivalent expressions, thereby producing more compact and human-readable representations without altering logical entailments. We evaluate the effectiveness of CES on class expressions learned from two medium-sized ontologies, demonstrating measurable improvements in reasoning efficiency and reductions in verbosity. This work contributes to the broader goal of making ontology-driven applications more accessible, maintainable, and scalable, with direct implications for knowledge graph construction, semantic search, and Web-scale reasoning. CES is implemented within the open-source Python framework OWLAPY and is publicly available.

---


### 132. [\textsc{TestifAI}: Tomography-Based Testing for Deep Learning Systems](https://arxiv.org/abs/2608.18900)

**<font color=#1a73e8>作者：</font>** Arooj Arif, Tobias Hartung, Elena Botoeva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems are increasingly deployed in safety-critical application domains (e.g., autonomous driving), associated risks increase too. Deep learning models underlying modern AI systems, therefore, must undergo thorough testing to ensure their correct behaviour. A single robustness test involves thousands of inferences to empirically verify if a model's outputs remain stable under a bounded perturbation of its inputs. However, existing testing frameworks lack the means to systematically explore and summarise robustness across a combinatorial space of perturbations.
We propose TestifAI, a deep learning testing framework for efficient and accurate estimation of robustness against combinations of perturbations. TestifAI enables users to specify operational conditions as structured spaces of semantic input perturbations (e.g., image blur, brightness and zoom) and discrete severity levels (e.g., low, medium and high). Users can query model robustness for any combination (e.g., "low blur, high brightness, and medium zoom"). To achieve efficiency and accuracy, TestifAI introduces partial model tomography, a novel approach to reconstructing model behaviour in a multi-perturbation space from tests that apply only a small number of perturbations (lower-order projections). To estimate robustness against at least three perturbations, TestifAI trains an auxiliary model on the results of tests involving up to two perturbations only, avoiding execution of an exponential number of tests. Our experiments on five image and language classification tasks show that TestifAI can predict higher-order (3 and 4 perturbations) test outcomes from low-order (1 and 2 perturbations) observations with an aggregate robustness estimation error of less than 7%, while reducing the number of inferences by 60-80%.

---


### 133. [A FEM-Based Surrogate Modelling and Optimization Framework for Physics-Constrained Electromagnetic Coil Design](https://arxiv.org/abs/2608.18903)

**<font color=#1a73e8>作者：</font>** Yucheng Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work evaluates surrogate-assisted optimization of a seven-parameter current-excited coil--core benchmark subject to geometric, manufacturing, and separate core and copper mass constraints. A Python--MPh--COMSOL workflow couples a two-dimensional axisymmetric finite-element method (FEM) model to a Matern 5/2 Gaussian-process (GP) probabilistic surrogate. Here, physics-constrained denotes a design problem evaluated by a governing-equation FEM model and restricted by explicit physical, geometric, manufacturing, and material-allocation constraints; it does not denote a physics-informed GP architecture. Sequential Bayesian optimization (BO) ranks candidates using expected improvement (EI), and every reported incumbent is verified by FEM. Five paired runs show that optimizer ranking depends on the available FEM-evaluation budget: EI--BO improves rapidly at small continuation budgets, COBYLA is stronger at the earliest checkpoint, and BOBYQA attains the highest mean terminal response. A retrospective finite-pool study further finds no robust endpoint advantage of EI over posterior-mean ranking on this smooth response surface. The broader result is that early progress, terminal response, information use, and wall-clock cost can favor different methods in simulation-driven design. A selected-design check at a common total current preserves the observed BOBYQA--COBYLA--EI-BO ordering. The conclusions nevertheless remain conditional on this axisymmetric benchmark and do not establish a fixed-current optimum, fixed-power performance, or electrical-efficiency superiority.

---


### 134. [Learning-State-Aware Dynamic Generative Data Augmentation on Small-Scale Datasets](https://arxiv.org/abs/2608.18907)

**<font color=#1a73e8>作者：</font>** Ting Xiang, Chenxi Deng, Jinhui Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small-scale image classification is often limited by the scarcity of training data. Generative data augmentation (GDA) based on pretrained generative models has emerged as an effective solution. However, existing methods rely on task-agnostic augmentation strategies that overlook downstream model needs. Although recent dynamic GDA methods incorporate model feedback to guide augmentation, they still struggle to reliably determine sample-specific augmentation strengths and adapt augmentation strategies to different image regions while balancing image diversity and class semantics.
To address these issues, we propose learning-state-aware dynamic generative data augmentation (LSADA). Specifically, LSADA constructs a learning state for each sample based on its current loss and loss-decrease rate, which is then mapped to a sample-specific augmentation strength. Furthermore, LSADA introduces a decoupled data augmentation and diffusion fusion strategy that applies strength-controlled transformations to class-relevant regions and generates diverse class-irrelevant regions, progressively fusing them to improve image diversity while preserving class semantics. Experiments on nine public datasets show that LSADA outperforms the existing SOTA dynamic GDA method by an average of 4.5% on six natural image datasets and 2.5% on three medical image datasets.

---


### 135. [On the Slow Convergence to Trivial Solutions of Algorithms for Hard Optimization Problems](https://arxiv.org/abs/2608.18910)

**<font color=#1a73e8>作者：</font>** Ali Hussaini Umar, Jean Barbier, Matthieu Jonckheere 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hard combinatorial optimization problems, many of which are NP-hard, present fundamental algorithmic challenges. Average-case analysis on random instances has emerged as a powerful framework for understanding typical algorithmic performance beyond worst-case guarantees. A substantial body of work has established negative results: for sufficiently hard instances (often controlled by the underlying graph connectivity/constraints density), no known polynomial-time algorithm can significantly outperform naive heuristics in the double asymptotic limit where both problem size and constraints density tend to infinity. We revisit this picture by studying the finite-size behavior of some optimization algorithms across easy, intermediate, and hard regimes. Through rigorous analysis of large-graph asymptotics combined with numerical experiments on canonical problems (maximum independent set and maximum $K$-SAT), we demonstrate that while algorithms do eventually converge to theoretically predicted bounds, this convergence can be remarkably slow. In the intermediate regime where instances are already highly constrained, local algorithms achieve solutions substantially better than their predicted performance in the high-constraint-density limit. This gap between finite-regime and asymptotic behavior has important practical implications: sophisticated algorithmic design remains crucial even when asymptotic theory predicts inevitable failure.

---


### 136. [Simple, Safe, and Overlooked: Reclaiming Sustainable Domain Generalization with Statistical Color Matching](https://arxiv.org/abs/2608.18915)

**<font color=#1a73e8>作者：</font>** Sebastian Doerrich, Francesco Di Salvo, Shyam Nandan Rai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hardware shifts, color variations, and changing patient characteristics between development and deployment routinely break trained medical image classifiers. Existing remedies fall short: standard color jittering provides insufficient diversity, while deep generative style transfer algorithms hallucinate features, destroy clinically relevant structures, and waste massive compute resources. To address this, we revisit classical statistical color matching and repurpose it as Colorist, a highly efficient data augmentation strategy that applies global mean-standard deviation matching directly in the RGB color space. We demonstrate that this training-free, fully interpretable approach safely generates structurally intact domain variations, outperforming deep generative models in structural fidelity and color alignment. Across out-of-distribution histopathology, peripheral blood, dermatology, and retinal datasets, it improves balanced accuracy by up to +9% over state-of-the-art domain generalization regularizers and by +13% over an unaugmented baseline. Moreover, by avoiding neural networks in the augmentation loop, Colorist preserves anatomical structure, minimizes carbon footprint, and integrates seamlessly into standard dataloaders. Together, these findings establish statistical matching as a safe, interpretable, yet overlooked alternative to deep architectures for clinical robustness. Source code is available at this https URL.

---


### 137. [Score the Algebra, Not the Span: Dimension Reduction for Transfer Operator Models of Dynamical Systems](https://arxiv.org/abs/2608.18918)

**<font color=#1a73e8>作者：</font>** Mark Kozdoba, Shie Mannor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimension reduction for dynamical systems is standard practice, and the standard route is spectral: model the transfer (Koopman) operator by its leading modes. We show that on systems assembled from several weakly interacting components --- a structure common in physical and biological settings --- this may either require an exponential number of modes, or drop an entire component: the component is absent from the model rather than modeled coarsely, and no function of it can be predicted at any accuracy. We call this linear masking.
The cause is that a rank-based model pays one coordinate per mode. We propose to score instead the $\sigma$-algebra the coordinates generate, so that products and powers come free and a component's cost is governed only by its generators rather than by all its interactions. The criterion is a $\chi^2$-divergence between the embedded present and future, and it carries a budget guarantee: twice the intrinsic dimension of the dynamics is enough coordinates for an embedding whose algebra carries the operator's entire spectrum, with its full infinite rank.
In variational form the criterion admits off-the-shelf estimators, and restricting its critic to the bilinear class returns the VAMP score on the span, so rank-based methods are one end of the same family. We demonstrate the proposed objective on a composite of published benchmark systems. We exhibit examples where the rank-based methods completely miss the masked components at all ranks $k<100$, while ten algebra coordinates recover all of them. In addition, the resulting algebra representation supports predicting the masked components from few labels, while direct regression from the high-dimensional observation or from the VAMP features fail.

---


### 138. [Lost in Aggregation: How Benchmarks Overlook Irreplaceable Model Strengths](https://arxiv.org/abs/2608.18919)

**<font color=#1a73e8>作者：</font>** Andrej Tschalzev, Stefan Lüdtke, Heiner Stuckenschmidt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular machine learning benchmarks typically summarize performance by averaging scores, ranks, or pairwise wins across datasets. Such aggregates are useful for selecting robust default models, but they can obscure a different question: which models are necessary to attain peak performance on particular datasets? We argue that benchmark evaluation should also consider the data-centric peak performance frontier, defined by the best statistically supported performance achieved on each dataset. From this perspective, a model may be irreplaceable, sufficient, redundant, or fallible depending on where it lies on the frontier relative to other models. Applying this framework to the TabArena benchmark, we find that common aggregation metrics are highly correlated and largely measure consistency and avoiding failures, while being much less aligned with dataset-level irreplaceability. Consequently, models performing decently across datasets without ever being the best choice are rewarded while models with unique dataset-specific strengths appear mediocre under aggregation. Hence, benchmark progress should be measured not only by improvements on aggregation metrics but also by whether new models expand the set of attainable peak performances across datasets.

---


### 139. [Transportable Causal Effect Estimation across Networks under Interference](https://arxiv.org/abs/2608.18932)

**<font color=#1a73e8>作者：</font>** Xiaojing Du, Jiuyong Li, Lin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating causal effects under network interference typically assumes that the network used for training and the network used for deployment coincide. In practice, an intervention is run on one population while the question of interest concerns a different population, and the two generally differ in topology, node-covariate composition, and spillover pathways. Transporting a causal effect across networks is therefore a data-fusion problem that no existing algorithm solves. We employ a selection diagram, extended to the network setting so that covariate shift and structural network shift enter as separate selectors, and derive from it a transport formula for the direct, spillover, and total effects in the deployment population. Each formula makes explicit which interventional mechanism is assumed invariant and which observational distribution must be reweighted. We then turn the formulas into TranCE (Transported Causal Effects), a doubly-robust algorithm combining an interventional outcome model, a domain density-ratio correction, and cross-fitted inference. Extensive experiments on two semi-synthetic benchmarks derived from real-world social networks and on a fully real weather-insurance field experiment, where the transported effects are checked against held-out randomized estimates, confirm the effectiveness of our approach. Our findings have the potential to improve intervention strategies in networked systems, particularly in social networks and public health.

---


### 140. [Institutional Books - Visual Elements: An open-source pipeline for extracting, classifying, deduplicating, and captioning visual elements from digital book collections](https://arxiv.org/abs/2608.18957)

**<font color=#1a73e8>作者：</font>** Jimmy Mendez, Matteo Cargnelutti, David Lowry-Duda 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Historical book collections contain rich visual elements - such as illustrations, photographs, engravings, and decorative art - that are frequently under-explored in large-scale digitization projects. While Optical Character Recognition (OCR) has standardized the extraction of textual content, these visual components offer a layer of nuance and context that remains largely untapped by automated text extraction workflows. This technical report introduces Institutional Books - Visual Elements, an open-source end-to-end pipeline for detecting, classifying, deduplicating, and captioning visual elements from historical book collections. Alongside this pipeline, we release an initial dataset of 22.6 million visual elements extracted from the 983,004 scanned volumes that comprise the Institutional Books: Harvard Library dataset. This work contributes to ongoing, community-wide efforts to enable new use cases for digitized library collections through computational access, from artificial intelligence model training to digital humanities research.

---


### 141. [Who Can Make the Action Happen? An Authority-Decomposition Framework for High-Risk Automated Systems](https://arxiv.org/abs/2608.18965)

**<font color=#1a73e8>作者：</font>** Mengting Wu, Lin Wang, Yong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> High-risk automated systems distribute control across services, credentials, protected components, and lifecycle mechanisms. Labels such as authorized, approved, privileged, or protected therefore do not answer a basic causal question: which actors can actually make a consequential action occur? This paper provides an action-relative method for deriving which trust-domain coalitions are sufficient to cause protected execution, defined as the occurrence of a designated protected state transition. The framework models components, powers, resources, boundaries, and alternative realization structures; includes update, recovery, override, disablement, and alternative invocation; and separates causal control over execution from control over the authoritative account of an operation. It derives inclusion-minimal sufficient coalitions and tests whether claimed execution boundaries remain independent of designated upstream domains. Cross-domain analytical cases illustrate the method. In a split-control, release-intended, open-state, source-bounded Havenlon protocol model, the ordinary witness requires five trust domains, while certificate replacement yields a three-domain inclusion-minimal known requirement set among source-enumerated protocol witnesses; the Linux domain remains insufficient for the complete transition. Deployed global non-bypassability and boundary-bound veto coverage remain unresolved. The framework is a conceptual and analytical tool. It does not certify implementations, establish deployment security, guarantee complete discovery of hidden powers, or define evidence-verification semantics.

---


### 142. [Frozen DINO Localizes Image Edits Without a Localizer](https://arxiv.org/abs/2608.18968)

**<font color=#1a73e8>作者：</font>** Zane Kumar, Vishal Jain, Bernhard Kainz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Localized image edits can change a photograph's meaning while leaving most of it authentic, so forensic analysis must identify where an edit occurred. We show that patch-level perturbation responses from frozen DINO encoders are themselves localization maps. Training-free Localization of AI-image Edits from patch-token Drift (TRAIL) applies one global Haar perturbation and maps cosine drift between corresponding patch tokens. On 80 source-disjoint CocoGlide test images, TRAIL reaches .903 patch AUROC versus .912 for the mask-supervised Detective SAM; fixed-threshold Dice is .619 versus .709, while an oracle threshold raises TRAIL to .790. Transferred unchanged to Poisson image interpolation, TRAIL reaches .855 AUROC versus .864, showing that the cue persists without a generator. Across sixteen DINO encoders, the best block lies at normalized depth .80-.94. Global context matters: AUROC falls from .903 globally to .857 for local-in-canvas perturbations and .735 for independently encoded crops. Frozen DINO patch tokens therefore contain a strong late-layer localization signal whose visibility depends on the perturbation and preserved context. Code: this https URL.

---


### 143. [Fuzzy Accuracy Compensates for Label Subjectivity in Classification of Skin Tone Using Wearable Photoplethysmography Signals](https://arxiv.org/abs/2608.18969)

**<font color=#1a73e8>作者：</font>** Padmini Krishnadas, Urs Hackstein, Alen Bosnjakovic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of classification of skin tone using photoplethysmography (PPG) signals with labels of the ordinal six-class Fitzpatrick skin tones. A typical accuracy for this task is a poor 40-55 %. However, the labels are subjectively determined by comparing the skin with a colour chart, and hence contain widespread small-scale inaccuracies. By working with a "fuzzy accuracy", which deems a prediction of skin tone class to be correct if its difference from the labelled class is not greater than one, much higher accuracy is obtained which provides more convincing evidence that skin tone can be accurately predicted from PPG signals. Three machine learning approaches were used, namely deep learning or tree-based approaches on raw PPG signals, deep learning on image representations of the signals generated by the Symmetric Projection Attractor Reconstruction (SPAR) method, and machine learning on features extracted from the signals. The first method also employed a fuzzy version of the cross entropy loss function, which gave the best results. Tree-based models on raw signals give accuracies up to 55 % and higher fuzzy accuracies up to 96 %, while deep learning models on the SPAR images obtained lower results of 44 % accuracy and 85 % fuzzy accuracy. The machine learning on PPG features gave similar results to the SPAR method with accuracy of 42 % and fuzzy accuracy of 87 %. We have shown that classification of skin tone using PPG signals is possible with high fuzzy accuracy which implies that our modelling approach enables accurate prediction of skin tone class within at most one class of the observer's choice of class, from which we conclude that PPG signals are affected by skin tone in a discernible way.

---


### 144. [Institutional Newspapers Pipeline: Deriving billions of high quality tokens from historical newspapers](https://arxiv.org/abs/2608.18972)

**<font color=#1a73e8>作者：</font>** Matteo Cargnelutti, Catherine Brobston, Eben English 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Historical newspapers are an abundant record of public life, but their dense, irregular and sometimes noisy layouts make computational access to these materials both challenging and limited. We present the Institutional Newspapers Pipeline, a modular system we jointly designed with Boston Public Library to extract high-quality, structured datasets from historical newspaper scans. It was architected so that each step remains interpretable and customizable, and so that the pipeline as a whole remains computationally frugal enough to run on workstation-level hardware. The pipeline runs each scan through a multi-step process: it segments scans into individual type-agnostic crops and performs OCR on each resulting segment before then performing text analysis, type classification, reading order detection, named entities recognition, subject classification, language detection, and pre-computed embeddings generation on every crop. We ran this pipeline against a portion of Boston Public Library's holdings and released the results as an open dataset. The optical character recognition (OCR) output represents 16.3 billion o200k_base tokens across 83.1 million individual crops, extracted from 1,473,635 public domain newspaper scans published between 1795 and 1930. This report describes our methods for each processing step, the small models we trained, as well as the evaluation results and dataset-scale measurements we collected in the process. It accompanies the release of the pipeline, models, and dataset. We position this work as a substantial step towards unlocking high-quality data from tens of millions of newspaper scans.

---


### 145. [Catastrophic Learning: A New Attack Vector on Continual Learning Networks](https://arxiv.org/abs/2608.18976)

**<font color=#1a73e8>作者：</font>** Benedikt Kluss, Niklas Bunzel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Continual Learning (CL) enables deep learning models to iteratively learn from a stream of data without forgetting prior knowledge. Existing adversarial research on CL primarily aims to re-enable catastrophic forgetting, attacking stability and reducing availability. We identify a novel security flaw: data manipulated by an attacker can reduce the learnability of current or upcoming iterations. We term such manipulations learning blockers, as they attack the plasticity of CL algorithms. They are particularly harmful because they are difficult to detect during training of the current iteration, since they can target iterations whose data the model has not yet encountered. When learning blockers additionally induce catastrophic forgetting, the resulting overall degradation is what we call catastrophic learning. We formalize this scenario, define a threat model and propose six attack strategies: Label-Exchange, Tensor-Exchange, Attraction-Coincident, Attraction-Preceding, Repulsion-Coincident, and Repulsion-Preceding. The Attraction variants minimize the loss between the poisoned and the victim iteration label, pulling their representations together in feature space; the Repulsion variants maximize this loss, pushing them apart so stability mechanisms resist the required parameter shift. In the Coincident variants, the poisoned and the victim iteration coincide, using a clean reference iteration only as a label source; in the Preceding variants, the poisoned iteration precedes the victim, leaving it unlearnable due to distorted representations. We evaluate on MNIST and Split-CIFAR10 against three CL strategies - DER, ER-ACE, and iCaRL - across more than 4,480 simulations. Our results demonstrate a strong vulnerability: an adversary can selectively impede plasticity to hinder the acquisition of new knowledge, while promoting loss of prior knowledge, inducing a catastrophic learning scenario.

---


### 146. [When Simplicity Wins: Bottleneck-Aware Context Modeling for Lightweight Semantic Segmentation](https://arxiv.org/abs/2608.18979)

**<font color=#1a73e8>作者：</font>** Mian Muhammad Naeem Abid, Nancy Mehta, Zongwei Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation demands a careful balance between accuracy, efficiency, and scalability, which remains difficult to achieve for high-resolution imagery. Convolutional networks effectively model local patterns but struggle with long-range dependencies, whereas Vision Transformers capture global context at a high computational cost. While recent work largely focuses on encoder design, the bottleneck stage, central to contextual aggregation and information flow, has been relatively overlooked. We propose SiConMo, a lightweight yet effective framework, implemented in two variants: an RGB-only model (SiConMo) and a GME-enhanced variant (SiConMo$_\dagger$). We show that simplicity arises from a key design principle: at very low computational budgets, the bottleneck is the most efficient stage to integrate local and global context. SiConMo integrates three complementary components: a Token Pyramid Extraction Module for hierarchical multi-scale representation, a Transformer-Branched Depthwise Convolution block for bottleneck-aware context modeling, and a Feature Merging Module that preserves spatial structure while enhancing semantic consistency. Extensive experiments on ADE20K, PASCAL Context, Cityscapes, and COCO-Stuff demonstrate that SiConMo achieves a state-of-the-art accuracy-efficiency trade-off among lightweight semantic segmentation models, highlighting simplicity as a powerful design principle.

---


### 147. [X-LMC: Cross-View Spatiotemporal Collateral Circulation Scoring from DSA](https://arxiv.org/abs/2608.18986)

**<font color=#1a73e8>作者：</font>** Maedeh Hafezi Moghadas, Hakim Baazaoui, Lukas Bastian Otto 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital subtraction angiography (DSA) is the reference standard for leptomeningeal collateral (LMC) assessment, providing critical prognostic insights to guide secondary treatment strategies, neurorehabilitation planning, and retrospective stroke research. However, clinical LMC grading via the ASITN/SIR scale relies on manual, highly variable visual inspection. We introduce X-LMC, a spatiotemporal framework for automated collateral scoring from time-resolved biplane DSA. The proposed architecture encodes spatial frame representations through a DINOv2 backbone, fuses orthogonal projections via a token-level cross-view attention module, and models representations of contrast bolus dynamics using a recurrent network architecture. We evaluate our framework on a multicenter dataset of 134 patients with M1-segment occlusions. In a 5-fold cross-validation setting, X-LMC yields higher point estimates than static architectures and spatiotemporal baselines adapted from related angiographic tasks, achieving a Quadratic Weighted Kappa (QWK) of 0.398 (vs. 0.322) and a dichotomized macro-F1 score of 0.711 (vs. 0.663) against the best-performing baseline. X-LMC performance also aligns with the observed clinical inter-rater agreement (QWK: 0.314). As the first DSA study attempting to automate LMC scoring, we demonstrate that multi-view temporal deep learning can capture collateral-specific contrast kinetics. Ultimately, these benchmarks delineate the clinical ambiguities and achievable performance boundaries of automated ASITN/SIR grading, establishing a reproducible foundation for objective hemodynamic phenotyping in stroke cohorts. Code is available at this https URL.

---


### 148. [A 12-Step Process for Industrial Internet of Things (IIoT) Forensics](https://arxiv.org/abs/2608.18991)

**<font color=#1a73e8>作者：</font>** Victor Kebande  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing deployment of the Industrial Internet of Things (IIoT) in critical infrastructure sectors like manufacturing, healthcare, and transportation has shown new challenges for Digital Forensics (DF). Traditional DF methodologies are not well equipped to handle the complexity, scale, and heterogeneity of IIoT environments. This paper introduces a comprehensive Twelve-Step Process (TSP) tailored specifically for IIoT incidents, addressing the need for effective investigation and Potential Digital Evidence (PDE) handling in such dynamic environments in DF. We begin by exploring the importance of IIoT and its role in industrial ecosystems, followed by an examination of existing DF challenges. Each step of the process, from forensic readiness to investigation closure, is designed to ensure robust PDE collection, analysis, and legal compliance to increase chances of admissibility from a DF scenario

---


### 149. [GrabVG: Graph-Attentive Binding for Visual Grounding in UAV Imagery](https://arxiv.org/abs/2608.18996)

**<font color=#1a73e8>作者：</font>** Chaowei Wang, Yan Di, Jingjun Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding in Unmanned Aerial Vehicle (UAV) imagery aims to localize a target object in complex bird's-eye-view scenes according to a natural language description. However, the abundance of small, densely distributed, and visually similar objects creates high visual redundancy, while repetitive local configurations give rise to strong topological ambiguity. Existing approaches mainly focus on visual--language feature alignment or dense contextual interaction, yet they struggle to distinguish subtle inter-instance differences and effectively exploit spatial topological structures, leading to inaccurate grounding in highly crowded scenarios. To address these challenges, we propose $\textbf{GrabVG}$, a novel visual grounding framework inspired by human visual search. GrabVG explicitly decomposes grounding into two sequential stages: $\textit{preattentive hypothesis search}$ and $\textit{graph-attentive feature binding}$. Specifically, we first generate a compact set of reliable object hypotheses through distillation-guided proposal induction and text-aware hypothesis filtering, substantially reducing background distractions and semantic mismatches. These hypotheses are then organized into a sparse graph, where language-guided intra-instance visual cues and inter-instance topological relationships are jointly bound and propagated via graph attention, enabling efficient spatial reasoning and accurate target localization. Extensive experiments on AerialVG and AerialSense show that GrabVG achieves a favorable accuracy--speed trade-off, reaching 67.31$\%$ and 80.34$\%$ Acc@0.5 and outperforming the corresponding baselines by 10.55 and 8.76 percentage points, respectively.

---


### 150. [Structure, Association, and Decision Value: Representation-Based Difficulty Estimation for Adaptive Inference in African-Language NLI](https://arxiv.org/abs/2608.19003)

**<font color=#1a73e8>作者：</font>** Toheeb Ogunade  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We ask whether internal representation statistics can provide useful example-level difficulty signals for adaptive inference in multilingual African NLP, and find that they cannot in this setting. Studying natural language inference across 15 African languages with frozen off-the-shelf checkpoints, we report four results. First, AfriXNLI's English configuration shares 1,047 of its 1,050 examples verbatim with XNLI evaluation data, and one widely used NLI checkpoint scores 1.000 on that test split, consistent with XNLI test exposure. Because AfriXNLI is derived from XNLI, its English, French and Swahili configurations cannot serve as clean evaluations for XNLI-trained models. Second, parameter count does not reliably order capability across African languages: our larger checkpoint is better in seven languages and worse in eight, with no significant aggregate difference. Third, across three multilingual representation spaces, angular dispersion is consistently more language-determined than effective rank, so pooled correlations can inflate one and mask the other. Fourth, the association that survives language control depends on the target: effective rank predicts probability gain from escalation but not whether escalation changes the prediction, while cheap-model confidence shows the opposite pattern; the two targets correlate at only 0.655. Under the tested models, signals, and compute budgets, no evaluated signal makes adaptive routing preferable to always-expensive inference, although an oracle exceeds it by 11 accuracy points at 60% of the compute. Our central methodological finding is that a representation statistic can be statistically significant for one notion of computational benefit while being irrelevant to another, and therefore be a poor decision variable.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-184](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
