# 📦 其他研究 | 2026年09月21日

> 本类共 **247** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-247](./part-05.md)

---

### 51. [VGGT-GS SLAM: Uncalibrated Monocular Gaussian Splatting SLAM with Feed-Forward Priors](https://arxiv.org/abs/2609.19628)

**<font color=#1a73e8>作者：</font>** Yuhang Han, Hao Wang, Jiaxi Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present VGGT-GS SLAM, a monocular 3D Gaussian Splatting SLAM system designed for uncalibrated videos. Starting from feed-forward VGGT pose and depth priors, our system performs submap differentiable bundle adjustment that jointly refines camera poses and a 3D Gaussian map, while optimizing submap-shared intrinsics and radial--tangential distortion through analytic calibration Jacobians. To improve global consistency, we introduce Gaussian-native alignment (GNA) for camera-anchored scale refinement between sequential submaps and verification of loop-closure candidates. Extensive experiments on standard indoor benchmarks show consistent improvements in localization accuracy and strong rendering quality under uncalibrated settings, establishing a strong baseline for uncalibrated Gaussian SLAM.

---


### 52. [Instance Segmentation and Fine-grained Classification for Urban Buildings with Adaptive Region Dividing and Spatially-Supervised Contrastive Learning](https://arxiv.org/abs/2609.19631)

**<font color=#1a73e8>作者：</font>** Weiyuan Zhang, Qi Zhang, Hui Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate instance-level and functional understanding of urban buildings in large-scale point clouds is essential for digital city modeling and urban analysis. However, the extensive spatial coverage of urban scenes leads most existing methods to rely on predefined blocks for training and evaluation, although such partitions are rarely available in real-world applications and introduce additional preprocessing while fragmenting complete building structures. To address this issue, we propose an adaptive region-dividing strategy with unified scene-level evaluation. Specifically, the 3D point cloud is projected onto a bird's-eye-view (BEV) plane, where a pretrained segmentation model is used to detect building regions. The detected bounding boxes are then back-projected to the original point cloud to construct structure-aligned adaptive training blocks, enabling semantically guided dynamic partitioning without manual design. Furthermore, beyond instance-level understanding, few methods have explored fine-grained classification for urban buildings, and thus we also put forward a fine-grained classification model for urban buildings with a spatially-supervised contrastive loss. First, for each segmented building, a point transformer classifier jointly encodes its body and local context using geometric, color, and core-context information. Then, the class-balanced weighted cross-entropy is used to alleviate severe class imbalance. The proposed spatially-supervised contrastive loss further enhances inter-class discriminability by assigning greater weight to spatially proximate, same-category buildings, encouraging compact functional representations while separating easily confused categories. Extensive experiments on UrbanBIS and STPLS3D demonstrate the advantages of the proposed method in building instance segmentation and fine-grained classification compared to existing SOTA methods.

---


### 53. [A Policy Profile for Croissant: Refusal as a Property of the Dataset](https://arxiv.org/abs/2609.19640)

**<font color=#1a73e8>作者：</font>** Alexander Chernov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Croissant is the de facto machine-readable descriptor for ML datasets: JSON-LD over this http URL. Since version 1.1 it also carries data use conditions, recommending DUO and ODRL for them. What no version specifies is how any of them is evaluated: no decision procedure, no bound on evaluation cost, no outcome for a condition an implementation cannot evaluate, no record of what was checked, and nothing on composition with caller-side authority. We supply that half. An additive profile lets a dataset declare the operations it admits and the conditions under which it admits them, over a closed set of five operators whose decision procedure is given in full, so a gate decides from the descriptor alone and records what it checked. Two corpora evaluate it and their evidence is kept apart. Three descriptors that gated a real nf-core pipeline give the deployment result: decisions from a profile document match the gate's native descriptor record for record, stripping the layer leaves a valid Croissant document, and the added cost is 11.7 $\mu$s against a 119 $\mu$s decision. A corpus generated from the profile's grammar gives the breadth, covering every operator, refusal class and conformance clause. Across its valid cases, 552 complete decision records agree three ways -- native descriptor, profile terms, and the same policy as ODRL in usageInfo. The carrier is therefore not the contribution; the evaluation semantics is. Finally, caller-bound and data-bound policies range over non-overlapping state spaces, so neither permit set contains the other.

---


### 54. [ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI](https://arxiv.org/abs/2609.19644)

**<font color=#1a73e8>作者：</font>** Jaehyun Nam, Jinsung Yoon, Yanzhou Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery is defined by the ability to identify the boundaries of existing knowledge and venture into unexplored territory. The ultimate vision for AI in science is problem-driven autonomous research: given a fundamental challenge by a human expert, the AI independently navigates the scientific landscape, uncovers theoretical and empirical bottlenecks, and systematically expands the frontier of knowledge. In this paper, we introduce ScientistTwo, a fully autonomous multi-agent framework designed to realize this vision. Specifically, ScientistTwo takes an initial problem as input, establishes state-of-the-art baselines, formulates novel hypotheses, and coordinates specialized agents to orchestrate an end-to-end discovery cycle without human intervention. Moreover, the framework rigorously conducts experiments using diverse datasets and metrics, refines methodologies through automated ablation studies, and validates research findings via a closed-loop simulated peer-review rebuttal engine. To evaluate ScientistTwo's capabilities against the highest standards of human scientific achievement, we benchmark it across papers accepted at top-tier conferences such as ICLR, ICML, and NeurIPS. As a result, ScientistTwo autonomously generates expert-level, publishable papers and fully verified, executable codebases. Its solutions consistently outperform human state-of-the-art models, and achieve higher average review ratings than human-authored papers under automated AI review agents. These results show that ScientistTwo is not merely an assistive tool but an autonomous scientific pioneer capable of pushing the frontiers of human discovery. Project website: this https URL

---


### 55. [Improving Cross-Lingual Transfer for Sequential Sentence Classification in Research Papers via Structural Similarity](https://arxiv.org/abs/2609.19650)

**<font color=#1a73e8>作者：</font>** Kazuhiro Yamauchi, Marie Katsurai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sequential sentence classification (SSC) is an essential task for structuring scientific publications, and extending SSC research to languages other than English can improve accessibility to scientific knowledge in multilingual digital libraries. Cross-lingual transfer is a promising approach to address the scarcity of training data in non-English languages. Prior work on other natural language processing tasks has shown the benefits of capturing linguistic similarity between source and target languages. However, SSC inherently depends on patterns at the discourse level, such as label sequences and positional regularities, which appear consistently across languages regardless of linguistic differences. To examine the factors that determine transfer success in SSC, we constructed a multilingual SSC dataset covering 13 non-English languages collected from five academic databases. Our cross-lingual transfer experiments, using both encoder-based and generative models, show that linguistic proximity has no consistent predictive power for transfer performance, whereas structural similarity in rhetorical organization shows a weak but consistent positive correlation across models. After controlling for source-language performance, the similarity of label distributions is the most consistent predictor. Building on this finding, we propose a set of three methods that explicitly leverage structural information using generative models. In the in-domain evaluation, the best combination reaches parity with the strongest encoder baselines, and in transfer to languages unseen during training, it outperforms the strongest encoder baseline.

---


### 56. [VideoResearcher: Self-Improving Tool Design for Long-Video Understanding](https://arxiv.org/abs/2609.19664)

**<font color=#1a73e8>作者：</font>** Dingqiang Ye, Dongdi Zhao, Kaishen Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video agents have made substantial progress in long-video understanding. Yet effective video-agent systems require costly, time-consuming manual design and trial and error. Current self-improvement methods either refine low-impact prompts, recombine predefined micro-tools, or struggle with convergence in harness optimization. To bridge this gap, we target high-impact video-tool with VideoResearcher, a training-free multi-agent framework that autonomously designs, tests, and refines tools for video understanding, like a human researcher. VideoResearcher operates through dual Solving and Evolving loops: it analyzes tool-use trajectories to identify capability gaps, coordinates specialized agents to develop and validate executable tools, and reuses evolved tools to strengthen evidence acquisition in subsequent video reasoning. Through iterative tool refinement and validation, it progressively strengthens evidence acquisition without updating model parameters. VideoResearcher achieves state-of-the-art performance among self-improving agents and approaches the human-designed upper bound, demonstrating a training-free paradigm for long-video understanding that expands agent capabilities through autonomous tool development while reducing costly manual engineering.

---


### 57. [CoRe: Coherence and Relational Alignment for Multivariate Time Series Forecasting](https://arxiv.org/abs/2609.19670)

