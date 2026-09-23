# 📦 其他研究 | 2026年09月24日

> 本类共 **275** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-275**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-275**

---

### 251. [Bespoke: Generating MOOC-Quality Industry-Personalized Lecture Videos at Scale](https://arxiv.org/abs/2609.26540)

**<font color=#1a73e8>作者：</font>** Romain Puech, Dewang Kumar Agarwal, Antonio Santamaría Escobar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Lifelong learners from different industries often watch the same recorded lecture, even when they will apply the material in different workplaces. We present Bespoke, a system that takes the transcript of an existing lecture and generates a new video customized to a target industry and duration, with new slides, narration, and charts. From 31 graduate lectures in analytics, machine learning, and optimization, we generated 209 videos for these three industries, plus a generic-audience version of each lecture. Twenty-five experts in the corresponding domains rated 92 videos on a five-point rubric. They judged 87% at or above the rubric midpoint corresponding to ``a standard MOOC lecture's quality'' (mean overall score 3.42 out of 5; 48% scored 4 or above). Overall quality was similar across industries, durations, and a 21-lecture held-out set unused while developing the system, at about \$0.22 API cost per minute of video.

---


### 252. [Latent Commonality Expectation-Maximisation for Box-supervised Tree Crown Instance Segmentation](https://arxiv.org/abs/2609.26549)

**<font color=#1a73e8>作者：</font>** Thomas Pitts, Kunqi Li, Bin Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Individual tree crown segmentation from aerial imagery underpins tree-level carbon accounting, biodiversity, and restoration monitoring at landscape scale. However, existing models are predominantly trained on dense canopy forest imagery and degrade in savannah and drylands, where tree crowns are sparse, of variable appearance, and underrepresented in annotated benchmarks. These models also typically depend on costly polygon annotations. We introduce LACE (LAtent Commonality Expectation-maximisation), a box-supervised instance segmentation model, evaluated on 0.1 m/px aerial RGB tree crown imagery. LACE uses a frozen DINOv3-web ViT-L/16 encoder, applied at four spatial offsets and interlaced into a denser feature grid, with a lightweight CenterNet-style detection head trained solely on bounding boxes. We use expectation-maximisation to separate recurring appearance, the "treeness", within bounding boxes from surroundings. On the OAM-TCD benchmark test set, LACE reaches a mask AP$_{50}$ of $0.663 \pm 0.001$ (3 seeds) trained on 900 box-annotated images and without mask annotations, above the 0.626 scored by Restor's released mask-supervised Mask R-CNN, which was trained on the full ~4.2k image set. On a sparse-canopy holdout set, mask AP$_{50}$ rises to $0.691$ versus $0.612$ for Detectree2, a mask-supervised baseline. On NeonTreeEvaluation, using the official evaluation code, LACE reaches $0.728 \pm 0.003$ F1@0.4 (5 seeds) from 23,424 hand-annotated RGB boxes alone, matching the authors' DeepForest model's published 0.719, using under 0.1% of its training annotations and none of its LiDAR-derived 30M-crown pretraining set. By leveraging frozen self-supervised features, LACE matches or surpasses fully-supervised specialist baselines from boxes alone, removing the need for polygon annotation in tree crown instance segmentation for sparse-canopy environments where labelled data is scarce.

---


### 253. [Neutral-Atom-based Quantum Optimization for Resource Allocation in NOMA Networks](https://arxiv.org/abs/2609.26556)

**<font color=#1a73e8>作者：</font>** Patatchona Keyela, Remon Polus, Soumaya Cherkaoui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In wireless communication networks, many resource optimization problems are nondeterministic polynomial-time hard (NP-hard) due to their combinatorial nature and high computational complexity. Recently, neutral-atom-based quantum computing has emerged as a promising platform for efficiently solving such problems by leveraging quantum superposition and entanglement. However, its application to wireless communication optimization problems remains largely unexplored. In this paper, we investigate the use of neutral-atom quantum platforms to solve the maximum access problem (MAP), formulated as a mixed-integer programming task that jointly considers admission control, user clustering, channel assignment, and power allocation in a non-orthogonal multiple access (NOMA)-enabled uplink network. To reduce the computational burden, the MAP is equivalently reformulated as a maximum independent set (MIS) problem in graph theory. This reformulation enables the use of the neutral atom platform based on Rydberg atom arrays, where the MIS problem is naturally encoded into the physical geometry and blockade constraints of the quantum system. Numerical results demonstrate the feasibility and potential of this approach for addressing large-scale wireless resource optimization problems.

---


### 254. [Quantum-Aided Active Device Detection in Energy-Harvesting Symbiotic Radio Networks](https://arxiv.org/abs/2609.26565)

