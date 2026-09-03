# 📦 其他研究 | 2026年09月04日

> 本类共 **187** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-187](./part-04.md)

---

### 51. [Refining Heuristic-Based Bitcoin Address Clustering with Graph Neural Networks](https://arxiv.org/abs/2609.01942)

**<font color=#1a73e8>作者：</font>** Hugo Schnoering, Roman Bresson, Michalis Vazirgiannis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bitcoin's pseudonymous nature makes it challenging to analyze user-level activity, since a single user may control multiple identifiers (addresses). Existing heuristic-based methods attempt to identify addresses belonging to the same user, but they often produce flat cluster assignments with limited modularity and are prone to errors such as merging different users together. In this work, we propose a method for refining heuristic-obtained clusters by grounding our clustering on contrastive embeddings yielded by graph neural networks. Our contributions are threefold: (i) we release a publicly available dataset of Bitcoin transaction graphs containing a substantial number of clusters; (ii) we propose a methodology for learning address embeddings consistent with heuristics, and back it up with theoretical guiding intuitions; (iii) through hierarchical clustering, we enable a finer analysis of heuristic clusters and provide a quantitative criterion for flagging suspicious merges.

---


### 52. [Privacy Amplification Without Independence: How Far Negative Dependence Carries the Guarantees of Poisson Subsampling](https://arxiv.org/abs/2609.01944)

**<font color=#1a73e8>作者：</font>** Xujun Che, Depeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Poisson subsampling is the default sampler in differentially private optimization because its independence makes privacy amplification tractable. Practical systems, however, are moving toward structured participation: random allocation (balls-in-bins), per-epoch allocation, random check-ins, schemes widely believed to be at least as private as Poisson subsampling at the matched rate. We isolate the probabilistic mechanism behind this belief and delimit it exactly, for Gaussian mechanisms up to correlated-noise matrix mechanisms.
(1) If the participation indicator vector is negatively associated (NA), then at every integer Rényi order $\alpha\ge2$, exactly at all finite parameters, its remove-direction Rényi divergence is dominated by that of the marginal-matched independent scheme. For fixed gradient sequences, this extends to the mechanism level whenever the noise strategy's Gram matrix is sign-balanced, an $O(t^2)$-checkable condition.
(2) The integer-order restriction is essential. For random allocation with $k=1$, we prove a linear law for the Rényi-difference criterion: at large $t$, dominance reverses for every $\alpha<3/2$, including KL divergence, while the crossing order tends to $3/2$ independently of $\sigma$.
(3) We also localize the known failure of rate-matched Poisson domination exactly: below $(1-q)^t$, the hockey-stick ordering reverses, so substituting the Poisson pair into composition machinery is unsound. An upper-tail argument yields a finite crossover $\gamma_\star$, connecting this threshold picture to the Rényi boundary at $3/2$.
Together, these results give a substitution map for privacy accounting: when Poisson-based computations remain sound for structured participation, where they fail, and what sound alternatives cost in deployment.

---


### 53. [Pushing Forward Multi-Secret-Key Homomorphic Encryption for Private Average Aggregation](https://arxiv.org/abs/2609.01945)

**<font color=#1a73e8>作者：</font>** Miguel Morona-Mínguez, Fernando Pérez-González, Alberto Pedrouzo-Ulloa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning enables multiple clients to train a shared model while keeping their local datasets isolated. However, the exchanged model updates may still leak sensitive information, making private aggregation a central building block in practical deployments, especially in the cross-silo setting. Homomorphic Encryption naturally fits the client--aggregator communication pattern of Federated Learning, but conventional single-key deployments rely on strong non-collusion assumptions. Multiparty Homomorphic Encryption removes this limitation, although recent attacks under restricted decryption access require large-variance smudging noise during collaborative decryption, which significantly increases ciphertext size and implementation complexity. In this work, we propose lightweight multi-secret-key protocols for private average aggregation based on RLWE-based Homomorphic Encryption. Our construction departs from the usual multiparty blueprint by avoiding the generation of a collective public key. Instead, each client encrypts its update under its own secret key, while the resulting ciphertexts remain compatible with homomorphic aggregation and collaborative decryption. By explicitly tracking and cancelling the ciphertext noise during decryption, the protocol removes the need for large $\lambda$-dependent smudging noise. We instantiate the construction with both exact BFV-based and approximate CKKS-based variants, prove its security in the semi-honest model against an adversary corrupting the aggregator and up to $L-1$ clients, and compare its communication and runtime performance with state-of-the-art MHE-based aggregation. Our results show that the proposed approach substantially reduces ciphertext expansion and online cost, while preserving practical homomorphic aggregation performance.

---


### 54. [Convergence Theory of Knowledge Distillation in Asynchronous P2P Gossip Learning Network](https://arxiv.org/abs/2609.01952)

**<font color=#1a73e8>作者：</font>** Lucas Qingyang Fang, Tiyao Liu, Jinhao Jing 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized, serverless learning increasingly connects devices running different architectures, where the standard tool, decentralized SGD, is undefined as models with different parameter counts cannot be averaged. Knowledge distillation (KD) exchanges soft predictions rather than weights and sidesteps this obstacle, yet convergence theory for fully decentralized, asynchronous peer-to-peer (P2P) KD is lacking. We provide one, relocating consensus from parameter space to function (output) space: a KD event is a geometric contraction operator in logit space on the peers' predictive distributions, which we analyse in the Hilbert space of predictions on a reference measure. Under standard smoothness/variance assumptions and two realizability assumptions, one bridging parameter SGD to the functional step and one controlling restricted task/KD alignment, the time-averaged functional stationarity and function-space disagreement converge at rate $O(1/(\eta T))$ to an $O(\eta)+O(B_f^2)+O(\zeta_f^2)$ neighbourhood. Here $B_f$ is the distance from the task optimum to the peers' reachable classes and $\zeta_f$ measures persistent local-task heterogeneity. Across homogeneous, width-heterogeneous, and mixed-family networks of the experiments, KD contracts function disagreement by $40-61\times$, while isolated training does not. The sampled stationarity diagnostic has late transient exponents $0.99-1.90$ on the shared-skeleton main runs, and the four-point step-size sweep exhibits the predicted transient: neighbourhood tradeoff.

---


### 55. [FlashKAN: B-Spline KANs via Truncated Power Form](https://arxiv.org/abs/2609.01956)

**<font color=#1a73e8>作者：</font>** Naveen Mysore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) place learnable B-spline activations on network edges rather than fixed activations on nodes. The standard Cox-de Boor recursion evaluates these activations through k sequential passes for degree-k splines, consuming over 90% of forward-pass time. FlashKAN replaces this recursion with the truncated power form, a classical result from approximation theory that expresses each uniform cubic B-spline as five (x)_+^3 terms at shifted knot positions. This paper makes three contributions: (1) a this http URL-fused implementation that collapses these operations into a single GPU kernel, eliminating all recursion, span lookup, and scatter-gather operations; (2) a bounded-coordinate stabilization that clamps the normalized input to [0, k+1], preventing the catastrophic cancellation that historically motivated the Cox-de Boor recursion; and (3) a production-ready, open-source package (pip install flashkan) that serves as a drop-in replacement for existing KAN layers.

---


### 56. [Aggregating Neighbor Embedding Projection and Rank-Based Manifold Learning for Image Retrieval](https://arxiv.org/abs/2609.01963)

**<font color=#1a73e8>作者：</font>** Vinicius Atsushi Sato Kawai, Gustavo Rosseto Leticio, Lucas Pascotti Valem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Content-based image retrieval (CBIR) has advanced significantly with deep learning, yet effectively ranking similar images remains challenging, particularly in high-dimensional feature spaces, where pairwise distances often fail to capture contextual relationships and the semantic gap between visual features and high-level concepts persists. Manifold learning and rank-based refinement methods have emerged as complementary strategies, respectively improving feature representations and exploiting contextual information embedded in ranked lists, such as neighborhood relationships among images. However, combining these projection-based and rank-based strategies to exploit their complementary properties remains a challenging research problem. To address this, we propose a framework that combines neighbor embedding projections with rank-based manifold learning through rank aggregation. Uniform Manifold Approximation and Projection (UMAP) generates alternative low-dimensional feature representations, and ranked lists obtained from UMAP projections and rank-based re-ranking methods are combined using the Borda Count aggregation strategy. Experiments were conducted on several public datasets using deep learning features extracted from ResNet152, Swin Transformer, and DINOv2 models. Results show that the proposed approach improves retrieval effectiveness in several scenarios, particularly when the baseline representation struggles to achieve high precision. The aggregation strategy also often improves the quality of top-ranked positions, leading to competitive Mean Average Precision (MAP) and Precision values across different datasets and feature extractors. These findings suggest that combining projection-based and rank-based manifold learning strategies through rank aggregation can provide complementary contextual information for image retrieval tasks.

---


### 57. [A Unified Particle Filter LSTM for Data-Driven Process Simulation](https://arxiv.org/abs/2609.01967)

