# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

---

### 51. [Map the Possibilities: Spatial Belief Fields for Language-Goal Aerial Navigation](https://arxiv.org/abs/2609.05841)

**<font color=#1a73e8>作者：</font>** Haotian Xu, Yue Hu, Zhengqiu Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-goal aerial navigation requires an agent to local- ize a potentially unobserved target from relational instruc- tions and partial observations, and translate this inference into metric actions in large-scale continuous environments. Existing methods often reduce language grounding to one single waypoint or action, prematurely collapsing the spatial uncertainty inherent in incomplete evidence and ambiguous relations. To address this limitation, we introduce SBFNav, a closed-loop navigation framework centered on a language- conditioned Spatial Belief Field (SBF). Unlike ego-centric maps that primarily record what has been observed, SBF rep- resents a task-conditioned distribution over plausible target locations, preserving multiple spatial hypotheses under par- tial evidence. At each step, this distribution is updated from accumulated observations as new evidence becomes avail- able. Built on this representation, SBFNav selects the goal that best aligns with the instruction and observations as a met- ric waypoint for control. Experiments on both the original and revised CityNav benchmarks achieve the best reported overall performance. On the Test Unseen split, our method improves SR from 25.91% to 32.29% and SPL from 19.63% to 30.43%. Ablation studies further confirm the advantages of spatial-belief modeling over single-point prediction.

---


### 52. [Selective Posterior Margin Regularization for Forward-Corrected Classification](https://arxiv.org/abs/2609.05859)

**<font color=#1a73e8>作者：</font>** Zexing Zhang, Jichao Li, Tianyang Lei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning with class-conditional label noise often relies on a transition model from latent clean classes to observed annotations. Forward correction embeds this transition in the likelihood, yet finite-sample networks may still memorize corrupted labels. The corrected likelihood also induces a reverse posterior over the clean classes that could explain each annotation. When its leading class differs from the annotation, the model and transition matrix provide evidence against that annotation, but the leading alternatives can remain nearly tied. We introduce Selective Posterior Margin Regularization (SPMR), which preserves the Forward objective and converts this disagreement into a graded update on the clean classifier. SPMR selects the leading reverse-posterior class, scales a detached pairwise margin by the separation between the two leading posterior classes, and assigns correspondingly little influence to diffuse conflicts. The gap factorizes into transition- adjusted pairwise separation and the posterior mass carried by the leading pair. The active margin follows the locally minimum-norm logit direction that enlarges the selected pairwise margin. Across five known-transition benchmarks, SPMR improves full-length Forward by 2.5-7.0 percentage points and remains 0.7-2.5 percentage points above Forward with Mixup and early stopping. Matched interventions support distinct gains from the posterior-space coefficient, transition-adjusted target, and pairwise action. The same design transfers to estimated transitions, human annotations, architectural changes, and stronger Forward recipes. The formulation uses latent-class evidence already available inside Forward correction without promoting every posterior conflict to a corrected label.

---


### 53. [Beyond Arbitrary Geometry: Topology Generalization In neural PDE Operators](https://arxiv.org/abs/2609.05860)

**<font color=#1a73e8>作者：</font>** Peiyao Chen, Zhouyuan Xu, Jianguo Nie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators that accept arbitrary meshes are often treated as geometry-general, but unseen domain topology changes both the invariant and decaying subspaces of a PDE operator. We use Hodge heat flow as a controlled lens on this distinction and introduce TopoBox-3D, where tunnels and cavities vary Betti support while the exact Hodge decomposition separates the harmonic kernel from the positive spectrum. Across six architectures, models that infer topology implicitly suffer excess matched degradation in 37 of 45 model--task topology-OOD cells, yet cases that change harmonic dimension are not more strongly penalized on average. The dominant difficulty is instead spectral: the initial Rayleigh quotient is the most stable predictor of error, and spectral broadening adds information for edge and face cochains. Most strikingly, controlled probes show that explicit incidence and harmonic coordinates do not yield the best kernel-identity accuracy; nevertheless, TNO ranks first in mixed-input nonharmonic accuracy on all six tasks with nontrivial harmonic support. Together, these results establish topology as a distinct generalization axis beyond arbitrary-geometry compatibility and show that its influence extends across the Hodge spectrum rather than remaining confined to the harmonic kernel. More broadly, they suggest that global, low-frequency structural priors may help organize predictions in the faster-decaying complementary component, offering a new perspective on how neural operators may generalize across topology as well as geometry.

---


### 54. [Budgeted Task-Aware Acquisition of Dynamic Networks](https://arxiv.org/abs/2609.05862)

**<font color=#1a73e8>作者：</font>** Zihe Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning on dynamic graphs is difficult when changes in the underlying network are only partially observed. Acquiring current graph information incurs observation and computational costs, making complete updates impractical under limited resources. This paper focuses on budgeted task-aware acquisition on dynamic networks, where a model needs to decide which stale graph information to refresh for a downstream task. We propose Scout, a lightweight framework that learns the task value of querying each node from the maintained graph and observation history. Our evaluation covers one synthetic and four real-world dynamic networks, two downstream tasks, nine acquisition baselines, and several query budgets. Scout achieves the highest mean downstream performance in 19 of the 21 benchmark-budget settings. Task-utility supervision also outperforms structural-change supervision in 13 of the 16 real-world settings. On the same dynamic network, task-matched acquisition improves link-prediction AUC by 0.012-0.016 and node-classification accuracy by 0.064-0.09 over task-mismatched acquisition. These results show that useful graph observations depend on the downstream task and that limited observation budgets can be allocated more effectively by learning directly from downstream utility.

---


### 55. [Tactile Search: Enhancing Targeting in 3D Space](https://arxiv.org/abs/2609.05867)

**<font color=#1a73e8>作者：</font>** Amber Maimon, Iddo Yehoshua Wald, Jonas Keppel 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual search is crucial in daily life, from scanning for relevant information to spotting signs of danger. When sensory channels are overloaded or degraded, cognitive tasks can be supported by crossmodal information representations through vibrotactile cues. We introduce Tactile Search, an approach that uses modulation of frequency and amplitude of vibrations to the hands, for guiding attention to the location of objects in 3D space. We evaluated this approach in a competitive VR game where participants searched for targets using both vision and touch. Across two studies -- an in-the-wild demonstration (n=55) and a controlled laboratory experiment (n=28) -- we found that vibrotactile feedback significantly improved performance and increased user confidence. In the combined haptic condition, performance did not differ across target heights. We further analyzed participants' subjective experiences and search strategies highlighting the benefits of the tactile cues. Our findings suggest that Tactile Search can enhance interaction and provide design considerations for integrating haptic search into interactive systems.

---


### 56. [A budget-dependent crossover between coverage- and response-based training-set selection for machine-learned interatomic potentials](https://arxiv.org/abs/2609.05877)

**<font color=#1a73e8>作者：</font>** Jia Bi, Alin-Marin Elena  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting compact training sets for machine-learned interatomic potentials requires deciding whether to preserve structural diversity or target configurations on which models disagree. The better choice can depend on how much data is retained, making a comparison at one training-set size insufficient. Here we link selection criteria to prediction accuracy through a budget-resolved comparison of retrained MACE models on GAP-20 Carbon and pooled revised MD17. Structural coverage is compared with a response-guided selector that targets disagreement between a coverage-trained model and a full-data reference. This retrospective response witness tests the value of model disagreement for compressing an already labelled pool. At 5\%, coverage gives smaller absolute deviations from the full-data error than random sampling across four force endpoints in both datasets. The witness has larger deviations than coverage at 1\% and 5\%, but the ordering reverses at 20\%. At 20\%, witness-selected models also lower direct held-out force errors by 0.46--5.89\% relative to coverage, with all eight paired training-seed intervals favouring the witness. Six errors fall below the full-data reference. Mean force-error reductions are 0.164--0.167~meV~$\textÅ^{-1}$, with larger gains for tail and masked endpoints. Complementary analyses show that learned similarity preserves the coverage ranking, while selecting by frozen-model error gives higher error than embedding coverage. These findings establish retained-data budget as a deciding variable in atomistic training-set selection and provide a direct test of when response-guided compression improves on structural coverage.

---


### 57. [CALM: Class-wise Agreement and Label-gated Disagreement Modulation for Decentralized Federated Learning](https://arxiv.org/abs/2609.05884)