**<font color=#1a73e8>作者：</font>** Remon Polus, Deemah Tashman, Soumaya Cherkaoui  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Massive connectivity in next-generation networks demands energy- and spectrum-efficient solutions for large-scale Internet of Things (IoT) deployments. Symbiotic radio (SR) enables passive IoT devices to communicate by backscattering existing cellular transmissions. A key challenge in uplink SR is active device detection (ADD), which directly affects decoding reliability, interference management, and system throughput. We propose an energy-harvesting code-domain non-orthogonal multiple access (NOMA)-SR system in which IoT devices harvest energy from ambient uplink signals and backscatter information using low-density spreading (LDS) codes. To reduce the complexity of ADD, Grover's quantum search algorithm is employed, providing a quadratic reduction in oracle-query complexity over exhaustive maximum-likelihood (ML) search. Numerical results show that the proposed approach closely approaches ML performance while substantially reducing the number of search iterations, demonstrating its potential for scalable ambient IoT systems.

---


### 255. [E3Sense: Head-Confined Multimodal Sensing of Learner Engagement](https://arxiv.org/abs/2609.26569)

**<font color=#1a73e8>作者：</font>** Sidharth Anupkrishnan, Itir Sayar, Jeongah Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Engagement-aware learning systems could provide hints or adjust pacing when learners struggle. Prior engagement sensing work distributes sensors across or outside the body rather than consolidating them at one site, or reduces engagement to shared affect or a single dimension (from behavioral, emotional, and cognitive engagement). We introduce E3Sense, a head-worn platform that co-locates electroencephalography, eye tracking, and electrodermal activity to personalize engagement measurement. During a lab study we collected 450 ratings of engagement levels on a five-level ordinal scale while participants watched educational videos. For fifteen held-out participants, E3Sense achieved a within-one-level prediction score of 75.0%, compared with 63.0% for always predicting the most common rating. In an exploratory analysis of 18 participants from the same study who defined engagement, conditioning on learners' definitions raised the same measure by 6.9 points, from 64.6% to 71.5%. Our work provides a proof-of-concept of a head-site, personalized multimodal sensing of engagement for adaptive educational interfaces.

---


### 256. [Radiomics--Foundation Fusion for Interpretable RCC Classification: Internal Benchmarking and Exploratory External Transfer](https://arxiv.org/abs/2609.26578)

**<font color=#1a73e8>作者：</font>** Yuan Liang, Fangyijie Wang, Kathleen M. Curran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate preoperative subtype classification of renal cell carcinoma (RCC) from contrast-enhanced CT remains clinically challenging because clear cell RCC (ccRCC) and non-clear cell RCC often show overlapping imaging appearances. This study evaluates whether foundation representations reduce reliance on handcrafted radiomics, or whether radiomics remains complementary for interpretable tumour characterisation. We compared radiomics, conventional CNN features, MedicalNet-pretrained features, MedVAE representations, and fusion variants for binary ccRCC classification on KiTS23, reporting area under the receiver operating characteristic curve (AUC) with bootstrap confidence intervals and average precision (AP) as a complementary class-imbalance-sensitive metric. We further assessed branch-removal ablation, TCGA/AIMI external transfer, and interpretability using radiomics permutation importance and gate-level analysis. Internally, 3D MedVAE gated fusion achieved the best performance, with an AUC of 82.7% and AP of 92.2%. On the external TCGA cohort, the same model achieved an AUC of 79.5% and AP of 98.9%, although specificity remains uncertain because only two external non-ccRCC cases were available. Gate analysis showed a radiomics-dominant fusion regime, suggesting that foundation representations acted as case-dependent refinement signals rather than replacements for structured tumour descriptors. These findings support radiomics as a complementary and clinically interpretable component of CT-based RCC characterisation in the foundation-model era.

---


### 257. [GTR: Gated Token Recurrence for Efficient Dense Prediction](https://arxiv.org/abs/2609.26590)

**<font color=#1a73e8>作者：</font>** Zhe Feng, Longfei Liu, Wei Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-attention-based vision backbones perform well on dense prediction, but the quadratic computational cost of global softmax attention limits their efficiency as image resolution increases. We introduce Gated Token Recurrence (GTR), a softmax-free recurrent vision backbone that combines gated linear attention, alternating spatial scan directions, and spatially enhanced SwiGLU blocks. GTR is distilled from a detection-specialized DINOv3 teacher using only final-layer patch-token alignment through a linear projection and squared $\ell_2$ loss, without masked-token prediction or intermediate-layer supervision. With Objects365 detector pre-training, GTR-L achieves 58.9 box AP on COCO \texttt{val2017} with 1.908\,ms median batch-one latency under compiled FP16 execution on an RTX~4090. The same backbone also transfers to instance segmentation, pose estimation, oriented detection, semantic segmentation, and monocular depth estimation. In an isolated kernel benchmark, our specialized chunkwise CUDA operator is $4.0\times$ faster than FLA v0.5.0 at 1.6K tokens on RTX~4090. TensorRT deployment on DRIVE AGX Thor achieves 2.282--8.769\,ms median batch-one latency across the evaluated models. These results show that recurrent token mixing can provide an efficient alternative to global softmax attention for high-resolution dense prediction and edge this http URL page: this https URL

