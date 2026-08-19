# 📦 其他研究 | 2026年08月20日

> 本类共 **173** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-173](./part-04.md)

---

### 51. [How smoothing the affinity matrix affects neighborhood preservation in t-SNE](https://arxiv.org/abs/2608.17190)

**<font color=#1a73e8>作者：</font>** Shirin Mohebi, Guillaume Bied, Jefrey Lijffijt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimensionality reduction methods are instrumental to visualize high-dimensional data, and t-SNE stands as one of the most widely used methods due to its emphasis on local neighborhood preservation. A central component of t-SNE is the affinity matrix, which expresses pairwise similarities in the form of symmetrized probabilities, over which the optimization problem of t-SNE is defined. We study how the sharpness of this probability distribution affects neighborhood preservation at different scales. We introduce a row-wise power transform controlled by a parameter gamma that can smooth or sharpen each row of the affinity matrix while preserving sparsity and rank order. We show that this transform is equivalent to rescaling the Gaussian bandwidth and thus to changing the perplexity. However, as the sharpness of the probability distribution varies per point, a fixed gamma leads to point-dependent effective perplexities, making it distinct from changing the global perplexity. Empirically, we find that sharpening improves preservation of the very nearest neighbors, while smoothing improves preservation of broader local neighborhoods, outperforming alternative affinity constructions including multiscale methods in the mid-local range.

---


### 52. [Pessimistic Meta-Induction and Its Limits: Lessons from Frequentist Statistics and Machine Learning Theory](https://arxiv.org/abs/2608.17213)

**<font color=#1a73e8>作者：</font>** Hanti Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper challenges the pessimistic meta-inductive argument against scientific realism by undermining its inductive step rather than its historical premise. Although related challenges already exist, I develop a new one. Drawing on a general epistemology of scientific inference developed in frequentist statistics, machine learning, and formal epistemology, I evaluate induction in terms of convergence to the truth. I argue that ordinary enumerative induction can achieve everywhere convergence, whereas meta-induction fails even to achieve almost everywhere convergence. Indeed, in the problem context where meta-induction arises, the failure is deeper: no inference method whatsoever achieves almost everywhere convergence.

---


### 53. [Probing Association Instability with Track-State Perturbations for Clip-Level Active Learning in Query-Propagation Multi-Object Tracking](https://arxiv.org/abs/2608.17224)

**<font color=#1a73e8>作者：</font>** Riku Inoue, Shogo Sato, Kazuhiko Murasaki 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training query-propagation end-to-end multi-object tracking (MOT) models requires dense bounding-box and identity annotations across video sequences, making dataset construction expensive. Clip-level active learning reduces this cost by selecting video clips for annotation, but prior acquisition criteria based on output-level temporal uncertainty may miss clips whose informativeness comes from association instability in propagated track states. We propose QPID (Query-Propagation Instability and Diversity), a clip acquisition method for query-propagation MOT that targets association instability in propagated track states. QPID estimates this instability by applying two-sided perturbations to internal track states and measuring prediction differences from a clean reference branch. The key idea is that, in stable clips, each propagated track should continue to follow the same target under small perturbations, whereas in ambiguous clips, small changes in the track state can alter which target the track follows, leading to changes in localization or confidence. QPID measures these perturbation-induced prediction differences with two metrics: Localization Drift and Entropy-Weighted Confidence Discrepancy. These metrics are aggregated into a clip-level association-instability score. To avoid redundant uncertainty-only selection, QPID selects a representative annotation batch from high-instability clips using Uncertainty-Weighted Visual Coverage with track-level visual prototypes. Experiments on DanceTrack and SportsMOT with MeMOTR and SambaMOTR show that QPID achieves strong performance compared with active learning baselines under the same annotation budget.

---


### 54. [Delta2Gamma: Band-Wise Adaptive Contrastive Learning of EEG for Alzheimer's Disease Detection](https://arxiv.org/abs/2608.17231)

**<font color=#1a73e8>作者：</font>** Chanwoo Park, Chanwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-cost, scalable screening for dementia remains an open problem. Imaging-based diagnosis is costly and hard to deploy widely. Electroencephalography (EEG) is portable and inexpensive, but its recordings are noisy, vary widely across subjects, and carry few clinical labels. We tackle this with Delta2Gamma, a self-supervised framework that learns EEG representations from unlabeled data by contrasting augmented views of each signal. Rather than treat EEG as a single stream, Delta2Gamma decomposes every recording into the five canonical neural rhythms (delta, theta, alpha, beta, gamma). Each band gets its own encoder and projection head. Each also gets a temperature that is predicted adaptively during contrastive training, so bands with different signal statistics are balanced automatically. On the ADFTD cohort under a strict leave-one-subject-out protocol, Delta2Gamma separates Alzheimer's disease from cognitively normal controls with 92.4\% accuracy. This exceeds both supervised backbones and recent dedicated EEG methods.

---


### 55. [Physics-Informed and Hybrid Machine Learning in Additive Manufacturing: Application to Fused Filament Fabrication](https://arxiv.org/abs/2608.17246)

**<font color=#1a73e8>作者：</font>** Berkcan Kapusuzoglu, Sankaran Mahadevan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article investigates several physics-informed and hybrid machine learning strategies that incorporate physics knowledge in experimental data-driven deep-learning models for predicting the bond quality and porosity of fused filament fabrication (FFF) parts. Three types of strategies are explored to incorporate physics constraints and multi-physics FFF simulation results into a deep neural network (DNN), thus ensuring consistency with physical laws: (1) incorporate physics constraints within the loss function of the DNN, (2) use physics model outputs as additional inputs to the DNN model, and (3) pre-train a DNN model with physics model input-output and then update it with experimental data. These strategies help to enforce a physically consistent relationship between bond quality and tensile strength, thus making porosity predictions physically meaningful. Eight different combinations of the above strategies are investigated. The results show how the combination of multiple strategies produces accurate machine learning models even with limited experimental data.

---


### 56. [ADAPTD: Adaptive Detection and Proactive Threat Defense for Autonomous APT attacks](https://arxiv.org/abs/2608.17251)

**<font color=#1a73e8>作者：</font>** Yeongwoo Kim, Quanyan Zhu, György Dán  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advanced persistent threat (APT) actors increasingly employ sophisticated techniques to propagate laterally through segmented enterprise networks. Timely detection and defense depend on cross-subnetwork coordination, yet maintaining global situational awareness generates substantial communication overhead. To manage this tradeoff, flexible monitoring and adaptable containment are imperative. This paper presents ADAPTD, a communication- and computation-efficient, decision-theoretic framework integrating: (i) compact kill chains for identifying diverse attack vectors, (ii) an immediate blocking mechanism for timely containment, and (iii) a predictive eviction strategy to restore system security. Our experiments validate ADAPTD's effectiveness across diverse threat scenarios. First, our decentralized belief update scheme outperforms state-of-the-art diffusion HMM. Second, ADAPTD substantially reduces false evictions compared to transformer-based detection. Third, under noisy environments, adaptive blocking contains attackers while minimizing unnecessary disruption. Lastly, the ablation study confirms that combining two defensive actions significantly reduces the defender's total cost.

---


### 57. [Heterogeneity-Aware Deep Learning for Tumour Classification from Multiparametric MRI](https://arxiv.org/abs/2608.17254)

**<font color=#1a73e8>作者：</font>** Yue Xia, Euijoon Ahn, Tian Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intra-tumoural heterogeneity (ITH) reflects spatial variation in tumour biology and is an important determinant of tumour behaviour, prognosis, and treatment response. Radiomics and deep learning have shown promise for tumour classification from multiparametric MRI (mp-MRI), but radiomics relies on handcrafted features, while most deep learning methods use whole-tumour representations or manually defined sub-regions, limiting scalable modelling of tumour heterogeneity. We propose a Heterogeneity-Aware Deep Learning Classification (HA-DLC) framework that explicitly models imaging-derived tumour sub-regions for lesion-type diagnosis and molecular-status prediction. HA-DLC consists of: (1) a Heterogeneous Sub-region Generation (HSG) module that produces initial pseudo-labelled sub-regions via unsupervised clustering, followed by Cross-Patient Sub-region Alignment (CPSA), which maps cluster-derived regions to a shared label space using soft assignments; and (2) a Dual-Stream Feature Extraction (DSFE) module that integrates local heterogeneity-aware features with global tumour representations. Given the initial clustering masks, CPSA, segmentation, feature extraction, and classification are jointly optimized end-to-end using soft-target segmentation and classification objectives. We evaluate HA-DLC on the LLD-MMRI2023 liver lesion dataset and the RSNA-ASNR-MICCAI 2021 Radiogenomic Brain Tumour dataset. HA-DLC consistently outperforms state-of-the-art radiomics and deep learning baselines, demonstrating the value of cross-patient sub-region alignment and dual-stream heterogeneity modelling for tumour classification from mp-MRI.