**<font color=#1a73e8>作者：</font>** Parvin Malekzadeh, Opher Baron, Dmitry Krass  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven process simulation aims to generate realistic case trajectories from historical event logs without requiring an explicitly specified model of the underlying dynamics. Deep sequence models can capture complex temporal dependencies through next-activity probabilities and conditional time distributions. However, event logs provide only a partial view of the underlying process state, often recording activity completions without the corresponding service-start times. Consequently, the same observed process history may be consistent with multiple plausible latent process conditions, whereas standard recurrent models compress each process prefix into a single deterministic recurrent state. We propose a Unified Particle Filter LSTM (Unified PF-LSTM) that maintains and sequentially updates a weighted set of recurrent-state hypotheses. We summarize this particle belief using its weighted mean and learned features based on the moment-generating function. The resulting representation is used to predict a categorical distribution over the next activity and conditional quantiles of the current activity's sojourn time. The framework is trained end-to-end from event-log data and evaluated on three real-world emergency department datasets. The results show that the proposed framework consistently outperforms the considered data-driven baselines in reproducing routing, duration, and system-level behavior across all datasets, with particularly strong gains in settings where complex process dynamics are only partially reflected in the available event logs.

---


### 58. [Exploring Breathing-Music Coupling: Using the Breathing Mirror for Somatic Reflection in Piano Performance](https://arxiv.org/abs/2609.01974)

**<font color=#1a73e8>作者：</font>** Ziyue Piao, Yohei Wada, Isabelle Cossette 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While breathing is essential to living and for sound production in some instruments, for pianists, it is often a hidden and automatic process, making it difficult to analyze or refine. A critical gap exists between data and awareness: while sensors record precise physical metrics, they fail to capture the performer's somatic experience. Conversely, the high cognitive load of performance makes it nearly impossible for musicians to recall their internal states with temporal precision. To address this, we present a system, Breathing Mirror, and associated methodology designed to externalize the pianist's internal somatic experience through three analytical lenses: a Baseline View (synchronized signals), a First-Person View (subjective recall), and an Interpersonal View (collaborative reflection).
Through a four-week longitudinal study with a skilled amateur pianist (35 years of experience), we evaluated the system's effectiveness by recording respiratory data using textile-integrated strain sensor belts. The results show that the Breathing Mirror reveals some patterns of breathing-music coupling and identifies critical blind spots where objective data diverges from subjective perception. Furthermore, we propose four somatic themes regarding the link between breathing and musical elements, offering a foundation for future large-scale validation across a broader range of pianists. This work provides a new way to study body signals, transforming breathing from an internal biological function into an articulate expressive parameter.

---


### 59. [Reconciling Kinesthetic Mismatches: A Somatic Alignment Mindset for Musical Body Transformation](https://arxiv.org/abs/2609.01981)

**<font color=#1a73e8>作者：</font>** Ziyue Piao, Isabelle Cossette, Marcelo M. Wanderley  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mastering musical performance requires precise multisensory coordination, yet learners encounter a kinesthetic mismatch, which is a discrepancy between the internal perception of an action and the actual physiological state of the body. While multisensory Body Transformation Experiences (BTE) provide tools to bridge this gap, existing designs often focus on external correction rather than internal alignment. To address this, we propose the Somatic Alignment Mindset (SAM), a conceptual lens that integrates Taoist philosophy to shift the focus of HCI design from prescriptive feedback toward holistic embodied unity. By positioning technology as a reflective medium, SAM operationalizes the principles of Adaptation, Assessment, and Awareness to reconcile somatic discrepancies and foster deep, self-aligned musical mastery.

---


### 60. [CAHR-Net: Condition-Adaptive Hysteresis Reconstruction for Compact and Interpretable Magnetic Core Loss Modeling](https://arxiv.org/abs/2609.01991)

**<font color=#1a73e8>作者：</font>** Chunye Gong, Cong Yao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Magnetic core loss originates in the hysteresis loop: the energy dissipated per excitation cycle equals the loop area, and frequency, temperature, and waveform shape set the loss by reshaping the loop geometry. Most existing models let these conditions act only on a terminal scalar - empirical equations fold them into fitted exponents, and data-driven predictors append them to encoded features - so no intermediate hysteresis representation remains for the conditions to reshape. This paper proposes CAHR-Net, a condition-adaptive hysteresis reconstruction network that injects the operating conditions where they physically act. It preserves the interpretable chain from flux density waveform to magnetic field reconstruction, loop-area integration, and power loss estimation, and uses feature-wise linear modulation to inject frequency, temperature, and waveform statistics into the intermediate reconstruction representation. A matched large-batch training protocol based on AdamW, cosine scheduling, and a staged reconstruction-to-power-loss objective is also reported, because the modulation pathway takes effect only within it. On the MagNet final A-E material protocol, CAHR-Net attains an average p95 relative error of 6.89% with only 1874 parameters, the lowest among all compared methods, together with a lower worst-material p95 than the strongest black-box solution at about 48x fewer parameters; it reduces the average p95 of the physical reconstruction backbone from 7.47% to 6.89% and the p95 of material D, the most difficult material, from 16.40% to 14.87%. Ablation and condition-slice analyses attribute the improvement to the coupling of physical loop reconstruction, structured condition modulation, and the matched optimization trajectory.

---


### 61. [ClaimReceipt: Verifying Evidence Sufficiency and Coverage in Agent Evaluations](https://arxiv.org/abs/2609.01992)

**<font color=#1a73e8>作者：</font>** Peiying Zhu, Sidi Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent evaluations face two distinct evidentiary questions: whether a reported claim is recomputable from retained evidence (sufficiency), and whether the retained records cover the committed experiment set (coverage). Generic logs and hash-linked transcripts answer neither reliably. We introduce ClaimReceipt, a claim-relative receipt specification and selective verifier that binds typed transaction evidence to a signed experiment manifest and returns PASS, INVALID, or INCONCLUSIVE per claim. We freeze the specification before implementation (SHA-256 18d109...b81). On 1,392 historical buyer--seller records, a CR-2 verifier reproduces all five manually labeled audit verdicts, exactly replays 600 deterministic and 792 post-generation records, makes every one of 13 declared field groups non-redundant under tested ablations, and returns the expected result on 11/11 semantic faults with 0/8 false positives. We then run a separate prospective CR-3 epoch: 30 assignments are committed before inference, terminal receipts are signed and chained, and private evidence is encrypted for an auditor. Complete evidence yields coverage and accounting PASS; withholding one terminal receipt returns INCONCLUSIVE_COVERAGE, while withholding all private openings preserves coverage and protocol verification but makes economic claims inconclusive, exactly matching a preregistered prediction. Receipt instrumentation adds 0.021% of model-inference time and 9.9 KB per transaction. A specification-legibility probe indicates that our own frozen specification is not yet unambiguous to an independent reader. Claim verification therefore requires both claim-sufficient evidence and a committed universe against which omissions become visible.

---


### 62. [Linear Fusion MultiDiffusion for Fast Training-Free Spherical Panorama Generation](https://arxiv.org/abs/2609.01997)

**<font color=#1a73e8>作者：</font>** Akio Hayakawa, Yusuke Mukuta, Tatsuya Harada  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose LF-MultiDiffusion, a training-free panorama generation method that extends MultiDiffusion to support linear projections between target and reference image spaces. Our key idea is to reformulate latent aggregation as a regularized least-squares problem and solve it efficiently with a Krylov-based iterative solver inside the denoising loop. This formulation enables denser and more natural mappings than prior training-free methods, yielding more stable generation with far fewer perspective views. As a result, LF-MultiDiffusion reduces the number of image generator evaluations during denoising and significantly improves inference efficiency. Experiments show that LF-MultiDiffusion achieves better visual quality, text alignment, and panoramic consistency than the strongest training-free baseline, while providing a 15.36$\times$ speedup. Our project page is available at: this https URL.

---


### 63. [InsightSeg: Reusing Correction Insights for Guideline-Consistent Segmentation](https://arxiv.org/abs/2609.02002)

**<font color=#1a73e8>作者：</font>** Vanshika Vats, Ashwani Rathee, James Davis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Guideline-consistent semantic segmentation requires more than category recognition, as real-world labeling policies demand fine-grained, task-specific decisions. Recent multi-agent refinement systems improve compliance with such textual guidelines by detecting and correcting errors. However, they are stateless: feedback from the critiquing agent is discarded, causing the same guideline-specific mistakes to be repeatedly rediscovered and corrected across the dataset at the cost of additional refinement. We introduce InsightSeg, an episodic memory mechanism that converts successful correction episodes into reusable, visually grounded insights. A meta-analyzer distills each qualifying episode into directive natural-language insights and anchors them to the local image regions that caused the error using patch-level visual concept vectors. On subsequent images, these concepts are matched against dense patch embeddings to retrieve relevant insights, which condition the segmenting agent before making its first prediction. This shifts the system from correcting recurring errors to preventing them, improving segmentation quality before any refinement occurs. Across Waymo and Cityscapes, InsightSeg improves both first-pass and final guideline-consistent segmentation performance while requiring fewer refinement steps, demonstrating that multi-agent refinement can become more accurate and efficient by drawing on past correction experience.

---


### 64. [InstEditSeg: Instruction-Driven Image Editing for Polyp and Skin Lesion Segmentation](https://arxiv.org/abs/2609.02004)

