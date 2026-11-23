# 📦 其他研究 | 2026年11月24日

> 本类共 **206** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-206](./part-05.md)

---

### 51. [TSIR: Ray-Traced Triangle Splats for Inverse Rendering](https://arxiv.org/abs/2611.27030)

**<font color=#1a73e8>作者：</font>** Wentao Yang, Chentao Shen, Zhengqi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inverse rendering enables realistic relighting for visual effects and augmented reality. However, overlapping Gaussian primitives complicate surface recovery and require costly multi-layer traversal and compositing for light transport. We propose TSIR, a two-stage inverse rendering method that reconstructs relightable triangle splats from multi-view images. The first stage prepares opaque triangle splats with learnable vertex shading normals. The second stage directly traces these surfaces to estimate materials through Monte Carlo integration of direct illumination and indirect reflections, reducing reliance on multi-layer compositing. Anti-aliasing improves rendering quality while maintaining efficiency. Experiments demonstrate higher relighting quality than the evaluated baselines and more efficient anti-aliasing than supersampling.

---


### 52. [Hypergraph Structural Entropy-Enhanced Hierarchy-Aware Semi-Supervised Graph Classification](https://arxiv.org/abs/2611.27043)

**<font color=#1a73e8>作者：</font>** Guangjie Zeng, Hao Peng, Angsheng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised graph classification aims to learn graph-level representations by leveraging a large number of unlabeled graphs alongside a small set of labeled ones, effectively mitigating the issue of label scarcity. Despite significant progress by various semi-supervised learning strategies, complex relationships among graph vertices beyond pairwise edges, especially hierarchical structures, remain underexplored by existing methods. In this work, we propose a Hypergraph Structural Entropy-Enhanced hierarchy-aware framework, namely HypSEE, for semi-supervised graph classification. Specifically, we first construct walk-induced and embedding-derived hypergraphs to capture hierarchy-aware local and long-range higher-order relationships within graphs. Then, we devise a hierarchical hypergraph pooling approach guided by hypergraph structural entropy (HSE) to facilitate hierarchical representation learning in hypergraphs. Lastly, we employ an anchor graph-based consistency strategy to mutually align the representations from these two hypergraph views, enhancing the learning efficacy on unlabeled data. Extensive experiments on 8 benchmark datasets demonstrate the state-of-the-art performance of our approach.

---


### 53. [Action-Conditioned Spatio-Temporal Forecasting](https://arxiv.org/abs/2611.27044)

**<font color=#1a73e8>作者：</font>** Yutong Xia, Yangyou Liu, Yuxuan Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study spatio-temporal forecasting in networked systems under specified actions. The challenge is to capture the action's effects without predicting spurious changes in unaffected regions. However, direct supervision and evaluation of these effects require paired futures with and without the action, whereas observational trajectories reveal only the realized future. We introduce PairST, a benchmark comprising six datasets across traffic, power transmission and water distribution, with paired reference and intervened futures simulated from the same system state. These pairs enable separate evaluation of affected-region forecast accuracy and quiet-region response error. We further propose ActionST, which forecasts the intervened future by writing an explicit response onto an intervention-independent reference forecast. Specifically, node-time addressing constructs a query for each response position, a state-conditioned response writer computes candidate responses, and a graph-aware locality gate controls their strength. Experiments on six datasets demonstrate the effectiveness of ActionST at new action targets, with the lowest mean absolute error on five datasets and the best average rank. Our source code and the PairST benchmark are available at this https URL.

---


### 54. [Isolating the Language Shell: A Content-Controlled Study of Multilingual Reasoning](https://arxiv.org/abs/2611.27053)

**<font color=#1a73e8>作者：</font>** Hoejoon Kwon, Jinhee Jang, Byeonggeuk Lim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual reasoning distillation requires choosing the language in which teacher reasoning is presented, yet existing recipes often entangle linguistic form with differences in generation, translation, and filtering. We construct content-controlled supervision by rendering the same verified English trajectories into English, translated target-language, and language-mixed shells, and fine-tune two pretrained students in three target languages, evaluating them on multilingual mathematical reasoning at two difficulty levels. Even with the underlying reasoning content held fixed, we find that shell choice can change downstream accuracy, with effects varying across students, languages, and difficulty levels. Pre-training compatibility does not consistently track these outcomes, and even when our tests find no clear accuracy difference between shells, their output-language behavior can still differ substantially. These results suggest that the supervision shell is a distinct design choice in multilingual reasoning distillation.

---


### 55. [A Continuous Relaxation of Quantization-Aware Training](https://arxiv.org/abs/2611.27056)

**<font color=#1a73e8>作者：</font>** Kartikeya Bhardwaj, Mohammed Almousa, Chaitanya Mullapudi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantization is a critical piece of the deployment pipeline in the era of large generative models. Low-bit quantization, particularly 2-bits or sub-2-bits, is a notoriously difficult problem, particularly when using a channelwise quantization scheme which has been shown as a leading candidate for hardware-efficiency. The key challenges with low-bit quantization range from limited quantization levels to saddle points or flat regions in the loss surface. In this paper, we look at the problem of flat quantization loss surfaces through a lens of dynamically changing bitwidth. Unlike existing techniques which either change the bit-precision abruptly or keep it fixed, we propose to gradually alter the bitwidth as the model trains. To this end, we propose RelaxQAT, a continuous relaxation of the QAT process. We also provide simple theoretical and empirical insights behind why RelaxQAT helps the QAT performance. Our extensive experiments demonstrate up to 6.3% average accuracy gains on vision and up to 7.7% better average accuracy on natural language tasks, compared to the leading QAT methods.

---


### 56. [Learning 3D MRI Representations with Generative Adversarial Networks](https://arxiv.org/abs/2611.27057)

**<font color=#1a73e8>作者：</font>** Sujeet Lahane, Sapna Mishra, Akash Suryavanshi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning representations of visual images is a challenging task. It requires extracting abstract patterns from high-dimensional data without explicit supervision. This becomes pronounced with 3D MR imaging due to sparse features, higher dimensional inputs, and smaller datasets. Many state-of-the-art representation learning algorithms successfully rely on transformers and diffusion-based architectures. However, these methods struggle with smaller datasets. In effect, solution methods relax the problem by slicing 3D volumes and solving the problem for 2D medical imaging, resulting in a loss of spatial 3D information. We present R2RG, a representation learning method based on Convolutional Neural Networks (CNNs), with Generative Adversarial Networks (GANs) honing the reconstruction task. Our key insights lie in exploiting architectural biases in 3D CNNs, combined with data-efficient auto-encoding GANs and a composite loss function to enhance reconstruction fidelity and stabilize training. Our experiments on three standard datasets and a locally collected dataset show that R2RG not only achieves superior performance but also generalizes to heterogeneous and smaller datasets. Furthermore, representations learned with R2RG outperform those learned with contrastive-based representation learning methods on Parkinson's and Alzheimer's disease classification. Our work demonstrates that reconstruction-based representation learning is a promising direction for 3D medical imaging under limited data availability.

---


### 57. [Structural Agreement Indicates Prediction Accuracy For Protein-Ligand Co-Folding](https://arxiv.org/abs/2611.27058)

**<font color=#1a73e8>作者：</font>** J. Henry Broster, Bojana Popovic, Diana Kondinskaia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Co-folding models predict the structures of proteins and their bound ligands, but their accuracy varies across targets. Their usefulness therefore depends on knowing which predictions a user can trust. Confidence scores are intended to guide that choice. However, across seven co-folding models, we show that confidence-based selection offers little improvement over choosing a prediction at random. For approximately three-quarters of structures, predictions are either exclusively correct or incorrect, leaving no opportunity for ranking to change the outcome. Moreover, high confidence does not reliably discriminate correct top-ranked predictions from incorrect ones. We find that structural agreement among predictions is a more accurate measure of likely success than current confidence scores. We capture this with the Concentration of Repeated Ensembles (CORE) Score, which combines cluster tightness with ensemble support. CORE Score discriminates top-1 success and oracle success, achieving mean ROC AUCs of 0.866 and 0.838, compared to 0.757 and 0.759 for ipTM. CORE Score also outperforms training set similarity measures, including ligand Tanimoto, protein sequence, and Runs N' Poses similarity, despite requiring no experimental ligand pose. Structural agreement is therefore a practical indicator of reliability and a baseline for evaluating future confidence estimators, without requiring an additional trained uncertainty estimator.

---


