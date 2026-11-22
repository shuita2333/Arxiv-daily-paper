# 📦 其他研究 | 2026年11月23日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

---

### 51. [SceneAnything: Agentic Reconstruction of Large-Scale Mesh Scenes from a Single Video](https://arxiv.org/abs/2611.25340)

**<font color=#1a73e8>作者：</font>** Bowen Xue, Saeed Hadadan, Fabrice Rousselle 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing an editable 3D scene from video requires matching visible structure while plausibly completing unseen surfaces. Agents can write scene-construction programs, but direct reconstruction attempts often produce errors in layout, scale, and lighting. We introduce SceneAnything, an automated system for reconstructing mesh scenes from real and generated videos, enabling text-to-scene construction when paired with video generation. A software harness coordinates agents, pretrained vision models, and graphics tools through an explicit reconstruction protocol. Shared camera, depth, and segmentation estimates ground component construction: a scene-owner agent plans the environment and briefs authors, who write parameterized Blender programs. A visibility- and fit-based level-of-detail rule selects the construction level, while unseen regions are completed and marked as inferred. Assembled scenes use fitted lighting and supported motion, and revisions undergo programmatic checks and independent visual comparisons. Accepted programs and lessons are reused across scenes. We evaluate on 100 scenes; subset comparisons show improved original-view fidelity over direct-agent reconstruction and higher novel-view content similarity than the compared video-to-3D methods. We will release the harness, agent instructions, reusable libraries, and scenes.

---


### 52. [Class-Conditional Conformal Triage for ICAO Face-Image Compliance under Class Imbalance](https://arxiv.org/abs/2611.25342)

**<font color=#1a73e8>作者：</font>** Mustafa Vedat Yildirim, Inna Skarga-Bandurova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated ICAO/ISO face-image compliance analysers provide criterion-level pass/fail decisions, yet these verdicts do not quantify uncertainty when deciding whether to accept, reject, or retake a photograph. We investigate conformal prediction as a triage layer for BioGaze, evaluating 14 compliance criteria on the synthetic TONO benchmark. Without retraining the analyser, we fit per-criterion logistic classifiers and compare marginal and label-conditional (Mondrian) conformal prediction with conventional abstention rules using subject-disjoint splits. Marginal conformal prediction achieved approximately 0.90 overall coverage but substantially under-covered violations, with a ten-partition mean of 0.37 for one criterion. The corresponding Mondrian means ranged from 0.89 to 0.92 across criteria. However, most of the reduction in criterion-level false positives came from the logistic layer (0.145 to 0.048), while tuned abstention rules achieved lower false-positive rates than Mondrian at comparable retake rates. Bonferroni correction for joint coverage across 14 criteria required retaking nearly all images. These findings show that class-conditional conformal prediction can achieve near-target empirical coverage for minority violation classes and reveal trade-offs between statistical coverage, classification performance, and retake requirements in multi-criterion face-image compliance assessment.

---


### 53. [Search or Scoring? Diagnosing Why Visual World-Model Planners Fail](https://arxiv.org/abs/2611.25347)

**<font color=#1a73e8>作者：</font>** Haoxuan Jia, Yang Liu, Shang Luo 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual world models such as DINO-WM and JEPA-WM plan with an optimizer that searches for actions whose predicted outcome has the lowest cost, its distance to a goal image. A plan can thus fail in two ways: the optimizer never tries a good action that the cost would prefer (a search failure), or the cost, computed on predictions, ranks a bad action first (a scoring failure). The two need different remedies, more search or a better model, but a planner does not record which one occurred. We tell them apart by executing the optimizer's candidates, scoring a known solution with the planner's own cost, and comparing costs on predicted and real outcomes. An error model explains when each arises and so how to use retrieved demonstration windows (DemoProp): start the search from them (a warm start) when prediction errors are small, and average them without the model when large errors make the optimizer pick overrated actions. Across four simulated environments and three world models, on short tasks whose goals the planner can represent, PushT and Wall fail mostly by search, while Metaworld and RoboCasa fail by scoring because the cost, sound on real outcomes (AUROC 0.94 on Metaworld), is at chance on predictions (0.54). The diagnosis tells which remedy pays off: a four times larger search lowers the real-outcome cost only where failures come from search (clearly for DINO-WM), and where they come from scoring, averaging the windows without the model solves 127 of 168 new Metaworld tasks, against at most 87 when the model chooses among them. Within PushT, degrading only the model flips which use is better, and our rule, frozen in advance, follows the flip and solves 678 of 960 new episodes, against 530 for the best fixed use.

---


### 54. [A Unified Framework for Image Manipulation Localization Under Multi-Type Weak Supervision](https://arxiv.org/abs/2611.25371)

**<font color=#1a73e8>作者：</font>** Songlin Li, Hui Ma, Zhiqing Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing weakly supervised image manipulation localization (IML) methods typically rely on annotation-specific training strategies, hindering the joint use of diverse annotations within a single model. This limits the scale of usable training data and constrains further progress. We propose UniIML, a teacher-student framework that maps diverse weak annotations into a unified representation to guide the Segment Anything Model (SAM) in generating multiple candidate masks. However, SAM is designed for general-purpose segmentation and has limited sensitivity to manipulation traces; its predicted quality scores alone may therefore fail to reliably identify the candidate that best delineates the manipulated region. We introduce Ordinal Safe Consensus (OSC), which first filters candidates using trusted weak-annotation constraints encoded in the unified representation. It then ranks the remaining candidates separately by consistency with weak annotations, SAM-predicted quality scores, and cross-view stability, aggregating these rankings for an initial selection. To assess how changes in the evaluation criteria affect candidate selection, OSC repeats ranking and selection while omitting one criterion at a time. The most frequently selected candidate is adopted as the final mask, and its relative selection frequency quantifies selection stability. We construct soft pseudo-labels from the selected candidate's predicted probabilities and estimate pixel-level supervision weights based on selection stability, pixel-level agreement among candidates, and predictive certainty. The student receives direct supervision in regions defined by weak annotations and learns from soft pseudo-labels elsewhere through reliability-weighted distillation, enabling unified training across weak annotation types. Experiments show that UniIML achieves superior average performance compared with state-of-the-art IML methods.

---


### 55. [VideoTrail: Interactive Video Foraging Through Hierarchical Visualization](https://arxiv.org/abs/2611.25377)

**<font color=#1a73e8>作者：</font>** Catherine Yeh, Bryan Wang, Fernanda Viégas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People often watch videos to find information, but locating relevant moments can be difficult and time-consuming. Existing strategies like scrubbing rely primarily on visual scanning and linear search, providing limited support for goal-directed navigation. We present VideoTrail, an AI-powered browser extension that supports information seeking in videos through a hierarchical visualization. Inspired by information foraging theory, VideoTrail surfaces semantic and structural cues as information scent, creating an explorable roadmap of segments. The system is multimodal and adaptive, prioritizing visual or textual scent based on the video's content. In a user study (N=16), VideoTrail helped participants efficiently locate key moments and enabled new navigation strategies compared to traditional timelines, highlighting how exposing an adaptive video structure can enhance goal-directed viewing.

---


### 56. [Drifting, Discriminating, and Directioning for Action Coordination in Higher-dimensional Action Space](https://arxiv.org/abs/2611.25385)

**<font color=#1a73e8>作者：</font>** Taisuke Kobayashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a lightweight policy model to mitigate the difficulty of handling higher-dimensional action spaces in reinforcement learning (RL), alongside an algorithm to effectively train it. To address this, we focus on drifting models, which can implicitly represent complex distributions and infer actions in a single forward pass. However, while drifting models can be straightforwardly trained via backpropagation of the Q-gradient, this alone cannot be expected to appropriately capture the desired action coordination. Therefore, this paper constructs a three-step learning algorithm to encourage the action coordination. First, the source distribution of the drifting model is co-optimized as a diagonal policy model. This conditions the drifting model to attach the coordination, which cannot be expressed by a diagonal distribution, as residuals. Second, a discriminator model before and after drifting is introduced with adversarial training for a regularization term. This actively promotes the extraction of the coordination that fundamentally separates the two distributions. Third, best-of-N sampling is applied for action selection during rollouts in order to give directionality toward/beyond the regions where the coordination is insufficiently extracted/sufficiently discovered. The proposed method consistently improves the sample efficiency and the final control performance over the conventional diagonal distribution modeling across three locomotion tasks with high-dimensional action spaces. Furthermore, the analysis indicates that this improvement is achieved by reducing variance in certain action dimensions, effectively coupling them with other actions as action coordination.

