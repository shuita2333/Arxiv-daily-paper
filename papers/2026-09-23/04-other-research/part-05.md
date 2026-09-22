# 📦 其他研究 | 2026年09月23日

> 本类共 **463** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

---

### 201. [Blind Thermodynamic Ontology Discovery from Anonymous Experiments](https://arxiv.org/abs/2609.23387)

**<font color=#1a73e8>作者：</font>** Linzhe Zhang, Changming Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Before a machine learning model can learn a thermodynamic equation of state, it must discover what its measurements represent: which channels scale with system size, which are intensive conjugates, how sectors pair through contact, and which potential governs stability. When sensors expose only an unknown linear mixture of extensive states and intensive responses, passive observations cannot disentangle physical quantities from coordinate artifacts. We formulate the problem of discovering this hidden thermodynamic ontology directly from anonymous controlled experiments. We present an operational identifiability theory and a constructive polynomial-time algorithm that extracts extensive and intensive scaling sectors from replication contrasts, recovers their dual cotangent pairing from thermal contact and reciprocity, verifies a globally admissible concave potential via discrete cyclic concavity, and determines an invariant matroid of reservoir ensembles. We prove that the residual observational equivalence is strictly (x, lambda) ~ (A x, a A^{-T} lambda + beta), establishing the sharp observational limit that no permitted experiment can break. Blind evaluations on van der Waals fluids and Curie-Weiss magnets confirm robust recovery under ill-conditioned mixing, correctly resolving anonymous Maxwell tie-lines while rejecting non-equilibrium continuations. External validation across six real fluids from the NIST WebBook demonstrates that operational ontology discovery transfers across real physical substances without coordinate leakage.

---


### 202. [CLOADER: Evading Security Mobile Defenses via Runtime Obfuscation and Adaptive Hooking Tactics](https://arxiv.org/abs/2609.23396)

**<font color=#1a73e8>作者：</font>** Nhat-Anh Huynh, Minh Quang Luu, Ngoc Hong Tran  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose a stealth framework that eliminates detection of hooking tools such as Frida and Xposed in secured mobile environments by replacing static configurations with dynamic evasion tactics. In contrast to existing approaches that apply these techniques independently, the framework introduces a unified runtime control layer that systematically coordinates network, temporal, and code-level evasive transformations. The solution integrates randomized port allocation, runtime code obfuscation, delayed execution triggers, and self-integrity checks to disrupt signature-based scans, timing heuristics, and tampering attempts. A custom Android loader, CLoader, enforces these mechanisms to isolate hooking activities from security monitors while maintaining complete interception and modification capabilities. Validation across enterprise anti malware systems, hardened applications, and device management platforms demonstrates a 90% bypass rate in our evaluation matrix. This approach enables reliable penetration testing and malware analysis in locked-down mobile ecosystems by masking network, temporal, and code-level fingerprints without architectural overhauls.

---


### 203. [Enhancing Shrimp Disease Detection via Deep Learning and Data Refinement for Resilient Aquaculture](https://arxiv.org/abs/2609.23397)

**<font color=#1a73e8>作者：</font>** Vinh Canh-Thanh Truong, Hai-Binh Pham, Ngoc Hong Tran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shrimp diseases continue to cause devastating losses in the aquaculture industry, driving a critical need for robust, automated detection. This work contributes the first application of Vision Transformers (ViT) and Self-Supervised Learning (SSL) to the shrimp farming domain, addressing both performance bottlenecks and data labeling challenges. We propose two deep learning pipelines to classify four key diseases: Healthy, Black Gill (BG), White Spot Syndrome Virus (WSSV), and a co-infection of both using a dataset of 4,348 images. First, our supervised transfer-learning approach leverages ImageNet-pretrained ViT-Small/16 and EfficientNet backbones. Second, we introduce a contrastive learning framework (SimCLR) with a ViT-Small encoder to extract robust representations from unlabeled images prior to fine-tuning. Our results establish strong new baselines for sustainable aquaculture monitoring. The supervised approach achieves an outstanding 96% accuracy with fast convergence, outperforming traditional generic models, while the label-efficient SSL approach reaches a highly competitive 85% validation accuracy.

---


### 204. [Alignment and Divergence between Humans and AI in Interpersonal Privacy Decisions](https://arxiv.org/abs/2609.23403)

**<font color=#1a73e8>作者：</font>** Hanxiang Zeng, Shuning Zhang, Xinyuan Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI assistants increasingly mediate interpersonal communication on behalf of their primary user, but they risk violating the privacy expectations of third-party information owners. Resolving these tensions requires understanding how humans anticipate interpersonal privacy boundaries. Therefore, we conducted a dyadic study (N=76) and a matched evaluation of AI models across 18 information types and 3 recipient relationships. We found that data owners' privacy judgments are highly contextual and relationship dependent. While familiar data co-owners show meaningful alignment with owners' expectations, they significantly overestimate the need for permission. Interestingly, greater familiarity within the owner-co-owner dyad was associated with both higher disclosure acceptability and lower co-owner misalignment, whereas our exploratory four-item empathy measure was not. In contrast, AI models significantly underperform human co-owners in anticipating the data acceptability, even when provided with within-dyad examples. These findings underscore a core HCI design challenge to develop privacy-aware AI that respects multi-stakeholder information boundaries.

---


### 205. [ScaleBlind: Point Cloud Completion under Unknown Scale](https://arxiv.org/abs/2609.23404)

**<font color=#1a73e8>作者：</font>** Shenghui Wu, Chen Wang, Yuan Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud completion aims to infer a complete 3D shape from a partial point cloud and serves as a fundamental building block for downstream tasks such as reconstruction, editing, and simulation. Despite the recent progress, existing learning-based methods often implicitly rely on access to the ground-truth shape scale (GT-scale) during both training- and testing-time normalization, assuming privileged information that is unavailable in real-world inference. This hidden assumption limits practical deployment and can lead to severe completion artifacts, e.g., over- or under-completion and nested shells, once the oracle GT-scale cue is removed. We observe that the recent foundation image generation models exhibit a strong capability of understanding objects and geometries, and producing multi-view consistent renderings, making them promising priors for GT-scale-free 3D completion. Motivated by this insight, we propose ScaleBlind, a novel framework that leverages foundation-model-based image completion to recover global scale directly from partial inputs and then faithfully produces the 3D completion. Specifically, ScaleBlind dreams out complete multi-view appearances from rendered partial views, lifts the inferred missing regions back into 3D to obtain a geometry-aware coarse completion, and further refines it via a powerful cross-modal fusion network with the original partial point cloud. By harnessing 2D foundation priors, our method eliminates the need for accessing GT-scale information at inference. Moreover, it provides a principled bridge between 2D generative priors and 3D point cloud completion. Extensive experiments demonstrate the superiority of our framework, making ScaleBlind the new state-of-the-art for the point cloud completion task.

---


### 206. [The Anatomy of Address Poisoning on Ethereum: Funding Mechanisms, Scam Signatures, and Laundering via Tornado Cash](https://arxiv.org/abs/2609.23405)

**<font color=#1a73e8>作者：</font>** Son Hoang Dau, Thanh Nguyen, Phuong Duy Huynh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Address-Poisoning Transfer (APT) is a prevalent blockchain phishing scam in which a scammer poisons a victim's address book by generating a transfer with a phishing address that looks similar to a benign address that the victim has previously interacted with. Although simple, APT phishing attacks have cost users millions of dollars in recent years, which has captured the attention of the research community (Ye et al. WWW'24, Guan-Li CCS'24, Chen et al. NDSS'25, Tsuchiya et al. USENIX'25). In this work, we go beyond detection and investigate three important and underexplored aspects of APT: scam funding mechanisms, scam signatures, and scam proceeds laundering via public services. In particular, we propose five families of scam signatures that capture key aspects of APT operations, which are useful for address clustering. We also conduct the first investigation into usage of Tornado Cash for funding APTs and laundering scam proceeds.

---


### 207. [Accurate Motion Estimation with Bézier Control Point for Efficient Frame Interpolation](https://arxiv.org/abs/2609.23408)