**<font color=#1a73e8>作者：</font>** Xiaoyu Lin, Huiran Duan, Yining Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct forecasting has become a standard paradigm for multivariate time-series forecasting because it predicts the full future horizon in a single pass. However, its training objective is often still decomposed into pointwise errors such as MSE. Such objectives provide stable supervision, but they do not explicitly preserve the structure of the future trajectory: temporal coherence within each variable and relational consistency across variables can both be weakened. We propose CoRe, a model-agnostic learning objective for direct multivariate forecasting. CoRe replaces pointwise supervision with two output-space constraints: a frequency coherence loss that aligns predicted and target spectra, and a low-rank relational graph loss that matches sampled pairwise differences in a target-derived PCA subspace. The resulting objective introduces no trainable parameters and can be applied to existing forecasting backbones by changing only the loss. Experiments on standard benchmarks show that CoRe improves strong baselines, compares favorably with recent forecasting objectives, and remains effective across different backbones, datasets, and hyperparameter settings overall consistently.

---


### 58. [Conservation Buys Stability and Factoring Buys Counterfactuals in Physical World Models](https://arxiv.org/abs/2609.19674)

**<font color=#1a73e8>作者：</font>** Yufeng Wang, Parivesh Priye, Lu Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A learned simulator can reproduce its training conditions accurately yet fail in two distinct ways once those conditions change. Over long rollouts, small errors accumulate until the trajectory drifts away from physically plausible behavior; under an intervention on a physical parameter, the model may continue to follow the law seen during training rather than the intervened one. We show that these two failures require different structural remedies. Evolving a learned energy with a symplectic integrator preserves the geometry of the conservative dynamics and keeps rollouts bounded and physically meaningful for up to $100\times$ the training horizon, while equal-capacity predictors, an energy-regularized predictor, and a tuned neural ODE diverge. By contrast, encoding the physical coupling through an explicit linear factorization enables the model to follow a never-seen sign of that coupling, whereas an unrestricted parameterization remains locked to the training law. Crucially, the two mechanisms are separable: removing the structure responsible for long-horizon stability leaves counterfactual transfer intact, while removing the factorized coupling destroys counterfactual transfer without eliminating stability. This double dissociation, established with matched controls that remove or replace one structural component at a time, persists beyond the headline three-body system and remains visible when the physical state must be inferred from pixels rather than provided directly. The result is a concrete design principle for physical world models: long-horizon stability and changed-law generalization arise from distinct structural commitments, and each can be imposed deliberately without requiring the other.

---


### 59. [FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA](https://arxiv.org/abs/2609.19680)

**<font color=#1a73e8>作者：</font>** Yanzhang Ma, Zhenghan Tai, Hanwei Wu 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial QA systems are typically improved before deployment through better retrieval, prompting, or agent coordination, leaving their reliability behavior fixed thereafter. In practice, new SEC-filing questions repeatedly expose heterogeneous errors in period, entity, evidence use, and calculation. Existing self-improvement methods can turn failures into new behaviors, but offer limited control over where a correction should apply or which previously correct answers it may break. We therefore frame post-deployment improvement as controlled behavioral maintenance: recurring failures should become scoped skill patches, and each patch should earn deployment with- out introducing regressions. We instantiate this view in FINSKILLOPS, a multi-agent system for SEC filing QA. FINSKILLOPS derives reusable skills from evidence-grounded, typed failure diagnoses and governs them through targeted validation, protected-case regression checks, negative controls, and versioned replacement or retirement. Across six financial QA benchmarks, a single frozen skill registry achieves the highest verdict-weighted correctness and reference consistency among the evaluated systems. Evolved skills raise correctness from 3.70 to 4.55 on our enhanced benchmark. In a separate 12-round operational study, only six of 33 proposed skills are promoted, while the monitoring non-correct rate falls from 20.0% to 12.5%. These results establish controlled skill scope, admission, and lifecycle management as the foundation for reliable self-improvement.

---


### 60. [Opinion Dynamics-based Coalition Formation for Federated Learning in Heterogeneous IoT Systems](https://arxiv.org/abs/2609.19695)

**<font color=#1a73e8>作者：</font>** Mohammed El Hanjri, Anas Abouaomar, Hamidou Tembine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables privacy-preserving, on-device training across heterogeneous Internet-of-Things (IoT) deployments such as smart-city water-metering networks, where each smart meter observes a household-specific consumption time series. Under such statistical heterogeneity, the standard Federated Averaging (FedAvg) aggregation averages dissimilar local models into a single global model that may fail to capture client-specific patterns. We address this by forming client coalitions directly in the local-weight space and aggregating at the coalition level. Extending a prior weight-driven coalition-formation scheme, we model coalition formation as a Hegselmann-Krause (HK) bounded-confidence opinion-dynamics process acting on the local weights, and develop variants of the HK interaction based on Euclidean-distance and cosine-similarity confidence criteria. The framework is applied to short-term water-consumption forecasting with local Long Short-Term Memory (LSTM) models and evaluated against FedAvg, Per-FedAvg, FedProx, and FedAvg with Euclidean-distance or cosine-similarity coalition formation. Experiments on a real smart-metering dataset of water consumption show that the proposed HK-based coalition formation produces stable, endogenous coalition structures within at most ten inner iterations, incurs no additional client-side computation or communication compared to FedAvg, and reduces the average MAE by up to 54% relative to FedAvg, 39% relative to FedProx, and 24% relative to Per-FedAvg, while achieving the highest global accuracy (83-85%).

---


### 61. [Odds-Ratio Thompson Sampling: A Specification and Design Guide for Contrast-Based Multi-Armed Bandits](https://arxiv.org/abs/2609.19709)

**<font color=#1a73e8>作者：</font>** Sulgi Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Batched multi-armed bandits update on a service's own schedule, and the usual implementation carries each arm's absolute reward rate from one update to the next. When the shared level moves between batches, that memory goes stale even though the comparisons between arms may not have. Odds-Ratio Thompson Sampling (OR-TS) instead carries the joint posterior over log-odds contrasts and fits the common level afresh in every batch, marginalizing it out. This paper specifies that update, places it inside a Bayesian bandit agent with two controls, decay for how much past evidence survives an update and aggressiveness for how sharply belief becomes allocation, and evaluates it against absolute-rate memory. Across 86 public A/B series the level varies about twenty-five times more than the contrast. In prespecified synthetic environments a moving level costs absolute-rate memory five times the regret and leaves the best arm below a majority of traffic in 7 of 20 runs, against none for OR-TS. In a policy simulation built from 71 real experiments, where the contrasts are too small to resolve, expected-click differences stay within 0.1% for 58 of them, yet contrast memory still ends on the better arm more than twice as often. Where the contrasts themselves move, the bet fails, and that case is reported too.

---


### 62. [GAPrompt++: Multi-Granular Geometry-Aware Point Cloud Prompt for 3D Vision Model](https://arxiv.org/abs/2609.19716)

**<font color=#1a73e8>作者：</font>** Zixiang Ai, Zhenyu Cui, Yufei Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained 3D vision models have substantially advanced point cloud analysis, yet adapting them to downstream tasks via full fine-tuning is computationally expensive and storage-intensive. Parameter-Efficient Fine-Tuning (PEFT) offers a promising alternative by reducing both adaptation cost and storage burden. However, existing prompting-based approaches ignore the intrinsic geometric structures of point clouds, thereby limiting their adaptation capability. This limitation stems from their inability to encode both fine-grained geometric cues and coarse-grained structural semantics, as well as failing to propagate such information effectively through the model hierarchy. To address these challenges, we propose GAPrompt++, a multi-granular geometry-aware prompting method that provides richer geometric guidance for efficient 3D task adaptation. Specifically, we introduce a Point Shift Prompter that extracts multi-granular geometric features across different scales, enabling instance-specific geometric adjustments during adaptation. Next, a Keypoint Prompter adaptively generates point-level prompts to highlight local geometric saliency and fine-grained structural details. Furthermore, a Prompt Propagation mechanism injects these multi-granular geometric cues throughout the feature extraction hierarchy, strengthening the ability to capture essential geometric characteristics. Extensive experiments show that GAPrompt++ achieves state-of-the-art performance among prompting-based PEFT methods and even surpasses full fine-tuning across diverse benchmarks, while requiring less than 2\% trainable parameters. In addition, to address the saturation of existing evaluation datasets, we construct two more challenging benchmarks derived from 3D Gaussian Splatting and Multi-View Stereo reconstruction, offering diverse and realistic point cloud scenarios to promote future research.

---


### 63. [SeetaPsych v1.0: An Open-source Computer Vision Toolkit for Behavior-based Psychological Measurement](https://arxiv.org/abs/2609.19719)