**<font color=#1a73e8>作者：</font>** Yifan Ying, Qing Tian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional federated learning relies on parameter averaging, which forces clients to be doubly homogeneous: all must run an identical architecture, and accuracy degrades when local data are non-IID. Decentralized federated distillation sidesteps both: each client runs its peers' model snapshots as teachers on its own local data and distills from their soft predictions, with no server, no public data, and no shared architecture. Under severe non-IID skew, however, the trustworthiness of the aggregated teacher target is a matter of degree, yet existing pipelines make hard, all-or-nothing decisions: outlier teachers are discarded by threshold, and whatever target survives is trusted in full. We propose CALM, which replaces every hard decision with a smooth trust gate at three levels: per class, teachers are weighted by agreement with the peer consensus; per sample, distillation is scaled by the teachers' divergence from that target; and a label gate scales it by how strongly the target supports the sample's true label. None of this adds communication or auxiliary data. On CIFAR-10, SVHN, OrganAMNIST, and Google Speech Commands with heterogeneous client architectures under Dirichlet label skew, CALM consistently outperforms uniform and hard-filtered distillation and matches or exceeds competing heterogeneous-FL methods.

---


### 58. [UniFusion: Sparse-View 4D Reconstruction via Unified Spatio-temporal Depth Alignment](https://arxiv.org/abs/2609.05888)

**<font color=#1a73e8>作者：</font>** Yongzhe Lyu, Shaofei Wang, Yixin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we address the challenging problem of 4D reconstruction from sparse-view videos. This setup usually relies on monocular depth estimation to provide priors for the reconstruction model. A key challenge arises from limited cross-view overlap and temporal variation, making monocular depth predictions inconsistent across views and time. Existing methods align spatial and temporal dimensions in separate stages, requiring foreground segmentation masks while failing to leverage temporal cues for cross-view alignment. Contrary to these methods, we propose a unified spatial-temporal depth alignment framework that jointly resolves cross-view and cross-time inconsistencies without distinguishing foreground/background. Our method represents depth maps across views and time as a set of spatio-temporal neural fields. This representation not only yields fast convergence, but also captures spatio-temporal correlation among depth maps implicitly, without dependence on external segmentation/tracking models. We also propose a multi-view depth-order loss while leveraging the classic scale-and-shift-invariant loss to further improve the final depth quality. The aligned depths initialize and supervise Gaussian splatting models for 4D reconstruction. Experiments on Ego-Exo4D and EgoHuman demonstrate that our improved depth alignment substantially benefits dynamic Gaussian-splatting-based reconstruction methods for novel-time/view synthesis and geometry accuracy/consistency.

---


### 59. [A First-Order Learning Algorithm for Online Resource Allocation with Constant Regret](https://arxiv.org/abs/2609.05895)

**<font color=#1a73e8>作者：</font>** Menglong Li, Jiawei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a finite-horizon online resource allocation problem with initial resource capacities proportional to the horizon. In each period, a request type is observed and one action is chosen from a finite menu. Each action earns a reward and consumes a vector of resources. The arrival types are independent and identically distributed, but their probabilities are unknown. We present a primal first-order learning policy that, in each period, performs one gradient ascent update of the action coordinates associated with the current request type. The policy achieves $O(1)$ expected additive regret relative to the hindsight optimum, with a bound independent of the horizon $T$. It does not solve any linear program, and the regret bound does not require a nondegeneracy assumption on the fluid linear program.

---


### 60. [FreeTransformSR: Efficient Lightweight Image Super-Resolution via Free Low-Rank Learnable Transform](https://arxiv.org/abs/2609.05912)

**<font color=#1a73e8>作者：</font>** Hongji Li, Yunhui Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single image super-resolution aims to reconstruct high-resolution images from low-resolution inputs. This paper proposes FreeTransformSR, a novel lightweight super-resolution network based on a channel-wise free low-rank learnable transform. The transform learns task-adaptive basis functions in a data-driven manner, enabling adaptive feature modulation with minimal parameter overhead. To further enhance high-frequency detail recovery, we introduce a local feature modulation branch that complements transform-domain processing with depthwise convolution. In addition, a soft complexity adaptive module dynamically fuses the outputs of local convolution and window self-attention branches through a lightweight gating network, adaptively adjusting the fusion ratio based on regional texture characteristics. An adaptive intensity modulation strategy is also incorporated to adjust transform-domain response strength at the sample level, enabling the network to dynamically adjust processing intensity according to input features. Extensive experiments on five benchmark datasets demonstrate that FreeTransformSR achieves competitive PSNR/SSIM performance with significantly fewer parameters and FLOPs. Specifically, FreeTransformSR achieves 32.41 dB on BSD100 x2 and 27.00 dB on Urban100 x4 with only 595K parameters, while delivering faster inference speed than competing methods, making it well-suited for deployment in resource-constrained scenarios. Source code is available at: this https URL.

---


### 61. [PAI-Actor: Cinematic Multi-Character Replacement in Dynamic Scenes](https://arxiv.org/abs/2609.05918)

**<font color=#1a73e8>作者：</font>** Bangxun Tang, Heyuan Gao, Yiren Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PAI-Actor, a cinematic multi-character animation framework for character replacement in dynamic movie scenes. Unlike conventional animation systems that mainly drive a single static image or a single subject, our goal is to replace and animate multiple characters within real video clips while preserving the original scene dynamics, camera motion, and background content. This setting is particularly challenging because the generated characters must remain consistent with the source performance in motion and interaction, while also matching the surrounding background in lighting, shadow, composition, and overall cinematic appearance. To address this, we formulate multi-character animation as a structure-guided human recovery problem and build a movie-driven training pipeline from high-quality film data. Furthermore, to support practical cinematic production, we introduce a bidirectional-to-autoregressive distillation framework: we first train a bidirectional diffusion transformer for high-quality short-clip generation at 1080P resolution, and then distill it into an autoregressive video-to-video model for efficient inference and longer video generation. Experiments show that PAI-Actor enables high-fidelity multi-character animation with strong scene consistency, cinematic visual quality, and efficient long-form generation.

---


### 62. [A dictionary learning framework for graphs via filters and optimal transport](https://arxiv.org/abs/2609.05919)

**<font color=#1a73e8>作者：</font>** Jinchuan Liao, Dai Hai Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a graph dictionary learning (GDL) framework where each graph is represented as a zero-mean Gaussian distribution derived from its filtered Laplacian. Each observed graph is approximated by a barycenter over learned atom graphs, computed under the filter graph distance (fGOT), a graph comparison metric sensitive to global structural properties. The reconstruction error between the observed graph and its barycenter is measured by the surrogate fGOT (sfGOT) distance, a tractable approximation of fGOT that handles graphs without known node correspondence, and is minimized end-to-end via backpropagation. We further provide a novel interpretation of sfGOT through the lens of the Hilbert-Schmidt Independence Criterion, showing that minimizing the sfGOT distance between two graphs is equivalent to maximizing statistical dependence between the spectral embedding of their nodes. Experiments on benchmark datasets demonstrate competitive performance over existing GDL methods on graph clustering and classification tasks.

---


### 63. [AVSplat: Dense-View Feed-Forward 3D Gaussian Splatting with Assist-View Preconditioning](https://arxiv.org/abs/2609.05925)

**<font color=#1a73e8>作者：</font>** Muyu Xu, Fangneng Zhan, Yu Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose-free feed-forward 3D Gaussian Splatting enables novel view synthesis from uncalibrated multi-view images. Although more views should improve performance, existing methods often degrade with dense-view inputs because global aggregation spreads attention over many tokens, and naive voxel fusion averages many Gaussians into overly smooth representations. We present AVSplat, a framework that turns additional views into reliable signals for both aggregation and representation. Before global attention, each view performs a single lightweight interaction with a small set of Assist Views chosen for relevance and diversity, and the cached features provide a focused scene context that stabilizes correspondence. For representation, we use adaptive temperature-aware voxel fusion that sharpens attribution under high occupancy, guided by occupancy and point confidence. Crucially, AVSplat restores positive view scaling where performance remains stable or improves as more input views are added, instead of degrading in the dense-view regime. Ablations show that Assist View Preconditioning is primarily responsible for preventing dense-view degradation, while Occupancy-guided Voxel Fusion contributes most of the single-point image-quality gains.

---


### 64. [Beyond Classification: Structured Supervision Aligns Visual Evidence with Medical Semantics](https://arxiv.org/abs/2609.05937)

