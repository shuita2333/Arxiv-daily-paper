# 📦 其他研究 | 2026年11月26日

> 本类共 **342** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-342**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-342**

---

### 301. [Motion Conditioned World Modeling for Embodied Visual Tracking](https://arxiv.org/abs/2611.32900)

**<font color=#1a73e8>作者：</font>** Jiahao Zhang, Xuan Yao, Junyu Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models support embodied decision-making by predicting future environment states. In embodied visual tracking, uncertain target motion and robot-induced viewpoint changes jointly affect visual observations, making future-state prediction challenging. We propose Motion-Conditioned World Modeling, which incorporates predicted target-motion distributions and robot ego-motion into latent state transitions. A Geometry--Progress module jointly models geometric paths and single-step travel distances through shared motion modes and path-conditioned progress distributions. This formulation captures uncertainty in route selection and motion progress while preserving their dependence. Action-induced coordinate transformations express predicted paths in the next robot frame, providing geometrically grounded conditions for future visual-state prediction. Future visual feature reconstruction supervises the motion predictor through the conditioned transition branch, linking explicit motion representations to subsequent observations. The model is jointly optimized with motion likelihood, feature reconstruction, and expert-action supervision, enabling the tracking policy to combine visual context with predictive motion this http URL on three embodied tracking benchmarks demonstrate improved tracking performance and cross-environment generalization with a lightweight $0.5$B backbone.

---


### 302. [IMPACT-Seg: Consistent Anatomical Segmentation and Representation Learning Across CT, CBCT, and MRI](https://arxiv.org/abs/2611.32903)

**<font color=#1a73e8>作者：</font>** Cédric Hémon, Valentin Boussot, Matthew McCormick 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT), cone-beam CT (CBCT), and magnetic resonance imaging (MRI) provide complementary representations of the same underlying anatomy, yet substantial differences in image appearance challenge consistent segmentation and deformable registration in adaptive radiotherapy. We investigate whether dense anatomical segmentation supervision can promote cross-modality correspondence without explicit feature alignment. We introduce IMPACT-Seg, which segments 126 structures across CT, CBCT, and MRI using shared network parameters. A collection of 8,290 volumes was assembled from public cohorts through label harmonization, model-assisted pseudo-label completion, iterative refinement, and 2,864 physics-based CBCT simulations with voxel-aligned CT labels. Unpaired images were used to jointly train 2.5D and 3D residual-encoder networks.
On 139 real CBCTs, IMPACT-Seg 3D achieved a mean Dice of 0.842 versus 0.671 for the strongest comparator. On 497 voxel-aligned CT-simulated-CBCT pairs, the CT-to-CBCT Dice decrease was 0.022 versus 0.153-0.178 for competing methods. On independent pancreatic radiotherapy CBCTs, gastrointestinal Dice was 0.735 versus 0.634 for TotalSegmentator. Prediction agreement reached 0.881 on registered CT-CBCT and 0.790 on CT-MRI pairs. Adding MRI training data reduced CT-MRI encoder feature retrieval error from 36.8 to 3.2 mm. Registration pipelines incorporating IMPACT-Seg features ranked first on two multimodal Learn2Reg benchmarks. The 3D model segmented a whole-body CT in 15 s.
These findings show that dense anatomical segmentation supervision can support consistent anatomical representations across modalities, with applications to both segmentation and registration. Code, datasets, and pretrained models are available at this https URL.

---


### 303. [Reading Decisions Before Spans: Efficient Generative Verification](https://arxiv.org/abs/2611.32931)

**<font color=#1a73e8>作者：</font>** Yanbin Gong, Lei Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A developer checking an assistant's report may need only an alarm that a claim is unsupported. A generative verifier, however, can continue decoding to quote and classify the errors. We study how much of that output is needed to recover its decision. In a frozen 2B span verifier, the choice between an empty error list and its first object precedes all localization. Native8 stops generation at this branch. The preceding seven syntax tokens are fixed, so Prefill1 supplies them as input and generates only the unrestricted branch token, using the same native instruction. On 2,015 code-agent TEST responses, Prefill1 reduces eager resident service by 84.84% relative to full generation, with released-reference F1 of 83.43 versus 83.41. It saves 31.98% over Native8 even though their logical token totals are identical. Under default compiled execution, the extra saving is 6.74-26.73% on the complete workload, with small decision changes. Controlled evidence interventions and first-location decoding establish what these shorter readouts retain and what requires further generation.

---


### 304. [HARI4D: Hand-Articulation Aware 4D Reconstruction of Human-Object Interaction](https://arxiv.org/abs/2611.32932)

**<font color=#1a73e8>作者：</font>** Semin Kim, Xianghui Xie, Chuqiao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning about human-object interaction from RGB cameras is important for gaming, VR environments, and robot learning. Yet 4D reconstruction from a monocular RGB camera is challenging, especially when articulated hands are involved. Prior full-body works neglect hands during reconstruction, causing them to penetrate into, or float from the object. We present HARI4D, a hand-articulation-aware method for reconstructing spatially and temporally consistent 4D human-object interaction from monocular RGB video. We introduce a history-aware object tracker that provides robust and stable tracking. Based on these tracks, we improve the interaction configuration through coarse-to-fine reasoning that follows the order of object manipulation: ReachNet first brings the full body and arms to the object during contact, and TouchNet then finalizes hand articulation according to temporal context and local object geometry. On ARCTIC, unseen in training, our method reduces the object error by 56% and improves hand contact F1 from 0.866 to 0.921 over prior art. Our method recovers accurate full body-object interaction with coherent hand articulations and applies to online videos. Our code and pretrained models will be released.

---


### 305. [ProX-MAD: Aggregating Spatial Context into Representative Proxies for Few-shot Medical Anomaly Detection](https://arxiv.org/abs/2611.32941)

**<font color=#1a73e8>作者：</font>** Seunghyun Oh, Seongsu Lee, Seunghye Chae 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot medical anomaly detection (MAD) has largely followed a dataset-specific "one-for-one" paradigm, leaving unified "one-for-many" modeling underexplored. Naively extending existing methods to this setting causes substantial performance degradation, especially at the pixel level. We attribute this to their detection mechanisms: a shared decision boundary becomes unreliable across heterogeneous lesion definitions, whereas a normal-only memory bank cannot adequately cover diverse normal distributions with few references. We propose ProX-MAD, a proxy-based framework that aggregates spatial context into compact, learnable, state-specific proxies for unified few-shot MAD. Its Masked Proxy Infusion Attention (MPIA) module cross-attends proxy tokens to reference patch features and applies proxy-wise masking to retain high-confidence correspondences, mitigating proxy collapse and encouraging diverse proxies that summarize both normal and abnormal references. Across six medical datasets, ProX-MAD exhibits only a marginal performance drop from one-for-one to one-for-many training. Despite being trained only once as a unified model, it also outperforms prior state-of-the-art methods on average even when they use their more favorable one-for-one protocol, demonstrating the practicality of unified multi-dataset MAD.

---


### 306. [Beyond Expected Value: PPO with Distributional Critics for Systematic Conservation Planning](https://arxiv.org/abs/2611.32948)