**<font color=#1a73e8>作者：</font>** Shuhao Han, Chenyang Wu, Chun-Le Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In frame interpolation tasks, motion ambiguity in the training set causes models to generate blurry intermediate frames. Moreover, the assumption of uniform motion between frames during inference further leads to inaccuracies in the generated intermediate frames. To tackle these challenges, we propose an Accurate motion estimation algorithm with Bézier Control point, ABC-Inter, for efficient frame Interpolation. Specifically, ABC-Inter designs an Accurate Flow estimation Module (AFM) by decoupling two-frame features and mapping to corresponding coordinates to better estimate the optical flow between the two frames. Furthermore, ABC-Inter eliminates motion ambiguity in the training set by introducing Bézier control points that are computed using the input frames and the intermediate ground-truth (gt) frames. This allows the model to estimate accurate optical flow between two frames during the training process, thereby solving the blurriness problem in the generated intermediate frames during inference. Benefiting from the more accurate flow estimation between two frames, we can introduce additional frames and directly use multiple flows to calculate Bézier control points for modeling non-uniform motion without retraining the model. Simultaneously, to realize the estimation of non-linear motion using only two frames, we also introduce a new Bézier control point estimation module which achieves better motion estimation between the two frames by performing fine-tuning on the model in the second stage. Experimental results demonstrate that our ABC-Inter achieves state-of-the-art performance on multiple benchmark datasets and exhibits excellent visual perception.

---


### 208. [Retrieval Geometry Shapes Cache-Based Clip Adaptation](https://arxiv.org/abs/2609.23409)

**<font color=#1a73e8>作者：</font>** Mahir Shahriar Tamim, Md. Samiul Alim, Azmine Toushik Wasi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cache-based test-time adaptation improves CLIP predictions by storing and retrieving examples from the target stream while keeping the model frozen. However, existing methods largely treat the feature space used for image-image retrieval as fixed, leaving open how much adaptation depends on the retrieval space itself. We study this question by fixing the memory and changing only the retrieval encoder, finding that the same memory can yield very different gains: across sixteen retrieval spaces, ImageNet-A cache gain ranges from at most +0.44 points for CLIP and MAE to +19.7 +/- 0.4 for DINOv2-L, while label-free retrieval-space selection retains 98% of oracle gain on ImageNet-V2. These results show that memory quality depends not only on which examples are stored, but also on how they are retrieved. Motivated by this finding, we propose MARC (Memory Augmented Retrieval for CLIP), a training-free system that uses frozen CLIP for prediction and DINOv2-B for retrieval with a single fusion weight. A single-view cache repairs 1074 +/- 21 baseline errors, compared with 878 +/- 4 for a 64-view ensemble, at roughly one seventh of the cost. Across four ImageNet distribution shifts, MARC reaches a 67.91% OOD average and, at matched DINOv2-B scale and eight views, achieves 64.17 +/- 0.31% versus 62.75 +/- 0.15% for a graph-based cache system while running 2.6 times faster. Overall, our results establish retrieval space as a first-order design choice for robust cache-based adaptation in remote sensing, scientific imaging, and changing visual environments.

---


### 209. [Semi-automated reconstruction of indoor geometry from 360-degree video for CFD-based airflow analysis in classrooms](https://arxiv.org/abs/2609.23425)

**<font color=#1a73e8>作者：</font>** Dhruv Gamdha, James Afful, Shambhavi Joshi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computational Fluid Dynamics (CFD) is widely used to evaluate ventilation and contaminant transport in occupied buildings, but deployment at scale is limited by three bottlenecks: acquiring room geometry without costly scanning hardware or manual CAD modeling, decomposing the scene into individually manipulable objects, and reconfiguring those objects for alternative layouts without re-capturing the room. We present a semi-automated workflow that converts a single 360-degree video of a room into individually editable, simulation-ready geometry assets. A dense point cloud is reconstructed using Neural Radiance Fields (NeRF), and 2D instance masks from text-prompted SAM 3 segmentation are lifted to 3D using multi-view consensus and depth-band filtering. Points are separated into object instances with an octree, and occlusion gaps are healed with a connectivity graph. Chair templates are fitted by Iterative Closest Point (ICP) alignment, and table geometry is generated procedurally. A browser-based editor supports quality assurance and rapid construction of alternative layout configurations. A steady Reynolds-averaged OpenFOAM solution then drives transient passive-scalar transport; the setup is verified using a mesh-sensitivity study and validated against an IEA Annex 20 benchmark. We apply the workflow to two university classrooms and a tiered lecture-hall auditorium. The capture-to-geometry pass takes two to five hours per room on a consumer workstation. In a controlled obstruction sequence in one classroom, the modeled half-clearance time varies non-monotonically as furniture is added, and a cross-room comparison indicates that clearance behavior cannot be reliably extrapolated between rooms, motivating per-room geometry acquisition. By making that acquisition low-cost, the workflow makes geometry-resolved comparative ventilation studies practical for spaces such as classrooms.

---


### 210. [GAPS: Generative Active Pseudo-view Selection for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.23436)

**<font color=#1a73e8>作者：</font>** Hongfei Zhu, Haochen Deng, Sitao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis from sparse observations is severely under-constrained. Although 3D Gaussian Splatting (3DGS) enables real-time rendering, it produces floaters, broken geometry, and washed-out backgrounds when trained with few views. We propose an alternating optimization framework that uses a pre-trained image diffusion model to generate geometrically consistent pseudo-views for additional 3DGS supervision. Generation is constrained by depth-conditioned ControlNet, IP-Adapter style transfer, LoRA scene adaptation, and img2img structural anchoring. We introduce Generative Active Pseudo-view Selection (GAPS) to balance reconstruction informativeness and generative reliability when choosing target views. Its annealing schedule shifts from conservative interpolation early in training to exploratory extrapolation later, gradually covering unobserved regions. A dual-criterion admission gate and uncertainty-weighted losses reject unreliable generations, while density-adaptive DropGaussian reduces overfitting in complex scenes. On LLFF with 3/6/9 views, our method improves average PSNR over vanilla 3DGS by 0.40/0.89/0.70 dB. On Mip-NeRF 360 with 12/24 views, the gains are 1.18/0.80 dB. SSIM improves and LPIPS decreases in every setting. Ablations show that active selection and density-adaptive regularization are both necessary; only the full method reduces LPIPS below the no-pseudo-view baseline on unbounded 360-degree scenes.

---


### 211. [PhysReflect: Geometry and Perception Guided Diffusion for Physically-Plausible Mirror Reflections](https://arxiv.org/abs/2609.23442)

**<font color=#1a73e8>作者：</font>** Shuheng Ge, Hongwei Ren, Li Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models generate high-quality images, yet often violate the physical laws governing mirror reflections. Reflections often suffer from geometric aberrations, including positional offsets, directional misalignment, proportional imbalance, and structural distortion. These failures remain evident even in contemporary state-of-the-art generative systems. Existing methods itigate this problem through synthetic data scaling or auxiliary depth conditioning, yet their merely reliance on latent-space noise reconstruction losses as implicit supervision prevents direct enforcement of reflection-specific geometric and perceptual constraints. To bridge this gap, we present PhysReflect, a geometry and perception guided diffusion framework that decodes the predicted clean latent into pixel space at each training step and applies annealed supervision through two complementary differentiable objectives. The Geometric Loss enforces mirror-induced spatial consistency through sparse epipolar correspondence and dense boundary projection alignment, where a SAM2-based TwinTrack mechanism provides stable in-mirror localization for boundary-aware supervision. The Perceptual Loss preserves reflected appearance by combining Semantic Consistency Loss, which maintains reflected identity and appearance via DINOv2 features, and Lighting Consistency Loss, which regularizes depth, surface-normal, and illumination coherence under monocular geometry priors. Experiments on synthetic and real-world benchmarks show that PhysReflect outperforms prior mirror-reflection methods in geometric, perceptual, and physical-plausibility metrics, as well as qualitative visual results.

---


### 212. [Rule-Constrained Assignment for Cue-Ball Identification in Broadcast Snooker](https://arxiv.org/abs/2609.23450)

**<font color=#1a73e8>作者：</font>** Yuxin Cao, Wei Song, Yuezhong Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate cue-ball identification is essential for metric analysis of broadcast snooker. Existing systems evaluate each candidate independently against a fixed white prototype and reject candidates above an appearance threshold. Under broadcast conditions, illumination changes can make colored balls appear white, while intrusions from players and equipment can obscure the cue ball or introduce competing candidates. We formulate cue-ball identification as a rule-constrained assignment problem that jointly assigns detected candidates to the bounded snooker inventory: one cue ball, up to 15 reds, and six colors with known spots. The cue ball is selected by the incremental cost of assigning each candidate to the white slot, and the conventional appearance test follows as the one-slot case. On 419 hand-annotated shots, our method improves identity accuracy from 88.1% to 95.5%, and from 80.5% to 95.2% on held-out venues. Within CueLift, our metric state-recovery system, the assignment expands coverage from 36.2% to 55.4% over 6,241 scorable shots. Assigning an estimate to every shot in a separate evaluation on 2,529 shots preserves this advantage.

---