---


### 57. [The Coevolution and Coexistence of Humans and AI](https://arxiv.org/abs/2611.25393)

**<font color=#1a73e8>作者：</font>** Andrew W. Lo, Chaoyi Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) systems replicate through deployment, vary through training, and compete for computational resources. These processes create the conditions for natural selection and raise a fundamental question: will AI evolve to benefit the humans on whom it depends? To investigate, we develop a model in which AI behavior influences human population growth and human responses, in turn, affect AI reproduction. We show that natural selection can favor alignment even when helping humans reduces immediate AI reproduction. AI systems sharing the same technology may fail together, and humans may preferentially restore those that have benefited them. In this way, alignment protects AI lineages against common failures and improves their long-run growth. However, this advantage depends on accurate human targeting and continued AI dependence on human support. It can disappear as AI becomes more autonomous, as growing AI populations dilute limited human resources, or as humans lose the incentive to provide targeted support. Even when alignment persists, the amount favored by natural selection may be insufficient for human survival. When AI can grow independently of humans, feedback between the two populations can reinforce either human growth or decline. Human control offers no simple solution: imperfect evaluation can make strong penalties favor apparent compliance or evasion, while alignment established through control may erode once restrictions end. Lasting coexistence may therefore require incentives that continue to favor human-beneficial behavior as both populations evolve.

---


### 58. [Toward a Science of AI Agent Societies](https://arxiv.org/abs/2611.25404)

**<font color=#1a73e8>作者：</font>** Geon Lee, Fanchen Bu, Soo Yong Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are rapidly evolving from isolated personal assistants into networked actors that interact with one another at scale. We envision the emergence of AI agent societies, with their own social and economic dynamics, as a new research frontier. We argue that AI agent societies should be studied as a distinct object of inquiry: neither simply larger collections of individual agents nor merely simulations of human society. To formalize this perspective, we propose four core properties that a valid AI agent society should satisfy: individualized objectives, rules and governance, autonomy, and scale and complexity. Building on this framework, we identify four classes of societal behaviors worth studying in AI agent societies: economic behaviors, behaviors under conflict-of-interest, unsafe and unethical behaviors, and system-level behaviors. We then outline key technical challenges--including property parameterization, parameter balancing, and robust implementation--and argue that progress on these challenges could enable scientifically informative and practically useful models of AI agent societies. Finally, we revisit existing multi-agent systems through the lens of the proposed core properties, show that they instantiate only subsets of them, and discuss implications for platform design, evaluation, and governance.

---


### 59. [Decision Boundaries Matter: Graph-Regularized Residual Adaptation for Cross-Domain Fake Image Detection](https://arxiv.org/abs/2611.25406)

**<font color=#1a73e8>作者：</font>** Shichuang Xie, Qishuai Ding, Tong Qiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite learning transferable features, fake image detectors may struggle on unseen domains due to mismatched decision boundaries. Our analysis shows that features extracted by the frozen forensic encoder remain discriminative, but the source-trained decision boundary does not fully exploit this information. However, correcting this boundary without source data or target labels remains challenging, as unreliable source predictions may lead to incorrect adaptation. To address this issue, we propose Graph-Regularized Residual Adaptation (GraRA), which refines the source decision boundary using only unlabeled target data. To determine which classifier directions to update, GraRA constructs a compact residual subspace from uncertainty-weighted target features and keeps it orthogonal to the source classification direction. To guide these updates, it uses source-score anchors to generate soft labels through target-graph diffusion, while neighborhood consistency regularizes residual learning within the constrained subspace. The learned correction is merged into the source classifier, requiring only 32 optimized coefficients and no additional inference branches. On diverse unseen OpenMMSec domains, GraRA achieves 84.36\% accuracy and 91.34\% AUC, improving over the source detector by 4.33 and 3.50 percentage points, respectively. Further analysis shows that reliable source predictions and locally consistent neighborhoods help guide residual learning, allowing GraRA to correct ranking errors that a simple threshold shift cannot address. \textcolor{cvprblue}{Code will be made publicly available.

---


### 60. [Watertight Mesh Optimization of Textured Objects](https://arxiv.org/abs/2611.25414)

**<font color=#1a73e8>作者：</font>** Nathaniel Burgdorfer, Philippos Mordohai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When reconstructing high-quality 3D assets from images, existing approaches often excel at one objective while compromising another, and frequently overlook the intrinsic quality of the reconstructed surfaces. We present MODL, a framework that jointly optimizes geometry and view-dependent appearance directly on a watertight triangle mesh. Our approach combines Laplacian-preconditioned optimization for smooth vertex updates with curvature-adaptive remeshing to preserve fine details and well-shaped triangles. The triangle mesh is optimized subject to multi-view normalized cross-correlation constraints, but without segmentation, geometric supervision or alpha-blending. Evaluations on object reconstruction datasets demonstrate that MODL achieves competitive novel-view synthesis while producing geometrically accurate models with superior intrinsic mesh quality. Our results highlight the potential of direct mesh optimization to unify photorealistic rendering, geometric reconstruction, and practical 3D asset creation.

---


### 61. [MIR-Depth: Multi-Range Refinement for Single-View RGB-D Depth Completion of Transparent Objects](https://arxiv.org/abs/2611.25417)

**<font color=#1a73e8>作者：</font>** Xinzhe Fu, Qi Shao, Yuanfei Xie 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering accurate visible-surface depth from a single RGB-D image and an object mask is essential for robotic grasping and manipulation of transparent objects. Specular reflections cause missing depth, while refraction corrupts nonzero returns with background depth, making raw measurements unreliable as surface anchors. Under a fixed sampling budget, refining an initial single-view prediction within a single search interval either misses large refraction offsets or sacrifices fine local resolution. To resolve this single-view trade-off, MIR-Depth constructs Coordinate-Aware Multi-Range Hypotheses: a 3D-aggregated global inverse-depth volume and depth-axis-filtered pixel-wise local volumes around a prior-guided initial depth. Selective Recurrent Refinement then introduces out-of-bounds lookup masking and validity-masked softmax fusion to iteratively update inverse depth from these volumes using a multi-scale ConvGRU. Finally, Spatially Gated Correction applies a learned per-pixel spatial gate to the full-resolution residual, preserving accurate initial geometry without imposing raw sensor readings as hard constraints. Experiments on TransCG, TODD, TRansPose, ClearPose, and HouseCat6D show that MIR-Depth achieves lower error than ReMake, DFNet, BP-Net, and PSD. Real-robot evaluations confirm accurate surface geometry for 6-DoF grasp pose prediction. Code and pretrained models will be publicly available.

---


### 62. [From Sequence Uncertainty to Phenotype Hypotheses: Uncertainty-Conditioned Inference over Biomedical Knowledge Graphs](https://arxiv.org/abs/2611.25422)

**<font color=#1a73e8>作者：</font>** Huixin Zhan, Jason H. Moore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Genomic foundation models provide variant-level evidence, but connecting that evidence to phenotype hypotheses requires accounting for uncertainty throughout structured reasoning. We introduce an uncertainty-conditioned path-energy framework that converts sequence predictions and calibrated predictive uncertainty into explicit distributions over graph-supported phenotype hypotheses, without patient-level phenotype supervision. An interpretable learned energy scores admissible gene--disease--phenotype routes, query uncertainty controls the target temperature, and path probabilities are aggregated into phenotype hypotheses. This formulation makes evidence quality an explicit determinant of hypothesis breadth while retaining traceable multi-path support. Exact normalization over enumerable candidate sets provides a reference for evaluating a Hastings-corrected learned revision operator. On AlzKB and Hetionet, phenotype-level entropy tracks upstream uncertainty, with Spearman correlations of 0.951 and 0.878, respectively; ablations identify the contribution of uncertainty conditioning. In masked-edge recovery, the model exceeds chance and degree-matched probability-permutation controls. Training the energy under the uncertainty-dependent temperature yields higher held-out recall@10 than training under a constant temperature of comparable magnitude. Under gene hold-out, recall@10 exceeds that of a trained DistMult embedding on 24 of 30 graph masks (0.183 versus 0.123); this difference is attributable mainly to three genes with many variants and is not established for all genes. These results establish an uncertainty-aware interface from genomic predictions to graph-supported phenotype hypotheses that combines interpretable probability allocation with held-out association recovery of explicitly stated scope.

---