**<font color=#1a73e8>作者：</font>** Ana Maria Quintero Ossa, Daniele Silvestro, James Rudd-Jones 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systematic conservation planning must allocate limited protection budgets sequentially under ecological and climatic uncertainty. Static tools cannot adapt as conditions change, and policies optimised only for expected outcomes can fail on the worst-case trajectories climate change makes increasingly likely. CAPTAIN was the first framework to cast this as sequential reinforcement learning, but its gradient-free Evolution Strategies (ES) optimiser lacks per-timestep credit assignment. We replace ES with Proximal Policy Optimisation (PPO) via a Plackett-Luce solution to CAPTAIN's non-differentiable action space, and replace its scalar critic with an Implicit Quantile Network (IQN) modelling the full return distribution. A matched-granularity comparison shows decision granularity, not the optimiser, drives most of the ecological gain, so the real contribution is training efficiency and extensibility to risk-sensitive objectives. On a New Zealand marine dataset, it matches or exceeds ES's outcomes at a fraction of the training cost, offering a template for future work ES's black-box design could not support

---


### 307. [FedTumor-IoMT: Federated Learning-Aided Brain Tumor Diagnosis on Resource-Constrained Edge IoMT Devices](https://arxiv.org/abs/2611.32952)

**<font color=#1a73e8>作者：</font>** Pranshu Jena, Prajnyajit Mohanty, Umesh C. Pati  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint brain tumor segmentation and classification models are computationally intensive, limiting their training on resource-constrained edge platforms and restricting privacy-preserving Federated Learning FL in the Internet of Medical Things IoMT. Existing approaches either perform both tasks on GPU-equipped workstations or support only classification on edge devices. To address this gap, this work proposes a lightweight multitask FL framework for joint segmentation and classification through local edge training. A shared pretrained LiteMedSAM encoder with TinyViT extracts features for a coordinate-attention-based segmentation decoder and a segmentation-guided classification head, eliminating a separate feature extractor. Selective encoder freezing retains 95\% trainable parameters while reducing on-device training costs. The proposed framework is experimentally validated on a laboratory testbed of five resource-constrained edge clients using 1,200 T1-weighted MRI samples. It achieves 94.20\% classification accuracy, 88.53\% DSC, 83.68\% IoU, and 99.87\% ROC-AUC. Its classification accuracy remains within 0.6\% of the GPU-trained baseline of 95.21\% across five FL rounds. The attention and feature refinement modules improve DSC and IoU by 3.82\% and 4.60\%, respectively, with 0.74 GFLOPs of additional computation. On edge hardware, the framework achieves 46.54 s inference latency, 52.8\% CPU utilization, and a peak temperature of 65$^\circ$C without thermal throttling. Its inference latency is observed to be 6.4--10.5 times lower than that of existing frameworks. These results demonstrate the feasibility of privacy-preserving joint brain tumor segmentation and classification on resource-constrained edge platforms.

---


### 308. [Polynomial-Time Learning of Random Automata from One Label per Word](https://arxiv.org/abs/2611.32959)

**<font color=#1a73e8>作者：</font>** Yilin Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a binary deterministic finite automaton whose $2n$ transitions are chosen independently and uniformly from its $n$ states. The learner observes independent uniform words of length $m$, each labeled with a single bit indicating acceptance. For every fixed $\beta>0$ we give a polynomial-time algorithm that works outside a set of transition tables of probability $o(n^{-\beta})$. On each remaining table, for any start state and accepting set, the predictor has error at most $\epsilon$ on fresh uniform words of length $m$ with probability at least $1-\gamma$ over the training sample and the learner's random choices. Its sample size and running time are polynomial in $n$, $m$, $1/\epsilon$ and $\log(2/\gamma)$, with degree depending only on $\beta$. Although each word reveals only one output, comparing label moments at two consecutive history lengths lets us estimate the expected product of the signed outputs of two continuations from the same hidden state.
We also refute Conjecture 4 of Fish and Reyzin on meeting times. For two distinct states fixed before the table is drawn and every fixed $c>0$, the fraction of words of length $\lfloor cn\rfloor$ that send them to different states converges in probability to $e^{-c}$. On a typical table, driving this fraction down to $1/n$ takes asymptotically $n\log n$ letters. Selected proof steps are formalized in Lean.

---


### 309. [Multi-Agent Coordination Through Stigmergy for Canal Network Formation on Real Terrain](https://arxiv.org/abs/2611.32966)

**<font color=#1a73e8>作者：</font>** Jordan Kennedy, Federico Oliva, Amir Degani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Terrain-modifying robot swarms operating in unstructured outdoor environments must coordinate under uncertain dynamics despite unreliable communication and incomplete global information. Stigmergy offers a decentralized alternative by allowing agents to coordinate indirectly through persistent environmental modifications, yet its application to large-scale terrain construction on real landscapes remains largely unexplored. Inspired by beaver canal construction, we present a minimal stigmergic framework for multi-agent systems in which decentralized agents follow local wetness cues, excavate terrain, and interact through a closed agent--environmental feedback loop. The framework couples agents with seasonal hydrology on a real digital elevation model (DEM). Across 110 simulations on an 862m x 1167m region spanning agent count and hydrological recession rate, the model produces emergent canal-like networks whose morphology varies predictably with environmental constraints. An alignment-invariant morphological evaluation against a field-annotated reference network identifies parameter regimes that reproduce key canal characteristics, while failure cases reveal over-canalization and fragmentation. These results demonstrate that simple local terrain-modifying behaviors can generate plausible landscape-scale structures through environmental feedback, providing a minimal framework for studying decentralized terrain construction and bio-inspired swarm coordination.

---


### 310. [VidForce: Predicting Force-Aware Articulation by Observing Humans](https://arxiv.org/abs/2611.32967)

**<font color=#1a73e8>作者：</font>** Rafay Mohiuddin, Jiaqi Chen, Marc Pollefeys 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> People can anticipate how an object moves and the effort an interaction may require by watching others. How can embodied agents acquire this understanding from video? Force measurements provide direct sensory supervision, but require specialized equipment and remain limited in quantity. We introduce VidForce, which estimates an interaction trajectory together with a force profile from a third-person RGB video; 2D contact clicks and textual object-action prompts are optional. Our approach makes limited instrumented measurements useful for interpreting human interactions through learned physical prototypes as a prior. The prototypes share learned force levels and temporal profiles across interactions of comparable effort, with visual and semantic cues determining their contribution to each observation. Geometric and vision-language features adapt this prior to the observed interaction, while a joint conditional flow refines an initial tracked trajectory together with the force profile. Paired human and instrumented-gripper recordings provide measured force references for supervising human video, and a separately trained torque model demonstrates that the formulation extends to other sensory quantities. We evaluate trajectory recovery and force estimation through baseline comparisons and controlled ablations on held-out interactions from the Hoi! dataset. On this evaluation subset, VidForce achieves 6.6 cm ATE, peak-force MAE and RMSE of 4.81 N and 5.92 N, respectively, and force-profile RMSE of 5.52 N. On real-world videos, VidForce infers motion and force reliably and consistently despite the variability in human execution. We further deploy VidForce on a Spot robot, where trajectories and force profiles estimated from human demonstrations drive real-world articulated-object manipulation, and report success rates across repeated trials. Project page: this https URL

---


### 311. [FocusAnchor: Zero-Shot Metric Depth by Anchoring a Depth Foundation Prior to Focus Cues](https://arxiv.org/abs/2611.32970)