**<font color=#1a73e8>作者：</font>** Jiabei Zeng, Chiqin Li, Kaizhou Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated visual analysis opens new avenues for behavior--based psychological measurement. Nevertheless, existing technological modules are typically scattered across task specific systems with heterogeneous interfaces and disparate deployment requirements. In this work, we present SeetaPsych v1.0, an open source, unified and extensible computer vision toolkit designed to extract psychologically relevant signals from facial images and/or face based videos. The current release encompasses four major core modules aiming at behavior--based physiological perception: unified face based emotion analysis (simultaneous facial expression recognition, facial action unit detection, and valence--arousal estimation), camera based heart rate estimation, screen point--of--gaze estimation, and scene gaze following. A suite of auxiliary preprocessing modules for human centric visual analysis is also included, comprising face detection, facial landmark detection, and head detection. These functionalities are encapsulated within a modular Pipeline/Runner architecture that automatically resolves attribute dependencies, constructs computation graphs, and support intermediate result sharing among modules. SeetaPsych provides standardized Python APIs to facilitate reproducible, large scale analyses, alongside an interactive WebUI for rapid, code--free method evaluation. Overall, SeetaPsych offers an integrated and accessible visual measurement platform for research in psychology, behavioral science, human computer interaction, and related fields.

---


### 64. [A Phonemically Comprehensive, ASCII-Only Romanization Scheme for Thai and Lao: Systematic Cross-Lingual Correspondence and Chinese-User-Friendly Design](https://arxiv.org/abs/2609.19736)

**<font color=#1a73e8>作者：</font>** Zijie Zhang, Tan Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper proposes a phonemically comprehensive, ASCII-only romanization scheme for Thai and Lao, treating the two closely related languages as a unified cross-lingual design problem. The scheme represents segmental contrasts, vowel length, and lexical tone while maintaining one-symbol-one-phoneme transparency and systematic correspondence between Thai and Lao. The scheme prioritizes synchronic phonetic correspondence, including correspondence with Pinyin and Jyutping where applicable, while preserving historical-phonological correspondence where it does not conflict with phonetic transparency. Tone uses a compact single-digit default notation, supplemented by optional tone-value and historical tone-category representations. The resulting scheme provides a readable, keyboard-friendly, and machine-processable phonemic representation for language learning and cross-lingual speech processing.

---


### 65. [Federated Learning Framework for Privacy-Preserving Kidney Stone Detection](https://arxiv.org/abs/2609.19740)

**<font color=#1a73e8>作者：</font>** Najiyya Younas, Omar Abdulkader, Yaser Ali Shah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent innovations in deep learning have significantly enhanced the diagnosis of medical images, although they are based on the use of centralized data storage that pose severe threats to patient privacy and medical data security. To address this issue, this research proposes a Federated Learning (FL) model that is coupled with an optimized YOLOv8 network to detect the kidney stones on a computed tomography (CT) image and at the same time, protect privacy of the patients. The suggested system can help various medical organizations to jointly train a common model without exchanging the information about the patients. This is to ensure that data protection laws like GDPR and HIPAA are adhered to. The residual feature fusion and DropBlock regularization among other architectural improvements are also included in YOLOv8 to enhance detection robustness and minimize overfitting. Experimental analysis carried out on a distributed CT dataset demonstrated that the federated YOLOv8 model has a mAP at 50 of 0.733 and is able to keep the data confidential. Moreover, its lean design facilitates fast edge deployment and real-time inference across a clinical setting. Altogether, these findings indicate that Federated Learning is a safe and efficient solution to AI-assisted diagnosis in contemporary healthcare when combined with the use of sophisticated object detection models.

---


### 66. [STAR: Structure-aware Test-time Adaptation for diffusion-based light field Reconstruction](https://arxiv.org/abs/2609.19747)

**<font color=#1a73e8>作者：</font>** Wontae Choi, Ki Ryum Moon, Jae Young Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Light field (LF) reconstruction from limited and noisy focal stack (FS) measurements is a highly ill-posed inverse problem. Although the LF-to-FS imaging geometry is fixed for a given optical setup, LF spatial-angular structure---including within-view spatial details, cross-view angular dependencies, and disparity across views---varies across scenes. Consequently, a fixed pre-trained prior may not optimally capture the spatial-angular structure of each test LF. We propose Structure-aware Test-time Adaptation for diffusion-based light field Reconstruction (STAR), the first test-time adaptation framework for reconstructing an LF from FS. For each test LF, STAR freezes a pre-trained diffusion prior and fits three lightweight adapters to the observed FS to jointly adapt the three components of the LF's spatial-angular structure. STAR outperforms existing state-of-the-art methods in both two- and three-focal-sheet settings, with shorter inference times than those with test-time parameter updates.

---


### 67. [Alliance Beats Isolation: Unifying Heterogeneous Allied Datasets Improves Classifier Performance](https://arxiv.org/abs/2609.19748)

**<font color=#1a73e8>作者：</font>** Girish Keshav Palshikar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many application domains, such as student dropout, insurance fraud, loan approval, and machine failures, several labelled public datasets are available where (i) data is about the same type of objects but the set of actual underlying objects are disjoint; and (ii) the class labels are same; and (iii) the feature spaces of the datasets are largely distinct (heterogeneous), with a few shared features. We call such datasets as allied. A single classifier cannot be trained on both datasets together, and one classifier trained on one dataset cannot be tested on the other. In this paper, we propose a method to merge the feature-spaces into a single feature-space for a pair of given allied heterogeneous datasets. We then use a matrix completion method to create a unified dataset based on the merged feature-space. The hypothesis is that the merged representation facilitates the transfer of classification knowledge from one dataset to another. We conduct experiments on several pairs of allied, heterogeneous datasets and several classifiers to demonstrate that any classifier trained on the unified representation always outperforms classifiers separately trained on the constituent allied datasets on several pairs of allied datasets. This work provides an easy way to substantially improve classifier performance by unifying and using multiple allied datasets together.

---


### 68. [TorchCraft: Unified binder design by inverting an all-atom structure predictor](https://arxiv.org/abs/2609.19770)

**<font color=#1a73e8>作者：</font>** TorchCraft Team, Yu Liu, Zhouhanyu Shen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> All-atom structure predictors model diverse molecular interactions, but using their learned structural priors for binder design remains challenging. Here we present TorchCraft, a unified binder-design framework that optimizes sequence logits through a frozen all-atom predictor. Implemented in TorchFold, TorchCraft combines confidence, contact, geometric, and sequence-prior objectives within a shared optimization procedure for minibinders, framework-conditioned VHHs, cyclic peptides, and ligand-binding proteins. Using pretrained AlphaFold 3 weights, TorchCraft generated representative minibinders and VHHs with experimentally measured binding across four targets in each format, without post hoc sequence redesign. Computational benchmarks further demonstrated the framework's applicability to cyclic peptides and ligand-conditioned pocket design. TorchCraft extends predictor inversion to multiple binder formats and molecular contexts, providing a common framework for reusing all-atom structural priors in design.

---


### 69. [Treadstone: A Social-Media-Inspired Platform for Multi-Agent Collaborative Data Analysis](https://arxiv.org/abs/2609.19774)

**<font color=#1a73e8>作者：</font>** Hyunwook Lee, Sungbeom Cho, William Benjamin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Coordinating human analysts with autonomous AI agents faces the same challenges as human-to-human collaboration: sharing intermediate results, avoiding conflicts, and maintaining group awareness. Current tools rely on unstructured messaging or single-threaded chatbot interaction, which lack the structure to track evolving hypotheses or link claims to evidence. We propose agentic social data analysis, a collaboration paradigm extending social data analysis with a shared coordination feed modeled on the content timeline in social media services. We instantiate this concept in TREADSTONE, a platform where human and AI agents asynchronously post, link, and contest analytical claims via threaded messages within a shared feed. By allowing agents to proactively broadcast hypotheses and enabling users to steer the analysis through lightweight curation, Treadstone seeks to balance machine autonomy with human analytical control. A qualitative user study shows that Treadstone fosters collaboration while preserving human analytical agency, in contrast to the solitary experience of conventional chatbot interaction.

---


### 70. [Integrating knowledge from case reports: a medical ontology based multimodal information system with structured summary](https://arxiv.org/abs/2609.19775)