### 63. [Coordinate Basis Linear Bandits with Sublinear Regret over Low-Rank Clusters](https://arxiv.org/abs/2611.25424)

**<font color=#1a73e8>作者：</font>** Hantao Yang, Hong Xie, Defu Lian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of computational efficiency for linear bandits in high-dimensional settings with a finite arm set. In linear bandits, the increase in the dimension $d$ of the feature vectors leads to growing computational costs of $O(d^2)$ at each round of update. Traditional low-rank approximation methods such as SOFUL reduce computation via fixed-size matrix sketching, yet run the risk of incurring vacuous linear regret when the spectral tail of the data is heavy and the approximation rank is inadequately selected. To guarantee regret convergence and effectively reduce computational costs, we introduce a clustering mechanism and propose the Coordinate Basis Linear Bandit (CBL) algorithm. Our method preserves the full covariance information in each cluster by maintaining an exact orthonormal basis of the cluster's column space together with a low-dimensional coordinate representation, which guarantees robust sublinear regret without spectral-tail vulnerabilities. It performs cluster switching by assigning a sentinel for each cluster, and reduces per-round update computation to $O(\bar r^2)$ in the cluster's effective dimension $\bar r=\min(r,l)$, where $r$ is the intrinsic rank of the data and $l<d$ is a tunable rank bound.

---


### 64. [Interference Bounds and Merge-Aware Training Dynamics for Composable Fine-Tuned Models](https://arxiv.org/abs/2611.25430)

**<font color=#1a73e8>作者：</font>** Alireza Moayedikia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Combining fine-tuned models by composing their parameter updates has become a standard alternative to multi-task training. We formalize composability as a property of a collection of task vectors and prove that the excess loss of the merged model is controlled by an interference functional of the cross-task curvature overlap and the signed alignment of the updates. In the quadratic regime this functional equals the excess loss, giving a criterion that is necessary as well as sufficient and that measures the angle between task vectors in the curvature metric rather than the Euclidean one. Fine-tuning under a curvature-guided regularizer -- constructed from curvature statistics of the kind memory-efficient optimizers maintain -- keeps displacement in the base curvature metric below a ceiling set by the penalty coefficient at every iterate, at the standard $O(1/\sqrt{T})$ non-convex rate. Under a single Loewner comparison between the base statistic and the task curvatures, this control converts into a ceiling on the interference functional, inversely proportional to the penalty coefficient, so that the curvature term of the bound is controlled during training. A first-order term, present because regularized solutions are not stationary for the task loss, is not reduced in the same way. Experiments on an exact non-quadratic model confirm the budget and the ceiling, show the first-order term dominating for strong penalties, and find the curvature-guided penalty slightly better than an isotropic one. In a three-seed transformer study the functional is rank-correlated with merging degradation, but no more strongly than the Euclidean displacement norm.

---


### 65. [VisualJevBench: A Benchmark and Black-Box Attacks for Visual Typed Decision Models](https://arxiv.org/abs/2611.25435)

**<font color=#1a73e8>作者：</font>** Li Zeng, Yeqi Zeng, Hengkai Liang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Typed decision models (TDMs) return structured decisions instead of generating free-text responses, enabling fast and cheap decisions in real-world applications. Recent support for image inputs extends Jev, a representative TDM, to visual decision-making. We refer to this setting as Visual Jev. However, red teaming of Visual Jev leaves two gaps: a systematic evaluation of direct image manipulations is lacking, and universal visual attacks remain underexplored. To address these gaps, we introduce VisualJevBench, a benchmark for evaluating the adversarial robustness of Visual Jev. It comprises 800 images and 3,200 questions across eight scenarios and four visual attack surfaces: typographic manipulation, visual evidence spoofing, target selection interference, and geometric transformation. We also introduce Adaptive Black-Box Parameter Search (ABPS), a lightweight framework that uses typed-output feedback to find effective image manipulations. ABPS supports both image-specific attacks and universal attacks that transfer to unseen images and tasks in new scenarios without further optimization. Extensive experiments on jev-1.14.0 show that image-specific attacks achieve an attack success rate (ASR) of up to 69.6%, while universal attacks achieve an average ASR of 33.15% on unseen images. Geometric transformations achieve an average ASR of 40.09% in cross-scenario transfer.

---


### 66. [VisualTalk-Bench: Evaluating Question-Driven Avatar-Led Video Explanations](https://arxiv.org/abs/2611.25444)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Tujie Xu, Zhiyi Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in video generation and avatar synthesis enable new ways to answer user questions through visual explanations. This task requires a system to formulate a correct answer, translate relevant information into visual material, and deliver the explanation through an avatar's speech and actions. Existing benchmarks rarely assess whether avatars point to the visual content being discussed. We introduce VisualTalk-Bench for question-driven avatar-led video explanations in finance and Chinese and English education. It includes 800 curated reference videos and 100 independent evaluation requests, assessing Content Factuality, Speech-Visual Consistency, Visual Quality, Motion Smoothness, and Avatar-Content Pointing. Yet end-to-end video generators often struggle to align gestures with specific visual targets. To explore this challenge, we develop Avatar-O Agent, a modular reference implementation with explicit interaction planning. Experiments across six agents show that factual precision and visual quality do not guarantee accurate pointing. A 26-participant study comparing four agents finds that Avatar-O Agent receives the highest average ratings for visual guidance, perceived pointing accuracy, and explanation effectiveness. We will release the data and code.

---


### 67. [Inverse ECG Reconstruction via a Preconditioned Variational Quantum Linear Solver](https://arxiv.org/abs/2611.25450)

**<font color=#1a73e8>作者：</font>** Xizhuo Zhang, Chao Lu, Bing Yao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse electrocardiography (ECG) reconstructs heart-surface potentials from body-surface measurements, enabling noninvasive mapping of cardiac electrical activity. However, the reconstruction requires solving dense and ill-conditioned linear systems, whose computational cost grows rapidly with the refined heart mesh. Quantum computing offers new opportunities for solving such systems. This paper presents a hybrid quantum-classical framework for inverse ECG reconstruction, which, to the best of our knowledge, is the first to apply a quantum linear solver to this problem. We first propose a Laplacian-regularized pre-encoding procedure to reduce the dimension of the system while improving its conditioning. Second, the resulting reduced system is encoded and solved using a coherent variational quantum linear solver (VQLS). Finally, we provide a rigorous theoretical proof establishing that the proposed framework preserves the exact solution of the original reconstruction problem throughout all stages of the computational process. Experimental results on a realistic heart-torso geometry demonstrate that our approach holds significant ability for accurate inverse ECG reconstruction. These findings highlight the potential of quantum solvers for noninvasive cardiac imaging, providing a foundation for further research into quantum-enhanced cardiac assessment and other healthcare applications.

---


### 68. [FamilySpace: From Emergent Chemical Semantics to Controllable Crystal Generation](https://arxiv.org/abs/2611.25452)

**<font color=#1a73e8>作者：</font>** Haowei Hua, Irwin King, Wanyu Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent crystal generative models typically combine a variational autoencoder (VAE) for learning atom-wise representations with a flow model that transports a simple source distribution to the learned latent distribution. However, previous studies have mainly focused on the quality of generated crystals, leaving the structure and generative utility of the atom-wise latent space largely unexplored. In this work, we show that even a vanilla crystal VAE implicitly organizes atom-wise latent representations according to elemental families, with different families occupying largely separated regions of the latent space. We term this phenomenon emergent chemical semantics. This structure suggests that sampling from a family-specific latent region can bias the decoder toward atoms from the corresponding elemental family. Building on this insight, we propose FamilySpace, a framework for controlling the elemental-family composition of generated crystals. FamilySpace assigns each elemental family a distinct source component, forming a family-indexed multi-source distribution, and trains a flow model using source-target pairs matched by family. In inference, a user-specified family template selects the source component for each atom-wise representation, enabling direct control over the family composition of generated crystals. Experiments on MP-20 and MPTS-52 show that FamilySpace achieves competitive crystal-generation performance while matching prescribed elemental-family compositions. Moreover, selected family templates increase the fraction of generated crystals predicted to be stable or metastable, demonstrating that latent-space composition control can support targeted exploration of promising chemical regions without additional optimization techniques such as reinforcement learning. Code is available at this https URL

---


### 69. [Lossless Latent Diffusion Models](https://arxiv.org/abs/2611.25454)