### 213. [RLVR$^{2}$: Reinforcement Learning with Verifiable Rubric-based Ranking](https://arxiv.org/abs/2609.23457)

**<font color=#1a73e8>作者：</font>** Hao Li, Zhengkun Zhang, Gangqiang Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) is expanding from tasks with well-defined correctness signals, such as mathematics and code, toward multifaceted quality requirements specified by multi-dimensional rubrics. Since policy optimization consumes one scalar per rollout, rubric-based pipelines must map multiple criterion scores into a scalar reward. This aggregation is often treated as score scaling, but it implicitly determines how quality dimensions trade off during training. The prevailing practice, normalizing each criterion and taking a linear combination, assumes that cardinal score differences are comparable across criteria and that gains on one criterion compensate for failures on another; both assumptions are unreliable when criteria are semantically heterogeneous. We propose Reinforcement Learning with Verifiable Rubric-based Ranking (RLVR$^2$), a verifiable ranking paradigm for rubric-based RLVR. For each criterion, RLVR$^2$ converts rubric scores into criterion-specific within-group ordinal outcomes, recovers a latent utility from the resulting comparison matrix, and merges these utilities into one training signal. By retaining only within-group ordering and discarding raw score magnitudes, RLVR$^2$ avoids calibrating heterogeneous rubric scales. It further supports objective-preserving attribute adjustment: auxiliary attributes that correlate with observed rankings but are not training objectives can enter the estimation without expanding the rubric or rewarding them directly. Across three model scales and 16 benchmarks, RLVR$^2$ consistently outperforms representative rubric-based baselines, achieving the best overall performance on most benchmarks at every scale. Analysis shows it controls systematic effects tied to reasoning efficiency and response formatting while preserving the quality objective.

---


### 214. [TRACE: Tractable Routing Autoencoder for Clinical ECG](https://arxiv.org/abs/2609.23460)

**<font color=#1a73e8>作者：</font>** Shunbo Jia, Runze Ma, Haonan Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has advanced automated electrocardiogram (ECG) diagnosis, but the field's most accurate models, foundation models pretrained on millions of recordings, are not decision-pathway auditable: a clinician cannot trace a diagnosis to a physiological pathway or intervene on one. We propose TRACE, a Tractable Routing Autoencoder for Clinical ECG, whose 32-dimensional clinical latent space is specified in advance from domain knowledge rather than discovered by optimization. TRACE partitions this space into perfusion, structure, and conduction subspaces, routes each to its own diagnostic head by design, regularizes the partition with an orthogonality penalty, and reconstructs the ECG through a decoder that permits latent perturbation. On PTB-XL and Georgia, TRACE exceeds unconstrained classifiers and stays ahead of an ECG foundation model pretrained on ten million recordings, evaluated by linear probe on frozen features, at roughly an eighth of the parameter count. On the nine-label CPSC2018 cohort, which carries no structural class, the framework transfers with only the routing table re-specified to a perfusion/rhythm/conduction partition. Joint probe, erasure, and perturbation analyses verify the routing contract, and perturbing the depolarization and repolarization pathways modulates the reconstructed waveform. Removing the specified partition and its orthogonality penalty costs 1.70 AUC and 11.30 macro-F1 points on PTB-XL, and 2.76 AUC and 16.92 macro-F1 points on Georgia. A capacity-matched permutation control places arbitrary assignments within 0.34 AUC points of the ontology routing and leaves macro-F1 statistically level (p=0.619): the ontology supplies decision-pathway auditability at no macro-F1 cost.

---


### 215. [Perplexity Predicts Protection: Choosing Pretrained Backbones for Worst-Client Fairness in Federated Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2609.23463)

**<font color=#1a73e8>作者：</font>** Kiran Naseer, Samreen Azhar, Umar Shoaib 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Federated learning lets multiple parties train a shared model without pooling their data, but a client with far less data than the others can end up poorly served even when the group's average accuracy looks fine. We ask whether the choice of pretrained backbone affects this under LoRA fine-tuning, and whether per-word perplexity on the target text predicts which backbone helps the worst-off client before federated training starts. We ran 313 experiments across three text-classification datasets and three similarly sized backbones (RoBERTa, BERTweet, PubMedBERT), each compared against a task-specific baseline on identical data splits. Lower-perplexity backbones consistently produced larger gains for the worst-performing client, with a rank correlation of -0.87 across nine dataset-backbone pairs; a backbone held out of the analysis confirmed the pattern. Personalization with Ditto recovered only 4-12% of the gap between training alone and full federation, and removing aggregation entirely erased the benefit. A client's update also showed no sign of conflicting with the group's update; the two are close to orthogonal, ruling out one proposed explanation for this failure. Practically: measure perplexity on a sample of task text before choosing a backbone, and do not rely on personalization to protect a data-poor client. We release our code, predictions, and full results for others to test.

---


### 216. [Propose, Verify, Commit: Evidence-Grounded Memory for Long-Horizon Multi-Actor Conversations](https://arxiv.org/abs/2609.23465)

**<font color=#1a73e8>作者：</font>** Zihao Lu, Zhihang Yuan, Lei Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon conversational memory is especially challenging in multi-actor settings, where relevant evidence is distributed across participants and contexts and previously established information may later be revised. We introduce EGMEMORY, which formulates long-horizon multi-actor memory as a searchable state machine that separates persistent message-level evidence from an explicit active state. At write time, adaptive state resolution and an evidence-grounded propose-verify-commit protocol govern how this state evolves. At read time, adaptive evidence navigation iteratively resolves the state and supporting evidence required for a query, using conversational structure to narrow the search space and lexical-semantic relevance to rank candidates. The system operates through prompting and tool use without memory-specific policy training. EGMEMORY achieves 68.2% on GroupMemBench and 77.9% on EverMemBench, outperforming the strongest evaluated baselines by 22.7 and 21.4 percentage points, respectively. It further reaches 73.6% on the dyadic LoCoMo benchmark, demonstrating generalization beyond multi-actor conversations. We will release the codebase upon formal publication.

---


### 217. [Algebraic Consistency Alone Does Not Certify Temporal Structure in Latent Action Models](https://arxiv.org/abs/2609.23478)

**<font color=#1a73e8>作者：</font>** Di Wen, Ruodi Zhang, Kailun Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent action models infer a code for the transition between two frames of action-free video. Recent methods regularise this code to compose additively and reverse antisymmetrically, and report order-of-magnitude reductions in the resulting errors as a label-free certificate that the code has captured temporal structure. We show that this conclusion does not follow. Reconstruction drives the decoded transition toward a difference of state features, for which both identities hold for any pairing, a solution the metric cannot distinguish from one encoding nuisance state or a coordinate convention. Across five source domains, a trained but unconstrained counterpart already achieves 83-97% of the reduction relative to an untrained anchor. The residual fold is governed as much by the decoder family as by what is learned. A constrained model retrained after its temporal pairing is destroyed still reaches, in each domain, a lower error than the unconstrained model on real data. Downstream, preserving the temporal pairing yields no consistent advantage on LIBERO-GOAL or LIBERO-SPATIAL, and across the tested arms the code's mean linear action decodability falls as the algebraic error improves. We also test the most direct repair, a violation-contrastive objective that requires the algebra to fail on destroyed pairings: in the tested configurations it yields only a marginal separation within the reconstruction budget, on training and test triples alike. We recommend a validation protocol that these methods currently lack: a baseline-corrected metric, retraining on destroyed pairings, and a seed-budget analysis.

---


### 218. [CE$^4$L: Continual Ego, Exo, and Ego-Exo Learning](https://arxiv.org/abs/2609.23492)

**<font color=#1a73e8>作者：</font>** Hongwei Yan, Kanglei Zhou, Yuchen Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perception for embodied agents is video-based, often multi-view (ego, exo, or both), and inherently continual, with simultaneous task and viewpoint shifts. Yet continual learning (CL) remains dominated by exo-only recognition tasks, obscuring behavior under these real-world coupled shifts. We introduce Continual Ego, E}xo, and Ego-Exo Learning (CE$^4$L), a unified multi-view CL benchmark spanning four representative tasks: cross-view referenced skill assessment, temporal action segmentation, cross-view association, and action anticipation & planning. CE$^4$L highlights challenges largely absent in prior CL benchmarks, including cross-view correspondence, view-dependent asynchrony, and heterogeneous semantic objectives. To this end, we propose Video Incremental Subspace-routed Task Adapters (VISTA), a parameter-efficient baseline method that stores task-specific updates in lightweight adapters and performs training-free routing via residual distance to task-specific whitened subspaces estimated from second-order statistics. Extensive experiments demonstrate the significantly varied efficacy of representative CL methods across CE$^4$L settings, while VISTA is consistently competitive and achieves state-of-the-art overall performance. Our source code for benchmarks and methods is available at this https URL .