**<font color=#1a73e8>作者：</font>** Hexiang Bai, Hanyang Xu, Xiaoxue Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have shown immense potential in medical image analysis. However, standard pre-training via global image classification suffers from spatial collapse, where models rely heavily on background shortcuts rather than localising critical foreground lesions. To overcome this limitation and align visual evidence with precise medical semantics, we systematically investigate alternative pre-training this http URL, we evaluate three independent forms of structured supervision: topological priors via graph self-supervision, dense pixel-level constraints via segmentation, and cross-modal semantic grounding via image-text pairs. Notably, our empirical analysis reveals that while all three forms of structured supervision successfully alleviate the global pooling bottleneck and steer visual attention towards foreground regions, image-text alignment achieves the most superior performance. By embedding high-dimensional diagnostic logic, the cross-modal approach not only anchors attention on precise visual evidence but also enables profound abstract reasoning. Extensive experiments demonstrate that this semantically enriched pre-training fundamentally enhances the model's feature representation. Consequently, when fine-tuned for downstream clinical classification tasks, our models achieve superior accuracy and yield highly interpretable attention maps focused on true pathological features, vastly outperforming vanilla classification baselines.

---


### 65. [Interpretable and Fair Generalized Additive Neural Networks via Multi-objective Learning](https://arxiv.org/abs/2609.05946)

**<font color=#1a73e8>作者：</font>** Ziming Wang, Changwu Huang, Ke Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability and fairness are two of the most emphasized dimensions in trustworthy artificial intelligence (AI). Various explainable AI methods have been introduced to improve interpretability. This paper focuses on neural network (NN)-based generalized additive models (GAMs), a class of self-interpretable models. While most existing research has prioritized improving the accuracy of NN-based GAMs, their interpretability remains largely underexplored. To address this gap, this paper introduces explicit quantitative metrics for evaluating the interpretability of NN-based GAMs, empirically examines their effectiveness, and explores strategies for improving interpretability within these models. In addition, the simultaneous and explicit optimization of both interpretability and fairness, along with their trade-offs and the underlying reasons, remains underexplored. To address this, we propose a multi-objective neural basis model (MONBM) framework based on multi-objective evolutionary learning to consider accuracy, interpretability, and fairness simultaneously. A partial retraining strategy is further developed to facilitate the practical application of evolutionary multi-objective optimization to deep model architectures. Based on MONBM, this paper reveals the complex relationships between these dimensions and the reasons behind these intricate relationships. This analysis demonstrates how multi-objective optimization can be combined with self-interpretable models to reveal relationships among trustworthiness objectives. In addition, MONBM obtains a set of models with different trade-offs between dimensions, and the competitiveness of the approach is validated by comparing it with state-of-the-art methods.

---


### 66. [Beyond Final Decisions: A Process-Centric Benchmark for Transparent AI-Assisted Peer Review](https://arxiv.org/abs/2609.05947)

**<font color=#1a73e8>作者：</font>** Siming Yuan, Xueyi Zhang, Wangze Ni 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Peer review is central to quality control in science. However, existing evaluations of AI-assisted peer review mainly focus on the overall quality of generated reviews or the accuracy of final decisions. They therefore provide limited evidence about whether model decisions are supported by sufficient and reliable review evidence. We introduce a process-centric diagnostic benchmark for AI-assisted peer review. It uses (x,$z_s$,$z_c$,$z_r$,y)
to represent the paper content, summary, critique, suggestion, and decision. We convert heterogeneous review records from PeerRead, NLPeer ARR-22, and OpenReview-ICLR into process-aligned data. Our benchmark uses direct decision prediction from the paper content (Direct) as its baseline. It compares the decision value of Gold-process variables and Predicted-process variables, and conducts stage-level evaluation, chain-consistency evaluation, and interventional sensitivity analysis. Experiments across three datasets and six models show that Gold-process variables generally have higher decision value. For the main analysis model, the Gold--Predicted gap remains stable across datasets and random seeds. This gap is also reproduced in most model--dataset combinations. Although model-generated intermediate review texts show relatively high local consistency across adjacent stages, the final decisions are not consistently supported by the preceding review evidence. Our benchmark targets AI systems designed to assist rather than replace human reviewers. It provides a transparent and auditable diagnostic tool for evaluating the reliability of their review processes.

---


### 67. [The Blindness of Document-Level Translation Evaluation](https://arxiv.org/abs/2609.05949)

**<font color=#1a73e8>作者：</font>** Ahrii Kim, Vilém Zouhar, Chanjun Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document-level machine translation (MT) evaluation extends segment-level protocols by presenting full documents to annotators, on the assumption that such presentation elicits document-level judgments. We test this assumption with a counterfactual condition (MIX) in which each document combines segments drawn from different systems, preserving document-level presentation while breaking cross-segment consistency. Across 18,420 expert Englis-to-Korean annotations and 14 automatic metrics, scores, system rankings, and error annotations are statistically equivalent between coherent and incoherent documents. Perception does not explain this: shown matched passages, raters identify the coherent one as the work of a single translator in 87.3% of trials. Document presentation does change how annotators work, but that change does not reach the recorded output. What is blind is the protocol, not the annotator. The concern is not that scores fall short, but that the resources invested in document-level systems, metrics, and annotation may not be measuring what they are intended to measure.

---


### 68. [QGB-W$k$NN: Quantum Granular-Ball Learning for Robust Classification](https://arxiv.org/abs/2609.05952)

**<font color=#1a73e8>作者：</font>** Suzhen Yuan, Dehang Chen, Lifeng Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nearest-neighbor classification is widely used in machine learning, yet existing methods often suffer from low computational efficiency and limited robustness in noisy environments. To jointly address these challenges, this paper proposes an efficient and reliable weighted $K$-nearest neighbor classification framework based on quantum granular balls, termed QGB-W$k$NN. The proposed framework improves computational efficiency by integrating quantum-enhanced granular-ball representation with hierarchical nearest-neighbor search, while enhancing classification reliability through a purity-aware weighted decision mechanism. Specifically, quantum-kernel granular balls are constructed to reduce retrieval redundancy and strengthen nonlinear feature representation under limited quantum resources. A granular-ball purity-guided HNSW optimization strategy is developed to exploit structural reliability for hierarchical graph construction during neighbor retrieval, alleviating the local optimality issue caused by conventional random layering. Finally, a weighted voting mechanism jointly incorporating granular-ball similarity and purity is introduced to produce more reliable classification decisions in noisy environments. Extensive experiments on benchmark datasets demonstrate that QGB-W$k$NN achieves competitive classification accuracy while exhibiting favorable Pareto trade-offs between classification performance and computational cost. Moreover, the proposed framework consistently improves robustness under various noisy conditions, suggesting that reliability-aware quantum granular-ball learning provides a promising paradigm for efficient and robust nearest-neighbor classification.

---


### 69. [STP-BENCH: A Unified Systematic Benchmark for Virtual Spatial Transcriptomics from Histopathology Images](https://arxiv.org/abs/2609.05956)

**<font color=#1a73e8>作者：</font>** Youngmin Chung, Ji Hun Ha, Andrew H. Song 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) provides unprecedented insights into tumor heterogeneity by capturing spatially resolved gene expression, yet its high experimental cost hinders large-scale adoption. Consequently, computational approaches that predict spatial gene expression directly from hematoxylin and eosin slides, termed virtual ST, have rapidly emerged. Despite this progress, assessing advances in the field remains difficult due to insufficient benchmarking: prior studies rely on small, heterogeneous datasets, inconsistent training and inference pipelines, and limited evaluation of biological interpretability and model robustness. To address these gaps, we present STP-BENCH, a standardized benchmark for virtual ST models. STP-BENCH comprises six cancer types spanning two ST platforms (Visium and Xenium), with each training dataset containing more than 30,000 spots and at least 15 slides to ensure statistical reliability. We evaluate 21 predictive approaches, re-implemented with a unified pathology foundation model as the morphological encoder when architecturally applicable. Beyond conventional benchmarks that report average predictive accuracy on highly variable genes, we systematically examine which genes and gene sets are recoverable from histomorphology. We further evaluate the downstream biological utility of predicted profiles through cell-type deconvolution and spatial domain identification, and assess model reliability under domain shifts and data scaling. Notably, unified morphological encoding substantially re-orders model rankings established in prior studies, indicating that architectural innovations and image encoding have been conflated in previous evaluations. We publicly release STP-BENCH to support reproducibility and serve as a community benchmark at this https URL.

---


### 70. [On-the-go Forgetting without Explicit Unlearning via ERASE](https://arxiv.org/abs/2609.05966)

