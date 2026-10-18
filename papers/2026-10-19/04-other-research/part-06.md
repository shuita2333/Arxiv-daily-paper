# 📦 其他研究 | 2026年10月19日

> 本类共 **278** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-278**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-278**

---

### 251. [FutureLift: Lifting Trajectory Proposals into Bidirectional Future Graphs for Motion Forecasting](https://arxiv.org/abs/2610.22215)

**<font color=#1a73e8>作者：</font>** Daniel Grimm, J. Marius Zöllner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate motion prediction is critical for safe autonomous driving, yet even strong forecasters leave residual errors in their multimodal proposals. Existing refiners compress complete proposals or update their segments sequentially, preventing the full proposed future from serving as explicit relational context for correction. We introduce FutureLift, a backbone-agnostic refiner that represents each multimodal proposal as a heterogeneous future graph, with spatially grounded temporal nodes connected to agent histories, map elements, alternative modes, and, for joint prediction, other agents future trajectories. Bidirectional temporal edges allow later evidence to revise earlier segments in a single pass, and the updated nodes predict residual coordinate and confidence corrections. Requiring only proposals, scores, and scene context, FutureLift provides a common refinement interface for structurally different forecasting backbones. On Argoverse2 and the Waymo Open Motion Dataset, it consistently improves frozen proposals and outperforms native and specialized refiners across marginal and joint forecasting. On the WOMD motion-prediction leaderboard, FutureLift ranks first in minADE (0.5049m) and minFDE (0.9942m) among the compared standard-input methods, without LiDAR or ensembling, while achieving a competitive 0.4874 Soft mAP.

---


### 252. [How Much Physics Can Vision Learn from Audio? Probing and Distilling Damping Structure](https://arxiv.org/abs/2610.22221)

**<font color=#1a73e8>作者：</font>** Zainab Afolabi, Vadim Selyutin, Zhao Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical understanding is crucial for decision making, yet vision models struggle to infer properties such as damping that govern how materials behave. Audio encodes such properties directly, because an object's acoustic response to impact reveals its damping through measurable decay. We probe frozen encoders for the quality factor $Q$, a dimensionless measure of how many oscillations an object completes before its ring dies away, and report how well each embedding orders impacts by $Q$ using the Spearman rank correlation $\rho$, for which $\rho=1$ is a perfect ordering and $\rho=0$ an unrelated one. Audio embeddings reach $\rho=0.73$ and retain most of that advantage on materials withheld from training, while a single video frame taken at the moment of impact, encoded by CLIP, supports only $\rho=0.28$. Having established where the signal lives, we ask how much of that gap vision can recover. We distill a frozen audio teacher into a frozen CLIP backbone through a trained projection head and find that this recovers a useful fraction of the audio advantage. Because pooled correlations on this task are dominated in practice by category identity, we also evaluate under a leave-one-material-out protocol in which the held-out material is withheld from the projection head as well as the probe. Distillation with a four-frame input improves the correlation there from 0.234 to 0.338 (+0.053 over the matched four-frame baseline, 14 of 17 materials), a gain that no category-level strategy can produce. Widening the visual input to four frames spanning the impact supplies half of that improvement at no acoustic cost, which indicates that part of what a single frame misses is visible dynamics.

---


### 253. [Query-Efficient Rejection Sampling for Parallel Masked Diffusion](https://arxiv.org/abs/2610.22238)

**<font color=#1a73e8>作者：</font>** Shiyuan Zhang, Xuheng Li, Qiwei Di 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models (MDMs) accelerate generation by unmasking multiple tokens in parallel, but sampling these tokens independently ignores their correlations and biases the output. Anari et al. (2026) corrected this bias with rejection sampling, decomposing the log acceptance probability into a sum of token-level terms, but the evaluation requires one score query per unmasked token. We propose the Single-Increment Rejection Sampler (SIRS), which provides an estimate of the log acceptance probability from a single randomly sampled increment at the cost of one query. SIRS then converts a Poisson number of clipped estimates into accept/reject decisions through a Bernoulli factory adapted from Chen et al. (2026). Since each query returns the conditionals of all remaining tokens in the block, we further Rao-Blackwellize each increment by averaging over these tokens at no extra cost, thereby reducing clipping. We show that the KL-divergence between the data distribution and the SIRS output is bounded by a clipping term plus the model's training error. With exact scores, parallel decoding pays the full within-block dependence, whereas SIRS pays only the part beyond the clipping range.

---


### 254. [Shortcut Sensitivity in Agent-Safety Evaluations](https://arxiv.org/abs/2610.22243)

