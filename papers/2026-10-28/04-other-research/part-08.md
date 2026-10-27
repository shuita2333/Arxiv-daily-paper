# 📦 其他研究 | 2026年10月28日

> 本类共 **446** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-446](./part-09.md)

---

### 351. [Efficient Exact Unlearning for Federated Zeroth-Order Optimization](https://arxiv.org/abs/2610.35211)

**<font color=#1a73e8>作者：</font>** Weijun Yin, Yanqing Yao, Falko Dressler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated zeroth-order optimization (FedZOO) reduces the memory and communication costs of collaborative training for edge intelligence by avoiding backpropagation while communicating only random seeds and scalar coefficients. However, existing methods lack efficient mechanisms for exact unlearning to fully remove the influence of training data when users request deletion. A key insight is that total variation stability of the learning algorithm creates overlap between model distributions before and after data deletion, allowing exact unlearning to reuse computation through coupling. Based on this observation, we jointly design two stable zeroth-order learning algorithms and their corresponding exact-unlearning procedures: \textsc{FedZOO-S} obtains stability through client and mini-batch subsampling, enabling \textsc{FedZOUL-S} to perform efficient unlearning by preserving earlier updates and restarting from the first affected step. \textsc{FedZOO-NS} further combines subsampling with Gaussian noise to increase overlap between update distributions; \textsc{FedZOUL-NS} exploits this overlap through rejection--reflection coupling to reuse affected updates when the coupling is accepted. We prove exact unlearning for both algorithms: the model and saved state have the same joint distribution as retraining with the corresponding learner on retained data. We further establish stability and convergence guarantees for the learning algorithms and derive upper bounds on expected unlearning cost. Experiments demonstrate effective unlearning with competitive model utility and up to $56.1\%$ less cumulative unlearning time than re-optimization. Compared with first-order baselines, our methods reduce communication overhead by up to approximately four orders of magnitude.

---


### 352. [One-Shot Federated Model Editing for Device Dynamics at the Edge](https://arxiv.org/abs/2610.35212)

**<font color=#1a73e8>作者：</font>** Youming Tao, Weijun Yin, Huanyi Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard federated learning (FL) requires persistent device connectivity across multiple communication rounds, making it unsuitable for dynamic environments such as vehicular networks, where devices frequently join and leave. One-shot FL offers a promising alternative by completing training in a single communication round. However, one-shot FL suffers from model solidification and cannot readily adapt to subsequent client dynamics, including new client contributions and the withdrawal of previous contributions. We therefore consider exact model editing, which removes withdrawn contributions through unlearning or incorporates newly contributed ones through incremental learning without retraining from scratch. We identify that efficient editing fundamentally hinges on learning stability. To this end, we propose F-SOSA, the first stable one-shot FL algorithm that enables rapid and exact model editing. F-SOSA leverages sub-sampling of local models with carefully tuned rate for stable aggregation and performs curvature-aware model fusion to preserve utility. We prove that F-SOSA achieves vanishing training error and reasonably small generalization error bounds. Building on this stability, we further develop two single-round editing algorithms: F-SOSA-U for unlearning and F-SOSA-I for incremental learning. They ensure that the edited model, along with all intermediate algorithmic states, is statistically indistinguishable from retraining while incurring only an expected $O(\rho)$ fraction of its cost, where $\rho$ quantifies stability. Experiments demonstrate that our approach matches retraining performance while reducing cumulative time and communication overhead by at least 36% and 22%, respectively, under realistic urban mobility simulations.

---


### 353. [MuSID-KD: Multigranularity Knowledge Distillation for Generative Recommendation with Semantic IDs](https://arxiv.org/abs/2610.35218)

**<font color=#1a73e8>作者：</font>** Fengshi Zhang, Xiyan Ding, Shuxiao Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative recommendation with semantic IDs (SIDs) represents each item as a sequence of discrete tokens and autoregressively predicts the next item's SID. Despite strong recommendation performance, repeated decoding over multiple SID positions incurs substantial inference cost. Knowledge distillation transfers knowledge from a powerful generative teacher to a lightweight student, yet conventional objectives do not fully account for multi-token SID generation. We identify two limitations: item-level distribution alignment may not adequately preserve the teacher's ranking of candidate groups sharing SID prefixes, while uniform alignment across SID positions may affect final item ranking differently. We propose MuSID-KD, which combines Hierarchical Candidate Distribution Alignment (HCDA) and Ranking Impact Guided Levelwise Distillation (RIGD). HCDA aggregates item probabilities according to shared SID prefixes and aligns candidate distributions at successive levels, from candidate groups to individual items. RIGD evaluates the reduction in pairwise ranking surrogate loss when one student score contribution is replaced with the teacher's contribution, and allocates supervision accordingly. Experiments on real-world recommendation datasets using three lightweight student architectures demonstrate improved recommendation accuracy and better alignment of prefix marginal distributions and pairwise item rankings, without modifying the student's online inference architecture. Code is available at this https URL.

---


### 354. [Multi-Agent Relay Thinking](https://arxiv.org/abs/2610.35219)

**<font color=#1a73e8>作者：</font>** Xu Liu, Jungang Qiao, Guikun Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing multi-agent collaboration (MAC) methods have primarily explored a group thinking collaboration topology, where agents independently generate solutions and aggregate their outputs. In this work, we investigate an alternative relay thinking topology, where reasoning ownership is dynamically transferred across agents, allowing subsequent agents to inherit and refine an evolving reasoning trajectory. We introduce Multi-Agent Confidence-guided Relay (MACR), a framework that enables dynamical relay collaboration among agents. The key challenge is determining when reasoning should be relayed and which agent should continue the process. method addresses this challenge through confidence-guided relay triggering and a bidding mechanism that selects the next agent based on its confidence. Experiments on four benchmarks show that method outperforms the strongest single-model strategies in accuracy, e.g., +3.3% on MathVista and +3.9% on MMStar, and remains on par with multi-agent strategies while consuming 6.0x less token overhead on HallusionBench and this http URL analysis demonstrates that relay collaboration enables heterogeneous agents to progressively integrate complementary insights, combining heterogeneous capabilities across reasoning stages. Our source code is available at this https URL.

---


### 355. [O2D-MedNet: An Optimization-Aware Dual-Domain Framework for Robust Medical Image Segmentation](https://arxiv.org/abs/2610.35220)

**<font color=#1a73e8>作者：</font>** Shipeng Hu, Miaohui Wang, Jing Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation (MIS) remains challenging due to composite degradations and multi-scale geometric variations, which jointly impair lesion-background separability, structural consistency, and optimization stability. Existing single-stream frameworks entangle heterogeneous cues within a single representation pathway, while hybrid-stream approaches often rely on generic or static fusion, limiting effective coordination across domains and failing to explicitly address optimization instability. To overcome these limitations, we propose a new optimization-aware dual-domain framework for MIS (O2D-MedNet). First, a degradation-aware dualdomain interaction (DDI) module integrates Fourier - and Wavelet-domain features to suppress degradation-sensitive responses while preserving structural and fine-detail information. Second, a cross-backbone contour-guided fusion (CGF) module enables selective interaction between CNN-based local detail modeling and visual state-space-based global structure modeling, improving boundary accuracy and representation consistency. Third, a gradient-context optimization (GCO) strategy stabilizes training by adaptively adjusting learning dynamics based on loss trends and gradient statistics, mitigating instability caused by class imbalance and heterogeneous sample difficulty. Extensive experiments on six benchmarks demonstrate consistent improvements over state-of-the-art MIS methods across multiple imaging modalities. Further analyses confirm enhanced sensitivity, structural consistency, and optimization stability, validating the effectiveness of the proposed O2D-MedNet for robust MIS under heterogeneous conditions.

---


### 356. [Joint Latent Reasoning and Observation for Agentic Video Understanding](https://arxiv.org/abs/2610.35229)

**<font color=#1a73e8>作者：</font>** Junzhang Liu, Hao Yuan, Qi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective video agents must learn not only how to answer, but also where to look next. Transferring this capability to smaller models is challenging because each observation serves two purposes: supporting an answer and guiding the search for further evidence. Textual descriptions may capture what is currently visible while omitting cues needed for subsequent acquisition. We introduce Latent Agentic Reasoning for Video Analysis (LARVA), a framework that distills multi-round video agents through jointly learned latent reasoning and visual observations. Rather than communicating through captions, an observer passes compact continuous representations to a reasoner that selects the next acquisition action or produces the final answer. Crucially, action and answer supervision propagate through this interface, training the observer to communicate information useful for downstream decisions. Observation reconstruction and reasoning-distribution alignment provide auxiliary supervision from textual teacher trajectories. Across five video-understanding benchmarks, LARVA achieves strong performance with 4B and 7B backbones. On VideoHolmes, Video-MME, and LVBench, the 7B model outperforms a textual CoT student trained on the same teacher trajectories by 5.1, 2.5, and 3.7 percentage points, respectively. These results highlight the value of jointly learning how agents represent evidence and act on it when distilling video-understanding capabilities.