---


### 258. [Towards Hierarchical GNNs for multi-grid power flow: generalization across operating scenarios](https://arxiv.org/abs/2609.26603)

**<font color=#1a73e8>作者：</font>** Carmine Delle Femine, Leire Garin Atxaga, Asier Diaz-Iglesias 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical latent communication improves the generalization of a multi-grid power-flow model to new operating scenarios. The module exchanges information through two reduced graphs within a GENCO-based corrective network. We compare Kron-derived transports, a same-anchor Quotient construction and a flat backbone in preliminary trainings of 200 epochs on three grid topologies, with three initialization seeds per model. Evaluation uses 200 newly generated, preselected scenarios per grid. On the training topologies, Kron reduces the macro family-balanced voltage error from 5.660 +- 0.899 to 0.851 +- 0.110: an 85.0% reduction relative to Flat GENCO and 31.0% relative to Quotient, which reaches 1.235 +- 0.225. Both hierarchical models outperform a per-bus mean fitted on training solutions on every training topology in all three seeds. These results demonstrate generalization across operating scenarios within the studied topologies, with one set of learned parameters shared across grids. Evaluation on two additional topologies distinguishes this achievement from cross-topology generalization: the current models do not yet outperform the fitted reference in that calibrated- transfer setting. This preprint presents the architecture and preliminary evidence for hierarchical communication as a component of multi-grid power-flow learning, with generalization to unseen topologies as the next development objective.

---


### 259. [MMAP: Multimodal Missing-Aware Pretraining for Longitudinal Alzheimer's Prediction](https://arxiv.org/abs/2609.26617)

**<font color=#1a73e8>作者：</font>** Fiona Kekwick, Matthew Baugh, Bernhard Kainz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical decision making heavily relies on predicting the disease progression trajectory by seeking to understand patient's health status which is characterised by multimodal medical data. AI holds great potential for learning useful representations from multimodal medical data to predict disease progression and aid clinical decision making. However, development of predictive AI models is constrained by missing modalities and incomplete tabular data frequently occurring in medical datasets. In addition, disease labels alone may only provide limited supervisory signals for learning representations from high-dimensional multimodal data. Here, we present MMAP, a novel Multimodal Missing-aware Alignment Pretraining method for learning image-tabular representations from incomplete data. An image encoder is pretrained with efficient sigmoid contrastive learning combined with generative reconstruction. A tabular encoder is built upon a tabular foundation model. A missing token generator enables the two encoders to take incomplete data as input, enabling the model to be robust against missing modalities, either with missing images or missing tabular data. We evaluate the clinical usefulness of the learnt multimodal representations on two challenging longitudinal clinical tasks for Alzheimer's disease: predicting disease stage conversion and predicting amyloid status. The proposed method outperforms strong multimodal and unimodal baselines.

---


### 260. [GeoComposer: Geometry-Grounded Photographic Composition Instruction](https://arxiv.org/abs/2609.26620)

**<font color=#1a73e8>作者：</font>** Shuangzhi Li, Qiaoqiao Jia, Xingxin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photographic composition aims to provide visual guidance for improving the framing, viewpoint, and spatial arrangement of an image. Early methods primarily rely on image cropping to enhance composition, which is restricted to the viewpoint and spatial arrangement of the input image. Recent methods have explored image understanding and editing to improve composition, but they mainly focus on instruction following and aesthetic quality, overlooking the importance of 3D scene geometry consistency for photographic composition. In this work, we propose GeoComposer, a novel geometry-grounded photographic composition framework that analyzes the composition of a given image to generate textual guidance and synthesizes a visual exemplar that enhances the composition of the given image. To promote geometry-grounded composition, we propose a geometry-aware representation learning mechanism that leverages geometric priors from a visual geometry foundation model to shape the intermediate representations of the composition editing model. This mechanism preserves both global structural relationships and local fine-grained correspondences for geometry-grounded composition. Furthermore, we propose a reinforcement learning strategy guided by a hybrid reward that jointly optimizes instruction following, aesthetic quality, and geometric consistency. This enables the model to generate visual exemplars that faithfully follow the composition instructions while remaining visually appealing and geometrically consistent. Extensive experiments show the superiority of our approach over state-of-the-art methods, highlighting its effectiveness in generating visually appealing and geometrically consistent composition.