**<font color=#1a73e8>作者：</font>** Ashkan Ganj, Hang Su, Tian Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing depth-from-focus methods can struggle with weak focus cues, new cameras, or fewer focal slices. We present FocusAnchor, a recurrent model that uses focus-volume lookups to refine metric depth and repeatedly aligns a relative depth prior from a frozen foundation model to the current depth estimate. The aligned prior guides subsequent refinement in a feedback loop, carrying metric scale recovered from textured regions into regions where focus cues are weak while preserving scene structure. To support transfer across cameras, we synthesize training stacks with randomized camera parameters and focus distances. However, stack synthesis blurs existing image noise differently across slices, creating artificial depth cues even on textureless surfaces. We add independent per-slice noise to suppress these cues. We also introduce variable-stack training to improve robustness with fewer focal slices and support more practical mobile capture. Compared with FOSSA ViT-B, FocusAnchor reduces AbsRel by 36% on NYU Depth V2 and by 9% on DDFF-12 after fine-tuning. In zero-shot evaluation, FocusAnchor and its variable-stack variant, FocusAnchor-flex, achieve the two lowest AbsRel values on all five benchmarks. On ZEDD test, FocusAnchor achieves 9% lower AbsRel than the best competing method, FOSSA ViT-B, while FocusAnchor-flex achieves lower AbsRel with 40% fewer focal slices on ZEDD validation.

---


### 312. [File Size as a Potential Dataset Bias in Audio-Visual Deepfake Data](https://arxiv.org/abs/2611.32979)

**<font color=#1a73e8>作者：</font>** Marcella Astrid, Niki Maria Foteinopoulou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deepfake detection benchmarks are commonly designed to evaluate whether models can distinguish authentic from manipulated audiovisual content. However, benchmark construction pipelines may introduce unintended associations between class labels and simple file-level properties. In this work, we identify a potential file-size bias in two widely used audio-visual deepfake datasets. In the 1M-Deepfakes Detection Challenge dataset, a score derived from file size alone achieves 70.13% AUC on the validation set. When file size is considered together with video duration, simple file-level methods exceed 90% AUC on 1M and 85% AUC on FakeAVCeleb. Although the same pattern is not observed in DFDC, the results suggest that the observed association is dataset-dependent rather than an inherent property of deepfake videos. We discuss several possible explanations, including differences in encoding, compression, source data, manipulation procedures, and post-processing, although the present analysis does not establish the underlying cause. We further discuss whether the factors associated with file size may also leave traces in decoded video or audio, and consequently whether they could influence content-based deepfake detection, as an important direction for future work. Our findings highlight the importance of examining simple file-level properties when constructing and evaluating deepfake datasets and benchmarks.

---


### 313. [NEST: Uncovering and Nesting Unknown Objects in Open-World Object Detection](https://arxiv.org/abs/2611.32981)

**<font color=#1a73e8>作者：</font>** Yuchen Zhang, Yuan Gao, Sebastian Schmidt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world object detectors aim to localize objects of classes not covered by their training annotations, but most label them only as "unknown". This label tells a system that an object is present but not what it is, while its broader category would allow a more informed decision. We therefore address both uncovering unknown objects and assigning them to the broader categories of a given class taxonomy. For uncovering, we find that most unknown objects are already localized and labeled "unknown" in our base detector, but are discarded during final top-k selection because background receives higher scores. To mitigate this, we propose a class-agnostic ranker that estimates how well each predicted box fits an object and uses these scores to select the final predictions. Across three benchmarks, our detector improves unknown recall by 3.8% to 195.1% relative to the strongest baseline in each task, while maintaining competitive known-class detection. For categorizing, we draw on Euler diagrams, in which the region of a category contains the regions of its members. Our categorizer builds each category's region from the known classes and learns how much room to leave for members it has never seen. On the same detections, it categorizes unknown objects more accurately than existing hierarchical methods. Code is available at this https URL.

---


### 314. [AVQ-Attention-2: Adaptive Vector-Quantized Attention with Exact Local Blocks and Linear-Cost Training](https://arxiv.org/abs/2611.32989)

**<font color=#1a73e8>作者：</font>** Winfried van den Dool, Patrick Forré, Amir Habibian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention costs $\mathcal{O}(N^2)$ in the number of tokens. Vector-quantized attention reduces this to $\mathcal{O}(NM)$ by clustering the $N$ keys, attending to the $M$ codewords instead, and its adaptive form, AVQ-attention, concentrates codebook resolution where a query's attention mass actually falls. We present AVQ-Attention-2, a better design that merges it with exact local attention and attends to the mean of each cluster's keys rather than to a codeword. We show three improvements: consistently better quality at comparable cost; training that now also costs $\mathcal{O}(NM)$ rather than $\mathcal{O}(N^2)$; and an approximation accurate enough that the layer can be dropped into a pretrained transformer without fine-tuning. Across a variety of sequence lengths the result is competitive not merely with other approximate attention but with exact dense attention, running faster than FlashAttention at little to no loss in quality.

---


### 315. [Decision-Native Multimodal Clinical Modeling via Anatomical Grounding and Confidence Calibration](https://arxiv.org/abs/2611.32993)

**<font color=#1a73e8>作者：</font>** Juntao Jiang, Wenqi Zhong, Guangyu Guo 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured clinical decisions from volumetric computed tomography (CT) require anatomically grounded predictions and calibrated confidence estimates. However, existing 3D medical multimodal models often suffer from uncalibrated autoregressive decoding and shortcut reliance on irrelevant anatomical regions. We introduce Radev, a decision-native multimodal model that integrates anatomy-guided visual compression, direct candidate prediction, and counterfactual confidence supervision. To bridge global context with fine-grained slice details, a frozen 3D encoder extracts reusable organ-level features, which are dynamically selected by the query to attend to 2D slice features within predicted anatomical bounds. The resulting compact visual tokens enable the language backbone to estimate candidate probabilities in a single forward pass without autoregressive decoding. We further propose Counterfactual-Calibrated Training (CCT) to compare predictions under intact and intervened organ representations. CCT encourages confidence to decrease when removing target-organ evidence degrades decision quality, while penalizing excessive confidence drops under unrelated-organ removal. To facilitate rigorous evaluation, we construct CT-Verdict, a comprehensive benchmark spanning binary finding presence, multiple-choice questions, and ordinal severity assessment across both in-distribution and external cohorts. Extensive experiments demonstrate that Radev significantly outperforms state-of-the-art methods in both decision accuracy and confidence calibration, while generalizing robustly under distribution shifts. Project page at this https URL

---


### 316. [First-Hit Photoconsistency for Neural Surface Reconstruction](https://arxiv.org/abs/2611.32998)

**<font color=#1a73e8>作者：</font>** Gabriel Lenain, Edmond Boyer, Jean Ponce  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent neural implicit and Gaussian splatting approaches have achieved impressive results in multi-view surface reconstruction. However, jointly optimizing geometry and appearance introduces ambiguities. A parametric appearance model can compensate for geometric errors, reproducing the input images accurately without an accurate surface. We demonstrate accurate neural implicit surface reconstruction using only multi-view patch photoconsistency with geometry-based visibility, without volumetric rendering or parametric appearance models. For each reference ray, sphere tracing computes the first surface intersection. Its position and normal define a local patch whose photoconsistency is evaluated across visible neighboring views using colors sampled directly from the input images. For efficient sphere tracing, we use a 1-Lipschitz multi-layer perceptron. We use a single photoconsistency loss, without foreground masks or auxiliary geometric regularization. Experiments show that our method achieves the lowest mean Chamfer distance on BlendedMVS (BMVS) among compared methods and matches the geometric accuracy of leading reconstruction methods on DTU.