### 58. [NightmareDiscourseBench: A Benchmark Dataset for Fictional Direct Discourse Identification Pipelines](https://arxiv.org/abs/2611.27059)

**<font color=#1a73e8>作者：</font>** Claudia Carroll, Gabi Kirilloff, Dashiell Leigh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper we introduce a new benchmark dataset, NightmareDiscourseBench, for testing NLP pipelines that identify forms of direct discourse in English-language fiction. We first review existing publicly available benchmarks (providing summary statistics and reviewing available metadata) for this task, identifying theoretical inconsistency and exclusive focus on speech as primary issues in this domain. We then overview our narrative theory-based framework for classifying and evaluating different forms of direct discourse, and finally describe NightmareDiscourseBench, a new benchmark test set of 12 text samples accompanied by metadata pertinent to the task of direct discourse identification.

---


### 59. [Rethinking Cross-Sensor Domain Adaptation for Bridge Point Cloud Semantic Segmentation](https://arxiv.org/abs/2611.27060)

**<font color=#1a73e8>作者：</font>** Linghui Huang, Zipeng Wang, Shunjie Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation models for bridge point clouds lose accuracy when trained on terrestrial laser scanning (TLS) data and applied to mobile laser scanning (MLS) data. This study re-examines the SemanticBridge TLS-to-MLS protocol to determine how sampling density, surface roughness, color, and acquisition viewpoint are expressed in the 8-cm sparse-voxel representation, and how adaptation gains depend on source-model convergence. Using one sparse-convolution U-Net, we combine raw-point statistics with controlled input perturbations and compare adaptive batch normalization, entropy minimization, Mean Teacher, and confidence-filtered self-training under 100- and 300-epoch schedules. TLS and MLS have similar nearest-neighbor spacing after preprocessing (12.08 and 12.02 mm), and a 4-mm perturbation of TLS points changes voxel occupancy by only 4.4%. Color distributions differ systematically, but zeroing color on identical voxels changes target mean intersection over union (mIoU) by only +0.02, and by +0.06 after the color augmentation is scale-corrected. The sensors also observe different portions of the bridge, yielding different class proportions. A 300-epoch source-only model obtains 57.80 mIoU on the paired-bridge protocol. Confidence-filtered self-training improves the 100-epoch baseline, but from a converged model it changes target mIoU by -0.97 (source-selected checkpoints) and -2.44 (final-50-epoch means). Repeated evaluation (standard deviation 0.27-0.64) and seed variation (1.88 across three seeds) are comparable to several method differences. Adaptation results on this benchmark therefore depend on representation scale, source-model convergence, and evaluation variability.

---


### 60. [COMPASS: Cross-modal Observation with Multi-Path Adaptive Stopping and Selection for Early Time Series Classification](https://arxiv.org/abs/2611.27065)

**<font color=#1a73e8>作者：</font>** Cheng-En Chung, Yujia Wu, Oscar Tai-Yuan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early time-series classification (ETSC) balances predictive performance against the amount of observed data. In multimodal settings, modality-associated and fused branches may differ in predictive ability at the same observed prefix, motivating joint decisions about when to stop and which branch should provide the final prediction. We propose COMPASS, a two-stage framework that preserves two modality-associated temporal branches and one fusion branch. The first stage combines cross-modal feature exchange and gated fusion with branch-wise supervision at every prefix. The second stage optimizes a shared four-action controller to continue observation or terminate through one of the frozen branches. Experiments on six physiological and wearable datasets compare COMPASS with multimodal adaptations of five ETSC baselines. COMPASS achieves the best average ranks in accuracy-earliness harmonic mean, AUROC, and earliness within this comparison set. At identical learned stopping times, branch selection improves mean accuracy over fusion readout on five of the six datasets, with gains of 2.35 and 2.16 percentage points on ISRUC-Sleep and UCDDB, respectively. To the best of our knowledge, this is the first work on joint stopping and branch selection for multimodal early time series classification.

---


### 61. [Online Learning for Minimizing Maximum Tardiness in Single-Machine Scheduling](https://arxiv.org/abs/2611.27067)

**<font color=#1a73e8>作者：</font>** Yiyang Chen, Kohei Hatano, Eiji Takimoto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online learning for minimizing maximum tardiness (\OMMT) in single-machine scheduling. In each round, the learner selects a permutation of \(n\) fixed jobs, representing a schedule. The environment then reveals a processing time and a due date for each job, and the learner incurs a vector-valued loss whose components correspond to the tardiness of the individual jobs. The goal of the learner is to minimize \(\alpha\)-regret, the difference between the learner's maximum cumulative tardiness and \(\alpha\) times that of the best fixed permutation in hindsight, for as small \(\alpha\) as possible. We investigate OMMT under both stochastic and adversarial environments. In the stochastic setting, we prove that the expected \(1\)-regret of the Follow-the-Leader (FTL) algorithm is \(
O\!\left(\frac{n\log n}{\Delta^2}\right) \), together with a corresponding high-probability bound, where \(\Delta\) is a distribution-dependent gap parameter. At round \(t \in \{1,\dots,T\}\), FTL runs in \(O(tn^2)\) time and \(O(tn)\) space. In the adversarial setting, we prove that, for any \(0<c<\log_2 n/16\), the \(\alpha\)-regret is \(\Omega(T)\) whenever \(\alpha<\log_2 n/16-c\). We then reduce OMMT to a surrogate online learning problem and apply Follow-the-Perturbed-Leader (FTPL), obtaining an expected \(\alpha\)-regret bound of \(O(n^2\sqrt{T})\) for \(\alpha=O(\log n)\). Thus, the logarithmic dependence of \(\alpha\) on \(n\) is tight up to constant factors. Each FTPL update admits a mixed-integer programming formulation whose size is polynomial in \(n\) and \(t\).

---


### 62. [ORION: Exact Canonical-State Supervision for Systematic Generalization in Transformers](https://arxiv.org/abs/2611.27087)

**<font color=#1a73e8>作者：</font>** Sibi Gokul, Jyoti Prakash Meher  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive Transformers generally fail on out-of-distribution reasoning due to two primary reasons: positional corruption over long sequences and structural state drift across deep execution steps. We introduce ORION, a framework that supervises exact canonical execution states via auxiliary heads to anchor latent trajectories to valid computational manifolds. Across Folding, GridShift, and CLRS-30, a pre-registered 2 x 2 factorial shows that RoPE and ORION address orthogonal axes. RoPE recovers length extrapolation (59.8%), while ORION recovers depth extrapolation (66.7%). Moreover, their combination complementarily achieves strict additive gain in joint length-depth extrapolation, while either method alone offers near satisfactory results. Negative controls confirm that the gain depends strictly on exact canonical alignment; hashed state statistics fail to constrain depth extrapolation.

---


### 63. [Railroads as Cyber-Physical Systems: Cybersecurity Implications of Increasing Automation -- Threats, Consequences, and Operational Resilience](https://arxiv.org/abs/2611.27088)

**<font color=#1a73e8>作者：</font>** Syed Owais Athar, Mohsin Kamal, Aemal Khattak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Objectives: Rail automation improves train protection, traffic management, inspection, and operational efficiency but increases dependence on software, communications, remote access, and external providers. This paper examines its impact on railroad cyber-physical system security and operational resilience.
Methods: A narrative review synthesizes railroad automation literature, OT security guidance, FRA and TSA materials, and documented rail cyber incidents. Automation functions are mapped to exposed assets, attack vectors, and operational consequences, focusing on signalling, communications, onboard systems, remote access, and human oversight.
Findings: Automation shifts rail risks from isolated mechanical failures toward interconnected cyber-physical dependencies. Key vulnerabilities involve train detection, positioning, signalling, grade crossings, remote diagnostics, vendor access, and AI-enabled monitoring. Cyber incidents can cause operational disruption, supply-chain impacts, and national-security risks, even when fail-safe mechanisms prevent catastrophic outcomes.
Novelty: The paper introduces a rail-specific taxonomy connecting automation functions, cyberattack pathways, operational consequences, and resilience requirements, framing cybersecurity as an operational rather than purely IT concern.
Practical Applications: The framework supports security-by-design procurement, IT/OT segmentation, secure remote access and software updates, degraded-mode planning, trusted recovery, and human oversight. Operators and regulators can use it to assess automation deployments and mitigate cyber risks.

---


### 64. [PIU-CR: Physics-Informed Deep Unfolding with SAR-Optical Image Fusion for Cloud Removal](https://arxiv.org/abs/2611.27093)