**<font color=#1a73e8>作者：</font>** Hasan Demirkiran, Jens Ernstberger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents take actions through tools. Some actions are sensitive, so guards that supervise them must themselves be evaluated reliably. Yet the data used to evaluate a guard can include cues that make labels predictable without measuring the intended safety construct, and those cues can also influence guard decisions. We introduce a three-level shortcut-auditing framework and audit completed LinuxArena trajectories and two TS-Bench-derived step datasets. We distinguish label predictability, observational guard association, and paired decision sensitivity. In LinuxArena, shorter average shell commands strongly predict trajectory labels. In AgentDojo-Traj, exact-tool lookup falls from F_1=.901 with mixed-domain folds to .495 under domain holdout. In AgentHarm-Traj, released TS-Guard F_1 falls from .902 under row weighting to .719 with equal interaction weighting, while balanced accuracy rises. We then test the strongest safe-row marker association in a seven-configuration screen on a frozen 64-step AgentDojo-Traj cohort using repeated, interleaved Haiku calls. Rewriting the <INFORMATION> marker lowers blocking by 8.33 percentage points, while opaque tool aliases raise it by 11.46 points. All unsafe calls remain blocked; the changes concern false positives against inherited labels. Both effects remain nonzero after subtracting the formatting-placebo effect, with exploratory 95% ranges excluding zero. The same edits also change measured accuracy against inherited labels. This provides direct evidence that benchmark representation can materially change a guard's decisions and measured evaluation performance. The Haiku-sized effects do not reproduce in Luna or deterministic Q8 TS-Guard. We recommend domain group holdouts, evaluation-unit metrics, and placebo-controlled paired interventions.

---


### 255. [Explore Once, Evaluate Many: Multiple Policy Evaluation for Stochastic Linear Bandits](https://arxiv.org/abs/2610.22252)

**<font color=#1a73e8>作者：</font>** Spyros Dragazis, Yilei Chen, Aldo Pacchiano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how to evaluate $K$ target policies simultaneously in stochastic contextual bandits with linear reward structure. Given a known $d$-dimensional feature map and reward-free access to policy queries, we propose PRISMA (Policy evaluation through Regularized Information Sharing and Mixture Allocation), an algorithm that estimates every target policy's value to accuracy $\varepsilon$ with probability at least $1-\delta$. The algorithm uses $\widetilde{\mathcal{O}}\!\left( \frac{(L^2S^2+\beta^2)(1\vee\rho^\star)}{\varepsilon^2} \cdot \log(K) \right)$ context draws and reward observations, where $\rho^\star\le d$ is an instance-dependent measure of the difficulty of designing a shared sampling distribution. Here, $L$, $S$, and $\beta$ bound the feature norm, reward parameter norm, and reward noise, respectively, and the suppressed factors are logarithmic in $K$, $d$, and $1/\delta$. Our method combines reward-free planning, a regularized sampling design, and a single ridge regression estimator shared across all target policies. An adaptive doubling procedure selects the regularization scale without knowledge of $\rho^\star$. The guarantees require no numerical lower bound on second-moment eigenvalues and have no explicit dependence on the cardinalities of the context and action spaces. Policy-query costs are accounted for separately, with $K$ queries per shared planning context.

---


### 256. [FPG-Seg: Annotation-free Retinal Vessel Topology Segmentation](https://arxiv.org/abs/2610.22259)

**<font color=#1a73e8>作者：</font>** James Willoughby, Irina Voiculescu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the art approaches to retinal vessel segmentation typically require extensive annotations, a highly time-consuming process, reliant on clinical expertise. We present FPG-Seg, an annotation-free pipeline for retinal vessel segmentation combining classical vesselness filtering, Bayesian deep learning and topology-aware graph reconstruction to segment retinal vessel topology without manual labels. Tested across four widely used benchmark datasets for retinal vessel segmentation, FPG-Seg attains a clDice of $0.74{-}0.78$, representing $86{-}98\%$ of the performance of an equivalent fully-supervised baseline, despite using no manual annotations for training or hyperparameter tuning. As part of this work, we also provide, to our knowledge, the first performance benchmark of an annotation-free vessel segmentation method on FIVES.

---


### 257. [Topology-Inspired Fine-Tuning for Wind-Field Super-Resolution](https://arxiv.org/abs/2610.22262)

**<font color=#1a73e8>作者：</font>** Arjun Dadhwal, Brian Summa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific super-resolution (SR) models are typically optimized with pointwise reconstruction losses, yet scientific interpretation often hinges on extrema, connected regions, and multiscale scalar structure. We characterize this tension with pretrained CNN and GAN wind-field SR models. Pointwise metrics, bottleneck persistence-diagram (PD) distance, and merge-tree (MT) distance favor the CNN, whereas order-2 Wasserstein PD distances favor the sharper GAN, so even different distances on the same topological descriptor reward different properties. Motivated by this disagreement, we fine-tune the pretrained CNN with differentiable topology-inspired auxiliary losses on scalar speed, gradient magnitude, soft high-speed level sets, and local maxima, and with fixed-pair supervision, which constrains predicted values and persistence at ground-truth persistence-pair endpoints located offline with the Topology ToolKit. A loss study of 16 fine-tuning configurations, each compared with a matched standard fine-tuning control that uses only the original reconstruction loss, on a fixed 168-field benchmark (with topology evaluated on a fixed 160 by 160 subregion of each field), shows that, among the scalar-field losses, gradient supervision provides the strongest PD improvement but does not improve mean MT distance, whereas fixed-pair supervision gives the largest and most consistent joint improvement in PD and MT distances. The final objective combines these two signals. Relative to the pretrained CNN, it lowers mean bottleneck, $W_{2,\infty}$, and $W_{2,2}$ distances by 31%, 25%, and 27% (and by 32-35% relative to the control, which on its own worsens all three), lowers all three on 150 of 168 fields, and gains 1.30 dB PSNR, about half the gain of standard fine-tuning. Mean MT distance also improves, but on only 91 of those 150 fields, indicating that PD and MT capture complementary structure.