---


### 357. [False-Alarm Improvements and Detection Trade-Offs in QML Intrusion Detection: A Secondary Analysis of the Kaissar Corpus](https://arxiv.org/abs/2610.35235)

**<font color=#1a73e8>作者：</font>** Roberto Fernández-Barrios, Iker Pastor-López, Asier González-Santocildes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Published results in quantum machine learning for intrusion detection (QML-IDS) require joint interpretation of false-positive rate (FPR), attack true-positive rate (TPR), and evaluation provenance. We reconstruct operating points in the 25-entry frame selected by Kaissar and colleagues: 21 included articles, 20 identified documentary families, substantive methodological material consulted for 15, and 24 descriptive points from five. In one test-labelled comparison, a quantum support vector machine reduces FPR from 6.875% for random forest to 3.329%, while TPR decreases from 93.955% to 93.682%; both rates improve against three other comparators. In another study, a complete benign row identifies FPR as 12/6000 (0.200%), despite incomplete attack-side allocation that requires additional assumptions for TPR. Normalized matrices identify detection ranges rather than a unique aggregate rate. A uniform provenance rule separates training-described and test-adjusted results from six conditional illustrations whose independence remains unverified. The contribution is a reproducible interpretation of favorable comparisons and detection trade-offs, without converting descriptive results or hypothetical calculations into operational guarantees.

---


### 358. [NOMAD-EEG: Native Omni-Montage Adaptive Diffusion](https://arxiv.org/abs/2610.35246)

**<font color=#1a73e8>作者：</font>** Abdulkader Helwan, Khadidja Henni, Lina Abou-Abbas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Purpose. Electroencephalography (EEG) montages, channel counts and recording lengths vary widely, but most EEG foundation models are bound to the channel set and input length they were trained on. We aimed to build a generative EEG foundation model independent of the number, identity and order of electrodes and of the input length. Methods. NOMAD-EEG is a 12.0 M-parameter diffusion model that alternates state-space layers along time, without patches, with attention across electrodes identified only by their 3D scalp position. It was pre-trained on 147 h of unlabelled EEG from a single corpus and evaluated with frozen linear probes on ten datasets with 1 to 64 electrodes against seven foundation models run under one protocol, and on two unseen populations. Results. Despite its small size (12.0 M parameters against 69 M for REVE) and single pre- training corpus, NOMAD-EEG outperformed all seven foundation models on EEGMMIDB mo- tor imagery (balanced accuracy 0.442), Siena seizure detection (macro F1 0.622) and Bonn seizure detection (AUROC 0.999), had the highest accuracy of the seven compared models on TUEP epilepsy diagnosis (0.640) and, after fine-tuning, the highest \k{appa} (0.635) and weighted F1 (0.814) on TUEV event classification. It was the best of five models on P300 detection in autism with an unseen eight-electrode montage (AUROC 0.718). With only 5 of 19 electrodes, its mean AUROC fell only from 0.942 to 0.891. Conclusion. Identifying electrodes by position and modelling time without patches let one small model, pre-trained on one corpus, outperform much larger EEG foundation models on seizure detection, epileptiform event classification, epilepsy diagnosis and motor imagery.

---


### 359. [Conversational Generalized Linear Bandits with Hybrid Feedback](https://arxiv.org/abs/2610.35262)

**<font color=#1a73e8>作者：</font>** Yurui Zou, Qirun Zeng, Jinhang Zuo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conversational bandits improve recommendations by actively querying users about key-terms to elicit their item preferences. However, existing methods typically assume homogeneous feedback for items and key-terms, using either absolute rewards or pairwise comparisons. In practice, item feedback often takes the form of clicks or ratings, while comparisons are more natural for key-terms. To address this gap, we study conversational generalized linear bandits with hybrid feedback, combining absolute item rewards and relative key-term comparisons. We propose Conversational UCB with Hybrid Feedback (HyConUCB), which constructs unified confidence bounds from heterogeneous feedback and adaptively selects key-term comparisons by balancing information gain and directional coverage. Through a refined regret analysis that jointly exploits both feedback sources, we establish a regret bound that improves upon reward-only and adapted dueling-only benchmarks. Experiments on synthetic and real-world datasets validate the effectiveness of our algorithm.

---


### 360. [Low-rank MERA Decomposition of 3D OCT Image Volume for Compression, Denoising, Feature Extraction and Diagnosis of Retinal Diseases](https://arxiv.org/abs/2610.35271)

**<font color=#1a73e8>作者：</font>** Ivica Kopriva, Fei Shi, Marija Štanfel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical coherence tomography (OCT) is a non-invasive imaging modality used for visualization of retinal tissue. However, OCT volumes are affected by speckle noise, which degrades image contrast and obscures fine structural details. Furthermore, modern clinical practice requires large field-of-view, high-resolution OCT volumes, whose storage and transmission are demanding for archiving and teleophthalmology applications. To address aforementioned challenges, we propose a low-rank multi-scale entanglement renormalization ansatz (MERA) tensor network approximation of 3D OCT image volume, where the image volume is represented as contractions of a top core factor encoding global features and multiple interacting low-rank orthogonal or semi-orthogonal factors modeling inter- and intra-B scan correlations. This representation jointly enables compression, denoising, and feature extraction. Unlike deep learning approaches, the proposed approach is training-free and processes each OCT volume independently. We evaluate the proposed framework on OCT image volumes acquired by two different scanners and demonstrate improved visual quality and reduced retinal layer segmentation errors in comparison with several competing methods. We also extract MERA features from two clinical OCT volume datasets. They are subsequently classified using a Grassmann-manifold nearest-subspace classifier. With the subspace dimension as its only hyperparameter, the classifier is theoretically shown to be robust in small-sample clinical scenario. We demonstrate competitive accuracy of classification of retinal diseases in these small-sample settings, where deep learning methods are often limited by the scarcity of labeled data. The proposed structure-aware model-driven representation learning for high-dimensional data under limited supervision provides good generalization performance while maintaining high interpretability.

---


### 361. [Self-Supervised Pretraining for PHM: What Transfers, What Does Not, and What Federating It Costs](https://arxiv.org/abs/2610.35280)

**<font color=#1a73e8>作者：</font>** José Sanz-Durán, David Solís-Martín  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-supervised pretraining has produced capable time-series foundation models, but its value for Prognostics and Health Management (PHM) has not been measured under leakage-controlled conditions. We measure it on a corpus of 47 public PHM datasets, harmonized to a single tensor contract and partitioned so that 11 datasets are withheld from pretraining in full. Transfer turns out to be task-dependent: a compact channel-independent Transformer encoder (801,808 parameters) pretrained with masked patch prediction raises fault-classification macro-F1 from 0.350 to 0.812 on CWRU and from 0.569 to 0.951 on HSG18, yet on CMAPSS remaining-useful-life estimation no pretrained checkpoint reliably improves upon a from-scratch baseline. We pretrain under two regimes---centralized, and simulated cross-silo federated with ten clients grouped by physical domain---holding architecture, objective, source data and optimization budget fixed. Two further findings are negative. At matched budget the centralized encoder leads by 15.5--20.2 macro-F1 points in four of four comparisons, although the comparison is confounded by a learning-rate schedule that favours the centralized arm and rests on a single pretraining run per regime; on RUL the two regimes are indistinguishable. And the intrinsic SSL loss is not a valid selection criterion: the centralized encoder more than halves the federated reconstruction loss without a corresponding gap on RUL, and a server-momentum sweep moves downstream validation macro-F1 by up to 0.29 while the SSL loss varies by 0.021. Transfer also hinges on the backbone learning rate: the same checkpoint yields 0.169 or 0.829 macro-F1 on CWRU depending on a single order of magnitude. We release the corpus pipeline, the protocol and the code.

---


### 362. [AgenticCity-Bench: Longitudinal Multimodal Observations of Urban Dynamics with Agentic Reasoning](https://arxiv.org/abs/2610.35293)

**<font color=#1a73e8>作者：</font>** Xiaofei Yu, Kailai Sun, Yanyu Mao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> City systems are shaped by interactions among infrastructure, human activity, and environmental conditions. Existing earth observation and urban benchmarks are limited in unified modeling and in capturing their joint dynamics. We introduce AgenticCity-Bench, a longitudinal multimodal benchmark for multi-layer unified state modeling and agentic city task reasoning. The benchmark covers 16 cities in 12 countries across six continents from 2000 to 2025, and includes 18 modalities spanning urban function, activity, and environmental state. It organizes heterogeneous data sources around a common spatial reference and calendar index while preserving spatial and temporal coverage, provenance and tile-level availability. On this foundation, AgenticCity-Bench supports urban cross-modal translation together with diverse agentic city tasks involving forecasting, planning and resource analysis. This study provides a unified benchmark for studying the transition from multimodal urban and earth observation to joint understanding and agentic city decision-making. The dataset is available at this https URL.