**<font color=#1a73e8>作者：</font>** Ziquan Liu, Zhewei Zhu, Xuyang Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of polyps and skin lesions is pivotal for clinical diagnosis, yet existing methods struggle with low contrast, ambiguous boundaries, and cross-domain distribution discrepancies. Discriminative networks and most diffusion-based segmentation approaches predict standalone binary masks, leaving the visual priors of large-scale pretrained generative models largely unexploited. We propose InstEditSeg, a unified generative framework that reformulates medical segmentation as an instruction-driven image editing problem. Instead of emitting a mask, the model renders a color-coded overlay on the original image, conditioned on a textual instruction, so that the edited output aligns with the natural image distribution learned by latent diffusion models and mitigates the domain gap between natural and medical imagery. To recover fine anatomical structures, we introduce DINOv3 as an auxiliary visual encoder and a DINO Feature Guidance Block that builds a multi-scale feature pyramid. The pyramid is fused into the diffusion U-Net by channel concatenation and zero-initialized convolution so that hierarchical discriminative priors can be injected without perturbing the pretrained weights. A dual-branch classifier-free guidance strategy requiring only two forward passes per denoising step reduces inference cost. On polyp and skin lesion benchmarks the framework achieves accuracy competitive with strong discriminative baselines, and it further demonstrates concrete advantages of the generative formulation: notably better cross-domain generalization on unseen data, more complete multi-lesion segmentation, instruction-conditioned task control, and sampling flexibility. We also analyze the strengths and limitations of the paradigm, including its color sensitivity and unsupported attribute-conditioned selection. Code is available at: this https URL.

---


### 65. [C$^2$T-OpenMax: A Novel Open-Set WiFi RF Fingerprinting Method via Center Constrained Learning and Confidence-Guided Tail Modeling](https://arxiv.org/abs/2609.02007)

**<font color=#1a73e8>作者：</font>** Yuanyu Zhang, Junjie Yang, Ji He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Radio frequency fingerprinting (RFF) enables device authentication from transmitter-specific hardware imperfections, but practical deployment requires cross-environment open-set recognition. Data augmentation improves environmental generalization, yet may yield dispersed, low-confidence known-class representations that distort the class statistics used by OpenMax. To address this problem, we propose C$^2$T-OpenMax, an enhanced OpenMax framework combining center-constrained learning with confidence-guided tail modeling. The former improves intra-class compactness, making class-wise representations more suitable for distance-based modeling. The latter retains only correctly classified, high-confidence logits for mean activation vector estimation and Weibull fitting, reducing bias from ambiguous boundary samples. Together, the two modules refine representation geometry and OpenMax construction while preserving augmentation benefits. Experiments on a public WiFi CSI dataset show that C$^2$T-OpenMax achieves the highest open-set accuracy in seven of eight location groups and outperforms all baselines in area under the receiver operating characteristic curve (AUROC) and open-set classification rate (OSCR) across every tested openness level. Under the largest-openness setting, it improves accuracy by 12.31%, AUROC by 0.0887, and OSCR by 0.0856 over the augmented OpenMax baseline.

---


### 66. [GeoStore: Finding Small Storefronts in Large Scenes -- A Fine-Grained POI Localization Benchmark with Global-to-Local Asymmetric Matching](https://arxiv.org/abs/2609.02012)

**<font color=#1a73e8>作者：</font>** Lu Han, Xiting Sun, Hao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point-of-interest (POI) localization -- matching a user's close-up storefront photograph against large-scale geo-tagged street-view imagery -- underpins map construction, POI verification, and location-based services. Its closest existing paradigm, visual place recognition (VPR), assumes symmetric, whole-image matching of the same scene at a comparable scale; POI localization instead must match a close-up query, in which the target fills the frame, against wide references in which the same POI occupies only a small, off-center region among visually similar shops, under a substantial capture-domain gap. We introduce GeoStore, to our knowledge the first benchmark dedicated to this asymmetric, fine-grained, open-set formulation, and show that global-descriptor methods tuned for symmetric VPR are systematically limited on it, since a single global vector dilutes the small target. We further propose GLAM (Global-to-Local Asymmetric Matching), which couples a retrieval-anchoring global descriptor with an asymmetric local pathway: each reference is kept as a compact set of pooled region tokens and matched against a single query probe through a learnable soft late interaction; at inference, the same tokens enable a lightweight mutual-nearest-neighbor re-ranking. GLAM surpasses strong global and two-stage baselines on Recall@1/5/10 and mAP, with ~5x smaller re-ranking features and ~two orders of magnitude lower per-pair matching cost than prior local re-ranking. The benchmark and code will be publicly released.

---


### 67. [Source-Free Class Relearning: Diagnosing Forgetting in Class Unlearning](https://arxiv.org/abs/2609.02018)

**<font color=#1a73e8>作者：</font>** Zahra Dehghani, Pablo Piantanida, Mohammadhadi Shateri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class unlearning aims to remove a model's ability to recognize designated forget classes while preserving performance on retain classes. However, low forget accuracy after unlearning does not necessarily mean the class structure has been erased. Approximate unlearning methods can alter classifier decision boundaries while leaving recoverable structure in the representation. Prior work has shown that forget classes can be recovered, but existing approaches require real forget or retain samples, auxiliary data, or reference checkpoints. We study class relearning in a strictly source-free setting, asking whether a forget class can be recovered through a classifier-head update using only the unlearned model. Our approach rests on a theoretical analysis establishing a sufficient alignment condition under which a single gradient step on a synthetic probe set increases the expected logit margin of the forget class. Building on this, we propose a white-box Source-Free Relearning Audit (SFRA), which generates candidate embeddings in representation space and uses model-guided confidence filtering to construct high-confidence retain probes and low-confidence boundary-adjacent probes that are relabelled as the forget class. Gaussian sampling and Softmax confidence are used by default, while ablations with alternative proposal distributions and uncertainty criteria show that recoverability is not specific to these choices. To quantify recoverability, we introduce the Relearning Score (RS), which jointly measures forget-class recovery and retain-accuracy preservation, and report class-matched $\Delta$RS relative to a retrained reference. Experiments on CIFAR-10, CIFAR-100, and TinyImageNet with ResNet-18, ViT-B/16, and Swin-T show that several unlearning methods exhibit substantial source-free recoverability, and that for a subset of methods this recoverability exceeds the matched retrained reference.

---


### 68. [SelfLift: Accelerating Few-Step Diffusion via Self-Recovering Resolution Transition](https://arxiv.org/abs/2609.02036)

**<font color=#1a73e8>作者：</font>** Tingyan Wen, Chenqian Yan, Xurui Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step diffusion models substantially compress temporal computation, making the spatial cost of each model evaluation an increasingly dominant source of inference latency. Progressive-resolution inference reduces this cost by performing early denoising at low resolution and reserving high-resolution computation for refinement. However, existing methods typically lift intermediate latents directly and rely on subsequent steps to absorb the induced distribution mismatch. In the few-step regime, the limited recovery budget leaves these errors as visible artifacts, constraining how late the transition can occur and, consequently, how efficiently it can be performed. We introduce SelfLift, a self-recovering progressive-resolution framework that derives both transition-repair signals and trajectory-aligned supervision from the generative model itself. SelfLift-zero proposes a training-free Artifact-Aware Consistency Lift, using disagreement between direct latent lifting and pixel-VAE re-encoding as both a localized artifact-risk signal and a model-native correction direction. It enables reliable late transitions without external super-resolution, extra denoiser evaluations, or sampling-schedule modifications. Building on this robust transition, SelfLift-rich performs On-Policy Self Recovery on student-visited states, transferring dense high-resolution guidance from an internal self-teacher while remaining aligned with the altered progressive-resolution dynamics. Across FLUX.2-Klein and Z-Image-Turbo, SelfLift reduces end-to-end latency by 41.5% and 44.1%, respectively. Combined with timestep distillation, it delivers overall speedups of 29.61x and 19.21x over the corresponding 50-step models while preserving competitive generation quality, establishing a stronger speed-quality frontier for few-step diffusion.

---


### 69. [Type-Directed, Secure-by-Construction Enclave Partitioning for LLVM](https://arxiv.org/abs/2609.02048)

**<font color=#1a73e8>作者：</font>** Wesley B. Nuzzo, Samuel Dodson, Benjamin Houle 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) provide hardware-supported isolation through enclaves that protect code and data independently of software abstractions. However, TEEs alone cannot enforce information-flow security. This problem is further aggravated in LLVM-like low-level languages that allow unrestricted pointer manipulation and unstructured control flow. Moreover, using TEEs effectively typically requires manually partitioning applications into enclave and non-enclave components, a process that is labor-intensive, error-prone, and lacks fine-grained control.
We address these challenges with a three-step approach. First, we formalize SIR, an enclave-oblivious calculus based on LLVM IR, equipped with a novel permissive type system that enforces security against low-level attackers. To obtain meaningful guarantees, SIR combines information-flow control with security-aware coarse-grained memory safety. Second, we extend SIR to SIREN, an enclave-aware calculus that enforces noninterference against stronger attackers capable of observing arbitrary non-enclave memory. Third, we develop a type-driven, type-preserving compilation from SIR to SIREN that automatically produces secure enclave-aware programs, eliminating manual partitioning while providing fine-grained control over host-enclave boundaries.
We implement and evaluate SPLITR on thirteen microbenchmarks and real-world workloads, including applications from SGXGauge, on Intel SGX hardware. SPLITR scales to OpenSSL (425,953 LLVM IR instructions) and supports multiple objectives that expose trade-offs among enclave TCB size, host-enclave transitions, and boundary data movement. For OpenSSL, optimizing for transitions reduces them from 393 to 187. Runtime overhead is dominated by fixed enclave costs for short-running workloads, whereas long-running applications better amortize these costs and approach native performance.