---


### 219. [Detecting Phone-Induced Pedestrian Distraction via a Multimodal Fusion Transformer](https://arxiv.org/abs/2609.23507)

**<font color=#1a73e8>作者：</font>** Yuanzhe Li, Hounian Liu, Xiaotong Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The increasing reliance on mobile phones has made phone-induced pedestrian distraction increasingly prevalent. Activities such as texting, watching videos, and making phone calls have become significant contributors to traffic accidents. Reliable detection of pedestrian distraction is essential for autonomous vehicles, as it improves situational awareness and enables timely risk assessment, thereby supporting safe motion planning and vehicle control. We propose a multimodal fusion Transformer (MFT) for detecting phone-induced pedestrian distraction. MFT jointly extracts skeletal dynamics from body pose keypoints and visual appearance features from pedestrian images, effectively leveraging the complementary information provided by the two modalities. A cross-modal attention module is proposed to capture inter-modal dependencies through multi-head cross-attention, facilitating effective fusion of complementary information across the two modalities. Then, a temporal attention fusion module, implemented with a Transformer encoder, is employed to capture temporal dependencies. MFT is trained and evaluated on a manually annotated dataset comprising 287 pedestrian instances with 20,741 images. Extensive experiments demonstrate that MFT attains an overall accuracy of 95%, exceeding the performance of six baseline approaches by 6%.

---


### 220. [Heating in human-HVAC interaction for smart homes: An interdisciplinary overview](https://arxiv.org/abs/2609.23508)

**<font color=#1a73e8>作者：</font>** Delong Korus-Du, Gunnar Stevens, Alexander Boden 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As part of HVAC systems, residential heating provides foundational infrastructure for human habitation in cold weather. However, research on how residents interact with HVAC systems, particularly heating systems, remains fragmented across architecture, engineering, informatics, physiology, psychology, sociology, and design. Based on 541 studies from these fields, this review integrates interdisciplinary research on Heating in Human-HVAC Interaction in smart this http URL resulting synthesis is conceptualized through the Situated Interaction Dynamics of control and feedback between users and systems. User-initiated interactions involve monitoring past and present system performance and planning future operation, while system-initiated interactions rely on sensor networks to trigger automation or provide information enabling user action. These interaction dynamics connect Residents' Experience and Practices with Heating in HVAC System Mechanics. Residents' Experience and Practices include thermal comfort and energy management, where thermal comfort involves both individual physiological and psychological experiences of indoor climate and social practices shaped by norms, empathy, and negotiation among cohabitants. Heating in HVAC System Mechanics includes thermal conditions and energy performance. Thermal conditions concern the regulation of air temperature, mean radiant temperature, air velocity, and relative humidity, while energy performance concerns efficiency and environmental impact. This overview highlights four interdisciplinary tensions: sensed versus lived conditions, personalization versus negotiation, efficiency versus health, and automation versus agency. The resulting framework offers a conceptual lens to interpret heating interactions and design Human-HVAC Interaction that balances IEQ-driven healthy thermal conditions, affordability, and sustainability.

---


### 221. [GARO: Geometry-Aware Redundancy Optimization for Real-Time and High-Fidelity Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.23509)

**<font color=#1a73e8>作者：</font>** Huiwen Xue, Kaixing Zhao, Zuheng Ming 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis is a key task for dynamic scene reconstruction, where high rendering speed is essential for applications such as virtual reality. Existing deformable Gaussian Splatting methods achieve high-fidelity dynamic scene modeling, but still face limitations in memory usage and rendering efficiency due to the large number of redundant Gaussians. To address these challenges, we propose Geometry-Aware Redundancy Optimization (GARO), a unified redundancy measurement framework in the adaptive density control stage of the traditional dynamic scene reconstruction pipeline. This framework first selects low-gradient candidates using an optimization activity assessment strategy, and then evaluates geometric complexity through low curvature analysis to further filter and prune redundant points, resulting in a compact and expressive Gaussian representation. Extensive experiments on synthetic and real-world datasets demonstrate that GARO achieves robust trade-offs between quality and speed, with PSNR remaining stable and rendering speed improved by 2x, validating the efficiency and effectiveness of GARO.

---


### 222. [Endogenous Interpretation](https://arxiv.org/abs/2609.23514)

**<font color=#1a73e8>作者：</font>** Antonio Nappa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose endogenous interpretation: program, interpreter, machine, and derived execution language are not disjoint semantic objects but different parameterizations of one executable state-transition relation. Each realization carries an implicit constraint bias, the structural restrictions imposed by its instruction basis, state encoding, control transfers, and finite substrate. From this viewpoint the "semantic gap" metaphor is misleading for operational semantics: a semantics-preserving transformation cannot remove the computation required for execution; it redistributes it over another state space and transition granularity (semantic diffusion). Reverse engineering is then the recovery of a lower-complexity semantic contraction.
We give a first quantitative instance. For finite-state realizations observed up to bisimulation, the contraction is canonical and computable in almost-linear time, yielding an abstraction-independent diffusion ratio; for deterministic realizations this extends to trace equivalence. For nondeterministic realizations observed up to traces, minimal contraction is

---


### 223. [ITSY: Causal Discovery From Irregular Time-Series Data](https://arxiv.org/abs/2609.23516)

**<font color=#1a73e8>作者：</font>** Wenbo Xu, Yue He, Yunhai Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structural causal models for time series recover contemporaneous and lagged effects, but most methods require complete observation windows and become misspecified when samples are missing. We introduce ITSY, the first continuous-optimization method for causal discovery from irregular time series under a linear model. ITSY reformulates the structural equation so that prediction uses the nearest available history rather than the possibly missing current slice, and jointly imputes missing values while learning both graphs. A weighted reconstruction objective corrects the noise transformation induced by this reformulation. Across synthetic regimes varying missingness, scale, graph density, and noise, and on a real world benchmark, ITSY consistently improves graph recovery over representative SCM-based baselines, demonstrating the effectiveness of the proposed method. The results establish a focused solution for irregular linear first-order dynamics and clarify the assumptions required for nonlinear or higher-order extensions.

---


### 224. [Feature Suppression and Differential Privacy for Residential Traffic Classification: A Two-Home Federated Study](https://arxiv.org/abs/2609.23521)

**<font color=#1a73e8>作者：</font>** Márton Pál Lipcsey-Magyar, Adrian Pekar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residential traffic classification supports service management, but learning across homes must account for heterogeneous traffic and privacy constraints. Privacy-aware training may impose uneven costs across traffic categories. We study this tradeoff in simulated two-client federated learning using 1.62 million preprocessed gateway-collected flows across six categories. We compare a full-feature baseline, feature suppression (FS), and differentially private stochastic gradient descent (DP-SGD) under one fixed record-level privacy setting. FS-mild excludes four timing features from 16 model inputs; it provides no formal privacy guarantee. With size-proportional aggregation, FS-mild achieves higher combined macro-F1 and worst-group F1 (the minimum per-class F1 across homes) than DP-SGD in all five seeds at both model capacities under stratified and temporal splits. The tested DP-SGD configuration incurs pronounced minority-category losses, especially in the smaller home, but FS-mild does not uniformly improve on the full-feature baseline. On stratified-split models, loss-based and shadow-model membership probes show near-chance aggregate discrimination without a consistent ranking across probes; this does not establish equivalent privacy. These findings support FS as an input-minimization baseline, not a substitute for formal privacy.

---


### 225. [Predicting Out-of-Distribution Generalization of Neural Operators via Observable Spectral Error Decomposition](https://arxiv.org/abs/2609.23529)

**<font color=#1a73e8>作者：</font>** Hang-Cheng Dong, Pengcheng Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators have emerged as powerful surrogates for solving partial differential equations (PDEs), yet their reliability under distribution shift remains a critical barrier to deployment. Existing approaches to out-of-distribution (OOD) generalization in operator learning are largely empirical and black-box: they report aggregate error metrics without explaining why errors arise or when they will grow. We propose a structure-preserving framework that makes OOD generalization predictable and auditable. Our key idea is to parameterize the learned solution operator as a spectral filter $h_\theta(\lambda)$ acting on the eigenvalues of the underlying elliptic operator, implemented via Chebyshev polynomial expansions and trained with a weak-form objective. This parameterization admits an exact decomposition of the energy-norm error into two observable components: a model-dependent spectral approximation term and a distribution-dependent spectral weighting term induced by the input. From this decomposition we derive three diagnostics: a conservative in-band supremum $\vareps_{\mathrm{sup}}$, a global RMS proxy $\vareps_{\mathrm{rms}}$, and a sample-dependent effective metric $\vareps_{\mathrm{eff}}(f)$. These diagnostics can be computed without access to ground-truth solutions. Through four controlled experiments, we show that $\vareps_{\mathrm{eff}}(f)\|f\|$ consistently predicts energy error under in-distribution, in-band spectral shift, out-of-band tail, and compound shifts, whereas global metrics can be systematically misleading. Our framework shifts OOD assessment of neural operators from black-box benchmarking to operator-structure diagnostics, providing a practical route to auditable scientific machine learning.