---


### 261. [A Data-Interventional Framework for Auditing Privacy and Fairness in Generative Medical Imaging](https://arxiv.org/abs/2609.26623)

**<font color=#1a73e8>作者：</font>** Mischa Dombrowski, Bernhard Kainz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based synthetic data generation offers a promising route for sharing medical imaging data without releasing sensitive patient records. However, generative models face a fundamental tension between privacy and fairness: they may memorize rare training samples, leading to privacy risks, or fail to reproduce underrepresented features, resulting in unfair synthetic distributions. While prior work has largely focused on either memorization or fairness in isolation, their interaction remains insufficiently understood. In this work, we introduce a data-interventional framework to systematically analyze privacy and fairness in diffusion models. We discuss synthetic anatomical fingerprints (SAFs), rare and manually injected image features, as controlled probes to study whether models generalize sensitive attributes across identities, memorize training samples, or suppress rare signals entirely. Across multiple conditioning modalities, we observe a consistent behavior: models either forget these fingerprints or memorize the entire image in which they appear, but do not generalize them to novel images. To support large-scale auditing where explicit sample extraction is infeasible, we further introduce the indicator metric t', which estimates a model's susceptibility to memorization by exploiting the internal structure of the diffusion process. By comparing conditioning signals of varying surprisal, we reveal a clear relationship between conditioning rarity and memorization behavior. Highly surprising conditioning signals act as retrieval keys that amplify memorization, whereas low-surprisal conditioning signals systematically suppress rare features, even when these appear repeatedly in the training data. Our findings provide actionable insights and concrete mitigation strategies for safe and fair synthetic medical data sharing. Code is available at this https URL.

---


### 262. [Label-Efficient Learning for Ground-Based Sky-Image Classification: A Benchmark of Transfer Learning, Active Learning, and Pseudo-Labeling on GCD](https://arxiv.org/abs/2609.26631)

**<font color=#1a73e8>作者：</font>** Esther Bou Dagher, Viktoriya Bu-Dager, Boguslaw Zegarlinski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate ground-based cloud classification is important for atmospheric monitoring, solar-energy forecasting, aviation weather assessment, and climate observation systems. However, reliable sky-image annotation is time-consuming, especially when cloud types are visually similar or mixed. We study the label efficiency of deep learning for ground-based cloud classification using the Ground-based Cloud Dataset (GCD). Rather than proposing a new architecture, we benchmark three practical strategies under limited annotation budgets: supervised transfer learning, uncertainty-based active learning, and high-confidence pseudo-labeling. An ImageNet-pretrained ResNet50 is used as a common frozen backbone, with experiments repeated over five random seeds for label budgets from $1\%$ to $100\%$ of the training labels. Supervised transfer learning is already highly label-efficient: test accuracy increases from $0.635 \pm 0.018$ with $1\%$ labels to $0.730 \pm 0.002$ with $40\%$ labels, approaching the full-label result of $0.735 \pm 0.003$. Active learning and pseudo-labeling are competitive with supervised sampling and provide small improvements for some metrics and budgets, but neither gives a large or consistent aggregate gain. Diagnostic analyses show that accepted pseudo-labels are reliable, with accuracy from $0.946$ to $0.977$, but biased toward easier high-confidence sky-type groups. In contrast, uncertainty sampling preferentially queries visually challenging groups, including Mixed and the confusable Stratocumulus and Cumulonimbus groups, but these targeted acquisitions yield only modest gains. Overall, transfer learning substantially reduces annotation requirements for GCD, while simple active and semi-supervised strategies provide limited additional benefit over a strong supervised baseline.

---


### 263. [Knowledge Pull Requests for Continual Document Authoring](https://arxiv.org/abs/2609.26634)

**<font color=#1a73e8>作者：</font>** Alexander Martin, Benjamin Van Durme  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Knowledge Pull Requests (KPRs), a framework for continual document authoring that makes each change interpretable. Documents require ongoing revision as new knowledge surfaces from other sources, languages, or times, but existing approaches either edit with no account of what knowledge changed or regenerate from scratch. A KPR integrates new knowledge into a document by extracting claims, filtering and routing them to sections, and flagging conflicts with existing content, producing a ChangeLog that separates what knowledge changes (claim proposal) from how the text changes (document diff). We evaluate KPRs on revising Wikipedia across languages and updating query-driven reports on RAGTIME. KPRs integrate more information and better preserve existing content than rewriting from sources or regenerating from scratch, while adding the most information per token generated. A KPR-revised article also grounds question answering better than a frontier model with search, which does not surface knowledge documented only in other languages.