---


### 58. [Learning Where and What to Lift for Bi-planar X-ray-to-CT Reconstruction](https://arxiv.org/abs/2608.17255)

**<font color=#1a73e8>作者：</font>** Yifei Wu, Yicheng Wu, Qiang Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> X-ray imaging can be approximately modeled as the projection of an underlying volumetric attenuation field, with each measurement recording the accumulated attenuation along a corresponding ray path. Reconstructing a CT volume from only a few X-ray views is therefore severely ill-posed, as the projections collapse depth information and leave 3D locations of anatomical regions and their corresponding intensity distributions highly entangled and ambiguous. We observe that once the spatial organization of anatomical regions is established, estimating their CT intensities becomes substantially more tractable. Motivated by this, we propose LiftXR, an interleaved, geometry-guided framework that explicitly incorporates spatial layout recovery into CT reconstruction. Specifically, a layout lifter first generates a 3D anatomical layout from bi-planar X-rays, providing spatial guidance for an intensity renderer to reconstruct a CT volume. An anatomical parser then performs volumetric perception on the reconstruction, exploiting its spatially resolved boundary and intensity cues to recover a refined anatomical layout. This transition from projection-conditioned layout generation to reconstruction-conditioned anatomical perception allows the parsed layout to provide feedback for region-specific intensity calibration. Extensive experiments on two public datasets demonstrate that LiftXR consistently outperforms recent X-ray-to-CT reconstruction methods, establishing a new state of the art. Moreover, the reconstructed CT achieves superior performance in external downstream segmentation, indicating improved anatomical fidelity. Code will be released.

---


### 59. [ASI-Bench: At the Dawn of Artificial Superintelligence](https://arxiv.org/abs/2608.17271)

**<font color=#1a73e8>作者：</font>** Junwei Zhou, Zhen Sun, Binyu Li 等 42 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial superintelligence (ASI) requires AI to move beyond mastering existing knowledge toward exploring the unknown, creating new knowledge, and turning new ideas into verifiable results. However, the capabilities of today's AI systems are still largely built on learning, compressing, and applying existing human knowledge. Accordingly, existing benchmarks primarily test whether AI can produce correct answers based on learned knowledge, or whether it can complete tasks under extensive human guidance. We therefore introduce ASI-Bench, the first benchmark to jointly evaluate AI systems' capabilities of innovative exploration and autonomous scientific execution across general research domains, and the first to progressively withdraw human methodological guidance within the same research project to test how far AI can proceed on its own. Built by over 40 experts with the cost of 31,000+ human hours, ASI-Bench contains 60 project-level research tasks across 11 scientific domains and progressively reduces methodological guidance to test whether AI can independently select methods, conduct research, and produce verifiable results. All tasks undergo expert review, AI-assisted auditing, sandbox execution, and scorer validation. Across 18 state-of-the-art agent--model configurations, the average score drops from 50.91 with full methodological guidance to 29.10 with only the method specified and 26.62 when agents must determine the method themselves. This sharp decline shows that current systems remain heavily dependent on human guidance and are still far from autonomously conducting end-to-end, project-level scientific research. ASI-Bench is open to the world. We invite researchers and builders everywhere to contribute new tasks, challenge the limits of today's AI, and help accelerate humanity's collective path toward artificial superintelligence at this https URL.

---


### 60. [When Agents Act on Web3: An Attack-Surface Survey of MCP, Skills, and Tool Calling](https://arxiv.org/abs/2608.17275)

**<font color=#1a73e8>作者：</font>** Rabimba Karanjai, Yang Lu, Nour Diallo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly act rather than merely read: across the Model Context Protocol (MCP) ecosystem, the share of deployed tools that modify external state has risen from 27% to 65% of tool use. When agents exercise this authority on public blockchains through MCP, skills, and tool calling, the consequences of an attack are governed by the blockchain execution layer rather than by conventional software assumptions. This survey argues that four properties of that layer (irreversibility, signing authority, continuous autonomy, and sequence-level composition) qualitatively change the threat model, turning the recoverable failures of generic agent security into a standing, irreversible loss. We organize the fragmented MCP-security literature into an attack-surface taxonomy, then contribute a Web3 risk-mapping matrix that ties each attack class to its amplified impact, the responsible amplifiers, a representative mitigation, and the residual gap. We synthesize defenses, including emerging blockchain-based mechanisms, and find them improving but insufficient: measured protections stop fewer than 30% of attacks, and model-level safety refuses fewer than 3%. We close by positioning the work against adjacent surveys and deriving a research agenda from the matrix's open cells.

---


### 61. [DeAR: Decentralized Agentic Reasoning via Capability Grounding and Collaborative Thought Navigation](https://arxiv.org/abs/2608.17282)

**<font color=#1a73e8>作者：</font>** Xing Wei, Changmeng Zheng, XiaoYong Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing agentic reasoning systems typically rely on centralized protocols. This design introduces routing bottlenecks and static role allocations that often fail when handling complex multimodal queries. We propose DeAR (Decentralized Agentic Reasoning), a framework that shifts from central control to autonomous peer-to-peer collaboration. DeAR is built on three mechanisms: (1) decentralized capability grounding for query-dependent agent specialization, (2) thought map navigation for targeted peer interactions, and (3) topology update for adaptive error correction. Evaluations across 9 diverse multimodal reasoning and text-based QA benchmarks indicate that DeAR consistently outperforms recent baseline methods, validating that decentralized and adaptive collaboration among agents enhances accuracy in knowledge-intensive reasoning tasks. The source code will be available at https://open_upon_acceptance.

---


### 62. [UniQuery4R: Unified 4D Scene Reconstruction from a Single Query](https://arxiv.org/abs/2608.17283)

**<font color=#1a73e8>作者：</font>** Tiancheng Chen, Sheng Tang, Wenhua Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic 4D scenes requires jointly estimating correspondence, geometry, object motion, and camera motion. Existing feed-forward methods typically predict dense task-specific maps or independently process source-target pairs, leading to unnecessary computation for sparse queries and limited feature reuse across different frame pairs. We present UniQuery4R, a query-conditioned framework that encodes a multi-frame clip once and selects the source view, target view, and continuous source-image coordinate only at decoding time via source-to-target cross-attention. Each query jointly predicts target correspondence, target-time 3D position, and scene flow, along with source depth, while camera parameters are estimated per view. This design allows the encoded clip to be reused across arbitrary source-target selections and supports both sparse inference and dense reconstruction through batched queries, without learned temporal embeddings tied to a fixed clip length. We further introduce a direction-magnitude parameterization of scene flow with separate supervision for moving and static points. Among the evaluated methods, UniQuery4R achieves the best macro-average results on WorldTrack for both scene-flow estimation and dynamic-point reconstruction.

---


### 63. [Rethinking Irregular Time Series Forecasting from the Perspective of Basis Functions](https://arxiv.org/abs/2608.17284)

**<font color=#1a73e8>作者：</font>** Rongwen Li, Changjian Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregular time series forecasting is crucial in many domains, such as healthcare and meteorological observation. However, due to the inherent characteristics of irregular time series, including sparse observations and non-uniform sampling, accurately predicting future dynamics remains challenging. In light of these two characteristics, many existing methods aggregate irregular observations into fixed-dimensional estimated response coefficients through predefined basis functions and use these coefficients as sequence representations. Nevertheless, this modeling paradigm still suffers from two key limitations: (i) a potential non-vanishing asymptotic bias caused by ignoring the sampling density of timestamps; and (ii) the limited adaptability of predefined basis functions to diverse temporal patterns. In this study, we propose a Debiased Neural Basis-Function Network (DNBNet) to address these challenges. Its core is a debiased neural basis-function response mechanism, which corrects asymptotic bias through importance sampling while parameterizing basis functions with neural networks to adapt to diverse temporal patterns. In addition, considering the sparsity of irregular data, we design a novel multi-scale decomposition module based on average pooling, together with a mass-aware fusion mechanism, to obtain richer representations. Finally, a dual-branch decoder is employed for forecasting. Extensive experiments on multiple real-world datasets demonstrate the effectiveness of DNBNet and its strong generalizability across diverse irregular time series scenarios. Our code can be obtained at this https URL.

---


### 64. [B-Spline Embedded Structure Learning for 3D Tooth Segmentation](https://arxiv.org/abs/2608.17291)