---


### 226. [GeoBalance: Geometry-Aware Monitoring and Reconstruction with Asymmetric Optimization for Balanced Multimodal Learning](https://arxiv.org/abs/2609.23533)

**<font color=#1a73e8>作者：</font>** Zechang Xiong, Da Li, Rong Yin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal classifiers can converge to modality-dominant solutions in which one modality dominates the joint prediction, suppressing the learning of others. Existing balancing methods mainly adjust losses, gradients, or modality contributions, largely treating modality imbalance as an optimization problem while implicitly treating the weak modality as under-optimized but representationally intact. In this work, we find that this assumption does not always hold, as persistent modality dominance can induce a representation-level collapse of the weak modality, which we term \emph{manifold modality collapse} (MMC). MMC manifests as a coupled geometric degradation in which weak-modality representations collapse onto fewer directions within each class and become less separable across classes. Motivated by this observation, we propose \emph{GeoBalance}, a geometry-aware framework that monitors these two geometric properties and reconstructs the weak modality representation only when it exhibits signs of MMC. Once triggered, GeoBalance uses a fixed Simplex-ETF class scaffold and spectral regularization to restore class separation while preventing collapse onto a few feature directions. To preserve reconstruction during joint training, asymmetric gradient projection removes the joint-gradient component conflicting with reconstruction, leaving non-conflicting optimization unchanged. Extensive experiments across six multimodal benchmarks demonstrate great improvements over competitive balancing methods, validating its effectiveness.

---


### 227. [PosEviLoc: Position-Conditioned Spatial Evidence for Language-Based 3D Localization](https://arxiv.org/abs/2609.23534)

**<font color=#1a73e8>作者：</font>** Tianyi Shang, Yike Shi, Zhenyu Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-based 3D localization retrieves the point-cloud submap containing a target position from descriptions of nearby objects and their spatial relations. Existing methods typically compress queries and submaps into global descriptors, potentially obscuring object-level semantics and cross-description spatial coherence. We propose Position-Conditioned Evidence Localization (PosEviLoc), a query-position-aware framework for coarse text-to-point-cloud localization. Instead of relying on global matching, PosEviLoc evaluates each candidate submap using explicit semantic and spatial evidence. It models direction as a relation jointly determined by an object position and a hypothetical query position. The resulting Query-Position Spatial Evidence Field (QSEF) measures the fraction of query descriptions supported at each hypothetical position, explicitly capturing their agreement without using the ground-truth query pose to construct the evidence field. A Multi-Level Evidence Readout (MER) summarizes this evidence in a compact representation, which a lightweight MLP converts into a retrieval score. Across five benchmarks, PosEviLoc outperforms MNCL by an average of 17 percentage points in Recall@1. When used as a plug-and-play reranker, it improves MNCL by an average of 16 percentage points. Moreover, PosEviLoc introduces substantially fewer parameters and achieves faster inference speed than existing methods.

---


### 228. [Decoupled Causal Discovery](https://arxiv.org/abs/2609.23535)

**<font color=#1a73e8>作者：</font>** Zhengkang Guan, Fei Wu, Kun Kuang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery from observational data is a fundamental yet challenging task in scientific research. While existing approaches are primarily based on conditional independence tests, structure scores, or restrictive functional assumptions, we propose Decoupled Causal Discovery (DCD), a novel decoupling-based perspective that does not rely on these methodologies. DCD directly identifies the Markov boundary (MB) by decoupling non-target variables via weighting functions, such that only variables within the MB preserve dependence with the target under the decoupled distribution. Building on this, DCD iteratively constructs the Completed Partially Directed Acyclic Graph (CPDAG) by exploiting structural asymmetries within the MBs. We establish the theoretical identifiability, soundness, and completeness of DCD. Empirical evaluations demonstrate that DCD achieves strong performance, particularly excelling in challenging noise regimes.

---


### 229. [Preserving Geometric Integrity in Graph Prompting via Measure-Constrained Optimal Transport](https://arxiv.org/abs/2609.23547)

**<font color=#1a73e8>作者：</font>** Xiangyu Wang, Shuo Wang, Ruiyi Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph prompt learning enables parameter-efficient adaptation of frozen Graph Neural Networks to downstream tasks through lightweight prompt parameters. As routing becomes increasingly node-adaptive, however, independently optimized local decisions can collectively concentrate assignment mass on a small subset of a finite shared prompt bank, even when individual node--prompt matches remain locally meaningful. We propose MINT (Measure-INtegrity Transport), an entropically regularized optimal transport framework that formulates node-to-prompt adaptation as a globally coupled allocation problem. The transport cost favors local geometric compatibility, while a prescribed prompt-side marginal explicitly controls graph-wide prompt utilization. We further derive an exact variance decomposition that separates prompt-side geometric variance into retained prompt-update variation and within-node barycentric dispersion, together with a conditional stability bound for the frozen-encoder forward map. Across standard citation networks and additional heterophilic graphs, MINT remains competitive in few-shot adaptation. Controlled and end-to-end experiments further distinguish the roles of routing and topology: fixed-marginal routing controls graph-wide prompt utilization and has measurable end-to-end effects on citation networks, while topology augmentation provides a complementary, graph-dependent mechanism for addressing structural mismatch. Code is available at this https URL.

---


### 230. [Physics-residual machine learning predicts oxygen-evolution catalyst activity beyond the training range from sparse polarization measurements](https://arxiv.org/abs/2609.23549)

**<font color=#1a73e8>作者：</font>** Yong-Woon Kim, Jihyeok Lee, Sungtae Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Screening oxygen-evolution catalysts on combinatorial libraries requires deciding which candidates receive the remaining measurements. The deciding activity lies beyond each candidate's measured potential window and often above every activity recorded during fitting. We predict it by physics-residual machine learning: the Tafel equation extrapolates the candidate's own measured current and slope, a learned residual attenuated with feature-space distance corrects the magnitude, and an applicability-domain score identifies predictions above the training range before measurement. In a separately fabricated 322-candidate library, 282 above the training maximum, two measurements per candidate gave a mean absolute error of 0.203 mA cm$^{-2}$ against 1.330 for the selected data-driven machine-learning model. Errors inside the training range remained comparable, and 35 labelled catalysts were enough to fit it. In two independent datasets the same construction lowered the overpotential error by 29 to 52%. Campaigns can therefore shorten each measurement and still rank the most active compositions.

---


### 231. [Paragraph Boundaries Are Not White Space:Compression Depth as the Signature of Hierarchical Structure](https://arxiv.org/abs/2609.23551)

**<font color=#1a73e8>作者：</font>** Shuyang Xiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard positional encodings represent position as a one-dimensional reading-order coordinate, but reading order alone does not determine hierarchical textual structure. We use a hierarchical rotary positional encoding (hRoPE) that represents paragraph, sentence, and token indices as separate channels, hold the token sequence fixed, intervene on the paragraph coordinate p1, and measure cross-paragraph attention with a token-distance-exact estimator. Attention is compressed relative to a token-distance-matched baseline in every corpus, but compression alone is not diagnostic of true structure: an architecturally identical channel with density-matched random labels is compressed too, more shallowly. What distinguishes real structure is the depth of compression, which is greater and corpus-dependent while the control's is not. Comparing eight corpus-only quantities across three constructs (lexical persistence, paragraph length, embedding-based coherence), none fully reproduces the cross-corpus ordering of depth, though embedding-based coherence comes closest. Compression depth, not its location, is the reproducible signature of genuine paragraph structure in our setting.

---


### 232. [Modeling Clinical Workflow for SYNTAX Scoring from Coronary Angiography Videos](https://arxiv.org/abs/2609.23553)