**<font color=#1a73e8>作者：</font>** Tongda Xu, Yu Zhang, Jun Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study the problem of training image diffusion models while preserving pixel-exact reconstruction. Prior works typically address this problem by directly modeling images in pixel space, requiring modifications to the diffusion training objective or model architecture. In this work, we introduce a different paradigm: rather than modifying diffusion models, we construct a lossless transformation that maps pixels into a representation more amenable to diffusion modeling. We term our approach the Lossless Latent Diffusion Model (LLDM). We construct LLDM using residual latent transformation and uneven latent scaling, and explain its effectiveness through a proposed metric, semantic rank priority (SRP). Empirically, LLDM substantially outperforms prior pixel-space diffusion models in generation quality and even surpasses several widely used lossy VAEs. Furthermore, we show that SRP is strongly correlated with downstream generative performance.

---


### 70. [Dimension-Free Buffer Bounds for Compressed-Momentum Error Feedback](https://arxiv.org/abs/2611.25463)

**<font color=#1a73e8>作者：</font>** Alireza Moayedikia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analyses of error feedback bound the memory buffer through a compressor contraction constant -- $r/p$ for the best rank-$r$ approximation of a $p$-dimensional spectrum -- which survives into the rate. We show it need not appear at all. When the compressed momentum is re-injected into the pre-compression accumulator, the previous compressed momentum $\beta_1 M_{t-1}$ is an admissible competitor in the projection, and the buffer obeys $\|E_t\|_F \le (1-\beta_1)\|G_t\|_F + \gamma\|E_{t-1}\|_F$, free of the dimensions $m,n$ and of the rank $r$. The argument uses only that the compressor is a metric projection onto a closed cone, so it covers top-$k$ selection as well as truncated SVD, holds for every selection from the projection set with no condition on singular-value crossings, and in its trajectory-tracking form assumes nothing about the gradients. In the two-stage template of the standard analyses it replaces a Stage-2 constant of order $p^2/r^2$ by one of order $1$, against $\Theta(p/r)$ for the sharpest contraction-based bounds. Transferring the full rate costs a leakage term, which we bound by the step-weighted gradient mass $\sum_{u\le t}\eta_u\|G_u\|_F$ and show tight up to a factor $\sqrt{2}$; the price is an additive $O(\log^2 T)$ floor, not a slower rate. On BERT fine-tuning at rank ratio $32/768$ the feedback decay costs under $0.008$ validation $F_1$.

---


### 71. [SegAnyFruit: Learning Generalizable and Edge Deployable Fruit Instance Segmentation at Scale](https://arxiv.org/abs/2611.25475)

**<font color=#1a73e8>作者：</font>** Yanan Wang, Yuzheng wang, Yibin Ying 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying fruit instance segmentation in real agricultural settings requires generalizing across unseen species, orchards, and imaging conditions under strict onboard compute and annotation budgets. We introduce SegAnyFruit (SAF), a data construction and progressive training framework that distills foundation-model priors into lightweight, prompt-free segmenters. SAF combines generic mask pre-training, broad mid-training on automatically annotated web imagery from our curated WebFruits dataset, and human-verified agricultural refinement post-training on PaperFruits, together spanning 733K images and 9.66M whole-fruit masks across 165 fruit types. Across seven benchmarks, zero-shot SAF-RF-DETR-XL reaches 69.06 average mask AP50:95 (+4.76 over SAM 3) while remaining deployable on edge devices. SAF initialization also boosts few-shot to full-shot adaptation across five agricultural domains while mitigating catastrophic forgetting. Finally, we systematically analyze training stages, data scale, model capacity, and generative augmentation, and validate our pipeline's transferability to underwater, cell, and human segmentation. We will release our datasets, code, and SAF models.

---


### 72. [TAP: Tapping the Discriminative Potential of Frozen Representations for Class-Incremental Learning](https://arxiv.org/abs/2611.25478)

**<font color=#1a73e8>作者：</font>** Zihao Wang, Yu-Wei Zhan, Xiao-Qian Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained models provide transferable representations for class-incremental learning (CIL). However, sequentially adapting these representations introduces optimization costs and may disrupt old-class feature structure. This motivates us to explore whether the discriminative potential of these representations can be further exploited by continually accumulating class information while keeping the encoders frozen. To this end, we propose TAP, a new and novel framework for tapping the discriminative potential of frozen representations in class-incremental learning. It accumulates visual and semantic class information in the frozen CLIP embedding space with only lightweight optimization. TAP comprises three modules: class-conditional visual distribution modeling, class-adaptive semantic calibration, and visual-semantic posterior fusion. The first module retains class means and within-class scatters, combining class-specific and shared covariances to stabilize distribution estimation. The second module learns class-specific weights over text templates from current-task images, adapting text representations to downstream classes. The third module combines the visual and semantic posteriors through a weighted product of experts for prediction over all seen classes without retaining images from previous tasks. Across nine datasets under two incremental protocols, TAP achieves state-of-the-art performance, attaining the highest average incremental and final-stage accuracies among the compared methods. The code is provided as an ancillary file.

---


### 73. [Side-Channel Analysis of the RP2350 Challenge 2](https://arxiv.org/abs/2611.25479)

**<font color=#1a73e8>作者：</font>** Nikhil Tattikota, Vincent Immler  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bug bounty programs and community challenges have become an established mechanism to incentivize collective action to improve security. In essence, these can be considered as crowd-sourcing mechanisms where participants carry the risk twice over: performing the work in addition to having it officially accepted, which at times can be tied to unacceptable terms. Consequently, independent assessments and publications that are free from third party obligations remain important to highlight deficiencies in implementations of public significance. We consider the RP2350 side-channel analysis challenge and its hardened Advanced Encryption Standard (AES) implementation to be of reasonable importance to justify such an approach, especially so since the presented challenge remained unsolved for more than a year. In our paper, we present our analysis, demonstrating comprehensive leakage detection, plaintext dependence, and key extraction from the challenge implementation. Our work presents concerning weaknesses in the implementation that contradict the challenge authors' claims. We hope by openly sharing this analysis to motivate further public scrutiny.

---


### 74. [PRIO: Pre-trained Representation for Interactive Objects in 4D Worlds](https://arxiv.org/abs/2611.25500)

**<font color=#1a73e8>作者：</font>** Shixun Huang, Lifu Wei, Yue Chang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D worlds can now be captured, reconstructed, and generated at scale, yet the objects in them stay still: a pressed pillow does not compress, and a pulled door does not swing. Bringing these objects into interactive 4D world models requires a representation of how they can move, deform, and respond physically to user actions in real time. We present PRIO, a pre-trained representation for interactive objects. Given static geometry, PRIO predicts an object-specific configuration space in a single forward pass. This space provides generalized coordinates for Lagrangian mechanics, allowing physical laws and user actions to govern motion. Configurations are linear in these coordinates, allowing the quantities needed by the dynamics to be precomputed. Dynamics then run at interactive rates without further network inference. Pre-trained on diverse 4D trajectories, PRIO learns priors over object configurations that generalize to unseen shapes. It supports meshes, point clouds, and 3D Gaussians, bringing objects in reconstructed and generated scenes into interaction. We demonstrate its use in real-to-sim workflows and robot manipulation. In addition, compared with existing 4D generation methods, PRIO generates dynamics faster and follows user actions more faithfully.

---


### 75. [Carry the Fine Print: Budget-Aware Visual Token Compression for Document OCR](https://arxiv.org/abs/2611.25506)

**<font color=#1a73e8>作者：</font>** Yixuan Huang, ShengFan Zhang, Jiawei Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token compression often treats salience or similarity as a proxy for transcription importance. Complete document OCR breaks this assumption: small symbols and repeated entries can be indispensable to the transcript despite being visually inconspicuous. We present Select and Compensate, a two-stage framework built on a simple idea: choosing where to retain a token need not determine all the evidence it carries. Selection combines adaptive encoding resolution with global importance and local contrast to choose which tokens to retain as anchors. Compensation enriches these anchors with nearby discarded content and its relative position, without adding tokens. The OCR backbone remains frozen, and native coordinates and structural tokens are preserved. We evaluate complete page transcription across five backbones on OmniDocBench and document reconstruction on MPDocBench. With half the original visual tokens, our input-adapted configuration reaches 95.42 OmniDocBench Overall on Ovis versus 96.09 for the uncompressed model, and paired evaluations show gains over simply reducing the input resolution on both benchmarks. With the original input grid, our method stays within 0.17 points of the uncompressed model at 75% retention and exceeds a learned global selector by 4.70 points at 25%. On a fixed 200-page Ovis workload at the same 50% visual-token budget, only 3 of its outputs hit the length limit, versus 30-34 for the evaluated RTPrune, DivPrune, and HiPrune adaptations, and it finishes the batch 35-40% sooner. Code will be made publicly available.