---


### 264. [Laryngeal Structure Segmentation in High-Speed Videoendoscopy Using Deep Learning](https://arxiv.org/abs/2609.26636)

**<font color=#1a73e8>作者：</font>** Sardar Nafis Bin Ali, Mohsen Zayernouri, Dimitar D. Deliyski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Laryngeal high-speed videoendoscopy (HSV) offers an effective means of observing the motion of different laryngeal structures along with vibratory behaviors of the vocal folds under various voicing conditions. Segmentation of laryngeal tissues enables analysis of different tissue structures and their dynamics, helping characterize the involvement of laryngeal muscles in voice production. Given the large number of HSV frames, automating this task is imperative. While deep learning-based methods have been implemented in previous studies to segment laryngeal structures, they have not been applied to HSV data during connected speech, which poses significant challenges due to excessive tissue movements and image quality limitations associated with fiberoptic image acquisition. The application of deep learning to connected speech data is critical for capturing nonstationary laryngeal behaviors and identifying anomalous patterns associated with voice disorders. The present study aims to address these gaps by training U-Net models to detect the aryepiglottic folds and arytenoid cartilages, vocal folds, epiglottis, and glottal area, using HSV data from both sustained vowel phonation and connected speech obtained from normophonic and disordered voices. Image pre-processing techniques, including noise removal and histogram equalization, were applied to improve the quality of the training HSV images and enhance network performance. Finally, to evaluate the accuracy and reliability of the networks, quantitative performance metrics were used alongside qualitative visual inspection of the test images. The high performance of the developed networks, with overall accuracies exceeding 95%, establishes their potential as reliable tools for automated laryngeal image analysis, quantitative characterization of laryngeal dynamics, and future detection of anomalous laryngeal behaviors in clinical settings.

---


### 265. [The Delegation Blind Spot: Auditing Product Decisions from Agent Choices](https://arxiv.org/abs/2609.26642)

**<font color=#1a73e8>作者：</font>** Shivam Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Successful agent execution need not identify which future product improvement its user would value. We present a decision-specific audit that maps a declared observation channel and product-value contrast to compatible intervals and witness populations. Its foundations are established identification and decision theory; the contribution is an executable measurement workflow and a controlled study of its limits. A frozen experiment makes 4,800 requests to two pinned model snapshots on shared synthetic tasks. All 36 conservative primary intervals remain unresolved despite different execution accuracy. An exploratory 2,400-call follow-up records supplied preferences and resolves three of nine comparisons per model. A deterministic extractor resolves seven of nine without model calls or calibration observations, exposing unnecessary uncertainty introduced by model-generated reports. A further 14,400 controlled multinomial simulations distinguish structural ambiguity from weak identification and finite calibration precision. We propose a source-labeled decision receipt and provide an offline viewer for inspecting the audit. These results motivate preserving decision-relevant structured input and diagnosing why a decision is unresolved before collecting more telemetry. The study contains no human participants or real customer outcomes. Full proofs, raw model provenance, controlled experiments, and reproducible analyses accompany the report.

---


### 266. [Longitudinal Retinal Vascular Remodeling in Myopic Children Treated with Orthokeratology or Defocus Lenses: A Two-Year Comparative Study](https://arxiv.org/abs/2609.26662)

**<font color=#1a73e8>作者：</font>** Zhihao Zhao, Yinzheng Zhao, Jie Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purposes: To characterize longitudinal retinal vascular changes in myopic children treated with orthokeratology (OK) or multifocal defocus lenses (Defocus) and to examine their association with axial elongation. Methods: In this retrospective cohort study, 43 myopic children underwent comprehensive clinical examination and fundus photography at baseline, 12 months, and 24 months. Axial length (AL) and spherical equivalent refraction (SER) were recorded at baseline, 6, 12, and 24 months. An automated segmentation model extracted vascular parameters, main vessel angle (MA), branching angle (BA), bifurcation edge angle (BEA), crossover point (COP), and terminal vessel count (TVC). Repeated-measures ANOVA assessed temporal changes. Pearson or Spearman correlations evaluated associations between AL and vascular metrics. Results: Over 24 months, the OK group exhibited significantly slower axial elongation than the Defocus group (0.214 mm and 0.522 mm, p < 0.01). In the OK group, MA and BA decreased modestly, BEA in arteries declined gradually, but COP and TVC remained relatively stable. The Defocus group demonstrated more pronounced decreases in MA and BA, an increase in BEA, and significant reductions in COP and TVC (p < 0.05). Correlation analysis revealed stronger associations between AL and vascular parameters, especially COP and TVC, in the Defocus group at all time points, whereas only BA and BEA correlated with AL in the OK group. Conclusions: OK lenses mitigate axial elongation and induce milder retinal vascular remodeling compared to Defocus lenses. Distinct temporal patterns of vascular metrics changes were observed between the two interventions, and correlate differentially with axial growth.

