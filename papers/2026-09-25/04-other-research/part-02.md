# 📦 其他研究 | 2026年09月25日

> 本类共 **240** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-240](./part-05.md)

---

### 51. [Diverse by Design: Architectural Constraints for Prototype-Based Interpretability](https://arxiv.org/abs/2609.27194)

**<font color=#1a73e8>作者：</font>** Xinmiao Lin, Matthew Wright  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prototype-based neural networks provide inherent interpretability through case-based reasoning, yet suffer from critical limitations: prototypes converge to redundant features, fail to capture diverse semantic parts, and lack quantitative interpretability assessment. We propose Diversity-Aware Prototype Learning (DAPL), which enforces prototype diversity through architectural constraints rather than explicit regularization. Our approach leverages multi-head self-attention with strict one-to-one attention-to-prototype mapping, ensuring each prototype specializes in distinct visual features. We further introduce foreground-aware training to focus prototypes on semantically meaningful regions and develop comprehensive evaluation metrics (Coverage and Diversity) for quantitative interpretability assessment. Experiments on CUB-200-2011 demonstrate substantial improvements: DAPL with foreground-aware training achieves 81.69\% accuracy with 0.596 Coverage and 0.427 Diversity, providing the best overall balance across all evaluated prototype-based methods. Code is available at this https URL.

---


### 52. [A Systematic Benchmark of Explainable Methods for Temporal Attribution in Sequential Recommendation Systems](https://arxiv.org/abs/2609.27201)

**<font color=#1a73e8>作者：</font>** Akash Pandey, Kanisha Shah, Addrish Roy 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential RecSys are central to modern personalization, exploiting user's historical interaction sequences to drive next-step decisions. Deep learning models, particularly CNN and Transformer-based architectures, have proven highly effective at capturing temporal dependencies in these histories. For transparency and trust, understanding which past interactions drive a given recommendation is increasingly important --- both for developers auditing model behavior and for users seeking a rationale. However, the non-linearities that give these models their predictive power also render them black boxes, making it difficult to attribute decisions to specific interactions. While gradient-based, perturbation-based, and attention-based explainability methods exist, a systematic benchmark of their faithfulness for sequential recommendation is missing. We address this gap by introducing a dual-model masking metric in which one model supplies per-timestep attribution scores and a separately trained, masking-robust probe measures the resulting change in predicted probability. Using this metric, we benchmark ten XAI methods across CNN, Transformer, SASRec, and BERT4Rec backbones on KuaiRand and MovieLens, complemented by analyses of temporal attribution patterns, item popularity confounding, and robustness to input corruption. Our key findings are: (1) gradient-based methods, particularly GradientSHAP and Integrated Gradients, yield the most faithful and robust attributions; (2) raw attention weights are unreliable, but gradient-weighted attention restores faithfulness on shorter sequences, with degradation on longer horizons as softmax attention probabilities converge toward uniform importance scores, diminishing the method's ability to identify informative interactions; and (3) temporal attribution patterns in faithful methods reflect genuine task structure rather than recency or popularity bias.

---


### 53. [Reliable Federated TinyML Deployment for IoT Security](https://arxiv.org/abs/2609.27202)

**<font color=#1a73e8>作者：</font>** Younsoo Park, Seokhyoen Bae, Shasi Kumar Ramachandran Prabhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing deployment of Internet of Things (IoT) devices has increased the need for privacy-preserving intrusion detection systems that operate directly on resource-constrained hardware. Federated Learning enables collaborative model training without sharing raw data, but conventional federated models are often too large and unstable for deployment on microcontroller-class devices. TinyML techniques enable compact neural networks but are typically designed for inference-only workloads.
This work investigates combining Federated Learning with TinyML-based model compression for intrusion detection in IoT environments. We evaluate compression strategies including knowledge distillation, structured pruning, and quantization within a federated training pipeline. Preliminary results show that training stability plays a critical role in federated TinyML systems. In particular, server-coordinated cosine learning-rate scheduling improves Attack Recall from 46.7% to 93.85% while enabling substantial model compression and efficient edge deployment. These findings provide insights for designing lightweight and privacy preserving intrusion detection systems for IoT devices.

---


### 54. [XLOG: A CUDA-Native Engine for Neurosymbolic Integration](https://arxiv.org/abs/2609.27203)

**<font color=#1a73e8>作者：</font>** Levi Dubrovin, Nikita Pospelov, Kirill Sabitov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> xlog is a CUDA-native logic programming engine integrating neural perception with deterministic Datalog, probabilistic inference, and epistemic world views through a typed frontend and provider-owned CUDA runtime. Its reasoning modes share device data planes, but their execution boundaries differ: ordinary Datalog and exact inference are host-orchestrated, while certified resident recursive and Monte Carlo sampled cores record zero tracked host-device transfers before a bounded terminal receipt. The probabilistic path supports end-to-end gradients through GPU knowledge compilation from provenance to CNF to Decision-DNNF, exact weighted model counting, and backward gradients. A final smoothed circuit is certified against its source formula before caching or evaluation. Circuit caching yields a 2.74x MNIST-addition training speedup; a worst-case-optimal join subsystem yields a 27.96x geometric-mean gain over xlog's binary-join baseline. MNIST-addition accuracy matches Scallop's (0.9561 versus 0.9468), but no per-epoch speed claim is made because baseline epoch time varies with CPU quota. In five hub-skewed triangle-counting cases, the Souffle-to-fused-xlog execution-time ratio rises from 0.88x at 150k edges, where Souffle is faster, to 5.54x at 1.2M; fused peak device allocations are 85-1,033 MB versus 3,287-44,979 MB for the materializing arm. Exact inference is correctness-equivalent to but slower than ProbLog2. On a public video benchmark, a proximity predicate trained only through symbolic credit replaces hand-set geometry at unchanged held-out accuracy; within Event-Calculus rule search it fails ten-fold cross-validation and does not transfer on a leak-free split. On a maritime corpus, weighted clauses beat crisp selection by 0.065 F1, with the result reproduced by one chronological training pass.

---


### 55. [Benchmarking Active Spot Selection for Cost-Efficient Spatial Transcriptomics](https://arxiv.org/abs/2609.27208)

**<font color=#1a73e8>作者：</font>** Zheyu Zhu, Junchao Zhu, Fengbei Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) measures gene expression in tissue context, but dense capture grids can be costly and may repeatedly sample morphologically similar regions. Most active learning strategies were developed for categorical labels and independent samples. We conduct a retrospective pool-based benchmark of active learning versus uniform Random sampling for ST, where expression vectors are high-dimensional and continuous and candidates are spatially correlated. Using two fully profiled public ST cohorts, we mask candidate expression vectors and simulate multi-round selection with uncertainty-based Monte Carlo dropout (MC-dropout) and temporal output discrepancy (TOD), and diversity-based CoreSet and TypiClust-inspired selection. We compare 160 completed configurations at 5%, 10%, 30%, and 50% of the fold-wide training spot pool under patient-level cross-validation, with a separate full-label reference. Within each budget, strategies share the selection schedule, morphology-to-expression predictor, and optimization protocol. We assess mean per-gene within-slide Pearson correlation coefficient (PCC), expression-cluster agreement, and Moran's I fidelity. On HER2-positive breast cancer, pooled mean PCC differences from Random across the four active strategies were -0.0176, -0.0117, +0.0056, and +0.0057 at 5%, 10%, 30%, and 50%, respectively. On cutaneous squamous cell carcinoma (cSCC), three strategies were below Random at 5%, and all four were below Random at 10%. On HER2-positive breast cancer, CoreSet and MC-dropout had lower PCC but higher expression-cluster agreement than Random at the two smallest budgets; this pattern did not reproduce on cSCC. Under the reported fixed training horizons, the evaluated active strategies do not consistently improve on Random at small budgets, and rankings depend on the evaluation measure.

---


### 56. [Scalable Subgraph Sampling via Resistance Curvature](https://arxiv.org/abs/2609.27209)

**<font color=#1a73e8>作者：</font>** Chaoqun Fei, Tinglve Zhou, Tianyong Hao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subgraph sampling reduces the training cost of large-scale graph neural networks, but sampling criteria may overlook the geometric roles of edges. We propose a resistance-curvature-guided sampling framework built on ERC-LG, a curvature approximation method for large-scale graphs. ERC-LG combines Johnson-Lindenstrauss projections with regularized multi-GPU batched conjugate gradient solvers, avoiding explicit Laplacian pseudoinverse computation and full embedding storage. The resulting curvature informs node- and edge-sampling probabilities for constructing GNN training subgraphs. Experiments show numerical agreement with pseudoinverse-based curvature and reduced runtime compared with CG-only computation. ERC-LG-based sampling variants achieve the highest mean accuracy on six of seven real-world datasets in downstream node classification.