---


### 363. [Application of Artificial Intelligence in the Management of Climate Change-Related Health Issues in Africa](https://arxiv.org/abs/2610.35294)

**<font color=#1a73e8>作者：</font>** Peter Kokol, Martha Kachweka, Helena Blazun Vosner 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While climate change disproportionately impacts African public health, AI predictive modeling remains heavily constrained. Using a Synthetic Knowledge Synthesis approach and VOSviewer, we conducted a bibliometric analysis of Scopus-indexed literature, comparing Global and African corpora. Network analysis reveals stark divergences: global research emphasizes complex, predictive models for planetary health, whereas African research focuses on localized, reactive solutions for immediate infectious disease triage. Severe structural barriers in Africa, including compute deficits, data silos, and energy instability, hinder advanced AI scaling. Ultimately, international funding must shift from siloed pilot projects toward building foundational digital infrastructure and localized AI frameworks.

---


### 364. [Inference Latency-Aware Tsetlin Machine Training](https://arxiv.org/abs/2610.35304)

**<font color=#1a73e8>作者：</font>** Yefan Zeng, Shengyu Duan, Rishad Shafik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Tsetlin Machine (TM) is a logic-based machine learning model well suited to low-latency inference on resource-constrained edge devices. Because each clause is an AND over Boolean literals, both the literals and their associated Tsetlin Automaton (TA) actions can be represented at the bit level, enabling bitwise evaluation and an early exit that is triggered as soon as any included literal evaluates to zero, forcing the clause output to zero. In this work, we study how the two TM training hyperparameters, T and s, govern both classification accuracy and inference latency. Building on the inversely proportional T-s relationship along which accuracy is nearly constant, we find that inference latency is reduced primarily by increasing s; rather than exhaustively searching the (T, s) grid at high training cost, we propose a directed search strategy that treats accuracy as a constraint and advances toward larger s to reduce inference latency within a fixed evaluation budget. Experimental results on the gem5 simulator with an ARM processor show that, for certain datasets, the search is able to increase s while preserving the baseline accuracy, thereby reducing inference latency at negligible accuracy cost: across six datasets, the method reduces inference latency by up to 16.34%, while some datasets exhibit an accuracy reduction of only 0.06%. The proposed strategy requires far fewer configuration evaluations than an exhaustive grid search.

---


### 365. [OVM-Occ: Open-Vocabulary Monocular Occupancy Prediction via Geometry-Aware Vision-Language Distillation](https://arxiv.org/abs/2610.35312)

**<font color=#1a73e8>作者：</font>** Shuyang Yu, Haibo Qin, Shaohan Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular occupancy prediction in indoor scenes aims to recover a scene's 3D geometry and semantics from a single RGB image. Existing methods are restricted to a closed set of predefined categories, limiting their ability to generalize to unseen categories. This limitation is particularly critical in indoor scenes, where objects exhibit highly diverse and fine-grained semantic categories. We study open-vocabulary monocular occupancy prediction for indoor scenes and present OVM-Occ, a Gaussian-based occupancy framework with an instance-aware vision-language teacher. Specifically, we adopt Language-Embedded Gaussians as the intermediate scene representation, propose a geometry-aware deformable attention module to refine Gaussian semantic features, and construct instance-level vision-language embeddings to provide reliable semantic supervision. We further introduce geometry-aware decoupled semantic distillation to mitigate the interference between geometry learning and semantic learning. To evaluate open-vocabulary occupancy prediction performance, we introduce OpenOcc-ScanNet and OpenOcc-Replica, two extended benchmarks with more diverse and fine-grained semantic categories. Experiments show that our method achieves state-of-the-art performance in open-vocabulary monocular occupancy prediction for indoor scenes, outperforming the previous state-of-the-art approach by 12.2 mIoU and 0.6 IoU on the Occ-ScanNet dataset, with consistent gains under new open-vocabulary evaluation protocols.

---


### 366. [CoPE-CGL: Community-aware Prototype Extraction for Replay-Free Continual Graph Learning](https://arxiv.org/abs/2610.35313)

**<font color=#1a73e8>作者：</font>** Bo-Young Lim, Seokhwan Kim, Kisung Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual graph learning (CGL) maintains models as graphs evolve without retraining from scratch, while mitigating catastrophic forgetting. Existing methods typically target either transductive or inductive settings and often store past subgraphs or require task identifiers at inference. We propose Community-aware Prototype Extraction for Continual Graph Learning (CoPE-CGL), a replay-free framework that uses a parameter-free structural prior, precomputed by multi-hop Laplacian smoothing, to anchor learning, memory, and inference. CoPE-CGL combines topology-infused bottleneck adaptation, community-level prototypes, and dynamic routing by majority vote over node-to-prototype matches. The default protocol assumes each test graph comes from one learned task; a node-level variant handles mixed-task graphs. Each task adds at most a constant amount of storage, with no past graph data retained. At equal storage and without task identifiers, CoPE-CGL matches the strongest replay baseline even when it receives true task identifiers: average performance (AP) is 95.17% and 95.72% versus 94.28% and 95.82% on Arxiv and CoraFull, respectively, with 5.9-14.0 times faster runtime and zero forgetting. Across four transductive and three inductive benchmarks and mixed streams, CoPE-CGL exceeds the second-best of up to eleven baselines by up to 1.41, 6.32, and 9.33 AP percentage points, respectively. It runs 1.3-7.9 times faster end-to-end than the most accurate competitor on each benchmark and scales to the largest benchmark graph. On graphs mixing two tasks, its node-level variant achieves the best AP among CGL methods. The design targets homophilic graphs with community structure.

---


### 367. [Targeted Deep Regression - Initial Applications in Whole-Body Water-Fat MRI in UK Biobank](https://arxiv.org/abs/2610.35339)

**<font color=#1a73e8>作者：</font>** Filip Marttala, Taro Langner, Johan Öfverstedt 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UK Biobank is a British clinical study which, in addition to large amounts of medical data collected, plans to include detailed Magnetic Resonance Imaging (MRI) examina- tions from 100,000 participants. The image data can be analyzed for example by auto- mated analysis with neural networks for image segmentation or classification to expand the collection of image-derived phenotypes for medical research. In this work, we pro- pose, present and evaluate a methodology that uses image-based regression to estimate numerical properties from the collected neck-to-knee water-fat MRI scans. It applies a ResNet50-style network to 2D multi-channel collages that represent targeted and study- specific anatomical sub-regions from the MRI scan. The targeted sub-region sampling is achieved by propagating manually defined subregions from a reference scan to the other >30,000 analyzed scans using image registration. The resulting collages can be compact while retaining high-resolution, for example by providing multiple slices of kidney tissue for a kidney volume regression network. This approach also enables group-wise saliency analysis that highlight image and anatomical regions used by the network for the pre- dictions. The method was applied for the regression endpoints of kidney volume, heart volume, and age. Predictive performance was found between R2 = 0.731-0.984 and the group-wise saliency maps were found to highlight medically relevant regions. We con- clude that the method can be used to standardize and restrict the information presented to a deep regression analysis pipeline, increasing information density and opening up a wide range of future medical inference studies.

---


### 368. [Should Pseudo-Labels Share Mini-Batches with Labeled Examples? Semi-Supervised Continual Active Learning with Limited Training Cost](https://arxiv.org/abs/2610.35345)

**<font color=#1a73e8>作者：</font>** Shiqi Zhang, Tuomas Virtanen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active learning (AL) reduces annotation by querying informative examples. Continual active learning (CAL) also cuts the training cost, the total number of gradient steps, by training one model across AL rounds with a fixed number of mini-batch steps per round. Pseudo-labels add supervision without annotation, but they increase training cost. In CAL, where every round trains on a fixed number of mini-batches, whether and how pseudo-labeled examples should share these mini-batches with labeled examples is therefore open. We provide the first formalization of this problem as two decisions after each query, namely (i) which unlabeled examples should enter training with a pseudo-label and (ii) what share of each mini-batch they should take. Our method, semi-supervised continual active learning (SSCAL), works with any acquisition function. It admits pseudo-labels based on distances from unlabeled examples to labeled neighbors, caps their share, and reweights the loss on labeled examples to keep their expected gradient contribution unchanged. On frozen embeddings, its pseudo-labeler updates incrementally without extra model forward passes. Across two audio datasets, two frozen encoders, six acquisition functions and ten seeds, SSCAL ranks first on average among four protocols with equal training steps, answering the question affirmatively.

---


### 369. [CVTSplat: Multi-view Reconstruction Using an Adaptive Centroidal Voronoi Tessellation](https://arxiv.org/abs/2610.35347)

