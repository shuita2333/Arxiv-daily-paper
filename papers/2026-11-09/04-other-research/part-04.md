# 📦 其他研究 | 2026年11月09日

> 本类共 **237** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-237](./part-05.md)

---

### 151. [GuidedWAM: Training-Free Energy Guidance for World Action Models in Autonomous Driving](https://arxiv.org/abs/2611.07912)

**<font color=#1a73e8>作者：</font>** Xiyan Su, Finn Rasmus Schäfer, Hojun Lim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) for autonomous driving couple the driving policy and the visual world model in a single generative network whose objectives are fixed post-training. Conditioning on a new driving objective requires retraining. We study energy guidance as a general mechanism and present GuidedWAM, a model-agnostic framework for injecting driving objectives into frozen WAMs at sampling time. Our framework constructs each objective as differentiable energies on the sampler's intermediate clean-action estimate, which needs only forward access to the frozen model, and is stabilized by sampling-time guidance scheduling, per-energy normalization, and velocity-bounded correction. On the NAVSIM v2 hard-split, guidance improves all three frozen, publicly released WAMs by 1.8 to 3.6 EPDMS, averaged over three sampler seeds, and adds less than 10% to the sampling time per step. These results position energy guidance as a practical post-training control channel for WAMs.

---


### 152. [How Finite Brains Generalize Without Bound: Spatial Memory as a Universal Computer](https://arxiv.org/abs/2611.07920)

**<font color=#1a73e8>作者：</font>** Yuhang He, Si Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A child who learns to add small numbers adds numbers of any length. LSTMs and Transformers trained on short sequences fail on longer ones. We trace the difference to what a learner reads when it decides. A position, a count or a time keeps taking new values as the input grows: it is a coordinate, and a learner that reads one meets in every long input values its experience never covered. Whether two things are the same has the same two answers at every size: it is a coincidence, and a learner that reads only coincidences finds in a long input nothing that short inputs lacked, so finite experience fixes its rule for every size. The memory carries the size of the input and the rule stays finite, and this determines the memory a generalizing brain can have: a memory that grows while what the learner reads of it stays finite has to look the same from every place, so it is made of cycles, and the past is reached by asking what happened when the cycles last stood where they stand now. The cycles are the grid modules, the cells that detect their return the place cells, the records the hippocampal index; a prefrontal controller moves the cycles and never sees them. Reading only coincidences costs no power: what finite experience fixes in such a learner is what Turing machines compute in step with their input, which is why a circuit that evolved to find the way home can learn arithmetic and grammar. In a network of neurons this machine of cycles is the dynamics seen through its symmetry, and symbols are its invariants. Trained on strings up to 40 symbols, the machine is at least 99% correct, on average over lengths 41 to 500, on nine of fifteen benchmark tasks, five of them tasks that no LSTM or Transformer solves; given new cycles after training it reverses strings of 15,015 symbols without error and fails beyond that on the curve the theory predicts; and its controllers run unchanged on neurons.

---


### 153. [StitchEdit: Stitching Depth Priors into Image Editors via Per-Layer Gradient Probing](https://arxiv.org/abs/2611.07922)

**<font color=#1a73e8>作者：</font>** Qin Guo, Dan Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided image editing with diffusion models struggles with spatial edits (e.g. manipulating objects, changing viewpoints, manipulating occlusions) that depend on the 3D structure understanding of a scene. Marigold and follow-up work demonstrate that a pretrained diffusion backbone already harbors strong geometric priors that can be activated for depth estimation, yet how to redirect these priors toward editing remains unresolved. Through per-layer gradient probing, we discover that the editing and depth objectives are compatible in early transformer layers but actively conflict in late layers, explaining why naive depth-conditioned editing either ignores geometry or degrades visual quality. We present StitchEdit, which first activates the backbone's geometric capability via a lightweight depth-denoising adapter, then selectively fine-tunes this adapter for editing using a probe-guided per-layer learning rate schedule that preserves depth knowledge where it helps and prunes it where it conflicts. On the proposed StitchEditBench, a benchmark of 150 geometry-dependent edits spanning spatial transformation, occlusion manipulation, and viewpoint change, StitchEdit consistently surpasses both instruction-based and depth-conditioned baselines on perceptual quality and geometric fidelity.

---


### 154. [AraEngage: Interpretable Linguistic Correlates of Engagement in Arabic Facebook News](https://arxiv.org/abs/2611.07926)

**<font color=#1a73e8>作者：</font>** Shimaa Ibrahim, Nour Elhouda Dalloua, Md. Rafiul Biswas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Engagement features developed for English are routinely applied to Arabic, but unvocalized Arabic changes what a lexical feature measures. We introduce AraEngage, a query-defined sample of 10,000 public Arabic Facebook news posts from 2,451 pages in 57 countries (2023-2024) that pairs engagement counts with interpretable linguistic features. We use it to examine which interpretable Arabic indicators are associated with follower-normalized engagement, and how far those associations can be trusted given publisher context, the definition of engagement, and lexical ambiguity. Religious expressions, message length, sentence length, and lexical density are the leading correlates in a Random Forest model ($R^2$ = 0.38 on a post-level split) interpreted with SHAP. Unlike English news, positive sentiment is associated with higher engagement in this Arabic news sample. Message length shows a length paradox: unadjusted raw engagement is highest for long posts, whereas the model's attributions for follower-normalized engagement favor short posts. A linguistic audit identifies why standard lexicon features are fragile in unvocalized Arabic: imperative lists contain homographs such as the form read as "express!" that is also the frequent preposition "via", hedge lists conflate the possibility marker qad + imperfect ("may") with the emphatic qad + perfect ("has indeed"), and religious lists mix devotional formulas with place names in political news. These are plausible sources of measurement error that may attenuate the near-zero associations of imperatives and hedges. All findings are observational associations with operationalized indicators. We release the derived linguistic features, engagement counts, refined lexicons, and analysis code; raw posts are not redistributed, in line with CrowdTangle terms.

---


### 155. [Flux as a Codec: Zero-Shot Lossy Compression with Flux](https://arxiv.org/abs/2611.07929)

**<font color=#1a73e8>作者：</font>** Fuma Kimishima, Jinjia Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose FluxC, a zero-shot codec that uses Flux as a compression prior. Although DiffC has shown that pretrained diffusion models can serve as zero-shot codecs, we ask how the choice of coding path and reconstruction method affects rate--distortion--perception behavior. We analyze FluxC along three axes: coding cost and bit allocation, reconstruction method, and low rate distortion. At matched signal-to-noise ratio (SNR), we show that the path choice does not affect the ideal information rate, but changes how bits are allocated across time steps. For reconstruction, we compare ancestral sampling, one-step ODE reconstruction, and many-step ODE reconstruction. Our analysis shows that ODE-based reconstruction can achieve lower distortion than ancestral sampling, especially in the low rate regime. Experiments on Gaussian sources and natural images support this prediction. Moreover, FluxC performs competitively with, and in some cases outperforms, recent neural image compression methods, suggesting that Flux can serve as a principled zero-shot codec.

---


### 156. [The Blindfolded Controller: Decision Model-Guided Training for Reinforcement Learning](https://arxiv.org/abs/2611.07934)

**<font color=#1a73e8>作者：</font>** Muhammad Ibrahim Khan, Aniket Dixit, Faizan Ahmed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) provides a framework for continuous improvement through interaction with an environment. However, RL agents struggle against tasks that offer exploration challenges and sparse rewards, because learning efficient policies from scratch is slow and sample-inefficient. In contrast, decision models (DMs), given a description of the environment and task, can perform well in sparse-reward tasks, but, as they do not learn from reward, they are not able to improve towards the optimal solution. In this paper, we present Decision Model-Guided Training (DMGT), a technique that uses a DM with a description of the environment and task to initialise an RL policy, combining the DM's ability to act without training with RL's ability to improve from reward. Instead of exploring from scratch, the agent reaches the goal and receives reward from its first episodes, and RL then improves its policy beyond what the DM achieves. We demonstrate through experiments on seven tasks that our approach outperforms RL in all seven and DM in five. In addition, we provide comprehensive guidelines, derived from ablation studies, for describing an environment and task to a DM.

---


### 157. [Towards Scalable Diagnostic-Driven Whole-Slide Image Retrieval for Pathology Archives](https://arxiv.org/abs/2611.07935)