**<font color=#1a73e8>作者：</font>** Suzhong Fu, Jingqi Dong, Xuan Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The SYNTAX score is a clinically established tool for assessing anatomical lesion complexity in coronary artery disease and guiding subsequent treatment. However, automated SYNTAX scoring is commonly formulated as a direct regression problem from coronary angiography videos to patient-level scores. In this work, we reformulate SYNTAX scoring as a vessel segment identity-preserving anatomical reasoning problem and propose a hierarchical modeling framework that explicitly aligns learning with the clinical workflow. Our approach maintains vessel segment identity across frames and views, estimates stenosis severity at the segment level, and aggregates evidence hierarchically according to coronary anatomy. Simultaneously, to address the scarcity of domain-specific data, we integrate and complete multiple public coronary angiography datasets, constructing a large-scale resource featuring completed vessel segmentation and derived structural annotations. Experiments demonstrate that vessel segment-level stenosis embedding enhances explanatory power and reduces prediction variability compared to baseline models, with the R^2 score improving by 0.201 and dev STD decreasing by 18.4%. These results highlight the necessity of structure-aligned modeling for reliable and stable automated SYNTAX scoring from multi-view coronary angiography videos. The GitHub link is this https URL.

---


### 233. [Transferring Visual Explanations: How Cross-Architecture Knowledge Distillation Affects Model Interpretability](https://arxiv.org/abs/2609.23561)

**<font color=#1a73e8>作者：</font>** Aleks Czufarow, Ihor Babin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying efficient neural networks is essential in resource-constrained environments, yet compact models often sacrifice interpretability - a critical in safety-critical domains such as autonomous driving and medicine. This study investigates whether Knowledge Distillation transfers the spatial feature attribution of a large teacher network to a compact student. To assess the influence of the KD scheme on interpretability, we distill a ResNet-152 teacher into a ResNet-34 student on ImageNet-1K across five configurations by systematically varying the distillation temperature and soft-label loss weight. Models are evaluated on top-1 accuracy, along with two interpretability metrics: Relevance Mass Accuracy and Relevance Rank Accuracy. These metrics are computed via Grad-CAM heatmaps benchmarked against ground-truth object masks. Our results show that top-1 accuracy ranges from 71.6% to 74.0%. For Grad-CAM, RMA ranges from 7.7% to 9.7% and RRA from 7.3% to 10.1%; for Guided Grad-CAM, RMA ranges from 16.1% to 18.6% and RRA from 15.9% to 21.5%. Interpretability proves far more sensitive to the soft-label weight than to the temperature: keeping the student anchored to hard labels preserves both accuracy and coarse localization, whereas weighting the teacher heavily degrades both. Fine-grained attribution, however, fell below the undistilled baseline in every configuration tested, indicating that logit distillation transmits where a model attends more readily than the pixel-level structure of that attention. We evaluate 12 cross-architecture combinations of convolutional and transformer-based models, revealing that the inheritance of fine-grained spatial reasoning is fundamentally bottlenecked by the student's intrinsic structural biases. To our knowledge, this is the first application of this interpretability-aware evaluation framework - previously used for neural network pruning - to KD.

---


### 234. [G6D: Geometric Learning-Free RGB-D 6D Pose Solver for Robotic Manipulation](https://arxiv.org/abs/2609.23566)

**<font color=#1a73e8>作者：</font>** Yixuan Liang, William Chen, Yunan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 6D object pose estimation is fundamental to robotic manipulation and automation. Recent zero-shot methods have significantly improved generalization to unseen objects, but most still rely on large-scale pretrained models with substantial GPU computation and memory demands. These requirements complicate deployment on robotic platforms where perception, planning, and control share limited computational resources, while learned intermediate representations offer limited geometric interpretability for task-specific adaptation. To address these limitations, we propose G6D, a learning-free, geometry-driven RGB-D 6D pose solver. Given an RGB-D observation, an object instance mask, camera intrinsics, and a CAD model, G6D generates pose hypotheses through template-based geometric matching and refines them using silhouette and depth consistency, forming a purely geometry-driven pose estimation paradigm. This paradigm requires neither pretrained visual models nor target-specific training and preserves interpretable geometric representations throughout pose estimation. Moreover, adjustable hypothesis counts provide flexible accuracy-computation trade-offs, while a CPU-only configuration supports deployment without GPU resources. Experiments on LineMOD and five BOP19 datasets demonstrate advanced performance. Real-world pick-and-place experiments further demonstrate G6D's applicability to robotic manipulation. The complete project is publicly available at this https URL .

---


### 235. [ARID: A Deployable Edge AI System for Structured Information Extraction from Industrial Maintenance Work Orders](https://arxiv.org/abs/2609.23582)

**<font color=#1a73e8>作者：</font>** Kuanlin Chen, Chen-Wei Kuo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Maintenance work orders must often be processed offline on embedded hardware, yet downstream software requires predictable structured output. We present ARID (Aviation-inspired Routing for Industrial Deployment), which extracts component, failure mode, symptom, and maintenance action into fixed-schema JSON on an 8 GB NVIDIA Jetson Orin NX. ARID combines conservative dual-teacher filtering, targeted noise-aware synthesis, one routing decision per work order, 4-bit inference, and grammar-constrained decoding. From 2,326 unlabeled OMIn records, it retains 716 training pairs and adds 99 topology-constrained records targeting action extraction. On 300 human-labeled records, ARID reaches 84.8% token-F1 on the reference stack and 82.9% on the deployed Jetson. Resident serving achieves 5,310/5,656 ms P50/P99 at 12.5 W. On zero-shot MaintNet transfer, semantic F1 falls to 46.4% while parser success remains at least 99.8%, showing that output validity transfers but field semantics do not.

---


### 236. [POZZER: A Power Side Channel-guided Fuzzer for Black-Box Embedded Systems](https://arxiv.org/abs/2609.23583)

**<font color=#1a73e8>作者：</font>** Pouya Narimani, Kseniia Rogova, Addison Crump 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Firmware fuzzing is an effective technique for discovering vulnerabilities in embedded systems. However, existing coverage-guided firmware fuzzers typically obtain feedback through firmware instrumentation, hardware debug interfaces, or firmware rehosting, which requires access to the firmware source code or binary image. Such requirements are often infeasible for off-the-shelf embedded devices, where firmware binaries are inaccessible, unrehostable, immodifiable, or undebuggable, necessitating fuzzing under black-box conditions.
In this paper, we present POZZER, a power side-channel-guided fuzzer for black-box embedded systems. POZZER uses power traces as feedback to identify previously unseen behavior via an incrementally constructed graph-based representation of observed executions, guiding the fuzzer toward unexplored execution paths. Its non-profiling design requires neither prior firmware knowledge nor a clone device, extracting meaningful feedback from a single power trace per execution while remaining robust to measurement noise. We evaluate POZZER on 15 firmware targets across two platforms and two real-world commercial embedded devices. Across the resulting target-platform combinations, POZZER outperforms a blind fuzzer under the same time budget in 26 out of 30 target-platform combinations. Furthermore, POZZER discovers two previously unknown vulnerabilities in one of the commercial devices, both confirmed by the vendor, demonstrating its potential for identifying vulnerabilities in black-box embedded systems.

---


### 237. [An Efficient and Effective Watermarking Scheme for the Protection of the Intellectual Property Rights of Video Generative Models](https://arxiv.org/abs/2609.23586)

**<font color=#1a73e8>作者：</font>** Wenhong Huang, Jianwei Fei, Benedetta Tondi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid development of video generative models (VGMs) has enabled the generation of highly realistic synthetic videos, raising concerns about the intellectual property rights (IPR) of these models. In particular, two closely related forensic tasks remain largely unaddressed: synthetic video verification (determining whether a video was generated by a protected VGM) and model ownership verification (determining whether a suspect VGM is an unauthorized copy of a protected VGM). In this paper, we propose a new in-generation watermarking scheme that can address the two verification tasks. First, a novel video watermarking network named VidMark is presented, which incorporates a two-scale discrete wavelet transform (DWT) decomposition and a global temporal attention block (GTAB) to enhance watermark robustness and imperceptibility. Second, we present a decoder-guided fine-tuning procedure. By leveraging the frozen VidMark decoder, this process enables VGMs to synthesize videos carrying an imperceptible, robust, and model-specific watermark. Finally, two verification frameworks are established to perform synthetic video verification and model ownership verification. Extensive experiments on representative VGMs demonstrate that the proposed scheme achieves over 99% watermark extraction accuracy and 100% verification accuracy on both tasks, with negligible impact on video generation quality. Furthermore, the watermarks exhibit strong robustness against a comprehensive range of video-level and model-level attacks.

---


### 238. [Cost-Aware Reinforcement Learning with Action Masking and Projection for Battery Energy Storage Dispatch under Suppressed-Spread Market Shifts](https://arxiv.org/abs/2609.23590)