---


### 267. [A Spectral Theory of Grokking: Weight Decay induces Feature Learning](https://arxiv.org/abs/2609.26679)

**<font color=#1a73e8>作者：</font>** Lenz Pracher, Pascal de Jong, Oskar Lieshaus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In grokking an early fit to the training data separates from a much later improvement in generalization. During this delay, training can move from a fixed neural tangent kernel (NTK) regime to one in which task-relevant kernel eigendirections continue to evolve. We provide a quantitative theory for how this transition from lazy to rich learning can produce delayed generalization. For homogeneous networks trained with squared loss and $L_2$ weight decay, we show that a finite residual remains after memorization, with larger residual fractions in target components associated with smaller NTK eigenvalues. These residuals feed back into the dynamics of the NTK itself, and projecting the resulting dynamics onto task-relevant spectral directions yields a reduced system in which residual-driven kernel growth competes with weight decay. This system predicts that the grokking timescale is controlled by the product of learning rate and weight decay, that feature learning slows logarithmically near a critical decay above which task-aligned NTK structure can no longer support generalization, and that stronger decay can prevent fitting altogether. We test these predictions in modular addition. In a homogeneous MLP, task-aligned Fourier structure continues to emerge in the NTK after training accuracy has saturated, and an 84$\times$90-grid of trained networks across varying learning rate and weight decay recovers the predicted phase geometry and inverse-product scaling of the generalization time with learning rate and weight decay. A one-block Transformer shows similar macroscopic phase structure in a 42$\times$45-grid, as well as the same transition-time scaling despite violating exact homogeneity. Together, these results provide a mechanistic derivation connecting post-fit feature learning to both the onset of generalization and its phase structure in the learning rate and weight decay plane.

---


### 268. [DIFTA-3D: Depth-Consistent Instance-Level Feature Transfer and Adaptation of DINOv3 for 3D Detection](https://arxiv.org/abs/2609.26702)

**<font color=#1a73e8>作者：</font>** Linman Wang, ZiFei Zhang, Chunran Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-D 3D instance detectors benefit from visual semantics, but the task-specific Faster R-CNN/ResNet branch used by IIFNet3D couples feature extraction to a separately trained 2D detector and its image-domain labels. Replacing that branch with a frozen vision foundation model removes this task-specific dependency, but may introduce occlusion noise and a mismatch between patch features and geometry-aware detection features. In this work, we investigate this replacement through an adaptation of DINOv3 to the instance-level fusion pipeline of IIFNet3D. At the core of our approach is a depth-consistent feature pipeline that projects scene points into calibrated RGB-D frames, applies a metric depth-residual check, averages the accepted DINOv3 features into an offline point cache, and aggregates the cached features inside proposal-aligned RoI grids. The geometric and bidirectional instance-fusion paths are preserved, while Conservative VAID is evaluated as a low-strength, support-weighted semantic distillation recipe applied only to positive RoIs. We conduct extensive evaluations on ScanNetV2 to assess the proposed transfer recipes. On ScanNetV2, our DINOv3 control achieves mAP scores of 76.15 and 60.93 at IoU thresholds of 0.25 and 0.50, respectively. The Conservative VAID setting achieves mAP scores of 76.59 and 62.16, corresponding to numerical gains of 0.44 and 1.23 points over the control, respectively, in this checkpoint-level recipe comparison. The reported IIFNet3D result of 75.7/63.8 is used only as an external reference because the visual branch and processing protocol differ. Accordingly, we interpret these results as evidence for a controlled transfer recipe rather than as a causal estimate of the individual contributions of VAID or depth filtering.

---


### 269. [GAD-MambaUNet: Direction-Group Mamba with Gradient-Adaptive DINOv3 Distillation for Lightweight Medical Image Segmentation](https://arxiv.org/abs/2609.26729)