**<font color=#1a73e8>作者：</font>** Jingsong Liu, Youssef Wally Han Li, Weiwei Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing adoption of digital pathology has rapidly expanded collections of hematoxylin-and-eosin whole-slide images, yet efficient navigation through these archives remains challenging, as metadata is often inconsistent or unavailable. Content-based image retrieval addresses this challenge by identifying similar cases directly from visual representations instead of manual annotations or metadata. Existing retrieval systems have demonstrated promising performance but largely rely on handcrafted indexing pipelines and predefined sampling strategies, constraining scalability and generalization. Here, we present CLEAR-WSI (Constant-Length Embedding for Automatic Retrieval of Whole-Slide Images) as a scalable, diagnostic-driven slide-retrieval framework, validated on both public and clinical data. Using a fixed-length slide embedding, CLEAR-WSI refines retrieved candidates with either a predicted diagnostic label or the ground-truth label, depending on the retrieval setting. Newly processed cases are subsequently added to the expanding memory bank, allowing the retrieval archive to grow over time. On a comprehensive benchmark consisting of two public and one private clinical datasets representing four retrieval tasks, CLEAR-WSI improves Precision@5 over the strongest evaluated baseline, with gains on CAMELYON16 (3.10), BRACS-1 (2.75), BRACS-2 (1.95), and X-HER2 (3.75). Additional ablation and latency studies further examine the contribution of each component and highlight its potential for scalable deployment.

---


### 158. [IDPrior: Decoupling Identity Generation from Facial Image Synthesis](https://arxiv.org/abs/2611.07941)

**<font color=#1a73e8>作者：</font>** Fadi Boutros, Meriç Demirörs, Darian Tomašević 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale identity-labeled face datasets are essential for training modern face recognition models, yet collecting and annotating such data is costly and raises privacy and ethical concerns. Existing synthetic face generation methods typically derive identities from predefined class labels, unconditional image generation, or predefined latent sampling strategies, without explicitly modeling the underlying distribution of facial identities. In this paper, we propose IDPrior, a two-stage framework that decouples identity generation from image synthesis. We first learn a diffusion prior in the embedding space of a pretrained face recognition model to model the distribution of facial identities and generate novel identity embeddings. These embeddings are then used to condition a pretrained identity-conditioned diffusion model (DM), enabling the synthesis of multiple images of the same identity. This modular design provides a scalable approach to identity generation while remaining compatible with existing and future identity-conditioned DMs. Experiments indicate that IDPrior generates diverse and well-separated identities while maintaining a closer correspondence to the distribution of authentic identities. Face recognition models trained on datasets generated using IDPrior-generated identities achieve competitive or improved performance compared with existing synthetic-data-based methods across multiple face verification benchmarks. Code and generated datasets are publicly available at this https URL.

---


### 159. [Beyond the Keyword: A Human-Annotated Benchmark for Arabic Anxiety-Related Discourse](https://arxiv.org/abs/2611.07949)

**<font color=#1a73e8>作者：</font>** Shimaa Ibrahim, Mabrouka Bessghaier, Md. Rafiul Biswas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Keyword retrieval returns expressions of personal anxiety together with many other uses of anxiety-related language. We present a benchmark of 1,000 Arabic Twitter/X posts retrieved with the keyword qalaq ("anxiety/worry") and annotated for six discourse functions. Two native Arabic-speaking annotators labeled every post independently, reaching 51.1% raw agreement (Cohen's $\kappa = 0.378$). We then reviewed all 489 disagreements and all 511 agreements under the same guidelines. The review changed 120 of the agreed labels (23.5%), which shows that agreements need auditing as well as disagreements. The final labels form a consensus reference; on a random sample of 200 posts, an additional annotator agreed with it on 60.5% of posts ($\kappa = 0.517$). Against this reference, Fanar-C-2-27B reaches 79.8% accuracy and macro-F1 0.784 ($\kappa = 0.749$). Its errors concentrate in the residual category (41.1% of errors; precision 0.905, recall 0.447), whose definition is internally inconsistent in the executed prompt, so the low recall cannot be attributed to the model alone. Sociopolitical Anxiety (27.1%) outnumbers Personal Emotional Expression (22.0%); these are assignment proportions in the sample, not estimates of prevalence or retrieval precision. We release the guidelines, a residual-subtype scheme, a fixed data split, label provenance, and evaluation code.

---


### 160. [Leakage- and Label-Aware Benchmarking of Class-Imbalance Strategies for Multimodal Chest X-Ray and EHR Classification](https://arxiv.org/abs/2611.07950)

**<font color=#1a73e8>作者：</font>** Dang-Khoa Bui, Quang-Huy Tran, Minh-Khoi Nguyen-Bui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarks of class-imbalance strategies for multimodal chest X-ray (CXR) and electronic health record (EHR) prediction are often evaluated on record-level splits of cohorts in which one patient contributes several radiographs. We audit such a benchmark on 29,083 MIMIC-CXR radiographs of 10,479 patients with eight diagnosis targets. First, the record-split benchmark was misleading: a lookup table that copies the label of a development-set radiograph with the same EHR vector nearly matched the best model, and on unseen patients every model fell to the level of predicting every case positive. Second, tracing the labels back to MIMIC-IV explained why: each patient's labels are keyword matches on the diagnosis codes of a single admission, copied, with one EHR vector per patient, to all of the patient's radiographs, so about a third of the radiographs carry labels that differ from the codes of their own admission. Third, under patient-separated evaluation with admission-aligned and rule-refined labels, the initial conclusions do not hold: in the evaluated configurations no imbalance strategy raised the observed mean macro F2 over no augmentation by more than 0.01, tuned tree ensembles showed no consistent advantage over tuned logistic regression, and the released EHR variables stayed at the level of the all-positive baseline, whereas the diagnostic history available at imaging time and image embeddings exceeded it, including, with rule-refined labels, a CheXpert-trained encoder that never saw these radiographs; RAD-DINO had seen 96.6% of them during self-supervised pretraining. Adding either encoder to the diagnostic history gave no statistically significant F2 gain; exploratory AUROC gains were significant with RAD-DINO but not with DenseNet. We provide reusable diagnostics, a leakage-aware protocol and a checklist.

---


### 161. [Invariance before structure: two modes of emergent compression in representation learning](https://arxiv.org/abs/2611.07952)

**<font color=#1a73e8>作者：</font>** Hardik Rajpal, Dan Goodman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned representations show striking invariance across biological and artificial neural networks, with different substrates and variations driven by drift, heterogeneity and initialisation. To understand this invariance, we propose Emergent Adaptive Representation Learning (EARL), a framework that distinguishes two modes of emergence in learned representations: state-space compression, where a learned representation gains predictive power over its own future beyond what the network's units can predict individually, and parameter-space compression, where networks with different micro-level parameters converge to the same representation. We formalise both as Fisher sensitivities and introduce ensemble-level information-theoretic measures for each. In a recurrent reservoir with a trained bottleneck, parameter-space compression rises within the first few epochs of training and partly independently of the task, whereas state-space compression rises about 30 epochs later and only when the network begins to learn the temporal structure of the task. These results suggest that invariance to the substrate and task-specific emergent structure are acquired in distinct phases of learning.

---


### 162. [A Behavioural Framework for Predicting and Understanding Loss of Control in Frontier Artificial Intelligence Systems](https://arxiv.org/abs/2611.07953)

**<font color=#1a73e8>作者：</font>** Yao Huang, Yichi Zhang, Yifan Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier artificial intelligence (AI) systems are increasingly operating over longer horizons with diminishing human oversight, raising the risk of loss of control: systems acting beyond effective human control with potentially irreversible consequences. Because such failures may become observable only after containment is difficult, they must be assessed prospectively. We introduce a behavioural framework that decomposes loss-of-control risk into three factors: misaligned motive, harm-enabling capability, and monitoring evasion. We operationalise these factors through 13 measurable aspects and 29 evaluation tasks, whose scores are combined into a single loss-of-control (LoC) score. Across 13 frontier models, the LoC score shows strong prospective validity, correlating with failure rates in contained long-horizon risk scenarios (Pearson r = 0.84). Risk varies systematically across models and cannot be explained by capability alone. We further show that the framework can guide targeted mitigations: fine-tuning and monitoring directed at diagnosed vulnerabilities reduce failure rates while largely preserving general performance. These results provide a practical basis for predicting, understanding, and mitigating loss-of-control risk before it materialises.

---


### 163. [Rotation Is Token-Blind: A Structural Criterion for Post-Training Quantization of Feed-Forward Geometry Transformers](https://arxiv.org/abs/2611.07955)