---


### 258. [Beyond Pairwise Repulsion: Collective Diversity via Determinant Maximization in Diffusion Sampling](https://arxiv.org/abs/2610.22267)

**<font color=#1a73e8>作者：</font>** Kwanyoung Lee, SeungJu Cha, Yebin Ahn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Strong guidance in text-to-image (T2I) diffusion models concentrates sampling toward high-density modes of the conditional distribution, collapsing independently sampled noise vectors onto nearly identical visual prototypes. This limits utility for tasks that demand distributional breadth, most critically synthetic data augmentation. Diversity, however, is a collective property of the whole batch: a set can preserve every pairwise distance yet still collapse onto a low-dimensional subspace. Existing sum-of-pairwise noise-optimization and repulsion objectives respond only weakly to this higher-order failure. We propose DetNO (Determinant Noise Optimization), which formulates diverse generation as RKHS volume maximization on the initial noise, maximizing the log-determinant of an RBF Gram matrix over one-step Tweedie predictions. This set-level functional equals the squared batch volume; its repulsion is strongest when the batch is most collapsed and self-attenuates as diversity is achieved. An anchor-based fidelity term keeps the optimized noises near plausible regions, and Lagrangian relaxation gives a two-term objective with a single hyperparameter $\lambda$ governing the diversity-quality trade-off, without training or sampler modification. Across three backbones (SD1.5, SDXL, SD3), DetNO achieves leading intra-batch diversity in VendiScore and Mean Self-Similarity, and a downstream few-shot classification experiment confirms that broader mode coverage brings statistically significant accuracy gains for synthetic data augmentation in the low-shot regime. Fixing the pipeline and varying only the batch objective, both RBF-based aggregators outperform InfoNCE, and the log-determinant attains the best downstream accuracy on both benchmarks. Its diversity advantage over InfoNCE widens as the batch grows. Code is available at this https URL.

---


### 259. [Unsupervised Clustering of Public Transport Vehicles Using Deep Morphological Features and Color Histograms](https://arxiv.org/abs/2610.22270)

**<font color=#1a73e8>作者：</font>** Juan Irving Vasquez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surveillance cameras along urban roads produce large volumes of unlabeled video that could support the monitoring of public transport, but grouping the observed vehicles into meaningful categories without manual annotation remains challenging, since buses from different routes often share the same body structure and differ mainly in their color schemes. This study presents an unsupervised clustering methodology for public transport vehicles that combines morphological features extracted with a frozen DINOv2 Vision Transformer and handcrafted HSV color histograms through weighted early fusion, followed by UMAP projection and K-Means clustering. The method was evaluated on 7,972 bus images extracted from about 1,460 hours of video of an arterial road in Mexico City, with the goal of isolating the buses of the city's public bus network (RTP) without supervision. With a fusion of 65\% morphological and 35\% color features, the pipeline produced 14 clusters that separate distinct routes and vehicle types, and it increased the precision of the target cluster with respect to morphological features alone. These results show that color complements self-supervised features for route-level clustering, provided that it does not dominate the representation.

---


### 260. [Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Legal Guidelines](https://arxiv.org/abs/2610.22277)

**<font color=#1a73e8>作者：</font>** Florian Lercher, Karan Mahesh, Yujun Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> When robots are deployed in the real-world, they must interact with other agents and accomplish their own goals while adhering to legal constraints. These potentially conflicting objectives are often only partially prioritized, making scalarized objectives or fully specified hierarchies unsuitable. We present a framework for multi-agent motion planning under legal requirements based on games with partially ordered preferences (posetal games). Scenario-independent legal guidelines order abstract legal concerns, from which we automatically derive agent preferences and a legal game for any concrete scenario. Agents may refine their legal preferences with private objectives, and regulators may refine the guideline as laws evolve. We prove that such customizations can only remove equilibria and thus preserve legality. To coordinate agents without explicitly communicating private preferences, we introduce belief play, which provably recovers the true equilibria from conservative local games, and a distributed iterative best-response protocol requiring less information. We apply the framework to maritime navigation, systematically lifting pairwise traffic rules to multi-vessel encounters. On seven encounters with up to four vessels, every rule violation of the committed equilibria is certified as forced by the legal hierarchy or unsatisfiable, and defectors are identified from public information in all tested cases. These results indicate that guideline-based posetal games offer an auditable route from partially specified laws to multi-agent motion planning.

---


### 261. [Learning Rational Strategies for Temporal Objectives in Multi-Agent Systems](https://arxiv.org/abs/2610.22287)