---


### 317. [One, No One and One Hundred Thousand CTs: Testing Anatomical Control in Text-to-CT Generation](https://arxiv.org/abs/2611.33003)

**<font color=#1a73e8>作者：</font>** Francesca Pia Panaccione, Eugenio Lomurno, Matteo Matteucci  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in deep learning and the public availability of computed tomography (CT) datasets with paired reports have enabled many Text-to-CT generators. However, their evaluations almost always differ in preprocessing and metrics, which hinders comparison. Moreover, their protocols almost never test how editing the report changes the CT, not even at the same seed, so the report is often assumed to control the anatomy without evidence of how much and how consistently it does. We therefore propose CtrlCT, a toolkit that tests two properties of a generator, Credibility and Control. Credibility tests compare generated CTs, as a population, with real CTs and reports; Control tests are metamorphic and need no reference CT: at a fixed seed, editing one finding should change it as requested, keep negated findings absent and shift distant anatomy no more than a new seed, and the change should hold across seeds. A Report Card summarises all measures and insights for each generator. We benchmark five public generators on 940 chest CTs and 687 edits of pleural effusion and cardiomegaly, holding out a sixth to test the toolkit. Among them, the most credible generators barely respond to an added effusion, while the most responsive produce less realistic and less diverse CTs. The analyses proposed in the literature do not reveal this. We release CtrlCT, its edits, seeds and 30,525 synthetic CTs after acceptance.

---


### 318. [Train What You Run: Probabilistic Convolutions for Learning Token Compaction in State Space Models](https://arxiv.org/abs/2611.33009)

**<font color=#1a73e8>作者：</font>** Piotr Kubaty, Mikhail Saladkou, Jacek Tabor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token compaction reduces inference cost by passing only selected image patches or video tokens to later layers. In sequence models with local convolutions, each removal changes which tokens are neighbors. Learning which tokens to keep therefore requires a training signal that accounts for the new neighborhoods. We introduce ProbConv, which computes the exact expected convolution before activation at a kept position under independent keep decisions. The operator is differentiable in the keep probabilities. With binary decisions, ProbConv and step gating reproduce the compacted Mamba block. Across image, vision--language and video backbones, ProbConv is strongest under strong compaction: its advantage over matched training controls grows as more tokens are removed. In Cobra, it also outperforms adaptations of published vision--language pruning methods at matched inference budgets. ProbConv also improves over matched zero-mask training in video frame selection and speech frame dropping. Our code is available at: this https URL

---


### 319. [MESSI: Multi-Expert Soccer Skill Integration for Physics-Based Character Control](https://arxiv.org/abs/2611.33011)

**<font color=#1a73e8>作者：</font>** Xiaogang Peng, Jiaqi Zou, Lei Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physics-based soccer characters must perform diverse motor skills and transition smoothly between them, such as dribbling into a shot. However, skills that perform well in isolation may fail when executed sequentially, as preceding behaviors can leave the character and ball in unfamiliar states. We present MESSI (Multi-Expert Soccer Skill Integration), a framework that enables multiple soccer skill transitions through shared adaptation while preserving the original skill policy outside transitions. MESSI first trains eight task-competent experts using motion priors and task rewards, then distills them into a unified, skill-conditioned Transformer. Rather than retraining individual experts for different transitions, we train a shared, context-conditioned low-rank adapter on the frozen student through online reinforcement learning. Activated upon skill switching, the adapter helps the target skill handle unfamiliar entry states, while a learned exit mechanism determines when to return control to the original student. By disabling the adapter during native skill execution, MESSI preserves the original student policy by construction. Experiments across individual skills, skill transitions, and continuous skill chains demonstrate substantial improvements over direct switching, including an increase in dribbling-to-shooting success from 19.8% to 61.8%.

---


### 320. [RFW-W: Scaling Physical Asset Universes for Generative Embodied Simulation](https://arxiv.org/abs/2611.33013)

**<font color=#1a73e8>作者：</font>** Jiawei Weng, Rui Zhang, Saining Zhang 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling embodied simulation requires diverse objects with executable physical representations. We present RFW-W, a physical asset universe connecting rigid, articulated, and deformable asset sources to task-conditioned scene composition. Its reported inventories comprise 1,010,386 asset records: 524,611 rigid assets in 1,212 categories (RFW-R), 402,410 articulated assets in 531 categories (RFW-A), and 83,365 jointly verified deformables in 485 categories (RFW-S). These taxonomies contribute 2,228 dataset--category entries. RFW-R couples category-guided generation with collision geometry, composed physical properties, and interaction annotations; RFW-A uses reusable agent-authored procedural generators with explicit part and joint structure; RFW-S uses structure-aware simulation representations, calibration, and independent testing. A common interface preserves physical requirements specific to each asset type for retrieval and scene assembly. Quantitative evaluations demonstrate that RFW-R provides broader asset coverage and stronger scene-fulfillment capabilities than existing datasets. Across five RoboTwin tasks, using 100 demonstrations per task for each asset source, policies trained on RFW-R achieve macro success rates of 71.2% in clean settings and 41.8% under randomization, exceeding the strongest baseline by 15.8 and 10.6 percentage points, respectively. RFW-W provides a scalable and unified asset foundation for generating physically grounded, task-conditioned embodied worlds.

---


### 321. [RePix-VFI: Re-rendering Observed Pixels for Video Frame Interpolation with Generative Priors from One-Step Diffusion](https://arxiv.org/abs/2611.33016)

**<font color=#1a73e8>作者：</font>** Dayeon Kim, Jeonghyeok Do, Munchurl Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-frame video frame interpolation (VFI) aims to reconstruct dense video from sparse keyframes, requiring accurate intermediate motion and faithful appearance. As temporal gaps grow, flow-based methods can retain observed textures but misplace them under ambiguous motion, whereas iterative latent-diffusion models can synthesize plausible content but incur substantial sampling costs and may alter details during reconstruction with a variational autoencoder (VAE). We present RePix-VFI, named for Re-rendering observed Pixels, a multi-frame VFI framework that couples draft-conditioned one-step video diffusion with reconstruction from observed keyframes. A pretrained video diffusion model refines a flow-rendered draft of the whole window in a single forward pass. For each target frame, our generative readback matches its two bounding keyframes to the generated prediction using an optical-flow estimator. The resulting correspondences guide re-rendering of original keyframe RGB pixels outside the VAE. A lightweight appearance fusion head combines these renderings with generated appearance. Experiments on benchmark datasets demonstrate significant improvements in reconstruction and perceptual quality. On SNU-FILM at $\times$8 and $\times$16, RePix-VFI achieves the highest PSNR and the lowest LPIPS, FloLPIPS, and tOF among the compared methods, exceeding the best evaluated diffusion-based baseline by 1.71 and 1.48dB in PSNR, respectively. It also runs 32--42$\times$ faster than the state-of-the-art multi-frame VFI diffusion model.

---