**<font color=#1a73e8>作者：</font>** Huanfei He, Bohao Zhang, Jiaxin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D models use Transformers to predict camera poses, depth, and structure in one pass, avoiding iterative multi-view optimization. Long sequences and deep attention incur high compute and memory costs, motivating Post-Training Quantization (PTQ) for deployment. Existing PTQ methods mainly suppress channel-wise outliers by smoothing or orthogonal rotation. Geometry Transformers introduce a different challenge: heterogeneous token types share one activation quantization grid. A few special tokens may exert high leverage over global outputs and be updated by only a subset of blocks. Token-blind transforms, which apply the same transformation to every token, reduce overall quantization error but cannot remove differentiated degradation across token types. We propose QMapAnything, a structure-aware PTQ framework. We cast floating-point-preserving rotation and smoothing as a token-blind reparameterization group, and prove that they yield common-mode gains while leaving relative token SNR unchanged. We introduce a statistic $\Gamma$ that combines a special token's quantization disadvantage and output leverage to predict whether differentiated bias correction is needed beyond rotation. Experiments on geometric benchmarks show that W4A8 closely matches full-precision performance. Under W8A8, peak memory falls by $2.2$--$3.1\times$ versus FP32, with up to $3.1\times$ speedup on real hardware. These results provide a principled and efficient approach to deploying feed-forward 3D reconstruction models in resource-constrained edges.

---


### 164. [Bri3D: Bridging the Object-Scene Gap in Single-Image 3D Generation via Scene-Anchor](https://arxiv.org/abs/2611.07961)

**<font color=#1a73e8>作者：</font>** Hongye Hou, Shuai Zhang, Hongjie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating compositional 3D scenes from a single image requires recovering detailed object geometry and coherent spatial arrangements. Existing object-to-scene methods, including SAM3D and MIDI, extend object generation through image-context reasoning or inter-instance modeling. Coordinating objects remains challenging with limited scene-level supervision. Directly extending object-centric generators to entire scenes can degrade geometry and fail to preserve instance scale, orientation, and pose. We propose Bri3D, a framework bridging scene-level structural reasoning and object-level generative priors through instance-aware voxel scene anchors. Bri3D predicts a color-coded scene scaffold encoding coarse object geometry and spatial arrangements. Each instance is extracted as a scene anchor and refined into a pose-preserving, prior-compatible voxel support, enabling a frozen object generator to synthesize detailed textured geometry in the anchor-defined spatial reference. This coarse-to-fine design separates scene organization from object-scale detail synthesis, focusing scene-level training on spatial organization and anchor refinement while reusing pretrained object priors. Experiments demonstrate improvements in scene layout, object geometry, visual quality, and generalization. Bri3D predicts scene layouts efficiently; full scene generation is faster than SceneGen and SAM3D.

---


### 165. [Tight Asymptotic Bounds on the Maximum Number of Linear Regions of Piecewise-Linear Kolmogorov--Arnold networks](https://arxiv.org/abs/2611.07973)

**<font color=#1a73e8>作者：</font>** Ye Su, Yong Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Schoots et al.~\citep{schoots2025relating} (AISTATS 2025) established a generally loose upper bound on the number of linear regions of continuous piecewise-linear (CPWL) Kolmogorov--Arnold networks (KANs), without providing a lower bound. We consider a $T$-layer network with width vector $\mathbf n=(n_0,\ldots,n_T)$, input dimension $n_0=d$, output width $n_T=1$, and at most $k\geq2$ affine segments per edge. Our matching upper and lower bounds determine the tight growth order $\Theta_{\mathbf n}(k^{\sum_{\ell=1}^{T}\rho_{\ell-1}})$ in $k$, where $\rho_{\ell-1}:=\min_{0\leq s\leq\ell-1}n_s$. When every hidden width is at least $d$, the tight order simplifies to $\Theta_{\mathbf n}(k^{dT})$. The upper bound of \citep{schoots2025relating} is $k^{\sum_{\ell=1}^{T}n_{\ell-1}n_\ell}$. Our upper bound improves it by a factor of $\Theta_{\mathbf n}\!\left(k^{\sum_{\ell=1}^{T}n_{\ell-1}n_\ell-\sum_{\ell=1}^{T}\rho_{\ell-1}} \right)$, with strict asymptotic improvement whenever a hidden layer has width greater than one. We further compare CPWL KANs with rectified linear unit (ReLU) networks using dense parameterizations with at most $\Lambda$ parameters per model and the same fixed nonlinear depth $T$. Counting trainable knot locations and optimizing the widths and $k$, we prove that the maximum region count of CPWL KANs divided by that of ReLU networks is $\Theta_{d,T}(\Lambda^{d\lfloor T/2\rfloor})$ as $\Lambda\to\infty$, yielding a polynomial advantage for KANs when $T\geq2$. These tight bounds characterize the attainable geometric complexity of CPWL KANs, providing a foundation for understanding their expressive power and guiding architectural design.

---


### 166. [Stealthy Malicious Interference Detection in UAV Formations: A Power-Domain Signaling Game Approach](https://arxiv.org/abs/2611.07977)

**<font color=#1a73e8>作者：</font>** Jianle Ba, Shaolong Guo, Yuntao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reliable intra-swarm communication is fundamental to cooperative sensing, control, and mission execution in unmanned aerial vehicle (UAV) swarms. In open low-altitude shared-spectrum environments, coexisting UAVs may cause benign interference through spectrum reuse and signal leakage, while jamming UAVs may deliberately degrade critical intra-swarm links. Since a jamming UAV can adjust its transmit power to disguise signal-to-interference-plus-noise ratio (SINR) degradation as link fluctuation in benign interference, stealthy jammer UAV detection remains a challenge. In this paper, we propose a novel belief-driven stealthy jammer UAV detection scheme from the perspective of Bayesian security game. To capture stealthy interference in shared-spectrum UAV swarms, the interfering UAV is modeled as a hidden benign or jamming type, whose transmit power strategy induces the SINR observed by the defender. The defender updates its posterior belief from the observed SINR and decides whether to maintain normal operation or trigger defensive power boosting. We characterize pure-strategy perfect Bayesian equilibrium (PBE) conditions under separating structures with distinguishable type and pooling structures with indistinguishable observations. Numerical results show that the proposed scheme improves the defender's expected utility compared to the conventional schemes.

---


### 167. [Reviving the Discarded High-Resolution Feature for Transformer-Based Tiny Object Detection](https://arxiv.org/abs/2611.07994)

**<font color=#1a73e8>作者：</font>** Zehao Wang, Si Wu, Guiping Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tiny object detection remains challenging because tiny instances occupy only a few pixels, and their fine-grained details are easily lost during feature downsampling. Although the highest-resolution feature preserves rich local details for tiny objects, DETR-like detectors often discard it due to its large computational cost, while directly reintroducing this feature also brings dense background noise. To address this problem, we propose ReDHF, a novel framework that Revives the Discarded High-resolution Feature for tiny object detection. ReDHF has three cooperative components. Cross-Scale Deformable Fusion (CSDF) first constructs a semantically enhanced highest-resolution feature and injects its fine-grained details into the shallow feature under a moderate cost. Ellipse-Guided Shallow Supervision (EGSS) then guides the enhanced feature to learn more reliable classification and localization priors by applying geometry-adaptive auxiliary supervision. Full-Scale Query Interaction (FSQI) further enables decoder queries to access both low-level details and high-level semantic information, allowing them to aggregate richer cues for tiny objects. Extensive experiments show that ReDHF consistently improves multiple baselines across different DETR variants and achieves state-of-the-art performance on the evaluated benchmarks. The best ReDHF variants surpass their baselines by +1.4 AP on AI-TOD-v2, +1.6 AP on VisDrone, and +1.5 AP on SODA-D, with especially notable gains on tiny and small objects.

---


### 168. [Towards Multiscale Molecular Representation Learning through Geometry-Based Fragmentation for Polymer Property Prediction](https://arxiv.org/abs/2611.07998)

**<font color=#1a73e8>作者：</font>** Makoto Takamoto, Chaitanya Sampara, Viktor Zaverkin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It is well established that molecular substructures can contribute unequally to chemical and physical properties, with specific motifs or side chains often playing dominant roles. Fragment-based representations have therefore emerged as an effective strategy for incorporating chemically meaningful inductive biases, as exemplified by molecular fingerprints and fragment-based attention mechanisms. However, many existing fragmentation-based machine learning methods rely on predefined chemical rules, which may yield suboptimal fragmentation for previously unseen or chemically unfamiliar structures and often overlook the importance of multiscale molecular representations. To address these limitations, we formulate molecular fragmentation as a radius-constrained optimization problem inspired by the k-center formulation, where the number of clusters is not fixed a priori but emerges from the specified radius, and propose a geometry-based fragmentation method that partitions arbitrary molecular or material structures using largely geometric information, without relying on predefined chemical fragmentation rules. The method provides flexible control over fragment size, enabling the construction of multiscale fragment representations for scale-adaptive modeling. Building on this framework, we develop a geometric fragment-based attention mechanism that integrates multiscale structural information and incorporate it into a multimodal machine learning model combining p-SMILES representations with three-dimensional (3D) conformational information. Experiments on a benchmark polymer dataset show that incorporating 3D conformational information improves prediction accuracy for several properties over models based exclusively on p-SMILES representations. Explainable artificial intelligence analyses further provide insights into the physical relevance of the learned representations.