**<font color=#1a73e8>作者：</font>** Shuyu Guo, Lan Huang, Yichen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Published medical case reports serve as a crucial medical information carrier, documenting discoveries in rare diseases, diagnostic methods, and innovative treatments. Despite the wealth of clinical knowledge in millions of case reports in the public medicine literature database (PubMed), accessing relevant information efficiently is hindered by the limitations of traditional keyword-based retrieval tools on unstructured and diverse case reports. To address the above issues, we introduce a comprehensive multimodal information system for case reports integrating structured clinical summaries of patients including medical images and biomedical named entities from 52949 open-access case reports published from 2000 to 2021. The multimodal essential information is organized in a well-structured medical ontology. Also, a powerful interface for searching and browsing case reports is designed to assist junior clinicians in retrieving cases effectively and improving the identification and diagnosis of rare diseases.

---


### 71. [PhyRestore: Physics-Structured Latent-Factor Restoration](https://arxiv.org/abs/2609.19776)

**<font color=#1a73e8>作者：</font>** Ahmed Shafee, Chayan Lahiri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating temporal soil-loss change is challenging when physically meaningful input factors are noisy or corrupted, particularly because substantial changes are rare relative to the large number of locations exhibiting little change. We study this problem through the Revised Universal Soil Loss Equation (RUSLE) and introduce PhyRestore, a physics-structured latent-factor restoration framework. Rather than directly predicting soil-loss change or correcting a degraded physical estimate, PhyRestore restores corrupted physical factors and reconstructs temporal change through the known physical relationship. We evaluate PhyRestore in a watershed-scale bitemporal raster setting under isolated and simultaneous corruption of rainfall erosivity and cover management, comparing it with the degraded RUSLE estimate and Direct RF, XGBoost, MLP, and CNN models. Factor restoration improves high-magnitude recovery when the corrupted factors remain identifiable, but its advantage weakens under joint corruption, sparse positive extremes, and factor values outside the training support.

---


### 72. [Learning-Based Reconstruction of Optical Properties in Bilayered Media from Single-distance Time-Resolved Reflectance Measurements](https://arxiv.org/abs/2609.19786)

**<font color=#1a73e8>作者：</font>** Caterina Amendola, Giulia Maffeis, Lorenzo Buffoni 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The inverse problem of reconstructing optical properties, specifically absorption and scattering coefficients, in layered biological media from time-domain reflectance measurements remains a significant challenge for traditional analytical models. Inverse solvers based on the diffusion equation often struggle with structural heterogeneity, frequently yielding poor accuracy for superficial absorption and deep-layers scattering. In this work, we propose a machine learning framework as an alternative approach to reconstruct the optical properties of a bilayered medium, benchmarking its efficiency and accuracy against model-based algorithms. To overcome the intrinsic approximations of diffusion theory and inverse reconstruction, we generated a robust synthetic dataset of forward DTOF using exact Monte Carlo simulations at multiple source-detector distances. A machine learning pipeline was then trained on this dataset and validated against state-of-the-art model-based reconstruction methods. Besides the significant reconstruction speed-up, the machine learning approach achieves higher accuracy than model-based inverse solvers, further providing an estimate of the parameter space dimensionality without requiring any a priori information about the number of layers in the investigated geometry. Further enhancements in the reconstruction accuracy can be expected in future extensions of this work, by training the pipeline over multiple DTOF curves from the same medium, in a joint multi-distance reconstruction approach.

---


### 73. [Sybil-TraceGuard: Traceability-enhanced Sybil Guardian for Connected and Autonomous Vehicles Using Dynamic Semi-supervised GNN](https://arxiv.org/abs/2609.19791)

**<font color=#1a73e8>作者：</font>** Qian Xu, Jiaxun Zhang, Chengyue Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Connected and autonomous vehicles (CAVs) face severe Sybil attacks, where attackers exploit privacy-preserving pseudonym-switching mechanisms to anomaly alternate identities while forging Basic Safety Messages (BSMs). Although existing schemes can flag suspicious behaviors, these temporally fragmented Sybil identities render traditional single-point and sequence-based deep learning methods ineffective. Linking these fragmented identities back to the source attacker is essential for root-cause elimination, particularly under extreme label scarcity. Therefore, the Sybil-TraceGuard is proposed as a dynamic semi-supervised spatio-temporal GNN framework for Sybil Guardian, prioritizing "who is responsible" over "whether an attack is happening". It comprises four tightly coupled modules: Incremental Stream Attack Detection (ISAD) for efficient Sybil attack pre-screening; the Dynamic Topology-aware Constructor (DTC) for constructing spatio-temporal dynamic graphs; the Spatial GAT-Encoder with Multi-head Attention (SGEM) to capture multi-identity logical conflicts in spatial interactions; and the Multi-scale Spatio-Temporal Audit (MSTA) to audit short-term and long-term temporal inconsistencies. These modules are optimized within a semi-supervised Mean-Teacher framework via feature-edge shuffling perturbations, regularizing the latent feature space using minimal labels. Experiments across four Sybil attack scenarios demonstrate that Sybil-TraceGuard effectively links fragmented pseudonyms to source attackers. It outperforms state-of-the-art baselines across unlabeled ratios of 0.70-0.95, maintaining high stability and sensitivity despite extreme class imbalance and varying hyperparameter settings.

---


### 74. [AI Smart Glasses for Wearable Intelligence: From Egocentric Sensing to Agentic Personalization](https://arxiv.org/abs/2609.19793)

**<font color=#1a73e8>作者：</font>** Xu Yuan, Yi Wang, Zhuohang Jiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in artificial intelligence (AI) are reshaping smart glasses from egocentric capture and display devices into platforms for wearable intelligence. Smart glasses increasingly serve as wearable AI systems that connect first-person observation with real-time assistance under strict form-factor constraints. We frame this transition through the lens of \emph{AI smart glasses} and define them as a system-level concept in which egocentric sensing, resource-aware computing, intelligent reasoning, multimodal interaction, and real-world application constraints are co-designed for personalized assistance in the physical world. To systematically study this perspective, we organize the survey around four connected dimensions. First, we examine the hardware foundation that bounds sensing, computation, feedback delivery, and sustained deployment. Second, we study wearable intelligence, where egocentric signals are transformed into perceptual, contextual, and agentic capabilities. Third, we discuss interaction design, through which users request, receive, correct, and regulate assistance during ongoing activity. Fourth, we analyze application scenarios across healthcare, accessibility, situated learning, daily life assistance, cultural tourism, and industrial support, showing how domain requirements reshape system design and evaluation. We further identify five cross-cutting research challenges for future AI smart glasses: next-generation hardware, trustworthy egocentric intelligence, lifelong personalized memory, proactive intelligence, and embodied foundation models. By centering smart glasses as wearable-intelligence platforms, this survey provides a unified framework for organizing technologies, applications, and open challenges in this emerging area.

---


### 75. [MetaRTL: Meta-path Attention Enhanced Relational Table Learning](https://arxiv.org/abs/2609.19832)

**<font color=#1a73e8>作者：</font>** Ken Zhong, Weichen Li, Zheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Relational table learning has gained increasing attention with the widespread use of relational databases. Existing methods typically rely on deep GNN or HGNN stacks, leading to high computational costs and limited performance on large real-world databases. We propose MetaRTL, a two-stage framework for scalable and expressive relational table learning. In the first stage, MetaRTL obtains initial table embeddings via lightweight pre-training. In the second stage, it performs non-parametric message passing to derive meta-path features, which are then aggregated by an attention module, MetaAttn. By shifting computation from deep message passing to efficient meta-path aggregation, MetaRTL captures rich relational semantics while maintaining high efficiency. Experiments on 10 real-world datasets across 24 tasks demonstrate the effectiveness of the proposed method.

---


### 76. [Point, Revise, Review: Grounded Agentic Analysis in Reactive Notebooks with marimo-lens](https://arxiv.org/abs/2609.19839)

**<font color=#1a73e8>作者：</font>** Péter Ferenc Gyarmati, Trevor Manz, Dominik Moritz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In a computational notebook, a human can point to a rendered result and ask about "this," while an agent acts through cells, dependencies, and runtime state. When what the human sees and what the agent operates on are disconnected, the human must describe what they mean and trace what the agent did in prose that strips away situated visual and computational context. We present marimo-lens, an extension to the reactive Python notebook marimo for grounded human-agent analysis. Lens connects a human's marked output and note to its producing cell and relevant contributing computation, giving the agent computational context for the request. It surfaces agent activity, returns selected results to the notebook, and preserves the initiating selection for human review and reopening. We illustrate the lifecycle through an exploratory human-agent analysis of a real-world open dataset, showing how visually situated questions lead to computational inspection, notebook action, and returned evidence for human review.

---


### 77. [KoUniTalk: A Lightweight Articulation-Centered Korean-English 3D Talking Face Benchmark](https://arxiv.org/abs/2609.19840)