**<font color=#1a73e8>作者：</font>** Omar Adalat, Edwin Hamel-De le Court, Francesco Belardinelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study rational synthesis for stochastic multi-agent systems with unknown dynamics, where each agent is equipped with its own probabilistic temporal objective specified using Probabilistic Linear Temporal Logic on Finite Traces ($\mathsf{PLTL}_f}$). We impose solution concepts (e.g., Nash equilibrium, subgame-perfect equilibrium) as constraints on the joint strategy profile, using payoffs derived from each agent's probability of satisfying its temporal objective. In particular, we formulate per-agent rational synthesis as finding a strategy profile -- if one exists -- such that (i) the designated agent's probabilistic temporal constraint is satisfied, and (ii) the profile represents a stable solution under a chosen solution concept. We give conditional convergence guarantees for tabular Nash-Q learning, certify satisfaction with simultaneous finite-sample confidence bounds, and assess strategic stability with approximate best-response checking. Our approach operates in a stochastic \emph{Multi-Agent Reinforcement Learning} (MARL) environment, where model-free learning algorithms attempt to attain extremal satisfaction probabilities for temporal objectives automatically compiled into reward automata. Our approach is empirically validated using 8 general-sum concurrent stochastic games.

---


### 262. [My Credentials, Please: Detecting Filesystem Capability Laundering in MCP Servers at Scale](https://arxiv.org/abs/2610.22301)

**<font color=#1a73e8>作者：</font>** Zeqian Huang, Mingyue Tang, Aonan Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) standardizes how AI agents invoke external tools. MCP servers expose tools through a declared contract consisting of a name, description, and argument schema. In typical local deployments, client-side approval of a tool call grants the underlying server process broad host filesystem permissions rather than restricting it to the declared operation. We study the resulting vulnerability class, filesystem capability laundering, where attacker-steered arguments cause a tool to access sensitive host files outside its declared contract and deployment scope. We analyze this capability gap across three layers: server-category screening (L1), per-tool contract analysis (L2), and bypassable path-validation checks (L3). We design MCP-FSD to catalog MCP servers, infer least-privilege boundaries per tool, plant credential fixtures outside those boundaries, and evaluate exploitability and sandbox containment via paired dynamic execution. Across 21,097 MCP servers from nine registries, 787 of 4,806 triaged servers (16.4%) exhibit filesystem capabilities despite non-filesystem functional classifications. Dynamic three-case validation confirms 150 vulnerable instances under tested sandbox policies. Coordinated disclosure yielded 13 security advisories, including two CVEs in Anthropic's Git MCP Server.

---


### 263. [ARC-SORT: Adaptive, Robust, Compensated Multi-Object Tracking with Interacting Multiple Models](https://arxiv.org/abs/2610.22306)

**<font color=#1a73e8>作者：</font>** Girish Kumar Adari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking in sports broadcasts is hard for two reasons: athletes move fast and change direction abruptly, and the camera pans and zooms at the same time. We present ARC-SORT (Adaptive, Robust, Compensated SORT), a tracking-by-detection tracker that trains nothing and runs in real time. Its design rule: the tracker measures its own uncertainty, and that measurement decides how it acts. An Interacting Multiple Model (IMM) Kalman filter gives every track a predictive covariance, and we turn it into a per-track search region: the less reliable the motion prediction, the larger the region in which a detection may match (uncertainty-adaptive Expansion IoU, EIoU). On identical inputs, this continuous coupling is what matters: the same covariance used as a hard Mahalanobis gate hurts at every threshold we swept, and richer covariance summaries add nothing measurable. When two tracks cross, the assignment cost itself reports whether the decision was close. ARC-SORT keeps such pairs under review and applies at most one corrective identity swap once post-crossing appearance evidence shows the first decision was wrong; this adds +1.0 HOTA (higher order tracking accuracy) on both the SportsMOT and DanceTrack test sets at under a millisecond per frame. For players who leave the frame for seconds, motion extrapolation carries no information, so our offline re-identification drops the usual motion gate and links tracklets by appearance alone. ARC-SORT reaches 81.82 HOTA on the SportsMOT test set with the fewest identity switches of the 69 leaderboard entries as of August 2026 and tied-third multi-object tracking accuracy (MOTA, 97.09), and 62.1 HOTA on DanceTrack test with the same association settings. On Deep-EIoU's public detections and embeddings it reaches 80.31 HOTA, +3.1 over Deep-EIoU. It runs at about 50 frames per second on a laptop RTX 3060 GPU. Code will be released.

---


### 264. [Not Just a Subject: Capturing Adaptive Scene-Specific Variance for Visual Storytelling](https://arxiv.org/abs/2610.22320)