**<font color=#1a73e8>作者：</font>** Xianghan Wei, Jianwen Lou, Zhiguo Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D tooth segmentation forms the cornerstone of digital dentistry, yet it remains a formidable challenge due to the inherent intricacy of real-world dentitions, such as crowding, misaligned teeth and high morphological similarity between adjacent teeth. To resolve this, we present B-Spline Embedded Structure Learning, a novel framework that distills the inherent sequential arrangement of teeth into a continuous structural constraint to regularize representation space. Our approach parameterizes the global dental topology by fitting a parametric B-spline trajectory to tooth centers, assigning each point a continuous structural embedding that forces the shared backbone to capture global arch organization. To fully exploit these embedded priors, we introduce a Structure-Aware Dynamic Classifier (SADC) to substitute rigid static templates with adaptive, case-calibrated decision boundaries. SADC regularizes dynamic prototype pooling via a localized Gaussian proximity gate and contextually co-evolves them through an attention block modeling spatial relations and bilateral symmetries across teeth. Extensive evaluations on the 3DTeethSeg22 benchmark demonstrate that our method establishes a new state-of-the-art accuracy with exceptional structural robustness and efficiency in computational overhead, markedly enhancing the model's capacity to handle complex dental configurations.

---


### 65. [Beyond MSE: Rethinking the Evaluation Metric and Benchmarking for Irregular Time Series Forecasting](https://arxiv.org/abs/2608.17293)

**<font color=#1a73e8>作者：</font>** Rongwen Li, Haixin Xie, Xiao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing research on irregular time-series forecasting has primarily focused on model design, while evaluation metrics remain insufficiently studied. Existing benchmarks typically use mean squared error (MSE) as the evaluation metric. We show that, in irregular forecasting, MSE is determined not only by the model prediction but also by the sample-specific timestamp sampling distributions, leading to a biased assessment of the models' continuous-time predictive performance. To address this issue, we propose the Continuous-time Squared Error (CSE), which employs importance weighting to eliminate the influence of the timestamp sampling distributions. We further theoretically prove that CSE's asymptotic estimation error with respect to continuous-time risk is no greater than that of MSE. Finally, we construct a systematic benchmark covering synthetic, semi-synthetic, and eight real-world datasets to validate the effectiveness of CSE and systematically evaluate models' continuous-time predictive performance. Experiments show that CSE can recover continuous-time risk more accurately than MSE, while relying solely on MSE may not fully reflect models' continuous-time predictive performance in real-world scenarios. Our code can be obtained at this https URL.

---


### 66. [SleuthTalk: Supporting Historical Photo Identification with Private Workspaces for Collective Sensemaking and Deliberation](https://arxiv.org/abs/2608.17297)

**<font color=#1a73e8>作者：</font>** Liling Yuan, Vikram Mohanty, Kurt Luther  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Identifying individuals in historical photographs is a critical task across fields such as history, journalism, genealogy, and archival research. While AI-based facial recognition can efficiently generate candidate matches, it often produces ambiguous results that require deeper analysis and contextual interpretation. Existing platforms lack robust support for collaborative deliberation, especially in uncertain or high-stakes cases. We present SleuthTalk, a private collaborative workspace integrated into Civil War Photo Sleuth, designed to scaffold structured comparison, discussion, and group decision-making. SleuthTalk enables users to curate custom shortlists, annotate facial features, and build consensus through structured feedback. In a mixed-methods evaluation with experienced historical photo researchers, SleuthTalk enhanced self-reported confidence, surfaced diverse perspectives, and supported transparent, reflective identifications.

---


### 67. [Scanline-Aware Animatable Gaussian Avatars from Rolling-Shutter Videos](https://arxiv.org/abs/2608.17314)

**<font color=#1a73e8>作者：</font>** Youxiang Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Animatable human avatars are routinely reconstructed from multi-view video under a silent assumption: that every pixel of a frame observes the same instant of the body's motion. Rolling-shutter (RS) sensors expose image rows sequentially, so within one frame the head and the feet of a moving person are separated by tens of milliseconds of articulated motion, and every scanline sees a different pose. Feeding such video to a state-of-the-art avatar bakes the distortion into the canonical representation, where it survives as shear and wobble under novel views and novel poses. Worse, every camera in a rig follows its own readout schedule, so the multi-view consistency that drives the reconstruction is violated even when the geometry is correct. We present RS-Avatar, which reconstructs a sharp, undistorted, animatable 3D Gaussian avatar directly from RS video. The formulation is minimal: a motion-aware avatar already renders the body at several sub-frame instants, and where a blur model averages those renderings, a rolling-shutter model composites them scanline by scanline. Changing that operator is the only modification required. On RS-ZJU, a benchmark we build from ZJU-MoCap, this improves novel-view synthesis over training as if the frames were instantaneous, on every subject. A motion-aware blur model built on the same sub-frame machinery does not transfer, and in fact falls below the shutter-oblivious baseline: the machinery is reusable, the operator is not.

---


### 68. [If, Then, Otherwise: Diagnosing Conditional Branching in Vision-Language Navigation](https://arxiv.org/abs/2608.17318)

**<font color=#1a73e8>作者：</font>** Seoyoung Lee, Neel P. Bhatt, Pranay Samineni 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language navigation agents are often evaluated on their ability to follow route-like instructions toward a fixed goal. Yet, real navigation instructions often depend on observed states of the environment: if a condition holds, then follow one path, otherwise take another. Such instructions require an agent to evaluate scene evidence, select the correct logical branch, and execute the corresponding navigation behavior. Existing evaluations provide limited control over conditional branch execution, making it difficult to determine whether agents fail because of perception, grounding, navigation, or logical decision-making. We introduce CondVLN, a scene-graph-grounded benchmark for diagnosing conditional branching in vision-language navigation. CondVLN programmatically generates instructions whose branch conditions are grounded in verifiable 3D scene-graph predicates, with controlled variation in branch depth, dependency chain length, spatial composition, evidence observability, and instruction horizon. CondVLN contains over 11,500 generated conditional instructions across AI2-THOR, Matterport3D, Gibson, and ReplicaCAD, and evaluates agents using standard VLN metrics and branch-specific diagnostics: Branch Selection Accuracy and Conditional Success Rate. Evaluating four state-of-the-art VLN agents (VLN-Zero, NaVid, NaVILA, and Open-Nav) shows that conditional branching exposes failures that are not captured by standard success rate or path length alone: agents can navigate plausibly while committing to a branch inconsistent with the observed scene condition. We also present a lightweight neurosymbolic branch-selection model that separates condition grounding from navigation execution, improving performance by 2x. CondVLN provides a reusable testbed for measuring whether embodied agents can not only follow instructions, but follow the right instruction under the right condition.

---


### 69. [What Tokens are Learned when Tokenization is Optimized Jointly with Language Modeling?](https://arxiv.org/abs/2608.17325)

**<font color=#1a73e8>作者：</font>** Saketh Reddy Vemula, Parameswari Krishnamurthy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenization is a fundamental component of language modeling pipelines. Despite its importance, it is often fixed, even though it significantly impacts model performance across languages. In this work, we analyze what tokens are learned when tokenization is jointly optimized with language modeling. We compare tokenizer-free approaches such as SSLMs and H-Nets with fixed tokenizers across 18 typologically and script-diverse languages. Our results show that joint optimization fundamentally alters token structure. SSLMs recover morphologically aligned and contextually efficient tokens, whereas H-Nets prioritize byte-level efficiency, producing longer tokens with very low overlap with standard subword vocabularies. We further show that tokenization behavior varies across language typologies. Agglutinative languages exhibit more dynamic segmentation patterns while learning. Through downstream evaluation, with pretrained-then-finetuned BERT models, we find that SSLM-based pretokenization consistently reduces language modeling perplexity and achieves competitive downstream performance despite distinct vocabularies. Overall, tokenizer-free approaches optimize for contextual and computational efficiency rather than strict morphological structure, resulting in fundamentally different yet effective vocabularies for downstream NLP.

---


### 70. [Learning latent progression states from spatial heterogeneity in uterine histopathology](https://arxiv.org/abs/2608.17337)

**<font color=#1a73e8>作者：</font>** Qiming He, Yan Liu, Shuang Ge 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tumor progression is accompanied by changes in architecture, morphology and microenvironmental organization, yet progression-associated heterogeneity is usually compressed into static diagnostic categories in histopathology. Here we present SpaTIE, a uterus-specific computational pathology framework that learns morphology-aware representations and organizes spatial histopathological heterogeneity into progression-associated tumor states. SpaTIE was developed using 10,426 uterine hematoxylin and eosin whole-slide images and evaluated in TCGA-UCEC and TCGA-UCS cohorts. The learned representations formed morphology manifolds, supported diagnostic, molecular and survival-related prediction tasks, and localized attention to informative tumor regions. Beyond supervised prediction, SpaTIE inferred tumor-state axes from cross-sectional morphology without temporal or molecular supervision. These morphology-derived states were spatially coherent and showed associations with clinicopathological variables and survival outcomes, while not simply recapitulating staging or diagnostic labels. Integrative multi-omics analyses linked the inferred states to DNA methylation, somatic copy-number variation, mutation, RNA-seq and RPPA profiles, highlighting molecular programs related to chromatin regulation, copy-number-associated structural variation, receptor tyrosine kinase signaling, cell adhesion, extracellular-matrix remodeling and metabolic adaptation. Progression-guided virtual perturbation further prioritized molecular features coupled to the morphology-derived state organization. Together, these findings suggest that uterine histopathology contains recoverable progression-associated tumor-state information and establish SpaTIE as a framework for connecting spatial morphology with multi-omics-informed tumor-state discovery.