---


### 57. [Learning Spectral Allocation: A Fractional Diffusion Framework for Adaptive Volumetric Segmentation](https://arxiv.org/abs/2609.27217)

**<font color=#1a73e8>作者：</font>** Yi-Hui Shen, Tie-Qiang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address adaptive computation in 3D medical image segmentation: instead of designing another backbone, we ask how much spectral mixing each network stage needs and let optimization answer. We derive FHEAT, a two-parameter operator family, from the discrete cosine transform (DCT) solution of a fractional heat equation. A fractional order alpha and a diffusion strength D govern the operator, and at D=0 it is exactly the identity. Reparametrized by the semigroup time tau = D*alpha, same-resolution instances compose exactly, so any distribution of diffusion across same-resolution stages amounts to a single Sobolev-type regularizer of learned strength. This identity limit lets the optimizer of each layer, not the designer, decide whether global mixing is needed and how sharp it should be. We instantiate FHEAT in a lightweight U-shaped architecture (Light-UNETR) paired with a Kolmogorov-Arnold mixer (KAN3D) with adaptive rational activations, yielding FHEAT-Seg. At 5% to 20% label rates on three public benchmarks, training produces gradient-driven spectral sparsification: seven of the eight stage-level operators drive D to zero, and the survivor saturates at the sharpest low-pass (alpha ~ 0.9) in the decoder layer feeding the semi-supervised attention map. The retired layers become exact identity shortcuts at inference, cutting FLOPs from 4.29G to 0.90G (a 79% drop) at 0.975M parameters. Under a standard semi-supervised protocol, FHEAT-Seg reaches Dice scores of 90.47% (left atrium), 78.79% (Pancreas-CT), and 81.90% (BraTS 2019), ahead of five semi-supervised methods and the Light-UNETR baseline. The large variant also surpasses Light-UNETR-L under full supervision (Dice 93.09%, 85.11%, and 87.19%) with 2.851M parameters and 55.75G FLOPs. These results suggest that the allocation of spectral computation is a learnable property of optimization dynamics, not a manual design commitment.

---


### 58. [Tail-Aware Geometry Learning for Conformal Ellipsoids](https://arxiv.org/abs/2609.27221)

**<font color=#1a73e8>作者：</font>** Xiang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies multivariate conformal prediction (CP), a distribution-free uncertainty quantification framework with finite-sample coverage guarantees. The efficiency of multivariate prediction sets hinges critically on the residual geometry encoded by the nonconformity score, while existing minimum-volume methods rely on quantile thresholds that ignore tail residual severity and implicitly bind geometry learning to coverage level. We propose a tail-aware geometry learning framework for conformal ellipsoids that decouples tail sensitivity in geometry learning from the final coverage guarantee. Using a two-split design, we learn the metric matrix via volume minimization under a CVaR constraint on an estimation split, then apply standard conformal calibration on a held-out calibration split. The resulting problem is convex and admits a bounded-reweighting interpretation that prioritizes high-residual samples. Moreover, we theoretically characterize the trade-off between ellipsoidal volume and tail severity. Experimental results demonstrate the effectiveness of the proposed method.

---


### 59. [Surgical Kinematics from Monocular Video with Learned Articulated Motion Constraints](https://arxiv.org/abs/2609.27227)

**<font color=#1a73e8>作者：</font>** Mehmet Kerem Turkcan, Soham Samal, Zoran Kostic  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective assessment of robotic surgery uses instrument kinematics, which must be reconstructed when only video is available. We introduce a kinematic reconstruction network for estimating instrument position, orientation and jaw angle from monocular video. Our visual representation combines global attention pooling of frozen DINOv3 features with local pooling at instrument landmarks from fine-tuned SAM 3.1 masks. Our shared Transformer encoder and temporal convolutional heads integrate this representation with mask geometry, monocular depth and visual state estimates from arm-specific multilayer regression networks. Our position branch predicts displacement magnitude and direction separately to preserve traveled distance. We fit trajectories to predicted state observations and motion increments by differentiable weighted least squares, expressing quaternion observations relative to cumulative predicted rotations to obtain a quadratic orientation objective. We evaluate reconstruction across 2,802 Open-H episodes. Compared with LiveMAE on the main Open-H benchmark, our method reduces path-length mean absolute error from 0.45 to 0.34\,cm and increases temporal mean average precision for motion segmentation from 44.54\% to 54.44\%.

---


### 60. [CoBranchMR: Supporting Parallel Design and Conflict Resolution in Mixed Reality](https://arxiv.org/abs/2609.27235)

**<font color=#1a73e8>作者：</font>** Niloofar Sayadi, Kaiyuan Tang, Yunhao Xing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present CoBranchMR, a mixed reality (MR) system that enables distributed collaborators to work in parallel from different locations on the same digital representation of a physical object. CoBranchMR lets users branch an object into editable virtual copies, customize them independently, and then merge their work back into a shared object. When merging copies, the system displays potential conflicts on the object's surface and provides several resolution options. By adopting branch-and-merge workflows for embodied spatial collaboration, CoBranchMR introduces a new collaborative interaction model that supports parallel design, conflict resolution, and negotiation in remote creative work.

---


### 61. [Strip Convolution and Direction-Aware Exclusion Loss for Oriented Ship Detection](https://arxiv.org/abs/2609.27238)

**<font color=#1a73e8>作者：</font>** Bin Chen, Yuanyuan Liu, Peng Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Oriented ship detection in very high resolution (VHR) remote sensing imagery remains challenging due to elongated hull geometry and dense target distributions in complex port scenes. Existing methods typically address geometric representation and duplicate suppression separately. To jointly tackle these issues, we propose an oriented ship detector with two complementary components. The C3k2_Strip module employs orthogonal strip convolutions to better capture elongated hull structures, while the Class-Aware Direction-Aware Exclusion Loss (CA-DAEL) suppresses redundant predictions using class, direction, and confidence cues. Experiments on HRSC2016 and DIOR-R achieve 78.45% and 53.71% mAP50:95, respectively, with only 2.91M parameters. On HRSC2016, the proposed method improves mAP50:95 by 6.32 percentage points over the YOLOv11-OBB baseline, demonstrating its effectiveness for accurate oriented ship detection.

---


### 62. [Listening and Mirroring: The Effects of Verbal Attunement and Behavioral Mimicry on Social and Empathic Perceptions of Embodied AI Agents in VR](https://arxiv.org/abs/2609.27246)

**<font color=#1a73e8>作者：</font>** Nathalia Gomez, Haig Shamlian, Omar Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As embodied agents take on increasingly social and relational roles in VR, visual realism and embodiment alone may be insufficient; users must also perceive these agents as emotionally attuned, supportive, and humanlike. Prior work suggests that verbal attunement and nonverbal mimicry can each improve users' social evaluations of embodied agents. However, behavioral mimicry has largely been studied outside of real-time, conversational AI interactions, leaving limited understanding of how users respond when an agent simultaneously generates contextually responsive dialogue and adapts its nonverbal behavior during an immersive conversation. To address this gap, we developed an embodied AI counselor that combines conversational AI with real-time facial-expression and posture mimicry, while producing either verbally attuned or neutral responses. We evaluated the system in a 2 X 2 within-subjects study with 20 participants, manipulating verbal attunement and behavioral mimicry. Results showed that verbal attunement was the most reliable driver of perceived empathy. Behavioral mimicry showed a marginal relationship with perceived humanness, while greater mimicry exposure showed preliminary, exploratory positive associations with empathy, positivity, and humanness, particularly among female participants. Together, these findings show that multimodal synchrony is not a simple additive strategy for designing empathic conversational agents in VR and underscore the need to consider how verbal and nonverbal behaviors are combined during real-time interaction.

---


### 63. [Anti-Localization Uplink Communications in Satellite-Terrestrial Systems](https://arxiv.org/abs/2609.27258)