---


### 169. [GTAFL: Addressing Test-Agnostic Long-Tailed Federated Learning in Medical Image](https://arxiv.org/abs/2611.08021)

**<font color=#1a73e8>作者：</font>** Guangyu Chen, Jingyun Zeng, Hui Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In healthcare, protecting patient privacy is crucial due to the sensitivity of medical data and its extensive accessibility. Federated Learning (FL) offers a decentralized and privacy-preserving training paradigm, making it an ideal solution for healthcare applications. A critical challenge in healthcare is that real-world medical data often exhibits long-tailed distributions in local and global views. Existing methods addressing long-tailed FL problem typically assume that the model will be evaluated on uniform test data distribution. However, practical test data in healthcare systems is often agnostic and unpredictable, leading to potential model failures in real-world scenarios. In this paper, we introduce a novel task termed Test-Agnostic Long-Tailed Federated Learning and propose GTAFL, a comprehensive framework to address this challenge. During the training stage, GTAFL employs adaptive re-sampling, expert classifier retraining, and self-supervised learning to correct biased classifiers and distorted feature spaces caused by long-tailed training distributions. During the inference stage, an ensemble mechanism combines retrained expert classifiers to handle test data with unknown distributions. Extensive experiments on CIFAR10 and two medical datasets manifest that our framework outperforms other state-of-the-art methods. The code is available at this https URL

---


### 170. [Reproducing Kernel (Quasi-)Banach Spaces with the $\ell^p$ Coefficient Norms](https://arxiv.org/abs/2611.08032)

**<font color=#1a73e8>作者：</font>** Tianfang Wang, Guohui Song, Haizhang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper advances the theory of reproducing kernel Banach spaces (RKBSs) by investigating the general $\ell^p$ regularization framework, with a particular focus on the non-convex regime $0<p<1$.
While our preceding work established the foundation for RKBSs with the $\ell^1$ norm, the pursuit of stronger sparsity---closer to the $\ell^0$ pseudo-norm---naturally motivates this exploration into $\ell^p$ quasi-norms.
For $0<p<1$, we construct reproducing kernel quasi-Banach spaces (RKQBSs) with $\ell^p$ quasi-norms and establish existence and sparsity results for interpolation and regularized learning under appropriate assumptions.
We characterize the linear and relaxed representer theorems in terms of a generalized Lebesgue constant and derive bounds under kernel decay, sample spacing, and stability assumptions.
For $p>1$, we construct RKBSs using a fixed countable dictionary, establish minimizer existence, and identify the optimal relaxed representer factor through an off-sample coefficient operator.
These results reveal fundamental differences between the regimes $0<p<1$, $p=1$, and $p>1$.
Numerical experiments compare the accuracy and sparsity of solutions for these three cases.

---


### 171. [Secure Formal Raising: Protecting the Development of AI through Executable Properties](https://arxiv.org/abs/2611.08042)

**<font color=#1a73e8>作者：</font>** Rolf Drechsler, Christina Plump  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model raising revisits Turing's developmental view of machine intelligence. Formal Raising (FR) has recently been proposed to complement this view with explicit behavioral properties. This paper extends that proposal to the security of the raising environment. Secure Formal Raising (SFR) models policy integrity, authorization, and confidential data flow using four-valued evidence that preserves unknown and inconsistent assessments. We prove six security invariants and show that they force admission to accept only confirmed evidence. A plain-C reference implementation satisfies the invariants in a bounded exhaustive exploration, which also exposes a confused-deputy gap for tool calls that a provenance requirement closes.

---


### 172. [Performance metrics in machine learning: a scenario-based guide from the confusion matrix to calibration, regression and uncertainty](https://arxiv.org/abs/2611.08048)

**<font color=#1a73e8>作者：</font>** Mehmet Baygin, Sengul Dogan, Turker Tuncer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Performance metrics can yield different conclusions from the same predictions. This methodological tutorial explains the effects of class prevalence, decision thresholds, aggregation rules and software conventions through controlled scenarios. Twenty-two confusion-matrix metrics are organized in a prevalence-coded map. Fifteen scenarios cover binary and multi-class classification, score discrimination, probability calibration, regression, uncertainty and consistency checks. Inputs are fixed in released files, and one factor is varied in each scenario. All 205 verification checks passed; 202 were independent and 3 were internal. An always-negative rule achieved an accuracy of 0.990 at a prevalence of 0.010, with balanced accuracy of 0.500. At fixed sensitivity and specificity, precision fell from 0.889 to 0.008 as prevalence fell from 0.5 to 0.001. Three probability variants shared a ROC-AUC of 0.825 but had calibration slopes of 2.08, 1.04 and 0.52. With 10 participants, participant-majority accuracy of 0.700 had a 95% interval of 0.348-0.933. Fold-averaged scores were falsely flagged as inconsistent under an inappropriate pooled-test-set model. A goal-based metric table and a reporting checklist are provided. The scenarios illustrate mechanisms and do not estimate their frequency in published studies. A literature audit and a real-data demonstration are specified as future protocols and were not executed.

---


### 173. [When Imperfect Automated Fact-Checking Backfires: Social Learning in the Presence of Misinformation](https://arxiv.org/abs/2611.08053)

**<font color=#1a73e8>作者：</font>** Zixuan Liu, Ming Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated fact-checking tools, cheap and fast but imperfect, are increasingly available on social platforms. We study when such tools can backfire in a sequential social learning model of misinformation. Agents observe an article's reliability and their predecessors' actions, which indicate whether they liked or disliked the article. They may also pay to fact-check it. We examine how welfare, defined as the probability of a correct cascade, changes when a free, error-prone automated tool supplements costly but perfectly accurate manual fact-checking. Two opposing effects arise. Broader use of fact-checking helps agents escape wrong cascades. At the same time, errors from the automated tool can mislead agents who would otherwise have verified the article perfectly, reducing the likelihood of correct cascades. We prove that adding the tool strictly lowers welfare for articles of intermediate reliability when truthful articles are not too informative and manual checking is sufficiently costly. Simulations show that the tool can help on either side of the intermediate range, and that it improves on manual-only checking on average only above a threshold accuracy.

---


### 174. [Optimal Competitive Ratios for Chasing Convex Functions with Quadratic Growth](https://arxiv.org/abs/2611.08078)

**<font color=#1a73e8>作者：</font>** Linzhe He, Sifan Yang, Wei Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chasing convex function has attracted much attention in recent years, which can be formulated as a game between a learner and an adversary. In each round, the adversary reveals a convex function, and the learner selects a decision and incurs a hitting cost and a movement cost for changing its decision. The performance of the learner is measured by the \emph{competitive ratio}, which compares its cumulative cost with that of an optimal offline decision sequence. For Euclidean movement, existing upper and lower bounds for $\kappa$-well-conditioned functions exhibit a polynomial gap. For squared Euclidean movement, dimension-free competitive guarantees have been established under quadratic growth, but the optimal competitive ratio remains unclear.
In this paper, we establish optimal dimension-free competitive ratios for convex function chasing under two types of movement costs. For Euclidean movement, we propose Clipped Proximal Descent (CPD), which combines a balanced proximal step with a clipped correction toward the current minimizer. CPD achieves an $O(\kappa^{1/3})$ competitive ratio for smooth convex functions satisfying quadratic growth, improving the previous $O(\sqrt{\kappa})$ upper bound and matching the existing $\Omega(\kappa^{1/3})$ lower bound. For squared Euclidean movement, we establish the exact optimal dimension-free competitive ratio for convex functions satisfying quadratic growth. Our result is based on a new tight competitive analysis of Regularized Online Balanced Descent (R-OBD) and a matching lower bound against randomized algorithms.

---


### 175. [TerraMesh-Masks: Open-Vocabulary Segmentation for Earth Observation](https://arxiv.org/abs/2611.08081)