---


### 71. [Tight Bounds for Data-driven Multiple Hyper-parameter Tuning with Structured Loss Function](https://arxiv.org/abs/2608.17343)

**<font color=#1a73e8>作者：</font>** Anh Tuan Nguyen, Viet Anh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven algorithm design frames hyperparameter tuning as a statistical learning problem, but establishing generalization guarantees remains challenging due to the implicit, non-smooth dependence of model performance on hyperparameters. Existing multi-dimensional bounds under piecewise-polynomial assumptions remain theoretically loose and lack comprehensive lower bounds. We resolve this by establishing tight pseudo-dimension bounds for multi-dimensional data-driven tuning. First, we refine the learning-theoretic upper bound using real algebraic geometry; by analyzing invariant connected sign cells during block elimination rather than isolated sign vectors, we avoid topological over-counting to derive strictly sharper sample complexities. Second, we present a multi-regime lower-bound framework that disentangles combinatorial and algebraic capacities. By constructing shattered problem instances across distinct regimes, we prove our upper bounds are tightly saturated. Finally, we extend our topological framework to accommodate general bi-level validation-loss tuning and broader semi-algebraic applications.

---


### 72. [Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning](https://arxiv.org/abs/2608.17347)

**<font color=#1a73e8>作者：</font>** Hoda Yamani, Yuning Xing, Koen van Rijnsoever 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repetition is a fundamental mechanism in human learning, where revisiting successful experiences strengthens memory, consolidates skills, and improves future performance. Motivated by this biological principle, we introduce Instant Episode Repetition (IER), a simple and novel mechanism that improves sample efficiency by immediately repeating action sequences from successful episodes during environment interaction. Unlike conventional approaches such as Experience Replay and Self-Imitation Learning (SIL), which passively reuse past experience during training updates, IER directly influences the data collection process. Upon identifying a high-reward episode, the agent repeats its action sequence for a fixed number of subsequent episodes, reinforcing valuable behaviors through renewed interaction with the environment. We integrate IER into state-of-the-art SAC and TD3 algorithms and evaluate its effectiveness on continuous-control benchmarks, including MuJoCo, the DeepMind Control Suite, and a real-world dynamic object translation task with a robotic manipulator. Experimental results demonstrate that this simple mechanism improves learning performance over standard and self-imitation-based baselines.

---


### 73. [Primitive-Driven Compositional Forensic Visual Prompting for Open-World Face Anti-Spoofing](https://arxiv.org/abs/2608.17351)

**<font color=#1a73e8>作者：</font>** Fangling Jiang, Qi Li, Bing Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world face anti-spoofing must address both covariate and semantic shifts: source and target domains differ in imaging conditions, while target domains contain diverse attack types absent from training. Existing prompt-based approaches often express spoofing through category semantics or language guidance, which is effective for modeling high-level concepts but is less suited to explicitly capturing the evolving fine-grained and spatially heterogeneous forensic evidence of unseen attacks. Motivated by the hypothesis that many unseen attacks can be characterized by new combinations of recurring visual cues, we propose a compositional forensic visual prompt learning framework that operates entirely in the visual feature this http URL on a frozen ViT-based vision foundation model, the framework employs patch-aware attention to refine a shared set of learnable micro-forensic primitives into localized forensic evidence units derived from image patches. Class-specific global contextual prompts then provide input-dependent routing weights that adaptively select and compose these primitives into compositional forensic visual prompts for real/spoof discrimination. The primitives are not assigned predefined semantic meanings; instead, their specialization and reuse emerge from shared parameterization and joint optimization across this http URL experiments on nine open-world protocols demonstrate state-of-the-art performance, strong cross-domain generalization, and robust adaptation to unseen attacks.

---


### 74. [Cognitive Graph Intelligence for Adaptive and Robust DDoS Attack Detection in Next Generation Networks](https://arxiv.org/abs/2608.17352)

**<font color=#1a73e8>作者：</font>** Mohammad Arif Hossain, Yeahia Sarker, Md Jafrin Hossain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distributed Denial-of-Service (DDoS) attacks threaten network availability, requiring a cognitive detection process that senses traffic, infers intent, and supports an adaptive response under severe class imbalance and non-stationary conditions. This paper proposes a Graph-based Generative Adversarial Network (GraphGAN) that serves as the cognitive detection engine for this task. GraphGAN captures the relational structure among traffic flows while addressing imbalance through adversarial generation of synthetic samples. Sequential flows are converted into $k$-nearest neighbor graphs using sliding windows to preserve feature-similarity and temporal dependencies among flows. The generator learns the distribution of DDoS attacks to synthesize realistic minority samples, while a Graph Convolutional Network (GCN)-based discriminator distinguishes real from synthetic graph data. A separate GCN classifier, trained on the balanced dataset, performs the final detection decision. Evaluations on four benchmark datasets show that GraphGAN achieves superior accuracy, precision, and recall compared to state-of-the-art approaches, particularly in data-scarce scenarios. By integrating temporal graph construction, adversarial augmentation, and GCN classification, GraphGAN effectively models coordinated attack behaviors and mitigates class imbalance, providing a robust and topology-aware solution for intrusion detection in data-constrained environments.

---


### 75. [Trusted Workflow Relays:Cross-Tenant Email Abuse and Composable Red Team Initial-Access Primitives in Multi-Tenant Clouds](https://arxiv.org/abs/2608.17361)

**<font color=#1a73e8>作者：</font>** Priyank Nigam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud applications routinely send notifications through provider-operated mail identities, which improves deliverability but separates the actor who supplies notification parameters from the service principal that originates the message. In three responsibly disclosed and remediated cross-tenant notification workflows, an authenticated actor could reach recipients across tenant boundaries and, to varying degrees, control content that a trusted provider service delivered. In the first, backend requests bypassed a UI length limit, raw HTML and CSS survived into the delivered message, attacker links rendered, and CSS could hide service-controlled text; iframes and non-web URI schemes were rejected. The second combined missing recipient-tenant validation with attacker-controlled subject and HTML fields. The third, an approval application, added weak access control, sequential object identifiers, missing action authorization, and incomplete token validation, composing notification abuse with authorization failures.
The pattern is analogous to a classical unauthenticated SMTP open relay, but the failure has moved up the stack: the actor is authenticated and the provider is the legitimate sender, yet application-layer authorization still fails to constrain who may cause it to send what to whom. We define a trusted workflow relay as a delivered, service-authentic message for which the application-level send-authorization predicate is false. We give a test matrix for notification pipelines, map the primitive to MITRE ATT&CK techniques for attachment-free phishing, and link it to device-code phishing (RFC 8628). SPF, DKIM, and DMARC can authenticate a message yet cannot establish that an application-level send was authorized. We conclude with controls for tenant binding, typed templates, object-level authorization, token audience validation, and identity telemetry.

---


### 76. [Continuity-Driven Representation Learning for Industrial Defect Detection](https://arxiv.org/abs/2608.17362)

**<font color=#1a73e8>作者：</font>** Minjong Kim, Hyun Jun Kim, Jeongrae Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial defect detection differs from natural-image object detection because inspection images are captured under controlled conditions and contain large normal-dominant regions with repetitive structures. Defects therefore appear as localized disruptions of otherwise predictable patterns, while conventional detectors rely mainly on sparse bounding-box supervision, resulting in weakly constrained normal-region representations. We propose a continuity-driven representation regularization framework that exploits normal-dominant regions as dense auxiliary supervision. The framework introduces two detector-agnostic objectives: Multi-Continuity Loss, which combines 1D patch-sequence prediction and 2D masked spatial prediction, and Differencing Loss, which regularizes first-order feature variation and second-order curvature between neighboring patch embeddings. Both objectives are applied with box-derived region weighting to stabilize normal-region representations while preserving defect-related discontinuities.
Experiments on two real-world industrial datasets and the public NEU-DET benchmark, using six detector architectures including YOLO-family models, MambaYOLO, and DETR, demonstrate consistent improvements over native detector baselines. In the full-data setting, the proposed regularizers improve average mAP@0.5:0.95 by up to 3.49 percentage points on Industrial Metal, 5.38 percentage points on MEA, and 5.03 percentage points on NEU-DET. Under limited-data conditions, the gains become more pronounced, with Differencing Loss achieving improvements of up to 21.07 percentage points in mAP@0.5 and 8.23 percentage points in mAP@0.5:0.95 on NEU-DET using only 25% of the training data. These results suggest that continuity-driven regularization provides an effective prior for improving industrial defect detection, particularly when annotated data are scarce.