### 322. [E-MAPS: Event-Based Promptable Video Segmentation with Memory-as-Prompt](https://arxiv.org/abs/2611.33017)

**<font color=#1a73e8>作者：</font>** Adonay Demewez Gebremedhin, Mohamad Alansari, Wessam Shehieb 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-based video object segmentation (VOS) remains brittle under fast motion and adverse illumination. Event cameras preserve signal under blur and challenging exposure, but provide little evidence when motion slows. Interaction can restore object state for subsequent propagation, yet promptable event methods merely address single windows. We formalize event-based Promptable Video Segmentation (ePVS), where prompts at arbitrary windows initialize, correct, or introduce objects and predictions. We present Event Memory-As-Prompt Segmentation (E-MAPS), which transfers a pretrained promptable segmenter to event streams and learns propagation and correction. Event-to-Token (E2T) aligns recurrent event features with pretrained representations while preserving prompt-conditioning priors. Memory-Aware Prompting (MAP) converts object-conditioned history into sparse prompts, allowing memory and user inputs to share one decoder pathway efficiently. We construct Event-View Masklets (EViM) from 206K aligned RGB-event pairs and 620K masks for two-stage representation transfer and native event-video learning, and establish three training-disjoint benchmarks. E-MAPS leads prompt-once and interactive ePVS across all three benchmarks while being more efficient. It further demonstrates strong performance on zero-shot object tracking benchmarks. Project page: this https URL

---


### 323. [PAC-style Bounds on the Conditional Validity of Conformal Predictors](https://arxiv.org/abs/2611.33023)

**<font color=#1a73e8>作者：</font>** Nicolo Colombo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction sets are guaranteed to be marginally valid over the attribute space, but local coverage can diverge from the user-defined target $1-\alpha$. Constructing conditionally valid prediction sets with finite calibration data is impossible for a general data-generating distribution. We derive PAC-type probabilistic lower bounds on the input-conditional coverage of any conformal predictor, without assumptions on the data distribution. They are based on the Markov and Cantelli inequalities and adapt to both calibration-marginal and calibration-conditional setups. A tighter, model-dependent Cantelli bound depends on the variance of the conditional coverage and is estimable from data using a fully non-asymptotic Hoeffding argument. The results suggest conditional-coverage variance as a scalable and theoretically motivated empirical measure of conditional validity.

---


### 324. [Best Arm Identification with Unknown Post-Action Context Distribution](https://arxiv.org/abs/2611.33024)

**<font color=#1a73e8>作者：</font>** Amir Mohammad Abouei, Mohammad Shahverdikondori, Emad Emamjomeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study best arm identification (BAI) with post-action context in the fixed-confidence setting. After choosing an action, the learner observes a post-action context together with a reward whose distribution depends only on this context. Incorporating such intermediate information can substantially reduce the sample complexity of identifying the best arm. While Shahverdikondori et al. (2026a) analyzed the case where the distribution of contexts given actions is known, we address the more challenging and practically relevant case where this distribution is unknown. We derive an instance-dependent sample complexity lower bound and propose a Track-and-Stop algorithm that matches it asymptotically with access to an optimization oracle. Our stopping rule uses a new concentration inequality that jointly controls uncertainty in the context distributions and reward means, removing the factor of two incurred by separate concentration bounds. Implementing the algorithm generally requires solving nonconvex optimization problems. We propose a convex relaxation with instance-dependent approximation guarantees, including asymptotic tightness on hard Gaussian instances. Experiments demonstrate that exploiting post-action context reduces the sample complexity relative to baselines that ignore it, even when the context distributions are unknown.

---


### 325. [Score-Based Diffusion for Hypergraph Signals in the t-Spectral Domain](https://arxiv.org/abs/2611.33026)

**<font color=#1a73e8>作者：</font>** Zhiyuan Dong, Carlos Mundo-Levano, Daniel L. Lau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the first score-based generative model for signals on a fixed hypergraph, formulated in the spectral domain of t-product hypergraph signal processing (t-HGSP). The naive tensor heat semigroup is ill-posed, since after palindromic symmetrization the spectral slices of the Laplacian tensor are no longer positive semidefinite. A per-mode frequency shift repairs it, yielding a forward Ornstein-Uhlenbeck diffusion that decouples per (eigenmode, slice) pair with closed-form marginals, exact score targets, and an exactly isotropic stationary law. A lightweight slice-conditioned denoiser is trained on the resulting real spectral grid. Sampling combines its score on data-active modes with the closed-form score elsewhere, which proves essential for stability at scale. A closed cosine-form observation operator turns missing-node recovery into linear-Gaussian guidance with stabilized posterior sampling. On hypergraphs of up to 500 nodes, our model beats a clique-expansion baseline by margins growing from $2\times$ to $27\times$ in covariance error, matches the graph-spectral statistics of the data better than the graph-basis model itself, and reaches the finite-sample estimation floor on data rotated off the t-spectral axes. Posterior sampling reduces missing-node NMSE to 0.28-0.64 (classical baselines 0.87-1.1) at conservative coverage, and cuts the framework's own denoising baseline by up to $3.6\times$.

---


### 326. [SHARPnP: Self-Supervised and Plug-and-Play Hyperspectral Super-Resolution from Real Noisy Unaligned Camera Measurements](https://arxiv.org/abs/2611.33032)

**<font color=#1a73e8>作者：</font>** Mohamad Jouni, Brayan Monroy, Jorge Bacca 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Affordable snapshot hyperspectral cameras capture spectral images in a single exposure but suffer from limited spatial resolution and sensor noise. Low-cost RGB cameras provide fine visible details to guide NIR reconstruction, but introduce spatially varying cross-camera misalignment. Supervised fusion methods require relatively large datasets of clean, high-resolution hyperspectral images, are sensitive to sensor noise, and generalize poorly across new sensors. We introduce SHARPnP, an interpretable, flexible framework coupling registration and reconstruction for RGB-guided hyperspectral super-resolution from noisy, unaligned measurements without clean references. We adapt a pretrained registration model via a cross-view loss backpropagated through a fixed plug-and-play fusion module. Temporal and recorrupted pairs enable reference-free self-supervision on noisy inputs. At test time, we calibrate cross-camera radiometry and refine alignment. Plug-and-play fusion employs sequential three-band denoising. On the REAL benchmark, SHARPnP outperforms supervised fusion baselines at $4\times$, $8\times$, and $16\times$ on clean inputs and at $4\times$ under Gaussian noise ($\sigma=5/255, 10/255$). On native RGB-HSI snapshot measurements, it reconstructs all 51 VIS-NIR bands, beyond the conventional 31-band VIS setting, without high-resolution references.

---


### 327. [Hybrid AI for AI-Native RAN Control: A Functional Perspective](https://arxiv.org/abs/2611.33035)