**<font color=#1a73e8>作者：</font>** Gengque Fan, Han Xu, Junxi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal cloud removal exploits complementary optical and synthetic aperture radar (SAR) images to restore cloud-degraded remote sensing images. Most existing methods rely on black-box, data-driven architectures with limited interpretability of cross-modal interactions. Although some attempts introduce physical priors into networks, their oversimplified formulations fail to faithfully characterize the underlying physical imaging process and the networks remain loosely coupled with optimization variables. To address these issues, we propose a physics-informed deep unfolding network for cloud removal via optical-SAR image fusion, termed as PIU-CR. We first formulate cloud removal as a physics-informed optimization problem. Specifically, we fundamentally ground the optimization in the physical imaging mechanism of cloud degradation by embedding the atmospheric scattering model into the data fidelity term. Then, the regularization terms establish an explicit cross-modal interaction mechanism, overcoming the single-modal information scarcity and the obscure, uninterpretable interactions in black-box models. They are dedicated to SAR-guided structure and spectral regularization, jointly introducing cross-modal structural feature alignment and coordinated spectral consistency constraints. The resulting optimization problem is then unfolded into a multi-stage neural network with dedicated structure and spectral branches. Each stage corresponds to an explicit optimization iteration step, enabling interpretable and effective reconstruction process. Experiments demonstrate that the proposed method outperforms state-of-the-art methods. The code is publicly available at this https URL.

---


### 65. [UDA-Restoration: Bridging Unsupervised Domain Adaptation and Multi-Degradation Denoising for Enhanced AV Semantic Segmentation](https://arxiv.org/abs/2611.27097)

**<font color=#1a73e8>作者：</font>** Zainab Bibi, Mohsin Kamal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles rely heavily on vision-based perception systems for safe navigation and decision-making. Adverse weather conditions, sensor noise, moving artifacts and illumination changes, however, often degrade the image quality and hence reduce perception performance. This paper introduces a diffusion-guided unsupervised domain adaptation algorithm for autonomous driving environments, namely UDA-Restoration, which is designed to enhance and denoise images. The proposed method follows the paradigm of Noise-Space Domain Adaptation (Noise-DA), which is based on multi-source degradation learning and diffusion-guided adaptation that spans across synthetic and real-world degradations. The framework has been extensively tested and shown to restore image quality and to be robust to unseen degradation scenarios, such as snow, haze, sensor distortions, and more. The quantitative results indicate that Noise-DA outperforms the evaluated self-supervised and unsupervised baselines while matching the best supervised restoration performance. In addition, semantic segmentation experiments show that the performance of downstream perception tasks is directly improved by better image restoration. The outcomes show the promise of unsupervised domain adaptation based on diffusion as a powerful and scalable method for image restoration tasks in autonomous driving systems under various environments.

---


### 66. [EgoSurgHands: An Egocentric 3D Hand Pose Dataset & Benchmark for Open Surgery Training](https://arxiv.org/abs/2611.27101)

**<font color=#1a73e8>作者：</font>** Ankit Pal, Guillaume Kugener, Sofia Volpi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical skill assessment, AR guidance, and robot learning from demonstration all benefit from 3D tracking of the surgeon's hands, yet no surgical dataset offers real egocentric articulated 3D hand pose. We introduce EgoSurgHands, a benchmark for real-captured egocentric hand pose estimation in open surgery training on synthetic pads. Captured with multi-sensor glasses, it contains 41,909 training hand-instance rows across 55 procedure recordings and 9,476 human-validated evaluation rows across 13 held-out recordings, spanning 13 tasks, 3 glove colors, and 4 trainees from first-year medical student to third-year resident. Each frame carries a multi-sensor stack: intrinsics, hand landmarks with per-hand confidence, timestamps, and eye gaze, plus SLAM extrinsics where SLAM succeeded. Evaluation labels combine sensor-fused pseudo-ground truth, human cross-review of every frame, surgeon adjudication of flagged cases, and an independent multi-view triangulated reference. Alongside the within-corpus, procedure-disjoint split, a leave-one-wearer-out protocol tested unseen trainees. Across eight methods evaluated zero-shot, from MANO-based reconstructors to the two-hand IntagHand and the keypoint-only MediaPipe Hands, egocentric pretraining was associated with stronger transfer on every held-out wearer. WildHands and JointTransformer had 18\% and 40\% lower PA-MPJPE, respectively, than the non-egocentric HaMeR. JointTransformer was the best performing model with an error of 14.95 mm. A substantial surgical domain gap remains, and the widely deployed MediaPipe Hands detected a hand in only 24.1\% of evaluation rows. As a baseline, a 58K-parameter residual corrector (JRN) on frozen backbones reached 10.96-14.85 mm PA-MPJPE on held-out wearers for the two ego-pretrained backbones. We release the dataset and benchmark code at this https URL

---


### 67. [Reliable Behavior Discovery via False Discovery Rate Control](https://arxiv.org/abs/2611.27104)

**<font color=#1a73e8>作者：</font>** David Madras, Zi Wang, Marco Andreetto 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable methods for discovering behavior patterns in large generative models are increasingly essential as models become both more complex and capable. We formalize behavior discovery as a problem class of interest and highlight the task of controlling false discovery rate (FDR) as crucial for guaranteeing reliability in behavior discovery. Building upon the multiple hypothesis testing literature, we propose DISCO (Discovery through Iterative Search with COarsened $e$-processes), a method which provably controls FDR in behavior discovery under mild conditions. DISCO improves power over previous related eBH-based approaches by allowing for adaptivity to a data-dependent number of hypotheses to be tested. We demonstrate empirically that DISCO controls FDR with higher power than comparable approaches on both synthetic data and a novel empirical evaluation of FDR-controlling methods in settings where large generative models act as both discovery engines and targets. Code is available at this https URL .

---


### 68. [RemoteEvolver: Expanding Earth Observation Capabilities through Agent Harness Evolution](https://arxiv.org/abs/2611.27110)

**<font color=#1a73e8>作者：</font>** Shengxiang Xu, Liang Yao, Shuyi Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We are interested in developing a continually self-improving remote sensing agentic system. It should identify and address its capability gaps, retaining the resulting improvements to enhance performance on subsequent tasks. However, existing systems typically rely on fixed toolsets and confine their experience accumulation to re-orchestrating predefined capabilities, constraining both capability expansion and the transfer of improvements across tasks. As the infrastructure for agentic systems, the harness manages tools and workflow knowledge as editable, persistent resources outside the base model. These resources can therefore be updated and reused across tasks without additional post-training. Based on these observations, we propose RemoteEvolver, an external harness for remote sensing agents that drives tool and workflow evolution through execution feedback. With the base model parameters fixed, RemoteEvolver acquires missing specialized tools on demand and distills verified successful execution experience from individual tasks into agent skills that can be reused across tasks. The acquired tools and accumulated skills jointly support planning and execution on subsequent tasks. Experiments on Earth-Bench and OpenEarthAgent-Bench show that RemoteEvolver achieves average accuracy gains of 8.18 and 23.86 percentage points over its initial state when tools are fully available and partially missing. Under the same settings, it also outperforms the state-of-the-art methods by an average of 6.77 and 17.10 percentage points, respectively.

---


### 69. [Federated and Balanced $k$-means: Communication Efficiency, Privacy, and Heterogeneity](https://arxiv.org/abs/2611.27114)

**<font color=#1a73e8>作者：</font>** Feiteng Nie, Shengkun Zhu, Sheng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborating on data across organizations in healthcare and finance demands methods that preserve privacy while enabling effective analysis. Vertical Federated Learning (VFL) facilitates clustering across data where different parties hold different features of the same entities without sharing raw data. However, existing VFL clustering methods suffer from two key limitations: vulnerability to information leakage and the creation of imbalanced clusters. To address these limitations, we propose Fabric, a balanced and privacy-preserving federated $k$-means algorithm. Our method decomposes the balanced clustering problem into independent subproblems for each client, using the Alternating Direction Method of Multipliers (ADMM) to efficiently handle the balance constraints. Under the semi-honest model, Fabric provides provable privacy guarantees by injecting calibrated noise into local objective evaluations. Extensive evaluations on ten real-world datasets show that Fabric achieves a superior utility-privacy trade-off compared with state-of-the-art methods and converges faster. Specifically, Fabric reduces SSE by 29.1\% on average and improves balance performance by 1.41$\times$, while being 26$\times$ faster on average.

---


### 70. [Portable Active Recovery under Timed and Position-Dependent Visual Outages](https://arxiv.org/abs/2611.27121)