**<font color=#1a73e8>作者：</font>** Briac Toussaint, Diego Thomas, Jean-Sébastien Franco 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Voronoi tessellations have recently emerged as an adaptive, space-partitioning discretization for shape and appearance reconstruction from multi-view images. However, the irregular cells they produce make the repeated reconstruction of the tessellation during optimization costly. We therefore explore adaptive centroidal Voronoi tessellations (CVTs), which extend standard CVTs with non-uniform cell sizes while preserving the regular, well-shaped cells that make them efficient to compute. In CVTSplat, cell size is modulated by the evolving signed distance field, concentrating sites near the zero level set while keeping cells nearly centroidal. This regularity lets us specialize the whole pipeline, with GPU algorithms for nearest-neighbor queries and approximate Voronoi construction, and a rasterizer tailored to small, nearly isotropic cells. Our Voronoi construction is 5 to 10 times faster than general-purpose alternatives in this regime. On DTU and BlendedMVS, CVTSplat reaches geometric accuracy competitive with the best Gaussian-splatting surface methods while training in about 2.5 minutes on a single GPU.

---


### 370. [Benchmarking uncertainty quantification for engineering regression under graded distribution shift](https://arxiv.org/abs/2610.35356)

**<font color=#1a73e8>作者：</font>** Ahmad Lawal, Rahim Pasbanigoloojeh, Asmau Lawal Bilbis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models in engineering are often used beyond their training conditions, where reliable uncertainty quantification (UQ) matters most. Existing comparisons of regression UQ methods rely on random splits, which assess calibration only in distribution. We introduce a three-rung shift ladder (in distribution, soft shift and hard shift) built along physically meaningful shift variables, and evaluate 12 methods from five families on seven public engineering datasets: five extrapolation settings, an unseen turbofan fault mode and a winter air-quality sensor deployment. All tuning uses source data only. In distribution, conformal methods cover at least 0.946 of test points on every dataset. Under hard shift, mean coverage falls to 0.40-0.75 across the 11 methods that always return an interval, and no systematic difference in method ranks is detected (Friedman p = 0.63). Weighted conformalised quantile regression stays near nominal on the points it answers, but abstains on 85\% of hard-shift points on average and covers only 0.67 of the few Concrete points it answers. Source-validation gains predict improvement in distribution and under soft shift, but not under hard shift (Spearman's rho = 0.04). Engineering evaluations should split calibration data by deployment unit, report subgroup coverage and sharpness, and treat abstention as an explicit operational outcome.

---


### 371. [Evidence-Guided Selection of Retinal Vessel Segmentation Pipelines: A Cross-Dataset Benchmark of Performance, Structure, Failure Modes, and Reproducibility](https://arxiv.org/abs/2610.35357)

**<font color=#1a73e8>作者：</font>** Ruoyu Yan, Yuejia Liu, Shixin Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal vessel segmentation is widely used in retinal image analysis, yet model selection based only on aggregate overlap scores can overlook structural fidelity, cross-dataset robustness, and application-specific error costs. We evaluated five executable binary vessel-segmentation pipelines (FSG-Net, SA-UNetv2, DCP-1024, GAVE, and FR-UNet) on 244 images from six public datasets using pixel-level agreement, cross-dataset stability, thin-vessel retention, structural metrics, error composition, and available computational evidence. Results were aggregated with equal weighting across datasets. No pipeline was optimal in every setting. FSG-Net achieved the highest equal-dataset mean Macro-F1 (0.77), IoU (0.63), clDice (0.83), and Skeleton F1 (0.78), whereas SA-UNetv2 achieved the highest mean sensitivity (0.85) and Thin-Vessel Sensitivity (0.63). Differences across datasets were often larger than those among the leading pipelines, and errors shared by all five methods were concentrated near annotated vessel boundaries and faint peripheral vessels. In an ancillary analysis on 45 HRF images, segmentation masks were converted into 11 ring-wise vascular features for leave-one-out classification. Controlled perturbations showed that local mask errors can be amplified in downstream features, while targeted stabilization reduced sensitivity for five features. The results support task-conditioned, benchmark-relative pipeline selection rather than a single universal ranking and highlight the need to validate the selected pipeline on the intended target domain.

---


### 372. [Agreement Between Reconstructed and Native GDELT GKG Records: A Field-Level Baseline](https://arxiv.org/abs/2610.35358)

**<font color=#1a73e8>作者：</font>** Nikita A. Klimin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Global Knowledge Graph (GKG) of the Global Database of Events, Language, and Tone (GDELT) characterizes news articles using named entities, topics, quantitative and temporal features, quotations, tone, and dictionary-based content measures. Its codebook defines the record format, but the software that produces the records is not public, so researchers cannot generate compatible records for articles they collect themselves. We built an open-source reconstruction, gdelt-regkg, and measured how closely it agrees with GDELT's archived (native) records for 193,550 English articles from 8,729 publishers (2020-2025) and 2,500 articles in five other languages. Agreement depends strongly on the field. English tone, the percentage of positive minus negative words, has a mean absolute error (MAE) of 1.79 points and a concordance correlation coefficient of 0.75. Identity agreement (F1) is 0.65 for persons, 0.42 for organizations, and 0.65 for locations. It is lower for date components (0.42), complete counts with their objects and locations (0.07), and quotations (0.07), while GCAM category presence reaches micro F1 0.84 within the implemented dictionaries. In subsets where retrieved and native titles and lengths match, tone error falls to 1.47 and organization F1 rises to 0.48, yet most disagreement remains. A larger gazetteer raises coverage of native places from 89.5% to 97.1% with little change in location F1. Tone computed on English translations of non-English articles is less accurate (MAE 2.10-2.64) than for English articles. The results are conditional on article pages that could still be retrieved, and the correspondence subsets do not isolate the effect of input differences. Reconstructed records should therefore be assessed field by field and not treated as completely interchangeable with native ones.

---


### 373. [SG-Splat: Stable Geometry Learning under Pose Uncertainty for Pose-Free 3D Gaussian Splatting](https://arxiv.org/abs/2610.35361)

**<font color=#1a73e8>作者：</font>** Xiaohan Lu, Jiaqi Zhang, Weijia Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has become a promising representation for real-time novel view synthesis and 3D scene reconstruction. For practical deployment, recent studies have explored pose-free feed-forward 3DGS, which reconstructs Gaussian representations directly from unposed input images. However, these methods remain sensitive to residual pose errors, which perturb canonical-space Gaussian transformation, introducing noisy supervision for geometry and attribute learning. To address this problem, we present SG-Splat, a pose-free feed-forward 3DGS framework that improves robustness to pose uncertainty and stabilizes the learning of Gaussian primitives. SG-Splat decouples geometry estimation and Gaussian attribute prediction into two dedicated branches, reducing error coupling between pose-sensitive geometry and Gaussian attributes. We further introduce a coarse-to-fine refinement pipeline, consisting of Flow-Guided Pose Refinement (FGPR) and Residual-Guided Geometry Correction (RGC), to improve geometric alignment before Gaussian attribute reconstruction. Specifically, FGPR refines camera poses with flow-based correlation features and differentiable bundle adjustment. RGC then corrects initial point maps using depth residuals derived from FGPR, producing more reliable Gaussian centers. To stabilize training, we introduce a dual-path strategy that mixes ground-truth and predicted poses for canonical transformation. It provides clean supervision for Gaussian attributes while improving geometry robustness to residual pose errors. Extensive experiments on DL3DV and RealEstate10K show that SG-Splat achieves state-of-the-art performance in both novel view synthesis and pose estimation.

---


### 374. [Shared-Factor-Conditioned Diffusion for Low-Rank Tensor Recovery](https://arxiv.org/abs/2610.35368)

**<font color=#1a73e8>作者：</font>** Zhengyun Cheng, Guanwen Zhang, Wei Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tensor recovery spans heterogeneous data structures and observation processes, calling for a representation that can adapt across modalities and tasks. We propose DiffTR, an unsupervised framework that unifies tensor completion, denoising, and hyperspectral super-resolution through coordinate-conditioned diffusion. Shared factors indexed by tensor coordinates condition a compact score network, and score matching jointly learns the factors and an implicit tensor representation from the available observations. Scalar and vector-valued outputs accommodate individual entries and entire tubes, enabling a common formulation for tabular tensors, images, and videos. The framework separates representation learning from task-specific observation modeling: reverse diffusion recovers missing values; estimation via Tweedie's formula, soft thresholding, and optional spatial consistency support mixed-noise denoising; and measurement-guided sampling transfers a prior learned from low-resolution hyperspectral observations to high-resolution reconstruction, followed by post-sampling refinement with data consistency and spectral subspace regularization. This separation makes the representation compatible with different corruption models and permits task-specific constraints to be incorporated within the same recovery framework. Experiments across multiple tensor modalities and recovery tasks demonstrate competitive reconstruction quality and the flexibility of a unified conditional generative representation. The code is available at this https URL

---