---


### 70. [Monitoring Web Agents Without Internal Signals: Observable Trajectories and Key-Step Supervision](https://arxiv.org/abs/2609.02057)

**<font color=#1a73e8>作者：</font>** Sitong Pan, Yipeng Shen, Yilin Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable web-agent monitoring is difficult when model-internal uncertainty signals such as token logits are unavailable. In this work, we study prefix-level risk prediction for web agents using observable trajectory signals: given an evolving prefix, estimate whether the current execution remains on track or is tending toward failure. We derive two observable trajectory representations: Macro features summarize cross-step agent--environment behavior and feedback, while Micro features measure the consistency of intention, action, and anticipated state change through repeated black-box queries. Instead of inheriting the final result label, we label the first critical error that remains uncorrected in the observed continuation and is associated with final failure as a key-step boundary, preserving valid early prefixes of failed trajectories as on track. Across WebArena-Lite and Online Mind2Web web agent benchmarks with five open- and closed-source backbones, observable trajectory signals are competitive with internal-signal baselines. The resulting predictors also support early intervention under fixed false-cut budgets and transfer across held-out website categories. These findings show that observable trajectory signals support valuable risk prediction abilities.

---


### 71. [MineTRACE: An Evidence-Grounded Interactive Reasoning System for Mineral Prospectivity](https://arxiv.org/abs/2609.02060)

**<font color=#1a73e8>作者：</font>** Yiran Zhang, Jinwen Liu, Daniel Su 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mineral exploration requires integrating heterogeneous geochemical, geophysical, and geological evidence, yet existing prospectivity systems often provide only opaque scores or heatmaps. We present MineTRACE, a web-based system for evidence-grounded exploration of eight commodities: Cu, Au, Ni, W, Sn, Co, Ta, and Mn. Users can explore prospectivity maps, query locations or regions, inspect supporting evidence, and interact through natural language. A transparent expert tree, informed by geological knowledge and known deposits, combines multi-source evidence into interpretable prospectivity scores. For a new location, the conversational assistant retrieves the score and supporting evidence from the analysis pipeline and presents them in natural language. The scorer achieves spatial AUC values of up to 0.917 across different test scenarios, while end-to-end evaluation assesses query accuracy and response grounding. MineTRACE makes public geoscience data easier to access, interpret, and verify, supporting more efficient and transparent mineral exploration.

---


### 72. [LaST-SR: Laplace-Inspired Steady-Transient Complex-Frequency Decomposition for Single Image Super-Resolution](https://arxiv.org/abs/2609.02063)

**<font color=#1a73e8>作者：</font>** Linhao Li, Zhaojie Pan, Langkun Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image super-resolution (SISR) requires global context modeling for structurally consistent reconstruction. Fourier operators are increasingly adopted for global feature modeling. However, their periodic spectral bases constrain the representation of localized aperiodic variations, limiting the recovery of irregular structures and fine details. In dynamical systems, the Laplace neural operator extends Fourier modes to complex frequencies and decomposes the output signal into complementary steady-state and transient responses to jointly model periodic and aperiodic information. We derive, for the first time, an approximate steady-transient decomposition for two-dimensional feature maps, providing an analytical basis for the proposed complex-frequency decomposition. Accordingly, we propose LaST-SR, centered on a Complex-Frequency Decomposition module that couples a global full-spectrum Fourier branch for image-wide dependencies and long-range structural consistency with a window-conditioned local complex-frequency branch for localized, content-dependent aperiodic variations. To fuse the resulting features, we further design a Steady-Transient Collaborative Aggregation module for cross-branch interaction and joint aggregation. Experiments on five benchmarks show that LaST-SR achieves the best PSNR/SSIM among the compared methods for $\times2$ and $\times4$ SISR. Ablation studies further validate the effectiveness of the proposed architecture and its key modeling mechanisms.

---


### 73. [DynG-Diff: A State-Aware Dynamic Guidance Diffusion Framework for Probabilistic Time Series Forecasting](https://arxiv.org/abs/2609.02068)

**<font color=#1a73e8>作者：</font>** Zhente Zhang, Zhengwei Ni, Wei Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic multivariate time series (MTS) forecasting is crucial for modeling complex dynamical systems. However, existing diffusion-based methods rely on task-specific conditional paradigms that lack flexibility and struggle with inherent "information heterogeneity"--the significantly varying noise levels and evolutionary patterns across variables. To address this, we propose DynG-Diff, a variable-sensitive dynamic guidance diffusion framework for probabilistic multivariate time-series forecasting: (1) DynG-Diff adopts a two-stage separated training strategy and uses an unconditional diffusion backbone to model the joint distribution of multivariate time series. (2) DynG-Diff introduces a lightweight state-aware policy network that adaptively infers variable reliability from real-time noisy states and one-step denoising estimates, outputting a dynamic guidance strength matrix. (3) DynG-Diff mathematically formulates this dynamic weight as the local precision of the observation distribution, enabling precise guidance for high-confidence variables during inference while filtering out interference from anomalous noise. Extensive experiments on real-world benchmarks demonstrate competitive probabilistic forecasting performance against state-of-the-art conditional diffusion models and improved robustness under severe observation this http URL implementation code is available at: this https URL

---


### 74. [CHIME: Credit-Aware Hierarchical Memory Evolution for Long-Horizon Agentic Planning](https://arxiv.org/abs/2609.02074)

**<font color=#1a73e8>作者：</font>** Yongshi Ye, Tian Lan, Feihu Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Planning is a central capability that enables agents to decompose complex long-horizon tasks into manageable steps. Test-time search and training-based methods improve planning but incur high inference costs or require expensive training data. Self-evolving memory instead accumulates reusable experience from agent interaction outcomes into an external memory bank, so planning capability keeps improving at inference time without parameter updates. However, existing self-evolving memory methods share an inherent credit assignment problem: they rely on final task outcomes as feedback, but such outcomes conflate plan quality with execution errors and environmental factors, so the accumulated planning experience is often biased and noisy. To address this problem, we propose Credit-Aware Hierarchical Memory Evolution (CHIME), a self-evolving memory framework that maintains a separate planning bank and execution bank and follows an attribute-before-memorize principle: CHIME first attributes each task outcome to the plan, the execution, both, or neither, and then updates only the corresponding memory bank. Extensive experiments on four long-horizon agent benchmarks show that CHIME consistently outperforms state-of-the-art training-based and self-evolving memory baselines. Further analyses reveal several interesting findings. For example, CHIME accumulates effective memory with far fewer items. In addition, the learned memory values faithfully reflect downstream utility: high-quality planning memories are more valuable than execution memories. Finally, the accumulated memory effectively transfers across backbone models. Code will be released at this https URL.

---


### 75. [DPA: Decoupling Product-Agnostic Anomaly Representations for Zero-shot Anomaly Generation](https://arxiv.org/abs/2609.02075)

**<font color=#1a73e8>作者：</font>** Hang Yao, Yansheng Fu, Ming Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection benefits from anomaly samples, yet newly deployed products typically provide only normal images, making anomaly samples difficult to collect. Zero-shot anomaly generation offers a promising solution which avoids collection of target-product anomalies. However, existing methods mainly rely on texture images or text descriptions as anomaly sources, which often produce unrealistic anomalies. Observing that similar anomalies can recur across different products, we propose anomaly transfer-based zero-shot generation, which reuses real anomalies from existing source products, making target-product anomalies no longer necessary to generate realistic anomalious samples for unseen target products. Since not every anomaly type suits the target product, an anomaly type filtering mechanism first selects plausible source types. To transfer selected anomaly, we propose DPA, a diffusion-based framework that decouples product-agnostic anomaly representations. Instead of directly extracting anomaly representations, DPA learns product-irrelevant anomaly embeddings through training with the mismatched data pair, enabling transferable anomaly concept learning across products. Furthermore, we design an adaptive mask-guided pipeline that leverages adaptive masks to control the positional and geometric plausibility of generated anomalies during generation. A training-free anomaly labeling module is further introduced to produce pixel-level annotations aligned with generated anomalies. Extensive experiments on MVTec-AD, VisA, and a dedicated anomaly-transfer benchmark demonstrate that the proposed setting and DPA generate more realistic anomalies and significantly improve downstream anomaly detection performance under both zero-shot and few-shot settings. Source code and models will be released.

---


### 76. [KSG-Net: Key-Sparse and Global-Context Learning for Maritime 3D Ship Detection](https://arxiv.org/abs/2609.02077)