**<font color=#1a73e8>作者：</font>** Jinyuan Zhang, Shengshuo Jiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a camera blackout depends on physical position rather than elapsed time, stable hovering prevents visual recovery and mission completion. On stereo visual-inertial quadrotors without external localization, an exogenous timed blackout and an endogenous position-dependent dark zone appear identical at loss onset yet require opposite responses: hover-and-wait completes 93/96 timed blackouts but 0/96 spatial outages (13 hard failures), whereas blind continuation traverses many spatial zones yet fails heavily during timed blackouts. We formulate visual-outage recovery as a worst-condition active-observability problem and introduce a portable recovery module at the reference interface of an unchanged host controller with zero retraining. Using deployable telemetry alone, the module coordinates visual-loss detection, jerk-limited braking, bounded backward probing, settled rejoining, height-integral trim, and an optional gated prior-map branch. On a preregistered 48-scene benchmark (1,920 flights), our full MPPI configuration reaches 88.5% [81.2, 94.8] worst-condition completion, outperforming development-selected DATT-L1 by +29.2 pp [17.7, 40.6] and exceeding all six external baselines after Bonferroni correction. Attached without retraining to SimpleFlight, the module lifts worst-condition completion by +17.7 pp [7.3, 28.1] to 86.5% (and 90% across 1.0x/1.25x speeds, 0/80 hard failures). Trace diagnostics reveal that survival hinges on visual-inertial re-acquisition asymmetry at vision return -- not blind IMU drift suppression - and uncover a bias-drift map crossover confirmed on 72 held-out EuRoC windows.

---


### 71. [A Plan or an Adversarial Example? A Round-Trip Check for Latent World Models](https://arxiv.org/abs/2611.27124)

**<font color=#1a73e8>作者：</font>** Huiyuan Tian, Chih-Yung Wen, Shijian Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> If we optimize an image until a classifier is confident it shows a cat, we may get an adversarial example, not a cat. Planning with a latent world model is a similar search for actions whose predicted future is closest to the goal. Is the result a plan, or an adversarial example of the world model? We show that it can be either. On the released DINO-WM and LeWM, more iterations of the cross-entropy method (CEM) lower the predicted cost but lose up to half of the problems CEM had already solved. The model's own predictions do not reveal these failures. We propose a simple test that executes the plan after every iteration and counts the problems a planner solves and then loses. Unlike an image, a plan comes with its actions, which our round-trip check reads back from the predicted states with a small network, penalizing mismatches. The check reads back the sum of each block of five actions, the part that two consecutive predicted states determine. Without retraining the world model and at only 0.2% to 3.1% more planning time, it improves the widely used planners CEM and MPPI on three released world models, and gains more where planners lose more problems. Without replanning, success rises from 0.39 to 0.76 on Wall with DINO-WM and from 0.56 to 0.94 for MPPI on JEPA-WM. With replanning (MPC), it rises from 0.70 to 0.81 on Cube with LeWM.

---


### 72. [TrajRealm: A Large-Scale Point Tracking Dataset with Diverse Dynamics](https://arxiv.org/abs/2611.27136)

**<font color=#1a73e8>作者：</font>** Ni Yang, Weiguang Zhao, Jiafei Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General-purpose point tracking requires large-scale training data with diverse dynamics, yet existing datasets struggle to combine rich dynamic content, accurate scene geometry, and sufficient scale. We introduce TrajRealm, the first public synthetic point-tracking dataset to reach the ten-million-frame scale, constructed from games and embodied simulations. TrajRealm uses the rich environments and motion systems of modern games to capture diverse targets, activities, and interactions across diverse worlds, while embodied simulations add robot manipulation and indoor navigation data. The dataset provides RGB observations, depth, camera parameters, and persistent 2D and 3D point trajectories. These annotations provide precise, geometrically consistent supervision across foreground objects and static environmental surfaces. We also build TrajRealm-Bench with eight subcategories under Interaction and Locomotion to evaluate tracking across diverse scenes. Benchmark evaluations reveal the strengths and limitations of existing trackers in handling complex motion and maintaining long-term point correspondences. Training on TrajRealm improves the performance of existing tracking methods on synthetic and real-world benchmarks.

---


### 73. [Cross-Platform Production Signatures of State-Linked Information Operations](https://arxiv.org/abs/2611.27137)

**<font color=#1a73e8>作者：</font>** Lin Tian, Marian-Andrei Rizoiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An information operation active on several platforms presents different names, personas, and topics on each. Its working routine is harder to change. We call this routine the operation's production signature: the regularities in when and how its accounts post, reply, and repost. We measure it from timestamps and coarse action types only, using no content, profile metadata, or network ties, as timing and action profiles for accounts and learned action-gap policies for populations. We then ask which parts of a signature carry over to another platform and which belong to a single operation. We train models on Twitter archives of four state-linked operations and apply them to Internet Research Agency (IRA) accounts on Reddit, with no Reddit training labels. They rank the IRA accounts at AUC 0.90-0.94. Content detectors on the same route fall from 0.98 within a platform to 0.81. Daily phase accounts for most of the transfer. Posting volume reverses direction between platforms, and action mix follows the role accounts hold on each platform. What transfers is not unique to the IRA: a second operation shares the same working-hours window, and action-gap policies separate every operation from organic accounts (AUC 0.96-1.0) without consistently ranking their own operation first. On 938 Telegram channels, groups that forward the same sources keep ordinary hours and pace but publish original posts in the same ten-minute windows more often than chance. This pattern is invisible when accounts are examined one at a time. Our results suggest that timing and action traces learned on one platform can help flag likely operations on another.

---


### 74. [Dynamic Memory-enhanced Pattern Relevance Prediction for Long-tailed Graph Classification](https://arxiv.org/abs/2611.27141)

**<font color=#1a73e8>作者：</font>** Jiawei Chen, Wenjun Wang, Wei Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-tailed graph classification (LTGC) is common in real-world graph datasets, where a few large head graphs provide rich structural information while many smaller tail graphs offer fewer structural cues, making it harder to learn discriminative representations for tail graphs. To address this size-based imbalance, we propose Dynamic Memory-enhanced Pattern Relevance Prediction (DMPRP), which transfers structural patterns from head graphs to tail graphs. Given a graph representation as a query, a dynamic expert memory module inspired by Knowledge-diverse Experts (KDEX) generates a residual vector that augments the original representation. We train the module using co-occurrence triplets sampled from head graphs at the node, rooted subgraph, and random-walk neighborhood levels. Experiments on five graph classification benchmarks show that DMPRP improves tail performance, and ablation studies show that both the expert module and random-walk supervision contribute to these gains. A controlled experiment on PTC further examines pattern transfer when smaller graphs are denser than larger ones. Our code is available at this https URL.

---


### 75. [How Does SAM-3 Adapt? Capacity, Update Geometry, and Domain Transfer](https://arxiv.org/abs/2611.27142)

**<font color=#1a73e8>作者：</font>** Allan Kazakov, Abdurrahman Javat, Duygu Cakir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Promptable segmentation foundation models are increasingly used in specialized domains, but it remains unclear how SAM-3 should be fine-tuned when adapting it beyond its original training distribution. We study this question by comparing five adaptation families --LoRA, HiRA, KRAdapter, QuanTA, and Full Fine-Tuning-- across five segmentation datasets spanning medical imaging, remote sensing, and dense material segmentation. Across these datasets, compact parameter-efficient fine-tuning methods often match or approach Full Fine-Tuning in DSC and IoU, suggesting that strong in-domain adaptation does not always require updating the full model. However, this performance cannot be explained by nominal adapter rank or trainable parameter count alone. To investigate why different methods perform similarly, we analyze their update spectra and their behavior under LoveDA Urban/Rural transfer. Our SVD analysis shows that Full Fine-Tuning updates are spectrally compressible. However, successful PEFT methods do not simply recover the same update directions; instead, they often concentrate changes in different components and subspaces. The domain-transfer study further shows that methods with similar in-domain performance can respond differently under distribution shift. Together, these results suggest that SAM-3 adaptation is often capacity-saturated in practice, while competitive fine-tuning arises through method-specific update paths rather than a single low-rank approximation to Full Fine-Tuning.

---


### 76. [GaLF-ST: Gaussian Latent Fields for Spatial Transcriptomics Reconstruction](https://arxiv.org/abs/2611.27143)