---


### 77. [CORAM: Coherent Orthogonal Rotation for Model Merging](https://arxiv.org/abs/2608.17366)

**<font color=#1a73e8>作者：</font>** Xinyi Sui, Ziran Liu, Nam Ling 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Merging finetuned models combines specialized capabilities without joint training or access to the original data. Most methods operate by linear arithmetic in Euclidean weight space, which cannot carry the geometry of the update. Orthogonal Model Merging (OrthoMerge) uses a single orthogonal transform for each weight matrix, but such a transform cannot change singular values. We propose CORAM, which partitions each target matrix into row slices, represents every expert slice by its singular value decomposition in the corresponding base-model SVD frame, and merges the task-specific factors on their corresponding manifolds. Because manifold averaging contracts the merged update, CORAM applies an amplification coefficient $\lambda=\kappa\hat{c}$. The scale c_hat is estimated from the expert and merged update norms and is approximately $\sqrt{N}$ for $N$ experts with comparable update magnitudes. The restoration strength kappa is selected from the dispersion of expert updates without evaluating candidate merged models. This rule remains within 0.72 points of the best swept value on all evaluated suites. CORAM also includes spread slicing to distribute highly updated rows across slices and a residual pathway for non-target layers. Across four suites covering three model families, 3B to 9B scales, and language and vision-language experts, CORAM improves over OrthoMerge by 0.25 to 1.35 points and matches or exceeds the strongest weight-space baselines.

---


### 78. [Pathology Transport: Optimal-Transport Explanations for Clinical Data, and When Their Heatmaps (Fail to) Localize Disease](https://arxiv.org/abs/2608.17370)

**<font color=#1a73e8>作者：</font>** Lalit Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models promise a route to explainable clinical AI: rather than probe a classifier, model the distributions of healthy and diseased patients and read explanations off the geometry between them. We build such a system - an optimal-transport rectified flow trained between two clinical distributions - and use it to ask a pointed question the field too rarely tests: do the resulting explanation heatmaps actually localize disease? On tabular tumour biomarkers (Breast Cancer Wisconsin) a single flow yields per-patient counterfactuals, an unsupervised malignancy score (AUROC 0.91; 0.93 +/- 0.01 across five seeds), and a label-free attribution that agrees with a supervised classifier (r ~ 0.5) - a compact, honest interpretability engine, though it never out-predicts logistic regression. Moving to chest X-rays, we show the transport heatmap is a population-level signal, not a localiser; a reconstruction-based, identity-preserving variant does localize synthetic lesions (pointing game 0.52), yet on real RSNA radiologist boxes it collapses to chance while only supervised Grad-CAM stays above it. The central result is a synthetic-to-real gap: label-free heatmaps that look compelling on planted lesions are not evidence of real localisation. We contribute a reusable optimal-transport recipe for generative explanations and a controlled benchmark for stress-testing whether they localize.

---


### 79. [Integrating Novelty and Surprise for Experience Prioritization and Exploration in Image-Based Reinforcement Learning](https://arxiv.org/abs/2608.17373)

**<font color=#1a73e8>作者：</font>** Hoda Yamani, Henry Williams, Bruce A. MacDonald  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sample efficiency is a central challenge in reinforcement learning (RL), particularly in image-based domains where agents must learn from high-dimensional visual inputs. Traditional sampling often relies on random or suboptimal experience selection, leading to redundant updates and slow learning. Improving efficiency requires mechanisms that prioritize informative experiences while also encouraging effective exploration. Prioritized Experience Replay (PER) addresses part of this challenge by reusing high-value transitions, while intrinsic rewards promote the exploration of novel or uncertain states. However, their integration has not been extensively studied. This paper introduces Novelty and Surprise Prioritized Experience Replay (NSPER), which uses novelty to capture underrepresented states and surprise to expose gaps in the agent's understanding of the environment. We further extend this with NSPER+R, integrating these signals as intrinsic rewards to jointly improve replay quality and exploration. Experiments on DeepMind Control Suite tasks show that NSPER and NSPER+R improve training efficiency and convergence speed compared to existing methods in image-based RL.

---


### 80. [GeoWeaver: Accurate Long-Sequence 3D Reconstruction via Hierarchical Geometric Assembly](https://arxiv.org/abs/2608.17389)

**<font color=#1a73e8>作者：</font>** Tinghao Jiang, Sheng Tang, Shengzhe Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-sequence 3D reconstruction from RGB videos requires both accurate local geometry and globally consistent camera motion. Feed-forward models provide strong depth and pose predictions, but their memory cost prevents joint inference over long sequences. Chunk-wise processing improves scalability, yet independently predicted chunks often exhibit scale drift, pose errors, and point-cloud misalignment. We present GeoWeaver, a unified framework comprising a Geometric Prior Model (GPM) and Test-Time Adaptation (TTA). The GPM predicts chunk-wise depth, confidence, and camera parameters as adjustable geometric priors. TTA then performs sequential initialization, global chunk-level Sim(3) alignment, and coarse-to-fine refinement of camera poses, affine depth corrections, and intrinsics. Dense correspondences provide adjacent, cross-chunk, and long-range constraints, while a robust CDF-style objective jointly optimizes weighted 2D reprojection and 3D consistency residuals. This design preserves local geometric accuracy while correcting accumulated pose, scale, depth, and calibration errors. Experiments across diverse long-sequence benchmarks demonstrate improved camera accuracy, global consistency, and point-cloud quality. Ablations verify the contribution of each adaptation stage, and applying the same TTA procedure to different geometric prior models consistently improves their trajectory estimates, demonstrating that GeoWeaver is not tied to a specific GPM.

---


### 81. [Noisy group neurons with synchronous resetting for high-performance spiking neural networks](https://arxiv.org/abs/2608.17394)

**<font color=#1a73e8>作者：</font>** Yajie Zhai, Yanmei Kang, Meng Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs), characterized by bio-inspired neuronal dynamics and event-driven communication, have attained significant progress in recent years. Nevertheless, training deep SNNs remains challenging due to spatiotemporal information loss and gradient mismatching. To simultaneously address these issues, we propose a noisy group neuron (NGN) model, which incorporates population-level synchronous resetting and neural stochasticity as fundamental computational mechanisms. We then develop the NGN method as a framework that combines the NGN model with backpropagation learning based on mean-field dynamics. We demonstrate the advantages of the NGN method through theoretical analysis and experimental validation on CIFAR-10, CIFAR-100, Tiny-ImageNet, DVS-Gesture, N-Caltech101, and CIFAR10-DVS. The proposed approach achieves an accuracy of 87.35% on CIFAR10-DVS within 10 inference time steps. These results support NGN as a practical approach to high-performance neuromorphic computing.

---


### 82. [To Remove or Not to Remove Clouds: A Comparative Analysis and Fusion of Raw SAR and Synthetic NDWI for Overcast Water Segmentation](https://arxiv.org/abs/2608.17398)

**<font color=#1a73e8>作者：</font>** Saleh Sakib Ahmed, Sara Nowreen, M. Sohel Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Persistent clouds blind optical satellites during floods. While Synthetic Aperture Radar (SAR) penetrates clouds, its raw data is noisy and lacks clear contrast. To mitigate this, recent studies utilize deep learning models to translate SAR into cloud-free synthetic optical imagery for downstream tasks like water body segmentation. However, because raw SAR is the original source for both of these operations, a critical methodological dilemma arises: during complete overcast should segmentation models process the raw SAR directly, or rely on a translated synthetic Normalized Difference Water Index (NDWI) proxy? This study resolves the debate by demonstrating that synthetic NDWI yields better results, as the translation process acts as a powerful filter against radar noise. This raises a natural second question: what if we utilize both? Building on our findings, we introduce a Combined Framework that integrates both raw SAR and synthetic NDWI into a unified model. By fusing the sharp physical boundaries of raw SAR with the high contrast of synthetic NDWI, this hybrid approach consistently outperforms all standalone methods.

---


### 83. [The Oracle of Chemnitz: An interactive art installation to reanimate old things in a garage featuring a rotary phone](https://arxiv.org/abs/2608.17407)