**<font color=#1a73e8>作者：</font>** Zhouyuan Huai, Meiqi Wan, Yan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D ship detection in maritime environments is critical for autonomous navigation, yet remains challenging due to large-scale vessel variations, sparse point clouds of small vessels, and severe sea-clutter interference. Existing methods, primarily based on 2D features or dense representations, struggle to balance detection accuracy and computational efficiency, while sparse 3D detectors designed for road scenes generalize poorly to maritime scenarios. This paper focuses on two key challenges in maritime LiDAR perception: weak feature representation for small and sparse vessels, and insufficient global structural modeling for large vessels due to the limited receptive field of local sparse convolutions. To address these issues, we propose KSG-Net, a Key-Sparse and Global-Context learning network for maritime 3D ship detection. The core idea is to jointly enhance local discriminative features and global structural awareness within a unified fully sparse detection framework. Specifically, a Key Sparse Multi-scale Aggregation (KSMA) module is designed to enhance the representation of small and sparse vessels by selecting informative key voxels and aggregating cross-scale neighborhood features. Furthermore, a Global Context Aggregation (GCA) module is introduced to capture long-range geometric dependencies through scene-level context modeling with gated residual interactions, thereby improving the representation of large vessels. Extensive experiments on the Thames River vessel dataset and simulated datasets demonstrate that KSG-Net consistently outperforms existing methods in multi-scale vessel detection and exhibits strong robustness in complex maritime environments.

---


### 77. [TC-Next: Zero-Shot Multimodal Cyclone Forecasting](https://arxiv.org/abs/2609.02085)

**<font color=#1a73e8>作者：</font>** Zhe Wang, Sijie Chen, Yiming Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present TropicalCycloneNext (TC-Next), a multimodal deep learning model that forecasts tropical cyclone track and intensity at $6$-$24$ h leads by leveraging a foundation model's forecast fields of atmospheric kinematic and thermodynamic fields and GridSat infrared satellite imagery. Trained only on GraphCast forecasts over the Western Pacific (WP), yet reliant only on generic atmospheric variables, TC-Next on GraphCast lowers track error by $15$-$44\%$ and intensity error by a factor of $3$-$6$ relative to a conventional, rule-based tracker, TempestExtremes; applied without retraining to the forecast fields of Pangu-Weather and IFS HRES, it stays ahead of TempestExtremes on both. Applied zero-shot to the generic weather fields of WeatherNext Cyclones on the 2025 WP season, TC-Next attains lower intensity error at every lead time, and lower or comparable track error, compared to that model's specialized direct tracker in a deterministic comparison. Our ablation studies show that our multimodal model is able to utilize the additional modality to improve performance in tracking errors at every lead time and in intensity prediction at longer lead times.

---


### 78. [READY or Not: Reliable Enterprise Agent Deployment](https://arxiv.org/abs/2609.02095)

**<font color=#1a73e8>作者：</font>** Veronica Chatrath, Bryan Zhu, Jingxuan Fan 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An AI agent can perform well on benchmarks and still be unsuitable for deployment. Existing AI-agent benchmarks measure whether an agent can complete realistic professional work, whereas enterprise deployment asks a different question: whether an agent can meet a required reliability level, under acceptable human oversight, and at tolerable cost. We introduce Reliable Enterprise Agent Deployment (READY), a framework for qualifying AI agents for deployment on enterprise workflows. READY preserves each workflow's own definition of successful execution while applying a common qualification procedure. Given an agent, a workflow, and a class of candidate oversight policies, READY measures the reliability and operating cost of the human-AI system, selects the minimum-cost policy that satisfies a specified reliability target, and statistically qualifies it on held-out cases. The resulting deployment profile characterizes the supported operating point: reliability, human-oversight burden, and cost. READY is implemented as an open testbed that decouples workflow specification, execution, evaluation, and qualification, and runs on existing agent-evaluation infrastructure. In an end-to-end clinical-audit case study spanning 16 agent systems and 750 cases, READY reveals differences hidden by autonomous performance: two systems separated by only 0.3 points in autonomous accuracy (72.8% vs. 72.5%) require 39.2% versus 29.6% human review, respectively, to qualify at the same 76% reliability target under the evaluated oversight policy. READY thus shifts enterprise agent evaluation from how well can the agent perform the work? to under what conditions, and at what cost, can it be reliably deployed? By making those conditions explicit and statistically testable, READY provides a basis for comparing agent systems, setting oversight requirements, and making evidence-based deployment decisions.

---


### 79. [A Unified Rate-Distortion Perspective on Vector, Product, and Scalar Quantization](https://arxiv.org/abs/2609.02107)

**<font color=#1a73e8>作者：</font>** Xianghong Fang, Wenlong Mou, Yuan Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete visual tokenization, predominantly driven by vector, scalar, and product quantization, lacks a unified conceptual framework for understanding quantization tradeoffs. In this paper, we propose a unified rate--distortion perspective on modern discrete visual tokenization. By viewing quantization as lossy compression, we characterize the nominal fixed-length coding rate through token count and codebook size, and quantization error as the distortion. Within this framework, we resolve three central questions. First, we theoretically and empirically show that minimizing distortion, rather than maximizing codebook utilization, is the primary intrinsic objective for reconstruction fidelity, with a direct connection to the STE-induced gradient discrepancy. Second, we establish two critical fairness conditions for intrinsic quantization comparison: controlling latent feature statistics and enforcing identical coding rates. Third, under these conditions, we recover the VQ--PQ--SQ distortion hierarchy in modern visual tokenization and show empirically that modern VQ methods achieve the lowest distortion. This work provides a foundational rate--distortion reframing of modern discrete visual tokenization, resolves ambiguities in quantizer evaluation, and provides a controlled framework for isolating intrinsic quantization effectiveness under fixed-rate constraints.

---


### 80. [A Computational Comparison of Fourier Spectral Differentiation and Spatial Automatic Differentiation in Periodic Physics-Informed Neural Networks](https://arxiv.org/abs/2609.02110)

**<font color=#1a73e8>作者：</font>** Xilai Liang, Zhao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) commonly evaluate the spatial derivatives appearing in partial differential equation residuals using automatic differentiation (AD), whose computational and memory costs can become substantial when multiple or high-order derivatives are required. We perform a controlled comparison of spatial AD and Fourier spectral differentiation in periodic physical-space PINNs. Within each paired experiment, the neural representation, temporal differentiation, optimizer, sampling procedure, and training schedule are held fixed, so that the two cases differ only in the spatial differentiation procedure. For the Fourier variant, network outputs are evaluated on a uniform periodic grid and transformed to Fourier space, where spatial derivatives are obtained through spectral multiplication and the same Fourier coefficients are reused across derivative orders. We compare the two procedures in standard PINNs for the Allen--Cahn and Korteweg--de Vries equations and in Causal PINNs for the Allen--Cahn, Korteweg--de Vries, and Kuramoto--Sivashinsky equations. Across these five equation--framework settings, Fourier differentiation yields mean paired end-to-end training speedups ranging from $2.90\times$ to $18.52\times$ and reduces peak allocated graphics processing unit (GPU) memory by $68.7\%$--$94.1\%$. The final relative $L_2$ errors remain of the same order, with neither differentiation procedure showing a consistent accuracy advantage. For the one-dimensional periodic benchmarks considered here, Fourier spectral differentiation therefore provides substantially lower training time and memory usage than spatial AD while retaining comparable solution error, at the cost of requiring a uniform structured spatial grid.

---


### 81. [Disease Burden over Skin Tone: Decomposing the Dermatology-AI Generalization Gap](https://arxiv.org/abs/2609.02111)

**<font color=#1a73e8>作者：</font>** Nirajan Kunwor, Sanjaya Poudel, Quoc-Huy Trinh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dermatology artificial intelligence (AI) models are predominantly trained on light-skinned, cancer-focused image collections, yet they are increasingly proposed for deployment in resource-constrained settings where patients differ from training populations along two confounded axes: skin tone and disease distribution. We investigate whether poor generalization is primarily caused by skin-tone underrepresentation or disease-distribution shift. We evaluate a cancer-trained baseline (ResNet-50 fine-tuned on HAM10000 and ISIC 2019), two dermatology foundation models (DermLIP and MONET), and a general-purpose vision model (DINOv3) as frozen feature extractors. Models are evaluated on a tone-stratified disease-matched dataset (Diverse Dermatology Images, DDI) and a disease-shifted tone-diverse dataset (Skin Condition Image Network, SCIN). Our results show that disease-distribution shift contributes more than skin tone in the evaluated settings. The cancer baseline decreases from 0.62 to 0.21 balanced accuracy when transferred to unfamiliar clinical conditions, while the within-disease skin-tone gap is smaller (0.10-0.18) and inconsistent. Label-free representation analysis shows that this failure reflects a representational limitation rather than only missing output labels: cancer-specialized features poorly cluster unfamiliar conditions (kNN purity lift +0.06 over chance), whereas dermatology-pretrained features retain stronger transferable structure (+0.23). Finally, we show that representation quality predicts recoverable performance under lightweight adaptation. Starting from dermatology foundation models, approximately ten labeled examples per clinical category recover most attainable performance. We release the evaluation protocol and code to support reproducible auditing of dermatology AI generalization.