### 375. [GIFT: Representation Geometry Matters for Single-Domain Generalized Object Detection](https://arxiv.org/abs/2610.35374)

**<font color=#1a73e8>作者：</font>** Yin Zhang, Yaoyue Zheng, Yongqiang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-Domain Generalized Object Detection (S-DGOD) aims to generalize from a single source domain to unseen domains under distribution shifts. Existing efforts mainly focus on simulating unseen domains or suppressing domain-specific factors. However, they largely overlook the intrinsic generalization capability embedded in Vision Foundation Models (VFMs). In this work, we show that unconstrained fine-tuning disrupts the geometric structure of pre-trained representations, which encodes domain-invariant semantics. Motivated by this, we propose Geometric-Invariance Fine-Tuning (GIFT), a geometric-aware fine-tuning method for VFMs. Specifically, we introduce a series of learnable Householder reflections to the pre-trained weights to encourage geometry-consistent adaptation under domain shift. In addition, we propose a lightweight channel-wise scaling to facilitate effective task-specific adaptation. Extensive experiments demonstrate that GIFT consistently outperforms state-of-the-art (SOTA) approaches on two S-DGOD benchmarks. Notably, by introducing fewer than 1% additional trainable parameters into the frozen backbone, the proposed method achieves improvements of +7.9% and +2.9% in mPC over the previous SOTA on the Cityscapes-C and Diverse Weather Dataset, respectively. This finding highlights that preserving representation geometry is crucial for robust cross-domain generalization, establishing GIFT as a principled and efficient solution to domain shift.

---


### 376. [ACSAN: All-Convolutional Self-Attention Network Integrating Convolutional Operations with Vision Transformer](https://arxiv.org/abs/2610.35375)

**<font color=#1a73e8>作者：</font>** Zimian Wei, Tianqi Zhang, Hengyue Pan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the past few years, Vision Transformer (ViT) has achieved excellent performance in the field of computer vision. However, there still some problems remain. For instance, ViTs heavily rely on large-scale training data since they simply contain a large number of trainable parameters, which slows down their learning efficiency and limits their applicability in resource-constrained scenarios. In this paper, we propose a novel deep learning model, namely All-Convolutional Self-Attention Network (ACSAN), which applies convolution operations to replace fully-connected matrices multiplications in the ViT framework. To implement ACSAN, we firstly design Dynamic Convolutional Self-Attention (DCSA) as the basic module, which employs multi-scale dilated convolutions to generate Query, Key, and Value. We defined spatial self-attention and channel self-attention to generate attention features respectively. The two attention features are finally merged as the output of the DCSA module. Based on DCSA, we then construct the basic ACSAN block. Comparing with ViT, we use DCSA to replace the regular self-attention operations, and use convolution layers to replace MLPs. To evaluate the performance of the proposed method, we train ACSAN on three widely-used image classification databases, i.e. CIFAR-10, CIFAR-100 and ImageNet-1k, from scratch. Experimental results show that ACSAN achieves excellent classification accuracy comparing with standard ViT with comparable or fewer parameters, as well as other state-of-the-art methods. Ablation studies verify that each component contributes positively to the final performance.

---


### 377. [TransECG-SSL: Hybrid Self-Supervised Representation Learning for ECG Arrhythmia Classification](https://arxiv.org/abs/2610.35378)

**<font color=#1a73e8>作者：</font>** Ahtisham Ayyub, Fasih Haider, Muhammad Rehan Usman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-dataset generalisation remains a major challenge for automated electrocardiogram (ECG) arrhythmia classification because of differences in patient populations, acquisition protocols, annotation practices, and class distributions. Learning representations that remain informative across independent datasets could reduce reliance on dataset-specific labelled data. We propose TransECG-SSL, a self-supervised framework for transferable heartbeat representation learning from unlabelled ECG data. A Transformer encoder is pretrained using a hybrid objective combining masked signal reconstruction and contrastive learning, then frozen and evaluated by linear probing under patient-disjoint evaluation. Experiments across three public ECG databases and seven source--target settings show that Hybrid SSL consistently outperforms randomly initialised Transformers and achieves higher balanced accuracy than architecture-matched source-supervised pretraining. Reconstruction-only SSL remains competitive with Hybrid SSL, whereas contrastive-only pretraining performs substantially worse, highlighting the importance of masked reconstruction for transferability. Cross-dataset transfer nevertheless reduces balanced accuracy relative to target-specific self-supervised pretraining, while minority arrhythmia classes remain challenging under severe class imbalance. These findings demonstrate the potential of label-efficient self-supervised learning for cross-dataset ECG representation transfer while highlighting persistent limitations from domain shift and class imbalance.

---


### 378. [Toward Clinical Translation of Deep Learning-Based Intracranial Super-Resolution 4D Flow MRI Using Multi-Cohort Transfer Learning](https://arxiv.org/abs/2610.35396)

**<font color=#1a73e8>作者：</font>** Oliver Welin Odeback, Susanne Schnell, Patrick Winter 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We evaluated synthetic pretraining and multi-cohort transfer learning for deep learning-based super-resolution of intracranial 4D Flow MRI across heterogeneous neurologic cohorts. This mixed prospective-retrospective study analyzed 18 participants (12 healthy participants, 3 with moyamoya disease, and 3 with multiple sclerosis) with paired 1.2-mm and 0.6-mm 4D Flow MRI scans. A convolutional neural network pretrained on synthetic cerebrovascular data was fine-tuned using cohort-specific or pooled multi-cohort in vivo data. High-resolution-derived inputs enabled voxel-wise evaluation; native standard-resolution scans were used for angiographic and hemodynamic analyses. Synthetic pretraining reduced mean artery-wise velocity-normalized root mean square error (vNRMSE) versus interpolation (0.147 vs 0.166). Pooled transfer learning yielded the lowest mean vNRMSE (0.119 vs 0.127 for cohort-specific models and 0.147 for synthetic pretraining), with narrower 95% limits-of-agreement widths than synthetic pretraining across all test cases (0.109-0.222 vs 0.154-0.278 m/s). Super-resolved phase-contrast angiography achieved higher precision-recall area under the curve than native standard-resolution imaging in all cohorts (0.848-0.896 vs 0.486-0.805). These results indicate that pooled transfer learning improves cross-cohort reconstruction agreement and that super-resolution can improve vessel depiction, supporting further multi-center validation for cerebrovascular imaging.

---


### 379. [AdaTrendLike: Adaptive Hierarchical Detrending and Trend Likelihood Scoring for Time Series Anomaly Detection](https://arxiv.org/abs/2610.35400)

**<font color=#1a73e8>作者：</font>** Van Kwan Zhi Koh, Songnan Lin, Rongmo Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Industrial Internet of Things devices has led to increasingly large-scale and non-stationary time-series data, posing significant challenges for time-series anomaly detection (TSAD). Existing approaches often focus on reconstructing or forecasting observations while overlooking the role of trend dynamics, which constitute a major source of non-stationarity and contain valuable information for anomaly identification. To address this limitation, we propose AdaTrendLike, a TSAD framework that directly estimates trend likelihoods for anomaly detection. Specifically, we introduce Standardization Embedding to capture local statistical characteristics as latent representations and AdaDetrending to adaptively decompose input series into trend and detrended components. The detrended component is processed through a Fast Fourier Transform and a complex-valued convolutional neural network to learn normal periodic patterns, while TrendEst models the distribution of the trend component. Based on the estimated distribution, TrendLike computes anomaly scores by measuring the likelihood of observed trends, enabling effective detection of deviations from normal behavior. In addition to improving detection performance, the proposed framework provides feature-level interpretability by identifying anomalies through deviations in the estimated trend distribution. Extensive experiments on five public benchmark datasets demonstrate that AdaTrendLike consistently outperforms state-of-the-art TSAD methods, validating its effectiveness and robustness across diverse application scenarios.

---


### 380. [Unveil the Mask: Jointly-Optimized Diffusion Masked Pretraining for Appearance-Agnostic Operator Verification](https://arxiv.org/abs/2610.35414)

**<font color=#1a73e8>作者：</font>** Katsuya Ogata, Ryoya Yoshiyama, Kawachi Hodaka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photorealistic avatar videos decouple the appearance of a rendered face from the person who operates it, which makes conventional face recognition unsuitable for identifying the operator. Verifying the operator therefore requires representations of how a face moves that are insensitive to what the avatar looks like. We propose a verification framework built without any external pretrained model. It uses two complementary modalities provided for each sample: facial landmark sequences and video frames. From the landmark modality, it learns motion representations by diffusion masked pretraining over grouped landmarks, guided by lightweight auxiliary tasks that predict behavioral cues such as motion intensity and eye openness, and turns them into operator embeddings with a contrastive linear probe. To generalize to unseen avatar generators, the pretraining input is randomly transformed to simulate how a generator may alter the operator's motion. From the video modality, it captures fine facial motion through differences between consecutive frames. The embeddings of the two modalities are combined into one. Our approach reaches an overall AUC of 0.769 on the WBA2026 benchmark. Linear probing shows that the video embedding retains little information about the avatar's identity, whereas the landmark embedding retains some, and fusing the two modalities improves verification in particular across speaking and listening modes.