**<font color=#1a73e8>作者：</font>** Hyunjung Chung, Unsang Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality 3D talking face datasets remain largely English- centric, and Korean 3D facial motion data are difficult to combine with standard English benchmarks because of differences in mesh topology, spatial scale, coordinate system, and temporal sampling. We present KoUniTalk, a lightweight articulation-centered Korean-English 3D talk- ing face benchmark that retargets VOCASET and the released Korean speech-based 3D talking face data to a shared mesh topology using de- formation transfer. Rather than proposing a new deformation-transfer algorithm or a full-head identity-preserving avatar dataset, KoUniTalk provides an identity-neutral canonical output space for controlled speech- driven facial articulation training and evaluation across English and Ko- rean. The unified template contains 1,176 vertices and focuses on the mouth and adjacent lower- and mid-face regions, reducing the output dimensionality from 15,069 and 72,147 dimensions to 3,528 dimensions, corresponding to 4.27-fold and 20.45-fold reductions compared with VO- CASET/FLAME and the original Korean mesh, respectively. To exam- ine whether retargeting preserves speech-relevant motion, we evaluate semantic mouth-landmark trajectories, including mouth opening, mouth width, aperture ratio, and mouth-opening dynamics. Since the official test set of the Korean dataset is not publicly released, we additionally define a subject-disjoint Korean benchmark split. The processed matched benchmark contains 22 speakers, 4,978 sequences, and 642,781 frames, enabling Korean-English cross-dataset evaluation of speech-driven 3D fa- cial animation models in a single compact articulation-template space. Source-reported inventory counts are listed separately from these pro- cessed counts

---


### 78. [Beyond Flattened Tokens: Structure-Preserving EEG Decoding with Reusable TriDim Blocks](https://arxiv.org/abs/2609.19842)

**<font color=#1a73e8>作者：</font>** Shiyue Su, Song Wang, Zekai Zhan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective EEG decoding requires representations that preserve organization among channels, local waveform dynamics, and long-range temporal context. Existing EEG architectures often capture these structures using separate specialized modules or collapse them into a single token sequence, making it difficult to maintain their distinct roles and coordinate their interactions throughout the backbone. We propose TriDim, a reusable block that preserves the representation shape and keeps three EEG axes explicit: channel, sample position within each patch, and patch position across the recording. These axes correspond to spatial, short-term temporal, and long-term temporal information, respectively. Each TriDim block applies feed-forward transformations along individual axes and cross-axis attention to coordinate information exchange among them. By stacking TriDim blocks with a multi-level tri-axis readout, we construct TriDimEEG, a standalone EEG decoder. Under strict cross-subject evaluation on eight datasets spanning clinical diagnosis, sleep staging, motor imagery, and emotion recognition, TriDimEEG achieves the best overall performance among fifteen evaluated models, with a 4.3% relative improvement in average accuracy over the second-best model. Replacing Transformer blocks in three EEG foundation models with TriDim blocks yields an average relative improvement of 7.4% in downstream accuracy while reducing parameter counts by 17.0% to 47.3%. These results establish TriDim as an effective and reusable building block and TriDimEEG as a strong standalone EEG decoder. Code and parameters of TriDimEEG are available at this https URL.

---


### 79. [Trust, but Validate the Instrument: Auditing AI-Generated RTL Verification Plans on Authored Security-Regression Proxies](https://arxiv.org/abs/2609.19844)

**<font color=#1a73e8>作者：</font>** Hang Xiao, Chuhong Xu, Kainan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-generated RTL verification plans can satisfy a provider schema yet fail at the boundary to trusted execution. We present SecTB-RTL, an auditable framework covering 31 tasks and 124 authored hardware-security regressions. A deterministic non-AI baseline killed 36, 75, and 78 mutants at increasing resource limits. The first confirmatory run (C1-R2) failed before model execution because the provider rejected its response schema. After a schema-only repair made without viewing outcomes, a separately frozen follow-up run (C1-R3) completed 1,860 calls. The provider accepted 1,857 responses, but only nine passed the production semantic validator. The generation and execution rules did not match. We therefore preserve the run as an instrument-validation incident and report no prompt-effect estimate. This incident shows that provider or schema acceptance does not establish execution validity. Compilation and coverage are only diagnostics; the exact saved artifact must pass the full production path. A subsequent follow-up is excluded because it did not satisfy the preregistered evidence-completeness gate and is treated only as future work. We release the benchmark, failure-preserving contract, incident provenance, and governance controls needed to prevent infrastructure behavior from being misreported as model behavior.

---


### 80. [Constraint-Safe Graph-Context Scoring for Stable Point-Feature Labels Under Text-Width and Accessibility-Inspired Profiles](https://arxiv.org/abs/2609.19848)

**<font color=#1a73e8>作者：</font>** Taimoor Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Point-feature label placement on interactive maps must reconcile geometric validity, display yield, local placement utility, and stability across camera motion. Accessibility and multilingual requirements further change label dimensions, yet algorithmic evaluations often collapse these concerns into overlap counts. We present LABELSENSE-Pilot, a reproducible prototype that generates eight compass candidates per feature, scores candidates with a multilayer perceptron over graph-context summaries, adds a previous-placement bonus, and selects a layout through mixed-integer optimization. The executed scorer is deliberately not described as a graph transformer. Every returned layout is checked for viewport containment, per-feature uniqueness, and pairwise clearance. Experiments use 2,500 airport coordinates and names spanning 155 countries, with country-grouped splits and generated density, camera, text-suffix, preference, and enlarged-font stressors. Across five seeds, LABELSENSE-Pilot displayed 85.62 percent of labels with 2.09 percent flicker and zero collisions. Versus a handcrafted-utility integer program, LABELSENSE-Pilot sacrificed 1.43 percentage points of display while reducing flicker by 12.04 points. Enlarged-box-aware layouts produced zero proxy violations, whereas standard geometry reevaluated at 1.5x violated 52.57 percent of selected placements. These results establish an auditable engineering trade-off, not human accessibility, multilingual usability, or preference. Official recent baselines and participant evidence remain required before submission.

---


### 81. [PACE: Precise AI Cinematic Expression: A Typed Specification for Script-Grounded Previsualization and Geometric Conformance](https://arxiv.org/abs/2609.19853)

**<font color=#1a73e8>作者：</font>** Bing Duan, Qiang Guo, Linpu Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Between a screenplay and a film sits a planning problem that is spatial first: who stands where, and what a camera sees from where it stands. An image diffusion model asked for a shot in free text settles that plan by its own defaults. We present PACE (Precise AI Cinematic Expression), a typed representation for the plan: the screenplay evidence, the characters, props and locations it needs, where each subject stands, and what the camera does. A value is written once at the level it belongs to (script, scene, shot or panel) and inherited below it. A compiler turns the result into both the prompt sent to the diffusion model and a 3D scene built in metres, and a camera solver places the camera so that the declared framing is the framing built. Where a declared value becomes geometry, PACE measures, field by field, how far the compiled camera and the staged render sit from the declaration, rather than asking a model to judge.
On the 11-scene Automatic Drive screenplay, every staged single-subject panel places its subject within 1.2% of frame width of its declared position; with two or three subjects one camera pose cannot satisfy every position, and the residual is reported rather than absorbed. On 204 external director-storyboard shots, delivered head height is 1.906 times the staged target from the director's words, 1.733 from the compiled prompt, and 0.955 with the greybox control; the condition that holds framing best draws the described action least. Declaring the pose on 30 shots raises the action drawn from 58.9% to 74.4% without moving the framing. Transitions, fitted motion and human review of the generated panels remain open. Code: this https URL

---


### 82. [Expected Hypervolume Maximization for Multiobjective Optimization under Uncertainties](https://arxiv.org/abs/2609.19858)

**<font color=#1a73e8>作者：</font>** Victor Trappler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The problem of multiobjective optimization under uncertainties is often approached by taking the expectation of each objective. In this work, we propose instead to formulate this as a Bayesian decision problem and to rely on the expected value of the hypervolume, which is to be maximized with respect to a finite set of input points. We show that this can be performed using methods based on gradients in a stochastic optimization framework, provided that care is taken with respect to dominated points. Moreover, in the absence of readily available differentiable code, we propose to use Gaussian Processes as differentiable surrogate models, in order to perform the optimization. An additional contribution in this work are some active learning strategies, through acquisition functions which helps construct a surrogate model well-designed for the multiobjective optimization problem at stake. These strategies are compared on simple analytical problems to assess their performances.

---


### 83. [Pretrained Medical Representations for the Practical Screening of Drug Repositioning Candidates](https://arxiv.org/abs/2609.19865)