**<font color=#1a73e8>作者：</font>** Benedikt Blumenstiel, Hugues Devimeux, Johannes Jakubik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary segmentation (OVS) enables models to segment a variety of concepts specified in natural language, removing the need for fixed label sets and fine-tuning. While recent OVS approaches have shown strong performance on natural images, they transfer poorly to Earth observation (EO) data due to differing semantics, scales, sensing modality, and geographic context. To date, large-scale EO-specific datasets and benchmarks for OVS remain scarce. We, therefore, introduce TerraMesh-Masks, a large-scale open-vocabulary segmentation dataset for EO, comprising 16 million binary masks aligned with nine million multimodal TerraMesh samples and annotated using OpenStreetMap and Overture-derived semantics. In addition, we provide an expert-reviewed evaluation set of 523 samples covering over 200 classes to enable robust evaluation. To demonstrate the impact of TerraMesh-Masks, we build an open-vocabulary version of TerraMind. Our results demonstrate significantly improved performance over general-purpose state-of-the-art models reaching 35.18% IoU versus 16.29% for this http URL and 11.33% for SAM-3. We release the dataset publicly under a permissive license at this https URL.

---


### 176. [Value or Attention: Investigating Layer-wise Relevance Propagation for Graph Attention Networks](https://arxiv.org/abs/2611.08088)

**<font color=#1a73e8>作者：</font>** Ken Schreiber, René P. Klausen, Sebastian Lapuschkin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Attention Networks (GATs) are increasingly used in domains where scientists need to read a model's reasoning, from medicine to materials science, yet the routing they learn remains opaque to most explainers. Layer-wise Relevance Propagation (LRP) follows the model's computation, but in an attention layer the relevance reaching a node is the sum of two mechanically different quantities: its content relevance through the value path and its routing relevance through the attention path. Existing rules either drop one or add them into a single number. We write a single product rule with free weights on the two factors that recovers current approaches as special cases. The value path measures what content a node supplied against a zero baseline; the attention path measures how the node shaped what was passed relative to its neighborhood, and its sign records whether the node's features moved the gating the way the prediction demanded. On a ground-truth classification task, we show that the same node receives negative, positive and near-zero relevance under three settings of the rule. The separated relevance maps yield a hypothesis about the model: it gains by not reading that node. We give reading rules for both paths and argue that they should be interpreted separately.

---


### 177. [Gradient Boosting for Efficient Rank Discovery in Tensor Network Kernel Machines](https://arxiv.org/abs/2611.08093)

**<font color=#1a73e8>作者：</font>** Albert Saiapin, Kim Batselier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensor network kernel machines (TNKMs) combine nonlinear features with low-rank tensor representations to model complex relationships efficiently. However, selecting an appropriate tensor rank remains challenging, as conventional rank-search methods require training multiple candidate models, increasing computational costs. In this work, we focus on a canonical polyadic (CP) tensor network parameterization and propose GB-CPKM, a gradient boosting framework that builds a higher-capacity predictor by sequentially adding fixed-rank learners. This approach provides a new perspective on rank selection by incrementally increasing model capacity, with ensemble size selected based on validation performance rather than through explicit rank search. Experiments on real-world regression benchmarks show that GB-CPKM trains up to 6x faster and uses up to 2x less peak memory than a conventional rank-selection method based on cross-validation, while achieving comparable predictive performance. These results highlight the potential of gradient boosting to improve the computational efficiency and scalability of tensor-network learning.

---


### 178. [PersonaAgent: Retrieval-Augmented Transaction Anomaly Scoring with Refreshable Multi-Entity Persona Memory](https://arxiv.org/abs/2611.08094)

**<font color=#1a73e8>作者：</font>** Zhengyu Fang, Liang Wang, Yingtong Dou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In large-scale payment networks, entities (card, merchant, etc.) and their interactions play a key role in transaction anomaly detection. However, transaction patterns between different entities usually change more frequently than the production model refresh schedule. Meanwhile, entity embedding tables suffer from high-cardinality and sparse interaction issues. To resolve the above challenges, we present PersonaAgent, an agentic transaction anomaly detection framework which represents the latest entity behavior signals as personas and saves them in a refreshable memory. Offline, a weekly scheduled batch job is used to extract the latest behavior signals and update them in the memory. At inference time, a lightweight adapter retrieves the corresponding entity behavior signals of each transaction from memory and uses them to augment the base anomaly classifier's scoring. Through comprehensive benchmarking with different anomaly detection models at Visa, PersonaAgent is able to score transactions efficiently (a 1,000-transaction CPU batch in 1-2 ms), lifting the PR-AUC by 0.65-6.58% and the production business metric by 8.93-14.24% relatively in deployment.

---


### 179. [National-scale mapping of tree species composition in Switzerland from high-resolution aerial imagery and multimodal data](https://arxiv.org/abs/2611.08095)

**<font color=#1a73e8>作者：</font>** Yixin Zhou, Luca Ferrari, Verena C. Griess 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tree-species composition shapes forest productivity and how forests respond to climate disturbances such as drought, windthrow and insect outbreaks. Yet most national forest maps assign each pixel a single dominant species and cannot show the share of accompanying species. We mapped the basal-area shares of ten main tree species and a residual Other class across Switzerland at 30 m resolution. A deep-learning model combining 0.1 m aerial RGB imagery, airborne laser scanning (ALS), annual AlphaEarth satellite embeddings, and climate variables was trained on basal-area observations from 3,992 Swiss National Forest Inventory (NFI) sites. In spatial cross-validation, the model reached a macro-$R^2$ of 0.485 across the 11 classes. On an independent forest-reserve dataset, the map reached a macro-$R^2$ of 0.552 for individual 30 m pixels and 0.733 for plots, and identified the dominant class in 73.2% of pixels and 81.1% of plots. The map shows maple and ash as widespread minor components that dominant-class maps omit. It also reproduces the elevational sequence from broadleaved lowland stands through spruce to larch and Arolla pine near the treeline. By resolving the species mixture within each 30 m pixel, the map complements field inventory statistics with spatially continuous information that can support forest monitoring, the management of mixed stands, and climate-adaptation planning across Switzerland.

---


### 180. [Towards Practical 20 kbps Generative Video Compression via Adaptive Tokenization and Entropy Modeling](https://arxiv.org/abs/2611.08099)

**<font color=#1a73e8>作者：</font>** Jiancheng Zhao, Jixiang Luo, Haibin Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video compression at ultra-low bitrates remains challenging due to the loss of perceptually important details under limited bit budgets. Recent generative video compression methods leverage pretrained video priors to improve perceptual quality and temporal coherence, but many follow a compress-then-generate paradigm, where generative priors are primarily exploited during reconstruction. Moreover, representations learned for generation and reconstruction are not inherently optimized for entropy coding.
In this work, we propose \method, which adapts pretrained video representations into compression-oriented representations while preserving their reconstruction capability. Specifically, we adapt the pretrained causal video VAE of MiniMax-H3 into a discrete video tokenizer and develop a small autoregressive entropy model that captures local and global token dependencies, with grouped prediction for parallel decoding. To further improve coding efficiency, we jointly optimize the tokenizer and entropy model using a differentiable rate surrogate, allowing rate gradients to adapt token assignments toward lower coding costs while preserving reconstruction quality. Experiments on UVG, MCL-JCV, and HEVC Class B demonstrate superior perceptual rate--distortion performance, achieving BD-LPIPS savings of 82.2\%--87.5\% and BD-DISTS savings of 78.3\%--85.0\% relative to GLC-Video.

---


### 181. [Cloudy Skies: Early Detection of Jamming Against Iridium LEO Satellite-IoT Links](https://arxiv.org/abs/2611.08118)

**<font color=#1a73e8>作者：</font>** Ingrid Huso, Giulia Fliescher, Savio Sciancalepore 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Low Earth Orbit (LEO) satellite-IoT systems increasingly provide connectivity to mobile assets in remote areas, which makes their resilience to radio-frequency jamming a growing concern. Timely jamming detection, i.e., before complete link failure, has been studied for terrestrial networks and Global Navigation Satellite Systems (GNSS), but it remains unclear whether these approaches are effective on LEO links, where propagation varies rapidly, the received signal is weak, and jamming should be detected from the messages that are still correctly received. This paper investigates the extent to which jamming of Iridium LEO satellite-IoT links can be detected from the physical layer of correctly decoded messages. To this aim, we collect and publicly release a real-world dataset of Iridium messages under 47 jamming conditions, spanning two propagation environments, static and mobile receivers, and different jammer distances, powers, and signal types. We use this dataset to analyze three one-class autoencoder-based anomaly detectors operating on physical-layer information and compare them against two signal-quality estimators commonly used as jamming indicators in GNSS-based applications. Our results show that detectability is governed by the rise of the receiver noise floor, through which jammer power, distance, and receiver mobility act. With 1000-sample chunks, i.e., 40 ms of received signal at 25,000 samples per second (about four correctly decoded messages), the autoencoders reach an AUC of at least 0.84 whenever a noise jammer raises the noise floor by at least 9 dB, whereas the $C/N_0$ and SNR estimators fail, since received messages, although correctly decoded, retain a high SNR under jamming. Therefore, timely jamming detection for LEO satellite-IoT links like Iridium should rely on physical-layer information beyond the signal-quality metrics adopted in the GNSS domain.