---


### 381. [Simulation-Efficient Double-Flow Neural Posterior Estimation for Agent-Based Models](https://arxiv.org/abs/2610.35442)

**<font color=#1a73e8>作者：</font>** Junyao Zhang, Jinglai Li, Junqi Tang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Neural posterior estimation (NPE) enables Bayesian inference of the posterior parameter in agent-based models (ABMs) with intractable likelihoods, but simulating training data can be computationally expensive. We propose Double-Flow Neural Posterior Estimation (DF-NPE), which combines learned time-series summaries with two conditional normalizing flows for synthetic-data generation and posterior estimation. The framework supplements direct simulations with synthetic training pairs and supports both pooled and ordered training strategies. Experiments in two settings of the Brock-Hommes asset-pricing model show that DF-NPE can reduce direct simulations by 90 percent while achieving lower mean posterior discrepancies and runtime than standard NPE. Performance varies with the allocation of directly simulated and synthetic data and the training strategy. These results establish learned summary augmentation as a practical approach to reducing simulation costs for Bayesian posterior inference of parameters in ABMs.

---


### 382. [OBB-PBD: Extending Parallel Box Decoding to Oriented Bounding Boxes for Referring Expression Grounding in Aerial Imagery](https://arxiv.org/abs/2610.35450)

**<font color=#1a73e8>作者：</font>** Chang Woo Song, Yeong Jun Koh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring expression grounding in overhead imagery requires oriented bounding boxes rather than horizontal ones, since aerial objects appear at arbitrary orientations. Most grounding models emit box coordinates sequentially; Parallel Box Decoding (PBD) instead predicts all geometry slots in one forward pass, but only for four-coordinate horizontal boxes. We extend this block-aligned interface to a six-slot oriented representation using a double-angle parameterization. Rather than assuming correctness from a decreasing loss curve, we verify the extension with image/prompt-shuffle controls and visibility/leakage probes, which show that the corrected model depends on both the image and the prompt rather than on prompt statistics alone. On the aerial vehicle visual grounding (AVVG) benchmark, whose targets are genuinely oriented, the extended model improves rotated intersection over union (rotIoU) from 0.1253 for the zero-shot baseline to 0.303 +/- 0.012 (mean +/- standard deviation over three training seeds) across the complete 6139-record test split spanning all 120 images. Learning oriented boxes rather than their axis-aligned envelopes adds 0.055 +/- 0.008 rotIoU beyond a matched control (per-seed 95% confidence intervals all excluding zero), whereas block expansion alone yields no rotIoU gain distinguishable from zero.

---


### 383. [Prior Predictive Matching for Bayesian LoRA](https://arxiv.org/abs/2610.35457)

**<font color=#1a73e8>作者：</font>** Tomasz Kuśmierczyk, Eliezer de Souza da Silva, Marcin Sendera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian variants of Low-Rank Adaptation (LoRA) provide principled uncertainty estimation when fine-tuning large foundation models, but require specifying the prior over the low-rank weight updates. We address this hyperparameter selection problem by introducing a closed-form prior-predictive estimator that operates before fine-tuning.
We analyze a second-order expansion of the network and quantify how the low-rank prior drives function-space deviations from the pretrained outputs. We also show that these prior-predictive quantities depend on the prior only through the product of the adaptation rank and the fourth power of the prior scale. Because the training targets share a single draw of the latent weight update, we can leverage the covariance between example residuals to derive a moment-matching estimator. Furthermore, our theoretical analysis establishes that the optimal prior precision scales as $r^{-1/2}$ with the rank $r$, allowing a single estimate to generalize across all ranks.
Controlled experiments across regression and classification tasks validate our approximation and show that our estimator recovers the true prior scale. On RoBERTa-large, our approach improves predictive negative log-likelihood (NLL) and calibration over both MAP and marginal-likelihood selection without requiring validation data, while achieving competitive out-of-distribution detection.

---


### 384. [A Contextual Measure of Ambiguity in Prescriptive Text](https://arxiv.org/abs/2610.35461)

**<font color=#1a73e8>作者：</font>** Sally Dong, Luke Thorburn, Andrew Konya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambiguity in prescriptive text such as laws, contracts, rules, policies, or recommendations can be both desirable (e.g., if it enables a law to adapt to changing context, such as new technologies) and undesirable (e.g., if it leads to arbitrary discretion or conflict over the law's interpretation). To help navigate these trade-offs, it would be valuable to have methods for quantifying ambiguity that are predictive of such outcomes, but existing measures capture how text is perceived in isolation rather than how it is interpreted in context. In this paper, we propose quantifying ambiguity as the degree of disagreement among a set of stakeholders ("raters") on how alternative prescriptive texts ("policies") apply in each of a set of relevant scenarios ("cases"). Using two policy domains, we present preliminary analysis suggesting that, even when using simulated raters, this approach (i) correlates with real human disagreement, and (ii) is robust to spurious text features. We then apply the measure to existing deliberation datasets to describe the association between policy ambiguity and support for those policies.

---


### 385. [EvoBench: An Evolving, Diagnostic Benchmark Framework for Environmental Modeling](https://arxiv.org/abs/2610.35464)

**<font color=#1a73e8>作者：</font>** Yiming Sun, Yuan Zhang, Qi Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning models are now widely used to predict environmental variable dynamics in domains like hydrology, climate science, agriculture, and ecology. These models are usually compared on fixed benchmark datasets using a single average accuracy score. As models improve, their scores become very close when averaged over large regions and long time periods, so the benchmark can no longer tell them apart, and a single number hides \emph{where} and \emph{when} a model fails. Three failures are common across environmental domains: models get worse as the climate shifts (non-stationarity), models fail at unmonitored sites (spatial extrapolation), and models miss rare but important regimes such as floods and droughts.
We present \textbf{EvoBench}, a benchmark framework that shows where a model fails, tracks failures over time, and evolves to focus on model capability gaps. We apply EvoBench to daily streamflow prediction as a case study (\textbf{CAMELS-Evolve}, about 9{,}000 U.S. basins, 1985--2024) and compare an operational physical model (NWM), a conceptual reference (HBV), and several data-driven models. No model wins on every testing scenarios (e.g., in terms of average accuracy, performance at low flows and unmonitored basins). Also we observe that all data-driven models under-predict floods. Additionally, we show that targeted fix based on the reported failures could mitigate weaknesses the benchmark identified in certain scenarios. EvoBench turns model evaluation from a saturated ranking into a moving map of model limitations.

---


### 386. [Multi-Horizon Future Discovery for Physics-Informed Exploration](https://arxiv.org/abs/2610.35468)

**<font color=#1a73e8>作者：</font>** Shuwei Wang, Qiang Guan, Brian Qiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploration in physical control environments requires agents to identify actions whose consequences reveal previously unexplored aspects of the underlying dynamics. However, many intrinsic motivation methods rely on immediate prediction errors, state novelty, or local physical changes, which may overlook informative outcomes that emerge across extended temporal horizons. We investigate whether learning structured representations of reachable futures can provide a more effective basis for exploration. To this end, we introduce Hamiltonian Temporal Contrastive Curiosity (HTC$^2$), a framework that combines multi-horizon temporal representation learning with Hamiltonian phase-space structure. A horizon-conditioned contrastive critic learns temporal relationships from future-state pairs sampled within the same episode. The distance between positive-pair representations is then used as an intrinsic reward, encouraging the agent to explore futures that remain insufficiently organized in the learned representation. To incorporate information about physical dynamics, we additionally modulate this reward using bounded multi-step Hamiltonian variation, rather than directly rewarding changes in the Hamiltonian itself. We integrate HTC$^2$ with both Soft Actor-Critic (SAC) and Proximal Policy Optimization (PPO), and evaluate it across six DeepMind Control Suite tasks. Comparisons with ICM, RIDE, E3B, Plan2Explore, and a single-step Hamiltonian curiosity baseline are complemented by state-coverage evaluations, component ablations, and phase-space diagnostics to characterize the contributions of temporal learning and physical structure to exploratory behavior.

---


### 387. [MANTIS: Multi-Axis News Transformations for Instance-Wise Stress Testing and Worst-Case Training in Fake News Detection](https://arxiv.org/abs/2610.35475)