**<font color=#1a73e8>作者：</font>** Karola Köpferl, Albrecht Kurze  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Garages have a long tradition of tinkering, creativity and innovative change. School of Garage, a participatory artistic summer school project in Chemnitz, the European Capital of Culture 2025, took up this tradition and turned old Eastern Bloc garages into temporary ateliers for collaborative making and discussion. In our HackLab garage we conceptualized and created the Oracle of Chemnitz within one week. It gives a place filled with history back its stories. It is an interactive installation of artifacts from the past typically found in garages: an old typewriter, radio, desk, tires, mixer and a rotary-dial telephone. Each got a name, personality and story to tell. The phone rings when a visitor approaches. Once answered, it asks for name and month of birth before a story about a device is told, along with hints to other places in the city. Around 2,700 visitors interacted with the system over three months.

---


### 84. [Spectral Gradient Orthogonalization Improves Differentially Private Training at Scale](https://arxiv.org/abs/2608.17415)

**<font color=#1a73e8>作者：</font>** Sabari Shanmugam, Nick Barnes, Kerry Taylor  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Differentially private training adds isotropic Gaussian noise to clipped gradients, corrupting every singular direction equally. In vision models, where spatial correlation concentrates gradient energy into a low-rank subspace, most of this noise falls in directions that carry little signal. Spectral gradient orthogonalization via polar decomposition is introduced as a post-processing step that recovers directional signal from the noisy gradient's low-rank structure at zero additional privacy cost. A phase transition governs the utility of this approach: orthogonalization improves accuracy only when the per-direction spectral signal-to-noise ratio (SNR) suffices for singular vector recovery; in low-SNR regimes, the directional bias of the gradient is replaced by a nearly random orthogonal update, and the transformation is harmful. The recovery threshold is determined by the spectral gap of the gradient and is surpassed at large batch sizes. Empirically, the benefit scales with model capacity: spectral orthogonalization achieves a +20.9% improvement over DP-SGD on WRN-28-10 (B = 4096) and +14.9% on ResNet-18, while reducing inter-run variance by a factor of two to three. In the fine-tuning regime, spectral orthogonalization matches the stability of DP-Adam while maintaining a first-order memory footprint. Combining spectral with temporal denoising yields 50.3% on CIFAR-10 (epsilon = 4), the highest accuracy in any tested configuration. These gains are specific to moderate-to-high-SNR regimes such as large-batch training of higher-capacity models. Small-batch or low-SNR settings are better served by DP-SGD or temporal denoising.

---


### 85. [SPVC: Structured and Panoptic Video Fixing for Cross-Dataset Driving Scene Rendering](https://arxiv.org/abs/2608.17420)

**<font color=#1a73e8>作者：</font>** Gen Li, Shu Han, Yun Xi Qiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving scene reconstruction and rendering, especially with 3D Gaussian Splatting, has become an important component of autonomous driving simulation. However, rendered views often degrade under extrapolated ego trajectories and scene edits, producing blurry structures, temporal flicker, and foreground-background misalignment. Existing refinement methods are commonly designed for a specific setting, such as image-level novel-view repair or object-editing correction. In this paper, we introduce SPVC, a structured and panoptic video fixing framework for cross-dataset driving scene rendering. The name summarizes four design principles. (1) Structured fixing denotes the use of explicit spatial conditions, including camera pose, 3D bounding boxes, and HD maps, to guide the repair process and reduce uncontrolled hallucination. (2) Panoptic fixing refers to correcting both background rendering artifacts, such as distorted roads, buildings, and lanes, and foreground vehicle artifacts introduced by scene editing, such as inconsistent object appearance. (3) Video fixing means that the model operates on driving sequences rather than isolated frames, allowing temporal cues to be used during artifact correction. (4) Cross-dataset fixing means that a single shared network is trained and applied across multiple driving datasets, reducing the need for dataset-specific or scene-specific fixers. Concretely, we construct paired degraded-clean training data by simulating under-constrained 3DGS rendering and foreground vehicle insertion artifacts, and train a two-stage controllable video diffusion model that first addresses video-level appearance and then refines scene layout with structured controls.

---


### 86. [TEAMS: Text-prompted spatiotEmporal dual-heAd Mamba Snake](https://arxiv.org/abs/2608.17421)

**<font color=#1a73e8>作者：</font>** Ruicheng Zhang, Jianhui Lei, Kaiwen Shen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep snake is a promising family of instance segmentation methods that accurately predicts object-level contours, thereby overcoming common pixel-level misclassification issues such as mask cavities and jagged edges in semantic segmentation approaches. However, existing deep snake methods face challenges in handling complex morphological variations, accurately capturing fine-grained organ details, and correcting base detection errors. To mitigate these limitations, we propose a cohesive Text-prompted spatiotEmporal dual-heAd Mamba Snake (TEAMS), a novel vision-language Mamba snake framework with three key innovations: (1) A Spatiotemporal Snake Evolution Strategy (SSES) is introduced to tackle complex morphological variations by capturing bidirectional spatial dependencies along the snake contour and temporal dynamics across evolution steps in a state space model. (2) A Contour Morphology-Aware Mamba (CMAM) is proposed to quantify local contour morphologies to modulate the structured attention mask in the Mamba2 SSD dual form, which extends Mamba's capability to perceive the relative importance of its input sequence elements for better delineation of fine-grained organ details. (3) A Text-prompted Collaborative Dual-Head Snake (TCDHS) is designed to incorporate cues from textual prompts and transfer the evolved contour information to the base detection head, which enhances the deep snake workflow and mitigates wrong detections. Comprehensive evaluations on five datasets covering different organs and imaging modalities demonstrate that TEAMS outperforms existing semantic and deep snake segmentation methods (e.g., relative mDice/mBF improvements of 6.9%/9.1% in a spinal dataset), underscoring its potential as a reliable tool across diverse medical image segmentation scenarios.

---


### 87. [TF-CADE: Foreground-Concentrated Text-Video Alignment for Zero-Shot Temporal Action Detection](https://arxiv.org/abs/2608.17422)

**<font color=#1a73e8>作者：</font>** Yearang Lee, Ho-Joong Kim, Seong-Whan Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-Shot Temporal Action Detection (ZSTAD) aims to lo- calize and recognize action instances from unseen action categories in untrimmed videos. Although existing meth- ods have shown effectiveness by advancing architectural text-video alignment, they still struggle with capturing se- mantic distinctions between action classes, resulting in text- irrelevant predictions. To address this issue, we propose a Text-Foreground Concentrated Alignment for zero-shot temporal action DEtector (TF-CADE) that explicitly aligns textual information with action-relevant foreground regions. Specifically, we introduce Action Concentrate Aggregation (ACA), which extracts action concentrate scores to aggregate temporally informative video segments into a foreground- weighted video embedding. This foreground concentrated alignment enhances the semantic consistency between text and video features and improves inter-class discriminabil- ity. In addition, a Certainty-based Confidence Re-weighting (CCR) strategy refines per-snippet confidence scores by lever- aging foreground-aware similarity, effectively suppressing irrelevant action classes during inference. Extensive evalua- tions show that our TF-CADE not only achieves state-of-the- art performance under in-distribution settings but also excels in cross-dataset generalization to unseen action classes.

---


### 88. [GSToken: Geometry-Structured Gaussian Tokens for Compact 3D Medical Image Representation](https://arxiv.org/abs/2608.17425)

**<font color=#1a73e8>作者：</font>** Xiaoduo Li, Quan Gu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective segmentation of multi-modal MRI is central to improving neural network accuracy in brain tumor recognition. Existing methods typically compress 3D volumes into token sequences via fixed patch encoding or learned attention pooling (e.g., TokenLearner). However, these compression schemes discard explicit spatial shape information; the resulting tokens convey no notion of lesion morphology or spatial extent. Meanwhile, end-to-end evaluation entangles a tokenizer's information retention with the reconstruction capacity of the downstream decoder, and the lack of a unified capacity contract across methods makes performance differences difficult to attribute. In this paper, we introduce Gaussian tokens to multi-modal brain tumor segmentation for the first time: each token carries not only a semantic feature but also a learned 3D center, anisotropic scale, and orientation, endowing the representation with explicit geometric support at negligible parameter cost. We further propose a frozen-token utility evaluation protocol: the trained tokenizer is frozen, its output is cast into a fixed-capacity serialized contract, and a shared lightweight Transformer probe independently measures each tokenizer's retained information under strictly matched conditions. Multi-seed paired statistical testing shows that GSToken consistently and substantially outperforms capacity-matched adaptive baselines under frozen probing, with uniform advantages across all tumor sub-regions, surface, and distance metrics. These results demonstrate that explicitly encoding spatial geometry within tokens significantly improves the information density of volumetric representations, offering a new design principle for compact 3D medical image representation and downstream reading.