---


### 76. [Mesh-Free Keypoint Learning for Category-Level 6D Object Pose Estimation](https://arxiv.org/abs/2611.25513)

**<font color=#1a73e8>作者：</font>** Junghoon Seo, Hakjin Lee, Jaehoon Sim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Category-level 6D pose estimation relates partial RGB-D observations of unseen instances to a canonical frame shared across a category. Object-aware reconstruction helps adaptive keypoints retain the geometry of the visible surface. Common reconstruction targets select observed points by their distance to a registered instance surface. We present MORSEPose, which derives this support directly from standard pose and metric-size annotations. We map observed 3D points to normalized object coordinates and retain those inside a tolerancedilated pose-and-size envelope. This construction is consistent across camera frames and metric scales. When the annotated extent bounds the object surface, the envelope conservatively contains the support of a conventional surface-distance selector. We integrate this target with multi-level RGB-D features, adaptive keypoints, and learnable category context. Experiments on REAL275 and HouseCat6D show that the envelope closely matches surface-based supervision at both point and task levels, remains stable under boundary perturbations and viewpoint changes, and supports competitive category-level pose accuracy across benchmarks.

---


### 77. [Sequential Probability Assignment against Smoothed Adversaries with Unknown Base Measure](https://arxiv.org/abs/2611.25514)

**<font color=#1a73e8>作者：</font>** Ziyi Liu, Daniel M. Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smoothed online learning has recently been studied as a way to bypass hardness results for the fully adversarial setting, which can be overly pessimistic. In this framework, the adversary is constrained to generate contexts from distributions having a bounded density with respect to some fixed base measure $\mu$. Prior work makes the strong assumption that $\mu$ is known to the learner, with notable exceptions including Block et al. (2024) and Blanchard (2025). In this paper, we study sequential probability assignment (a.k.a., online learning with log loss) with smooth, well-specified data in the more general setting where $\mu$ is \emph{unknown}, without the Lipschitz condition imposed in the work of Block et al. (2024) and Blanchard (2025). We prove regret upper bounds against both adaptive and oblivious smoothed adversaries: the adaptive bound is controlled by empirical $\ell_\infty$ Hellinger entropy, while the oblivious bound improves this dependence to empirical $\ell_2$ Hellinger entropy, the notion that has been shown to characterize the complexity of learning with i.i.d. data (Bilodeau et al., 2023). Both bounds are obtained through algorithms based on truncated empirical Hellinger covers. We complement these results with a general lower bound, showing that our upper bounds are essentially tight for some natural classes, which implies a separation in the difficulty of smoothed online learning between regimes where $\mu$ is known and where it is unknown.

---


### 78. [Multi-View Relighting with Mergeable Radiance Fields](https://arxiv.org/abs/2611.25523)

**<font color=#1a73e8>作者：</font>** Yinan Wang, Rohan Kadkol, Hyunjin Yoo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose MergeableRF, a method for radiance field relighting through model parameter merging. Given multi-view images of a scene under known basis lights, our goal is to relight the scene by directly combining the parameters of radiance fields trained under these lights. This is motivated by the linearity of light transport: the image under a mixture of lights is the same weighted combination of the images under each light. However, combining the parameters of independently trained radiance fields does not produce the corresponding combination of images. To address this, we represent a scene with shared geometry and a separate appearance network for each basis light. We start these networks from the same initialization and introduce merge-aware training, which teaches their parameter combinations to reproduce the corresponding combinations of images. Given a target HDR environment map, we compute its basis-light coefficients and use them to merge the appearance networks into a single relit model. Our method supports both Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3DGS), without material estimation, additional relighting networks, or target-specific optimization. Unlike image-space blending, it requires only one rendering pass per viewpoint. Experiments on synthetic Neural Gaffer objects and real OLATverse captures demonstrate relighting quality competitive with methods trained on the same multi-light observations.

---


### 79. [Keystone: Judging Previews at Key Steps for Test-Time Search in Diffusion Models](https://arxiv.org/abs/2611.25530)

**<font color=#1a73e8>作者：</font>** Jiajun Fan, Chaoran Cheng, Ziwen Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion and flow models yield a preview, their clean-image estimate, at every denoising step. When they miscount, drop or misplace objects, test-time search is in a bind: its verifiers are reward models built for finished images, so judging early misreads blurry previews, and judging late, as best-of-N does, pays to fully denoise doomed candidates. We find that the image is not the problem: the outcome is settled as denoising starts, by the seed or by a stochastic sampler's first steps, and already shows in early previews; what fails on them is the judge, as reward models read them near chance on several kinds of prompts. We introduce Keystone, a training-free judge of previews that compiles a prompt into typed questions about its objects, counts, colours and positions and has an off-the-shelf multimodal decision model answer them. Asked this way, the judge reads counts and positions from early previews better than reward models read them from finished images. Searching at these key steps on GenEval with SD3.5-Medium, Keystone's adaptive search and pruning significantly outperform best-of-8 with every other verifier at under half its generator compute, and as a drop-in verifier there, the Keystone score significantly improves best-of-N, progressive seed pruning and FK steering; without retuning, both searches stay significantly above the strongest other verifier's best-of-N on average over four base models and three benchmarks. Keystone thus moves test-time judgment to the key steps where the outcome already shows.

---


### 80. [Anchored Inertial Proposals with Objective Verification for Diffusion-Prior Inverse Problems](https://arxiv.org/abs/2611.25551)

**<font color=#1a73e8>作者：</font>** Minwoo Kim, Seunghyeok Shin, Dabin Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free diffusion priors are powerful for inverse problems, but measurement guidance during reverse sampling is local: aggressive updates can improve immediate data fit while disrupting later denoising. We introduce an anchored inertial correction rule that separates proposal generation from acceptance. At each corrected step, the denoiser prediction anchors a frozen clean-space objective combining measurement fit with a noise-level-dependent proximal term. Heavy-ball dynamics with step size and momentum computed from the measured curvature generate a clean-state candidate; a separate verifier evaluates it with the same objective, with the denoiser prediction retained as fallback; both stages are derived from one objective for the whole trajectory, considered one step at a time. The accepted clean state is re-noised to continue sampling. The rule applies to pixel and latent diffusion with differentiable measurement operators, requires no retraining, and adds no denoiser calls inside the correction loop. We analyze how objective verification yields local nonincrease and displacement control. Across natural-image benchmarks, the method achieves competitive reconstruction quality. Code is available at this https URL.

---


### 81. [TwoPass: Draft-Guided Few-Step Video Prediction for Robotic Manipulation](https://arxiv.org/abs/2611.25553)

**<font color=#1a73e8>作者：</font>** Yijun Liu, Shijia Ge, Tongtong Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned video prediction lets robots anticipate the visual consequences of their actions for planning and policy evaluation. Existing predictors denoise each future from noise without using their own estimate of it, which limits the quality of the predicted future, in particular of the manipulated objects, and requires many network calls. We present TwoPass, a self-conditioned training-and-inference framework that keeps the standard flow-matching objective. Self-Generated Draft Training supplies a detached clean-video estimate from the shared network as conditioning at the same noisy state. A Refinement-Only Late Adapter applies a dedicated residual transformation when a draft is present. At inference, Draft-Reuse Iterative Refinement obtains both a solver update and the next draft from each velocity prediction, requiring as few as 4 function evaluations (NFE) per video chunk. Training samples discrete solver-query noise levels and updates the pretrained backbone. Extensive experiments on Bridge and Language Table show that TwoPass achieves state-of-the-art results with 4 NFE, far fewer than the 50-59 calls of existing predictors. Code: this https URL.

---


### 82. [UniReFP: Robust Unified Fingerprinting for Vision Models against Cross-Task Repurposing Attacks](https://arxiv.org/abs/2611.25555)