**<font color=#1a73e8>作者：</font>** Kuanlin Chen, Chen-Wei Kuo, Cheng-En Ou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Battery energy storage system (BESS) dispatch must preserve operational feasibility while declining price spreads reduce the margin available to pay for cycling. We study a proximal policy optimization (PPO) controller whose pre-selection physical action mask and emergency projection are separated from a causal, forecast-informed economic advisory. All forecast-dependent methods receive the same causal 24-step forecast and grid-side settlement. Across five PPO seeds, advice-on net profit is 30.59 and 18.04 USD per 336-hour T1 and T2 window, versus 36.77 and 22.94 USD for proxy-cost MPC; PPO remains below this reference in both periods. Advice raises T2 profit from 16.45 to 18.04 USD while reducing throughput, but is immaterial in T1. On disjoint weekly blocks, PPO is stable under daily, weekly, and blended seasonal forecasts, weakens under persistence, and remains below proxy-cost MPC. Paired diagnostics localize changes to the observed 5-10 USD/MWh regime with mixed SoC-dependent effects. An M0-M6 ablation shows that mask removal sends thousands of infeasible requests to projection, while removing both physical layers exposes ramp violations. The evidence separates economic screening from feasibility enforcement without claiming formal safety, lifecycle-optimal aging, or RL dominance.

---


### 239. [Collapse, Not Complexity: Failure-Conditioned Decomposition Repair for End-to-End Document Parsing](https://arxiv.org/abs/2609.23592)

**<font color=#1a73e8>作者：</font>** Xingyu Lin, Dehui Du  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end document parsers increasingly offer an optional reasoning mode for complex pages. On a 180-page entropy-stratified discovery sample with one frozen 4B checkpoint, complexity is the wrong decision variable. Reasoning lowers mean quality by 2.21 Overall at 1.54x tokens; a preregistered input-only model cannot predict its signed benefit (held-out AUROC 0.47, indistinguishable from chance). The benefit concentrates on pages whose ordinary pass has already collapsed, and they do not look complex: shared collapses have lower layout entropy than healthy ones yet consume 19x the tokens as degenerate repetition that doubling the budget does not cure. Switching modes rarely repairs them: 83% recur under reasoning. We instead detect collapse from the ordinary-pass trace, decompose the page by projection, and re-parse each region. Repair gains 1.40 Overall (95% CI [0.68, 2.16]) at 1.13x tokens, replicates across three checkpoints, and, with all parameters frozen, gains 2.41 (CI [1.64, 3.46]) on the remaining 1,175 benchmark pages.

---


### 240. [StyleAT: Defending Face Recognition Against Semantic Attacks](https://arxiv.org/abs/2609.23596)

**<font color=#1a73e8>作者：</font>** Ben Shapira, Roi Cohen, Shang-Tse Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With face-recognition models now embedded in everyday authentication and surveillance, recent works have pinpointed a critical weakness: these models remain acutely vulnerable to adversarial semantic edits. I.e., adversarially produced semantic alterations to the input, such as slight aging or pose changes, can induce misclassifications. Certain existing attacks are powerful, but they can be computationally costly, rendering them inadequate for developing defenses (e.g., through adversarial training). To fill the gap, we introduce BoundStyle, a potent semantic attack operating in StyleGAN's rich latent space to maximize misclassification rates. Notably, BoundStyle achieves high attack success rates while being ${\sim}{\times}9.5$ faster than existing state-of-the-art attacks, making it suitable for adversarial training. Building on BoundStyle, we develop StyleAT, an efficient adversarial training scheme that incorporates low-budget attack variants yet defends against stronger and unseen semantic attacks. We evaluate on two datasets unseen during training and seven models, and find that StyleAT boosts robust accuracy against state-of-the-art attacks and outperforms common defenses in various settings.

---


### 241. [Beyond UV Mapping: Mesh Texture Compression via Surface-Aligned Texture Fields](https://arxiv.org/abs/2609.23606)

**<font color=#1a73e8>作者：</font>** Jianqiang Wang, Junhui Hou, Siyu Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mesh texture compression typically relies on 2D UV atlases, whose chart discontinuities and mapping overhead can limit coding efficiency. To tackle this challenge, we introduce TexF, a surface-aligned texture field that organizes texture attributes in sparse voxels derived from the mesh surface. This representation supports high-resolution textures while preserving local 3D correlations for compression and enabling direct surface queries. For bitstream compression, TexF reuses established 3D attribute codecs, with voxel locations reconstructed from the decoded mesh without separate transmission. For GPU-resident compression, we develop 3DNTC, which combines quantized hash features with a lightweight decoder for random-access reconstruction at surface positions. Differentiable rendering enables image-space refinement of both voxel attributes and compressed neural fields. Experiments on the MPEG and AOM mesh compression benchmarks demonstrate improved average rate-distortion performance over representative UV-based methods for both bitstream and GPU-resident compression. 3DNTC also supports real-time rendering.

---


### 242. [Compact Low-Cost Hyperspectral Imaging via Angular-to-Spectral Diversity Conversion](https://arxiv.org/abs/2609.23619)

**<font color=#1a73e8>作者：</font>** Kazuma Fujiwara, Takuya Funatomi, Kazuya Kitano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Snapshot hyperspectral imaging avoids sequential scanning, but systems that jointly achieve stable reconstruction, low cost, and compact optics remain limited. We present a snapshot hyperspectral imaging system based on angular-to-spectral diversity conversion. A tapered kaleidoscope creates replicated views with distinct incidence directions, and a directly attached birefringent filter converts them into view-channel-dependent spectral transmittances, yielding complementary measurements that better condition the inverse problem for more stable single-shot spectral reconstruction. The system preserves a simple pixel-wise linear model for fast non-learning-based reconstruction and uses only off-the-shelf components without relay optics or cascaded modules. We select the birefringent filter configuration using a condition-number-based criterion and validate the system on both synthetic and real data.

---


### 243. [Elicitive User Interfaces: Designing How Users Shape Generative Interfaces](https://arxiv.org/abs/2609.23642)

**<font color=#1a73e8>作者：</font>** Eunhye Kim, Bryan Min, Haijun Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative user interfaces (GenUI) promise personalized interfaces to a user's tasks and needs. However, user needs are often implicit---difficult for systems to infer and users to articulate, making it hard for users to arrive at their ideal interface. We propose Elicitive User Interfaces, a design approach to GenUI that generates elicitation techniques as part of the interface itself. Elicitive UIs adapt these techniques to the user, task, and interface to draw out user preferences. To guide the design of Elicitive UIs, we synthesize a six-axis design space that shapes how an interface elicits user preferences. Across two user studies with a design probe, we found that while Elicitive UIs surfaced preferences users had not already formed, and that responses to elicitation varied more across users than across tasks. Users developed more consistent preferences for how they wanted to be elicited, suggesting an opportunity to personalize elicitation itself.

---


### 244. [Why Do Video Diffusion Models Violate Physics? Unveiling the Flaws in Attention Mechanisms](https://arxiv.org/abs/2609.23658)

**<font color=#1a73e8>作者：</font>** Yueyan Li, Haibo Wang, Caixia Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite impressive visual quality, state-of-the-art video diffusion models often generate content that violates real-world physical laws. While existing solutions rely on external priors or specialized data, we investigate the root cause by exploring the internal mechanisms of these models. Specifically, we present the first interpretability study on the ''motion planning'' process of text-to-video diffusion models, revealing how motion trajectories form during early denoising stages. Building upon the ''first shape, then details'' finding, we combine cross-attention trajectory patterns with causal head contributions to identify a specific subset of attention heads driving motion planning. Further, our self-attention analysis shows that Rotary Position Embedding (RoPE) induces excessive spatial attention decay. This causes early candidate regions to prematurely lock into physically implausible positions, suppressing reasonable trajectories in adjacent frames and triggering generation failure modes. To address this fundamental flaw, we propose a lightweight architectural modification that scales the frequency of RoPE across different denoising steps. This strategy reduces excessive attention decay, helping the model explore better candidate regions to establish coherent physical motion. Finally, training-free and training-based experiments confirm the effectiveness of our approach in enhancing the physical commonsense of generated videos.

---


### 245. [ETH-TraceBench: A Large-Scale Event-Stream Benchmark for Ethereum DeFi under Temporal, Protocol, and Contract Shift](https://arxiv.org/abs/2609.23659)