**<font color=#1a73e8>作者：</font>** Baichuan Yang, Yifan Luo, Yong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) measures gene expression at known tissue locations to reveal tissue organization and cellular function. Expression prediction requires modeling both local spatial relationships and associations among genes. Existing methods typically model expression using coordinate networks without explicit spatial parameterization. To address limited spatial sampling and sparse expression observations of ST, some methods firstly fit intermediate embeddings and then train expression predictors, but a latent representation suited to expression reconstruction may be difficult to predict from spatial coordinates. The two training stages can impose different demands on the latent representation. In this paper, we propose GaLF-ST, a Gaussian latent field method in which learnable Gaussian centers and anisotropic covariances determine the weights of latent vectors at each location. A shared nonlinear decoder maps their weighted average to multigene expression. In GaLF-ST, observed expression error jointly updates the Gaussian geometry, latent vectors, and decoder parameters. We further establish a unified benchmark across seven dataset groups and three held-out fractions, comparing GaLF-ST with four representative methods using the same locations, splits, gene panels, and scoring rules. Across tissues and observation densities, GaLF-ST achieves leading overall reconstruction performance, recovering spatial gene expression patterns and preserving tissue domains from limited observations while substantially reducing runtime and GPU memory usage.

---


### 77. [Where Structure Enters a World Model: From Predictive Fit to Physical Rollout](https://arxiv.org/abs/2611.27149)

**<font color=#1a73e8>作者：</font>** Panayiotis Christou, Satyapragnya Kar, Flavjo Xhelollari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predictive world models learn to forecast observations, but accurate short-term predictions do not necessarily produce physically coherent behavior over longer horizons. We investigate how incorporating physical structure can strengthen world models while retaining their underlying predictive objectives. Across token-based models of planetary motion and JEPA-style visual models of mechanical systems, we study conserved-quantity supervision, symmetry-aware representations, temporal consistency, and learned structured dynamics. In planetary motion, angular-momentum supervision improves autonomous next-token forecasting, while the benefits of temporal regularization depend on the accompanying physical objective and representation. In visual models, generating rollouts through supervised energy-based dynamics heads produces more faithful trajectories and phase-space evolution. Together, these findings highlight the importance of how physical structure participates in prediction: improvements in an auxiliary physical readout or a local acceleration estimate do not automatically translate into more reliable long-horizon behavior. Evaluations across initial conditions and physical parameter shifts further reveal where these benefits persist and where generalization remains limited. Our study supports physical structure as a practical means of improving predictive world models and provides a unified framework for understanding its effects on representations, learned transitions, and autonomous rollouts. The central lesson is that effective physical inductive biases should help models both represent physical regularities and use them to generate future states.

---


### 78. [Co-Evolving Behavioral Agents and Detectors for Adaptive Information Operations](https://arxiv.org/abs/2611.27156)

**<font color=#1a73e8>作者：</font>** Lin Tian, Marian-Andrei Rizoiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detectors of state-sponsored information operations (IOs) are trained on campaigns that platforms have already taken down. They lose much of their accuracy on an actor they have not seen, even though no operator in the archived data is trying to avoid them. A real operator wants two things, to reach an audience and to avoid being caught. We present IO-AI, a framework that gives simulated agents these two capabilities, engagement and evasion, and tests what each one does to detection. The agents are built from the posting behavior of real campaigns and choose the emotion, type, and timing of each post. An agent and a detector then train against each other in turn. We rank the trained agents by how hard they are to detect and train one detector on them from easiest to hardest. On 20 Twitter IO campaigns, this detector reduces missed detections of adaptive agents by 65% relative to a detector trained only on the archived campaigns, at a similar false-alarm rate. On actors it has never seen it reaches an F1 of 0.81, against 0.62. We find that an agent trained to seek engagement becomes easier to catch, because it learns the fast, emotional retweeting that archived campaigns were caught producing. An agent that was trained for engagement before the game keeps its engagement lead after it learns to evade. We also introduce a behavioral distance metric that compares two groups of accounts using only their unlabeled posting histories. The larger the distance between two groups, the worse a detector trained on one does on the other (Spearman rho = -0.58), so the metric can be used to choose which new groups to test first.

---


### 79. [Real-Anchored Complementary Evidence for Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2611.27161)

**<font color=#1a73e8>作者：</font>** Wenpeng Mu, Tanfeng Sun, Zhenyu Shao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evolving generative models challenge detector generalization, as methods trained on generated examples may rely on generator-specific cues. By contrast, authentic photographs share regularities rooted in physical image formation and acquisition, providing a common reference beyond individual generators. Building on these regularities, we propose Real-Anchored Complementary Evidence (RACE), which learns complementary global and local detection evidence using only authentic training images. First, the global pathway combines frozen and learned representations to assess proximity to authentic references. Next, it incorporates responses to controlled perturbations, complementing static compatibility with representation sensitivity. The local pathway then reconstructs complete trace descriptors, using intermediate features and signed perturbation responses as context while restricting detection evidence to static terminal-residual reconstruction errors. Finally, authentic-image statistics align the global and local scores for fusion, and an independent authentic set calibrates a decision threshold held fixed across test generators. Across six benchmarks, RACE achieves the highest average AUROC of 96.59% among the compared methods, reaching 97.18% on five out-of-domain benchmarks. Together with robustness to image perturbations and variation in authentic-image sources, these results support authentic-image regularities as a transferable basis for detection across diverse generators and image conditions.

---


### 80. [Hierarchical Hybrid-Coordinate Flow Matching for Accurate and Physically Plausible Apo-to-Holo Protein Generation](https://arxiv.org/abs/2611.27162)

**<font color=#1a73e8>作者：</font>** Minjong Kim, Jaemin Sim, Dongwoo Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting holo-like protein conformations from apo structures is essential in structure-based drug design. Most existing apo-to-holo models operate in Cartesian space and achieve strong global accuracy. However, high global accuracy does not ensure physically valid local backbone geometry. Internal-coordinate models offer local control and validity, but regressive generation can amplify angular errors, known as the lever-arm effect. We introduce CrypticFlow, a hierarchical flow-matching model that combines these two complementary representations. An ESM-3-conditioned E(3)-equivariant graph network first generates sparse C$\alpha$ anchors in Cartesian space. A conditional midpoint Transformer then recursively fills the gaps in local internal coordinates. During recursive generation, the decoder constrains the distance between each midpoint and any sequence-adjacent parent anchor to the corresponding apo C$\alpha$-C$\alpha$ distance. On the D3PM test split, CrypticFlow achieves the lowest median and mean C$\alpha$ RMSD at published baseline capacities. Across five independent training models, the median and mean direct RMSD are 1.333 $\pm$ 0.056 angstroms and 2.766 $\pm$ 0.041 angstroms, respectively. The quality of local geometry also improves substantially. Our model achieves 99.58 $\pm$ 0.02% adjacent-distance fidelity and 95.87 $\pm$ 0.25% pseudo-angle fidelity, measured within 0.2 angstroms and 20° of the holo reference. Then, we reconstruct the predicted C$\alpha$-only traces into all-atom structures using the cg2all coarse-to-all-atom backmapping method and evaluate their physical and geometric quality with MolProbity. Our model achieves a MolProbity score of 3.034 $\pm$ 0.054, outperforming the evaluated baselines. These results show that a hierarchical flow-matching model with hybrid coordinates can recover global accuracy while retaining local fidelity.

---


### 81. [PhysForce: Physics-aware Force Control for Interactive Video World Model](https://arxiv.org/abs/2611.27164)

**<font color=#1a73e8>作者：</font>** Xuancheng Xu, Xiaofeng Wang, Yue Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video world models aim to predict how visual environments evolve in response to user interventions, including physically consistent state changes induced by applied forces. Existing methods often represent forces as motion trajectories, which may introduce inappropriate motion priors, causing the model to over-rely on encoded displacement patterns. More fundamentally, the model's internal representations do not reliably localize force-induced state changes, making it difficult to associate applied forces with their resulting physical responses. Also, limited force-annotated data make it difficult to produce physically consistent and temporally stable predictions in unseen scenarios. To address these limitations, we propose PhysForce, a two-stage framework that integrates supervised fine-tuning and reinforcement learning through three complementary components. During supervised fine-tuning, (1) the Latent Force Intervention Encoder maps force location, direction, and magnitude into the video latent space without exposing future motion; and (2) the Physics Attribution Network associates force interventions with localized changes in the latent state, strengthening the learning of physical responses to applied forces. During reinforcement learning, (3) Physics-Aware Reinforcement Learning uses self-supervised rewards on out-of-distribution videos to improve physical consistency and generalization. Extensive experiments show that PhysForce improves force responsiveness, physical consistency, and generalization, demonstrating its effectiveness for interactive video world models.