**<font color=#1a73e8>作者：</font>** Sabrine Aroua, Osama Arouk, Pegah Alizadeh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-native radio access network (RAN) control involves interdependent decisions across network entities, protocol layers, and timescales. Understanding how AI and conventional methods can jointly support these decisions requires a common basis for comparing their functional roles. This survey introduces a technique-agnostic taxonomy of RAN decision-making organized around four complementary capabilities: Representation and Reasoning, Prediction and Simulation, Adaptive Control, and Decision Synthesis. These capabilities are defined by their roles in the control process, independently of the techniques used to implement them. Through this perspective, we examine representative AI and model-based approaches, including foundation models, world models, reinforcement learning, and optimization. We then apply the taxonomy to representative RAN control solutions across slow, medium, fast, and cross-timescale applications to identify which capabilities they implement and how these capabilities are combined in hybrid AI systems. We also review datasets, benchmarks, simulators, digital twins, and experimental platforms according to their support for the decision-making process and reproducible evaluation. The review highlights a gap between the availability of resources for closed-loop experimentation and the standardization of tasks, metrics, and evaluation protocols needed for meaningful this http URL, we identify research directions for hybrid AI in AI-native RAN, including capability integration, multi-agent and cross-timescale coordination, constraint handling, and reproducible closed-loop evaluation. A curated list of surveyed works and evaluation resources is available at this https URL.

---


### 328. [Linear Probes Can Guide: Training-Free Control of Representation Generators](https://arxiv.org/abs/2611.33037)

**<font color=#1a73e8>作者：</font>** Pengwei Wang, José Morano, Botond Fazekas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation-space generative models, such as Representation Autoencoders (RAEs), leverage pretrained vision foundation models (VFMs) primarily to accelerate training and improve sample fidelity. Yet VFMs are more than reconstruction tokenizers, as they feature rich representation spaces that are highly organized and linearly readable. We observe that this removes a key obstacle of post-hoc guidance: by linearity of expectation, a clean probe applied to an ideal denoiser's prediction yields the exact posterior mean of the probe scores at any noise level. This regime, which we call Semantic Mean-Space, turns semantic guidance into a Bayesian linear inverse problem, bypassing the need for training-time conditioning. With this foundation, we propose LiSM, a unified framework for Linear Guidance in Semantic Mean-Space. To validate the framework, we developed and adapted different solvers, and characterized them based on how they estimate probe-space uncertainty and propagate the correction through the representation. In addition, we propose Fit-Path, a solver designed to achieve strong global and local control. Our results in four control setups (class, attributes, foreground, and keypoints) show that LiSM methods, and Fit-Path in particular, provide effective, lightweight control across global and local tasks, outperforming noise-aware and pixel-space guidance.

---


### 329. [Spectrify: Framework for Hyperspectral Image Generation Using Computer Graphics](https://arxiv.org/abs/2611.33042)

**<font color=#1a73e8>作者：</font>** Yasin Mamedov, Daniil Vladimirov, Sofiia Dorogova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral images (HSIs) record the full spectrum of light at every pixel, so projecting an HSI through a camera's spectral sensitivities gives that camera's RAW image, and one HSI can supply training data for hyperspectral reconstruction and camera-pipeline methods. Real HSIs, however, are slow and expensive to capture, and the largest datasets hold only about 1,000 images. High-level vision commonly replaces scarce real data with images rendered from 3D scenes. Low-level tasks, however, need physically correct spectra, which requires spectral rendering with a measured spectrum for every material in a scene, and existing spectral renderings cover only a handful of scenes, mostly with a simplified image formation model. We present Spectrify, a framework that converts 3D scene datasets into HSIs, together with a library of reflectance spectra labeled by material and compiled from close-range hyperspectral datasets and spectrophotometer measurements. In Spectrify, spectra follow the material: each object receives a physically based optical model and measured reflectance spectra or optical constants from its material category, each lamp an emission spectrum of its type and the sky a modeled daylight spectrum, and Mitsuba 3 path-traces the full light transport of each scene per wavelength. We show that a hyperspectral reconstruction network trained only on our synthetic HSIs generalizes to unseen real datasets better than networks trained on the largest real HSI datasets on most test sets, and that assigning spectra by material category instead of by color alone improves this transfer on every test set. RAW images projected from our HSIs are also useful training data for color constancy, performing on par with existing synthetic RAW generators. We release the 4,500 rendered HSIs, the code of Spectrify and its material-labeled reflectance library.

---


### 330. [When Is Product Decoding of ECOC MAP-Consistent? Pair Structure and the n-vs-Rest Codes](https://arxiv.org/abs/2611.33044)

**<font color=#1a73e8>作者：</font>** Gendo Kumoi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Error-Correcting Output Codes (ECOC) combine binary classifiers by the sum decoder, which totals probabilities, or the product decoder, which totals log-likelihoods. In the noiseless setting, where the binary classifiers output the true posteriors, we ask on which code matrices each decoder always agrees with the Bayes-optimal (MAP) class. For the sum decoder the answer is known: the code must be equidistant (James and Hastie, 1998). We answer the question for the product decoder. Two classes are compared through the votes of the columns on which they differ: the sum decoder decides by their sample mean, the product decoder by an M-estimator with influence function artanh, and each vote is the MAP margin plus a bias determined by the other classes alone. Our main theorem states that the product decoder is MAP-consistent if and only if, for every class pair, the columns on which the two classes differ are matched with the columns obtained by swapping the two classes (or their complements), and equivalently if and only if the code is a union of n-vs-Rest codes. Efficient equidistant codes are therefore excluded: Hadamard codes ($M\ge 8$), which meet the Plotkin bound with $M-1$ columns, have no such pairs, and for the Sylvester type the reversal margin can be at least a constant 0.0182 independent of $M$. All theorems are machine-checked in Lean 4. On six real datasets with estimated probabilities, the product decoder is slightly more accurate when each column is calibrated, and the sum decoder is better when the calibration error differs across columns; in either case the decoders disagree only near ties.

---


### 331. [A Bernstein-Type Variance-Adaptive PMW Mechanism for DP Query Release](https://arxiv.org/abs/2611.33045)

**<font color=#1a73e8>作者：</font>** Mohamed Aniss Benstaali, Habib Louafi, Naima Bessah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Private Multiplicative Weights (PMW) is a central mechanism for the differentially private release of adaptive linear statistics over a finite universe. Its classical analysis uses a fixed multiplicative-weights learning rate and does not exploit the local variance of the current hypothesis. This paper presents PMW-Bernstein, a variance-adaptive refinement in which the update step is determined by the relationship between the privately estimated query error and the variance under the current hypothesis. The mechanism retains the standard PMW privacy architecture based on Sparse Vector screening, Gaussian numerical measurements, sequential composition, and post-processing. Through a potential-based analysis, we prove a one-step progress bound that yields a global weighted energy bound, recovers the classical $O(1/{\alpha}2)$ update regime in general, and establishes an $O(1/{\alpha})$ update regime under a Bernsteintype condition on updated rounds. Controlled simulations over synthetic finite-universe distributions and query workloads show that the adaptive rule reduces the number of updates in the low-variance regime, remains competitive in the high-variance regime, and succeeds within the prescribed update budget in the heterogeneous regime where the fixed-step baseline fails.

---


### 332. [Local Indices Are Not Enough: Synchrony and Global Information in Bandit Algorithms](https://arxiv.org/abs/2611.33056)