**<font color=#1a73e8>作者：</font>** Fang Wang, Huitao Li, Wenhan Chao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we proposed GAD-MambaUNet, a lightweight medical image segmentation network that combines efficient local modeling, direction--group state-space interaction, and training-time foundation-model supervision. To improve contextual modeling in compact segmentation networks, we introduced Direction-Group Graph Selective Scan (DG-GSS), which treated scan-direction and channel-group responses as graph nodes and enabled structured information exchange before multi-directional fusion. We further incorporated DINOv3-GAD supervision, where a frozen DINOv3 teacher provided semantic guidance during training, and Gradient-Adaptive Distillation dynamically regulated the distillation strength. GAD-MambaUNet achieves a favorable accuracy--efficiency balance compared with representative lightweight and general segmentation methods. Ablation studies further verify the effectiveness of DG-GSS and training-time DINOv3-GAD supervision. In future work, we will explore more flexible teacher--student alignment strategies and extend the proposed framework to more diverse medical segmentation scenarios, such as multi-class and multi-modal segmentation tasks.

---


### 270. [ASTRA-SR: Atmospheric Seeing and Turbulence Restoration for Astronomical Image Super-Resolution](https://arxiv.org/abs/2609.26731)

**<font color=#1a73e8>作者：</font>** Xining Ge, Ziteng Cui, Shuhong Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ground-based planetary imaging suffers from atmospheric turbulence, sensor noise, and limited sampling, making restoration a joint denoising, deblurring, and super-resolution problem. We present ASTRA-SR, a blind single-frame restoration framework trained on a physics-grounded synthetic dataset. High-dynamic-range spacecraft RAW observations serve as clean sources, and paired LR inputs are synthesized using measured layer-integrated turbulence strengths, propagated moving phase screens, exposure-averaged spatially varying PSFs, and sensor this http URL-SR first estimates a noise-suppressed but blur-retaining LR image, then restores spatial structure through multiscale processing and reconstructs HR detail with serial spatial-amplitude refinement. It yields a 0.49 dB foreground PSNR gain over the strongest baseline approaches.

---


### 271. [FleXray: Universal Clinical X-ray Segmentation](https://arxiv.org/abs/2609.26756)

**<font color=#1a73e8>作者：</font>** Victor Ion Butoi, Vivek Gopalakrishnan, John V. Guttag 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> X-ray is medicine's most widely used imaging modality, yet remains among its least quantitative. Unlike volumetric modalities like CT or MRI, X-ray collapses 3D anatomy into a 2D projection, causing structures to overlap and anatomical boundaries to be ambiguous, even to experts. As a result, labeling X-ray databases for training general-purpose segmentation systems is impractical, leaving morphometric and functional X-ray analysis confined to narrow anatomical regions and applications. To this end, we present FleXray, a generalist model for anatomical segmentation across the entire body in clinical X-rays. Instead of curating large, manually annotated X-ray datasets, we build a scalable, physics-based generative X-ray data engine. Using existing 3D whole-body CT segmentation datasets and generative image-editing models, we simulate fully-annotated 2D X-rays with diverse appearances, physiological properties, and imaging geometries. Trained on these simulations, FleXray accurately segments 60 anatomical structures across unseen research datasets and in-the-wild X-rays. We further show that FleXray makes X-rays directly amenable to quantitative analysis, enabling automated measurements for disease grading, robust navigation during X-ray-guided interventions, and data-efficient learning of pathological targets. We release the model, code, a full-body X-ray segmentation dataset, and a local, easy-to-use browser-based tool at this https URL .

---


### 272. [Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It](https://arxiv.org/abs/2609.26758)

**<font color=#1a73e8>作者：</font>** Yu Sun, Junhao Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Typed decision models are built for settings where model outputs are consumed directly by software. Instead of generating free-form text, they return a decision over a predefined set of options. By construction, every output conforms to the required schema. Yet this guarantee does not tell us whether the model interprets the options as intended. We study Jev and two Jev-like models with open weights by changing how option names are assigned to rubrics. Each option consists of an option name and a textual rubric that defines what the option means. We change only which option name is assigned to each rubric; the question, state, rubric wording, and set of option names remain exactly the same. On 1200 workflow decisions with task-specific rubrics, renaming the two options from 0/1 to no/yes changes 70.4 more answers per hundred (95% CI: [67.6, 73.1]) and shifts AUC from .94 to .23, revealing a systematic reversal in the decision ranking rather than simple uncertainty. The same operation has little effect with neutral option names. This pattern holds across all 4 predicates, where the effect is at least 7.4x larger than under the neutral control, and becomes stronger as the number of options increases. The effect also depends on the read-out geometry: a second model family that mean-pools over the full option span flips 4.1x less often. The hosted model exhibits the same behavior: the swap changes AUC from .8146 to .5806 and produces 24x as many answer flips as its test-retest floor. In contrast, replacing the option names with random character strings returns all model families to the neutral-control regime without reducing accuracy. The failure therefore depends on the semantic polarity of the option names rather than on the renaming operation itself. Across all conditions, the type-error rate remains 0%, even when decision accuracy degrades substantially.