**<font color=#1a73e8>作者：</font>** Dexin Liu, Fan Yang, Zimu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated fake news detection is vital on social media, where fake news is easily rewritten to fool detectors. However, existing approaches typically rely on superficial writing cues or single-style text rewrites, resulting in poor robustness under diverse cosmetic modifications. We construct MANTIS-Bench, a multi-axis presentation-attack benchmark that pairs original news with rewritten views across writing style, emotional expression, and dissemination framing. We further propose MANTIS, an instance-adaptive adversarial framework enabling dynamic worst-case training tailored to each news article with zero inference-time overhead. This reframes fake news defense from heuristic format smoothing into targeted, fact-invariant credibility assessment. Experiments on MANTIS-Bench show that MANTIS reduces the Union Attack Success Rate (UASR) by 3.55 percentage points relative to SheepDog on GossipCop and consistently outperforms prior single-axis defenses on Macro-F1 while maintaining competitive clean accuracy, demonstrating the effectiveness of multi-axis and instance-adaptive worst-case training.

---


### 388. [Beyond Words Alone: Disentangling Distributed Evidence for Visually Grounded Cultural Translation](https://arxiv.org/abs/2610.35482)

**<font color=#1a73e8>作者：</font>** Dingming Li, Yiwen Qiu, Linjuan Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social media enables cross-lingual communication, yet the meaning of user-generated content (UGC) is often distributed across text, images, and cultural knowledge, making translation challenging. Existing evaluations typically treat images as optional and assume textual information is sufficient, obscuring whether errors stem from missing visual evidence or inadequate cultural adaptation. We introduce \textbf{Culture-MMT}, a diagnostic benchmark for \textbf{distributed-evidence pragmatic reconstruction} in social-media translation. It contains 498 curated, de-identified UGC instances across 20 domains, categorized into Symbol, Visual, and Hybrid by their required evidence. We also develop a human-aligned domain-specific judge, Judger, and a controlled evaluation framework that systematically varies the evidence available to translators. Across 17 model configurations, real images improve performance by +0.280 on Visual and +0.197 on Hybrid, but only +0.050 on Symbol, while random images provide no comparable gains. Human-authored descriptions further show that jointly dependent cases remain more challenging even when visual facts are explicit. These results characterize culturally effective social-media translation as {meaning reconstruction from distributed evidence}, highlighting visual grounding and cultural-pragmatic adaptation as distinct model bottlenecks.

---


### 389. [Evaluating Bayesian deep learning for robust biomedical time-series classification under distribution shift: A sleep scoring case study](https://arxiv.org/abs/2610.35484)

**<font color=#1a73e8>作者：</font>** Mads Birch Sørensen, Ulrike Richter, Francois Gastambide 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In biomedical time-series classification, machine learning models often suffer from deteriorating accuracy and calibration due to distribution shift. We investigate to what degree Bayesian-inspired deep learning improves robustness through Bayesian model averaging (BMA). Using rodent sleep scoring as a case study, we evaluate BMA under distribution shifts in genotype, laboratory, and species. We systematically compare nine approximate inference methods spanning single- and multi-basin approaches across two neural network backbones on in-distribution (ID) data and five out-of-distribution (OOD) datasets. In our results, multi-basin methods perform best, outperforming baselines and single-basin methods. Compared with point estimates, BMA generally improves OOD accuracy and calibration across both architectures, while yielding only modest ID gains. It also often improves selective prediction and OOD and artifact detection, but, interestingly, not inter-rater disagreement detection.

---


### 390. [Learning Scene Coordinate Reconstruction from Unposed Images via Pose Graph Optimization](https://arxiv.org/abs/2610.35501)

**<font color=#1a73e8>作者：</font>** Tze Ho Elden Tse, Jizong Peng, Angela Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning-based structure-from-motion methods such as ACE-Zero have demonstrated strong performance in estimating cameraposes and scene coordinates from unordered image collections without requiring ground truth supervision. However, the lack of global and multi-view consistency constraints in ACE-Zero can lead to pose drift and misalignment, particularly in complex or ambiguous scenes. In this work, we propose a hybrid framework that integrates pose graph optimization (PGO) into ACE-Zero to refine camera poses and suppress incorrect refinements. We construct pose graphs directly from ACE-Zero outputs by extracting relative pose constraints from predicted scene coordinates. Furthermore, we introduce an uncertainty-aware optimization strategy by estimating confidence scores using geometric priors, including epipolar and optical flow consistencies across views. Our approach improves the robustness and accuracy of pose estimation, demonstrating that global geometric reasoning can effectively complement learning-based inference in structure-from-motion.

---


### 391. [Model reduction in time: Learning flow maps for reducing stochastic dynamical systems in time](https://arxiv.org/abs/2610.35504)

**<font color=#1a73e8>作者：</font>** Shreya Jha, Benjamin Peherstorfer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictions with dynamical systems can be computationally expensive---even with reduced models---because reaching future prediction times can require many sequential time integration steps. We propose Flow-Map First-Order Trajectory Matching (FM-FTM), a nonintrusive model reduction approach that accelerates ensemble predictions of stochastic dynamical systems by learning flow maps that replace multiple time-integration steps. Our method uses first-order trajectory matching (FTM) to learn a deterministic representation of the stochastic probability-current dynamics and then reduces its evolution over time into a flow map whose evaluation directly yields predictions over long time horizons. Numerical experiments on evolution problems with stochastic forcing demonstrate that FM-FTM accelerates ensemble predictions by up to two orders of magnitude while accurately predicting time marginals and ensemble statistics.

---


### 392. [HiFiPix: Bringing High-Fidelity Real-World Super-Resolution Back to Pixel Space](https://arxiv.org/abs/2610.35515)

**<font color=#1a73e8>作者：</font>** Wenjie Li, Du Chen, Hui Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based real-world image super-resolution suffers from limited reconstruction fidelity due to information loss in VAE-based latent representations. Recently, pixel-space diffusion models offer a promising high-faithfulness alternative by avoiding latent compression, but adapting them to Real-ISR remains challenging due to inherent patch boundary artifacts and degraded generative capability. To address the issues and maximize the potential of pretrained pixel-space diffusion models, we propose HiFiPix, a pixel-space Real-ISR framework capable of ultra high-fidelity reconstruction and fine-grained visual generation effects. To suppress patch boundary artifacts, we penalize unrealistic high-frequency periodic components with a Cross-Scale Wavelet Discriminator (CWSD) for image-level supervision, and Mixup Contrastive Self-Distillation (MixCSD) for intermediate representation regularization. Furthermore, we uncover a heterogeneous generation-fidelity trade-off across low-rank adapters (LoRA) and propose Selective LoRA Pruning (LoRA-SP) to adaptively prune LoRA layers, enhancing generative capability with minimal deterioration of reconstruction fidelity. Extensive experiments demonstrate that HiFiPix consistently outperforms existing state-of-the-art latent space methods in terms of both restoration accuracy and perceptual quality by a large margin. Code and models will be released.

---


### 393. [Learning High-Quality Pseudo-Labels for Point-Supervised Temporal Action Localization](https://arxiv.org/abs/2610.35516)

**<font color=#1a73e8>作者：</font>** Zhenying Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point-supervised temporal action localization (PTAL) aims to recognize and localize action instances in untrimmed videos using only point-level annotations. Existing pseudo-label-based methods have made substantial progress in PTAL. However, confidence-based initialization can overlook well-localized proposals. Meanwhile, existing methods either keep pseudo-labels fixed during detector training or update them without fully exploiting alternative boundary evidence from the original proposal pool. These limitations constrain supervision quality, thereby hindering detection performance. To learn high-quality pseudo-labels, we propose a framework that integrates prior-guided initialization with consensus-guided refinement during detector training. Our framework comprises two modules: Prior-Guided Initialization (PGI) and Consensus-Guided Refinement (CGR). PGI combines proposal confidence with point-derived priors to establish instance-specific reliability for initial pseudo-label selection and candidate retention. CGR continually uses the retained original candidates to construct boundary targets, combining their consensus with evolving detector predictions to refine pseudo-labels throughout training. Experiments on four benchmarks demonstrate that our method achieves competitive detection performance compared with existing methods. In particular, our method achieves 68.5\% average mAP over tIoU thresholds 0.1--0.7 on THUMOS14, surpassing PseR by 3.7 percentage points. Code is available at this https URL

---


### 394. [PRISMA: Differentially Private Synthetic In-Car Telemetry via Differentiable Simulation](https://arxiv.org/abs/2610.35521)

**<font color=#1a73e8>作者：</font>** Kilian Zeiseweis, Nele Sophie Brügge, Marven Kummerfeldt 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differentially private synthesis of in-car energy consumption data is challenging because the output is high-dimensional, and known lower bounds show that the privacy-utility trade-off degrades with the square root of the number of output dimensions. However, we observe that the intrinsic dimensionality of in-car energy consumption is much lower than that of the raw trace: given a small set of contextual personal variables-such as start point, end point, the car model, and the driving behavior-the consumption profile can be largely explained by publicly available map data (including elevation) combined with a physical model of vehicle energy use. We exploit this low intrinsic dimensionality in PRISMA, a Privacy-preserving In-car Synthesis and Modelling Algorithm. PRISMA involves three stages: (i) energy consumption traces are encoded into a low-dimensional latent space; (ii) the distribution of latent vectors is synthesized using the differentially private tabular data synthesis algorithm AIM, and (iii) samples drawn from this distribution are decoded back into full energy consumption traces via a differentiable physics-based simulation, a step that consumes no additional privacy budget since it uses only public information. By using a compact, physically-grounded latent representation of the traces, PRISMA significantly reduces the effective output dimension. Our experimental results show that PRISMA achieves for a competitive $\varepsilon = 0.5$ a better data synthesis performance than prior tabular and marginal-based DP synthesis baselines by preserving the diversity of the original power consumption profiles without collapsing to a small set of modes.