**<font color=#1a73e8>作者：</font>** Ranran Sun, Bin Yang, Yulong Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper investigates the anti-localization uplink communication in a satellite-terrestrial system, where a ground transmitter Alice communicates with a legitimate satellite receiver Bob in the presence of multiple cooperative adversarial satellites attempting to localize Alice with the time difference of arrival (TDOA) technique. Specifically, we propose a cooperative jamming-based scheme for such anti-localization communication,in which Alice exploits the superposition coding with power allocation to simultaneously transmit information/jamming signals for communication with Bob and for confusing signal detection/TDOA measurement at adversarial satellites, while Bob employs the combining vector technique to enhance the desired information signal and also suppress the jamming. We define a localization error probability (LEP) metric to jointly depict both the impacts of signal detection and TDOA measurement on localization performance, and then develop a theoretical framework for the LEP modeling under the proposed scheme. We further explore the joint optimal design of jamming coding and power for LEP maximization, subject to the constraints of AliceBob communication reliability and Alice's transmit power. An effective sample average approximation method is also provided to tackle this non-convex optimization problem. Finally, extensive numerical results are illustrated to validate our theoretical models and demonstrate how the cooperative jamming helps to provide an anti-localization guarantee while ensuring communication reliability

---


### 64. [GaussPDE: Graph-Based Partial Differential Equation-Driven Rendering for 3D Gaussian Splatting](https://arxiv.org/abs/2609.27264)

**<font color=#1a73e8>作者：</font>** Haoyuan Yue, Fengyuan Ye, Ziyin Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present GaussPDE, a framework that injects physically structured partial differential equation (PDE) dynamics into pretrained 3D Gaussian scenes without mesh extraction, voxelization, or retraining. Our key observation is that PDE rendering requires not only accurate appearance, but also a reliable discrete computational domain. We therefore first introduce camera-aware regularization during 3DGS reconstruction to suppress camera-near floaters and oversized primitives that would create unstable graph topology. We then construct an active Gaussian graph using covariance-aware distances and opacity, appearance, and boundary-aware conductance, enabling mass-weighted graph Laplacian PDE evolution directly over Gaussian primitives. The evolving scalar PDE state is coupled back to rendering by modifying the direct-current spherical harmonic color coefficients while preserving geometry, opacity, and view-dependent rendering behavior. Experiments on real and synthetic scenes show that GaussPDE produces stable, controllable, and spatially coherent dynamic visualizations, with reduced cross-boundary leakage compared with baselines.

---


### 65. [High Dynamic Range Video Reconstruction from Single-Exposure Raw Sequences](https://arxiv.org/abs/2609.27274)

**<font color=#1a73e8>作者：</font>** Tao Zhang, Peixian Su, Xingyu Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the limited dynamic range of conventional image sensors, captured low dynamic range (LDR) video often suffers from highlight clipping and shadow detail loss, making high-quality high dynamic range (HDR) reconstruction from single-exposure sequences highly challenging without alternating exposures or extra hardware. Alternating-exposure HDR methods sacrifice frame rate and struggle with motion alignment, making them impractical for real-world capture. To address this, we propose RawHDRV, an end-to-end framework for single-exposure Raw video HDR reconstruction, that fundamentally exploits the linear response and channel-specific characteristics of Bayer data. Specifically, it features a channel-decomposition temporal alignment and fusion strategy that processes Bayer channels separately to exploit their distinct exposure characteristics, together with exposure-aware weighted fusion. It further incorporates an exposure complementarity mask-guided restoration module that leverages inter-frame exposure redundancy to adaptively fuse reliable information and suppress saturation artifacts, and introduces a mask-guided color loss that combines normalized error constraints with gradient smoothing to enhance highlight recovery. Furthermore, we construct a large-scale mobile Raw-HDR video dataset with per-frame HDR annotations. Experiments show that our method achieves the state-of-the-art results in all metrics, demonstrating superior spatial quality and temporal stability under extreme exposure conditions. The code is available at this https URL.

---


### 66. [TimeEvo: Failure-Driven Self-Evolution of a Time Series Agent](https://arxiv.org/abs/2609.27277)

**<font color=#1a73e8>作者：</font>** Jie Yang, Yan Zheng, Jiarui Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series agents answer analytical questions by calling external tools, and which tools they carry is decided by people before the agent runs. However, we identify two failures in this setup. Human-Agent Tool Misalignment: a library of 21 expert-curated tools helps on some tasks and hurts on others, dropping anomaly accuracy under every backbone we test. Silent Harm: one round of generic self-revision changes 147 answers and breaks 56 of them, while the final score moves by less than a point. Both follow from the same gap: whether a tool helps is decided question by question at runtime, while tools are supplied in advance and judged by a single average. To address this, we propose TimeEvo, which clusters an agent's diagnosed failures into capability gaps, plans a measurement for each, synthesizes evidence-only tools that fill them, and admits the candidate library only through a paired admission gate. Experiments on ten time series QA tasks and three backbones show that TimeEvo, starting from an empty library, improves accuracy on every task and every backbone, and that a library grown on a cheap model still gains when it is installed into stronger ones. Code is available at this https URL.

---


### 67. [Graph Learning with Spectral Connectivity Priors for Scarce Data](https://arxiv.org/abs/2609.27278)

**<font color=#1a73e8>作者：</font>** Mingxiao Liu, Bahar Oveisgharan, Bingyan Zou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning a sparse graph from scarce data is practically important but challenging. Motivated by the desirable combination of local sparsity and strong global connectivity exhibited by expander-like graphs, we propose spectral connectivity-regularized graph learning (SCoGL), a framework that incorporates a family of Laplacian spectral priors to explicitly promote global connectivity. Specifically, SCoGL augments a combinatorial-Laplacian-constrained graphical lasso (GLASSO) objective over a target adjacency matrix $\mathbf{W}$ with a general connectivity prior computed from Laplacian eigenvalues. We derive gradients for several representative connectivity priors and develop a projected gradient descent (PGD) algorithm with Armijo backtracking to efficiently optimize $\mathbf{W}$. Experiments show that the proposed SCoGL variants improve graph recovery and enhance downstream tasks such as graph signal denoising when signal observations are scarce.

---


### 68. [PotARCin: Multi-Dimensional Evaluation of Skill Acquisition in Abstract Reasoning Tasks](https://arxiv.org/abs/2609.27288)

**<font color=#1a73e8>作者：</font>** Claas Beger, Ryan Yi, Melanie Mitchell  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Abstraction and Reasoning Corpus (ARC) has become a prominent benchmark for evaluating general abstract reasoning and fluid intelligence in AI models. Yet standard ARC evaluation considers only a single capability: producing the correct output grid for a test input. We argue that this narrow format fails to evaluate the diversity of abilities that genuine abstract skill acquisition should enable. We introduce PotARCin, a benchmark that extends ARC by assessing understanding of a task's underlying abstract rule across five dimensions: Definition, Classification, Constrained Generation, Editing, and Inversion. PotARCin employs programmatic methods to generate new task instances and transform given inputs for a given ARC task, enabling dynamic generative sampling beyond fixed input-output pairs. Across five state-of-the-art models evaluated on the ARC-AGI-1 training set, we observe a 25-52 percentage-point performance gap between standard ARC evaluation and evaluation on PotARCin, and find that multi-dimensional evaluation reorders models that standard accuracy ranks alike. We further investigate effects of generative sampling, difficulty of corruption types, and questions of self-consistency, showing that models frequently contradict their own formalized rule even where they have stated it correctly. We also introduce P-ARC, a held-out hand-crafted test set, on which models achieve 1-8% accuracy across all five dimensions, underscoring the importance of more holistic evaluations of abstract reasoning capabilities.

---


### 69. [Sparse-Observation Atmospheric Thermal Forecasting with Physics-Informed Neural Networks for Climate-Aware Digital Twins](https://arxiv.org/abs/2609.27290)

**<font color=#1a73e8>作者：</font>** Tannaz Goodarzvand Chegini, Elyas Shivanian, Behzad Karimi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Short-horizon forecasts of atmospheric temperature are needed to support climate-aware digital-twin systems, but such forecasts must be produced where thermal observations are incomplete. This study evaluates a physics-informed neural network for potential-temperature forecasting, constrained by a pressure-coordinate thermodynamic advection-source equation and a diabatic-source closure fit from the preceding 12-hour period and frozen before future-time training. Using hourly ERA5 reanalysis at three pressure levels, the model is evaluated as a conditional hindcast at lead times of one, two and three hours against persistence, local-trend, and two matched neural-network baselines, one of which receives the same future meteorological forcing as the PINN, helping distinguish the physical constraint from access to future forcing. In an Oklahoma development case, mean RMSE improvement over the strongest baseline grew from 8.1\% at one hour to 23.8\% at three hours; under an observation-density sweep down to 5\% of candidate locations, this 3-hour advantage remained 14.6--16.9\%, with no evidence that lower density improves performance. Under a fixed protocol transferred to an Alabama heat event with three virtual-observation layouts, three-hour improvement ranged 19.7-24.4\% with consistent origin-level wins. A parallel Montana stress test, in which fixed pressure levels intersected complex terrain, produced a three-hour degradation of roughly 17.5\%, identifying a terrain-related applicability limit of the formulation. Together, these results indicate that the physics constraint's benefit grows with forecast horizon, persists under severe observation sparsity, and transfers across regions, but is bounded by the validity of a fixed vertical-coordinate representation over complex terrain, evidence relevant to physics-constrained components of climate-aware forecasting and digital-twin systems.