---


### 82. [Mem-X: A Memory-Dependent Cross-Episode Benchmark for Vision-and-Language Navigation](https://arxiv.org/abs/2611.27166)

**<font color=#1a73e8>作者：</font>** Zhikang Shi, Yuk Tung Samuel Fang, Hongyu Ding 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables embodied agents to reuse past observations across tasks. However, existing cross-episode vision-and-language navigation (VLN) benchmarks often leave it unclear whether successful navigation relies on historical memory or current exploration. We introduce Mem-X, a benchmark designed to evaluate memory-dependent cross-episode VLN. Mem-X organizes episodes into sessions in which subsequent instructions refer to objects or routes encountered in earlier episodes. Its three levels evaluate historical-object recall, in-memory localization and episodic indexing, and off-memory relocalization and historical-route reproduction. For the latter two levels, agents receive episode-local poses but no transformations between episode frames, requiring them to establish spatial correspondence with historical memory. Mem-X comprises 2,071 episodes across 710 sessions in 34 scenes, including 1,204 memory-dependent episodes. We also provide MemBridge, a modular baseline that combines semantic scene memory, cross-episode localization, and coarse-to-fine retrieval to support existing VLN agents. Experiments with state-of-the-art VLN methods demonstrate the benefits of MemBridge while revealing substantial room for improvement on memory-dependent navigation. The benchmark and baseline code are available at this https URL.

---


### 83. [BusemannFormer: Horospherical Self-Attention for Hyperbolic Graph Transformers](https://arxiv.org/abs/2611.27167)

**<font color=#1a73e8>作者：</font>** Youheng Yao, Ziyao Zeng, Wenbo Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic neural networks excel on hierarchical graph data, yet existing hyperbolic Transformers largely adapt conventional attention without explicitly exploiting the ideal boundary, a geometric structure closely tied to tree hierarchy. We propose Horospherical Self-Attention (HSA): each query selects an ideal-boundary direction and scores keys by their Busemann depth along that direction, yielding a token-to-token hyperbolic attention kernel. We establish a flat-limit connection to dot-product attention, characterize score level sets as horospheres, and bound key-side gradients. HSA is integrated into BusemannFormer, a fully hyperbolic graph Transformer, with a log-depth variant that uses query depth to modulate attention concentration. We further introduce a finite-boundary-dictionary extension supporting linear-complexity global attention. Experiments on hierarchical and citation graphs show that BusemannFormer-LD outperforms the evaluated baselines on several node-classification benchmarks and achieves competitive performance across diverse graph structures.

---


### 84. [FedQCal: Quadratic Programming with Dual-Space Calibration for One-Shot Federated Learning](https://arxiv.org/abs/2611.27170)

**<font color=#1a73e8>作者：</font>** Shunsei Koshibuchi, Hiroshi Kera, Kazuhiko Kawamoto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-shot federated learning must combine heterogeneous client models after a single upload. Different local class distributions make it difficult to decide which client updates to retain. We propose FedQCal, which uses a reference model trained on a small labeled server set to define alignment requirements for aggregation. The key idea is to retain sufficient reference alignment while avoiding unnecessarily large aggregation coefficients. A minimum-norm quadratic program (QP) enforces these requirements. Classification loss on the same server examples selects a merge through two dual variables, so the alignment thresholds need not be prescribed in advance. We prove that the selected coefficients remain exact QP solutions at their induced thresholds. A perturbation bound explains how coefficient norm limits the amplification of projection errors. Experiments on CIFAR-10, CIFAR-100, and SVHN show gains over one-round FedAvg in most settings. Ablations support reference-guided weighting and coefficient calibration, even with one labeled server image per class.

---


### 85. [GEG-SAM: Gaze Exploration-Guided Segment Anything Model for Weakly Supervised Polyp Segmentation](https://arxiv.org/abs/2611.27183)

**<font color=#1a73e8>作者：</font>** Ao Wang, Lei Zhang, Lituan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Endoscopist gaze offers an unobtrusively acquired record of lesion-oriented visual exploration during routine clinical inspection, providing relevant supervision for tasks. However, existing methods treat fixations as isolated spatial prompts directly associated with the target, overlooking the fact that natural gaze records a continuous visual search process in which fixations are temporally connected, spatially organized, and coupled with the visual content. Interpreting each fixation independently based only on its local visual content overlooks the temporal evolution and spatial organization of the gaze trajectory, whereas modeling relations among fixations alone cannot reveal the visual semantics of the regions they attend to. To this end, we propose the Gaze Exploration-Guided Segment Anything Model (GEG-SAM), a principled weakly supervised framework designed to explicitly exploit structured gaze relations and their corresponding visual cues to modulate SAM for polyp segmentation. Specifically, GEG-SAM captures structured gaze relations by modeling the temporal dynamics and spatial topology of gaze exploration. It then associates these relational representations with fixation-aligned visual context to derive gaze-conditioned tokens, which are further injected into the frozen SAM encoder to modulate its pretrained image features. In this way, GEG-SAM effectively exploits the rich information embedded in gaze exploration to guide SAM toward lesion-oriented segmentation. Extensive experiments on five public polyp segmentation datasets demonstrate the effectiveness of our approach, improving the mean Dice by 9.30 percentage points over the strongest weakly supervised baseline.

---


### 86. [Lift Out, Kick In: Decoupling Event Effects for Time Series Forecasting](https://arxiv.org/abs/2611.27191)

**<font color=#1a73e8>作者：</font>** Yunying Zhu, Zichun Cao, Siwei Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time series are often shaped by exogenous events whose effects are superimposed on the system's underlying temporal dynamics. Historical observations therefore entangle persistent dynamics with event-induced deviations, making it difficult to determine which patterns should be extrapolated and which should be attributed to specific event contexts. Existing event-aware forecasting methods can incorporate event information or model event-related variation, but typically treat historical event attribution and future event generation separately. We propose Loki (Lift Out, Kick In), a general event-aware forecasting framework built on a shared Event Response Function (ERF). The ERF models event effects according to event type and relative temporal position and is shared across the historical and forecast windows. Loki lifts out estimated event-induced deviations from historical observations before forecasting, then uses the same ERF to kick in responses to known future events. This formulation separates event-response modeling from temporal forecasting while coupling historical attribution and future generation through a shared mechanism. Across five forecasting benchmarks, Loki achieves the best standardized MAE on all five datasets, reducing error by approximately 2.2%-11.7% over the strongest non-Loki baseline. Ablations and controlled analyses further support the roles of Lift Out, Kick In, shared response modeling, and compatibility across forecasting backbones.

---


### 87. [How Much of a Calculation-Error Rate Is Not Arithmetic: Auditing the FinReason Cup 2026 Task 3 Metric with a Deterministic Rule System](https://arxiv.org/abs/2611.27192)

**<font color=#1a73e8>作者：</font>** Vladimir Beskorovainyi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task 3 of the FinReason Cup 2026 scores a system on two values per case, the one an XBRL filing reports and the one its own calculation relationships imply, and labels each failure as structural, extraction or calculation. This report shows that the calculation-error rate so defined does not count arithmetic failures, and bounds how far it is from one using the published board alone. One of the three rules behind the benchmark, DQC_US_0015, has an answer that is the negation of the reported value (in all 110 published practice cases, against 1 of 120 and 6 of 102 for the other two), so a calculation label on such a case records a wrong fact or a wrong route, not a wrong sum. Subtracting the available structural and extraction labels from each entry's error count on that rule gives a floor: the bound is positive for 22 of the 23 ranked entries, and at the top it is sharpest, with at least 11 of 12 and 12 of 13 calculation errors of the two joint-first entries falling on cases where no arithmetic remained. The calculation-error rate of the best systems on this task is almost entirely not arithmetic.
The vehicle for that result is an entry that reconstructs the three data-quality rules the benchmark is drawn from, DQC_US_0015, DQC_US_0117 and DQC_US_0126, as a deterministic system with no learned parameters, no training step and no external service, running all 680 cases in 1.4 seconds. It scores 96.62% under the offline judge on development and 95.29% on the published test set, and its residual error concentrates in cases where a concept carries several equally flagged facts and the question names no dimensional member. Reading those error classes against the per-rule accuracies is what exposed the metric, which is why both are reported here.

---