**<font color=#1a73e8>作者：</font>** Yuhei Fujioka, Daitaro Misawa, Shingo Fukuma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation learning from medical code sequences in electronic health records and medical claims data has been successful in various clinical applications, such as those regarding disease prediction. However, significant challenges remain in extending this approach to the discovery of scientific hypotheses. One reason is that many existing BERT-based models fail to adequately capture the hierarchical structure of medical codes and the complex interactions between diagnoses and treatments. To address these limitations, we propose a new unified pre-training framework that explicitly integrates hierarchical sub-token aggregation, partial masking, and cross-reference mechanisms. The proposed model consistently outperformed existing methods on both pre-training objectives and downstream clinical event prediction tasks, including the onset of dementia and hospitalization. We also conducted an in silico drug repositioning case study targeting Alzheimer's disease. In the hypothesis generation step, our approach successfully rediscovered known promising drugs in a data-driven manner without relying on such external knowledge sources as the literature. Subsequently, in the hypothesis prioritization step, we introduced a Task-Adaptive Representation Approach to alleviate the over-encoding of historical prescription information within diagnostic vectors, enabling the robust prioritization of generated hypotheses. This study establishes an exploratory screening workflow for hypothesis generation and prioritization based on observational associations. Importantly, this framework is not intended to provide causal evidence, but rather to identify promising candidates for subsequent rigorous causal inference. Overall, this study demonstrates that domain-informed representation learning combined with task-adaptive representation control can enable a practical hypothesis discovery workflow.

---


### 84. [Socialized UAV Cross-Task Learning: Towards Cross-Granularity Collaboration through Hierarchical Interaction](https://arxiv.org/abs/2609.19867)

**<font color=#1a73e8>作者：</font>** Xinjie Yao, Ruipu Zhao, Yunqi Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint learning across heterogeneous tasks is often treated as task coupling through feature sharing, distillation, or auxiliary supervision. However, in cross-task learning, mismatched representational and supervisory granularities make such coupling prone to interference, teacher bias, or unidirectional collapse. We argue that cross-granularity learning is fundamentally a problem of hierarchical interaction regulation rather than simple task coupling. This issue is particularly evident in UAV perception, where visual shifts and detection--segmentation objectives naturally form coarse- and fine-grained knowledge sources. To systematically study this problem, we introduce CrossUAV, a UAV benchmark for joint object detection and instance segmentation that provides a unified evaluation platform for cross-granularity task collaboration. To address these challenges, we propose Cross-Granularity Socialized Collaboration (CGSC), a progressive and adaptive framework that regulates when, where, and how tasks exchange information across network hierarchies. CGSC progressively activates cross-task interactions and adaptively adjusts the strength according to task contribution, suppressing harmful interference while exploiting complementary coarse- and fine-grained structures. Extensive experiments demonstrate consistent improvements on both tasks, validating hierarchical dynamic interaction as an effective mechanism for cross-granularity collaboration.

---


### 85. [Physical knowledge on historical data matters more than enforcing physical constraints on the forecast](https://arxiv.org/abs/2609.19871)

**<font color=#1a73e8>作者：</font>** Etienne Lehembre, Pascal Audigane, Vincent Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series forecasting has seen signicant advancements with the emergence of new deep learning models. However, forecasting time series in applications involving physical processes remains a major challenge. Despite the apparition of Physics Informed Neural Networks (PINN), recent models do not estimate unobservable intermediate physical variables, which are important for domain experts to understand the target behavior. To this end, we propose a Physics Informed Recurrent Neural Network (PIRNN) which predicts, along the target, unobservable variables on both historic data and forecast target. This approach enhances the model robustness and results interpretation using domain knowledge. Our method is easily adaptable to any physical model using several equations, each having its own set of unobservable variables, to describe it-self. As a case study, we incorporate physical equations used for groundwater levels predictions by the physical model called Gardenia. This model uses transfers equations between reservoirs, optimized with data assimilation, to simulate the evolution of groundwater levels. Evaluation includes several well known neural network models and the Gardenia model compared on twelve real world datasets. In addition, we study the impact of each component through an ablation study. Our model outperforms other models on ve out of the twelve datasets and our ablation study underlines the importance of having a physical background in our time series forecasting task. Finally, the coherence of the physical variables predicted by our neural network is assessed by a domain expert.

---


### 86. [PART: Learning 3D Part Assembly and Retrieval with Transformers](https://arxiv.org/abs/2609.19872)

**<font color=#1a73e8>作者：</font>** Ruchao Bao, Wenzheng Wu, Chucheng Xiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D assembly is fundamental to modern manufacturing and digital content creation. In this paper, we present PART, a unified transformer-based framework for 3D part retrieval and assembly: given a target shape and a part library, PART automatically selects the appropriate parts and predicts their 6-DoF poses to reconstruct the target. While prior work has achieved impressive progress on assembling a pre-defined set of parts, this more practical retrieval-based setting remains largely unexplored. The task faces three key challenges: (i) a combinatorially explosive search space that grows exponentially with library size; (ii) variable-length outputs, as different targets require different numbers of parts; and (iii) continuous 6-DoF pose estimation for part assembly. To address these, we formulate retrieval and assembly as a set prediction problem and design a novel transformer-based framework that retrieves parts and regresses their poses with variable-length output. Additionally, we exploit the duality between part pose estimation and target segmentation through joint training and a novel segmentation-enhanced optimization module. Finally, We curate a large-scale dataset of 80K+ shapes, and the results show that PART generalizes to scene layouts, image targets, and real-world scans. Project Page: this https URL.

---


### 87. [BINDER: A Latent Variable Model for Probabilistic Medical Image Registration](https://arxiv.org/abs/2609.19875)

**<font color=#1a73e8>作者：</font>** Stefano Cerri, Amirhossein Hassankhani, Yaël Balbastre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a new probabilistic model for general-purpose medical image registration that builds upon the mutual information registration criterion. It centers around a spatial interpolation technique that assumes latent voxel-wise correspondences between the images being registered. By exploiting these latent variables, we derive dedicated optimization and MCMC sampling techniques that only involve closed-form iterative updates. When applied to nonlinear registration, an efficient demons-like optimization algorithm is obtained that shows robust out-of-the-box performance across a variety of monomodal and multimodal registration tasks. We also demonstrate a corresponding sampler that can quantify, for the first time, uncertainty in multimodal registration scenarios with very high-dimensional 3D deformations. Our code, which we call BINDER (Bayesian INference for DEformable Registration), is freely available at this https URL.

---


### 88. [SlugTrails: An Egocentric Benchmark for Floor Plan Localization in Large Buildings](https://arxiv.org/abs/2609.19876)

**<font color=#1a73e8>作者：</font>** Yunqian Cheng, Roberto Manduchi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Floor-plan-based indoor visual localization enables infrastructure-free positioning, but most methods are developed and evaluated in small residential environments unlike the large public buildings of real deployment. We introduce SlugTrails, a floor plan localization benchmark for large indoor spaces under realistic egocentric sensing: $30$ Hz Aria glasses recordings across three campus buildings and six floors ($22089$ m$^2$ of floor plan outline), CAD-derived floor plans with semantic classes and circulation space masks, and trajectories aligned into the floor plan frame using laser-surveyed anchors. One protocol covers three practical ways of gathering geometry under a limited field of view -- a single walking frame, a stationary multi-view sweep, and a walking stream with odometry -- so methods designed for different regimes are compared on the same buildings and ground truth. Evaluating five representative geometric and learned systems under their native sensing configurations, we find that stock checkpoints (official released weights) are near zero on SlugTrails (at most $0.004$ R@1m30$^{\circ}$ on walking single frames), while fine-tuning on SlugTrails improves every trainable family on all three tasks (e.g., F$^3$Loc $0.0 \rightarrow 0.141$ single-frame and $0.03 \rightarrow 0.66$ sequential), with gains compounding as observations accumulate. The same fine-tuned weights also improve cross-dataset generalization on LaMAR with no LaMAR training (sequential R@1m $0.048 \rightarrow 0.143$ for F$^3$Loc and $0.063 \rightarrow 0.127$ for UnLoc), whereas train-from-scratch on SlugTrails alone stays far below fine-tuning from stock weights -- evidence that floor plan localization is currently limited by indoor data rather than by architecture. We release the dataset, protocols, and tools at this https URL.

---


### 89. [BinoGen: Scaling egocentric binocular data for embodied visual perception and learning](https://arxiv.org/abs/2609.19881)