---


### 182. [ProtoGestalt: Interpretable Prototypes for Facial Phenotyping and Diagnosis of Rare Genetic Disorders](https://arxiv.org/abs/2611.08125)

**<font color=#1a73e8>作者：</font>** Ranga Baminiwatte, Alexander Hustinx, Fabio Hellmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rare genetic disorders are difficult to diagnose due to their diversity and overlapping clinical features. Facial morphology can provide diagnostic clues, yet most diagnostic models offer limited interpretability and are not designed to support broad screening for undiagnosed disease. We present ProtoGestalt, an interpretable prototype-based framework for facial phenotyping, rare-disease screening, and syndrome identification. The method extends prototype learning by constraining learned visual features to select facial regions, allowing predictions to be explained through localized and additive evidence. We assess ProtoGestalt's ability to distinguish syndromic from unaffected faces on multiple control datasets and class prevalence values. We further evaluate it's diagnostic performance on syndromes observed during training. The learned prototype-based representations provide significant separation between syndromic and case-matched control images and retain useful performance as the proportion of controls increases. The framework also demonstrates the ability to differentiate among syndromes. Although reasonably accurate specialized models for facial classification of rare disorders already exist, ProtoGestalt offers an interpretable alternative that links predictions to anatomically meaningful facial regions, potentially supporting clinical decision-making and the discovery of phenotype-gene associations.

---


### 183. [FreeOcc: Decoupling Ego-Motion for Efficient 4D Occupancy Forecasting via Continuous Flow Matching](https://arxiv.org/abs/2611.08128)

**<font color=#1a73e8>作者：</font>** Zeping Zhang, Zhuoya Zhao, Samy Metari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current 4D occupancy world models use heavy cross-attention or deep recurrence to disentangle ego-motion from scene dynamics. This requires significant computational capacity. However, this effort is largely redundant since the ego-vehicle's intended future motion is provided by the downstream motion planner. We present FreeOcc, a lightweight continuous-time world model that introduces explicit $SE(2)$ geometric decoupling into a conditional flow-matching framework. By mathematically factoring out self-motion, we create a purely dynamic feature space. This space supports attention-free temporal fusion and allows physics-constrained ODEs to operate strictly on residual agent kinematics. To maximize deployment efficiency, FreeOcc introduces an uncertainty-aware blending mechanism. This routes well-observed voxels to a single-pass decoder, reserving the ODE solver exclusively for ambiguous, high-uncertainty regions. Requiring only 28.3M parameters-roughly 40% of comparable models-our optimal ensemble mode (FreeOcc-E) runs at 27 FPS. On nuScenes, FreeOcc achieves state-of-the-art forecasting performance with a 0.47 m Near Field Chamfer Distance (NFCD) and 32.1% mIoU. Furthermore, the model transfers zero-shot to SemanticKITTI. It also proves highly robust, retaining 92.8% of its ideal mIoU under significant sensor packet loss and timestamp jitter.

---


### 184. [How Far Can Untrained Neural Networks Go in Anomaly Detection? From Tables to Pixels](https://arxiv.org/abs/2611.08136)

**<font color=#1a73e8>作者：</font>** Hyojun Yi, Geunyoung Kim, Hogeon Seo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection (AD) is often framed as a representation-learning problem, where strong performance is expected to require learned features or AD-specific optimization. However, this view can overlook the intrinsic separability of anomalies from normal references, even in the absence of learned representations. We therefore investigate how far untrained neural networks can go in anomaly detection. To this end, we propose PRISM, a framework combining fixed random nonlinear features with normal-reference Mahalanobis scoring for tabular detection and dense visual localization. Across 47 tabular datasets in ADBench, PRISM-T achieves the highest mean AUROC (86.4%) and the second-highest mean AUPRC (65.9%) among the compared methods. On MVTec AD and VisA, covering 27 visual categories, PRISM-V achieves mean image-level and pixel-level AUROCs of 90.4% and 96.4%, respectively. Notably, both models achieve these results without neural weight optimization or pretrained representations. A theoretical analysis further characterizes how nonlinear transformations affect the mean and covariance contributions to the Mahalanobis score gap, while empirical analyses examine the resulting score separability. These findings establish PRISM as both a competitive anomaly detector and a prior-to-learning baseline for assessing the added value of learned representations in anomaly detection.

---


### 185. [Fault-Guided Cross-Layer Prediction for Unsupervised Anomaly Detection](https://arxiv.org/abs/2611.08140)

**<font color=#1a73e8>作者：</font>** Tao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature reconstruction is widely used for unsupervised industrial anomaly detection in the single-class setting, where only normal images from one product category are available for training. We propose a single-class detector that asks what information one block can pass to another. We treat the depth of a frozen vision transformer as a sequence of discrete transitions. A directed predictor learns a block-to-block hidden-state transition pointwise over tokens. Adjacent-layer cosine similarity exposes four sharp fault lines in DINOv2 ViT-L, separating stable depth segments. The deepest blocks retain semantic context but lose local detail; a prediction from deep or shallow sources to sensitive targets therefore exposes the information that cannot be transported. The fault structure fixes the source and target roles, and the same rule transfers to ViT-B and RADIO-B. We use a bounded foreground prior calibrated solely on training images: it attenuates background evidence without also erasing defects outside the estimated foreground. Using one predictor architecture and a common training-only calibration protocol, image AUROC is 99.75 on MVTec-AD, 99.42 on VisA and 94.27 on Real-IAD. On Real-IAD the object-level AUROC is 96.26. At 256x256 pixel resolution, P-AUROC/P-AUPRO are 98.46/95.97 on MVTec-AD, 99.21/96.12 on VisA and 99.26/96.59 on Real-IAD.

---


### 186. [MCUFlowNet: Hardware-Aware Neural Architecture Search for Optical Flow on Microcontrollers](https://arxiv.org/abs/2611.08147)

**<font color=#1a73e8>作者：</font>** Enmin Lin, Jona Beysens  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense optical flow allows small drones to avoid obstacles. However, few dense optical flow networks are designed for microcontrollers (MCUs) with neural accelerators, whose on-chip SRAM limits the input resolution. We present PACE-NAS, a macro-to-micro neural architecture search framework that decouples memory from latency: a macro design fixes the backbone and its peak SRAM, and a micro design searches operators and depths to trade accuracy against compiler-estimated latency. We apply it to EdgeFlowNet on a Grove Vision AI V2 board (Ethos-U55), where profiling locates the peak SRAM at the full-resolution output head. Replacing transposed convolutions with bilinear upsampling and convolutions lowers the peak SRAM by 18%, and two lightweight context modules lower the endpoint error (EPE) without raising the peak. All searched subnets share this peak, so the search needs no memory constraint. We name the Pareto-optimal models MCUFlowNet; the fastest variant, MCUFlowNet-S, runs 1.76x faster than a retrained EdgeFlowNet at a 1.6% higher EPE and, in simulated forest flights at 2 m/s, reaches the goal without collision in 51.5% of trials, against 41.8%. PACE-NAS also applies to semantic segmentation, where a searched PIDNet-S variant runs 1.17x faster at similar accuracy. Code is available at this https URL.

---


### 187. [Detecting Weather Fronts from Satellite Observations: What Does Reanalysis Add?](https://arxiv.org/abs/2611.08148)

**<font color=#1a73e8>作者：</font>** Ioannis Dravilas, Miruna Stoicescu, Roope Tervo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weather fronts are transition regions between air masses with contrasting thermodynamic properties and are associated with mid-latitude precipitation and severe weather. We investigate machine learning (ML) methods for detecting weather fronts and quantify the contribution of reanalysis data to performance. We compare two configurations of the same ML model for pixel-wise frontal classification over the North Atlantic and Europe: (1) using only geostationary infrared satellite observations, and (2) additionally using 28 ERA5 reanalysis fields. The satellite-only model achieves a neighbourhood critical success index at a 150 km tolerance (CSI@150) of $0.402$, which lies within the range of agreement between analyses from different meteorological services. The satellite$+$ERA5 model achieves $0.575$, an improvement of $0.173$. Our analysis shows that low-level winds are the least predictable from the satellite representation ($R^2 = 0.23$, compared with $0.88$ for temperature), while removing winds or moisture causes the largest decreases in detection performance.

---


### 188. [Interpretable Multimodal MRI-Clinical Fusion for Functional Outcome Prediction After Acute Ischemic Stroke](https://arxiv.org/abs/2611.08154)