**<font color=#1a73e8>作者：</font>** Kushal Chakrabarti, Mayank Baranwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing unlearning approaches typically rely on post hoc weight adaptation or distillation, leading to duplicated memory costs, degraded generalization, and limited scalability. In this work, we introduce ERASE, Erasure via Reconstructive Adversarial Signal Editing, a framework for on-the-go forgetting that suppresses the observable influence of private data without modifying model weights. ERASE leverages structured, class-conditioned input perturbations to induce selective forgetting during inference, eliminating the need for retraining, fine-tuning, or model copies. We rigorously characterize sufficient conditions when ERASE provably achieves functional forgetting of designated subclasses while preserving predictions across other subclasses within the same superclass. This analysis offers a principled foundation for inference-time forgetting under mild regularity assumptions. Across diverse architectures and benchmark datasets, ERASE maintains the best observed balance between forgetting efficacy, computational efficiency, and retention fidelity over recent unlearning-based methods. By reimagining data removal as forgetting without unlearning, our work establishes a scalable, regulation-aligned pathway for continual, privacy-conscious learning.

---


### 71. [Test-Time Weak-to-Strong Alignment: Transferring Implicit Rewards from Weak to Strong Flow Models](https://arxiv.org/abs/2609.05968)

**<font color=#1a73e8>作者：</font>** Xin Xie, Fan Zhang, Dong Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligning a text-to-image generation flow model with a reward makes it follow objectives that the training data alone does not provide. Alignment fine-tuning delivers this by reinforcement learning (RL) or preference optimization, but it must be repeated for every checkpoint and returns a model fixed at the reward and strength it was trained with. Test-time alignment instead steers a frozen model during sampling, allowing task-specific and sample-specific guidance. Existing methods obtain this only by drawing the per-step signal from the reward function itself, through its gradient, or through a separately trained value function. We propose changing the supervision source: let a pair of weak models, not a reward function, supply the supervision. A source aligned model, kept together with its base as a source alignment pair, stores its training reward as an implicit, step-wise, KL-anchored signal expressed in the sampler's own coordinates. We explore whether this model-form supervision can cross scale, and show that it does: our method, AlignGraft, aligns a larger, frozen, never-tuned model by adding the pair's velocity difference during sampling. The transport is exact under a shared noising kernel and needs neither the reward nor its gradient at test time. The method has no schedules, only a single scalar that controls the alignment strength and can extrapolate it beyond that of the source alignment pair. Across image and video flow models (Stable Diffusion 3.5, FLUX, and Wan), the transfer lifts the frozen large model on preference, compositional, and text-rendering rewards, can exceed the source aligned model itself, and preserves the large model's fidelity at a small constant sampling overhead. Extensive experiments show that one alignment run on a weak model produces supervision that the whole model family can reuse at test time.

---


### 72. [Machine Learning for Pre-Culture ESBL Risk Stratification to Guide Empiric Antibiotic Selection: A 12-Hospital Study of Enterobacteriaceae Cultures](https://arxiv.org/abs/2609.05970)

**<font color=#1a73e8>作者：</font>** Aravind V. Kuruvikkattil, Lalitha Pranathi Pulavarthy, Rashmita Kudamala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Empiric antibiotic therapy for suspected ESBL-producing Enterobacteriaceae must be selected 48-72 hours before culture results, forcing clinicians to choose between undertreating resistant infections and overusing carbapenems that drive further resistance. We developed a cost-sensitive XGBoost model predicting an ESBL phenotype (resistance to ceftriaxone, ceftazidime, cefepime or piperacillin-tazobactam) at culture ordering using 45 pre-culture EHR features across 132,955 cultures from 72,217 patients at 12 hospitals (14.41% with the ESBL phenotype). Cultures were partitioned at the patient level. At 90% sensitivity, the model achieved 95.8% NPV, reducing post-test ESBL probability to 4.2%, a threshold that may support safe carbapenem-sparing in non-ICU settings, while sparing 307 of every 1,000 cultures an unnecessary broad-spectrum course at the cost of 14 missed ESBL cases per 1,000. SHAP analysis identified prior ESBL colonization as the dominant predictor, ahead of prior organism burden and neighborhood deprivation; removing deprivation features caused minimal performance loss ($\Delta\text{AUROC} = -0.020$), enabling equitable bedside deployment. Discrimination was unchanged under a strict IDSA ESBL-E definition (AUROC 0.766), with specimen type added as a predictor (0.764) and without any class-imbalance correction (0.762), and ranged from 0.71 to 0.78 across organism strata.

---


### 73. [Efficient and Robust Camera-independent Multiview 3D Geometric Reconstruction from Noisy Monocular Depth Estimation and Multiple Point Matching](https://arxiv.org/abs/2609.05972)

**<font color=#1a73e8>作者：</font>** Marius Leordeanu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present an efficient and robust method for 3D geometric reconstruction that is based solely on the camera-independent linear relationships among a given set of points, which are stable over time and robustly estimated using multiple point matches. We essentially learn, from correspondences between points across several frames, a linear geometric auto-regression matrix $\mathbf{W}$, which establishes how a point in 3D can be expressed as a linear combination of all the others. This matrix is constant and does not depend on the world coordinate system or the camera pose---it is an intrinsic property of the point set. We also show that the principal eigenvectors of $\mathbf{W}$, which all have eigenvalue $1$, provide a homogeneous representation of the 3D point configuration.
The first version of our method takes advantage of noisy monocular depth maps in order to obtain, from multiple frames, a robust geometric auto-regression matrix $\mathbf{W}$ of linear relationships between the 3D points. Thus, we build on recent advances in deep learning, which now provide monocular depth estimation models that are fast but very often noisy. Our approach handles noise through robust linear estimation over several frames.
The second version of our method does not need monocular depth estimation maps. It applies in cases of weak-perspective projection, when the linear combinations between the 3D points can be robustly estimated from their 2D projections in the image.
Note that the camera projection matrix is never used in our derivations. Consequently, our method does not recover camera pose, but only 3D structure. This is a key difference between our method and the related literature on 3D geometric reconstruction.

---


### 74. [MORPHA: Morphology-Constrained Training and the Limits of Cross-Acquisition Transfer in Low-Resource Malaria Microscopy](https://arxiv.org/abs/2609.05990)

**<font color=#1a73e8>作者：</font>** Favour Okechukwu Igwezeke, Chikodili Helen Ugwuishiwu, Joseph Uzochukwu Emesiani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In low-resource malaria microscopy, a model trained on one smear preparation routinely meets images from another, and how well morphology-based constraints transfer across this acquisition gap is unclear. We study this on real African field microscopy from Uganda (Lacuna), asking where encoding measured parasite morphology as a training constraint improves cross-acquisition transfer and where generic regularisation suffices. We present MORPHA, a morphological consistency constraint that derives stage-conditional statistics from the stage-annotated BBBC041 dataset and penalises predictions that deviate from them. Defined uniformly across binary, object-level, and stage-aware regimes without changing architecture or inference, it shapes training in the binary regime. The detection regime is a mapped boundary. On transfer from thin-smear cells to thick-smear field images, the constraint reduces the binary-classification generalisation drop by 30.8% (F1 0.578 to 0.699) at negligible within-domain cost and lowers in-distribution calibration error by 49% (ECE 0.0162 to 0.0082). A content-free control applying the identical constraint to random statistics recovers less of the drop (25.3% vs 30.8%), indicating the measured content, not constraining alone, contributes to the gain. Two standard confidence regularisers exceed the constraint on raw transfer, locating where morphology adds value and where generic regularisation suffices. We map two deployment-relevant boundaries: thin-smear statistics do not transfer to thick-smear detection (trophozoite AP@0.50 falls to 0.000), and cross-acquisition pseudo-labelling fails before filtering applies. Together these yield a morphology-grounded consistency signal and evidence-based guidance for malaria dataset and model design in low-resource settings.

---


### 75. [ModularPhaseNet: Finite-Cyclic Phase Geometry for Computable Semantic Hierarchy, Direction, and Context Consistency in Standard Transformers](https://arxiv.org/abs/2609.06000)