---


### 70. [NGN: Learning Neural Network Size as a Differentiable Count](https://arxiv.org/abs/2609.27291)

**<font color=#1a73e8>作者：</font>** Lixing Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network size is usually chosen before training, separating architecture selection from weight optimization. We introduce the Neurogenesis Network (NGN), a differentiable parameterization for learning how many ordered structural components a model should use. For each ordered component group, one learnable boundary selects an active prefix while the model parameters are trained. The boundary can grow from a compact initialization and can be deployed by discarding components beyond the learned boundary. Controlled experiments examine convergence of the learned boundary, the performance of deployed prefixes, and comparisons with fixed-size models and alternative approaches to learning capacity. We then apply the same mechanism to MLPs, convolutional and graph networks, Transformers, state-space models, LoRA, and adapters. Across these settings, deploying only the learned prefix usually changes performance little, and the selected architectures perform similarly to fixed models trained at the same size. These results show that structural capacity can be optimized directly as a count.

---


### 71. [Large Knowledge Model: From Papers to a Scientific Reasoning Landscape](https://arxiv.org/abs/2609.27297)

**<font color=#1a73e8>作者：</font>** Yuan Huang, Sihan Hu, Hongyu Gu 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accumulated scientific knowledge advances inquiry when prior findings help researchers choose new questions, design investigations, and interpret results. Realizing this value at scale requires access to the reasoning that connects research problems, scientific procedures, conclusions, and evidence. We introduce the Large Knowledge Model (LKM), a scientific knowledge infrastructure that transforms the literature into a shared, computationally accessible reasoning resource. LKM represents papers as source-grounded reasoning graphs, couples structural traversal with semantic retrieval over the same objects, and aligns related questions, claims, and reasoning chains across papers. This representation forms a Scientific Reasoning Landscape with three connected views: a Question Landscape that organizes research problems and open directions, a Workflow Landscape that exposes reusable scientific procedures, and an Evidence Landscape that connects conclusions to their support, disagreement, and conditions. The unified substrate supports reasoning-aware scientific search, evidence-grounded question answering, comparative evidence analysis, and research planning. Researchers and agents can retrieve relevant work through its scientific intent, synthesize answers with inspectable supporting arguments, and develop research plans informed by established workflows and unresolved evidence. We describe a corpus-scale system and evaluate scientific retrieval and knowledge-intensive question answering. With the answering model fixed, LKM retrieval improves accuracy by 9.30%, 4.20%, and 14.69% on ChemBench, PubMedQA, and SciBench, respectively. By connecting knowledge access to scientific reasoning and action, LKM provides a common foundation for discovering relevant research, reusing scientific knowledge, and coordinating cumulative inquiry across researchers, agents, and research cycles.

---


### 72. [SoK: You Find What You Seek: Rethinking Oracles, Guidance, and Input Generation in Hardware Fuzzing](https://arxiv.org/abs/2609.27300)

**<font color=#1a73e8>作者：</font>** G Abarajithan, Zhenghua Ma, Cristian Tirelli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware fuzzing is an active area in security verification research, yet its industrial adoption remains in its early stages. This SoK examines which lessons from software fuzzing carry over to hardware and where unique approaches are needed. By analyzing 52 fuzzers across RTL/IP, CPU, NoC, and SoC designs, we introduce an analytical framework that frames verification as a bounded search. This search is defined by its objective, oracle, guidance, input generation, target abstraction, and budget. Consequently, a campaign only uncovers failures it can effectively reach, recognize, and prioritize before exhausting its resources. We distinguish two roles for hardware fuzzing: (1) augmenting constrained-random verification (CRV) via feedback-guided coverage and (2) directed adversarial testing based on threat models and security specifications. Through our framework, we identify what each campaign can observe and generate, providing a basis for assessing the evidence behind reported results. Our analysis suggests that mainstream adoption of hardware fuzzing will require reusable interfaces, target-specific verification assets, reproducible evaluations, and transparent reporting of cost and user effort.

---


### 73. [Live Assistant: Learning Whether, When, and Whom to Assist in Real-World Live Social Streams](https://arxiv.org/abs/2609.27303)

**<font color=#1a73e8>作者：</font>** Shujian Gao, Jiamei Yan, Yuchen Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Livestreams are long-lasting interactive environments where audiovisual content, viewer activity, host behavior, and platform signals evolve together, creating assistance needs that emerge from the stream itself. We introduce \liveassistant, a framework for mixed-initiative, role-conditioned assistance that formulates livestream interaction as four coupled decisions: \textbf{whether to act, when to act, whom to address, and what to communicate}. At each 10-second interval, one autoregressive policy consumes native audio and video with synchronized comments, gifts, viewer dynamics, and room metadata, then selects \textsc{OBS}, \textsc{MEM}, or \textsc{ANS}. \textsc{OBS} remains silent, \textsc{MEM} records a private semantic update, and \textsc{ANS} specifies a recipient, task, and grounded message. To support this task, we build a trajectory engine that reconstructs real livestream sessions into structured causal supervision, yielding over 320 hours of optimization trajectories and a human-reviewed benchmark of 275 clips and 13,812 decision intervals. We train the policy with Marker-Aware Multiturn Supervised Fine-Tuning (MA-MSFT), which strengthens sparse structured decisions, followed by Streaming Multiturn GSPO (SM-GSPO), which optimizes self-generated trajectories with turn- and trajectory-level credit. On the held-out benchmark, \liveassistant reaches 71.14 state accuracy, 72.67 recipient accuracy, and 58.41 task accuracy, with consistent gains over representative streaming and general multimodal baselines. Together, the formulation, benchmark, and training framework establish livestream assistance as selective participation in a shared social stream.

---


### 74. [Discrete Diffusion Models via Evolving Variational Autoregressive Networks](https://arxiv.org/abs/2609.27306)

**<font color=#1a73e8>作者：</font>** Kewen Pan, Ying Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional score-based diffusion models learn scores without representing normalized densities, whereas tractable normalized models support both sampling and direct likelihood evaluation. A recent tensor-network approach provides such a representation but is largely restricted to low-dimensional lattices. Here we introduce a discrete diffusion model that parameterizes normalized probability distributions using variational autoregressive networks. Explicit Markov jump operators govern the forward noising and reverse denoising dynamics, extending discrete diffusion models with normalized distributions to spin systems on higher-dimensional lattices. We apply this framework to the two- and three-dimensional Ising models across ordered, critical, and disordered regimes, accurately computing thermodynamic quantities including free energy, energy, and magnetization. We further integrate the framework with Monte Carlo sampling, using adaptive diffusion steps to maintain high acceptance rates even at low temperatures while enhancing sample diversity. These results establish a neural-network framework for the discrete diffusion model with normalized probability distributions.

---


### 75. [Learn How to Act from Your Own Interactions: On-Policy Self-Distillation for GUI Agents](https://arxiv.org/abs/2609.27307)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Daiqing Wu, Huawen Shen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) agents enable the fulfillment of complex user instructions through multi-turn interactions with software environments, requiring step-wise reasoning and long-horizon memory to guide actions and retain task-relevant information, respectively. Recent on-policy self-distillation (OPSD) methods have achieved strong performance on GUI grounding, a foundational subtask for GUI agents, owing to dense token-level supervision from privilege-conditioned self-teachers. However, extending existing OPSD methods to multi-turn GUI agents is hindered by self-teachers' limited privilege-following ability and insufficient privileged guidance. In this paper, we introduce GUI-SD-v2, the next version of GUI-SD, which extends OPSD from GUI grounding to multi-turn GUI interaction and addresses key limitations through a two-stage training framework. Specifically, GUI-SD-v2 first strengthens privilege following by jointly optimizing rollouts with and without privileged guidance from the same GUI states. Furthermore, it selectively distills step-specific reasoning and memory guidance through a privilege-conditioned self-teacher, supporting action decisions and the retention of task-relevant information for subsequent interactions. Extensive experiments on two representative GUI agent benchmarks, AndroidWorld and MobileWorld, show that GUI-SD-v2 compares favorably with existing OPSD baselines while consistently outperforming the evaluated state-of-the-art methods in both Pass@1 and Pass@3 success rates. Code and training data will be publicly released.

---