---


### 395. [Generative Structure from Motion with Native 3D Diffusion](https://arxiv.org/abs/2610.35522)

**<font color=#1a73e8>作者：</font>** Haobin Duan, Binbin Huang, Mochu Xiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering an object's 3D structure and camera motion from a few uncalibrated views is a fundamental problem in computer vision. Classical structure from motion methods recover 3D geometry consistent with the input images but cannot recover unseen regions; native generation methods produce plausible 3D objects which are related but not necessarily faithful to the input images. Methods simply concatenating reconstruction and generation allow error to cascade across the two stages, instead of producing a 3D object consistent with both the distribution and the input. We propose GenSfM, which integrates image-based 3D reconstruction with a native 3D diffusion model. In particular, we use a multi-modal diffusion transformer to jointly denoise the shape latent and per-view pose latents under shared self-attention, grounding generated geometry in the observed views while using object-level priors to infer unobserved regions. A compact 3D-native UV-volume tokenization keeps the joint sequence small as views are added, and a pose-aware stage refines geometry and texture by sampling per-voxel image features at the recovered camera poses. On Toys4k and GSO, for $4$ uncalibrated views, GenSfM improves novel-view PSNR by $3.2$-$4.5$ dB and reduces median Chamfer distance by $2.8$-$3.8\times$ over a strong native-3D generation baseline, while recovering input-view poses over $96\%$ Acc@$5^\circ$ without any external pose-estimation backbone, post-hoc optimization, or known intrinsics. Project page: this https URL.

---


### 396. [JANUS: Synthesizing Cross-Layer Defenses Against Web Deserialization Attacks](https://arxiv.org/abs/2610.35532)

**<font color=#1a73e8>作者：</font>** Ruozhao Yang, Minglang Li, Jiongchi Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Unsafe deserialization turns untrusted data into attacker-controlled execution, and a single vulnerability can admit diverse exploit variants that evade defenses tailored to a known exploit. Existing defenses typically operate at a single enforcement point with limited visibility into the full attack. Combining controls across layers offers complementary protection, but coordinating them to preserve legitimate functionality and adapting them to new variants requires substantial expert effort.
We propose JANUS, a red-blue adversarial framework for automated cross-layer defense synthesis. Starting from a known exploit, \sys iteratively refines deployment-specific policies in an isolated offline environment. A black-box attacker probes the current policy for exploit variants using only externally observable feedback. The defender summarizes each verified variant into its security-relevant effects, uses counterfactual replay to separate complementary coverage from redundant enforcement, and jointly selects and scopes controls across layers. Each candidate policy is validated against accumulated exploits and benign workflows.
We evaluate JANUS on sixteen vulnerability deployments across six Java and PHP applications against gateway, application, system, and cross-layer defenses. JANUS reduces held-out attack success to 6.2%, compared with 18.8-55.0% for the baselines, fully mitigates 13 of 16 deployments, and preserves 98.4% of benign functionality tests at a 6.9% targeted P95 latency increase.

---


### 397. [Beyond Modeling Order: Dual-Path Spatiotemporal Representation Learning for Cross-Subject EEG Emotion Recognition](https://arxiv.org/abs/2610.35540)

**<font color=#1a73e8>作者：</font>** Zehui Xiao, Yi Zheng, Guixing Fu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-subject generalization remains a major challenge for EEG-based emotion recognition due to pronounced inter-subject variability in neural activity and emotion-related spatiotemporal patterns. Existing methods mainly alleviate inter subject differences through distribution alignment or contrastive learning, while paying limited attention to representation bias associated with fixed spatiotemporal modeling orders. We hypothesize that high-level emotion representations of the same EEG signal should remain consistent across different spatiotemporal modeling paths. Based on this hypothesis, we propose a Dual-Path Spatiotemporal Contrastive Learning (DP-STCL) framework for cross-subject EEG emotion recognition. DP-STCL employs two complementary encoders with independent parameters, namely a Temporal-to-Spatial (TS) path and a Spatial to-Temporal (ST) path, to model EEG spatiotemporal information under different integration orders. During representation learning, the same emotional stimulus is used to establish cross subject associations, while three complementary relations jointly constrain representation variations across subjects and modeling paths. This promotes stable and discriminative stimulus-related emotion representations. To further handle limited labeled target subject data, we introduce a LoRA-based few-shot adaptation strategy with low parameter overhead. Extensive cross-subject experiments on SEED, SEED-IV, SEED-V, and FACED show that DP-STCL consistently outperforms the compared methods, demonstrating its effectiveness in improving cross-subject EEG emotion recognition.

---


### 398. [The Agent in the Middle: How AI-Mediated Access Reshapes Web Vulnerability Exploitation](https://arxiv.org/abs/2610.35541)

**<font color=#1a73e8>作者：</font>** Ruozhao Yang, Jiongchi Yu, Ming Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web services increasingly expose backend interfaces that let users delegate tasks to AI agents, which invoke service operations directly without navigating websites. This shift changes how existing Web vulnerabilities can be exploited. We investigate these changes through VELA, an executable benchmark covering 44 vulnerabilities across twelve Web application families. The benchmark preserves vulnerable backends and derives agent-facing interfaces from legitimate workflows. We evaluate three commercial agents across multiple interface configurations, using controlled comparisons to separate interface effects from agent behavior and independent oracles to verify attack outcomes. Our results show that the agent realizes every attack that direct interface invocation realizes in the reference configuration, so exploitability is set mainly by the interface: 91% of vulnerabilities remain exploitable under the reference design. Interface restrictions prevent some attacks by removing required operations or limiting input control, while retention remains high across vulnerability classes. No case-level loss in the reference configuration is attributed to agent refusal or input normalization, and in one case the agent completed an attack by supplying calls the attacker omitted. Across the tested configurations, interface design affects exploitability more than agent choice, moving retention from 39% to 95% against at most 4.5 points across agents, but some restrictive interfaces also limit legitimate workflows. Our study provides a systematic empirical account of how agent-mediated access reshapes existing Web vulnerabilities, grounding future Web architecture design in measured security outcomes and trade-offs between reducing attack exposure and preserving legitimate functionality in agent-facing services.

---


### 399. [StateLoop: Persistent State for Looped Transformers](https://arxiv.org/abs/2610.35544)

**<font color=#1a73e8>作者：</font>** Feichen Song, Boyi Zeng, He Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped Transformers offer a parameter-efficient approach to language modeling by repeatedly applying a shared backbone. Vanilla looped Transformers use each backbone output directly as the input to the next iteration. These outputs may contain information useful several iterations later, but retaining it across the loop depends entirely on the single hidden state. We introduce StateLoop, which maintains one additional persistent state per token to retain information across iterations. At each iteration, a learned gate controls how much of the previous state is retained and how much information from the backbone output is incorporated. The updated state is projected back and added to the backbone output for subsequent iterations and final prediction. This design reduces Pile perplexity and improves average accuracy across eight zero-shot tasks over Vanilla Looped. Its perplexity advantage over Vanilla Looped grows with trained loop depth, consistent with persistent state becoming increasingly useful as recurrent computation deepens.

---


### 400. [Efficient probabilistic weather forecasting at quarter-degree resolution with two-sided transport attention](https://arxiv.org/abs/2610.35545)

**<font color=#1a73e8>作者：</font>** Junu Choi, Youngjoon Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-resolution probabilistic weather forecasting remains computationally demanding. Here we present Astra, a 0.25$^\circ$ ensemble model trained on eight H200 GPUs. It combines Kantorovich Attention, a two-sided transport attention in which each region chooses where it reads from and writes to, so every region sends and receives at token resolution, with a self-featurised continuous ranked probability score (CRPS) that also scores forecasts in the model's multiscale features. In WeatherBench 2, Astra matches GenCast's CRPS averaged over five upper-air targets and days 1-10 with 9.8% of its hardware-normalised training compute. Verified against ERA5, its CRPS and ensemble-mean root-mean-square error are lower than the ECMWF ensemble's on all 600 variable, level and lead-time combinations, and its CRPS is lower than GenCast's on 73.5% of them. A 15-day member needs 39 times fewer floating-point operations than GenCast's GPU implementation, and 50 members take under 40 min on one consumer GPU, within 21 GB.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-446](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