---


### 82. [Synergistic Information Disentanglement for Omni-modal Slide Representation Learning in Computational Pathology](https://arxiv.org/abs/2609.02118)

**<font color=#1a73e8>作者：</font>** Mingxin Liu, Chengfei Cai, Anwen Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In computational pathology (CPath), developing omni-modal self-supervised learning (SSL) models that integrate histology, genomics, and clinical reports enables transferable representation learning for whole slide images (WSIs). Existing approaches implicitly force heterogeneous modalities into a uniform latent space by contrastive alignment, causing modality collapse where unique, synergistic diagnostic signals (termed as $\mathrm{\Phi}$) are discarded in favor of trivial redundancy. We hypothesize that the strongest task-agnostic SSL training signal stems from distilling the synergistic interactions over merely aligning shared redundancy. To this end, we introduce \textsc{$\mathrm{\Phi}$-Omni}, a synergistic information disentanglement framework grounded in Partial Information Decomposition (PID) theory for slide representation learning. Unlike standard contrastive approaches, \textsc{$\mathrm{\Phi}$-Omni} employs a Synergistic Information Bottleneck (SIB) regulated by the proposed $\mathrm{\Phi}\text{ID}$ objective, which explicitly suppresses marginal redundancy while maximizing irreducible synergy, thereby distilling high-order cross-modal interactions. Following pretraining on breast ($n$=1031) and lung ($n$=919) cohorts, \textsc{$\mathrm{\Phi}$-Omni} demonstrates superior few-shot performance across five independent external datasets spanning eight tasks compared to supervised and SSL baselines. Source code is available here.

---


### 83. [Scalable Bayesian Optimization of Composite Functions for Image-Based Inverse Problems in Materials Characterization](https://arxiv.org/abs/2609.02126)

**<font color=#1a73e8>作者：</font>** Dasol Yoon, Poompol Buathong, Chia-Hao Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating physical parameters from scientific images is a common inverse problem in materials characterization that often relies on expensive physics-based simulations. In electron microscopy, specimen thickness and crystal mistilt are critical parameters that govern how electrons scatter through the sample, and therefore the accuracy of any atomic-scale structure recovered from it. They are commonly inferred by matching experimental position-averaged convergent-beam electron diffraction (PACBED) patterns to simulated ones, but grid searches scale poorly and neural-network methods require extensive pretraining that may not transfer to new conditions. Here, we propose scalable Bayesian optimization of composite functions (SBOCF), a simulation-efficient method that exploits the known composite structure of the image-matching objective and the intermediate information contained in simulated images. By representing PACBED images with patch-level summaries and two correction terms, SBOCF preserves the original pixel-wise objective while reducing the number of modeled outputs from 24,649 to 11. Under a budget of 50 simulator evaluations, SBOCF outperformed standard Bayesian optimization with expected improvement on synthetic SrTiO3 benchmarks with thick and thin specimens, reducing the median final SSE by up to 290x in the thick-sample case. On experimental data, SBOCF produced parameter estimates consistent with previously reported values without task-specific pretraining. For a simulated mistilted specimen, using the SBOCF estimates in a downstream ptychographic reconstruction recovered sharp atoms that were otherwise blurred. These results establish SBOCF as a promising approach for inverse problems involving expensive simulators and high-dimensional structured outputs.

---


### 84. [Beyond Context Windows: Persistent Discovery Context for Data-Centric Agents](https://arxiv.org/abs/2609.02129)

**<font color=#1a73e8>作者：</font>** Jalal Mahmud  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data-centric agents repeatedly perform a discovery step before planning or execution: identifying the data objects relevant to a task. Yet successful discovery outcomes are typically discarded rather than reused. We introduce persistent discovery context, a lightweight memory layer that stores prior intent-to-object mappings and reuses them to augment future retrieval. Across three structured data environments, persistent discovery context consistently improves retrieval quality over metadata-only search, remains effective with automatically generated memories, and exposes a reproducible interference failure mode. In lexically sparse domains, memory-only retrieval can even outperform metadata-based retrieval. These findings suggest that discovery outcomes constitute a useful form of reusable context for data-centric agents.

---


### 85. [Online Non-Monotone DR-Submodular Maximization Matching the Offline $0.401$ Factor](https://arxiv.org/abs/2609.02145)

**<font color=#1a73e8>作者：</font>** Vaneet Aggarwal, Yiyang Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online maximization of nonnegative, non-monotone DR-submodular functions over compact convex down-closed subsets of the $d$-dimensional unit cube. The best known constructive offline approximation factor is $0.401$ under the corresponding meta-solvability assumptions, whereas comparable adversarial online guarantees had remained at $1/e$. We show that this factor is also achievable online. In the post-decision full-information value-oracle model, our algorithm attains factor $0.401$ with sublinear approximate regret when oracle feedback is conditionally unbiased and bounded.
The online algorithm does not run the offline construction on a changing objective. Instead, it replaces the offline objective-dependent box step by a weighted online learner that controls the required residual terms cumulatively. An exact asymmetric balance theorem preserves the offline coefficients despite adversarial variation. The direct implementation has $O(T^{3/4})$ regret and uses $O(dT^{1/4})$ oracle calls per round. More generally, for every $\delta\in[0,1/4]$, batching gives $O(T^\delta)$ calls per round and $O(T^{4/5-\delta/5})$ regret, including a one-call $O(T^{4/5})$ endpoint. Under a positive-anchor condition, randomized blocking retains factor $0.401$ with $O(T^{5/6})$ one-point bandit regret.

---


### 86. [Exact Limits of Random Projections for Preserving Geometry: Distance Recovery, Nearest-Neighbor Rankings, and Covariance Shape in Gaussian Models](https://arxiv.org/abs/2609.02155)

**<font color=#1a73e8>作者：</font>** Piyush Sao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Johnson-Lindenstrauss (JL) lemma guarantees that a random projection of $n$ points to
$m=O(\varepsilon^{-2}\log n)$ dimensions preserves pairwise squared distances within relative
error $\varepsilon$ with high probability, and this dimension order is asymptotically
optimal. In high dimensions, however, distances concentrate around a baseline while key
geometric information lies in much smaller fluctuations. We show that the JL bound can
therefore be uninformative about retained geometry: an independent Gaussian replacement map
can satisfy it even though the replacement cloud is independent of the original data.
We then ask how well any decoder can recover a feature $f(D)$ of a squared distance $D$ from
a linear sketch. Under squared-error loss, the optimal decoder is conditional expectation, so
recovery defines a linear operator whose singular values quantify feature recovery. For
isotropic Gaussian data ($\Sigma=\sigma^2 I_d$), we diagonalize this operator in closed form.
For fixed $k$ with $m,d-m\to\infty$, its $k$th singular value satisfies $\ell_k\approx(m/
d)^{k/2}$.
This yields three sharp consequences. A rank-$m$ sketch retains at most an $m/d$ fraction of
the variance of any feature of one squared distance. If $m\to\infty$ and $m/d\to0$, the
expected Kendall correlation is $\frac{2}{\pi}\sqrt{m/d}(1+o(1))$; for fixed $q$, nearest-
neighbor agreement tends to $1/q$. Yet one projection can satisfy the JL bound while mean
Kendall correlation vanishes when $\log n\ll m\ll d$. After removing scale, Haar-averaged
retained covariance-shape information is $(m/d)^2$. Thus JL distance preservation does not
quantify the geometry available for comparison or inference.

---


### 87. [OBJECTION! Lawyer Agents Mitigate Guilty Bias in Legal Judgment Prediction](https://arxiv.org/abs/2609.02158)

**<font color=#1a73e8>作者：</font>** Jaehoon Jeong, Jay-Yoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal Judgment Prediction (LJP) models are typically trained on documents that describe facts from a prosecutorial perspective. Existing datasets further exhibit severe label imbalance toward guilty outcomes. Consequently, these models suffer from "Guilty Bias", blindly accepting the prosecution's narrative as objective truth. Previous studies employing three-step reasoning structures or training on synthetically generated innocence data improve overall accuracy, but they still fail to mitigate bias at inference time.
In this paper, we introduce OBJECTION, an inference-time pipeline that integrates an Adversarial Lawyer Agent into each 3-step reasoning of offense, unlawfulness, and culpability. Unlike generic critics, our agent actively challenges the model's presumptions of guilt by injecting legal defense arguments at each reasoning stage. To thoroughly evaluate this, we present a new "Natural Innocent" dataset including 3.4k real-world cases, overcoming the limitations of synthetic innocence benchmarks. Test results show that OBJECTION drastically reduces the False Guilty Rate (FGR) from 82.93% (SOTA baseline) to 16.69%, proving its capability to perform substantive legal reasoning. This work denotes a key progress toward aligning Legal AI with the presumption of innocence.

---


### 88. [GeoSPRINT: Geometric Redundancy-Aware Step Pruning for Inference in Diffusion Trajectories](https://arxiv.org/abs/2609.02160)