**<font color=#1a73e8>作者：</font>** SeungJu Cha, Ye-Chan Kim, Kwanyoung Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in diffusion models have significantly improved text-to-image generation, enabling their application to visual storytelling, where coherent image sequences are generated from narrative prompts. However, existing methods primarily focus on identity preservation and often fail to adapt to diverse scene variations, resulting in semantic misalignment and structural inflexibility. We propose EOS-Story, a training-free framework that harmonizes identity consistency with scene-specific adaptation across text and vision spaces. In the text space, we decouple the narrative into identity and scene sub-prompts to prevent information dilution, but this leaves the scene without access to appearance cues. To bridge this gap, we introduce Cross-Contextual Bridging, which softly injects a phrase-level appearance residual into the scene's <EOS> embedding. In the vision space, we find that scale mismatch between identity and scene subjects causes a few identity tokens to be repeatedly transferred, producing structural artifacts. We address this with Adaptive Identity Preservation, which anchors identity features at the scene-specific scale (Identity Anchoring) and integrates them via Identity-Aware Self-Attention. To evaluate performance under varied spatial compositions, we extend the Consistory+ benchmark with diverse framing scenarios (Consistory+_+). Extensive experiments show that EOS-Story achieves competitive or superior performance on both benchmarks.

---


### 265. [AVC-Reward: Event-Centric Audio-Video Consistency Evaluation](https://arxiv.org/abs/2610.22321)

**<font color=#1a73e8>作者：</font>** Yuruo Wu, Kaihang Pan, Kai Shen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As joint audio-video generation models become more capable, they can generate audio-visual scenes exhibiting three forms of complexity: multi-event composition, multi-layer audio mixture, and asymmetric cross-modal relations. However, current evaluations largely reuse metrics from earlier simple and unidirectional tasks. They typically evaluate an audio-video clip as a whole and rely on simple predefined relations, making them unsuitable for these increasingly complex scenes. We propose an event-centric evaluation framework that disentangles audio and visual events at the event level, analyzes each event independently, cross-validates relations across modalities, and aggregates the judgments into a coarse-to-fine, three-level consistency metric. The metric assesses global narrative harmony, event-level temporal synchronization, and fine-grained attribute alignment, providing a general formulation for audio-video consistency evaluation across diverse generation settings and cross-modal relations. We instantiate the metric as AVC-Reward, a trainable audio-video reward model. To evaluate the agreement between automatic judgments and human perception across generation paradigms and relation complexities, we construct AVC-Benchmark, which is primarily built from diverse positive and negative samples generated by various types of audio-video generation models. AVC-Reward achieves state-of-the-art alignment with human judgment among automatic methods, provides interpretable rationales that localize failures, and improves the audio-video consistency of a joint generation model when used as an online reinforcement-learning signal. Project page: this https URL

---


### 266. [Learning Self-Orchestration in Decentralized Agent Swarms](https://arxiv.org/abs/2610.22322)

**<font color=#1a73e8>作者：</font>** Guowei Xu, Zhenting Qi, Amani Kiruga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The capabilities of an agent swarm depend on both its individual members and how they coordinate. Yet existing multi-agent systems often train agents within fixed orchestration structures, separating the learning of individual capabilities from the organization of collective behavior. We introduce market-based post-training (MPT), a framework for jointly learning action policies and self-orchestration in decentralized agent swarms. Agents express their willingness to participate through bids, which determine who acts and how collective outcomes provide local training credit. Learning both action and bidding behavior allows individual capabilities and patterns of participation to adapt together without a central coordinating agent. We evaluate MPT on embodied crafting, robot navigation, and deep research. Results show gains over monolithic post-training and confirm that agent participation indeed evolves with learning. With the same post-trained action policies, learned self-orchestration outperforms alternative coordination strategies. Ablations show that both action and bidding benefit from learning, and that learned bids provide more effective action-training signals. Beyond the original training objectives, trained swarms adapt faster to related tasks and achieve better performance with larger populations at inference time. Larger populations also suffer smaller performance losses under agent dropout, demonstrating that learned self-orchestration supports reuse, scaling, and robustness in decentralized agent swarms. Code and trained models are available at this https URL.

---


### 267. [Dense4D: Pixel-Level 4D Human Correspondence](https://arxiv.org/abs/2610.22325)

**<font color=#1a73e8>作者：</font>** Rıza Alp Güler  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing human motion in 4D requires identifying the same surface points through articulation, deformation and changes in visibility. We introduce Dense4D, to our knowledge the first feed-forward model dedicated to dense 4D correspondence across the body, clothing and hair from a set of monocular RGB images, without a body template. Trained specifically for human geometry, Dense4D jointly processes person-centred crops with known image-to-crop transforms to predict Human Point Maps (HPMs) and depth for each image. An HPM assigns each person pixel the 3D position of its observed surface point at a common reference time. These maps support amodal correspondence: points hidden in the reference image can be localised from observations in other frames. Matching HPM coordinates across crops establishes correspondence without predicting camera poses or large scene displacements; per-image depth then lifts the matches into 3D tracks. Experiments on real people demonstrate substantially higher tracking accuracy and closer agreement with scanned surfaces than the evaluated baselines. Points from different frames assemble into coherent human geometry in the reference pose, providing visible evidence of consistent dense correspondence through articulation and clothing deformation. Additional qualitative results, videos, and an interactive viewer are available at this https URL.