---


### 89. [Depth Enables Local Entropy: Quadratic Depth Dependence in Deep Variation-Norm ReLU Regression](https://arxiv.org/abs/2608.17434)

**<font color=#1a73e8>作者：</font>** Tao Jiang, Minbo Gao, Shaowei Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study Gaussian regression over the explicit vector-valued Parhi--Nowak deep-RBV^2 architecture with depth L, width w, layer-sum variation budget A, and output bound B. For this O(L w^2)-parameterized architecture, the known lower and upper bounds differ by one factor of depth. We construct a local packing showing that the quadratic depth dependence is intrinsic under an explicit sample-size-dependent radius condition. The packing has log-cardinality Omega(L^2 w^2 log w); its codewords lie in an O(lambda) L^2 ball and are pairwise Omega(lambda)-separated. The main ingredients are a bias-corrected bounded-coefficient approximation theorem and balanced amplification: multiplying a depth-D ReLU network by q can be implemented using one constant channel so that every coefficient grows by only q^(1/D). Translation to vector-valued RBV^2 blocks then has layer-sum cost O(D w^2 q^(1/D)). Gaussian Fano yields a radius-explicit lower bound governed by the output, testing, and representation scales. Under A=B=R, sigma proportional to R, and the stated radius condition, this gives minimax risk at least of order L^2 w^2 log(w) R^2/n. A pseudodimension-based finite-net upper bound gives O-tilde(L^2 w^2 R^2/n) for unbounded Gaussian responses. Thus the minimax risk has quadratic polynomial dependence on depth, up to logarithmic factors, and exhibits a transition to representation-limited behavior at smaller radius.

---


### 90. [General Semantic Knowledge Infusion for Spatio-Temporal Traffic Forecasting](https://arxiv.org/abs/2608.17440)

**<font color=#1a73e8>作者：</font>** Mattis thor Straten, Yannick Wolker, Steffen Strohm 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although Graph Neural Networks (GNNs) have made significant advances in spatio-temporal traffic forecasting, their performance is limited when they rely solely on sensor proximity or road-network topology. This paper presents a spatio-temporal prediction framework, developed to incorporate knowledge in various forms. This framework aims to improve sensor-level, contextual understanding of the environment. A general-purpose knowledge graph (e.g., Wikidata) is used to create semantic subgraphs around traffic sensors and generate knowledge graph embeddings that capture meaningful relationships, such as nearby points of interest, administrative hierarchies, and the functional roles of locations. These embeddings are then fused with conventional traffic sensor graphs to provide additional adjacency matrices informed by semantics. This allows GNNs to learn the semantic context beyond physical connectivity. This study differs from previous research in two key ways. Firstly, rather than proposing a novel GNN architecture, it demonstrates the general impact of external knowledge on prediction accuracy. Secondly, experiments with well-established traffic forecasting approaches show that external knowledge provides additional information that street network data alone cannot convey. The results show that integrating data from general-purpose knowledge graphs and sensor networks through data fusion can enhance the prediction accuracy of traffic forecasting models, and offers a potential pathway toward improved interpretability.

---


### 91. [FESC: Remodeling Long-Context Private Inference with Encrypted State-Space Models](https://arxiv.org/abs/2608.17442)

**<font color=#1a73e8>作者：</font>** Yufan Zhu, Chao Jin, Khin Mi Mi Aung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Processing long, sensitive documents with machine-learning models requires efficient, privacy-preserving long-context inference. Prior private inference systems optimize or distribute encrypted Transformer attention, but its quadratic token-pair work remains the bottleneck as sequence length grows. Selective state-space models (SSMs) offer linear-time recurrence, yet direct encrypted implementation incurs linear multiplicative depth, sequence-wide state residency, or dense FHE-MPC conversion. We present Factorized Encrypted Scan-Contract (FESC), a hybrid FHE-MPC system for private long-context selective SSM inference. Its factorized scan-contract keeps input-dependent transitions compact across conversion boundaries, composes them without dense expansion, streams state chunks on demand, and contracts outputs before conversion. We demonstrate interface compatibility of the scan-contract implementation across invariant and selective SSM architectures. For our Mamba-2 instantiation, we design GPU-optimized CKKS kernels for linear computations, MPC protocols for SiLU, softplus, exponential, and RMSNorm, with approximation-aware fine-tuning. To our knowledge, FESC is the first private long-document inference system to complete native end-to-end execution at $L \geq 1{,}024$ on a single GPU. At $L = 2{,}048$, a 12-layer Mamba-base model completes inference in 77.3 minutes on one A100 GPU with a peak memory footprint of 32.7 GB, while maintaining near-plaintext accuracy on the evaluated long-document tasks.

---


### 92. [NGS-Marker: Robust Native Watermarking for 3D Gaussian Splatting](https://arxiv.org/abs/2608.17447)

**<font color=#1a73e8>作者：</font>** Hao Qin, Yukai Sun, Luyuan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid development and adoption of 3D Gaussian Splatting (3DGS), the need for effective copyright protection has become increasingly critical. Existing watermarking techniques for 3DGS mainly focus on protecting rendered images via pre-trained decoders, leaving the underlying 3D Gaussian primitives vulnerable to misuse. In particular, they are ineffective against Partial Infringement, where an adversary extracts and reuses only a subset of Gaussians. In this paper, we propose NGS-Marker, a novel native watermarking framework for 3DGS. It integrates a jointly trained watermark injector and message decoder, and employs a gradientbased progressive injection strategy to ensure full-scene coverage. This enables robust ownership decoding from any local region. We further extend NGS-Marker with hybrid protection (combining native and indirect watermarks) and support for multimodal watermarking. Extensive experiments demonstrate that NGS-Marker effectively defends against partial infringement while offering practical flexibility for real-world deployment.

---


### 93. [From Substitution to Scaffolding: Breaking the Self-Reinforcing Harm Cycle of AI in Education (and Beyond)](https://arxiv.org/abs/2608.17451)

**<font color=#1a73e8>作者：</font>** Lucile Favero, Juan Antonio Pérez-Ortiz, Tanja Käser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is being adopted in educational settings faster than its consequences are understood. We argue that the central risk is misalignment: AI that eliminates human effort erodes the very capacities education is meant to build. We organize this risk into an integrative framework of four interrelated dimensions -cognition, agency, emotional well-being, and ethics- linked by a self-reinforcing cycle where cognitive offloading reduces effort, weakens agency, and compounds emotional and ethical harm. We ground the framework in the perspective of a small cohort of students: an exploratory analysis of 49 International Baccalaureate argumentative essays about the impact of AI reveals that learners perceive these risks, with $80\%$ of essays reporting that AI reliance reduces thinking. At the same time, the essays articulate a consistent vision of the AI the students want: systems that support rather than replace learning by withholding immediate answers, prompting recall, and encouraging reflection through questions instead of solutions. These desiderata closely align with established principles from the learning sciences. Building on these insights, we propose a single design principle, scaffold, do not substitute. We argue that this principle extends beyond education. It represents a broader challenge for the AI ecosystem: any system that mediates human thinking can either weaken human capabilities through substitution or strengthen them through scaffolding. We conclude by outlining a research agenda for developing AI systems that foster enduring human capacity, an imperative not only for learners but, ultimately, for democratic societies.

---


### 94. [Causal Local States: Scalable Simultaneous Causal Network Inference and Forecasting for Dynamical Systems](https://arxiv.org/abs/2608.17452)

**<font color=#1a73e8>作者：</font>** Jonas Braun, Fabian Fischbach, Daniel Köglmayr 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning methods predict many real-world systems with remarkable accuracy, but they are typically treated as black boxes that offer no insight into which interactions drive the dynamics. Causal discovery methods reconstruct the interaction network from observational data, but without regard to whether the inferred structure supports prediction. Existing approaches combining both tasks rely on a single global hyperparameter, such as a causal threshold or a fixed neighborhood size, which cannot recover the structure of heterogeneous systems. Here we introduce causal local states (CLS), a framework that simultaneously infers an approximate Granger-causal interaction network and forecasts the system dynamics. For each node independently, we select the smallest set of neighbors that allows a predictive model to forecast the node near-optimally, and the resulting neighborhoods are then combined for a forecast of the full system. On three benchmarks of increasing difficulty, we achieve reconstruction of the underlying networks with high fidelity and forecasts on par with a model that is supplied with the true network, providing a step toward explainable and scalable forecasting of complex systems.

---


### 95. [S$^3$AM: A Single-Stream SAM with Reliability-Calibrated Frequency Adapter for Multi-modal Salient Object Detection](https://arxiv.org/abs/2608.17475)