**<font color=#1a73e8>作者：</font>** Sina Raeisadigh, Henning Müller, Abderrahmane Hedjoudje  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study evaluates the added prognostic value of day-1 multimodal MRI for predicting three-month functional outcome after acute ischemic stroke (AIS). Sixty-six AIS patients with ADC, DWI, FLAIR, and clinical data were analyzed. Three-dimensional pretrained ResNet embeddings were extracted from each MRI modality, reduced using fold-isolated principal component analysis, and combined with structured clinical variables and ADC-derived lesion biomarkers. Linear support vector machines were evaluated using eight-fold stratified group cross-validation across MRI modality combinations. Clinical-only modeling achieved strong performance (AUC = $0.899 \pm 0.151$), while MRI-only models showed limited discrimination (AUC $\approx$ $0.67$-$0.73$). Among multimodal configurations, FLAIR-clinical fusion achieved the highest mean cross-validated performance (AUC = $0.948 \pm 0.061$), followed by ADC-clinical fusion (AUC = $0.941 \pm 0.094$). Full ADC-DWI-FLAIR fusion did not consistently outperform single-modality clinical fusion. Feature-importance analysis identified age, NIHSS subscores, ADC lesion burden, and learned FLAIR representations as key contributors, while qualitative FLAIR activation maps showed responses over lesion-like regions. These findings suggest that compact day-1 FLAIR and ADC representations provide complementary prognostic information beyond clinical variables and support interpretable, data-efficient outcome prediction in AIS.

---


### 189. [Improving Context-Shift Robustness of Convolutional Networks via Context-Regularized Cross-Entropy](https://arxiv.org/abs/2611.08157)

**<font color=#1a73e8>作者：</font>** Jinen Setpal, Chaoyue Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image classification models often encounter objects in diverse and unpredictable contexts at test time, which may differ substantially from those seen during training. This phenomenon, termed context shift, exposes a key fragility in neural networks: when models rely on non-causal contextual cues for prediction, shifts in context can lead to significant performance degradation. In this paper, we propose a novel training framework to improve the robustness of convolutional neural networks under context shift. Our approach leverages spatial feature attribution to guide models toward making predictions that rely less on contextual regions and more on object-relevant features. As a first step, recognizing a theoretical limitation of existing feature attribution methods we introduce a new variant, ContrastiveCAMs, which produces more faithful attribution maps of model predictions. Building on ContrastiveCAMs, we further propose Context-Regularized Cross-Entropy (CR-CE), a modification of the standard cross-entropy loss that regularizes the model's attention by suppressing the influence of contextual regions, thereby improving robustness to context shift. We evaluate the effectiveness of our approach on several medium-to-large scale datasets (Waterbirds, Spawrious, ImageNet/ImageNet-BG, Hard-ImageNet), and report consistent improvements in context-shift robustness.

---


### 190. [Reflective Nature Experiences in Virtual Reality](https://arxiv.org/abs/2611.08167)

**<font color=#1a73e8>作者：</font>** Shiva Ghasemi, Maddie Oehler, Annie Xenakis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents the design and evaluation of an accessible virtual reality (VR) nature experience developed to promote mindfulness, reduce stress, and support emotional well-being. The system immerses users in a calming natural environment through realistic landscapes, ambient soundscapes, guided breathing exercises, and interactive checkpoints that encourage reflection. Accessibility was a central design consideration, particularly for users with diverse physical and sensory abilities or limited access to natural environments and traditional mindfulness resources. A pilot study with 10 participants indicated that the experience could support relaxation and emotional well-being. Participants also reported greater immersion with continuous movement than with teleportation, highlighting the importance of intuitive locomotion in designing inclusive, nature-based VR experiences for mindfulness and stress reduction.

---


### 191. [The Promise of Strategic Agentic Scambaiting](https://arxiv.org/abs/2611.08170)

**<font color=#1a73e8>作者：</font>** Abhishek Satyam, Hossein Siadati, Haadi Jafarian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Scammers have increasingly adopted AI-driven capabilities, evolving from automated message generation to fully agentic conversational systems that scale operations and maximize the exploitation of fraudulent resources before detection and takedown. In parallel, agentic scambaiting has emerged as a defensive approach in which autonomous agents impersonate potential victims and engage scammers in sustained interactions to extract actionable threat intelligence, such as mule bank accounts and cryptocurrency wallet addresses, that can be reported to disrupt fraudulent infrastructures. Together, these developments transform online fraud into an adversarial socio-technical ecosystem in which autonomous scamming and scambaiting agents engage in deceptive interactions while competing over the discovery, preservation, and exploitation of one another's resources. A fundamental and largely unexplored question is how defensive scambaiting can remain effective in an agent-to-agent environment, and under what conditions either side gains a strategic advantage. In this paper, we present a formal model of agent-to-agent fraud interactions that captures the strategic decision spaces available to both attackers and defenders. Using this framework, we analyze the dynamics of engagement, resource consumption, belief adaptation, and disruption outcomes. We find that scammer profitability turns negative once baiting-agent prevalence exceeds certain thresholds, and that when both sides improve at the same pace, defender investment in mimicry quality outpaces equivalent gains in scammer detection capability, so the arms race favors the defender under our baseline parameters. Our model and findings provide insights into the stability, scalability, and long-term effectiveness of autonomous defensive agents in an evolving AI-mediated fraud landscape.

---


### 192. [BabyTheorist: A Benchmark for Learning to Theorize the World from Observation Alone](https://arxiv.org/abs/2611.08177)

**<font color=#1a73e8>作者：</font>** Doojin Baek, Junyeob Baek, Mingyu Jo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How would we know whether a machine truly understands the world? We argue that one key capability is \textit{observational theory learning}: acquiring reusable theories from pure observations and applying them to new situations. Current visual reasoning benchmarks focus primarily on the latter, presenting each task as a few-shot puzzle grouped by a common rule. We introduce BabyTheorist, a benchmark for controlled training and evaluation of observational theory learning. BabyTheorist generates continual streams of before-after visual observations from hidden compositional programs; during training, learners see only the resulting transitions, with no program labels, task identities, or support sets. To support theory learning and evaluation, BabyTheorist controls the program language, a curriculum over program complexity, recurring frequent subprograms, and a continual train-test protocol with level skipping. Seven representative baselines plateau well below ceiling, with the gap widening as the curriculum advances---evidence that BabyTheorist isolates a capability current program-learning approaches do not yet address.

---


### 193. [Knowing When to Teach: Learning from Teachable Prefixes in Multilingual Reasoning Distillation](https://arxiv.org/abs/2611.08179)

**<font color=#1a73e8>作者：</font>** Jaewon Cho, Minseo Yoon, Jinyoung Park 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-Policy Self-Distillation (OPSD) improves reasoning by training a student on its own reasoning, using the same model conditioned on reference solutions as a teacher. Applying OPSD to multilingual reasoning requires the teacher to provide useful feedback across languages, even when the student makes mistakes in intermediate steps. We observe a phenomenon we call Teacher Drift: as these mistakes accumulate, the teacher may follow the student's incorrect steps instead of correcting them. Our analysis shows that this shift tends to occur earlier in lower-resource languages. To account for these differences across languages, we propose Teachable On-Policy Self-Distillation (TOPSD), which determines where and whether teacher supervision should be applied to each reasoning trajectory. TOPSD uses teacher-student likelihood to estimate where drift begins and select a prefix for supervision. It then verifies whether the teacher can recover the correct answer from that prefix, applying distillation only to prefixes that pass verification. Experiments on multilingual mathematical reasoning across ten languages and three model scales show that TOPSD consistently outperforms conventional OPSD, particularly in low- and medium-resource languages.

---


### 194. [BUMP: Brief Unexpected Mid-Interpolation Peak](https://arxiv.org/abs/2611.08182)

**<font color=#1a73e8>作者：</font>** Melinda Flóra Kiss, Márton Muntag, Adrián Csiszárik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We identify an intriguing phenomenon when linearly interpolating between permutation-aligned neural networks: test accuracy briefly improves near the interpolation endpoints before dropping toward the midpoint, which we term BUMP (Brief Unexpected Mid-interpolation Peak). We observe that BUMP appears consistently across datasets, architectures, training regimes, and remains robust under substantial perturbations such as early checkpoints and extreme pruning. Moreover, controlled ablations suggest that it cannot be attributed to trivial regularization effects. While similar near-endpoint gains are visible in prior interpolation plots, they have not been explicitly documented or systematically and thoroughly analyzed. Leveraging this effect, we propose a simple, novel ensembling scheme: weight-prediction mixed ensembling that combines weight mixing with prediction-space mixing. Across our experiments, the resulting ensembling method consistently outperforms standard logit ensembling in test accuracy and yields improved calibration trade-off, highlighting complementary benefits of weight- and prediction-space mixing.

---