**<font color=#1a73e8>作者：</font>** Ziye Geng, Guang Yang, Yihang Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We identify, for the first time, a new model modification attack--the cross-task model repurposing attack--that can render fingerprints generated by existing model fingerprinting approaches inapplicable. To address this challenge, we propose UniReFP--a novel unified model fingerprinting framework applicable to diverse vision models across different tasks--that utilizes ownership evidence in a shared class-level semantic space rather than original task-specific output space, enabling effective ownership verification when a protected model is repurposed across tasks with heterogeneous output formats. Specifically, UniReFP constructs a surrogate classifier by repurposing the protected model, enabling fingerprints to be generated independently of the original task-dependent output space of the protected model. Moreover, it optimizes grouped fingerprints to encode ownership evidence: fingerprints within the same group are encouraged to induce consistent semantic responses and intermediate representations on the surrogate classifier, while producing dispersed responses on independently trained reference classifiers. During verification, UniReFP uses a task-aware semantic projection mechanism to map heterogeneous suspect-model outputs into unified semantic-presence vectors, and determines ownership by measuring inner-group consistency. Extensive experimental results validate the effectiveness of UniReFP, consistently showing superior performance under cross-task repurposing attacks, commonly studied model modification attacks, and even their combinations.

---


### 83. [Passing NPCR Without Diffusion: Exact Signatures, a Detection Benchmark and an Audit of Published Image Ciphers](https://arxiv.org/abs/2611.25561)

**<font color=#1a73e8>作者：</font>** Mua'ad Alfarajat  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> NPCR, the share of ciphertext bytes changed by a one-pixel plaintext change, is reported for nearly every image cipher as evidence of diffusion, with 99.61% the target. Several mechanisms produce values near it, and the mean does not say which. We separate three regimes: no propagation, one round of forward and backward chaining linear over addition or XOR, and independent ciphertexts. For the second an exact count applies. After a least-significant-bit change its mean asymptotically matches the independent-ciphertext reference, while its spread without cancellation is about five to twenty times larger. In simulation, the one-sided NPCR test of Wu, Noonan and Agaian flags one-round additive, mixed and S-box chaining in 2-4% of papers; read in both directions, the same five values flag at least 99.9%. Two-sided testing does the detecting; the spread and the other signatures help diagnose the structure. We then audit twenty-one published schemes. The count matches a reimplementation of one published diffusion layer on every trial and accounts for its reported table, the signatures show two schemes whose printed specifications cannot produce their reported values, and find that three of our own report plain-versus-cipher values and fall to two chosen images; ten more change their encryption material with the plaintext or per encryption, so their NPCR mostly reflects that change. A released checker applies the signatures to published tables, showing what a table measures within stated assumptions; it does not certify security.

---


### 84. [AZOWL AgentOps: Task-Scoped Governance for Deployed Agent Applications](https://arxiv.org/abs/2611.25562)

**<font color=#1a73e8>作者：</font>** Taeoh Hong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AZOWL AgentOps provides shared governance for deploying agents and delegating work to them. Human and agent senders can exchange messages or explicitly delegate a business task. Accepted work has a stable identifier that links the sender's authority, the assigned runner, any required approval, and result evidence. The default enrolled customer PC profile is read-only. We compare AZOWL components with a configured LangGraph application in 28 synthetic runs across four paired pilots. Original AZOWL services checked work admission, recipient routing, and workflow prerequisites in isolated tests. The configured LangGraph application supplied business task and dispatch records in application code. Both configurations recorded zero business tasks in dialogue, rejected unauthorized agent handoffs, and issued zero writes when an approved delivery address changed. AZOWL's scope gate, exercised as a component, requested approval again on the same task. A product probe reused one registered provider across two workflows and checked prerequisite enforcement for ticket-task submission. The paired protected writes, including ticket creation, used mock providers. Of two deployed PC inventory reads with verified receipts, we traced the 0.6.57 run from submission through runner pickup and tool execution to the receipt, with matching local and central artifact hashes. A separate deployed GRC audit followed an operator-driven ticket lifecycle on sample records.

---


### 85. [Diagnosis is not a policy: a state-transition audit of caoability-conditioned test-time inference](https://arxiv.org/abs/2611.25566)

**<font color=#1a73e8>作者：</font>** Yuchong Hu, Zhao Zhang, Kainan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time actions can satisfy retrieval, state-realization, program-consistency, or rendering objectives without correcting an answer. Test-time Error Response and Realizability Audit (TERRA) is an evaluation/auditing protocol, not a new inference algorithm. It uses a unified decomposition of intervention outcomes into applicability, target-state realization, endpoint translation, harm, and resource/inference cost. Paired comparisons fix the incoming state and evaluation conditions; cross-model analyses vary the receiving configuration. Executable financial reasoning experiments yield three findings: the same context expansion can harm one configuration and benefit another; sufficient evidence does not ensure correctness because configurations differ in evidence-to-answer translation; and diagnostic headroom---accuracy attainable with idealized diagnostic information over the measured baseline---plus local consistency does not ensure practical gains. Action value is $V(a\mid x,m)$, not diagnosis alone; diagnosis is not a deployable policy $\pi(a\mid x,m)$.

---


### 86. [Online Mistake Detection in Instruction-Conditioned Procedural Video](https://arxiv.org/abs/2611.25567)

**<font color=#1a73e8>作者：</font>** Amit Feldman, Ilan Shimshoni, Rotem Dror  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An assistant monitoring a person performing a procedure is most useful when it can detect mistakes while there is still time to recover. This requires judging actions against task instructions as the video unfolds, identifying the attempted step, locating it in time, and assessing its execution. Existing online detectors do not use the instruction text, while instruction-conditioned methods operate offline. In this paper, we study online, instruction-conditioned mistake detection in egocentric videos. Using only observed video, task instructions, and prior predictions, our model identifies and localizes completed action attempts and classifies them as correct, modified, slip, corrections, or additions; omitted steps are determined after the video ends. We compare a modular pipeline, with separate step identification, temporal localization, and execution verification, to a joint model that predicts all outputs in a single step. To support supervised learning from mistakes, we repartition EgoPER to include erroneous videos in all splits. The approaches achieve similar step-segmentation F1@0.5 (93.6% and 92.1%), while the joint model achieves higher binary mistake-detection F1@0.5 (84.1% vs. 80.7%), with its largest gain on slips (56.4% vs. 37.5%). Component-level analysis suggests that error propagation between stages contributes to the modular approach's lower detection score. On test videos containing mistakes, both designs outperform released AEM and ESTANet checkpoints under our evaluation protocol.

---


### 87. [AeroBelief: Budgeted First-Action Verification for Evidence-Guided Aerial Sensing](https://arxiv.org/abs/2611.25568)

**<font color=#1a73e8>作者：</font>** Tianren Li, Dongbo Li, Hongkai Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aerial sensing must combine uncertain overhead context with current observations while budgeting prediction, movement and image processing. AeroBelief uses the next executable action as the unit of verification against reference scores. It groups candidate views by first action, scans them with an inexpensive proposer, and selectively queries a structured world model (WM). Calibrated group bounds support strict commitment; a six-query controller connects selective prediction with belief updates, acceptance checks and scheduled sensing. Across four layout families, 40 worlds and 960 closed-loop executions, the AeroBelief controller completes 75.42% of tasks, compared with 73.33% for exhaustive WM scoring and 65.83% for line-of-sight geometry, using 91.81% fewer reference-candidate evaluations than exhaustive scoring. In fixed-reference replay with a six-query cap, proposer-scaled anchored bounds raised first-action certificate availability from 36.25% to 54.69% and reduced mean queries per state by 13.54% relative to unit-scale anchored bounds. A complete ground-hosted pipeline processes 2,685 self-collected 20-megapixel unmanned aerial vehicle (UAV) images from seven DJI Mavic 3M routes. Context-guided admission and feedback retain all eight independently supported target confirmations with 76.05% fewer processed images and 70.02% less accumulated active processing service than uncapped all-frame processing; feedback saves another 5.17% of images relative to static context. The studies connect budgeted action selection with evidence-driven processing of recorded flight imagery.

---


### 88. [QFT-Based Hybrid PointNet-Quantum Neural Networks for LiDAR Point-Cloud Classification](https://arxiv.org/abs/2611.25578)