### 76. [Multi-View Fusion for Encrypted C2 Detection: A Leakage-Controlled Measurement Study of Evaluation Pitfalls](https://arxiv.org/abs/2609.27311)

**<font color=#1a73e8>作者：</font>** Hoang-Huy Nguyen-Huu, Van-Tri Phan, Khuong Nguyen-An  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Command-and-control (C2) traffic increasingly hides within TLS, so defenders now apply machine learning to traffic metadata. Many studies assume that combining two metadata views, namely flow statistics and TLS handshake fingerprints, improves both accuracy and robustness. We tested this assumption on 17,577 TLS flows from 62 real Cobalt Strike captures. Our evaluation removes the data leakage that leads to overly optimistic reported scores. We report three findings that matter more than the fusion result itself. First, an incorrect preprocessing step increases the F1 score by 0.28. This step computes the frequency encoding across the entire dataset rather than within each cross-validation fold. The increase is about ten times larger than any real effect we measured. Second, both the labels and the behavioral features depend on the destination address. Because of this, the 17,577 flows form only 2,132 independent groups, and the positive rate of 55.1\%, which looks balanced, drops to 4.2\%. Therefore, class balance is just a result of how we analyze the data, specifically whether we count flows or endpoints, and not a real feature of the task. Third, 20 of the 62 captures (32\%) have no TLS flows to any known C2 address, so they contain only benign samples. We checked these captures directly and confirmed that this is a gap in the ground truth, not a labeling error. In this context, fusion beats the best single view by only 0.022 in F1. When an attacker forges both feature surfaces simultaneously, every model performs worse than a simple baseline that always predicts positive (F1 = 0.711). For encrypted C2 detection, the evaluation design is not a preliminary step. It \emph{is} the main result.

---


### 77. [Breaking Weather-Content Coupling: Type-Severity Guided Progressive Disentanglement for All-in-One Infrared Restoration](https://arxiv.org/abs/2609.27317)

**<font color=#1a73e8>作者：</font>** Xinyao Wang, Lijun He, Zhihan Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared (IR) imaging is crucial for autonomous driving, remote sensing, and other perception tasks. However, adverse weather may introduce fake structural responses that are entangled with real thermal structures. Existing IR restoration methods are typically designed for a single degradation type or directly reconstruct from degradation-entangled representations. Consequently, they struggle to distinguish intrinsic thermal structures from weather-induced fake responses and to accommodate spatially varying degradation severity, leading to artifacts or the over-suppression of weak but meaningful thermal responses. To address these issues, we propose TSGPD-IR, a type-severity guided progressive disentanglement network for all-in-one infrared restoration that factorizes restoration guidance into task-level weather semantics and region-level degradation severity. Specifically, a Weather and Semantic Co-Guided Multi-Level Prompt Generation Module combines global weather semantics with stage-wise local features to generate adaptive prompts that progressively suppress degradation-induced responses while preserving intrinsic thermal structures. To complement global weather semantics with spatial restoration control, a Proxy-Supervised Regional Degradation Estimator derives severity supervision without manual annotations and predicts spatially varying degradation priors. Guided by these cues, a Multi-Source Collaborative Expert Selection Strategy uses a shared branch to preserve weather-invariant thermal structures and hierarchical routing to select weather-specific expert pools and severity-compatible regional experts. This design progressively separates degradation interference from genuine thermal content and enables region-adaptive restoration, reducing both residual artifacts and over-suppression.

---


### 78. [Stable Geometry with Divergent Task Evidence for Efficient Long-Horizon Agent Compression](https://arxiv.org/abs/2609.27332)

**<font color=#1a73e8>作者：</font>** Mingxuan Wang, Fei Luo, Bo Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long horizon agents accumulate growing interaction histories that increase context and inference costs. We find that geometric redundancy alone is an insufficient criterion for safe compression. Although agent histories exhibit strong low dimensional structure, similar global geometry can preserve very different amounts of task evidence. At identical retained block counts, evidence aware selection raises next action Top 3 retention from 0.31 to 0.69, while centroid similarity remains 0.98. Controlled replacement further shows that action related information can be substantially altered while global geometric measures remain nearly unchanged. Motivated by this gap between geometry and evidence, we introduce Geometry Guided Evidence Preserving Memory (GEM), a training free compressor that protects task and execution evidence before using geometric residuals to complete coverage. GEM reduces mean combined token usage from 2.69M to 2.11M per task, a 21.4% reduction, while maintaining comparable task reward. Our results show that efficient agent history compression should optimize for preserved task evidence rather than geometric coverage alone.

---


### 79. [Beyond Mean Foils: Auditing Worst-Foil Specificity in Frozen CLIP Region Explanations](https://arxiv.org/abs/2609.27356)

**<font color=#1a73e8>作者：</font>** Kaixin Liu, Zhipeng Ye, Feng Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A region can overlap a target object yet contribute more to another class. We test regions selected by Cluster-based Concept Importance (CCI) in frozen CLIP. Across COCO and VOC with two checkpoints, 41.08-64.78% of regions that pass overlap and mean-contrast checks fail against the strongest competing class. Removing competitors annotated in the image leaves 39.69-63.64% failing. We then test all eight candidate regions per image. An alternative passes the test for 6.25-7.84% of failures on COCO and 27.40-31.15% on VOC. Requiring it to preserve the original target-score drop within $\epsilon = 0.02$ reduces these rates to 0.16-0.98%. Available regions and target-drop tolerance constrain repair; relaxing the tolerance increases repair opportunities.

---


### 80. [SAGEGAN: Style-Based Anomaly Detection with Gaussian Embeddings using Generative Adversarial Networks](https://arxiv.org/abs/2609.27357)

**<font color=#1a73e8>作者：</font>** Thesath Wijayasiri, Kar Wai Fok, Vrizlynn L. L. Thing  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware evolves faster than rule-based and signature-driven detection pipelines. This paper presents SAGEGAN, a benign-only trained malware anomaly detection framework that converts portable executable files into compact three-channel images and models benign structure through style-conditioned adversarial reconstruction. The representation combines Hilbert-mapped byte values, benign-referenced byte-transition surprise, and entropy deviation from benign software. The model encodes each image into a layer-wise style tensor aligned with a seven-stage modulated generator, rather than a single latent bottleneck. A Gaussian style prior, moment-based prior alignment, and latent consistency are used to reduce mismatch between encoded benign styles and the generator's sampled manifold. For interpretation, a deterministic encoder pathway maps each executable to a fixed style tensor, enabling repeatable layer-wise family distance, gradient sensitivity, principal component, and class-behaviour analyses. On a self-collected portable executable corpus containing malware from 214 families, the Gaussian variant achieves 89.76% area under the receiver operating characteristic curve and 88.19% balanced accuracy, while the genome-style variant reaches 88.03% and 84.09%, respectively. Without refitting model weights, benign reference statistics, or decision thresholds, the same checkpoints are evaluated on DIKE, Microsoft BIG 2015, and Lester malware subsets. The results suggest that layer-wise style modelling supports both anomaly ranking and structured post hoc analysis of how malware families depart from the benign manifold.

---


### 81. [Anomaly-Free Self-Optimization via AUC Bounds](https://arxiv.org/abs/2609.27362)

**<font color=#1a73e8>作者：</font>** Kevin Wilkinghoff, Zheng-Hua Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomalies are rare, and anomalous data are often unavailable during development, making it difficult to determine which anomaly detection models and configurations will generalize to unseen anomalies. Recent approaches address this challenge by generating pseudo-anomalies and using bounds on the achievable area under the ROC curve (AUC) to select the optimal configuration from a finite set of candidates. Instead, we use the AUC bound as a differentiable, anomaly-free objective for directly optimizing continuous parameters of anomaly detection systems. We demonstrate this framework by optimizing ensemble weights and introducing a learnable score-rescaling mechanism that adapts pseudo-anomaly scores, enabling optimization beyond a predefined candidate set. Experiments across multiple datasets and embedding models show that AUC-bound optimization achieves significant performance gains over conventional model selection and prior development-set-based parameter selection. The results further show that direct optimization is less sensitive to the choice of pseudo-anomaly construction.

---


### 82. [Anchor and Perturb: Lazy Agent Remediation by Exploration Injection](https://arxiv.org/abs/2609.27365)