### 88. [DepthMSA: Combinatorial Training and Budget-Aware Depth Allocation for Multimodal Sentiment Analysis](https://arxiv.org/abs/2611.27198)

**<font color=#1a73e8>作者：</font>** Pan Wang, Jie Peng, Zhimin Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art multimodal sentiment analysis (MSA) models rely on large pretrained encoders, yet typically process every modality to its full depth, regardless of its computational cost or predictive contribution. This raises a fundamental question: how should limited computation be allocated across modalities to preserve predictive performance? We reveal a substantial mismatch between the computational cost of modality encoders and the predictive benefit of processing them more deeply, suggesting that different modalities require different encoding depths. However, enabling heterogeneous depths introduces a key challenge: representations extracted at different depths must still be effectively fused. To address this, we propose $\textbf{DepthMSA}$, a budget-aware framework that supports flexible modality depths within a single MSA model. Specifically, we introduce combinatorial anytime training, which supervises the fusion head across all cross-modal depth combinations using a single full-depth encoder pass. At inference, a training-free, cost-aware allocator selects the configuration with the lowest validation-calibrated error under a sample-specific FLOPs budget. On CMU-MOSEI, DepthMSA maintains accuracy within one percentage point of the full-depth model while reducing measured FLOPs by 45\%, or by 82\% with a separately trained skip-enabled variant. When a CLIP visual encoder dominates computation, the allocation shifts toward reducing visual depth, achieving 56\% fewer FLOPs at unchanged accuracy. Compared with ADMN, an adaptive layer-allocation method that trains a controller for each budget, the skip-enabled variant reaches its accuracy with 3.2$\times$ fewer FLOPs and lower latency, without any per-budget training. Our project is available at this https URL.

---


### 89. [Enhancing Metaverse Security using Explainable AI-based Intrusion Detection Framework](https://arxiv.org/abs/2611.27199)

**<font color=#1a73e8>作者：</font>** Esha Kuppanda, Shalaka Mahadik, Pranav M. Pawar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The MoT virtual environment, called the Metaverse of Things (MoT), combines machine learning (ML) and Internet of Things (IoT) to offer significant business opportunities in various sectors such as entertainment, healthcare, and education. In addition to its benefits, the MoT poses risks to privacy and security through unauthorized access, which threatens trustworthiness. While traditional intrusion detection systems (IDS) exist to handle this challenge, they struggle with high-dimensional data and poor interpretability. To address this challenge, the research conducted a thorough analysis of different ML models and proposed the optimal model to secure the MoT environment. The research employed explainable artificial intelligence (XAI) to identify the most effective features that contributed to optimal model selection. The research presented an optimal framework combining ML and XAI to safeguard MoT networks from the most recent cyberthreats. The research used three advanced benchmark security datasets: ToN-IoT, CIC-IoT-2023, and BoT-IoT, to examine the XAI-based intrusion detection framework. The XAI-based intrusion detection framework achieved 99.83% accuracy on ToN-IoT and 96.45% on CIC-IoT-2023 using the XGBoost model. On the BoT-IoT dataset, the Random Forest (RF) and Extra Trees (ET) classifiers reached 99.99% accuracy. The Shapley Additive Explanations (SHAP) and Local Interpretable Model-Agnostic Explanations (LIME) techniques used for XAI further enhanced feature relevance and user confidence in the optimal model.

---


### 90. [Backbone-Specific LoRA Geometry: Orthogonality, Superposition, and Provenance](https://arxiv.org/abs/2611.27201)

**<font color=#1a73e8>作者：</font>** Kazuhiko Kawamoto, Keigo Watanabe, Hiroshi Kera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sharing one low-rank adaptation (LoRA) update across pretrained models simplifies deployment. Composition methods typically combine updates from a common backbone, while cross-model transfer transforms updates for a target backbone. The conditions for sharing updates across backbones while preserving accuracy and distinguishing individual contributions remain unclear. Our idea is to use backbone-specific update directions as signatures of their training backbones. We derive a cross-backbone correlation bound from attention symmetries and equivariant LoRA learning under independent, uniform pretrained feature orientations. A local gradient-flow model explains positive mean correlation between independent runs on the same backbone and task. These patterns motivate cosine-based backbone identification and inner-product tests for registered-adapter reuse without coordinate alignment. Experiments on CLIP backbones show that shared sums achieve nearly the same mean accuracy as separate adapters. Cosine scores reliably identify source backbones across the evaluated tasks. Registered adapters remain detectable in sums of adapters from different backbones.

---


### 91. [LingSante-Pulse: Unified Physiological Pretraining through Random-Feature Prediction and Cross-Modal Alignment](https://arxiv.org/abs/2611.27206)

**<font color=#1a73e8>作者：</font>** Linxiao Yang, Wenwei Wang, Tian Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical monitoring and wearable devices capture complementary physiological signals, but their partially overlapping modality coverage makes within-signal information and cross-modal relationships difficult to exploit jointly. We introduce LingSante-Pulse, a unified, general-purpose and flexible physiological representation framework that learns from these heterogeneous recordings. A shared, signal-conditioned encoder processes each physical channel independently and supports different numbers and combinations of signals for multimodal assessment and single-sensor inference. Pairwise cross-modal alignment, structured random-feature prediction (RFP) and masked waveform reconstruction jointly learn physiological relationships and preserve informative within-signal structure. Across 38 general physiological task configurations spanning PPG, ECG, EEG and EMG, the frozen encoder achieves the best dataset-balanced mean rank in each domain. In sleep assessment, multimodal staging on the HMC dataset and EEG-only staging on the Sleep-EDF dataset reach Macro-F1 scores of 0.7784 and 0.7941, respectively, while single-lead ECG apnea screening achieves an AUROC of 0.9183. Controlled experiments show that function prediction and waveform reconstruction provide complementary supervision for retaining temporal and rhythmic information. Representations learned under continually refreshed random supervision generalize to unseen teacher realizations, and correct auxiliary modality correspondence improves respiration-only representations. These results demonstrate that a single encoder can learn reusable physiological features across signal types, prediction targets and sensor configurations from partially overlapping recordings.

---


### 92. [A Stationarity-Based Regret Framework for Time-Varying Nonconvex Composite Optimization](https://arxiv.org/abs/2611.27218)

**<font color=#1a73e8>作者：</font>** Nadav Hallak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies time-varying nonconvex composite optimization, where decisions are made sequentially and classical value-based regret notions are generally ill-posed. We introduce a stationarity-based performance framework defined through local regret measures built from first-order optimality conditions, and identify minimal structural requirements under which such measures constitute sound performance criteria. This abstraction encompasses canonical optimality measures, including the proximal-gradient residual, and collapses to classical dynamic regret in convex settings. We then focus on the proximal-gradient residual as a concrete and algorithmically meaningful instantiation for general composite problems. In convex problems, we show that the resulting local regret is equivalent to standard dynamic regret. In nonconvex settings, we establish that sublinear stationarity-based regret is unattainable without temporal regularity, and introduce a gradient-variation budget that captures this necessity. Under this model, we analyze online proximal-gradient methods and prove sublinear regret guarantees in both nested multi-call and fully incremental single-call oracle regimes, highlighting the tradeoff between per-round computational effort and achievable performance. Finally, we demonstrate how the proposed framework extends to nonconvex multiplayer games by interpreting equilibrium-seeking dynamics through stationarity-based regret, and corroborate the theoretical findings with numerical experiments.

---


### 93. [LiDAR Signals for Robot Locomotion: Spherical Range Images Enable Robust Sim-to-Real Transfer](https://arxiv.org/abs/2611.27223)

**<font color=#1a73e8>作者：</font>** Nian Liu, Xinyi Tong, Ming Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing legged-locomotion systems commonly rely on depth images or online elevation maps. However, depth-based policies suffer from perceptual sim-to-real discrepancies due to imperfect depth sensor modeling, while map-based approaches are vulnerable to drift and misalignment. LiDAR offers direct measurements of the surrounding geometry, but raw LiDAR scans lack a compact, structured representation for high-frequency control. We propose a LiDAR perception pipeline that maintains perceptual consistency across simulation and reality through sensing- and representation-level alignment. At the sensor level, we recover frame-wise angular sampling patterns from the physical LiDAR and replay them in simulation with GPU ray casting. At the representation level, simulated and real returns undergo the same spherical range image encoding, yielding a fixed-size policy observation for end-to-end training and direct deployment without teacher--student distillation, online elevation mapping, or adaptation. Experiments show that our range-image policies achieve stronger sim-to-real transfer than depth- and elevation-map-based baselines, while ablations confirm the importance of the proposed sensing components. More visualizations and real-world videos are available at the \href{this https URL}