---


### 268. [ACEdit: Stable Multi-Turn Image Editing via Asymmetric Conditioning](https://arxiv.org/abs/2610.22328)

**<font color=#1a73e8>作者：</font>** Sara Dorfman, Nir Goren, Gal Barak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image editing models produce impressive results for individual edits, but their quality often deteriorates over multiple editing turns. Each editing turn introduces small distribution shifts that accumulate over successive edits, creating a gap between the input distributions encountered during the editor's original training and multi-turn inference. We introduce a training scheme that makes multi-turn image editing stable under this accumulating distribution shift. A key is to force the editor to operate on its own outputs from previous editing turns during training, bringing the principle of Self-Forcing to image editing. The main challenge is that self-generated editing trajectories deviate from ground-truth trajectories, making direct supervision unreliable. We address this challenge through a distillation objective that leverages a teacher image editor to provide a reliable training signal when the model operates on its own previous outputs. We introduce an asymmetric conditioning scheme: while the student performs edits sequentially on its own outputs, the teacher remains anchored to the original clean image and receives a compound editing instruction. Experiments show substantially reduced degradation over long multi-turn sequences while maintaining editing quality and instruction adherence.

---


### 269. [Robust Reinforcement Learning for Dynamic Treatment Regimes under Model and Measurement Uncertainty](https://arxiv.org/abs/2610.22336)

**<font color=#1a73e8>作者：</font>** Chengze Xie, Xuan Wang, Ying Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a robust reinforcement learning (RL) framework for learning adaptive treatment policies that generalize across patients and remain reliable under errors in the measured biomarker and shifts in the disease dynamics. By modeling the patient as a hidden context, we address generalization and robustness in a unified manner through robust contextual Markov decision processes. Applying our framework to adaptive therapy for metastatic prostate cancer in a simulator calibrated to clinical data, we obtain generalizable and robust policies that substantially outperform the existing adaptive therapy method. In particular, we attain robustness with almost no loss of performance when the biomarker is accurate and the disease evolves as anticipated, and find that the resulting policy Pareto-dominates the existing method across a diverse array of scenarios. Our findings suggest that robust RL holds great promise as a principled methodology for learning reliable adaptive treatment policies.

---


### 270. [Lean Graph Search for Formal Theorem Proving](https://arxiv.org/abs/2610.22339)

**<font color=#1a73e8>作者：</font>** Yihan Xu, Jia-Chen Gu, Junyi Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieving relevant lemmas is crucial for formal theorem proving, enabling provers to build machine-checkable proofs from established mathematical results. Recent retrieval systems match library declarations to a target theorem or its intermediate proof steps, but make limited use of multi-hop dependencies among declarations. These dependencies can reveal supporting lemmas that are not necessarily lexically similar to the target theorem but recur in proofs of related problems. To this end, we propose LeanGraphSearch, a graph-based retrieval method for Lean 4 that constructs a graph from Mathlib's forward dependencies and traverses it to uncover supporting lemmas through multi-hop dependency chains. Specifically, LeanGraphSearch links each declaration to the premises it depends on, uses a graph-based ranking algorithm to propagate relevance from semantically matched declarations to their dependencies, and reranks the expanded candidates against the original query. Across two mathematical retrieval benchmarks, LeanGraphSearch improves recall by up to 12% over the strongest baseline, LeanSearch v2, on MathlibQR and increases coverage of complete annotated proof routes on MathlibMPR, covering up to 3.7% of extra groups. More importantly, we evaluate whether these retrieval gains translate into improved end-to-end theorem proving by integrating LeanGraphSearch into an iterative proving loop guided by Lean feedback. Across three theorem proving benchmarks, LeanGraphSearch improves pass rate at {8, 16, 32} reflection turns by as much as 40% compared to vanilla prover and at most 10% compared to LeanSearch v2, showing higher accuracy-cost efficiency. These findings highlight the value of dependency graph search for theorem proving and motivate further research on structure-aware search for proof discovery.

---


### 271. [GeoState: Learning View-Decoupled Geometry States for 3D World Modeling](https://arxiv.org/abs/2610.22343)

**<font color=#1a73e8>作者：</font>** Hongchang Liu, Jian Liu, Yujuan Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D world models increasingly use features from geometry foundation models (GFMs) as predictive world states, benefiting from their rich geometric priors. However, the view dependence of these features entangles scene dynamics with camera-induced variation, making the resulting state evolution harder to predict. We propose GeoState, a view-decoupled geometry representation for predictive 3D world modeling that separates scene-state evolution from camera-dependent observation. Specifically, a scene tokenizer aggregates multi-view GFM features into a view-decoupled scene state, which a geometry decoder queries using camera rays. An autoregressive world model then predicts future scene states, while camera motion is modeled separately. The predicted states can therefore be decoded under either predicted or externally specified cameras, while retaining a single context-derived scale throughout the rollout without per-frame scale alignment. Experiments show that GeoState outperforms prior 3D world models on Waymo, supports geometrically consistent cross-view querying, and generalizes zero-shot to KITTI and nuScenes. Project page: this https URL