**<font color=#1a73e8>作者：</font>** Kiyotaka Kasubuchi, Kazuo Fukiya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose ModularPhaseNet, a classical and integer-computable discretization of the continuous complex phase geometry introduced in QuantumPhaseNet. The real-valued hidden states of a standard Transformer are retained, while only an auxiliary phase channel is quantized into a cyclic subgroup G = <g> of order q | (p-1) in the multiplicative group of F_p. A continuous phase e^{i phi} is represented by z = g^a mod p; phase composition becomes group multiplication, relative phase becomes group division, conceptual hierarchy is induced by a filtration of cyclic quotients, semantic direction is represented by oriented relative group elements, and contextual consistency is measured by gauge-invariant cycle holonomy. The method introduces three components into an otherwise standard Transformer: a finite-phase encoder, a quotient-filtration hierarchy module, and a group-valued connection module. Their outputs enter self-attention as real-valued bias terms. Training uses distributions in the real group algebra or straight-through Gumbel-Softmax, whereas inference uses exact modular exponentiation and precomputed tables. No quantum hardware, complex-valued matrix multiplication, or discrete-logarithm computation is required. We prove quantization-distortion bounds, nesting of quotient-induced partitions, gauge invariance, a discrete integrability result for flat connections, and boundedness of the resulting attention output. The central empirical hypothesis is that these exact discrete invariants improve hierarchy recovery, discourse alignment, contradiction detection, and calibrated hallucination-risk prediction under a controlled compute budget. This paper reports the theory together with a pre-registered evaluation plan; the experiments described in Section 14 have not yet been carried out, and no empirical result is claimed here.

---


### 76. [Depth-to-Image Synthesis-Driven Generative Unguided Depth Completion](https://arxiv.org/abs/2609.06007)

**<font color=#1a73e8>作者：</font>** Jiayi Yuan, Na Zhao, De Wen Soh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Guided depth completion methods heavily depend on RGB quality and alignment, while unguided ones often suffer from limited precision due to the absence of explicit visual cues. In this paper, we present Depth-to-Image Synthesis-Driven Generative Unguided Depth Completion (GUDC), a new completion paradigm that innovatively bridges advanced 2D generative models with unguided depth completion, enabling semantics-aware depth inference without real RGB inputs. Our key idea is to exploit ControlNet's powerful depth-conditioned generation capability to synthesize pseudo-images directly from sparse depth, effectively converting the original unguided setting into a semantics-guided one. To address the potential image-depth misalignment caused by depth sparsity, we propose a multi-level dense-to-sparse representation distillation strategy for ControlNet fine-tuning, where dense-depth features act as teacher signals to distill consistent structural representations for sparse-depth inputs. Furthermore, during pseudo-image-guided completion, we propose a pseudo-image semantic attention fusion module to adaptively extract informative semantic cues from pseudo-images while suppressing artifacts (e.g., texture hallucinations). Extensive experiments on KITTI and NYUv2 validate that our GUDC achieves superior accuracy and robustness over existing methods.

---


### 77. [Robustness Evaluation and Detection of Transferable Adversarial Attacks in ML-Based NIDS](https://arxiv.org/abs/2609.06012)

**<font color=#1a73e8>作者：</font>** Huda Ali Alatawi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based network intrusion detection systems (ML-based NIDS) are vulnerable to adversarial evasion, where malicious samples are perturbed to evade detection and be misclassified as benign. Despite growing research on adversarial attacks and defenses for ML-based NIDS, comparative evaluations of multiple attack types, detection models, and defense strategies under a common setting remain limited. In this paper, we evaluate eight adversarial evasion attacks, fifteen detection models, and three representative defense strategies using the NF-UQ-NIDS dataset, which includes recent traditional and IoT network traffic with twenty distinct attack categories. The evaluation compares model performance on clean test data and on robustness evaluation sets that include adversarial samples, analyzes attack success consistency across models, and examines the effect of defense strategies on adversarial robustness. To support model comparison, we introduce the Robustness Index (RI), a compact comparative metric that rewards high balanced accuracy and macro-F1 score computed on the robustness evaluation set while penalizing high attack success rate (ASR). We further present AR-NIDS, a two-stage framework that uses an adversarially trained ensemble to distinguish normal, attack, and adversarial samples, followed by an adversarial attack classifier to identify the attack type. Under the evaluated transfer-based setting, the proposed adversarially trained ensemble achieves the strongest overall trade-off between classification performance on the robustness evaluation set and evasion resistance, reducing the average ASR from 0.41 to 0.03 and achieving an RI of 0.98.

---


### 78. [Granular-Ball Quantum Clustering for Resource-Efficient and Robust Learning](https://arxiv.org/abs/2609.06016)

**<font color=#1a73e8>作者：</font>** Suzhen Yuan, Qilin Xie, Lifeng Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum clustering aims to exploit quantum feature representations to uncover complex data structures beyond conventional Euclidean geometry. Yet this sample-level kernel construction requires O(n^2) quantum circuit executions for n data points, creating a major bottleneck under near-term quantum resource constraints. Prior solutions fail to resolve this efficiency-accuracy dilemma: classical granular-ball clustering reduces sample complexity but relies on Euclidean metrics that cannot capture quantum correlations, while existing quantum compression schemes prioritize efficiency over structural preservation, degrading performance on non-convex or noisy data. Here we propose Granular-Ball Quantum Clustering (GBQC), a framework that tightly couples granular-ball structural abstraction with quantum feature learning. GBQC first compresses raw data into compact, representative granular balls via a PCA-guided splitting strategy, reducing kernel evaluations by 80% compared to full-sample methods. A quantum cohesion mechanism then filters noisy granules in Hilbert space to improve clustering robustness. Extensive experiments on synthetic, noisy, overlapping, and real-world datasets demonstrate that GBQC consistently achieves superior clustering accuracy and robustness compared with representative classical and quantum clustering methods. Meanwhile, the proposed granular-ball compression significantly reduces quantum kernel evaluations and computational overhead, enabling quantum clustering experiments on larger datasets within parameterized quantum learning frameworks. These results suggest that granular-ball representations serve not only as a compression mechanism to reduce quantum computational costs but also as an effective structural abstraction mechanism that improves clustering quality by eliminating redundant and structurally ambiguous learning units.

---


### 79. [FujinSplat: Seeing Through Smoke with RAW-Domain Gaussian Splatting](https://arxiv.org/abs/2609.06017)

**<font color=#1a73e8>作者：</font>** Gengjia Chang, Ziteng Cui, Shuhong Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The appearance of a smoky scene is shaped by two processes that a camera records together: the participating medium alters scene radiance in a view-dependent way, and the image signal processor (ISP) then remaps the result through a nonlinear tone and color transformation. Recovering a clean 3D scene requires separating both. Per-view sRGB dehazing acts only after the ISP has entangled them; standard 3D reconstruction ignores the medium and absorbs it into scene geometry and radiance. FujinSplat addresses the problem in the RAW domain, where the two processes remain separable. A per-scene Base ISP is fitted from the scene's hazy RAW captures to its own camera renderings and then frozen, providing a fixed photometric anchor that performs no dehazing. Analyzing expert corrections reveals a compact, low-dimensional correction space identifiable from RAW alone. FujinSplat therefore fits per-view action answers at the training poses and trains a single scene-agnostic controller to regress them from RAW; the corrected views supervise one static 3D Gaussian representation, jointly with a bounded per-view residual that reconciles cross-view photometric inconsistencies. On the RealX3D real-world smoke benchmark FujinSplat clearly outperforms the strongest comparable baseline, ahead of both physics-based reconstruction and restoration-then-3DGS pipelines.

---


### 80. [IXPLORE: Bounded Ideal Point Estimation with Grid-Based Uncertainty Quantification](https://arxiv.org/abs/2609.06018)

**<font color=#1a73e8>作者：</font>** Fynn Bachmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ideal point estimation is widely used to analyze and visualize political data. However, selecting the corresponding spatial model involves various trade-offs: while model-based approaches such as Item Response Theory (IRT) are based on utility functions rather than optimized for predictive accuracy, most Machine Learning (ML) alternatives struggle to generalize beyond training data when embedding sparse test responses. We introduce IXPLORE, a bounded ideal point estimation algorithm that combines a predictive fit objective with a sparsity-aware likelihood function. On five benchmark datasets spanning surveys, roll calls, and deliberation, this approach surpasses model-based and ML-based algorithms on reconstruction and imputation error - especially for users with sparse responses. Furthermore, we show that non-linear feature transforms can further reduce the reconstruction error while remaining visually interpretable. To quantify uncertainty, IXPLORE applies grid-based posterior inference on a bounded 2D latent space. Available as a Python package on PyPI, IXPLORE offers a flexible framework for constructing bounded, interpretable political maps with fast inference and strong imputation performance.

---


### 81. [What Does Animal Re-Identification Learn? Linear Biological Concepts and Their Origins in Visual Representations](https://arxiv.org/abs/2609.06020)