**<font color=#1a73e8>作者：</font>** Aakash Gore, Shivaram Kalyanakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard index-based stochastic bandit algorithms such as KL-UCB and Thompson Sampling achieve optimal $O(\log T)$ regret over a horizon $T$. The former uses the global timestep to construct each arm's index, while the latter samples each arm's belief distribution at every timestep. The necessity of global information and synchronous index updates for achieving optimal regret has not been examined yet. In this paper, we investigate the fundamental limits of asynchronous local index algorithms---those that recalculate an arm's index only upon pulling it, using solely that arm's own reward history and a local randomness budget. We prove that no such algorithm can achieve $O(\log T)$ regret across all bandit instances. We then analyse the functional equations arising from asynchronous updates, and show that the achievable regret lies in a sub-polynomial, super-polylogarithmic regime. We propose an asynchronous local index policy whose regret upper bound also lies in this regime. Turning to synchronous local algorithms, which sample every arm's index at all timesteps as in Thompson Sampling, we show that a locally determined randomness budget per arm suffices to retain $O(\log T)$ regret, demonstrating that synchrony, albeit with some randomness, is essential to the optimality of Thompson Sampling.

---


### 333. [SUPRA: Synthesizing Amyloid PET from MRI and Plasma Biomarkers with an Explicit Regional SUVR Prior](https://arxiv.org/abs/2611.33061)

**<font color=#1a73e8>作者：</font>** Hanwen Li, Fadi Deek, Zhi Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Amyloid positron emission tomography (PET) quantifies brain amyloid-$\beta$ as a standardized uptake value ratio (SUVR), but is costly and not widely available. Structural magnetic resonance imaging (MRI) is routine, and plasma biomarkers such as phosphorylated tau 217 (p-tau217) are becoming practical. Synthesizing amyloid PET from MRI alone is ill-posed, because brain anatomy reveals little about amyloid burden. We present SUPRA (SUVR prior-guided amyloid synthesis), which divides this task between MRI and plasma biomarkers. A regression maps the plasma panel to regional SUVR levels, painted onto the subject's MRI segmentation as an explicit prior. A 3D network then adds a residual correction guided by MRI. The output is in absolute SUVR, and the model also runs on p-tau217 alone. On the Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort (111 test pairs), SUPRA reaches a peak signal-to-noise ratio (PSNR) of 23.4 dB, against at most 20.7 dB for four published models, and rank correlations of 0.56 to 0.67 with true SUVR in the composite cortex, an early-accumulation region and the striatum, against at most 0.24. In a second, cognitively unimpaired cohort with other plasma platforms (143 test pairs), it reaches 22.8 dB and 0.32 to 0.61, against at most 21.4 dB and 0.20. Its area under the curve for amyloid positivity is 0.91 and 0.82, against at most 0.63. Ablations show that plasma supplies the amyloid information and the network the image quality. Combining MRI with a blood test yields synthetic amyloid PET that is realistic and tracks burden across regions.

---


### 334. [Uncertainty-Aware Candidate Generation for Entity Linking in Cyber Threat Intelligence](https://arxiv.org/abs/2611.33086)

**<font color=#1a73e8>作者：</font>** Nasser Alkhulaifi, Direnc Pekaslan, Christian Wagner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Entity Resolution (ER) pipelines often collapse ambiguity into early hard decisions: upstream Named Entity Recognition (NER) selects a single span and type, and downstream Entity Linking (EL) treats that choice as ground truth. This discards valuable information about the ambiguity of the underlying data (e.g., span boundary disagreement and type confusion), leading to brittle systems that fail unpredictably when faced with uncertainty in inputs. Therefore, this work presents a proof-of-concept for uncertainty-aware ER that treats uncertainty as native data that should be preserved and exploited throughout ER pipelines. We (i) capture uncertainty signals in the NER stage and (ii) leverage these signals into the EL stage to improve candidate retrieval under ambiguity. Using a BERT-based NER model augmented with two auxiliary span-boundary prediction heads, we apply Monte Carlo (MC) dropout at inference time to derive three mention-level proxy signals: the MC-averaged start-boundary probability, the MC-averaged end-boundary probability, and De Luca-Termini fuzzy entropy computed over the Begin-Inside-Outside (BIO) predictive distribution. These signals are used to adapt the fuzzy cutoff in candidate generation (CG) for EL. Because CG is treated as a blocking step, we evaluate retrieval recall. On the AnnoCTR dataset linked to the MITRE ATTCK knowledge base, the boundary-aware and dual-signal fuzzy linking approaches improve Recall@10 from 0.6186 to 0.7966. The contribution lies not in an end-to-end optimised ER pipeline but in establishing uncertainty preservation as a viable and beneficial component of ER pipelines, enabling downstream EL to make better-informed decisions under uncertainty.

---


### 335. [The Radar-based Activities of Daily Living (R-ADL) Dataset](https://arxiv.org/abs/2611.33088)

**<font color=#1a73e8>作者：</font>** Dominique Regli, Brian C. Williams  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monitoring Activities of Daily Living (ADLs) supports safety and well-being for people living at home, especially older adults, and radar sensing is gaining increasing attention in the field of activity recognition for its ability to ensure privacy in the home while also surpassing technical limitations of other sensing modalities. However, radar-based activity recognition remains constrained by the limited availability of large-scale datasets. We introduce the Radar-based Activities of Daily Living (R-ADL) dataset to addresses the gaps identified in existing work: 1) it expands the scale of available data by providing over eight hours of annotated recordings in which a person performs eight distinct activities; 2) it overcomes room configuration limitations by recording from five different locations in a two-bedroom, two-bathroom apartment; and 3) it extends beyond primitive actions to focus on high-level ADLs. In addition to the dataset, this paper introduces practical guidance for future ADL dataset construction. We conducted a detailed analysis of how ADLs are prioritized across academic research, health survey tools, and clinical trials to identify clinically significant ADLs. Furthermore, we provide our experimental design, data collection and annotation strategies, post-processing pipeline for forming the R-ADL dataset from raw data, and baseline results on standard machine learning architectures. The R-ADL dataset serves as a valuable resource for advancing ADL recognition systems as we continue building larger and more diverse datasets.

---


### 336. [EventDiffusion: Learning Native Event Stream Distribution from Videos](https://arxiv.org/abs/2611.33096)

**<font color=#1a73e8>作者：</font>** Karthik Sundar Senthilkumar, Christopher Thirgood, Simon Hadfield  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras capture asynchronous brightness changes at high temporal resolution, but scarce recordings constrain data-driven research. Sparse RGB observations cannot uniquely determine intervening events since identical frames may correspond to streams with different activity, polarities, and timing. Existing simulators largely rely on prescribed sensor dynamics and estimated brightness trajectories, whose assumptions limit the diversity and fidelity of plausible event streams. We introduce EventDiffusion, a hierarchical generative framework that directly learns the conditional distribution of native asynchronous event streams from real recordings. EventDiffusion decomposes generation into three probabilistic processes: Event Activity Diffusion (EAD) learns stochastic discrete event counts; Event Spatial Allocation (ESA) distributes these counts to individual pixels while preserving cardinality; and Event Timing Diffusion (ETD) learns continuous asynchronous timestamp distributions. We also introduce CEFS, an event-stream realism metric combining event activity and polarity with multiscale space-time structure and temporal fidelity. Across all datasets, EventDiffusion achieves double the accuracy of SOTA methods and demonstrates robustness across different cameras at any resolution.

---


### 337. [GREMLIN: Generating Random Environments for Meta-Learning with Interacting Networks](https://arxiv.org/abs/2611.33101)