### 195. [Zirah: A Post-Quantum True Random Number Generator Hardware Signer With an Avalanche Noise](https://arxiv.org/abs/2611.08200)

**<font color=#1a73e8>作者：</font>** Muhammad Shaheer Bin Junaid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zirah is a hardware signer built around an STM32F407 microcontroller, and its purpose is to find out, on inexpensive hardware, where a post-quantum signing key is exposed and what actually protects it. The device draws every random bit from a reverse-biased 2N3904 junction in avalanche breakdown, amplified by an LM358 and screened by SP 800-90B health tests, computes ML-DSA-65 (FIPS 204, hedged) on the STM32 with two-share arithmetic masking of the secret-key multiplications, and adds ECDSA P-256 from an ATECC608 secure element over the same digest, once a person has matched an eight-digit digest prefix on its OLED with the PC and pressed a button. A desktop application and a command-line tool drive the board and verify its output, and because only a 32-byte manifest digest reaches the device, it signs files of any type and size, returning signed copies for PDF, Office Open XML, ZIP, PNG and JPEG files and detached records for every other format. NIST's SP 800-90B tool rejected the IID assumption for 1,000,000 raw samples and assessed 6.898 bits of min-entropy per byte on the non-IID track, against the 1 bit the firmware credits, while spectral lines near 116 Hz that hold about 5 % of the variance remain unexplained. At 168 MHz the masked signature took a median of 157 ms over 20 runs and a complete signing operation under 0.8 s, and the signer matched the pq-crystals reference in 1,976 checks natively and on an emulated Cortex-M4. The ATECC608 can neither store the 4,032-byte ML-DSA-65 key nor compute with it, so that key sits in ordinary flash behind readout protection, and on an earlier board, before that protection was enabled, a debugger copied it out and the copy produced a valid ML-DSA-65 signature without the device, although the leakage results come from an instruction-level emulator and nothing here is certified.

---


### 196. [Beyond Quadratic Attention: Separable Gaussian Operators for ODE Vision Transformers](https://arxiv.org/abs/2611.08236)

**<font color=#1a73e8>作者：</font>** Carlos Boned Riera, David Romero Sanchez, Oriol Ramos Terrades  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-attention carries a quadratic cost in token count, which limits how far Vision Transformers can scale with input resolution. We introduce SSoG, a separable sum-of-Gaussians spatial operator that replaces dense self-attention with a learned mixture of axis-factorized Gaussian kernels, reducing the per-layer cost from $\mathcal{O}(N^2)$ to subquadratic in $N$. Unlike dot-product self-attention, whose Lipschitz constant is unbounded outside a compact input domain, SSoG with fixed kernels is globally Lipschitz continuous, which, via the Picard--Lindelöf theorem, guarantees that the continuous-depth variant has a unique solution on the whole integration interval, a global guarantee that dense-attention counterparts lack in general. On CIFAR-100 at $224\times224$, in a matched discrete-Transformer setting and in the continuous setting, SSoG improves Top-1 accuracy by 2.2--4.1 points across three model widths while using 8.8--16.6\% fewer parameters, with depth and training recipe held fixed. In a looped-Transformer setting, SSoG improves Top-1 accuracy by 5.4--8.1 points. We further probe inference-time scaling by evaluating on inputs up to $1024\times1024$ at matched batch size: in the continuous-depth (Neural ODE) architecture, SSoG reaches up to 154\% higher throughput and over 60\% lower peak memory than dense attention, with the gap widening as resolution grows, consistent with the difference in asymptotic cost. In the discrete and looped settings, SSoG also achieves over 30\% higher throughput than dense attention at this resolution. Together, these results establish SSoG as a practical, parameter-efficient, and theoretically grounded alternative to dense attention across discrete, weight-shared, and continuous-depth Transformer variants.

---


### 197. [FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning](https://arxiv.org/abs/2611.08240)

**<font color=#1a73e8>作者：</font>** Haitao Lin, Minsi Ren, Yang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a standard post-training method for diffusion models, but most RL objectives roll out the current policy at every iteration, and with a many-step sampler these rollouts typically dominate the cost of training. Few-step models cut this cost, yet they model an average velocity over an interval, whereas existing RL objectives are built for an instantaneous velocity with a many-step sampler. We adapt RL objectives to few-step models systematically in three phases, namely a transformation, a decomposition and an adaptation. The transformation to $x$-space expresses each objective we consider through a common policy prediction, at the clean end by default and at an explicitly marked level for transition or flow-map objectives, so that objectives stated over densities, velocities or rewards become comparable. The decomposition writes the gradient of each of these objectives as the sum of a self-regression toward a reference and a reward augmentation, so that a method reduces, at the gradient level, to a choice of anchors and weights. The adaptation computes each anchor from a few-step model at the end of its transport or along its tangent, with the instantaneous velocity recovered from the network itself or from an auxiliary network. This yields few-step versions of FlowGRPO, AWM, DiffusionNFT, DiffusionOPSD and ReFL in one modular codebase. In our experiments, reward-gradient-based methods are the most effective when the reward is differentiable and its gradient is affordable; otherwise DiffusionNFT-style methods generally reach high rewards in relatively few iterations despite a sometimes higher per-iteration cost. Extra inference steps show no systematic aggregate benefit in our experiments, although selected outputs visibly improve with two to four times as many sampling steps as in training.

---


### 198. [Value-oriented policy distillation for interpretable wind farm power control](https://arxiv.org/abs/2611.08245)

**<font color=#1a73e8>作者：</font>** Max Bruninx, Timothy Verstraeten, Jan Decuyper 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wind farm power control can help the system maintain balance and avoid blackouts. In Europe, this can be achieved through implicit balancing, where a wind farm adjusts its power setpoint in anticipation of the imbalance price using information published by the Transmission System Operator. Thereby, the wind farm helps restore system balance while also reducing its own imbalance costs resulting from forecast errors. However, implicit balancing is a challenging problem since the settlement price is unknown in advance and can be impacted by the pursued control strategy. Reinforcement learning methods could help to solve this problem, but lack the interpretability needed to be deployed on real wind farms. Therefore, we propose a policy distillation framework using explainable boosting machines (EBMs), a variant of generalized additive models, to obtain a transparent control policy. To increase the value captured by the EBM model, we introduce a value-oriented perspective to policy distillation inspired by research in the field of energy forecasting. Furthermore, we suggest to include expert knowledge during model design, such that the control strategy is also justifiable to stakeholders. Using real data of the Belgian grid and an offshore wind farm, we find that our value-oriented and expert-based controller can reduce imbalance costs by 82%, while outperforming a price threshold controller as well as a policy distillation baseline using decision trees.

---


### 199. [Geometric Relevance Is Not Sufficient: Evaluating Focused Post-Training Supervision in Diffusion Docking](https://arxiv.org/abs/2611.08249)

**<font color=#1a73e8>作者：</font>** Michael Brown, Maryam Rahimimovassagh, Mehdi Yazdani-Jahromi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based molecular docking requires learning a corrective score field across a broad corruption distribution, yet individual pose errors can differ substantially in their structural consequences. This creates a post-training conflict between preserving broad score-field coverage and concentrating supervision on corrections that appear more relevant to docking geometry. Using DiffDock, a fixed-budget study compares broad continuation with torsional supervision focused on Cartesian consequence or conditional target consistency, and with a broad/focused mixture. Evaluation separates fixed score fidelity, generated-pose quality, best-of-10 sampling capacity, and confidence-selected Top-1 docking performance. At <5 Angstrom, broad continuation had the highest mean Top-1 success among trained policies, and focused or mixed supervision showed no consistent advantage under the tested budget. The starting model had better fixed score fidelity, whereas the evaluated broad-continuation model had higher mean Top-1 success with the same aggregate best-of-10 recovery. Focusing supervision on structurally consequential or more consistently specified corrections did not consistently improve returned-pose success over broad continuation.

---


### 200. [Nowcasting of Tropical Cyclone Wind Fields and Intensity from Geostationary Imagery](https://arxiv.org/abs/2611.08255)

**<font color=#1a73e8>作者：</font>** Simon Donike, Pritthijit Nath, Cristina Radin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-resolution tropical cyclone surface wind speeds derived from synthetic aperture radar (SAR) observations can support storm structure and intensity modelling, but remain spatially and temporally sparse and unavailable near-real-time. Geostationary satellites capture cloud tops continuously in space and time, but do not directly resolve surface winds. Here, we present simple neural networks to predict 2D wind fields and storm-scale intensity metrics from geostationary imagery. Through a series of ablation studies, we find that joint prediction of 2D fields and scalar metrics from the model latent space improves the retrieval of the (radius of) maximum wind, especially for rapid intensification events.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-237](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