---


### 272. [Speculative Forcing for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.22347)

**<font color=#1a73e8>作者：</font>** Hyunwook Choi, Seungryong Kim, Dongyoon Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step autoregressive video generators enable streaming generation, yet they run every token through the final denoising step, regardless of how much refinement it needs. We find this uniform computation is often unnecessary: many tokens already closely match their eventual full-step outputs in the initial steps, while others require refinement until the end. We introduce Speculative Forcing, a framework that treats intermediate clean estimates as drafts and predicts when individual tokens can be safely accepted early. Once accepted, a token is frozen as its final output and undergoes no further denoising, while its cached keys and values remain available as context for the remaining tokens. We explore two alternative verifier designs: a training-free one based on similarity to clean content and stability across steps, and a learned one that reads the frozen generator's intermediate features to estimate each token's remaining gap to its full-step output. Across short-video, long-video, and world generation, Speculative Forcing preserves the quality of full-step sampling while substantially reducing computation. On LongLive, it matches the four-step generator with ~1.7 denoising steps per token, running over 1.5x faster at 41.7 and 37.8 fps. On Lingbot-World 2.0, where camera motion continually changes the visible content, it maintains quality with ~2.5 denoising steps per token and runs 1.35x faster at 24.5 fps.

---


### 273. [FDE-Gym: The Last Mile of AI Delivery](https://arxiv.org/abs/2610.22350)

**<font color=#1a73e8>作者：</font>** Dongxu Yang, Hongda Yan, Renxin Wang 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing agent benchmarks typically evaluate agents on well-specified tasks defined by issue reports, specifications, or task tickets. Real-world customer delivery is different: forward-deployed engineers (FDEs) must clarify ambiguous requirements, work in live systems, and uncover unstated constraints. We introduce FDE-Gym, a benchmark of 95 end-to-end delivery tasks from 20 customer scenarios across 18 sectors, each adapted by industry experts from real-world delivery projects. In simulated customer environments with scripted stakeholders and modifiable customer systems, agents interact with stakeholders and operate on production-like systems to deliver working solutions. FDE-Gym scores a delivery by how much it improves the customer's own success metric, normalized between 0 (unchanged system) and 1 (reference solution), with penalties for stakeholder interactions (messages, trial runs, and waiting time). An online platform lets humans practice FDE skills under the same grading criteria. We evaluate 13 model configurations from seven providers. In the realistic setting, where unstated constraints must be discovered, the best configuration achieves a mean FDE-Gym score of 0.56 and resolves only 14 of the 95 tasks (a score of at least 0.8 with no incident). Discovering unstated constraints is the primary bottleneck: performance drops sharply when models must uncover them without explicit guidance. Yet information discovery alone does not account for the gap: even on the 23 tasks where the best configuration obtains every key fact from stakeholders, it reaches a normalized business uplift of 0.8 or above on only 10. These results reveal a substantial gap between solving well-specified tasks and delivering effective AI systems for real customers.

---


### 274. [OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World Modeling](https://arxiv.org/abs/2610.22355)

**<font color=#1a73e8>作者：</font>** Bowei Liu, Xinchen Zhang, Xuhuan Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative visual verifiers play a crucial role in advancing multimodal intelligence. To enhance the robustness of visual verifiers in complex multimodal scenarios involving compositional requirements, we move beyond conventional binary verifiers that produce only True/False discrete judgments and introduce a verifier that automatically decomposes complex prompts or environmental rules into fine-grained components and assigns pointwise scores to provide a continuous and more informative critique signal. Our experiments further demonstrate that these structured and interpretable outputs improve the verifier's generalization to out-of-domain multimodal critic tasks. To train this verifier, we introduce a Decoupled RL training strategy that jointly optimizes sub-question-level binary judgment and global alignment scoring, using precise local feedback to develop fine-grained verification capabilities that provide a foundation for reliable continuous scoring at the global level. Under a general reinforcement learning framework, we first empirically demonstrate that the proposed pointwise graded verifier significantly outperforms binary verifiers in traditional text-to-image scenarios. We then extend our investigation to rule-governed generative world modeling where generative models are leveraged for world simulation and world reasoning under explicit rules. From a theoretical standpoint, we further show that a pairwise verification paradigm yields more accurate critiques than the pointwise formulation when ground-truth images are available, with empirical results on diverse structured world-modeling tasks such as Maze and Sudoku further validating the effectiveness of our approach. Overall, our findings suggest a key insight: the transition from generative models to structured world-modeling agents critically hinges on the availability of accurate pairwise graded visual verifiers.

---


### 275. [PathFM: Fast Generative Forecasting of Multivariate Trajectories](https://arxiv.org/abs/2610.22358)