**<font color=#1a73e8>作者：</font>** Octave Gaspard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can randomly parameterized neural environments supply useful experience for learning a reinforcement learning algorithm? We investigate this question using DiscoRL's rule-discovery framework, replacing human-designed training games with sixteen selected neural environments. Each game combines bounded vector dynamics with a random strategy-based reward and an independent outcome reward. After 224.8 million agent-environment steps, we froze the teacher and trained fresh agents. DQN outscored GREMLIN on most games, both generated and human-designed. GREMLIN nevertheless outperformed the untrained teacher on all 26 games, showing that generated experience can improve a learning rule. It remains unclear whether this approach can yield a competitive rule with longer meta-training.

---


### 338. [Reinforcement Learning Can Be Recovered From Its Own Rollouts](https://arxiv.org/abs/2611.33102)

**<font color=#1a73e8>作者：</font>** Jiayi Sheng, Jingwen Gu, Guanning Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Broadly speaking, reinforcement learning (RL) post-training converts compute into model capabilities by training on model-generated data. Typically, the rollouts are discarded after each update, and the knowledge acquired during RL resides in the model weights. In this work, we investigate how much of this knowledge is retained in the rollouts themselves. A natural first attempt is to replay the original RL algorithm on archived rather than freshly generated rollouts, but this leads to catastrophic collapse. We provide a simple explanation for this phenomenon, which in turn suggests a remedy: maximum likelihood on the archived rollouts. Surprisingly, starting from the same base model and replaying the rollouts in the order in which they were generated, without any distinction between correct and incorrect responses, is sufficient to recover the performance of online RL. In fact, a single maximum likelihood update per rollout batch closely tracks the entire learning curve of online RL. Furthermore, maximum likelihood on the rollouts of the last few RL steps often suffices to recover the final model's performance. This suggests that much of the compute invested in RL goes into discovering an improved sampling distribution rather than learning it from samples.

---


### 339. [Temporal Conditioning for Human Behavioral Cloning in Chess](https://arxiv.org/abs/2611.33106)

**<font color=#1a73e8>作者：</font>** Victor Dziwniel, Tianxiang Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavioral cloning models in chess typically predict human moves from board states while ignoring temporal inputs such as the remaining clock. However, time pressure is a major determinant of human decision-making quality, and temporal state is a missing dimension of human behavioral modeling. This paper introduces a time-aware transformer that extends a Chessformer-style architecture with learned temporal conditioning tokens encoding player clock state, time control, and recent tempo, together with behavioral heads for thinking time and resignation. The model is trained on large-scale online chess data and evaluated against time-agnostic baselines and the state of the art. Results show that temporal conditioning yields modest overall accuracy improvements but substantially stronger gains under time pressure. Beyond move choice, it also produces more accurate thinking-time and resignation predictions. More importantly, the model better matches human move-quality degradation in critical time regimes, reducing the systematic over-strength observed in time-agnostic behavioral cloning models. These results suggest that temporal state is a previously underutilized but important signal for human behavioral cloning in chess.

---


### 340. [RenGen: Generating Images with as Many Tokens as the Scene Needs](https://arxiv.org/abs/2611.33109)

**<font color=#1a73e8>作者：</font>** Savya Khosla, Jay Mahajan, Akin Tuna Sakalli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RenGen, a latent diffusion model that generates simple scenes from a few tokens and busy scenes from many, saving time and compute on simple scenes without losing realism. Most latent generators represent every image as a fixed grid of patch tokens, so a simple image costs as much to generate as a complex one. Prior methods that vary the token count through content-adaptive tokenization lose image quality as the count shrinks. RenGen instead trades scene complexity, rather than image quality, for fewer tokens. It does so by generating in the latent space of a pretrained region encoder, where each token represents one region of the image, and a decoder renders these region tokens back into pixels. Unlike patch tokens, region tokens cover areas of varying shape and position, so each token must capture both what its region contains and where it lies on the image canvas. We encode this spatial extent by adding positional embeddings to the encoder features before pooling, and we generate it by anchoring each token to a single randomly sampled point, from which the generator infers the region's shape, size, and content. At sampling time, the number of anchor points sets the trade-off between scene complexity and compute. On ImageNet $256{\times}256$, RenGen reaches a gFID of 1.34 with 88 tokens per image on average, the best among methods that vary their token count. It approaches the quality of RAEv2, a state-of-the-art patch-based model, at $2.5{\times}$ lower latency, advancing the Pareto frontier of generation quality versus compute. RenGen's gFID stays flat across scene complexity while latency varies by $2.4{\times}$ between simplest and busiest scenes, and its autoencoder reconstructs nearly as well as RAEv2 (rFID 0.32 vs. 0.30) with $2.9{\times}$ fewer tokens.

---


### 341. [One Take, Many Cameras: Audio-Grounded Shot Synthesis for Dialogue Re-Cinematography](https://arxiv.org/abs/2611.33147)

**<font color=#1a73e8>作者：</font>** Anthony Chen, Naomi Ken Korem, Matan Ben-Yosef 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creating a dialogue scene typically requires cutting between multiple views (e.g., close-ups, medium shots, and over-the-shoulder shots) of the actors. Yet capturing such coverage is costly and in many settings unavailable. We study dialogue re-cinematography: synthesizing additional shots from a single wide-angle dialogue video. Existing video generators can synthesize new shots, but rely on visual cues alone, so when the source video barely shows the lips, the generated lip motion fails to match the speech. Our key observation is that the speech audio is view-invariant: it constrains lip motion in any target view. Building on this insight, we adapt a pretrained audio-visual diffusion model to generate the new shot from a target frame that specifies the view, a source video that contains the performance, and the speech audio that drives lip motion. In multi-person scenes, however, pretrained audio-visual models drive every visible face with the same speech, causing speech leakage, where silent listeners mouth the speaker's words. We therefore introduce speaker-aware audio gating, a training-free module that lets the audio drive only the faces that speak in the target shot. On a cinematic paired-view benchmark spanning diverse viewpoints and framings, our method lowers perceptual error by 59%, landmark error by 56%, and speech leakage by 97% relative to the strongest baseline, Wan 3.0. Our method also remains robust on in-the-wild scenes, highlighting its potential for film post-production.

---


### 342. [PointX: Multi-View Consistent Intrinsics by Querying Surface Points](https://arxiv.org/abs/2611.33157)

**<font color=#1a73e8>作者：</font>** Miguel Farinha, Sam Sartor, Iliyan Georgiev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The appearance of a scene is determined by the albedo, roughness, metallicity and normal of every point on its surface, and by the light that reaches it, its irradiance. Recovering these intrinsics from images is ambiguous, and methods that predict them per pixel give the same surface point a different decomposition in every view. We introduce PointX, a simple feed-forward model that predicts intrinsics per 3D surface point instead. A multi-view transformer encodes a set of unposed images, and for any queried surface point, PointX pools the point's tokens across the views in which it appears and decodes the point's intrinsics once. Each point of a 3D reconstruction of the scene, such as a point cloud or a mesh, thus receives a single prediction, which is exactly consistent across views by construction and enables view-consistent relighting and editing. The same model also predicts per-view maps, from one image or many, by querying the point seen at every pixel. These maps agree across views up to the precision of the estimated geometry and correspondences. PointX is significantly more consistent than existing methods, while remaining competitive in accuracy from a single image and improving as views are added. Project page: this https URL

---


> [!TIP]
> 当前位于：**301-342**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-342**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