**<font color=#1a73e8>作者：</font>** Chengxi Zhong, Yongzhe Chang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Anchor and Perturb (AnP) is a lightweight framework that resolves multi-agent coordination failures by decoupling exploratory variance injection from recurrent manifold stability. Existing remediation strategies predominantly alter mixing network architectures or enforce simultaneous exploration across the collective, which inevitably precipitates severe temporal-difference penalties in non-monotonic reward spaces. Specifically, AnP isolates underperforming lazy agents and injects an asymmetric exploratory pulse into targeted coordinates whilst anchoring converged teammates to nominal greedy exploitation. Empirical telemetry benchmarks demonstrate that AnP successfully rescues collapsed joint policies (recovering from a 5% evaluation win rate nadir back to 85%) and facilitates escape from suboptimal coordination plateaus, sustaining peak win rates of 90% without requiring structural network modifications.

---


### 83. [Geometry-Conditioned Visual Place Recognition in Natural Environments](https://arxiv.org/abs/2609.27370)

**<font color=#1a73e8>作者：</font>** Walter Nedov, Saimunur Rahman, Kavindie Katuwandeniya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Place Recognition (VPR) in natural environments remains challenging due to repetitive vegetation, sparse distinctive landmarks, and substantial appearance and viewpoint variation across traversals. While visual observations of the same place can change considerably, their underlying spatial structure is often more persistent. We exploit this complementary geometric consistency through Depth-Aware Distillation (DAD), which conditions the token representations of a pretrained Vision Foundation Model (VFM) on geometry inferred by a Geometric Foundation Model (GFM), without any depth sensor. Rather than treating geometry as an additional input modality, DAD projects image-aligned depth into the VFM token space and selectively modulates visual representations through channel-wise geometric conditioning. A two-stage teacher-guided learning strategy first anchors the geometry-conditioned representation to the pretrained appearance space, before refining it for place discrimination. Evaluated on the WildCross benchmark, DAD improves average inter-sequence Recall@1 from 61.41% to 66.37% and Recall@5 from 65.86% to 72.49% over a matched appearance-only baseline, with the largest gains under reverse traversal and long-term appearance variation. These results show that GFM-derived geometry can provide a persistent structural prior for VPR when visual appearance becomes unreliable.

---


### 84. [ASAP: Visual Analytics for Identifying and Analyzing Image Patterns in AI-generated Images](https://arxiv.org/abs/2609.27371)

**<font color=#1a73e8>作者：</font>** Jinbin Huang, Yuki Ueno, Chen Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative image models can produce highly realistic images, raising concerns about potential misuse in creating deceptive content. Current deepfake approaches face several challenges, including limited generalizability, lack of interpretability, and poor actionability. To help address these, we present ASAP, an interactive visualization system designed to empower users in the analysis and summarization of deceptive patterns in AI-generated images. ASAP introduces a novel CLIP-adapted image encoder that generates interpretable representations, enabling the extraction of influential pixel regions via calculated masks. This approach facilitates the identification of key deceptive features through influence measurement techniques. These backend techniques are integrated into a visual analytics dashboard that allows users to quantify and analyze authenticity-indicative patterns in image collections containing both authentic and AI-generated images. This approach also supports the comparative analysis of various generative models, including GANs and diffusion models. We demonstrate ASAP's efficacy through a user study and two application scenarios using established fake image detection benchmarks, showcasing its ability to effectively extract and quantify deceptive patterns.

---


### 85. [Neither Silence nor Overlap Is Failure: Intent-Conditioned Evaluation of Turn-Taking in Full-Duplex Spoken Dialogue Models](https://arxiv.org/abs/2609.27372)

**<font color=#1a73e8>作者：</font>** Kian Shamsaie, Iman Modarressi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmarks for full-duplex spoken dialogue models score turn-taking with binary fixed-window rules that reward immediate response or silence by completeness of the prior turn. We argue that the appropriateness of a response offset, whether delayed silence or anticipatory overlap, is conditional on the speaker's latent intent, identifiable only from that speaker's behavior. We introduce TACT, a benchmark of 9,728 episodes and 73.2 hours from five dyadic corpora; each episode carries dialogue history, a per-speaker memory profile, and an annotator-derived posterior over six intent classes. Scoring replaces binary windows with a strictly proper threshold-weighted continuous ranked probability score whose weights are intent-conditioned timing kernels fitted to human floor-transfer-offset distributions, proving boundedness, consistency, and binary reduction. Across eleven systems the best model reaches 0.47 against a human topline of 0.86, is nearly invariant to speaker profiles, and TACT agrees with human judgments at Spearman 0.81 versus 0.46 for binary metrics.

---


### 86. [Cross-Lingual Legal QA for Vietnamese Labour Law: Retrieval, Translation, and Verifier-Guided Correction](https://arxiv.org/abs/2609.27376)

**<font color=#1a73e8>作者：</font>** Nguyen Minh Chi, Mo El-Haj, Nguyen Ha Thanh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual legal question answering must retrieve statutes across languages while preventing unsupported legal claims. We introduce a bilingual evaluation suite of 231 Vietnamese--English question--answer pairs from Vietnamese labour law. Of these, 75 are additionally annotated for five challenging legal reasoning phenomena. We evaluate a verifier-guided pipeline that decomposes answers into claims, checks citation reachability and entailment, and corrects citation failures and contradictions. We also introduce six automatic diagnostics for faithfulness to retrieved evidence, covering citations, modality, exceptions, procedures, conclusions, and evidential support. Experiments show that learned-sparse retrieval performs poorly for English-to-Vietnamese retrieval (R@5~=~0.032), whereas dense retrieval reaches 0.358 and slightly outperforms hybrid retrieval. Translation placement has no statistically detectable effect on these automatic diagnostics in our controlled comparison and supporting sensitivity analyses. Verifier-guided correction improves citation preservation by $0.022$--$0.034$ at the system level but produces no reliable gains in the remaining dimensions. Human evaluation further shows that the automatic diagnostics do not fully align with human judgements of answer quality.

---


### 87. [MORSE: Multi-Context Ordering via Reverse Scoring for Evidence-Preserving Compression](https://arxiv.org/abs/2609.27380)

**<font color=#1a73e8>作者：</font>** Ke Wan, Yifan Wang, Liheng Lai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Likelihood-based context compression can account for cross-context redundancy through sequential scoring, but this makes compression outcomes sensitive to context order. We show that different permutations of the same context collection can produce markedly different evidence-retention outcomes under an unchanged compressor. We attribute this sensitivity to information preemption: earlier partially relevant contexts can absorb credit for shared information, suppressing the incremental score of later, stronger evidence carriers and increasing their risk of removal. Controlled pair-swap interventions directly support this mechanism by showing that evidence-first ordering substantially improves supporting-evidence survival. To address this problem, we introduce MORSE, a compression-aware method for evidence-preserving context ordering. MORSE applies a common reverse query-evidence principle to both individual contexts and compressed candidate outputs, using the former to construct an evidence-first anchor and the latter to guide compression-aware permutation selection. Across multi-hop QA benchmarks, compression procedures, budgets, and scoring models, MORSE consistently improves evidence preservation over static reverse ordering and compute-matched random search, with corresponding overall improvements in downstream QA. Our code is available at this https URL.

---


### 88. [AraGenre 2026: A Hierarchical Definition-Guided Arabic Genre Classification Shared Task](https://arxiv.org/abs/2609.27387)

**<font color=#1a73e8>作者：</font>** Mo El-Haj, Saad Ezzini, Shadi Abudalfa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AraGenre is a shared task on hierarchical, definition-guided Arabic genre classification, motivated by the limited availability of annotated data in Arabic and other low-resource languages. Systems assign each Arabic text segment both a broad communicative genre and a fine-grained specific genre. The released training and development sets contain limited, primarily synthetic and controlled examples, whereas the hidden final benchmark contains noisier naturally occurring text spanning Modern Standard Arabic, Classical Arabic, and multiple dialects. Participants received natural-language definitions for 74 previously unseen specific genres, creating a zero-shot label generalisation setting in which systems had to infer class semantics rather than memorise fixed label-feature associations. The task attracted 46 registrations and 373 submissions, with 17 teams completing the final evaluation. Thakaa ranked first with a Hierarchical Macro F1 of 0.7352, followed by HoangPhong (HP) with 0.7169 and NAMAA with 0.7013. The results show strong broad-genre recognition but a substantial gap in fine-grained classification under linguistic and domain variation.

---


### 89. [Active Learning for Biodiversity Monitoring: From Label Efficiency to Reliable Ecological Inference](https://arxiv.org/abs/2609.27409)