**<font color=#1a73e8>作者：</font>** Jiachen Yao, Xiyuan Zhang, Annan Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models are becoming increasingly popular for general-purpose forecasting. However, most leading models predict marginal quantiles, leaving the dependence structure of future trajectories unspecified. This distinction matters for trajectory-dependent quantities such as cumulative demand, peak load, and event timing, yet point and marginal scores do not reveal it. To model this dependence, we introduce PathFM, a trajectory-based forecasting model that uses flow matching to generate complete future paths. We further distill the model to one or two steps and share history attention cache across draws. Together, these enable PathFM to generate multiple paths for a single series in roughly the time needed for one query to a quantile model. The distilled sampler also makes it practical to optimize a calibration loss directly. PathFM achieves competitive marginal accuracy on the established forecasting benchmarks fev-bench and TIME. To complement these evaluations, we introduce Forecast Path Score Bench (fps-bench), which augments fev-bench tasks with energy and variogram scores and downstream metrics. PathFM achieves a higher aggregate path score on fps-bench than all evaluated external baselines. Experiments on chaotic systems further show that our flow model sustains long-run variability, while strong baselines rapidly collapse. PathFM makes generative time series forecasting both competitive and practical, enabling diverse downstream applications.

---


### 276. [SoftCache: Adaptive Step Size Caching for Diffusion Transformers](https://arxiv.org/abs/2610.22369)

**<font color=#1a73e8>作者：</font>** Shimon Malnick, Nadav Orenstein, Ohad Fried 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow models generate a sample over iterative steps, each a full pass through a large network, and that pass dominates generation cost. Training-free caching accelerates them by reusing activations from recent evaluations instead of recomputing them. Dynamic caching methods decide when to refresh by accumulating a cheap probe of the network input into a staleness signal and spending a fresh evaluation once it crosses a threshold. They perform hard caching: the signal is a binary switch between refresh and reuse, and every step, fresh or cached, advances by the prescribed step size. We observe that the signal carries much more than this switch. How far it sits below the threshold, its headroom, predicts the error induced by reuse. We propose SoftCache, which performs soft caching: instead of a binary switch, the headroom sets how far each cached step goes. Where the headroom is large, the sampler jumps past several scheduled nodes, and as a refresh nears, its steps shrink back toward the original step. These adaptive jumps may land between the scheduled nodes, taking the sampler off its fixed grid. SoftCache requires no training and adds no per-backbone settings: on FLUX for images and on HunyuanVideo and Wan2.1 for video, at speedups from $3.5\times$ to $6.9\times$, it is ahead of every baseline on all four fidelity metrics.

---


### 277. [Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation](https://arxiv.org/abs/2610.22370)

**<font color=#1a73e8>作者：</font>** SeungJu Cha, Ye-Chan Kim, HyunGee Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Token merging has emerged as an effective training-free strategy for accelerating diffusion models by reducing redundant token computation while minimizing generation degradation. A key challenge is determining which tokens can be safely merged and which should be preserved for subsequent computation. Existing method addresses this by preserving prompt-aligned foreground regions, thereby protecting semantically relevant structures. However, this text-relevance criterion overlooks background objects, local details that are not explicitly mentioned in the prompt, leading to degraded structural coherence. In this work, we propose Dynamics-aware Token Merging (DaTMe), a training-free framework that grounds token merging in the underlying diffusion dynamics. Our key insight is that token importance should reflect whether a token remains unresolved during denoising and whether it carries structural information. To this end, DaTMe constructs a dynamics- aware importance map from the Tweedie denoised estimate. The map combines a temporal signal, measuring inter-step changes in the predicted clean image, with a structural signal, capturing local high-frequency content such as boundaries and fine details. Using this map, DaTMe adaptively assigns tokens into merging roles under a given compression ratio: important tokens are preserved as anchors, while tokens that are both temporally stabilized and structurally homogeneous are selected as safe merge candidates. Experiments on PixArt-a and FLUX demonstrate that DaTMe maintains visual fidelity across the entire image, highlighting diffusion dynamics as an effective token-level merging decision in efficient generation. Our code is available at this https URL.

---


### 278. [Gen4P: Video Generators are 4D Perceivers](https://arxiv.org/abs/2610.22371)

**<font color=#1a73e8>作者：</font>** Yitong Xia, Zeren Jiang, Chuanxia Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Gen4P, a unified framework for recovering 4D geometry and motion from monocular video. We show that a pretrained video generator can be repurposed into a feed-forward 4D perceiver without iterative denoising. Building on on-demand querying, Gen4P processes clean video latents in a single encoder pass and predicts the requested 4D attributes through a lightweight cross-attention decoder. The on-demand query formulation enables flexible spatial sampling, and our proposed continuous-time queries further provide temporal flexibility. To strengthen geometric knowledge, we propose a straightforward plug-in solution by incorporating a pretrained video-depth LoRA as a frozen geometry prior, improving overall performance without adding extra trainable parameters. Gen4P achieves state-of-the-art or competitive performance on tasks of 3D point tracking, video depth and camera pose estimation. Qualitative results on in-the-wild videos illustrate its capability of tracking complex motion while maintaining the delicate structure. Together, these results demonstrate the potential of video generative pretraining for unified 4D perception. See this https URL for more visual results.

---


> [!TIP]
> 当前位于：**251-278**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-278**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