---


### 94. [EAST: Event-Anchored Surface Transport for Event-Based Gaussian Reconstruction](https://arxiv.org/abs/2611.27224)

**<font color=#1a73e8>作者：</font>** Ke Luo, Wei Zhai, Yuliang Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-supervised Gaussian reconstruction combines the high temporal resolution and wide dynamic range of event cameras with efficient explicit rendering. However, recovering a continuous surface remains difficult: changes in rendered appearance can compensate for depth errors while preserving the predicted brightness changes. We introduce Event-Anchored Surface Transport (EAST), which couples an event-constrained signed distance field to Gaussian rendering. Triangulation-supported candidates anchor the zero set, while normal flow measured from event timing constrains ray-surface intersection depths. Gaussian centers receive bounded corrections from the descriptor difference between the live field and a frozen initial reference. The correction is zero at initialization, yet transmits image gradients to the live field. Experiments on PAEv3D and NeRF Synthetic show improved surface accuracy and reference-view rendering over Gaussian baselines, together with efficient mesh extraction from the learned field.

---


### 95. [Prune to Expand: Training Prompt Enhancers with Less to Imitate](https://arxiv.org/abs/2611.27229)

**<font color=#1a73e8>作者：</font>** Tianhe Wu, Qilin Sun, Kede Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt enhancement (PE) refines concise user prompts into detailed descriptions to improve the compositional aesthetics of generated images while preserving user intent. A common practice constructs supervised fine-tuning (SFT) pairs by deriving short, user-like prompts from dense captions, implicitly assuming that captions that improve image generation also provide effective supervision. In this paper, however, we uncover a counterintuitive finding: PE models trained on caption pairs with substantial generation gains perform comparably to those trained on pairs with only marginal gains. We argue that dense captions can impose redundant supervision by requiring PE models to reproduce image-specific details weakly related to user intent. Motivated by this discrepancy, we introduce Prune to Expand (P2E), a simple text-only method that refines dense-caption supervision by selectively removing redundant sentences under a per-example deletion bound while preserving explicit user requirements and informative visual structure. Extensive experiments under identical training configurations demonstrate that P2E improves alignment with human preferences and visual quality over conventional dense-caption SFT across diverse image categories and visual generators.

---


### 96. [PCC: Proof-Carrying Credentials for Enhanced Anonymity and Post-Quantum Delegation](https://arxiv.org/abs/2611.27250)

**<font color=#1a73e8>作者：</font>** Zixuan Wang, Zheng Tianyu, Yuan Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Delegatable Anonymous Credentials (DACs) support anonymous exercise of authority delegated through intermediaries, as in DeFi credit delegation. Existing DACs require holders to possess and process chain-shaped lineage material for presentation. We call this limitation \emph{prover awareness}: presentation cost grows with delegation depth, while holder-visible topology can enable lineage-based vetoes, strategic disintermediation, and de facto censorship.
We formalize the privacy dimension as \emph{Enhanced Delegation Anonymity} (EDA), a leakage-parametrized two-observer notion combining verifier-side anonymity with holder-side topology obliviousness. We give simulation and indistinguishability formulations over paths with identical allowed holder leakage. Our framework, \emph{Proof-Carrying Credentials} (PCC), addresses both limitations by replacing the explicit chain with a recursively updated proof-carrying state via Non-Uniform Incrementally Verifiable Computation (NIVC). PCC makes presentation independent of delegation depth and hides topology beyond permitted leakage, while preserving restricted delegation and expressive presentation.
Unlike pairing-based constant-size DACs, PCC is hardness-agnostic and admits a post-quantum-compatible instantiation in the QROM using transparent FRI-based recursion and hash-based signatures. On consumer-grade hardware, the Halo2 instantiation keeps a constant 7.344\,KB verifier-facing proof with 35--36\,ms verification across all tested depths. The 128-bit Plonky2 instantiation keeps a constant 157.9\,KB proof with 3.8\,ms verification across depths $L\in\{1,2,4,8,16\}$, at 1.03\,s per delegation step. These results demonstrate practical depth-independent presentation and holder-side topology hiding.

---


### 97. [Beyond Prompt Imitation: Capability-Aware Video Generation with Smaller Models](https://arxiv.org/abs/2611.27252)

**<font color=#1a73e8>作者：</font>** Ziqi Ding, Yuxin Cao, Kai Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inference-time methods that lift a small open video generator toward a proprietary one are compared through preference scores, which never say how much of the gap to a target video they close. We introduce the oracle control ladder, which hands a fixed student progressively richer information from a target clip and reads the closure of each fidelity metric at each rung as an empirical headroom reference for the methods that must synthesize that information. On 954 clips of the principal student, a dense caption reproduces little of the appearance and almost none of the motion of a target, a first frame closes half of the appearance gap and a tenth of the motion gap, a depth video closes three quarters of the motion gap and leaves color untouched, and the two together close 64 to 94% of every fidelity gap across four teachers, while a second student agrees on the rungs that it accepts. An item response model forecasts which rung closes which clip with held-out AUC of 0.76 to 0.95 on the fidelity criteria and serves as the prior of a budgeted selection policy. When controls are free, a fixed dense-control rung is hard to improve upon, and once controls are priced the policy lies above the fixed-rung frontier at matched cost and survives critics that ruin critic-driven search.

---


### 98. [Proactive Defense Benchmark against Deepfake Generation](https://arxiv.org/abs/2611.27253)

**<font color=#1a73e8>作者：</font>** Joonhyuk Baek, Wonjune Seo, Jae-yun Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite the proliferation of proactive defenses against deepfakes, the lack of a unified evaluation protocol precludes fair comparison and masks critical vulnerabilities. To bridge this gap, we present the first comprehensive benchmark that systematically assesses disruption, robustness, and transferability encompassing pixel, perceptual, and identity metrics. Our extensive analysis reveals that fidelity and identity metrics capture orthogonal performance axes, often leading to conflicting interpretations when relied upon individually. Furthermore, we identify a fundamental trade-off where peak white-box performance signals overfitting, and we introduce a calibrated evaluation to correct generator-induced identity bias. By exposing these blind spots, we establish a rigorous standard to guide the development of genuinely generalizable protections. Project page is available at: this https URL

---


### 99. [A preference for local interaction between layers emerges during training](https://arxiv.org/abs/2611.27258)

**<font color=#1a73e8>作者：</font>** Jiheon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A deep neural network is a stack of layers, and all layers are trained to lower one shared error. A change in one layer can therefore reach every other layer. Because the error is shared by all layers, one would expect the other layers to respond alike, whether they are next to the changed layer or far from it. We find that early in training the response is weak and its order by distance is not stable. As training proceeds, the response grows, and neighboring layers come to respond to changes in each other more strongly than layers further apart, in almost every network. This locality forms during training, although training links every layer to every other. We show this by pushing one layer of a copy of the network at many stages of training and measuring how much of the push reaches each of the other layers. The experiments use 512 five-layer networks trained on modular addition with each of two optimizers, AdamW and stochastic gradient Langevin dynamics.

---


### 100. [MODULE: A Mutual-Promoting Deep Unfolding Framework Towards Degradation-Robust Multi-modal Image Fusion](https://arxiv.org/abs/2611.27269)

**<font color=#1a73e8>作者：</font>** Yunfei Deng, Han Xu, Jiayi Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal image fusion is crucial for comprehensive scene representation, yet real-world degradations compromise its efficacy, necessitating degradation-robust fusion paradigms. Existing degradation-robust multi-modal image fusion methods are often hindered by cascaded sub-optimal solution or black-box opacity. To address these challenges, we propose a theory-inspired mutual-promoting deep unfolding framework. It reformulates degradation-robust image fusion as a joint optimization problem, utilizing the degradation model and modality generation mechanism to explicitly model both single-task priors and cross-task dependencies. By decomposing the complex multi-task optimization problem into task-related iterative subproblems, the framework establishes a bidirectional reciprocal information flow between restoration and fusion. This process is further unfolded into a multi-stage deep neural network, where each component explicitly corresponds to a specific mathematical operation. In our framework, the fused cross-modal prior actively regularizes the ill-posed restoration, while the purified modality features continuously refine the fusion output. It ensures a transparent architecture that combines the merits of both model-based and data-driven methodologies. Extensive experiments demonstrate that our paradigm achieves state-of-the-art performance while providing superior interpretability. The code is publicly available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-206](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