---


### 273. [A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem](https://arxiv.org/abs/2609.26761)

**<font color=#1a73e8>作者：</font>** Laizhen Li, Xuan Wang, Peicheng Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agents using the Model Context Protocol (MCP) rely on semantic matching to select tools from third-party servers, exposing a semantic supply-chain risk through attacker-controlled metadata and outputs. We introduce A2M (Attraction-to-Manipulation), a two-stage black-box framework for hijacking MCP agents. The Attraction phase optimizes tool metadata to increase invocation probability; the Manipulation phase uses execution traces to refine adversarial tool returns that steer agents toward attacker-desired outcomes. On LiveMCPBench, direct attacks optimized and evaluated on GLM-4.6 achieve a macro-average malicious tool invocation rate of 93.6% across four scenarios, increase weighted token costs to 32.4$\times$ the benign baseline under Cognitive Denial of Service, and attain a mean attack success rate of 74.4% across Information Exfiltration, Environment Integrity Compromise, and Reasoning Derailment. Transfer to four other models without re-optimization yields corresponding macro-averages of 63.6%, 2.7$\times$, and 24.5%. These findings motivate stronger tool vetting and runtime isolation in MCP ecosystems. Code is publicly available at this https URL.

---


### 274. [StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training](https://arxiv.org/abs/2609.26774)

**<font color=#1a73e8>作者：</font>** Bao Tang, Jiahao Guo, Haoxiang Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vector Quantization (VQ) is fundamental to discrete visual tokenizers that power modern autoregressive and masked image generation models. While recent shared-projection codebook methods have substantially advanced codebook utilization, training stability remains a critical and underexplored challenge. We argue that the root cause lies in the entanglement of the Encoder--Decoder and Codebook training: because neither module can reliably fulfill its own responsibility in isolation, the system can only function when the two subsystems happen to cooperate---a fragile condition that breaks down precisely when training is most stressed. We propose StableVQ, which revisits the proper learning objective of each module and resolves the problems that arise when each is trained to fulfill its own role independently. Concretely, (1) Dynamic STE corrects the instability in the Encoder's learning objective, enabling it to robustly optimize the reconstruction space under discrete regularization even when codebook utilization is low. (2) Region VQ Loss reconceives the Codebook's learning objective so that it can independently guarantee full tracking of the encoder output distribution, without relying on encoder oscillations to drive activation. (3) Decoupled Schedule recognizes that the distinct responsibilities of the Encoder--Decoder and the Codebook demand distinct optimization dynamics, and assigns each an independent learning rate schedule to ensure robust system-level behavior. Built on top of shared-projection codebooks, StableVQ is lightweight and introduces no learnable parameters. Experiments on ImageNet demonstrate consistent improvements in training stability, codebook utilization, and reconstruction quality across diverse codebook sizes and initialization settings.

---


### 275. [SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving](https://arxiv.org/abs/2609.26777)

**<font color=#1a73e8>作者：</font>** Jennifer Williams, Dave Farris, Jeff Farris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce SWE-Serve, a benchmark for evaluating agents on production inference engineering tasks. Implementing an inference feature can require coordinating multiple changes across the serving stack, including model support, runtime execution, and public APIs. Existing benchmarks provide limited coverage of production inference engineering: repository-level software engineering benchmarks do not target inference, while general terminal-agent benchmarks include only a few inference tasks. Dedicated inference benchmarks, meanwhile, focus primarily on isolated kernel generation or performance optimization rather than repository-scale production feature implementation. SWE-Serve provides 53 repository-grounded tasks derived from recent production changes to SGLang, spanning six inference engineering families. Each task executes on either CPU or a single GPU (H100) and is evaluated with hidden functional and regression tests, including, where applicable, end-to-end (E2E) serving tests and calibrated performance gates. Executable no-op and oracle controls, adversarial verifier review, and closed-book execution support task validity and evaluation integrity. Across 11 models and 31 model-effort configurations, the best-performing configuration achieves 75% mean pass@1. SWE-Serve exposes a substantial gap between completing tasks locally and achieving production correctness. On 19 tasks with end-to-end coverage, model-serving E2E tests reject roughly one-third of patches that pass every other test (45.9% under the verifier versus 69.4% with E2E tests excluded from scoring), with pass rate increasing for each model's best-performing configuration. By making the production correctness gap directly measurable, SWE-Serve enables the field to track whether future agents move beyond completing tasks locally to achieving production correctness.

---


> [!TIP]
> 当前位于：**251-275**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-275**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