**<font color=#1a73e8>作者：</font>** Chunpeng Li, Ya-tang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied visual perception relies on temporally coherent visual experience accumulated through continuous engagement with the environment. However, collecting large-scale egocentric binocular observations together with dense annotations remains costly and difficult. Moreover, visual experience is shaped not only by the environment but also by the embodiment of the observer, including viewing height, field of view, binocular geometry, and motion through the scene. To address these challenges, we present BinoGen, an automated framework for generating large-scale, embodiment-aware egocentric binocular visual experiences in indoor environments. BinoGen jointly models environmental and observer variation through generative scene synthesis, probabilistic object instantiation, appearance randomization, stochastic trajectory generation, and configurable binocular camera setups. The framework produces synchronized binocular videos together with dense multimodal supervision, including depth maps, optical flow, surface normals, semantic maps, object coordinates, and camera poses. Using BinoGen, we construct a dataset comprising more than 20 million annotated images for supervised learning. We demonstrate two complementary utilities of BinoGen. First, incorporating BinoGen data consistently improves real-world visual perception, including depth estimation, object detection, and video object tracking. Second, paired human-inspired and mouse-inspired observations from the same environments enable controlled investigation of how observer embodiment affects perceptual learning. Embodiment-specific adaptation substantially improves performance, while joint training enables a single model to perform competitively across both embodiments. Together, these results demonstrate that large-scale, controllable visual experience can improve embodied perception...

---


### 90. [Evaluating Communicative Success in Machine-Translated Conversation](https://arxiv.org/abs/2609.19885)

**<font color=#1a73e8>作者：</font>** Faiz Ghifari Haznitrama, Alice Oh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpreter agents built on machine translation (MT) increasingly mediate live conversation between people who do not share a language, yet we still evaluate them with metrics built for isolated sentences, which measure fidelity rather than whether communication succeeds. We introduce a reusable three-layer checklist-and-judge framework that evaluates interpreter-mediated conversation across semantic, pragmatic, and cultural-social dimensions, covering the naturalness, intent, and social appropriateness that fidelity metrics leave unmeasured. It runs in both single-turn and interactive multi-turn settings, where simulated users reply to translated messages as the conversation unfolds and each turn is scored alongside the conversation as a whole. We extensively validate it through controlled perturbations, cross-judge comparisons, and human annotations. Our main single-turn benchmark evaluates 10 interpreter setups across Arabic, Bengali, Indonesian, and Korean from 5,624 OpenSubtitles-derived scenarios spanning 12 translation directions, and our multi-turn study covers all 6 language pairs in scripted and live modes. Results show a consistent decline from semantic to pragmatic and cultural-social success, while conventional MT metrics overlook failures among stronger interpreters, and prompt ablations show that scenario context, structured instructions, and cultural context improve communicative success, although gains vary across setups. Our work thus provides an evaluation framework and benchmark for interpreter agents in conversation, and highlights the importance of communicative success alongside existing translation metrics.

---


### 91. [Online Adaptive Kernel Mixing for Gaussian Process Decision Making](https://arxiv.org/abs/2609.19891)

**<font color=#1a73e8>作者：</font>** Kavin Aravindan, Mani Tej Sriram, Gautam Dasarathy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian Processes (GPs) are widely used as surrogates for black-box functions in sequential decision-making problems such as Bayesian optimization (BO), level set estimation (LSE), and Bayesian active learning (BAL). GP performance critically depends on kernels, and standard kernels can lead to suboptimal decisions under misspecification. To address this, we introduce HACK GPs (Hedge Adaptive Cumulative Kernels), a method that views kernel selection as an online learning with expert advice problem. HACK treats each candidate kernel as a GP "expert" and updates a distribution over experts online using AdaHedge, based on a loss received as a proxy for their ability to fit the function and align with the task objective. We provide two variants of HACK: (i) Mixture of Gaussians (MoG) and (ii) categorical sampling. We establish general guarantees showing that, under a loss-gap condition, the weight concentrates on the best kernel and the resulting acquisition function is close to that of the best expert. Empirically, we observe robust performance across BO, LSE, and BAL compared to standard kernels such as Squared Exponential and Matern-5/2, as well as simple ensemble baselines.

---


### 92. [Hopper: Bounded-Memory Collaborative Debiasing for Byzantine-Tolerant Peer Sampling](https://arxiv.org/abs/2609.19893)

**<font color=#1a73e8>作者：</font>** Joachim Bruneau-Queyreix, Laurent Reveillère, Augusta Mukam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Byzantine-tolerant peer sampling relies on continuously refreshed views, yet an adversary can bias the identifier streams used to construct them. Frequency-aware debiasing downweights overrepresented identifiers, but existing designs rely on cumulative per-identifier counts. We show that even exact, unbounded counters fail under a delayed balanced attack, in which a long benign prefix masks a subsequent adversarial frequency shift. We introduce Hopper, a bounded-memory debiasing protocol for Byzantine-tolerant peer sampling. We identify the stream-estimation properties required for debiasing and select BitMatcher as the estimator that best preserves adversarial frequency structure among the evaluated alternatives. Hopper adds BMDecay, a saturation-triggered decay and reconstruction mechanism that keeps this signal fresh over long executions. Hopper also supports trusted collaboration through authenticated fingerprint-aware reconstruction and role-specific debiasing. Experiments show that Hopper recovers from delayed attacks faster than when relying on BitMatcher, and debiaising as well as non-debiasing baselines under a fixed memory budget. Trusted collaboration reduces post-attack pollution peaks but creates a re-identification trade-off at high trusted-node densities. These results show the importance of occurence freshness, rather than exact counting alone, as a key requirement for practical frequency-aware Byzantine peer sampling.

---


### 93. [Delphi Scanner: efficient and interpretable static malware detection via API sequence modeling](https://arxiv.org/abs/2609.19900)

**<font color=#1a73e8>作者：</font>** Bijied Brahimi, Vincent Cohadon, Gabriel Glazman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static malware detection for Windows Portable Executable files demands a careful balance between detection effectiveness, computational efficiency, and analytical interpretability. This paper introduces Delphi Scanner, a static malware detection system for Windows PE files that balances efficiency with behavioral interpretation. It uses a convolutional neural network (CNN) to model Windows API sequences to classify PE and a decoupled interpretation layer based on a rule-based layer to categorize APIs into high-level malicious capabilities. Evaluated on over 190,000 Windows PE files, the system achieves 95.35% accuracy with a 1.53~MB model footprint. Robustness experiments on 5,647 out-of-distribution MalwareBazaar samples, paired packed and unpacked executables, and three adversarial manipulation strategies confirm generalization beyond the training distribution and resistance to functionality-preserving evasion techniques. Overall, these results demonstrate that API sequence-based static analysis offers a practical, interpretable, and efficient foundation for malware triage in local deployment scenarios.

---


### 94. [GS-PI: An Optimization-Decoupled Appearance Decomposition Approach for Generating PBR Gaussian Assets](https://arxiv.org/abs/2609.19907)

**<font color=#1a73e8>作者：</font>** Jieting Xu, Rengan Xie, Zijian Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting (GS) excels at novel-view synthesis but encodes baked-in radiance, tightly entangling illumination with geometry and preventing seamless integration into physically based rendering (PBR) pipelines. Existing inverse-rendering methods attempt to disentangle materials via joint optimization, but often suffer from competing objectives that cause severe ambiguities and residual lighting artifacts. To overcome this, we present GS-PI, a novel optimization-decoupled framework that casts PBR material generation as a geometry-conditioned diffusion process on 3D point clouds. By operating directly in the 3D domain, our method inherently guarantees multi-view consistency, sidestepping the severe pixel correspondence issues that challenge 2D diffusion approaches. We introduce a multi-scale cross-view conditioning mechanism that integrates three complementary components: a global semantic prior, source-anchored photometric cues, and an absolute spatial learned view-direction conditioning signal. This design efficiently compresses complex multi-view evidence, mitigating cross-view projection misalignment and successfully preventing specular highlights from baking into intrinsic colors. By extracting a point cloud from a pre-trained Gaussian model, predicting PBR attributes via conditional diffusion, and distilling them back through differentiable rasterisation, we yield a fully relightable PBR-GS asset. GS-PI outperforms recent inverse-rendering baselines while replacing per-scene joint illumination/BRDF optimization with a learned diffusion pass followed by a short target-driven distillation, without requiring proxy meshes.

---


### 95. [CitySTAR: Structured and Topology-Aware Reasoning for Open-Vocabulary Urban 3D Grounding](https://arxiv.org/abs/2609.19911)