**<font color=#1a73e8>作者：</font>** Ben McEwen, Shiqi Zhang, Dan Stowell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Limited expert annotation capacity is a pervasive constraint in biodiversity monitoring. Passive acoustic recorders and camera traps generate data faster than experts can analyse them. Machine learning (ML) models can process these data at scale, but their reliability depends on the quality, quantity, and coverage of labelled samples, so expert time remains a constraint. Active learning (AL) eases this bottleneck by selecting, under a fixed annotation budget, the samples expected to improve a model most, and published evidence shows it can reduce the labels needed to reach a target performance. Monitoring programmes, however, face a broader question: how should a limited expert budget be divided so that model training, validation, and the ecological estimates built on model outputs all remain reliable? Because AL selects samples non-randomly, its labels are unsuitable for validation, calibration, or threshold selection, a tension rarely acknowledged. We synthesise AL research across acoustic and image modalities and identify gaps and opportunities. Most studies evaluate query strategies on pre-labelled benchmarks with simulated annotators; deployments in real monitoring workflows are rare and concentrate on birds and cetaceans. Bats, insects, amphibians, and fish are underrepresented, and multimodal applications remain largely unexplored. Evaluation centres on headline reductions in annotation effort, often without random-sampling baselines, per-class results, or calibration analysis, and rarely accounts for the labels required for validation. We provide a tutorial treatment of the AL loop that makes these budget decisions explicit, and a roadmap towards AL methods that support label-efficient training, validation, and trustworthy downstream ecological inference.

---


### 90. [When Labels Are Scarce: An Oscillatory State Space Model for Vibration Diagnosis](https://arxiv.org/abs/2609.27411)

**<font color=#1a73e8>作者：</font>** Mainak Mallick, Seung-Kyum Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine fault diagnosis from vibration requires learning from scarce labelled fault recordings while meeting the computational constraints of edge devices for local inference. We introduce DualRes, a compact oscillatory state-space model that combines two complementary spectral views of vibration, capturing rapid changes and fine frequency structure. Time-aligned views are processed by selective oscillatory memory, which learns how long to retain temporal patterns. The encoder contains 39,528 parameters. We evaluate supervised learning across six bearing datasets and a gearbox benchmark, with an additional gearbox pilot. Recording-level splits and explicit accounting of labelled duration distinguish data efficiency from repeated exposure to correlated samples. On the main gearbox benchmark, DualRes achieves state-of-the-art performance among the nine evaluated methods at six of seven label budgets. With about six labelled seconds per class, it improves macro-F1 by 16.1 percentage points over the next strongest comparator. On the same benchmark, DualRes achieves a 1.44-fold recording-level speedup and a 24.8-fold reduction in checkpoint storage relative to a selective state-space baseline under matched hardware and runtime conditions. Bearing results reveal task-dependent trade-offs. These findings support oscillatory memory as a compact approach to vibration diagnosis under limited labelled exposure.

---


### 91. [S2A:Semantic-to-Spatial Alignment for Alignment-Free RGB-T Salient Object Detection](https://arxiv.org/abs/2609.27413)

**<font color=#1a73e8>作者：</font>** Qiangqiang Zhou, Yang Luo, Yong Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alignment-free RGB-T salient object detection (RGB-T SOD) aims to identify salient objects from unregistered RGB and thermal image pairs without costly pre-alignment. However, spatial misalignment breaks pixel-wise correspondence and causes feature contamination during cross-modal fusion. To address this issue, we propose S2A, a semantic-to-spatial alignment framework for alignment-free RGB-T SOD. Specifically, a global-guided hierarchical fusion module (GGHF) first exploits global semantic guidance to suppress background interference and refine hierarchical intra-modal features. Subsequently, the alignment-free cross-modal channel attention module (AFCA) globally exchanges complementary semantic information through channel-wise interaction, effectively overcoming the interference caused by local spatial misalignments. Finally, a spatial deformable cross-attention module (SDCA) predicts adaptive sampling offsets to recover local cross-modal spatial correspondence. Through this semantic-to-spatial paradigm, S2A first enables reliable cross-modal semantic interaction and subsequently performs local spatial calibration, effectively reducing misalignment-induced feature contamination. Without bells and whistles, S2A achieves highly competitive performance on multiple public alignment-free RGB-T benchmarks, demonstrating its effectiveness in alleviating misalignment-induced feature contamination.

---


### 92. [Forced Yet Free: What Magicians' Forcing Reveals Beyond Intentional Binding](https://arxiv.org/abs/2609.27416)

**<font color=#1a73e8>作者：</font>** Koichi Toida  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In magicians' forcing, spectators may experience a choice as self-determined even when that choice has been externally directed. Research on the sense of agency has developed largely around action-outcome relations, most notably intentional binding; however, the problem of choice authorship (why a particular choice is experienced as originating from oneself) must be treated as distinct. This paper integrates research on agency and forcing by distinguishing the locus of intervention within the choice-action-outcome chain, self-attribution at the Decision, Action, and Outcome levels, and the processes by which feeling of agency and judgment of agency are constructed. On this basis, a distinction is drawn between intentional binding, which concerns the temporal/causal relation between action and outcome, and the different binding problem exposed by forcing: the relation between a choice and its author. This theoretical relation is termed authorship binding. Authorship binding does not denote a new implicit measure; rather, it refers to the constructive relation through which a choice whose formation has been directed by external factors can nevertheless be experienced as originating from the self. Forcing can sustain this relation not by eliminating agency, but by selectively preserving, substituting, and redistributing agency cues. XR, in which body-centred spatial relations can be manipulated, is further conceptualised as a medium for extending the forced-yet-free structure into space.

---


### 93. [Emergi-PersonaOS: A Persona Agent Operating System for Situational Adaptation and Controllable Evolution](https://arxiv.org/abs/2609.27417)

**<font color=#1a73e8>作者：</font>** Haoluan Fu, Keni Chen, Xinyu Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Symbiosis between humans and digital beings offers a vision for the future of human--machine interaction. In enduring human--machine relationships, personality provides a foundation for continuity of identity, individuality in interaction, and development through experience. We investigate this capacity through persona agents as computational implementations and introduce Emergi-PersonaOS, a psychology-grounded operating system for managing persona objects throughout their lifecycle. The system organizes dispositional traits, characteristic adaptations, and narrative identity into a three-layer persona representation, distinguishing relatively enduring persona beliefs from their activation in the current persona state. During situational adaptation, it integrates the current interlocutor, relationship, event, and retrieved memories to infer a persona state and generate actions and replies; during long-term development, it records experiences and outcomes, and develops and evaluates revision candidates through change attribution, meaning-making, and behavioral testing. Belief updates are managed through explicit review, traceable evidence and version records, and the ability to reject candidates, making persona evolution controllable. Using television-character dialogue as longitudinal material, we demonstrate long-horizon system operation and examine its principal mechanisms in a concrete implementation. This work provides a computational framework for persona agents to maintain individual continuity, produce situation-specific expression, and develop through experience over sustained interaction.

---


### 94. [RAMP: Reversing Adversarial Perturbations to Strengthen Clean-Label Backdoor Attacks against Malware Detectors](https://arxiv.org/abs/2609.27422)

**<font color=#1a73e8>作者：</font>** Jinwen Xin, Dongni Zhang, Chenyang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep learning-based malware detectors are commonly updated by fine-tuning on newly collected samples, but this practical update pipeline also creates an attack surface for training-time backdoor attacks. In realistic crowdsourced data collection, however, strict label vetting typically restricts attackers to the clean-label setting, in which poisoned samples must retain benign labels and functionality, making effective backdoor injection substantially harder. We present a new attack perspective based on feature-space manipulation: instead of relying solely on stronger trigger designs or selecting benign samples that are naturally similar to malware, we deliberately construct benign programs whose representations shift toward the malware region before trigger injection, thereby creating stronger feature-label conflicts during training. Based on this insight, we propose RAMP, an attack enhancement method that uses a genetic algorithm to optimize reversed adversarial perturbations under black-box access and then injects them through functionality-preserving binary manipulations. Extensive experiments show that RAMP substantially improves attack effectiveness over trigger-only baselines, with especially pronounced gains at low poisoning ratios, while maintaining accuracy on clean data. Moreover, RAMP can be combined with advanced trigger designs.

---


### 95. [Overlapping Visual Grouping Without Semantic Priors](https://arxiv.org/abs/2609.27423)