**<font color=#1a73e8>作者：</font>** Arpita Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models achieve high sample quality but remain expensive at inference time because sampling requires many sequential neural function evaluations (NFEs). Existing acceleration methods either use fixed step-skipping schedules, adapt step sizes based on local numerical error, or require additional training. We introduce GeoSPRINT (Geometric Step Pruning for Inference in Trajectories), a training-free framework for constructing non-uniform sampling schedules from the geometry of denoising trajectories. GeoSPRINT detects geometrically redundant steps using a hyperplanarity test in latent space, implemented efficiently via QR factorization, and converts the resulting redundancy profile into a sampling schedule that allocates more steps to high-curvature regions of the trajectory. In addition, we introduce the trajectory projection score $\alpha_{\mathrm{traj}}$, a residual-variance metric that quantifies trajectory straightness and serves as a model-free diagnostic for rectified flow quality. Across CIFAR-10 ($32{\times}32$), LSUN Church ($256{\times}256$), and Stable Diffusion v1.5 ($512{\times}512$ latent), GeoSPRINT consistently improves over uniform DDIM (Denoising Diffusion Implicit Models) schedules at matched NFE budgets. On CIFAR-10, GeoSPRINT improves FID (Fréchet Inception Distance) by 0.7-1.1 over DDIM across 49-89 NFEs and surpasses DPM-Solver++ at NFE${\geq}30$ despite using a first-order DDIM solver. On LSUN Church, it reduces FID from 1.48 to 1.26 at 52 steps, and on Stable Diffusion v1.5 it achieves up to 1.93 FID improvement over DDIM. These results show that trajectory geometry provides a useful global signal for allocating inference steps and that schedule quality can substantially improve diffusion sampling efficiency without retraining.

---


### 89. [Progressive Pseudo-Label Optimization for Point-Supervised Change Detection](https://arxiv.org/abs/2609.02171)

**<font color=#1a73e8>作者：</font>** Hailong Ning, Hao Wang, Yimeng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point-supervised change detection (PS-CD) aims to identify pixel-level changes between bi-temporal images using only sparsely annotated points. Although point annotations substantially reduce labeling costs, their limited spatial coverage often results in incomplete and noisy pseudo-labels. To address this issue, we propose a two-stage framework that introduces SAM2 priors into PS-CD and progressively adapts them to the target task. In Stage I, SAM2 generates object-aware candidate masks from point annotations on the bi-temporal images, and a bi-temporal mask selection strategy is designed to convert generic segmentation responses into more reliable change pseudo-labels. Subsequently, a lightweight CNN refinement module with an uncertainty-aware loss is employed to improve boundary quality and local structural consistency. In Stage II, we construct a teacher-student self-training framework in which the teacher is updated by exponential moving average and periodically refreshes the pseudo-labels. This design establishes a closed-loop optimization process that alternates between pseudo-label refinement and model re-optimization. Experiments on three benchmark datasets, including WHU-CD, LEVIR-CD, and SYSU-CD, demonstrate that the proposed method outperforms previous weakly supervised approaches on most benchmarks and remains competitive with several fully supervised methods.

---


### 90. [CC-4DGS: Computational Deformation and Point-Cloud Compression for Storage-Efficient Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.02184)

**<font color=#1a73e8>作者：</font>** Kyungdae Park, Chae Eun Rhee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic four-dimensional (4D) Gaussian Splatting has emerged as a powerful explicit representation for high-quality view synthesis, yet existing methods still require tens to hundreds of megabytes per scene due to their heavy reliance on large multi-resolution hash tables and high-dimensional Gaussian attributes. This paper presents CC-4DGS, a storage-efficient and scalable framework that rethinks both deformation modeling and canonical attribute storage. First, we introduce a computational deformation field (CDF) that replaces large multi-resolution learnable hash tables with deterministic dense hash encoding and compact neural decoders, enabling on-the-fly synthesis of deformation features while reducing deformation storage to only 1--3 MB per scene. Second, we propose a compression of canonical point-cloud attributes (CCA) pipeline that compresses high-dimensional spherical harmonic appearance terms and auxiliary Gaussian attributes via conditional autoencoding, selective quantization, and residual codebooks, achieving 3--5$\times$ point-cloud reduction with negligible quality loss. Together, these components yield a unified representation that preserves real-time rendering performance while reducing total storage to 20--30 MB. Extensive experiments across the N3DV and Technicolor Light Field datasets demonstrate that CC-4DGS achieves reconstruction accuracy comparable to state-of-the-art methods such as Swift4D, while offering significantly improved storage efficiency and favorable runtime-memory trade-offs.

---


### 91. [Examining the Vulnerability of Multi-Agent Medical Systems to Human Interventions for Clinical Reasoning](https://arxiv.org/abs/2609.02191)

**<font color=#1a73e8>作者：</font>** Benjamin C Liu, Dillon Mehta, Rishi Malhotra 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human interventions at fault points can alter the diagnostic accuracy of multi-agent medical systems. We defined fault points as moments in AI agent conversations, in which an agent's reasoning became most vulnerable to external influence. Using the MedQA dataset, this study analyzed simulated doctor-patient conversations to measure how interventions shifted reasoning and accuracy. Correct intervention methods showed an improvement in baseline diagnostic accuracy of up to 40%, while incorrect or bias-related interventions degraded performance by up to 6% and increased diagnostic drift and uncertainty. Beyond performance changes, our analysis revealed behavioral similarities between cognitive biases in simulated agent environments and real-world clinical practice. Examples included premature closure and susceptibility to misleading cues. Overall, these findings demonstrate that identifying and guiding fault points with human interventions may provide a mechanism for improving diagnostic robustness in multi-agent medical systems.

---


### 92. [Learning the Constitutive Behavior of Materials via Neural Operators and Causal Attention: Case Studies in Plasticity and Damage](https://arxiv.org/abs/2609.02194)

**<font color=#1a73e8>作者：</font>** Rishabh Arora, Lisa Scheunemann, Tim Brepols 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical constitutive modeling of path-dependent inelastic materials relies on internal state variables whose evolution equations must be postulated based on domain knowledge and calibrated against experimental data. However, in many practical settings, the relevant internal variables are typically not measurable in experiments, and the constitutive response must be inferred entirely from measured strain-stress data without any prior knowledge of the material's internal state. We propose a data-driven constitutive modeling framework based on the concept of a material operator, which treats a deforming material as a functional mapping from its entire strain history to the corresponding stress response. In contrast to traditional autoregressive or recurrent formulations, the model is trained directly on full loading paths as function-to-function mappings, predicting complete stress trajectories in a single parallel forward pass. Temporal path dependence is enforced through a causally masked attention mechanism embedded within the operator, which restricts the model's attention to past material states while preserving computational parallelizability. Spectral convolutions provide discretization-invariant representations in the frequency domain, while causal attention captures highly adaptive, non-local history dependence. Furthermore, sinusoidal activation functions are used to resolve the strong nonlinear transitions inherent in inelastic regimes. The framework is evaluated across multidimensional, rate-independent material models exhibiting complex phenomena, with an emphasis on nonlinear plasticity and ductile damage accumulation. The results demonstrate accurate and robust predictions of irreversible deformation mechanisms while simultaneously achieving resolution invariance and excellent parallel efficiency.

---


### 93. [SMart: A Multi-source Multi-phase Time Series Representation Transfer Framework](https://arxiv.org/abs/2609.02203)

**<font color=#1a73e8>作者：</font>** Fang He, Wang-chien Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series representation learning (TSRL) has attracted growing research interests in recent years. Two recent explorations in TSRL are: i) exploiting a transformer-based framework to learn time series; ii) instead of using only the targeted dataset, borrowing time series from other datasets to to facilitate representation transfer. While these two explorations are shown effective, the self-supervised time series recovery task in (i) and the single-source dataset used in (ii) are technically simple and thus can be enhanced with new ideas. In this work, we propose a new TSRL framework, namely multi-source multi-phase time series representation transfer (SMart), which has two novel mechanisms to address the aforementioned deficiencies: 1) a multi-phase recurrence plots recovery task, in three alternative modes, for guiding the encoder to embed time series dynamics into the time series representation; and 2) a source dataset selector to select multiple suitable source datasets to supplement the original target dataset for pre-training the TSRL encoder. Experimental results show that SMart outperforms several state-of-the-art models for time series representation learning, classification and regression on both uni-variate and multi-variate time series datasets, reducing mean absolute error up to 19.5% for time series regression, and increasing average accuracy up to 1.34\% for time series classification.

---


### 94. [Agentic Settlement Protocol: An Application Profile for Refundable, Delayed-Fulfilment Agent Commerce on Stablecoin Rails](https://arxiv.org/abs/2609.02208)