**<font color=#1a73e8>作者：</font>** Shuai Zhang, Hongye Hou, Qinghe Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D grounding aims to localize target entities in complex scenes from natural language and plays a fundamental role in embodied perception and spatial reasoning. However, existing approaches mostly rely on feature similarity or direct matching, making it difficult to connect natural-language intent with the implicit semantic and geometric structures hidden in billion-scale urban point clouds. We reformulate city-scale 3D grounding as structured constraint reasoning, where description semantics are organized into computable cross-modal constraints over open-vocabulary 3D entities, attributes, and spatial relations. We present CitySTAR, a training-free framework for reasoning-driven urban 3D grounding. CitySTAR lifts raw billion-scale urban point clouds into a query-ready scene graph of open-vocabulary 3D instances, with CodeLLM-driven tools supplying multimodal evidence for node attributes and 3D spatial relations. It then models target-context topology with paired hypergraphs and performs bidirectional topology verification for structural disambiguation. Finally, a Reflective Cross-modal Grounding module integrates topology consistency and candidate-centered 2D visual evidence to make decisions over a metric-aware 3D context graph. To further support this setting, we introduce CitySTAR-3D, an enhanced benchmark that improves semantic coverage, instance completeness, bounding-box fidelity, and spatial-relation complexity in city-scale 3D grounding. Extensive experiments show that CitySTAR consistently improves open-world urban 3D grounding while maintaining strong interpretability and generalization.

---


### 96. [Amortizing Physics-Informed Neural Solvers via Graph Hypernetworks](https://arxiv.org/abs/2609.19915)

**<font color=#1a73e8>作者：</font>** Cheng Jing, Abhishek Verma, Kallol Bera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Amortizing physics-informed neural networks (PINNs) across related PDEs requires describing each equation to a reusable solver. Coefficient vectors encode numerical parameters in predefined slots, leaving operator and cross-field assignments implicit. We make these relationships explicit in an operator graph, with nodes for fields, derivatives, terms, and residuals and coefficients retained as term attributes. A graph hypernetwork generates diagonal codes that initialize a meta-trained factorized PINN for each target equation. Meta-training and target-specific adaptation use governing equations and prescribed conditions without solution labels. We compare coefficient-vector, DeepSets-based term-set, and graph conditioning by solution accuracy within a fixed adaptation budget. In scalar convection-diffusion-reaction problems, both term-based descriptors improve high-reaction accuracy, with similar performance. In two-field Fisher-KPP, meta-training sees uncoupled and one-way systems; after 3,000 adaptation steps on unseen two-way coupling, the graph's mean final error is 35.7% below the term set and 67.7% below the coefficient vector. In a fixed-structure capacitively coupled plasma model, the coefficient vector performs best. These results support extending coefficient conditioning with explicit equation relationships for physics-based solver adaptation.

---


### 97. [Mind the Gap: How SBOM Specification Ambiguities Lead to Divergent Software Bills of Materials. An Empirical Tool Study](https://arxiv.org/abs/2609.19920)

**<font color=#1a73e8>作者：</font>** Alan Prado, Olivier Zendra, Philippe Boinot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software Bill of Materials (SBOMs) will become mandatory starting in December 2027 under the European Cyber Resilience Act (CRA) [8]. Although previous studies have highlighted significant differences among SBOM generators, the reasons for these discrepancies remain unknown, as does whether they stem from implementation errors or deliberate design choices.  In this paper, we evaluate three widely used SBOM generators across more than 3,000 JavaScript and Rust projects, using a groundtruth baseline derived from dependency lockfiles.  Our results show that these tools diverge in terms of both dependency coverage and SBOM completeness. Importantly, most of these discrepancies are systematic rather than accidental: they arise from differing assumptions regarding dependency scope, naming, provenance, and representation, while others reflect inconsistent support for fields defined in SBOM specifications.  These findings demonstrate that many of the observed discrepancies cannot simply be ''fixed'': they require clearer standardization. As SBOM generation becomes a legal compliance requirement, the choice of tool itself can influence the resulting SBOM, potentially becoming a source of undetected non-compliance. We argue that future SBOM standards should define canonical rules regarding dependency scope, provenance, and representation to improve interoperability and compliance.

---


### 98. [DirtyMoCap: Robust Motion Capture from Unconstrained Markers](https://arxiv.org/abs/2609.19927)

**<font color=#1a73e8>作者：</font>** Long Wang, Shuting Zhao, Shen Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical motion capture delivers high-fidelity human motion, but its reliance on strict marker layouts and clean trajectories severely limits its real-world applicability. In practice, tracking systems frequently output unconstrained markers: sparse, noisy, and unordered point clouds with unknown or varying configurations. To bridge the gap between corrupted raw markers and parametric human models, we introduce DirtyMoCap, a robust, marker-layout-free framework. Our core insight is to map unordered marker observations to a fixed set of "proxy anchors" comprising skeletal joints and body surface points, which serve as a stable intermediate representation. We first initialize and track these anchors over long sequences using a recurrent sliding-window architecture. Then, a custom differentiable Gauss-Newton solver fits the SMPL-H model to the tracked anchors to recover full-body pose, translation, and shape. By explicitly deriving geometric residuals, our solver learns adaptive observation confidence, smoothness, and prior weights end-to-end, adapting dynamically to the reliability of the input data. Extensive experiments on diverse, noisy marker configurations demonstrate that DirtyMoCap successfully generalizes across arbitrary layouts using only a single trained model. It consistently outperforms state-of-the-art configuration-specific baselines in both joint and vertex reconstruction accuracy, while our custom CUDA solver achieves up to a 100x speedup over standard PyTorch implementations. We further apply DirtyMoCap to heterogeneous raw optical MoCap recordings of traditional Chinese martial arts, yielding a Kung Fu motion dataset of temporally coherent SMPL-H reconstructions. Code and data are available at this https URL.

---


### 99. [On the Leakage of Massey Secret Sharing Schemes under Linear Computations](https://arxiv.org/abs/2609.19929)

**<font color=#1a73e8>作者：</font>** Nadja Aoutouf, Daniel Augot  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Leakage attacks on secret sharing schemes exploit partial information about individual shares to recover the underlying secret. In coding theory, linear exact repair schemes (LERSs) enable the recovery of one codeword symbol from a small amount of information obtained from the remaining symbols, provided that the code has sufficiently low rate. This can be interpreted as recovering the secret from partial information, namely subfield symbols, of the shares. Recently, a randomized construction based on subfield subcodes was proposed for constructing LERS-derived leakage attacks against Massey secret sharing schemes based on general linear codes. We extend this framework to multiple shared secrets whose corresponding shares are related through linear computations, with leakage also allowed on the computation outcomes. More precisely, we consider N secrets, of which K $\le$ N are linearly independent input values and the remaining N -K secrets are determined by linear computations on these inputs. We analyse the existence of LERS-derived leakage that exploits this structure. We first study the case of addition and then generalize our construction to arbitrary linear computations. Our analysis applies to general linear codes of length n+1 and dimension k over F\_{q^m} with k $\le$ N n/(Km), and supports arbitrary linear computations, whereas the previous subfield subcode construction only applies to k $\le$ n/m -1. Consequently, exploiting the linear relations enables LERS based leakage which extend the range of code parameters vulnerable to such attacks. Finally, identical leakage functions can arise for certain linear relations, making this a more realistic yet still potentially powerful attack model. Finally, simulations indicate that identical leakage functions can be used for certain linear relations, yielding a more realistic attack model.

---


### 100. [One Intervention per Component is Enough: Towards Identifiability in Linear Stochastic Dynamics from Steady State](https://arxiv.org/abs/2609.19955)

**<font color=#1a73e8>作者：</font>** Saber Salehkaleybar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of recovering the parameters of a multivariate Ornstein-Uhlenbeck (OU) process from steady-state observational and interventional data. In many applications, such as large-scale gene perturbation experiments, only stationary "snapshot" measurements are available, making standard stochastic differential equation estimation methods that rely on time-series trajectories inapplicable. We first establish an identifiability result: one intervention per strongly connected component (SCC) of the drift graph suffices to recover all OU process parameters generically up to a global scaling factor. This holds provided that the SCC condensation graph is connected with a single root and certain spectral nondegeneracy assumptions hold. We propose a recursive learning algorithm that orders SCCs topologically and, for each component, isolates its marginal dynamics and solves a linear system derived from the steady-state moment equations, leveraging parameters recovered for upstream components. Building on this theoretical foundation, we propose a regularized least-squares estimator that jointly minimizes residuals of the steady-state mean and covariance equations across observational and interventional data. Experimental results validate our theoretical findings in recovering parameters of the underlying OU process.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-247](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