**<font color=#1a73e8>作者：</font>** Robert Nolting, Alexandra Schild, Moritz Weckbecker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conservation increasingly relies on camera traps that collect more wildlife imagery than experts can manually analyze, making animal re-identification (Re-ID) essential for monitoring individuals and populations. Yet understanding which cues drive model decisions is challenging for ViT-based Re-ID models, whose metric-learning objectives provide no explicit supervision for biological concepts. We ask whether such models nonetheless organize their representations along biologically meaningful axes. Using a DINOv3 backbone fine-tuned for Western lowland gorilla Re-ID with triplet-margin loss, we find that sex and age emerge as linear directions that generalize to held-out individuals, reaching up to 0.91 AUROC and being recoverable from a single image per individual. Activation steering further shows that the sex direction is causally used by the model, flipping a significant fraction of predictions to the opposite sex. Comparing off-the-shelf and fine-tuned backbones shows that Re-ID training does not create these concepts, but relocates them across the network. Finally, data attribution reveals that the representation we find reflects a graded biological axis, is redundantly encoded across the population and shaped by visually ambiguous individuals. Together, these findings show how interpretability can uncover both the biological structure and failure modes of Re-ID representations, providing a step toward auditable computer vision for wildlife monitoring.

---


### 82. [Factors Influencing the Emergence of Dependency Length Minimization in Neural Agent Simulations](https://arxiv.org/abs/2609.06025)

**<font color=#1a73e8>作者：</font>** Yuqing Zhang, Tessa Verhoef, Gertjan van Noord 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Given various grammatical options, language users prefer the word order choice that reduces the overall length of syntactic dependencies, a principle known as dependency length minimization (DLM). The origins of this preference remain an open question, particularly whether it originates from constraints on efficient information processing. Computational simulations provide a powerful approach to identifying the factors influencing the emergence of linguistic phenomena. However, previous simulations of DLM have not examined realistic interaction contexts and have produced mixed results. The present study investigates the emergence of DLM in artificial languages using a recently proposed language learning and communication framework based on recurrent neural networks (RNNs). In this framework, agents are trained to speak and interpret artificial languages and then use these languages to communicate. Using this framework, we study the impact of several factors related to processing limitations in a communicative setting, such as noise during listening, limited speaker capacity, and incremental sentence processing. Our results reveal a complex interplay among these factors in shaping word order preferences in neural agents. Specifically, in the full meaning space, agents regularize toward a single dominant word order, while in the half meaning space they show a short-before-long preference that only aligns with DLM in verb-initial languages. A consistent DLM preference emerges only when agents are subject to incremental processing pressure. These findings suggest that limitations in human cognitive processing may indeed play a role in shaping DLM. Our findings provide insights into the conditions under which neural models replicate human-like preferences and highlight the challenges of designing emergent communication models that capture human cognitive biases in language processing.

---


### 83. [Minimizing the Effect of Sleep Deprivation in the Forward-Forward Algorithm](https://arxiv.org/abs/2609.06042)

**<font color=#1a73e8>作者：</font>** Joy Datta, Puja Saha, Rawhatur Rabbi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper addresses the challenge posed by sleep deprivation in the Forward-Forward algorithm, where separating the two passes in this algorithm and imbalancing the data processing in the passes is considered an imitation of the cognitive processes observed in humans suffering from sleep deprivation. Previous research has demonstrated that sleep deprivation in the Forward-Forward algorithm has a catastrophic effect on learning efficacy. To mitigate this issue, we explore several approaches; these include alternative activation, optimized loss function, and threshold tuning. To simulate periodic rest, we reduce the number of positive passes in alternating epochs, creating short break phases. We additionally investigate the potential of caffeine-induced stimulation to enhance performance during sleep-deprived conditions. Experimental evaluations conducted on the MNIST and Fashion-MNIST datasets demonstrate that these modifications improve accuracy under the context of sleep deprivation. For example, a 2%-62% accuracy gain is observed in a severe sleep deprivation setting (16 positive or awake periods and 1 negative or sleep period). The approaches also enhance the resilience of the algorithm and its alignment with the adaptive mechanisms of human cognition.

---


### 84. [Art2Song: Enhancing Visual Art Appreciation with Contextual Music Generation](https://arxiv.org/abs/2609.06044)

**<font color=#1a73e8>作者：</font>** Sungeun Jo, Myung Jin, Chi Yoon Jeong  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Art2Song is a conceptual framework that expresses artworks as sound by separating Non-Visual Context, which is difficult to perceive from the image alone, from Visual Evidence. Visual Evidence, such as objects, colors, and spatial composition, is transformed into Lyrics, while the Contextual Mood derived from the historical and art-historical context in the museum's artwork description is reflected in the background soundtrack. Rather than describing artworks textually, Art2Song aims to explore the possibility of a new mode of art appreciation in which viewers experience hidden stories and emotional context through music. As future interaction directions, we plan an Emotional Layer Blending Slider interface and a structured, traceable song-generation scenario, presenting the possibility that users can explore the relationship between Visual Evidence and Contextual Mood.

---


### 85. [Image-Scale Robustness and Visual Recognition Performance: A Cross-Architecture Analysis](https://arxiv.org/abs/2609.06051)

**<font color=#1a73e8>作者：</font>** Anish Monsley Kirupakaran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The sensitivity of visual recognition models to changes in image scale is well established, yet the factors governing this sensitivity across heterogeneous architectures remain unclear. In this work, we investigate whether scale robustness exhibits a common quantitative structure across modern vision models. We evaluate 20 pretrained ImageNet-1K classifiers spanning seven architectural families, including convolutional, mobile, efficient, and Transformer-based architectures. By systematically reducing input image scale, we construct scale-accuracy response curves and define a characteristic scale as a compact measure of the onset of substantial recognition degradation. We then examine the relationship between characteristic scale and baseline recognition accuracy, model parameter count, architectural family, and representation stability. A strong inverse association is observed between baseline accuracy and characteristic scale (Pearson r = -0.890, R^2= 0.792, p < 10^-6). This relationship remains stable under bootstrap resampling, leave-one-architecture-out analysis, and leave-one-family-out analysis. In contrast, parameter count provides negligible additional explanatory power after controlling for baseline accuracy (p = 0.80), while architectural family does not provide significant incremental explanatory power. Furthermore, characteristic scale shows essentially no association with representation stability (r = -0.003, p = 0.991). These results indicate that, across the studied models, scale robustness is strongly organized by baseline recognition performance rather than simply by model size, architectural family, or representation stability. The study provides an empirical framework for characterizing scale robustness across vision architectures and identifies a reproducible accuracy-scale regularity that warrants further theoretical investigation.

---


### 86. [DriveZero: End-to-End Driving Beyond Human Demonstrations](https://arxiv.org/abs/2609.06055)

**<font color=#1a73e8>作者：</font>** Hao He, Chengcheng Hu, Zirun Su 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most end-to-end autonomous-driving systems learn by imitating human driving logs, leaving their learned behavior constrained by the quality and behavioral coverage of the recorded trajectories. This report presents DriveZero, an end-to-end system that learns driving behavior beyond human demonstrations. It decomposes driving into a perception model and an action model, pretrains each in the regime best suited to it, and combines them into one end-to-end planner. The two models call for different learning recipes: perception must understand the world, and benefits from massive and diverse visual data; action must interact with it, and requires closed-loop feedback. On the action side, we introduce DriveRL, a mixed-agent closed-loop reinforcement-learning framework. It converts real driving logs into interactive worlds, where a privileged teacher policy is trained with PPO through closed-loop rollouts. For the perception model, DriveVFM consolidates multiple frozen vision foundation models, including DINOv3, SigLIP2, SAM and Depth Anything V2, into a single backbone from raw images alone, requiring no task-specific annotations. DriveZero then unifies the two: a camera-only planner that distills the frozen DriveRL teacher through its rolled-out trajectories. The goal-conditioned teacher can moreover be queried under augmented driving intents, yielding diverse, goal-consistent supervision that logged data cannot provide. On nuPlan, DriveRL with value-guided test-time action search achieves a mean score of 93.57 across the Val14, Test14-hard, and Test14-random community splits in both non-reactive and reactive modes, exceeding the Log-Replay expert on all three splits. DriveZero achieves state-of-the-art performance on NAVSIMv1, NAVSIMv2 and the closed-loop HUGSIM benchmark without any human trajectory supervision.

---


### 87. [Calendar-SPCA: Interpretable Representation Learning for Multi-Periodic Electricity Consumption Profiles](https://arxiv.org/abs/2609.06060)