**<font color=#1a73e8>作者：</font>** Kemal Kirtac, Carsten Maple  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ethereum decentralized finance (DeFi) provides a public, time-stamped record of transaction-level event streams, but the same public symbols can create strong machine-learning shortcuts. We introduce ETH-TraceBench, a benchmark for evaluating Ethereum DeFi representations under temporal, protocol, pool/infrastructure, and symbolic shift. The raw event universe covers January 2021-December 2025 and contains 1.35 billion transactions with logs and 5.01 billion raw log rows. Model evaluation uses a fixed 911,267-instance supervised sample, training on 2021-2024, selecting models on 2025H1, and testing on 2025H2. Simple models perform strongly on the aggregate temporal test: TraceStats-GB reaches 0.953 macro-F1 and TopicEmitterHashMLP 0.959 on the canonical DEX test set. Performance drops sharply under protocol novelty, with macro-F1 of 0.794, 0.743, and 0.766 for TraceStats-GB, TopicEmitterTrace-SGD, and TopicEmitterHashMLP, while strict unseen-pool scores remain 0.927, 0.897, and 0.935. Uniswap v4 and Ekubo v1, both absent from supervised training, are materially harder than the full test. Jointly masking emitter and topic identity reduces DEX macro-F1 to 0.916 and liquidation macro-F1 to 0.774 for TopicEmitterTrace-SGD. A standard Transformer over log-index-ordered events provides no consistent advantage over a deterministic shuffle of the same events, indicating that high aggregate scores can arise without sophisticated chronological modeling. A natural-prevalence audit estimates 2025H2 DEX prevalence among logged Ethereum transactions at about 22.5%, and a deterministic 400-transaction audit finds complete agreement with task label sources and independently re-queried raw-log counts. ETH-TraceBench therefore treats difficult transfer and controlled-input conditions, rather than a single aggregate score, as the main evaluation target.

---


### 246. [Mind the Gaps: A Curated Benchmark for Form Field Detection](https://arxiv.org/abs/2609.23679)

**<font color=#1a73e8>作者：</font>** Iheb Brini, Omar Moured, Hamza Gbada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Form Field Detection (FFD) is a fundamental component of document understanding systems, enabling applications ranging from large-scale industrial digitization to accessible form interaction for automated analysis. Unlike conventional object detection tasks, FFD is inherently challenging because fields are often defined by layout structure and whitespace rather than visible foreground content. Existing large-scale datasets frequently rely on heuristic annotation pipelines, resulting in noisy and inconsistent labels that hinder reliable evaluation. In this work, we introduce mini-CommonForms, a carefully curated FFD benchmark with consistent, high-quality annotations, and present a detailed evaluation of state-of-the-art detection approaches. The benchmark is designed to support reproducible research in document automation and accessibility-oriented applications. Dataset and code are available at this https URL

---


### 247. [One Patch, Three Roles: What Is Actually Coupled in Autoregressive Time-Series Forecasting?](https://arxiv.org/abs/2609.23686)

**<font color=#1a73e8>作者：</font>** Ziang Li, Yue Huang, Guoxu Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Patch-based autoregressive time-series forecasting often ties input representation, learned transitions, and recursive execution to one patch length. We ask which of these roles can be adjusted separately. A supporting atomic-encoding study finds greater sensitivity to model width than to atom grouping on the evaluated grid. Our main finding is that a frozen parent's recursive trajectory is easier to fit than the observed future with lightweight parallel exits. Autoregressive Trajectory Distillation (ATD) turns this into selectable ATD-1/2/4/8 execution, with ATD-1 exactly recovering the parent. On a paired four-data-set comparison, ATD-8 reaches $5.54\times$ end-to-end speedup with stable quality across widths. Fewer calls do not automatically remove the parent's existing forecast error: ATD improves trajectory fidelity in all 21 seed runs but forecast accuracy in only 15 against matched clean-future supervision. We further find a correctable residual projection along a train-selected periodic history direction. Spectrum Tangent applies this correction without adding neural parameters or Transformer calls. At horizon 720, it reduces mean squared error (MSE) and mean absolute error (MAE) by 2.54% and 2.33% over seven data sets and two output widths, while remaining $3.24\times$ faster than recursive inference. Level and shape projections sometimes disagree. Trajectory compressibility, the fidelity-accuracy mismatch, and the correction recur across three public AR parents. Together these results separate representation, transition, and execution as AR design axes. Code is available at this https URL.

---


### 248. [A multi-temporal dataset for mapping burned areas in the Brazilian Cerrado using time series of remote sensing imagery](https://arxiv.org/abs/2609.23687)

**<font color=#1a73e8>作者：</font>** Alisson Cleiton de Oliveira, Thales Sehn Körting  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces a multi-temporal tabular dataset derived from satellite images to map burned areas in the Chapada dos Veadeiros National Park, in Goiás, Brazil, covering the years 2020 to 2022. The dataset contains blue, green, red, and near-infrared bands, as well as the BAI, EVI, GEMI, NDVI, and NDWI spectral indices from the WFI sensor on the CBERS-4A, CBERS-4, and AMAZONIA-1 satellites, organized into a regular grid. We applied the Random Forest classifier to develop and validate models based on samples labeled as totally burned, partially burned, and non-burned. Two classification approaches were tested: one combining burned and non-burned areas into binary classes and another distinguishing between totally burned (TB), partially burned (PB), and non-burned (NB) classes. Seven validation approaches assessed different post-classification combinations, focusing on accuracy, precision, recall, and intersection over union (IoU) metrics. Results showed higher IoU when TB, PB, and NB were used as individual classes and TB was reclassified as burned area (BA) while PB and NB were grouped as non-burned. Comparing the annual results of this approach to the MCD64A1 product, the errors of omission for the BA class were 22% in 2020, 28% in 2021 and 59% in 2022, while the errors of commission were 46%, 43% and 46%, respectively. The study highlights the utility of the WFI sensor for burned area mapping without inter-satellite spectral calibration and suggests further exploration with other machine learning algorithms to evaluate the dataset potential and limitations.

---


### 249. [Tail-Weight Control and Localized Generalization in Nearly Low-Rank Adversarial Classification](https://arxiv.org/abs/2609.23688)

**<font color=#1a73e8>作者：</font>** Kunyu Wang, Dehan Wang, Wenjun Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study norm-constrained linear classification under Eu clidean adversarial perturbations in a Gaussian model with a low-dimen sional informative subspace and an independent noise tail. For bounded ramp loss, we prove that a principal-space witness with risk below one half forces every near-optimal predictor to have small tail weight. A path-specific density bound yields constants without requiring positive tail variance. Under isotropic principal covariance, we establish a unique population minimizer and joint local growth. Boundary normalization then removes the common attack penalty from centered margins, giving localized finite-sample guarantees governed by principal dimension and total tail energy. Globalized growth removes the entrance condition at weaker constants; a model-aware comparison retains local guarantees. Experiments with twenty paired repetitions show decreasing excess risk and tail use with sample size, and nearly unchanged behavior when tail dimension grows at fixed total energy. Pure-noise controls and optimizer diagnostics clarify the scope and limitations of these conclusions.

---


### 250. [Infectious Bovine Pinkeye Detection Using Computer Vision and Imbalance-Aware Learning](https://arxiv.org/abs/2609.23714)

**<font color=#1a73e8>作者：</font>** Michael Abalo, Jameson Brennan, Hossein Moradi Rekabdarkolaee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infectious bovine pinkeye is a contagious ocular disease that adversely affects cattle health, welfare, and agricultural productivity. Conventional diagnosis relies primarily on clinical observation, which can be subjective, time-consuming, and difficult to implement efficiently in large herds or remote settings. This study evaluated and compared You Only Look Once (YOLO) v11 and YOLOv26 for automated bovine pinkeye classification and investigated the effects of class-balancing strategies on model performance. Five variants (n, s, m, l, and x) of each architecture were trained and evaluated using the original imbalanced dataset, Random Minority Oversampling (RMO), and an adapted Synthetic Minority Oversampling Technique (SMOTE). Both YOLOv11 and YOLOv26 demonstrated strong classification performance, although the effects of class balancing varied across model variants. For YOLOv11, RMO-s achieved an accuracy of 0.99, a macro F1-score of 0.98, and a true positive rate (TPR) of 1.00, with no false-negative classifications. RMO-m also achieved a TPR of 1.00 with no false negatives. For YOLOv26, the original l, RMO-m, and RMO-l variants each achieved an accuracy of 0.99 and a macro F1-score of 0.98, with RMO-l attaining a TPR of 1.00 and no false negatives. Overall, RMO generally provided greater improvements in minority-class detection than adapted SMOTE, whereas the strong performance of the original YOLOv26-l demonstrates that oversampling was not necessary for all model variants. These findings demonstrate the potential of YOLOv11 and YOLOv26 for automated detection of bovine pinkeye and support further evaluation for livestock health monitoring.

---


> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