**<font color=#1a73e8>作者：</font>** Teemu Saukkio, Hashem Haghbayan, Juha Plosila  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most computer-vision systems organize visual input toward a predefined interpretation, such as semantic categories, prompted regions, learned object-like representations, or a single spatial partition. This work considers an earlier stage of visual organization: the formation of candidate perceptual units directly from sensor measurements before their identity, meaning, or task relevance is known. We introduce Domain Parent Grouping (DPG), a sensor-grounded grouping method in which complementary measurement relationships are represented in separate processing domains. Spatially connected groups formed within these domains are related through cross-domain overlap, yielding a non-exclusive grouping representation rather than a single mutually exclusive segmentation. This representation retains broader and more localized groups, as well as alternative grouping boundaries over the same image locations, simultaneously available. DPG also includes a native mechanism for reprocessing selected group content, in which input-relative measurement ranges allow the observational resolution to change while preserving previously formed groups. DPG is implemented using three domains representing locally contextualized luminance, direct chromatic relationships, and contextual chromatic relationships. Experiments on the BSDS500 dataset demonstrate the benefit of combining the three domains. The results further show that DPG forms measurement-supported groups corresponding to low-level image structure, and that these groups exhibit measurable correspondence with human-annotated regions and boundaries. This demonstrates that structured visual organization can emerge directly from relationships among sensor measurements.

---


### 96. [EVAGE: Autonomous MEV Generation and Adaptation via Multi-Agent Harness](https://arxiv.org/abs/2609.27424)

**<font color=#1a73e8>作者：</font>** Yan Wen, Zichun Cai, Iliya Mirzaei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Maximal Extractable Value (MEV) has evolved into a major economic force in blockchain ecosystems, yet its capture is dominated by experienced teams, and both strategy design and implementation rely on manual expert work that scales poorly across heterogeneous protocols and chains. We present EVAGE, the first fully autonomous multi-agent framework for end-to-end MEV strategy generation and adaptation. Equipped with three specialized operation modes, it automatically discovers novel MEV variants, adapts execution logic across disparate protocols, and ports strategies between chains, including Layer-1 and Layer-2 networks. To avoid inference latency on the critical MEV execution path, EVAGE generates and refines MEV bot code offline rather than making real-time decisions directly. Under the coordination of an orchestrator agent, three specialized subagents collectively implement and repair the full MEV bot workflow via closed-loop diagnostics, eliminating human intervention while producing validated and deterministic Proof-of-Concept implementations. We evaluate EVAGE on over 1.5M blocks from each of Ethereum, Base, and BNB Smart Chain (BSC). On Ethereum, EVAGE uncovers five novel MEV strategy variants, yielding a profit increase of 1.02$\times$ to 15.97$\times$. It also successfully adapts 11 MEV strategies from CPMM to both CLMM and Balancer V2 and ports strategies from Ethereum to Base and BSC, all with less than 60 dollars in LLM token costs.

---


### 97. [Extracting CNNs in the Unknown-Architecture and Feedback-Agnostic Setting](https://arxiv.org/abs/2609.27427)

**<font color=#1a73e8>作者：</font>** Jiashuo Liu, Ruijie Ma, Manman Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper studies the cryptanalytic extraction of convolutional neural networks (CNNs). Existing cryptanalytic extraction attacks on CNNs assume that the network architecture is known, and try to recover model this http URL this paper, we prove for the first time that the architecture assumption can be removed for CNNs with both max and average pooling. Our core finding is that the spatial geometry of the weight vectors recovered by existing parameter-recovery attacks naturally leaks the architecture. We formalize this geometry and establish its correspondence with the architectural knowledge of a convolutional layer: (1) The sparsity consistency with the convolution receptive field reveals the layer type, the kernel size, and the stride; (2) The numerical consistency with the kernel parameters reveals the padding mode and the output-channel number; (3) The structural consistency with the pooling operation reveals the pooling type, the window size, and the stride. Although the recovered vectors are obtained using different methods in the raw-output and hard label settings, their spatial geometry remains the same. Therefore, our architecture recovery is feedback-agnostic: combined with a parameter-recovery attack, it yields a complete cryptanalytic extraction framework that recovers both the architecture and the parameters in the black-box setting. Extensive experiments, including both layer-wise and end-to-end ones, on a wide range of CNNs demonstrate that simultaneously recovering the network architecture and the model parameters is practical.

---


### 98. [Stable Neural Decoding Across Sessions via Task-Conditioned Latent Alignment for Brain-Machine Interfaces](https://arxiv.org/abs/2609.27441)

**<font color=#1a73e8>作者：</font>** Canyang Zhao, Bolin Peng, J. Patrick Mayo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Achieving stable long-term neural decoding in invasive brain-machine interfaces (BMIs) remains challenging due to variations in recorded neural populations across sessions. Current latent alignment approaches may overlook task-dependent structure during cross-session adaptation. We propose Task-Conditioned Latent Alignment (TCLA), a framework that stabilizes neural decoding by learning a shared latent space. TCLA learns a low-dimensional source representation using neural reconstruction and continuous behavioral supervision. During target-session adaptation, the shared representation is fixed, while target neural activity is mapped into the source latent space by aligning source and target distributions separately for each task condition. We evaluated TCLA on seven nonhuman primate datasets spanning multiple tasks. In long-term cross-session evaluation, TCLA achieved a mean $R^2$ of $0.476\pm0.014$ with a negative $R^2$ failure rate of only 6.8\%. Across 1,356 within-subject session pairs, TCLA achieved a mean $R^2$ of $0.371\pm0.009$ with a failure rate of 6.8\%. Across 2,134 cross-subject session pairs, TCLA achieved a mean $R^2$ of $0.218\pm0.004$ with a failure rate of 12.9\%, substantially better than those of the comparison methods. These results demonstrate that by preserving behaviorally relevant and task-dependent latent structure, TCLA improves the robustness of neural decoding across recording sessions and subjects. The source code is publicly available at \href{this https URL}{this https URL}.

---


### 99. [SatUnreal: A High-Precision Synthetic Dataset for Satellite Stereo Matching via Unreal Engine](https://arxiv.org/abs/2609.27442)

**<font color=#1a73e8>作者：</font>** Han-Gyeol Kim, JaeWan Park, Junmin Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D reconstruction from satellite imagery is essential for large-scale topographic analysis, yet the lack of high-fidelity training datasets with accurate occlusion labels remains a primary bottleneck. Existing benchmarks, such as US3D and WHU-Stereo, face inherent challenges in spatio-temporal mismatch -- environmental changes and shadow displacements between multi-view acquisitions -- and provide ambiguous ground truth in occluded regions due to LiDAR sparsity. In this paper, we propose SatUnreal, a high-precision synthetic dataset designed to fundamentally overcome these limitations through an Unreal Engine-based simulation pipeline. SatUnreal provides 10,000 stereo pairs with high resolution (0.3m GSD) and is characterized by: (1) Physical Geometry Simulation, replicating realistic satellite orbits by systematically varying baselines and azimuths; (2) Spatio-temporal Consistency, eliminating temporal noise through fixed virtual environments; (3) Topographic Diversity, spanning dense urban canyons to low-texture natural terrains; and (4) Mathematical Label Integrity, utilizing a novel two-step linetrace algorithm to generate flawless occlusion masks. Experimental results using SOTA iterative models demonstrate that models trained exclusively on SatUnreal achieve superior zero-shot transfer performance on real-world benchmarks (US3D, WHU-Stereo) compared to those trained on real datasets. Our findings prove that physically accurate synthetic data provides a more effective supervisory signal for learning geometric features than complex real-world observations, establishing a new paradigm for Sim-to-Real transfer in Earth Observation.
Code and dataset are available at this https URL

---


### 100. [Quantum Reinforcement Learning for Cost and Delay Tradeoffs in Quantum Cloud Orchestration](https://arxiv.org/abs/2609.27446)

**<font color=#1a73e8>作者：</font>** An N. H. Phan, Dang Van Huynh, Muhammad Usman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum cloud computing, delivered through the quantum-as-a-service (QaaS) model, provides access to quantum computing resources. However, applying uniform time-based pricing across fundamentally heterogeneous quantum resources significantly complicates task orchestration, particularly when addressing the tradeoff between execution costs and system performance. While heuristic methods rely on predefined scheduling rules, classical deep reinforcement learning (DRL) models may require more trainable parameters in this setting. Motivated by the potential of parameterised quantum circuits (PQCs) as compact function approximators, we propose QRLQ, a cost-delay-aware quantum cloud scheduling framework integrating PQCs with a dueling double deep Q-network (D3QN) to dynamically account for both cost and delay. Our simulation results show that QRLQ achieves lower mean cost and delay than the heuristic baselines, achieving a 5-11% lower mean cost relative to availability-based and rotation-based heuristics and reducing mean delay by 17% and 82% relative to the strongest and weakest heuristic baselines, respectively, while retaining execution fidelity within 2% of a fidelity-greedy policy. Compared with the classical DRL baseline, QRLQ achieves comparable scheduling performance while using 72% fewer trainable parameters. This work explores the feasibility of using QRL for task orchestration in quantum cloud environments and demonstrates its potential for cost-delay-aware quantum resource management.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-240](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