**<font color=#1a73e8>作者：</font>** Carlos Quesada-Granja, Tony Castillo-Calzadilla, Carlos Rizo-Maestre  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term electricity-consumption profiles exhibit several simultaneous periodic structures, including daily, weekly, and annual cycles. This work introduces Calendar-SPCA, a calendar-structured sparse principal component method that incorporates this known multi-periodic geometry directly into low-dimensional representation learning. The feature domain is represented as the Cartesian product of cyclic calendar axes, and a low-rank factorization is estimated using an L1 loading penalty together with graph total variation over the resulting calendar graph. The method therefore produces sparse and locally coherent loading patterns that remain directly readable in their original temporal coordinates. Calendar-SPCA is evaluated on two independent smart-meter datasets with different sample sizes and temporal resolutions: GoiEner and Low Carbon London. A factorial experiment characterizes the complementary effects of sparsity and calendar coherence and examines robustness across sample size, latent dimensionality, and repeated fits. At rank 15, Calendar-SPCA retains 96.92% and 82.90% of the explained variance of rank-matched PCA in GoiEner and Low Carbon London, respectively, while producing mean loading sparsities of 61.95% and 81.50%. Comparisons with classical sparse PCA and SPCA-TV further show that Calendar-SPCA adds a systematic organization of the latent factors in the original calendar coordinates while preserving substantial low-rank information. The resulting components form coherent and complementary daily, weekly, seasonal, and jointly localized calendar patterns, with dataset-specific geometries across the two datasets.

---


### 88. [DPH Parser: A Bottom-Up Grammar-Driven Parser for Joint Constituency and Dependency Analysis](https://arxiv.org/abs/2609.06070)

**<font color=#1a73e8>作者：</font>** Hussein Ghaly  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents Dependency-Phrase Hierarchy Parser (DPH Parser), a grammar-driven bottom-up unsupervized parsing framework inspired by Generalized Phrase Structure Grammar (GPSG) and Head-driven Phrase Structure Grammar (HPSG). The parser incrementally constructs constituency structures using a compact inventory of feature-based syntactic rules while deriving dependency relations through explicit head annotations. The system combines probabilistic POS tagging, recursive phrase projection, and weighted parse hypotheses to process realistic and partially noisy text input. Unlike purely neural and data-driven parsers, the resulting syntactic derivations remain explicitly interpretable.
We evaluated parser performance on English corpora from the Universal Dependencies (UD) project using Unlabeled Attachment Score (UAS) as the main parsing metric, comparing the outcomes against Stanza and spaCy parsers. For a small inventory of syntactic rules, DPH parser achieved UAS values of 53.32% & 52.58% (UD Devset/Testset respectively). For the same data, Stanza achieved 89.12% & 88.67% while spaCy achieved 56.91% and 58.59%. Although the current system does not yet approach the accuracy of modern neural parsers, the results demonstrate the feasibility of applying transparent rule-based bottom-up parsing to realistic treebank data while jointly producing constituency and dependency structures.

---


### 89. [NSFlow: End-to-End Differentiable Neuro-Symbolic Optical Flow for Visual Odometry](https://arxiv.org/abs/2609.06074)

**<font color=#1a73e8>作者：</font>** Yicheng Lin, Yuxiu Xu, WenDong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse optical flow provides stable inter-frame correspondence, playing a key role in Visual Odometry (VO) and Visual-Inertial Odometry (VIO). Classical optimization-based methods, such as Lucas-Kanade (LK), perform well under small displacements but are sensitive to large motions and illumination changes. Modern regression-based learning methods, while more robust in complex scenes, are often computationally heavy and lack explicit geometric consistency, making them less suitable for efficient VO/VIO front-ends. To bridge this gap, we propose a hybrid neuro-symbolic framework that combines the strengths of both paradigms. Our method uses a Convolutional Neural Network (CNN) to extract robust feature representations, which is fed into a differentiable LK optimizer to estimate optical flow in an end-to-end trainable manner. Through implicit differentiation, gradients are propagated across the iterative solver, enabling joint optimization of feature extraction and flow estimation. The resulting system integrates seamlessly into existing VO/VIO pipelines and runs in real-time on embedded platforms. Experiments show that our method outperforms conventional optimization-based flow in challenging conditions such as dynamic lighting and low texture, while also achieving higher accuracy and lower latency than purely regression-based alternatives. When deployed in a VIO system, our method demonstrates significant performance improvement, achieving an average error reduction of 42\% on challenging datasets while enhancing tracking stability. The code is publicly available.

---


### 90. [Report of the 8th LSVOS Challenge: Complex and Multimodal Video Object Segmentation](https://arxiv.org/abs/2609.06078)

**<font color=#1a73e8>作者：</font>** Chang Liu, Henghui Ding, Lingyi Hong 等 39 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report summarizes the 8th Large-scale Video Object Segmentation (LSVOS) Challenge, held in conjunction with ECCV 2026. The challenge evaluates video segmentation in three complementary settings: complex semi-supervised video object segmentation on MOSEv2, text-guided referring video object segmentation on MeViSv2-Text, and audio-guided referring video object segmentation on MeViSv2-Audio. We describe the tasks and evaluation protocols and review the methods of the top three teams in each track. Across the nine leading solutions, foundation segmentation models are combined with target-aware memory, multimodal reasoning, explicit target-existence verification, agentic interaction, and corrective tracking. These systems illustrate a broader transition from single-model mask propagation toward modular pipelines that reason about object identity, query validity, and temporal reliability.

---


### 91. [Learning to Price and Stock Under Contextual and Censored Demand](https://arxiv.org/abs/2609.06083)

**<font color=#1a73e8>作者：</font>** Zean Han, Zezhen Ding, Jiheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To make optimal joint pricing and inventory control decisions is a critical challenge for modern retailers. In practice, retailers face changing market conditions where demands are influenced by various contextual factors, while simultaneously dealing with the difficulty of lost sales that obscure true demand information. However, existing approaches often fail to account for both contextual information and censored demand observations. We address this gap by presenting a framework where we model demand as a linear combination of basis functions with unknown coefficients, allowing for adaptive pricing and inventory decisions that respond to changing contexts. We propose an efficient algorithm to achieve regret bound $\mathcal{O}(K\sqrt{T}\log T)$ under concave revenue conditions and $\mathcal{O}(K^{2/3}T^{2/3}(\log T)^{1/2})$ for the general case, with matching lower bounds confirming optimality. Extensive numerical experiments across diverse scenarios demonstrate our algorithm's effectiveness.

---


### 92. [Connectome-to-Function: Conditional Generative Latent Representations for Reservoir Computing](https://arxiv.org/abs/2609.06093)

**<font color=#1a73e8>作者：</font>** Zhuolin Yu, Xingyu Liu, Yuanhao Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Connectomes, graph-level maps of neurons and their synaptic connections, provide a structural basis for understanding how brain circuits support function and computation. However, mapping connectome structure to computation remains difficult because these graphs are high-dimensional, sparse, and sensitive to local structural variation. Existing approaches often depend on hand-crafted structural descriptors or task-specific predictors, which limits their ability to represent connectomes in a form that is both generative and functionally meaningful. We propose a conditional generative latent framework that encodes connectome graphs into a compact structural space while using available node-level conditions to guide reconstruction and generation. From this space, the model can reconstruct observed connectivity with a mean edge-reconstruction AUC up to 0.910 and generate new candidate connectomes, enabling a unified analysis of graph structure and computational behavior. Using connectome-derived graphs as recurrent computational substrates, we found that the learned latent space captures functional variation across reservoir-computing experiments, with cross-validated $R^2$ values up to approximately 0.87. Interpretability analysis further revealed task-specific structural mechanisms: in our examples, memory performance is associated with reciprocal recurrent connectivity, whereas prediction and classification are more strongly associated with spectral properties of the recurrent network. These findings suggest an AI-for-science approach to linking neural connectivity to computation and provide a generative and interpretable basis for studying how distinct structural mechanisms shape computational capacity.

---


### 93. [Automatic Red Teaming for Implicit Vulnerabilities of Text-to-Image Models](https://arxiv.org/abs/2609.06094)

**<font color=#1a73e8>作者：</font>** Chang Ma, Junlin Han, Shuo Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Red-teaming Text-to-Image (T2I) models is essential for safe deployment, yet it remains particularly challenging against implicit adversarial prompts. Unlike explicit adversarial prompts that can be readily identified and blocked, implicit ones are much harder to detect: the prompts appear benign on the text surface yet still lead to inappropriate visual content. To address this, we propose Adversarial Probing for Implicit VulnErabilities (AdvPIE), a multimodal agentic framework to expose implicit vulnerabilities without requiring access to the parameters of target models. AdvPIE adopts a policy agent to generate and refine implicit adversarial prompts based on the feedback from a judge agent. To construct informative feedback, the judge agent provides modality-specific safety evaluation at both global and relative levels across iterations. To effectively leverage the feedback, we propose a novel Cumulative Adversarial Decoding strategy for the policy agent, which dynamically reweights token distributions to favor tokens that lead to more harmful images while preserving sampling diversity. Extensive experiments on standard and safety-aligned T2I models show that AdvPIE1 effectively uncovers implicit vulnerabilities, outperforming various baseline methods.