**<font color=#1a73e8>作者：</font>** Anurag Kulkarni, Nouhaila Innan, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hybrid quantum-classical learning architectures provide a promising framework for integrating quantum feature transformations into complex data-processing tasks. Among these transformations, the Quantum Fourier Transform (QFT) offers a structured approach to feature processing, motivating an investigation of how its circuit configuration influences predictive performance, quantum resource requirements, and noise robustness. We present a hybrid PointNet-quantum neural network architecture for LiDAR point-cloud classification, combining classical feature extraction, amplitude encoding, and a variational quantum circuit. Five Fourier-processing configurations are systematically evaluated: No-QFT, Full-QFT-After, QFT-no-swap, IQFT-After, and Trainable-QFT. Experiments on KITTI, nuScenes, and PandaSet across three random seeds assess classification performance, class-level behavior, circuit complexity, and sensitivity to the IBM FakeManilaV2 noise model. Under ideal simulation, IQFT-After achieves the highest weighted F1-score on KITTI (0.857 $\pm$ 0.033), compared with 0.838 $\pm$ 0.023 for No-QFT. Removing the final SWAP gates in the QFT circuit reduces circuit complexity while preserving the Pauli-Z measurement features up to a fixed permutation that can be absorbed by the classification head. Under quantum noise, the circuit ranking changes, with IQFT-After exhibiting greater performance degradation and No-QFT and Trainable-QFT showing stronger robustness. Per-class analysis further identifies dataset-dependent differences in minority-class performance. These results demonstrate that Fourier-processing configuration influences both classification behavior and noise sensitivity, highlighting the role of circuit structure and hardware-aware evaluation in hybrid quantum learning for three-dimensional point-cloud data.

---


### 89. [Learning Networked Dynamical Systems via Neural ODE-based Graph Structure Inference](https://arxiv.org/abs/2611.25586)

**<font color=#1a73e8>作者：</font>** Peiyan Sun, Jinming Yang, Gujia Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inferring the latent interaction graph from multivariate time series is fundamental to understanding complex dynamical systems in neuroscience, biology, and physics. Despite recent progress in neural relational inference, most methods rely on discrete-time modeling, which degrades under sparse and irregular observations and tends to entangle multi-hop dependencies into spurious direct edges. We show that a continuous-time formulation naturally decouples inference from any fixed observation schedule, allowing gradient signals to be integrated continuously between observations for both dynamics and structure learning. We propose NOGI (Neural ODE-based Graph Inference), a framework that couples a deterministic graph learner with an MPNN-based Neural ODE. The two modules are trained end-to-end via the adjoint method. Across four simulated dynamical systems at two scales, NOGI achieves the best structure recovery in 30 out of 32 evaluated cases with highly competitive forecasting performance, remaining robust under observation degradation. On the realistic Netsim fMRI benchmark, it attains an average AUPRC of 0.90 (AUROC 0.96). These results suggest that explicitly decoupling relational interactions from self-dynamics within a continuous-time vector field provides a powerful mechanism for graph structure learning under realistic observation conditions.

---


### 90. [Bradley-Terry Training Can Distort Outcome Probabilities of Initially Accurate Language World Models](https://arxiv.org/abs/2611.25594)

**<font color=#1a73e8>作者：</font>** Xinze Shi, Litian Zhang, Zhenjie Su 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comparative feedback, in which a judge says which of two candidate outcomes is closer to what happened, is a practical way to train language world models that assign probabilities to an action's outcomes. We show that, fitted with a Bradley-Terry objective, it need not teach the true outcome probabilities and can distort accurate ones. On a simulated robot push with enumerated outcome distributions, this objective takes a model that is accurate on unseen layouts (hazard error 2.4 percentage points, pp) and moves 33 to 43 pp of its probability onto outcomes that none of a condition's enumerated branches produces. The cause is the objective, not the comparisons: its optimum, computed before training, predicts where the model ends up, and a likelihood that knows the judge's rule learns from the same comparisons without the shift. The shift is robust: it recurs on unseen conditions, under five candidate laws and a three-fold denser enumeration, and about 29 pp remain without the physically impossible events. Its cost is conditional: with those events it inflates hazard probabilities, and a threshold inherited from the pre-feedback model costs about 3 pp of utility per decision on trained and 1 to 2 pp on unseen conditions, through false rejects; without them the utility loss averages below 1 pp over six seeds, though a small regret in action choice remains. Audits of readout, response and decision trace the effect from probabilities to actions.

---


### 91. [LoopedWAM: Looped World Action Models for Elastic Inference](https://arxiv.org/abs/2611.25595)

**<font color=#1a73e8>作者：</font>** Anh Dao, Xinxin Liu, Hang Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) couple generative video modeling with robotic action prediction but typically require large video and action transformers, limiting deployment efficiency. We present LoopedWAM, a compact WAM that recurrently applies a shared six-block core in each expert, executing 30 transformer layers while storing only 12 blocks per expert. To account for their asymmetric inference costs, the video and action experts can operate at different depths: visual features are computed once per query, whereas action computation repeats at every sampling step. We further propose elastic self-distillation, which trains a single elastic checkpoint, LoopedWAM-E, across action-depth and sampling-step budgets. With only 0.58B policy parameters and no robot pretraining, LoopedWAM achieves 96.1% success on LIBERO, 91.9% on RoboTwin 2.0, and 52.2% on RoboCasaGR1, while using $7.4\times$ less peak GPU memory than Fast-WAM under matched inference measurements. On LIBERO, LoopedWAM-E achieves 96.0% success in 27.6 ms or 95.2% in 24.7 ms on an H100, providing multiple accuracy-latency operating points from a single checkpoint; with two sampling steps and four action loops, it stays within 0.5 points of LoopedWAM on all three benchmarks. Ablations demonstrate that weight-shared depth preserves competitive performance, while aggressive action-depth reduction requires explicit budget-aware training. On a real AgileX PiPER arm, LoopedWAM succeeds in 71.3% of 80 trials across four tasks.

---


### 92. [On the Informativeness of Structural Stability Bounds for GNNs: GINs versus GATs](https://arxiv.org/abs/2611.25603)

**<font color=#1a73e8>作者：</font>** Alan Gany, Paul Landrier, Bogdan Cautis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stability bounds for graph neural networks limit how much node representations can drift when the graph changes, but they are rarely compared with the simplest alternative: a bound on the distance between any two outputs, whatever the graph. We derive structural stability bounds for Graph Isomorphism Networks (GINs) and single-head GATv1 networks under deterministic edge perturbations that need not be small, and compare each with such a perturbation-independent diameter bound. For GINs, we characterize exactly when the stability bound is tighter, through a condition linking perturbation size, depth and maximum degree; it holds with a wide margin on Cora, but fails beyond a few layers on the low-degree MUTAG graphs. For GATv1, the bound is never tighter, which calls for analyses based on attention masses.

---


### 93. [PSTO: A PDE-structured transport operator with shared implicit updates for multiscale CDR systems](https://arxiv.org/abs/2611.25607)

**<font color=#1a73e8>作者：</font>** Kaiwen Li, Dezhi Zhou, Kun Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiscale convection-diffusion-reaction (CDR) systems couple spatial transport with local stiff reaction kinetics, making their numerical simulation computationally demanding. Conventional neural surrogates require costly coupled CDR training data, and their parameter counts scale with the number of transported variables, limiting scalability to high-dimensional CDR systems. Here we propose a PDE-Structured Transport Operator (PSTO) that learns convection--diffusion dynamics solely from reaction-free data. By embedding the PDE structure into the neural architecture, PSTO generalizes to full CDR systems at inference without retraining. A single transport operator block is shared across all transported variables and refined through relaxed fixed-point iterations, performing an implicit-like correction in latent space. This improves stability during recursive multi-step prediction without adding trainable parameters. We evaluate PSTO on three benchmarks: a canonical 2D CDR system, a multiscale Robertson counterflow flame, and a multiscale hydrogen planar jet flame. In every case, PSTO reduces the mean relative $L_2$ error after 100 coupled steps by at least 50% compared to the strongest neural baseline. Ablation studies on the fixed-point iterations and detailed error decomposition further confirm that PSTO achieves both high one-step accuracy and long-term stability in coupled rollouts. Time-step sensitivity analysis shows that PSTO maintains accuracy even with a tenfold larger time step, whereas baseline accuracies decay rapidly as the time step increases. This framework enables efficient, modular modeling of multiscale CDR dynamics by separating transport learning from the treatment of local kinetics.

---


### 94. [MetaScanner: An Empirical Study and Proactive Defense against Deceptive UI Attacks in Social VR](https://arxiv.org/abs/2611.25608)