**<font color=#1a73e8>作者：</font>** Ruichao Hou, Boyue Xu, Tongwei Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models have recently advanced multi-modal salient object detection (MSOD) through parameter-efficient tuning and prompt learning. However, existing Segment Anything Model (SAM)-adapted MSOD methods often rely on dual-stream encoders or auxiliary prompt generators, leading to redundant computation. Although a single-stream alternative can reduce this cost, early fusion may also propagate noisy or misaligned auxiliary high-frequency cues through the backbone. In this paper, we propose a novel single-stream framework that integrates reliability-calibrated frequency adaptation into the adopted SAM backbone for MSOD. It avoids duplicated foundation backbones while explicitly controlling auxiliary frequency injection. Specifically, we design a mixture of frequency experts module, which uses the stationary wavelet transform to decompose each modality and aggregate cross-modal frequency information. We further introduce a reliability-calibrated frequency adapter with a dual-gate calibration mechanism, which selectively propagates the calibrated residual across transformer stages while jointly controlling its injection strength and cross-modal reliability. A hypernetwork-guided semantic-structural decoder then combines semantic mask features from the adopted backbone with Mamba-based structural detail recovery. Comprehensive experiments on RGB-D, RGB-T, and RGB-NIR salient object detection benchmarks validate that the proposed framework achieves competitive performance with only 12.20M trainable parameters, accounting for 5.4\% of the total parameters. The code will be available at this https URL.

---


### 96. [NeuroPath: Brain-Inspired Dual-Pathway Graph Convolutional Networks for Skeleton-Based Action Recognition](https://arxiv.org/abs/2608.17487)

**<font color=#1a73e8>作者：</font>** Kanglei Zhou, Ruizhi Cai, Hubert P. H. Shum 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based action recognition aims to recognize human actions from sequences of human joint coordinates. Most existing Spatial-Temporal Graph Convolutional Networks (STGCNs) have achieved promising results by modeling skeletal structures with implicit spatial-temporal representations. However, our empirical study reveals a clear performance imbalance across different skeletal modalities, indicating that implicitly coupling spatial and temporal information limits the full exploitation of complementary structural and motion cues. Inspired by the ventral and dorsal pathways in human perception, we propose Dual-Pathway Graph Convolutional Networks (NeuroPath), which adopt a dual-pathway architecture for separate yet collaborative modeling of spatial and temporal information. Specifically, transformation units first convert the input into pathway-specific skeletal representations, allowing each pathway to focus on complementary aspects of human motion. To further capture coordinated joint behaviors and their interrelationships, we introduce a group graph convolution block that dynamically identifies key body parts and models their spatial-temporal dependencies. In addition, inter-pathway dynamic fusion modules integrate complementary inter-modal information across pathways, facilitating higher-level semantic interpretation of actions. Extensive experiments on Kinetics Skeleton 400, NTU RGB+D 60, and NTU RGB+D 120 demonstrate consistent performance improvements, validating the effectiveness of dual-pathway spatial-temporal modeling for skeleton-based action recognition.

---


### 97. [Cross-Domain Joint DDoS Detection in Multi-Controller SDN via Confidence-Based Entropy Fusion](https://arxiv.org/abs/2608.17507)

**<font color=#1a73e8>作者：</font>** Zhaoyang Zhang, Shen Wang, Xiaofeng Tao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In multi-controller Software-Defined Networking (SDN), Distributed Denial-of-Service (DDoS) attacks exhibit a "dispersed source, concentrated target" pattern across domains, i.e., attack traffic originates from multiple edge-controller domains but converges on a victim in a single aggregation controller domain. While entropy-based DDoS detectors are effective in single-controller settings, their direct application in multi-controller SDN reveals a previously overlooked anomaly. Through systematic experiments, we identify an aggregation bias: during the post-attack transition phase, the aggregation controller continues to generate excessive false positives, while edge controllers have already returned to normal. We attribute this phenomenon to the coupled effects of OpenFlow statistics lag and unconstrained dynamic-threshold drift. To address this issue, we propose a cross-domain confidence-fusion framework that leverages lightweight edge-side messages to calibrate aggregation-controller decisions without sharing raw traffic data. The framework is non-intrusive, communication-efficient, and incrementally deployable. Experiments on a three-controller linear Mininet testbed with 24 hosts over 10 runs show that the method preserves edge-controller performance while reducing the aggregation false positive rate from 8.87% to 1.96% and increasing the F1 score from 89.04% to 96.89%.

---


### 98. [Looking Beyond the Scale: Do Surgical Skill Models Learn Transferable Representations Across Assessment Rubrics?](https://arxiv.org/abs/2608.17519)

**<font color=#1a73e8>作者：</font>** Hanna Hoffmann, Felix von Bechtolsheim, Stefanie Speidel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based surgical skill assessment has shown strong in-domain results, yet a fundamental question remains unasked: do these models learn transferable representations of surgical proficiency, or do they merely encode dataset-specific visual patterns?
This paper systematically analyzes what limits cross-domain skill transfer between the GOALS and OSATS assessment scales using the LASANA and JIGSAWS datasets. Each evaluated method serves a targeted diagnostic purpose: end-to-end training to test whether supervised skill learning transfers directly, Adaptive Sharpness-Aware Minimization (ASAM) to probe whether flatter loss landscapes improve generalization, and augmentation-based self-supervised and contrastive learning to assess whether domain-invariant pretraining decouples skill from visual context. Transfer is evaluated in both directions using a disjoint-participant held-out test set for JIGSAWS.
Results reveal an asymmetry: backbones pretrained on JIGSAWS achieve CCC values of 0.77 to 0.80 on LASANA, closely matching the end-to-end baseline, showing cross-rubric transfer is feasible when the target domain provides consistent supervision. Transfer to JIGSAWS fails across all methods, likely due to annotation inconsistencies. Control experiments with a Kinetics-pretrained backbone suggest task-specific heads carry the majority of the skill prediction burden, while the backbone need only provide adequate spatiotemporal features.
These findings offer a new perspective on vision-based skill assessment: the central question of whether skill representations transfer across scoring systems has not been previously investigated. Results indicate the visual component is dominant but not solely responsible for skill prediction; further work is needed to conclusively disentangle transferable skill features from those bound to a specific visual domain.

---


### 99. [Explainable AI-Powered Framework for Video-Based Skill Assessment in Cataract Surgery](https://arxiv.org/abs/2608.17522)

**<font color=#1a73e8>作者：</font>** Mohammad Javad Ahmadi, Hamid D. Taghirad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Persistent shortages in the surgical workforce and inherent limitations of traditional training methods highlight the necessity of automated, data-driven approaches in surgical education. This study addresses these challenges by introducing a novel, explainable AI-powered framework for automated skill assessment, specifically focusing on cataract surgery. We present the world's largest dataset of cataract surgery videos, comprising 2,000 recordings. Additionally, we propose an AI-powered analytical framework that employs advanced computer vision and signal-processing techniques to automatically evaluate surgical videos to derive objective, quantitative performance indicators that complement or potentially replace subjective scoring methods. A significant advantage of our framework over previous methods lies precisely in its explainability of outputs, elevating it beyond merely an opaque skill classification tool. Through experimental analysis of 83 cataract surgery videos, we demonstrate that the automatically computed metrics exhibit strong correlations with expert-based subjective evaluations, achieving up to 87% accuracy in surgical skill assessment. Each metric was individually examined, and expert surgeons provided subjective ratings using the newly introduced Capsulorhexis Skill Assessment System (CSAS). These subjective assessments were compared with ten objective motion-based metrics extracted through our framework. The results indicated a robust correlation between subjective ratings and automated indicators, underscoring the framework's capacity to accurately model surgical expertise.

---


### 100. [CryptDough: A Unified Analytics Engine for Secure Multiparty Computation](https://arxiv.org/abs/2608.17529)

**<font color=#1a73e8>作者：</font>** Muhammad Faisal, Alessandra Lanz, Sam Buxbaum 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present CryptDough, a unified analytics engine for secure multiparty computation (MPC). CryptDough enables multiple distrusting parties to jointly execute a data analysis pipeline on their private inputs and learn nothing beyond the result (e.g., aggregate statistics). Unlike existing MPC solutions that support a single threat model or workload type, CryptDough provides built-in support for cross-domain analytics (relational, time series, ML inference) under various threat models, all within the same system runtime.
CryptDough contributes (i) a hierarchical system design that facilitates modularity and extensibility through progressive lowering of abstractions, and (ii) the concept of virtual vectors that enable users to write single-threaded code across all layers of the software stack, while pushing the complexity of communication, parallelization, and memory management down to the execution engine. We show that CryptDough generalizes the functionality of state-of-the-art MPC systems and remains competitive on the analytics they support, often outperforming them by more than $2\times$.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-173](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