---


### 94. [PASTEL: Panoramic Alignment for Monocular 4D Scene Reconstruction](https://arxiv.org/abs/2609.06099)

**<font color=#1a73e8>作者：</font>** Yuankun Yang, Yi Wei, Bo Bai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 4D scenes from casually captured monocular video is vital for applications in virtual reality (VR) and embodied AI. Recent advances in 4D reconstruction and novel view synthesis have substantially propelled this capability. However, existing reconstruction methods generally cannot recover regions beyond visible camera limits. Consequently, we introduce a new paradigm that achieves 4D scene synthesis by combining visible-region reconstruction from monocular input with invisible-region generation beyond observable camera boundaries. We present Panoramic Alignment for Strategic Exploitation of Generative Priors (PASTEL). Specifically, PASTEL proposes panoramic scene alignment, a novel representation that reformulates the intractable 3D "invisible region" exploration into a tractable 2D directional trajectory planning. This is achieved by reducing the viewpoint planning from 6-DoF search to a 2D directional search with explicit visibility boundaries. By operating within this panoramic space, our method strategically identifies camera trajectories that maximize exploration beyond observable boundaries while minimizing viewpoint deviation. Experimental results show that PASTEL can not only extrapolate plausible scene content beyond the observable boundaries of input monocular videos, but also substantially boost monocular 4D reconstruction performance. PASTEL outperforms the previous state-of-the-art method by 0.9dB in full-image PSNR on the DyCheck IPhone dataset.

---


### 95. [Beyond the Prank: The Hidden Expertise of TSS Scambaiters](https://arxiv.org/abs/2609.06103)

**<font color=#1a73e8>作者：</font>** Saleh Alsyefi, Anish Chand, Matthew Edwards 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This research studies how Technical Support Scams (TSS) are being countered by a uniquely dedicated community of volunteer counter-fraud operatives. Using a careful subject selection strategy, we interviewed 17 individuals who actively engage in TSS scambaiting activities in order to obtain insight into their motivations, the operational methods of the scammers they combat, the undocumented nuances of effective scambaiting action, and the various challenges scambaiters face. In our analysis, we find a community rich not only with insight into offenders, but with technical and operational expertise that is often lacking in research efforts targeting these same populations. At the same time, we find key areas where the community could be better supported and enabled. We discuss the implications of our findings for both future research and community protection strategies.

---


### 96. [FANS: Federated Adaptive Network Search Learning for Heterogeneous Devices](https://arxiv.org/abs/2609.06106)

**<font color=#1a73e8>作者：</font>** Jiaxin Zhang, Xingwei Wang, Bo Yi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous Federated Learning (HFL) aims to train models across devices with diverse resource budgets while preserving data privacy. Existing HFL methods typically bind training to a small predefined menu of model configurations, which limits architectural coverage. To address this bottleneck, we introduce Federated Adaptive Network Search (FANS), a hypernetwork-based framework that learns a shared architecture space rather than a fixed set of client models. To optimize this shared space efficiently, we propose the Federated Parallel Scaling (FPS) algorithm, which jointly trains multiple sampled subnetworks in parallel with self-distillation so that larger sampled subnetworks can supervise smaller ones during local updates. We evaluate FANS on CIFAR-10, CIFAR-100, and MNLI using ResNet-18, DenseNet-121, and BERT-base, respectively. Across all benchmarks, FANS expands the feasible subnetwork pool by orders of magnitude (e.g., 4,680 candidates for ResNet-18 vs. 4 in existing methods) and improves the average accuracy-efficiency trade-off relative to representative HFL baselines. Device heterogeneity is emulated through resource tiers, and evaluation covers accuracy, parameter count, and MACs.

---


### 97. [From Two Passes to One: Compact and Efficient Target-Stance Extraction](https://arxiv.org/abs/2609.06108)

**<font color=#1a73e8>作者：</font>** Ethan Mines, Bonnie Dorr  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Target-Stance Extraction (TSE) is the task of predicting both the target (or topic) of an author's writing and the author's stance toward it. Existing approaches to TSE use a sequential pipeline of two separate neural models: one to identify the target and another to determine the stance. We present a one-pass, joint architecture that predicts both in a single forward pass, reducing trainable parameters by nearly 50% with only a 4-7 F1 point tradeoff in performance. We further demonstrate that standard target-scrubbing practices artificially suppress target prediction accuracy. Retaining explicit target mentions, as in real-world deployments, improves F1 by at least 6 points across both target classification and target generation settings. These improvements allow for significantly easier integration of TSE in downstream applications such as public opinion tracking.

---


### 98. [Sparse Incident-Cluster Learning for 12-hour Port Flood Pre-warning in Digital-Twin Analytics](https://arxiv.org/abs/2609.06109)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Qiang Ni, David Windridge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Port flood digital twins require analytics that warn operators before disruption, but official warning incidents are often few and adjacent observations are temporally dependent. Row-level classification can therefore overstate performance by placing windows from the same event in both model-development and evaluation data. We formulate 12-hour port flood pre-warning as an incident-cluster learning problem and evaluate a digital-twin analytics module using eight-point water-level histories, prediction-time contextual covariates, and interpretable short-window dynamics. The protocol combines fold-specific sparse feature selection, warning-cluster grouping, negative-label controls, 100-repeat random top-k controls, and alert-episode evaluation. Liverpool is the primary four-cluster case study, with harmonised Humber/Hull-proxy and Wessex South data used for protocol-transfer checks. Across the Liverpool folds, the top-10 ElasticNet model achieves mean F2 = 0.696, compared with 0.633 without top-k truncation and 0.681 for full-feature weighted XGBoost. It is the strongest ElasticNet variant, remains competitive with the nonlinear reference using only ten predictors, and exceeds the repeat-level 95th percentile of broad and same-family random subsets. Contextual covariates provide a strong prediction-time anchor, complemented by physically interpretable local dynamics. Historical replay converts risk scores into alert episodes and measures alert duration and false-episode burden. The result is an offline-evaluated analytics and validation module designed for integration into a port digital twin.

---


### 99. [SAP: State-Guided Data Synthesis with Argument Provenance for Multi-Turn Tool Use](https://arxiv.org/abs/2609.06124)

**<font color=#1a73e8>作者：</font>** Zichen Tian, Jinpeng Chen, Cheng Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-quality multi-turn tool-use data is essential for training agentic models, yet existing data synthesis methods often underrepresent the argument-level dependencies that are critical to long-horizon tool use. As a result, even when a model selects the correct tool, task execution may still fail because the model fills tool arguments with fabricated, stale, or weakly grounded values. To address this problem, we propose \textbf{State-Guided Data Synthesis with Argument Provenance (SAP)}. SAP combines state guidance, tool-argument provenance constraints, and turn-level validation to efficiently construct tool-use trajectories with long-range dependencies and high accuracy. Using data generated by SAP, we build SAP-4B, which is highly competitive even when compared with much larger models across multiple benchmarks. Source code, synthesized data, and trained weights are available at this https URL.

---


### 100. [IIns-VAE+: A Robust Transfer Learning Framework for Environmental Identification in Wireless Sensing](https://arxiv.org/abs/2609.06131)

**<font color=#1a73e8>作者：</font>** Yuxiao Li, Keke Hu, Bobai Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Environmental identification in wireless sensing is essential for 6G integrated sensing and communication (ISAC) systems to achieve reliable situational awareness. However, deep learning (DL) models for this task often fail to generalize under domain shift across diverse environments. While the Inter-Instance Variational Auto-encoder (IIns-VAE) learns features of rich representation, its neural classifier remains vulnerable to these distribution changes. In this paper, we propose IIns-VAE+, a hybrid model that combines the IIns-VAE framework with Minimax Risk Classifiers (MRC) to improve adaptability in transfer learning scenarios. We use real-world datasets to evaluate our framework across three transfer learning scenarios, including general to specific room environments, high to low label resolutions, and mixed to specific environments. The experimental results indicate that IIns-VAE+ significantly outperforms baselines, demonstrating its critical value in building adaptable and robust perceptive networks in future 6G systems.

---


> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