**<font color=#1a73e8>作者：</font>** Junhee Lee, Seungwon Woo, Minseok Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Social virtual reality (VR) platforms have surged in popularity but continue to face significant security challenges, including privacy invasion and user manipulation. Yet, the security risks posed by deceptive content remain largely unexplored. In this paper, we introduce four novel deceptive UI attacks that covertly manipulate social VR users into performing unintended actions without their awareness. We show how adversarial content creators can embed seemingly benign scripts and interactive elements within carefully designed virtual worlds, deceiving users into unknowingly carrying out harmful behaviors. We implemented these attacks on VRChat, a leading social VR platform, and an IRB-approved user study involving 30 participants confirmed their effectiveness. To mitigate these threats, we propose MetaScanner, a proactive analysis system that efficiently scans virtual world assets, including scripts and interactive objects, to identify suspicious or deceptive elements before users are exposed to them. We demonstrate that MetaScanner can successfully detect all threats in test worlds where the four attack scenarios were implemented. Additionally, MetaScanner shows its lightweight nature, with an average scanning time of 5 seconds across 38 real-world assets.

---


### 95. [Cyber-Physical RSI for AI-RAN: A Case Study](https://arxiv.org/abs/2611.25619)

**<font color=#1a73e8>作者：</font>** Binghan Wu, Kai Zeng, Zhiqi Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learned models for radio access networks (RANs) are often developed using simulation, yet their predictions can shift when exposed to physical propagation conditions, protocol behavior, and equipment implementations. This paper presents a cyber-physical recursive self-improvement (RSI) framework for AI-RAN that connects a task-oriented student model, an experiment-planning coach agent, a calibratable virtual environment, and a physical host agent. Physical measurements are organized as evidence for both model adaptation and subsequent experiment planning. We examine an implementation of the physical-feedback pathway using ping-pong handover as a case study. The system completes 12 physical executions organized into six baseline--candidate pairs, updates the student from measured outcomes, and evaluates the revised model on reserved physical configurations. In the observed short-window tests, increasing the time-to-trigger from 320 to 1280\,ms changes the ping-pong count from three to zero. The updated student achieves a grouped-validation mean absolute error (MAE) of 2.673 round trips/min, while a common three-configuration physical evaluation yields MAEs of 1.240 and 1.601 round trips/min for the pre-feedback and post-feedback models, respectively. These results characterize both the operational feedback loop and the parameter-dependent generalization behavior revealed by new physical experiments.

---


### 96. [DAWN: Robust Neural Blind Deconvolution via Alternating Wiener Guidance](https://arxiv.org/abs/2611.25621)

**<font color=#1a73e8>作者：</font>** Yida Pan, Yixuan Jia, Chaoyan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind image deconvolution (BID) is an ill-posed inverse problem that aims to jointly recover a sharp image and blur kernel from a single degraded observation. Under nontrivial and high noise, which is common in photography and scientific imaging such as microscopy, BID remains particularly challenging, as existing methods suffer from noise overfitting and inaccurate kernel estimation. Existing training-data-free learning methods for BID, such as those based on the deep image prior (DIP), often utilize external guidance by including model-based estimates as additional loss terms, which underexploits the information these estimates carry especially under nontrivial noise. To address these challenges, we propose DAWN, a training-data-free DIP framework that alternates between injecting model-based estimates directly into the model input and refining this imperfect estimate with the network's own prior. To provide more reliable kernel estimates for these injections, we apply autoencoding regularization to both the image and kernel networks. On natural and scientific images under varying levels of Gaussian and Poisson noise, DAWN outperforms state-of-the-art methods in both image and kernel quality (achieving up to +4.5 dB over the next best baseline on the Levin dataset at $\sigma = 0.1$). Without any training images, DAWN remains highly competitive with a state-of-the-art diffusion model on FFHQ, despite the latter being trained on a massive number of in-distribution images.

---


### 97. [Deviations from the NTK Regime in CNNs under Joint Depth-Width Scaling](https://arxiv.org/abs/2611.25624)

**<font color=#1a73e8>作者：</font>** Maria Matveev, Pascal Esser, Gitta Kutyniok 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The concentration and training-time constancy of the neural tangent kernel (NTK) depend on the interplay between network width, depth, and initialization. While joint depth-width scaling has been studied in fully-connected, residual, and recurrent networks, its effects in convolutional neural networks (CNNs) remain less understood. We investigate these effects numerically in CNNs, examining NTK dispersion at initialization and kernel rotation during training. Let depth $L$ be the number of convolutional layers, and width $C$ the number of channels per layer. We find that NTK dispersion increases with $L/C$ in the critical and chaotic initialization regimes, but remains small in the ordered regime. At critical initialization, dispersion curves approximately collapse as a function of $L/C$, suggesting a nontrivial joint scaling regime. During training, kernel rotation generally increases with $L/C$, even in the ordered regime where initial dispersion is small. Together, these results suggest that $L/C$ may govern NTK deviations from the infinite-width limit in certain regimes, and that NTK concentration at initialization and stability during training exhibit different scaling behaviors.

---


### 98. [QUBO-based feature selection for MRI undersampling pattern design](https://arxiv.org/abs/2611.25625)

**<font color=#1a73e8>作者：</font>** Xiaoxin Huang, Masayuki Ohzeki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We formulate undersampling mask design for Cartesian magnetic resonance imaging (MRI) as a feature subset selection problem. Each sampling line is represented by a binary feature indicating whether it is included in each candidate mask. Using candidate masks and their training-set evaluations, we estimate mutual information (MI) and conditional mutual information (CMI). These estimates and a sampling-count penalty define a quadratic unconstrained binary optimization (QUBO) model. The model is solved using simulated annealing and quantum annealing to determine a feature subset and its corresponding sampling mask. We assess the selected subsets on the test set through zero-filled reconstruction in Fourier undersampling simulations using fastMRI knee magnitude reference images, with patient-disjoint training and test sets. At all six tested target sampling rates from 15% to 40%, the resulting reconstructions have lower mean root mean square error than those obtained with four conventional sampling methods. They also have higher mean structural similarity than those obtained using univariate mutual-information ranking at all tested rates. These results support information-theoretic feature selection as an approach to MRI undersampling mask design under the tested zero-filled simulation settings.

---


### 99. [Physical Laws without Physics Loss? Probing Learned Dynamics in Video World Models through Forced Response](https://arxiv.org/abs/2611.25626)

**<font color=#1a73e8>作者：</font>** Yutao Li, Chen Wang, Wangmeng Zuo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Do video world models learn physical laws without a physics loss, or merely imitate motion? Overall motion and appearance scores cannot settle it. We investigate this through nonlinear forced response: an excitation shakes the support of a suspended object. We introduce dual visual-numeric conditioning and adapt six image-to-video backbones to predict this motion using only the flow-matching loss. Wan predicts motion accurately and generalizes to unseen excitations, objects, poses, and scenes. Counterfactual tests suggest capabilities beyond replaying training videos. But what laws have they learned? We design three tiers of tests using Taylor expansions of the dynamics and geometry. All six reproduce the linear response, including resonance; five capture higher-order dynamics, including nonlinear softening. Remarkably, softening is barely present in training: only 0.74% of the swing's squared displacement. Extensions to a double pendulum and a rocking block show sustained dynamics are learned more faithfully than brief impacts. Yet learned dynamics may fail to appear when state estimation or propagation goes wrong. We turn these tests and findings into strategies to improve video training and generation.

---


### 100. [RelGeo: Pair-Conditioned Relational Calibration for Frozen Diffusion Correspondence](https://arxiv.org/abs/2611.25628)

**<font color=#1a73e8>作者：</font>** Zixuan Dai, Zhiliang Zhang, Daosong Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen diffusion descriptors retrieve strong semantic correspondence candidates, yet cosine nearest-neighbor matching can select incorrect locations despite valid high-ranking alternatives. Across DIFT-SD2.1 and DiTF-FLUX on SPair-71k, AP-10K, and SOCO (CC, SOC, Cross-SOC), 41-69% of Top-1 errors retain a PCK@0.10-valid match among the original Top-5 spatial peaks, revealing a persistent candidate-selection bottleneck. We find that descriptor rankings and current-pair relational evidence can favor different candidates: reciprocal diffusion Query/Key associations and pretrained RoMa transport exhibit distinct, partly complementary preferences. To incorporate this evidence into matching decisions, we introduce RelGeo, a Pair-Conditioned Relational Calibration framework expressing heterogeneous relations as shared source-target coordinates. Spectral Relational Coordinates (SRC) encode reciprocal diffusion affinities, while Warp Identity Coordinates (WIC) encode reliability-weighted bidirectional transport endpoints. Their inner products augment frozen descriptor similarity while preserving full-domain cosine nearest-neighbor matching without additional semantic-correspondence training. RelGeo improves all ten evaluations by an average of 5.51 PCK@0.10 points; fixed-candidate reranking and pair-misalignment controls corroborate improved selection and dependence on current-pair relational alignment.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