**<font color=#1a73e8>作者：</font>** Behnam, Mohammadkhani, Atul Khekade 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous agents can already pay per request: HTTP-native protocols such as x402 let an agent sign a stablecoin authorization and receive a resource in the same round trip. That model is atomic and final, which suits metered access and fails commerce: a purchase made on a person's behalf -- a service appointment, a physical order, a flight -- is large, frequently cancelled, and should not become the seller's money until delivery. We present the Agentic Settlement Protocol (ASP), an application profile over on-chain authorize-and-capture escrow (as standardised by the Commerce Payments Protocol) for businesses whose fulfilment is confirmed off-chain by their own order, scheduling, invoicing or booking system, abstracted as a fulfilment engine. ASP contributes: a three-deadline hold model separating the issuance deadline, escrow expiry and the engine's inventory expiry by an explicit submission-inclusion-finality margin, under which no inventory is issued against reclaimable funds; a fulfilment-verification ladder stating who is trusted to trigger capture, what their attestation proves, and under what challenge window; engine-authoritative partial refunds with a refund-liquidity order and per-seller exposure controls, including atomic exposure reservation, that bound the operator's credit risk; distributor revenue share that is provably unprofitable to self-deal; a single-currency-per-charge invariant; and a normative interface specification (x402 scheme, vault ABI, operator and connector APIs, conformance levels) intended to let independent implementations interoperate. The design originated in a review of travel-agency participation in agentic settlement and is instantiated on the XDC Network. This is a design paper; a fault-injection evaluation plan is specified and measurement is left to follow-up work.

---


### 95. [Asymmetric Paired-Annotation Learning for Multi-Structure ULF Pediatric Brain MRI Segmentation](https://arxiv.org/abs/2609.02210)

**<font color=#1a73e8>作者：</font>** Ha-Hieu Pham, Dang P.M. Cao, Minh Hoang Pham 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Portable ultra-low-field (ULF) MRI can expand access to pediatric neuroimaging, but segmentation at 0.064 T remains challenging because anatomical boundaries are weakly delineated, small structures may be only partially visible, and high-field references can be locally misregistered. The LISA 2026 Challenge provides two non-equivalent annotations reflecting different sources of anatomical evidence: a highfield-derived (HF) mask defining the scored target and a low-field-edited (LF) mask aligned with visible ULF anatomy. In this challenge report, we describe AURA, an nnU-Net-based asymmetric supervision strategy that treats these annotations as distinct observations rather than interchangeable ground truths. AURA anchors training to the HF mask and incorporates the LF mask through a bounded reliability gate based on label disagreement, boundaries, predictive uncertainty, class reliability, and training stage. On a 16-case development split, the HF-supervised baseline, AURA, and their ensemble achieved Dice scores of 0.7984, 0.7950, and 0.7988, respectively, while the ensemble achieved an HD95 of 1.8892 and an ASSD of 0.7855. These results provide a preliminary evaluation of AURA within the LISA 2026 Challenge and motivate further assessment on the hidden test set and external ULF cohorts. Our code and pretrained models are available at this https URL A-nnU-Net-based-asymmetric-supervision-strategy.

---


### 96. [FuDU: A Fuzzy Dual-dimensional Uncertainty Framework for Streaming Active Learning in Industrial Defect Detection](https://arxiv.org/abs/2609.02212)

**<font color=#1a73e8>作者：</font>** Zhaoyang Wang, Haiyong Chen, Binyi Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ensuring the reliability of deep learning models in real-time industrial defect detection is critical for high-stakes quality inspection. To mine uncertain samples within continuous industrial media streams, thereby enhancing the reliability of the detection system, this paper proposes a streaming active learning method based on the Fuzzy Dual-dimensional Uncertainty (FuDU) framework. Specifically, we first design a Prototype-based Global Uncertainty Quantification (PGUQ) module on the backbone to evaluate image-level uncertainty via normal/defective feature prototypes. A Dual-entropy defect Uncertainty Evaluator (DeUE) is then integrated into the detection head to quantify box-level uncertainty. Finally, by modeling uncertainty as systematic error, we propose a fuzzy dual-dimensional uncertainty-aware strategy that leverages fuzzy inference to fuse dual-dimensional uncertainties, enabling expert knowledge-driven adaptive sampling decisions. Comprehensive experiments demonstrate that FuDU is efficient and flexible, making it well-suited for challenging industrial inspection tasks such as the detection of nuclear fuel rod defects. Our code is publicly available at: this https URL.

---


### 97. [Signal or Noise? Auditing Rotation-Induced Saliency Drift in Medical and Aerial Imaging](https://arxiv.org/abs/2609.02224)

**<font color=#1a73e8>作者：</font>** Khawaja Murad ul Hassan, Mehran Ebrahimi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-hoc saliency maps such as Grad-CAM are increasingly used to audit why a deployed vision model made a decision, yet the heatmap drifts when the input is rotated, even when the prediction is unchanged. In domains with no canonical orientation, such as histopathology and aerial imagery, this undermines using saliency as evidence. We ask whether that drift is faithful signal or noise introduced by the CAM operator, and answer it by measuring equivariance at every stage of the operator rather than inferring it from the network's output. The instability is not where one would guess: the channel weights are the most rotation-stable stage, and on ResNet-50 exactly stable, because a GAP+linear head makes the class gradient field spatially constant. What moves is the spatial activation tensor, and the classifier's own pooling discards that movement. A causal test confirms the consequence: occluding the pixels whose saliency drifts costs the model less than occluding random pixels, at either orientation. The drift is carried by degrees of freedom the classifier throws away, which is what makes removing it faithful rather than destructive. EquiGrad-CAM is a training-free wrapper that takes T rotated views, inverse-rotates each view's saliency into a common canonical frame, and averages. On the full ImageNet-1K validation set it raises equivariance over single-view Grad-CAM by +36.0% (ResNet-50), +87.5% (VGG-16) and +247% (ViT-B/16); a scale-matched ablation isolates alignment before averaging, not the locus of aggregation, as the driver. It beats rotation-augmented training without retraining, lifts zero-shot CLIP by +145%, and yields rotation-consistent explanations on PatchCamelyon and RESISC45. Its by-product PEUM ranks explanations by how reproducible they are, at no cost beyond the views already taken. Code: this https URL

---


### 98. [PhoenixNest-Video: Evidence-Grounded Multimodal Agent Framework for Automated Video Interview Assessment](https://arxiv.org/abs/2609.02231)

**<font color=#1a73e8>作者：</font>** Fan Yuxuan, Huang Miaojun, Zhang Haimei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interview assessment requires per-criterion judgments grounded in behavioral evidence, yet surging applicant volumes have made human-only evaluation costly and inconsistent, while existing AI approaches yield opaque scores without traceable rationale. We introduce PhoenixNest-Video, an evidence-grounded multimodal agent framework for automated video interview assessment. It builds a semantic video graph as structured working memory, performs rubric-conditioned retrieval with cross-modal verification across visual, audio, and textual streams, and produces per-criterion scores anchored to the candidate's materials. A Scorer trained via Rubrics-based Reinforcement Learning with dual rewards for rubric alignment and score-level differentiation internalizes the discriminative structure of multi-level rubrics. PhoenixNest-Video attains 91.50\% grade-level accuracy on VInterview-2025, outperforming substantially larger proprietary models. A compact, rubric-grounded agent therefore scores candidates in closer agreement with an expert panel than direct prompting of much larger models, and exposes the evidence behind each score for human review.

---


### 99. [Recursive Value Learning for Long-Horizon Offline Goal-Conditioned RL](https://arxiv.org/abs/2609.02237)

**<font color=#1a73e8>作者：</font>** Hyeonseong Jeon, Youngwoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling offline goal-conditioned reinforcement learning (GCRL) to long-horizon tasks is difficult because (1) long-range value learning depends on shorter-range estimates that may still be inaccurate, and (2) max-based value backups can amplify overestimation through repeated propagation. We propose DCRL (Divide-and-Conquer RL), which recursively decomposes each trajectory segment into a balanced binary tree and trains the values from leaves to root. Each parent is therefore updated only after its children, using an exact factorization of the observed route rather than selecting among noisy alternatives. Since this objective learns values along demonstrated routes that are not necessarily optimal, DCRL jointly propagates values across trajectories to discover shorter routes. Thanks to the balanced binary tree, DCRL reduces worst-case bootstrap depth from linear to logarithmic, and this shorter dependency structure empirically corresponds to much slower error accumulation. Across diverse goal-reaching tasks, DCRL substantially outperforms prior flat offline GCRL methods, and on the five most challenging long-horizon OGBench tasks, it improves the best prior average score from 55 to 64, surpassing all flat and hierarchical baselines.

---


### 100. [Similarity-Aware Personalized Federated Learning in Heterogeneous Environments](https://arxiv.org/abs/2609.02241)

**<font color=#1a73e8>作者：</font>** Arun Kumar A V, Sunil Gupta, Dang Ngyuen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) allows decentralized clients to train models collaboratively while preserving data privacy. However, distribution mismatch across clients often leads to poor global generalization and degraded local client-level performance. In such scenarios, some of the clients with their local models trained solely on local data may perform better than the globally learnt model, thus nullifying the benefits of collaborative federated learning. To address this, we propose SAPE-FL (Similarity-Aware Personalized Federated Learning), a novel personalization framework that anchors each client's model to both the global model and a similarity-weighted peer averaged model. By incorporating dynamic, client-specific regularization based on both model similarity and output similarity, SAPE-FL adaptively balances global knowledge transfer and peer collaboration while filtering out dissimilar clients. This dual anchoring mitigates negative transfer and enhances robustness in heterogeneous settings. We theoretically analyze our algorithm establishing its convergence guarantees and empirically show that SAPE-FL outperforms state-of-the-art methods under high statistical heterogeneity and low client data regimes.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-187](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
