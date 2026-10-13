# 📦 其他研究 | 2026年10月14日

> 本类共 **244** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-244](./part-05.md)

---

### 101. [CAPE - Context-Aware Prioritization Engine for Vulnerability Scoring and Management](https://arxiv.org/abs/2610.13071)

**<font color=#1a73e8>作者：</font>** Rakesh Podder, Viktoria Koscinski, Indrajit Ray  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability patching is critical for safeguarding an enterprise's software ecosystem from cyber attacks. However, patching requires adequate preparation for potential system downtime and for unforeseen effects of the patched software on a live system. Thus, effective risk mitigation requires prioritization strategies that explicitly account for the operational context of the affected software. While vulnerability prioritization based on Common Vulnerability Scoring System (CVSS), Exploit Prediction Scoring System (EPSS) and CISA Known Exploited Vulnerabilities (KEV) catalog, can help, their differing goals and methodologies often lead to inconsistent, context-unaware decisions resulting in mis-allocated remediation efforts. In this work, we present the Context-Aware Prioritization Engine (CAPE), a vulnerability analysis framework that enriches each vulnerability scanner report of vulnerabilities (CVEs) with deployment-specific evidence. This evidence is used to perform vulnerability reachability, centrality, and exploitability analysis, producing a ranked priority score for the effective distribution of remediation effort. We evaluate CAPE on 30 open-source agentic applications comprising 6,138 scanner-reported CVEs. Our evaluation shows that a significant majority of CVEs are not reachable and exploitable which results in significant disparities between CAPE and context-free baselines - the CVSS, EPSS, and KEV. It also shows that CAPE consistently surfaces confirmed-exploitable CVEs at higher priority than all baselines, demonstrating that context-aware analysis provides substantially more accurate remediation guidance than context-free severity scoring alone.

---


### 102. [Double-Take: Improving Capacity, Binding, and Selectivity In Long-Context Within Bidirectional Memory](https://arxiv.org/abs/2610.13073)

**<font color=#1a73e8>作者：</font>** Vakul Raghavan, Utkarsh Grover, Mingyang Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Processing a long sequence does not guarantee that distant information remains usable. As context grows, a fixed-size memory must retain many associations, connect information across positions, and preserve relevant structure without being overwhelmed by everything it observes. These are distinct requirements: a memory may store more information without representing the relationships needed for retrieval, and it may transport those relationships without preserving the ones that matter. Thus, the challenge is not simply extending context length, but constructing a memory that remains usable as context grows. We study this problem in large-chunk test-time training (TTT) and identify two basic failures: single-step writes accumulate interference, limiting capacity, while self-associative writes cannot form cross-position bindings. We introduce Double-Take (DT), which repairs these failures with multi-step unpinned updates and cross-position mixing, and adds bidirectional change-sensitive writes for selective retention. Capacity alone leaves end-to-end recall at the $0.10$ chance floor; adding binding raises it to $0.92$. Trained only on $32\,\mathrm{kb}$ genomic contexts, DT reaches $0.927$ AUROC at $131\,\mathrm{kb}$ and $0.856$ near $1\,\mathrm{Mb}$, while transferring zero-shot from human to mouse. Together, these results identify capacity, binding, and selectivity as three requirements for usable long-range memory.

---


### 103. [The Limits of Query Monitoring against Distributed Model Extraction](https://arxiv.org/abs/2610.13083)

**<font color=#1a73e8>作者：</font>** Snigdha Chandan Khilar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model providers now face distillation campaigns run through thousands of accounts, each of which looks like an ordinary user. When network and payment metadata cannot link those accounts, the only evidence left is what they ask. We study what a provider can and cannot learn from those queries alone, using one million real chat turns for development and 17 later weeks that no design choice touched for a single frozen evaluation. The answer is set less by anything specific to extraction than by benign coordination: a campaign is visible only if it is more distinctive than the most distinctive group of ordinary users in the same week. We make this precise, show that a small but positive difference between campaign and users buys a detection time rather than detectability, and identify the campaign that is hardest to detect. Empirically, a calibrated monitor catches naive distributed extraction that per-account monitors miss (0.86-1.00 of weeks), and one variant - selecting accounts that move together after discounting how topical each one is - still catches campaigns padded with natural text (0.50-0.96 of weeks) where the other two spectral detectors catch none. Distilling each campaign into a small student shows that, in our testbed, campaigns that evaded every detector kept at most 42% of the capability of a detectable one. The limits are equally concrete: a campaign that ramps up slowly poisons every detector's calibration, benign evaluation pipelines look exactly like distillation, we found no deployable detector at colluder shares of 2.5% or below, and campaigns that relay real users' requests may be invisible to any query-only monitor.

---


### 104. [Safety Graph: When Safety Responses Become Attack Surfaces in Cyber-Physical Systems](https://arxiv.org/abs/2610.13086)

**<font color=#1a73e8>作者：</font>** Rakesh Podder, Philip D. Hopkins, Sarath Sreedharan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern industrial control systems (ICS) are susceptible to cyber attacks triggering safety failures in the operational technology (OT) layer. The traditional way to mitigate any failure in OT is to implement safety responses. However, we show in this work that these responses can open up new attack surfaces, thereby vastly expanding the scope of lateral movement. Existing frameworks model cyber-to-physical escalation but provide no mechanism to reason about how these safety responses to OT-failures can trigger new cascading cyber attacks in the Information Technology (IT) layer. To enable such reasoning, we introduce Safety Graph (SG), a formal framework unifying three paradigms - Attack Graphs (AG), Fault Trees (FT), and Event Trees (ET) - over a shared propositional state space, capturing the full bidirectional IT-OT cascade. We provide a sound and complete compilation of SG to a classical AI planning problem, performing plan search using A* to find cross-layer cascade paths. Through a Web3D modeling and simulation of the Tennessee Eastman chemical process plant, which is a widely used chemical engineering benchmark serving as a standard for testing control, monitoring and fault propagation, we demonstrate that the planning compilation of SG automatically discovers safety-response-induced lateral movements, and identifies the responsible barriers that are unidentifiable under existing models. A complexity and scalability analysis characterizes how the planning compilation of SG scales with model size and cascade depth. To the best of our knowledge, SG is the first framework to formally model IT-OT attacks and enable operators to explore the problem of cyber attacks triggering cascading failures in ICS.

---


### 105. [Volume Rendering with Metric--Phase Fields for Thin Structures and Sign-Ambiguous Geometry](https://arxiv.org/abs/2610.13088)

**<font color=#1a73e8>作者：</font>** Junkai Deng, Jiayi Kong, Xuhui Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural implicit surface methods that couple volume rendering with signed distance functions (SDFs), such as VolSDF and NeuS, achieve high-quality multi-view reconstruction for watertight objects. However, these approaches rely on a globally consistent inside-outside partition of space. This assumption becomes fragile for thin structures (e.g., sheets, tubes, and thin walls) and can break down for sign-ambiguous geometry (e.g., surfaces with boundary, non-manifold junctions, and closely spaced surface components), often resulting in spurious closures or loss of fine structures. Unsigned distance field (UDF) formulations relax the global sign requirement and better support non-watertight geometry, but are substantially harder to optimize. We propose PhaseSurf, a neural volume rendering framework built on Metric-Phase Fields (MPFs). MPFs decompose geometry into a nonnegative metric field capturing unsigned proximity and a continuous phase field providing a soft sign cue. By coupling the two through residual phase injection, MPFs yield a signed composite implicit function with stable near-surface gradients while retaining UDF-like robustness in sign-ambiguous regions. This design enables direct iso-surface extraction using standard Marching Cubes and avoids the failure modes of both pure SDF- and UDF-based formulations. We further introduce MPF-specific training losses that enforce metric consistency, stabilize phase transitions near the interface, and suppress spurious geometry in free space. Experiments on multi-view datasets with thin structures and sign-ambiguous geometry show that PhaseSurf produces more stable reconstructions and higher-quality geometry than UDF-based methods and recent 3DGS pipelines, while avoiding artifacts typical of SDF-based approaches.

---


### 106. [From 2.1M Hours of Raw Broadcast Audio to Finnish Speech SSL: Confidence Filtering and Architectural Analysis at Scale](https://arxiv.org/abs/2610.13102)

**<font color=#1a73e8>作者：</font>** Yaroslav Getman, Tamás Grósz, Tommi Lehtonen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Broadcast archives offer scale and diversity for self-supervised learning (SSL) but contain substantial noisy, non-speech, and multilingual content. Prior work typically relies on voice activity detection or language identification (LID) to extract speech, ensuring presence rather than quality. Whether and how to filter unlabeled speech by quality for SSL, particularly from noisy broadcasts, remains underexplored. We present a large-scale Finnish SSL study starting from 2.1M hours of unconstrained broadcast audio. We propose automatic speech recognition (ASR) confidence as a proxy for pretraining data quality and show 3-7% relative WER improvements over LID-based filtering despite a smaller training set. We further address the lack of controlled architectural comparisons in speech SSL by evaluating Transformer, Macaron-Net, Conformer, and E-Branchformer at matched parameter budgets. Our models improve upon prior Finnish SSL baselines, particularly at Base scale and out-of-domain.

---


### 107. [Replaying the Movie in Your Mind Decoding Dynamic Visual Perception and Recall from EEG](https://arxiv.org/abs/2610.13120)

**<font color=#1a73e8>作者：</font>** Zikai Fang, Tian-Yi Zhou, Xuan-Hao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decoding dynamic visual content from EEG has advanced rapidly for visual perception, yet it remains unclear which aspects of neural representations are preserved when people internally replay dynamic scenes. We introduce PAIR, an EEG benchmark collected from 20 participants using an interleaved, clip-wise paradigm that pairs naturalistic video viewing with immediate visual recall. This design enables a comparison between externally driven perception and internally generated recall for the same stimulus content within a fixed trial sequence. We benchmark multiple decoding models on hierarchical semantic classification at both fine-grained and coarse-grained levels, meta-feature decoding tasks covering motion, color, object number, face, and human presence, and a state-decoding task that discriminates perception from recall. Within-subject validation results show numerically similar performance for several model--task combinations, alongside higher perception accuracy in two coarse-grained comparisons after multiple-comparison correction. In contrast, perception and recall are highly separable at the state level under the present validation protocol. State accuracy remains high after alpha-band ablation, although this does not exclude ocular or other task-related contributions.

---


### 108. [BenCoDiC: A Large-Scale Contextual Cyberbullying Corpus for Bengali Political News Discourse FULL VERSION](https://arxiv.org/abs/2610.13121)

**<font color=#1a73e8>作者：</font>** Md. Nesarul Hoque, Rudra Pratap Deb Nath, Umme Salma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cyberbullying is a growing concern in online communities, yet existing Bengali corpora remain limited in contextual information, annotation transparency, scale, accessibility, and support for multidimensional analysis, thereby hindering robust detection and comprehensive study of harasser behaviors and networks. To address these gaps, we introduce the Bengali Contextual and Diverse Cyberbullying (\textit{BenCoDiC}) corpus, a publicly available contextual cyberbullying resource for Bengali political news discourse comprising 50,250 textual instances collected from 100 YouTube videos and their associated discussions. The corpus preserves caption--comment--reply relationships and is organized through a nine-dimensional star schema covering users, videos, textual content, context, time, engagement, political parties, target identities, and language categories. Five AI chatbots were initially evaluated for annotation but did not meet the predefined reliability criterion. Consequently, a two-tier human annotation process with expert verification was adopted, achieving Fleiss' $\kappa=0.86$ and Krippendorff's $\alpha=0.86$. Statistical analyses characterize the corpus, while transformer-based experiments show that incorporating conversational context yields modest but consistent improvements over isolated-text classification. \textit{BenCoDiC} supports context-aware cyberbullying detection and perpetrator-oriented behavioral and network analysis. The corpus is available at this https URL.

---


### 109. [GuidedNav: Shaping Vision-Language Navigation Representations through Pre-action Attention and Spatial Guidance](https://arxiv.org/abs/2610.13122)

**<font color=#1a73e8>作者：</font>** Jingyu Guo, Jiaxin Huang, Chengxing Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-language navigation (VLN) requires an agent to track progress through an extended instruction, identify landmarks relevant to its current objective, and understand the surrounding spatial structure to act. End-to-end navigation policies typically rely on action supervision to implicitly learn these capabilities. Without explicit guidance on the evidence underlying each decision, however, policies can overfit to correlations predictive of training actions rather than learn the task-relevant grounding and geometry needed for generalization. Our insight is to guide the representations that connect instructions to actions: identifying what remains to be done determines which visual evidence matters, while understanding the geometry around that evidence informs how to move. We introduce GuidedNav, a unified framework that explicitly shapes these representations through training-time guidance. Subtask and landmark guidance steer native pre-action attention toward the active instruction segment and relevant visual regions, grounding action prediction in the current objective. Spatial guidance aligns the policy's internal representations with geometric features that capture long-horizon context and local spatial structure. Together, these objectives strengthen navigation capabilities while avoiding the inference overhead of intermediate textual reasoning and online geometric encoding. We also introduce Guided-R2R and Guided-RxR, two annotation-enriched navigation datasets that support more interpretable VLN research. GuidedNav establishes state-of-the-art performance among the compared monocular RGB policies, improving success rates by 8.1% and 13.1% relative to the strongest prior results on R2R-CE and RxR-CE val-unseen, respectively, while achieving faster inference. Extensive experiments further demonstrate the effectiveness and real-world transferability of our approach.

---


### 110. [Looking Ahead and Back: Anticipatory Generative Modeling for Road-Network Trajectories](https://arxiv.org/abs/2610.13131)

**<font color=#1a73e8>作者：</font>** Zhenhao Huang, Li Sun, Philip S. Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trajectory generation underpins urban applications such as traffic management and urban planning. Within road networks, vehicle movement along road segments is largely deterministic, whereas transitions at intersections are critical--multiple outgoing paths may appear equally plausible, yet they can lead to substantially different downstream routes. Existing generative methods such as diffusion models simulate location sequences and fail short of next transition selection, even producing trajectories that drift off the road network. To fill this gap, we advocate a fundamental shift: moving beyond location simulation toward behavior modeling on the road network. In this paper, we revisit trajectory generation through the lens of generative route planning, and introduce a new graph-constrained generative paradigm, Anticipatory Generative Modeling, which resolves next transition selection by incorporating the Anticipation of how the future route may unfold toward the destination. Concretely, we propose a novel generative model named Foresight that formulates a probabilistic model for an "anticipate--select--update--re-anticipate" loop that enables longer-term foresight while continuing sequential generation along the historical trajectory. Extensive experiments demonstrate that Foresight wins state-of-the-art baselines.

---


### 111. [The Limits of Manipulation within Personalized Incentive Policies](https://arxiv.org/abs/2610.13133)

**<font color=#1a73e8>作者：</font>** Andrea Araldo, Alessa Mayer, Ravi Seshadri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Demand management policies aim to shift individual behavior toward sustainable choices (e.g., goods, transport modes). Personalized incentive policies tailor subsidies to agents' needs and constraints, but personalization also exposes the regulator to agents' strategic manipulative behavior. The extent to which agents can profitably manipulate such policies remains poorly understood, which limits their applicability.
This paper establishes analytically the conditions under which manipulation benefits the agent. We formalize a Stackelberg game in which an agent may simulate a different profile to extract higher incentives from a regulator. Previous work typically assumes that the regulator would instantaneously classify agents into the simulated user profile. In contrast, we explicitly model the regulator's process of learning the agent profile, based on observed past behavior. This makes manipulation harder, since it forces the agent to consistently behave according to a simulated profile, thus renouncing following their true preferences. Manipulative agents thus incur a Cost of Manipulation, which has typically been neglected. By accounting for it, we get a counterintuitive finding: although classification uncertainty reduces personalization accuracy, it may benefit the regulator by deterring manipulation. We establish an upper bound on the agent's gain from manipulation, which becomes stricter as profiles become harder to distinguish for the regulator. Simulations on the London Passenger Mode Choice dataset illustrate this deterrence effect. The framework can therefore be used to stress-test the robustness of personalized incentive policies before deployment.

---


### 112. [How Anthropomorphic Attitudes Toward Agents Divide User Behavior, and How Design Should Change](https://arxiv.org/abs/2610.13156)

**<font color=#1a73e8>作者：</font>** Tingyu Cao, Yan Tang, Keer Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Studies of conversational agents rely on interviews, surveys, lab tasks, or taxonomies. Whether anthropomorphic naming splits those patterns, and whether replies should change, lack field evidence. We report a field study of a desktop assistant (May-August 2026; n=257). Stance is an anthropomorphic assistant name (118 users; 45.9%). Behavior comes from a 128-unit sparse-autoencoder codebook, identity tags, and opening lexicons. Ranks differ by stance (Spearman rho=+0.249 vs. null mean +0.382; p=.0419). Teacher and tutoring identities covary with renaming, an introverted task-only orientation against it; renamers greet more and command less; confiding shows the codebook's largest gap. We revise the agent: greet and receive affect on relational openings, execute directly on tasking. In 1,744 judgments (n=129), renamers chose the revised reply far more often than default-name users on being treated as a person and having affect received, less robustly on willingness to continue, and neither judged it worse on task interference.

---


### 113. [SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for Search Agents](https://arxiv.org/abs/2610.13157)

**<font color=#1a73e8>作者：</font>** Shengze Huang, Zihao Tang, Jinluan Yang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for search agents often suffers from evidence fabrication, a failure mode where agents bypass external information ($E_{ext}$) and fabricate an incorrect answer. We argue that this fabrication arises from an over-reliance on unreliable internal knowledge ($E_{int}$) as shortcuts due to the inherent opacity of reasoning trajectories. To address this, we propose SOAR (SOurce-Aware Reinforcement learning), a paradigm that transforms monolithic reasoning into source-explicit trajectories. SOAR (i) disentangles $E_{ext}$ and $E_{int}$ into parallel, observable streams via a Source-Aware Workflow, and (ii) incorporates Source-Consistent Reward to guide the policy evolution. By making information-source attribution explicit, SOAR enables precise credit assignment between different knowledge streams. Evaluations show that SOAR outperforms baselines on 3B and 7B backbones by 7.3% and 5.4%, while reducing evidence fabrication by 74.8%. These confirm that SOAR significantly improves performance on knowledge-intensive benchmarks while effectively mitigating evidence fabrication, fostering more faithful and grounded reasoning with enhanced robustness.

---


### 114. [PreCoG: Preview-Edit for Efficient Video Correction in Generation-Time](https://arxiv.org/abs/2610.13174)

**<font color=#1a73e8>作者：</font>** Yilai Liu, Wenqi Pei, Zhifeng Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iterative text-to-video generation relies on feedback to correct compositional and temporal failures. However, existing methods typically require another full generation run for each correction, repeating computation and potentially disrupting already correct content. We introduce PreCoG, an iterative framework for correcting semantic failures during video generation. PreQA diagnoses failures from low-cost previews and constructs corrective conditions, while PreEdit edits cached generation trajectories under these conditions, attenuating orthogonal changes to limit disruption of already correct content. PreCoG completes generation only for the selected candidate, reusing its cached trajectory to reduce redundant computation and help preserve semantic consistency between the preview and the final video. Experiments show that PreCoG achieves the highest VBench and T2V-CompBench scores and approaches VSR's leading VS2 score at $0.56\times$ its inference time. It also outperforms GENMAC on all three quality and alignment metrics at $0.86\times$ its inference time.

---


### 115. [Fix the Match, Not the Solver: STITCH -- a Self-Supervised Compatibility Measure for Eroded Visual Puzzles](https://arxiv.org/abs/2610.13176)

**<font color=#1a73e8>作者：</font>** Nadav Alali, Ohad Ben-Shahar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlike the clean and pixel-aligned complete pieces of standard jigsaw benchmarks, real-world puzzle fragments lose their boundary regions to erosion, destroying the signal that classical compatibility measures (CMs) rely on. We first re-establish, via oracle experiments, that the CM, not the solver, is the performance bottleneck: with a perfect CM, even a simple greedy solver achieves perfect reconstruction. This motivates STITCH, a self-supervised CM that sidesteps missing boundaries by comparing frozen ViT patch tokens from piece interiors via a lightweight cross-attention head (~249K trainable parameters), trained without manual annotation. Plugged into unchanged compatibility-based solvers, STITCH reaches .992/.954 Abs/Perf on JPwLEG-5 (+.629 Perf over the best prior method), nearly saturating the benchmark. On a new ImageNet 7x7 benchmark, it outperforms all alternatives, including inpaint-then-match pipelines built on modern generative models. Importantly, performance remains robust across erosion levels and generalizes to puzzles with over 40% missing pieces without retraining. Trained on the recent GAP datasets of irregular, heavily eroded fragments, the same CM recipe enables compatibility-based solvers to surpass recent learning-based solvers on GAP-3 and GAP-5. Since this leap in performance is achieved by a pluggable CM module, the takeaway is clear: fix the match, not the solver.

---


### 116. [CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177)

**<font color=#1a73e8>作者：</font>** Bing He, Jingnan Gao, Yunuo Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D scenes from sparse views without per-scene optimization remains highly challenging, especially for recovering accurate geometry and fine textures. While recent feedforward approaches leverage generalizable 3D Gaussian Splatting (3DGS) for scene generation, they typically assign one or multiple Gaussians to each pixel. Such uniform allocation not only produces highly redundant representations by wasting primitives in homogeneous areas, but also fails to exploit the inherent geometric priors of planar surfaces, often resulting in sub-optimal structural modeling. To address these limitations, we present CompactSplat, a novel feedforward framework that enables a content-aware allocation of 3D Gaussians. By integrating texture-guided spatial partitioning with hierarchical sampling, CompactSplat adaptively distributes primitives - concentrating dense Gaussians in complex regions while tiling flat areas with expanded, scale-modulated primitives. Moreover, our framework inherently supports dynamic sparsity control at inference time, enabling seamless trade-offs between rendering fidelity and memory footprint without requiring network retraining. Extensive experiments on RealEstate10K, DL3DV, and ScanNet demonstrate that CompactSplat consistently outperforms prior methods on both standard metrics and high-resolution rendering consistency, achieving high-fidelity reconstructions with significantly fewer primitives.

---


### 117. [High-Throughput Generative Video Super-Resolution on a Single Consumer GPU](https://arxiv.org/abs/2610.13179)

**<font color=#1a73e8>作者：</font>** Georgios Panaretou, Sotirios Chatzis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative video super-resolution (VSR) can recover visually compelling high-frequency detail by leveraging diffusion priors, but iterative sampling and heavy spatio-temporal coupling make practical deployments difficult. We study a different operating point: practical HD generative VSR on a single high-end consumer GPU without end-to-end retraining. To this end, we present a zero-shot framework built entirely from pretrained components.
The proposed system decouples spatial enhancement from temporal stabilization. A time-distilled one-step diffusion backbone handles spatial upscaling, while temporal coherence is promoted by a lightweight pretrained flow-based interpolator that synthesizes intermediate frames between super-resolved keyframes. To further improve scalability, we introduce a resolution-aware hybrid attention scheme that, in a zero-shot manner, replaces selected high-resolution global-attention layers with neighborhood attention while preserving global attention in semantically critical low-resolution layers, while also improving temporal consistency.
Experiments show that the proposed framework reaches up to ~32 FPS at 720p resolution under interleaved inference on a single NVIDIA RTX 4090. At 4K, the proposed attention substitution can yield up to a 44% speedup over the original attention implementation. Across standard VSR benchmarks, the method consistently shifts the speed-quality trade-off decisively toward runtime efficiency, trading reconstruction fidelity for strong no-reference perceptual quality, while remaining reasonably competitive against generative approaches in temporal consistency. It also exposes clear limitations in handling more challenging motion, which a simple motion gate partially mitigates. Code will be released upon acceptance.

---


### 118. [MixTok: Adaptive Visual Tokenization with Global 1D Tokens and Sparse 2D Refinement](https://arxiv.org/abs/2610.13181)

**<font color=#1a73e8>作者：</font>** Chenge Li, Yefei He, Xinyu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient visual tokenization requires balancing representation compactness with the preservation of fine-grained image content. Conventional grid-based tokenizers allocate tokens uniformly across spatial locations despite non-uniform visual complexity, whereas compact 1D tokenizers aggregate global information but can struggle to preserve local details. We introduce MixTok, a hybrid visual tokenizer that combines a compact 1D global representation with sparse 2D tokens for local refinement. A content-adaptive router ranks candidate locations by refinement priority and determines the number of 2D tokens for each image under a target average token budget. At the highest-scoring locations, 2D token features replace the spatial features recovered from the 1D representation, and a shared decoder reconstructs the image from the resulting mixed features. On ImageNet 256 x 256, MixTok achieves highly competitive reconstruction and generation performance, with an rFID of 1.195 and a gFID of 1.95 at respective average budgets of approximately 128 and 131 content tokens per image.

---


### 119. [From Observation to Intervention: Identifiability of Latent User Bias in Human-AI Interaction](https://arxiv.org/abs/2610.13185)

**<font color=#1a73e8>作者：</font>** Lucas Biechy, Yuxiao Li, Zhonghao He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Alignment methods typically treat user behavior as a reliable proxy for underlying preferences. However, this assumption breaks down when users hold belief-dependent cognitive biases, risking irreversible ``confirmation traps'' and harmful feedback loops. In this paper, we formalize when an AI system can distinguish true user preferences from behavior shaped by cognitive bias. Modeling this interaction as a multi-armed bandit, we first prove a non-identifiability theorem: under passive observation, a static binary biased user produces action trajectory distributions strictly identical to an unbiased user in a transformed environment, forcing any action-only estimator to perform no better than random guessing. We then show that active preference elicitation breaks this observational equivalence. Specifically, we prove that an Observer applying a finite sequence of adversarial zero-reward interventions of length $m_\delta$ makes the post-intervention action distributions arbitrarily separable. Our theoretical results suggest that robust alignment requires actively intervening to tell informed preferences from biases.

---


### 120. [WaSA: Wavelet Scattering Autoencoders for Unsupervised Offline Detection of Malicious Clients in Federated Learning](https://arxiv.org/abs/2610.13186)

**<font color=#1a73e8>作者：</font>** Alessandro Licciardi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative model training without exposing raw data, yet remains vulnerable to malicious clients injecting poisoned datasets. Existing defenses are typically reactive (operating during training) or supervised (requiring prior knowledge of attack types) - assumptions that rarely hold in open-ended IoT deployments. We propose WaSA, a fully unsupervised, offline framework for malicious client detection. Before training, each client transmits a single, privacy-preserving spectral summary of its data to the server. A denoising autoencoder, trained solely on clean auxiliary data, scores clients based on their deviation from the learned benign manifold, identifying corruptions regardless of the attack type. WaSA requires no attack labels, generalizes to unseen anomalies, and introduces a Boltzmann sampling strategy for client selection that smoothly interpolates between hard exclusion and standard aggregation. Experiments on MNIST, CIFAR-10, and CIFAR-100 under diverse attack scenarios (up to 90 % malicious clients) demonstrate consistent improvements over supervised baselines and robust aggregation methods, with negligible communication overhead. Code is available at this https URL.

---


### 121. [Destination-Conditioned Adaptation with Semantic-Geometric Alignment for Generative Inbetweening](https://arxiv.org/abs/2610.13187)

**<font color=#1a73e8>作者：</font>** Zhiyu Xu, Wei Shang, Yushen Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative inbetweening aims to synthesize temporally coherent intermediate frames between a start frame and a target frame. Although pretrained image-to-video diffusion models provide strong priors for large-motion inbetweening, they are not explicitly designed to reach a specified target frame. They may therefore generate realistic individual frames while drifting from the target or producing unstable motion under large displacements and non-rigid dynamics. We propose DSG-GI, a framework that adapts pretrained latent video diffusion models through \textbf{D}estination-Conditioned Adaptation and \textbf{S}emantic-\textbf{G}eometric Alignment. Destination-Conditioned Adaptation treats the target frame as the destination of the sequence and provides temporally progressive guidance along the generated trajectory. Semantic-Geometric Alignment aligns the token-wise spatio-temporal relational geometry of backbone features with that of a frozen video foundation encoder and applies a flow-matching-aware latent flow constraint to samples near the data endpoint of the probability path. Together, these components strengthen destination guidance and preserve coherent semantic-geometric motion structure. Extensive experiments on standard and large-motion inbetweening benchmarks demonstrate improvements in temporal stability, target-frame faithfulness, and perceptual quality. Our code will be made publicly available.

---


### 122. [JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models](https://arxiv.org/abs/2610.13194)

**<font color=#1a73e8>作者：</font>** Mengdi Liu, Chenghao Jia, Hong Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon autonomous research has shown promise in accelerating scientific progress through sustained cycles of hypothesis generation, implementation, and validation. However, this Generate-Execute-Feedback paradigm relies on reactive trial-and-error, where costly and time-consuming executions introduce severe feedback delays, throttling evolutionary progress under explosively expanding search space. To address this challenge, we propose JANUS, a framework that unifies future outcomes forecasting and past experience reflection through a Predict-Verify-Evolve loop driven by a co-evolving world model. Within an evolving graph, the research agent proposes candidates while world model scores them by forecasting value improvement, information gain, and exploration utility, then accordingly selects, refines, or prunes branches prior to execution. After receiving ground-truth feedback, JANUS distills experience into evolving skills: hierarchical skills for research agent, exploration-strategy skills for world model, and their coordination protocols. This mechanism enables continual co-evolution: the research agent sharpens candidate generation while the world model refines its predictive judgment over extended horizons. Extensive evaluations on MLS-Bench-Lite and real research tasks demonstrate that JANUS significantly outperforms state-of-the-art baselines, achieving both higher evolving efficiency and ceiling.

---


### 123. [Does Learning Recurrent Networks Matter in Partially Observable RL?](https://arxiv.org/abs/2610.13197)

**<font color=#1a73e8>作者：</font>** Zekang Wang, Zhe He, Gaojie Jin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) under partial observability typically re- lies on recurrent networks to encode temporal information, with the recurrent module trained jointly with the policy or value function. This raises a natural question: is learning the recurrent network actually necessary? In this paper, we investigate whether a frozen recurrent network can provide sufficient memory for solving par- tially observable Markov decision processes (POMDPs). Motivated by the theoretical foundations of Reservoir Computing (RC) and Generalized Reservoir Computing (GRC), we study a simple archi- tecture that combines a fixed recurrent network with a trainable nonlinear output module. We evaluate this approach across tasks with varying memory demands, observation modalities, and action spaces. Surprisingly, frozen recurrent networks support recall over hundreds of steps and achieve competitive control performance across diverse POMDPs, while using less than half the number of trainable parameters required by their fully trainable counterparts. These results suggest that learning the recurrent memory module is not always necessary for solving POMDPs. Frozen recurrent networks therefore provide a simple, parameter-efficient, and sur- prisingly strong baseline for partially observable RL. Our source code is available at this https URL

---


### 124. [Golden Anchor for Video Generation](https://arxiv.org/abs/2610.13217)

**<font color=#1a73e8>作者：</font>** Jinyuan Xu, Shitong Shao, Lichen Bai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation supports digital content creation, with applications in virtual avatars, AI-driven filmmaking, interactive game engines, and world models. State-of-the-art systems achieve controllability primarily through image-to-video (I2V) generation, in which an injected anchor image determines the identity, composition, and style of the resulting video. In modern pipelines, this anchor is synthesized by a text-to-image (T2I) generator. This raises a largely overlooked question: Are images obtained directly from the T2I model truly suitable for current video models? Our analysis shows that anchor aesthetic and quality scores are weakly correlated with downstream video quality. The structure-and-texture score is negatively correlated with I2V video quality in both the visual and motion dimensions. Fine-tuning the T2I model on an image reward accordingly yields anchors with visibly denser structural and character detail: they score higher on image metrics, yet lower the video reward on every I2V model we test and change downstream motion unpredictably. We therefore introduce Golden Anchor Learning (GAL), to our knowledge the first framework for learning golden anchors by optimizing a T2I generator with downstream video feedback. GAL evaluates candidate anchors through the videos they induce under a frozen I2V model and converts video rewards into image-level preferences for DPO fine-tuning of the T2I generator. On all four I2V models, GAL raises the VBench average by $2.97\%$--$8.46\%$ over the untuned generator. The rendered clips also score higher under VideoReward-Overall, and their extracted frames under HPSv3 and UniPercept. GAL yields consistent motion gains across all four I2V models, as measured by a $5.62\%$--$38.24\%$ increase in VBench dynamic degree. Although GAL is trained only on HunyuanVideo-1.5 renders, these gains extend to the other three I2V models.

---


### 125. [Complexity-Calibrated Reconstruction Discrepancy for No-Reference Point Cloud Quality Assessment](https://arxiv.org/abs/2610.13219)

**<font color=#1a73e8>作者：</font>** Haocheng Wu, Xiangjie Sui, Xin Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The discrepancy induced by surface reconstruction in a distorted point cloud is jointly influenced by its intrinsic structural complexity and signal degradation. This observation motivates a referencefree point cloud quality assessment (PCQA) strategy that estimates and compensates for the complexity-induced component. We implement this strategy through successive reconstruction. Specifically, reconstructing the distorted point cloud produces an input-toreconstruction discrepancy that combines the effects of signal degradation and content complexity. Reapplying the reconstruction operator with stronger smoothing produces a discrepancy between successive reconstructions, which serves as a proxy for the complexityinduced component. This proxy is then used to calibrate the inputto-reconstruction discrepancy. We apply the same strategy to 3D geometry patches and their aligned 2D regions, enabling local comparison of the resulting discrepancies. The calibrated geometric and projected-view discrepancies are then fused into a final degradation score. For both branches, the discrepancies are measured using frozen pretrained perceptual representations. Our method does not require PCQA-specific training or fine-tuning. Experiments on three public databases show that the proposed method consistently outperforms most generic baselines and achieves performance comparable to several full-reference this http URL code is available at this https URL.

---


### 126. [Multi-Modal Graph Neural Network-Inspired Vessel Identification and Tracking for UAV-Based Maritime Surveillance](https://arxiv.org/abs/2610.13220)

**<font color=#1a73e8>作者：</font>** Chenjie Zhao, Jiangtian Nie, Jiawen Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The unmanned aerial vehicle (UAV)-based maritime surveillance is becoming an important part of maritime Internet of Things (IoT) and intelligent transportation systems. It provides a flexible and cost-effective way to large-scale maritime traffic monitoring. However, achieving robust situational awareness remains challenging in practical maritime environments. The main challenges arise from heterogeneous sensing modalities, adverse imaging conditions, and spatial misalignment caused by UAV motion. To address these problems, this paper proposes an airborne multi-modal graph learning-driven framework, termed AMGT, for vessel identification and tracking in UAV-assisted maritime IoT. Specifically, visible and infrared images are first aligned and fused through a multi-parameter perspective transformation model. This improves visual perception under low visibility and complex illumination conditions. Automatic identification system (AIS) messages are then temporally synchronized using interpolation and linear prediction. To detect small and oriented vessels, we develop a mixed-modality MAir-YOLOv8-OBB detector, followed by the MAir-SORT algorithm for stable vessel tracking. We further design a graph learning-driven association network to model temporal dynamics and spatial dependencies among vessels and between vessels and UAVs. A motion-aware coordinate unification (MCU) strategy is also introduced to reduce nonlinear misalignment caused by UAV motion. Experiments on the MAP-M2UAV50 dataset show that AMGT achieves high accuracy and efficiency. The results demonstrate its potential for UAV-assisted maritime IoT applications, including vessel monitoring, traffic situational awareness, and intelligent maritime transportation services. The dataset and code will be available at this https URL.

---


### 127. [Tensor-based Fusion of Multi-modal Data for Predicting Cancer Risk Levels](https://arxiv.org/abs/2610.13221)

**<font color=#1a73e8>作者：</font>** Ali Anaissi, Yuanzhe Jia, Qishun Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cancer diagnosis and treatment increasingly rely on multi-modal diagnostic technologies that generate high-dimensional datasets. Although these datasets are rich in pathological information, they pose considerable challenges in interpretation, dimensionality reduction, and clinical applicability. Conventional machine learning approaches often fail to extract meaningful cross-modal features, thereby limiting predictive accuracy in patient risk stratification. To address these limitations, this paper proposes an unsupervised machine learning framework that integrates feature extraction, tensor decomposition, and clustering to improve cancer risk prediction. The framework employs tensor decomposition to fuse heterogeneous genomic and clinical data, enabling the extraction of latent, biologically meaningful features that outperform unimodal feature sets. Multiple feature extraction strategies are investigated, and the resulting features are subsequently clustered using a range of clustering algorithms. Comparative evaluations based on internal and external metrics are then used to identify the most effective configurations. The framework is validated on LinkedOmics data comprising 11,158 patients across 32 cancer types. For patient risk stratification, clinically relevant attributes such as tumor purity, pathological stage, and survival outcomes serve as ground-truth indicators. Experimental results demonstrate the superiority of tSVD+GMM, which consistently outperforms other configurations across clinical benchmarks.

---


### 128. [Automated Detection and Encoding of Cartographic Signs in Historical Maps](https://arxiv.org/abs/2610.13224)

**<font color=#1a73e8>作者：</font>** Remi Petitpierre  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Symbols and icons in archival maps represent an expansive source of evidence for historical geography. In this paper, we present a two-stage framework for (1) detecting cartographic signs in historical maps and (2) generating interpretable sign embeddings that capture both semantics and stylistic variations. We also introduce CaSiDD, an open benchmark dataset spanning multiple sign categories and diverse cartographic styles, designed for generic sign detection. Using YOLOv10-X, we demonstrate the practicality of automated sign detection on historical maps. We then present strategies for creating contrasted, informative embeddings of cartographic signs. We approach embedding design systematically, maximizing expressiveness while suppressing digitization or background material confounders. Our final method, based on an adapted RADIOv4 backbone, effectively encodes both sign form and semantics, while producing interpretable representations. This work lays a foundation for scalable evidence extraction for the comparative study of map signs within cartographic culture and geohistorical research.

---


### 129. [ReSFlow: Rectifying Categorical Flows on Statistical Manifolds for One-Step Generation](https://arxiv.org/abs/2610.13225)

**<font color=#1a73e8>作者：</font>** Xiaohuan Jia, Renzhe Xu, Xiao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative modeling for discrete data has been significantly advanced by learning continuous vector fields on the statistical manifolds to transport simple priors to target discrete distributions. However, because these continuous-time flows are not constrained to follow geodesics on the statistical manifold, thereby requiring multi-step numerical integration for simulation and leading to substantial computational costs during inference. In this work, drawing inspiration from the "straight and fast" properties of Rectified Flow in continuous Euclidean space, we propose the Rectified Statistical Flow (ReSFlow) model, which enables one-step categorical generation on statistical manifolds by explicitly learning geodesic trajectories that adhere to the intrinsic Riemannian geometry. By rectifying the flow on the statistical manifold, we theoretically guarantee that trajectories between prior and target distributions approximate geodesics. This rectification significantly reduces the transport cost by aligning the learned trajectories directly along geodesics on the statistical manifold, allowing the model to map pure noise to target discrete data in a single step. Through extensive experiments on diverse real-world generative tasks, ranging from image and text to biological domains, we demonstrate ReSFlow's superior one-step generation quality, which truly embodies geodesically optimal and rapid categorical generation. Our code is available at this https URL.

---


### 130. [FPD-Drive: Future Policy Distillation for End-to-End Autonomous Driving](https://arxiv.org/abs/2610.13232)

**<font color=#1a73e8>作者：</font>** Li-Heng Chen, Qifeng Chen, Chengwei Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving models are typically trained on real-world driving logs, which record only the trajectory actually executed in each scene. This provides limited supervision for learning alternative valid behaviors. Multi-target supervision can mitigate this limitation, but broader trajectory coverage makes safe candidate selection more challenging. We propose FPD-Drive, an end-to-end planner that distills privileged future knowledge into a visual driving policy to improve both multi-trajectory supervision and safety selection. Specifically, we introduce Future-Privileged Multi-Target Distillation to transfer diverse, high-quality trajectory targets from a teacher with access to recorded future observations to the student. These targets extend supervision beyond the single recorded human trajectory. For candidate selection, we further introduce Safety-Aware Score Correction to correct ranking errors between nearby safe and unsafe candidates and raise underestimated safety scores of safe candidates. At deployment, the student requires neither future observations nor teacher inference. Our base model achieves 94.9 PDMS on NAVSIM v1 navtest and 55.9 EPDMS on NAVSIM v2 navhard. The scaled FPD-Drive-Pro improves these scores to 95.5 PDMS and 58.1 EPDMS, respectively, achieving SOTA performance among the compared methods on both benchmarks. Zero-shot closed-loop evaluation on HUGSIM further yields an HD-Score of 45.1 and RC of 55.3.

---


### 131. [Learning Schwarzschild Geodesic Motion with Lagrangian Neural Networks](https://arxiv.org/abs/2610.13234)

**<font color=#1a73e8>作者：</font>** Sukru Caglar, Sena Kalabalik, Abdullah Umut Hamzaogullari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lagrangian Neural Networks (LNNs) learn dynamics from trajectory data by parameterizing a scalar Lagrangian and deriving accelerations through the Euler--Lagrange equation, providing a variational inductive bias that improves physical consistency over purely data-driven models. LNNs have recently been extended to general relativistic settings, leaving Schwarzschild geodesics as an open challenge. Training on complex relativistic systems is hindered by the diversity of the dynamics, as well as numerical instabilities and the difficulty of adequately sampling physically relevant, diverse orbital regimes. We introduce two coordinated improvements: a decoupled position--velocity normalization scheme that independently rescales each coordinate and its time derivatives, reweighting acceleration targets to balance contributions across all channels; and an energy-constrained log-uniformly sampled dataset generation strategy informed by the innermost stable circular orbit (ISCO) structure. With these improvements, our model accurately reproduces perihelion precession and relativistic time dilation, conserves energy and angular momentum to within a few percent even after completing multiple orbits around the central mass and predicts orbital trajectories across eight orbital scenarios in close, medium, and far-field regimes. These results establish that LNNs, augmented with physically motivated normalization and sampling, can reliably learn geodesic dynamics in curved spacetime. Our work also represents the first successful training of LNNs on Schwarzschild geodesics and offers a promising direction for data-driven modeling of complex relativistic systems.

---


### 132. [How Reliable are AMR Parser Outputs? Uncertainty Estimation for AMR Parsing](https://arxiv.org/abs/2610.13236)

**<font color=#1a73e8>作者：</font>** Anuj Kumar, Shintaro Ozaki, Yamuna Prasad 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances have significantly improved the performance of Abstract Meaning Representation (AMR) parsers, yet determining when their outputs can be trusted remains largely unexplored. This work presents the first study of uncertainty estimation for AMR parsers in a black-box setting using top-k beam-search candidates. Uncertainty is estimated from pairwise candidate similarities and evaluated using the Prediction Rejection Ratio. This work characterises the relationship between parsing performance and uncertainty, evaluates the reliability of beam candidate distributions, analyses the effect of evaluation metrics on uncertainty assessment, and identifies parsers that provide the strongest balance between performance and reliability. Experimental results show the value of uncertainty estimation as a complementary dimension for evaluating AMR parsers.

---


### 133. [Jag: Direct Box Prediction for Efficient Visual Grounding](https://arxiv.org/abs/2610.13239)

**<font color=#1a73e8>作者：</font>** Xiuyuan Zhu, Ke Lu, Hao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding combines image--language understanding with geometric prediction, yet autoregressive multimodal models often express a box as a coordinate sequence. Sequential decoding adds computation to the multimodal processing needed for localization. Adapting these representations to box geometry offers a route to direct prediction. We present Jag, which adapts a compact pretrained multimodal model for direct continuous box prediction. A lightweight regression head reads the last valid input-token state, conditioned on the image and referring expression, and predicts all four box coordinates together. Geometric supervision jointly adapts the language backbone, visual merger, and regression head, allowing localization losses to shape both the multimodal representations and the coordinate mapping. Inference retains image--language processing and returns the box in one forward pass, without coordinate generation or text parsing. Across benchmarks, Jag consistently improves grounding accuracy over its base model across the observed target sizes and expression groups. Component ablation show that jointly adapting the representations and head substantially improves accuracy over training the head alone. Against existing specialized grounding models, it achieves competitive accuracy with lower single-request latency and GPU memory use. These results show how supervision tailored to the geometric answer can specialize a compact pretrained multimodal model for accurate grounding and efficient direct prediction. Project page: this https URL

---


### 134. [Deep Learning Approach for RealTime Contraction Detection in Laboring Dairy Cattle](https://arxiv.org/abs/2610.13242)

**<font color=#1a73e8>作者：</font>** Sebastian Puchala, Dominik Gronkiewicz, Marcin Gołębiewski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Currently, the animal production sector is undergoing rapid development of techniques that allow automatic monitoring of animal behaviour and health. This paper presents a computer vision-based approach for the automatic recognition of labor contractions in cows. During the course of the study, videos depicting 100 cow births were collected. From the obtained videos, 8500 cow contraction actions and about 25 000 non-contraction sequences were extracted which constituted the dataset. Leveraging image processing techniques and deep learning algorithms like Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs), our methodology extracts relevant features from video frames to detect and classify contractions. Our study demonstrates a high accuracy rate of over 95% in detecting labor contractions. This automated system has the potential to enhance productivity and animal welfare in the dairy industry by providing real-time monitoring and facilitating timely intervention during difficult calvings. The video demonstration of the system can be found at the following URL: this https URL

---


### 135. [Vision Transformers Learn Word Meaning from Images Alone](https://arxiv.org/abs/2610.13252)

**<font color=#1a73e8>作者：</font>** Anders Gjølbye, Sebastian Ray Mason, Stella Frank 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a vision model learn what words mean from pixels alone? We show that the two largest DINOv3 vision transformers organize words rendered in images by word meaning, despite being pretrained using self-supervision on images only, without paired captions, class labels, or other language supervision. We derive word representations from embedding differences between word images and matched controls, then test whether semantically related words are neighbors within each model's embedding space, while controlling for spelling similarity. We find that brand names in the same industry group together, as do nouns from the same semantic domain. Country-capital pairs exhibit consistent vector offsets, similarly to word embeddings trained on text. These word representations also align with the representations of the visual object categories they name. DINOv3-H and DINOv3-7B are, to our knowledge, the first self-supervised vision models to show substantial semantic structure for rendered words. Comparisons with text and speech encoders reveal shared structure among representations of the same words. Contrastive alignment with either encoder further strengthened DINOv3-H's word-level semantic structure, while leaving the other finetuned vision models largely unchanged. Image-only training can therefore teach vision models not just what words look like, but also how their meanings relate.

---


### 136. [Neural Surrogate Modeling of Ultrasonic Wave Propagation in Heterogeneous Media](https://arxiv.org/abs/2610.13258)

**<font color=#1a73e8>作者：</font>** Burla Nur Korkmaz, Petro Moilanen, Ari Salmi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogates provide computationally efficient auto-regressive modeling of wave propagation, enabling e.g. fast inverse solutions. Despite recent progress, the current surrogates are not yet sufficient for the needs of ultrasonic sensing, characterized by high frequency and heterogeneous propagation media. We show how methods building on Fourier Neural Operators (FNO) fail to capture essential signal features, such as reflections, whereas U-Net -based methods learn the wave fields well but lack the ability to transfer information across different spatial scales. We then propose a new surrogate that captures the best of the two worlds, by integrating FNOs and local-integral resampling into a U-Net architecture. We show it can be trained on limited data, and that the predictions are robust to input noise and work across spatial scales.

---


### 137. [Data-Adaptive Mahalanobis Metric Learning for Cross-Head Attention in Transformers](https://arxiv.org/abs/2610.13261)

**<font color=#1a73e8>作者：</font>** Zhenke Duan, Xin Li, Jiqun Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose Data-Adaptive Mahalanobis Cross-Head Attention (DAMCHA), a simple and effective attention mechanism that generalizes Multi-Head Attention (MHA) through the lens of metric learning. Standard MHA implicitly learns a static, head-wise Euclidean similarity corresponding to the diagonal blocks of a unified cross-head metric matrix, discarding all off-diagonal interactions across heads. DAMCHA addresses this limitation via two key innovations. First, it learns the full cross-head metric matrix, inducing a Mahalanobis-like similarity that explicitly captures inter-head interactions beyond the restricted block-diagonal structure of MHA. Second, it parameterizes the metric matrix as an input-dependent function, enabling the attention geometry to dynamically adapt to the intrinsic manifold structure of the data rather than remaining fixed after training. We further introduce principled regularization strategies, most notably stack-wise parameter sharing, to ensure computational efficiency and stable optimization. DAMCHA serves as a drop-in replacement for MHA and its variants in various Transformer architectures, delivering superior expressive power and learning performance with comparable or reduced computational overhead. Extensive experiments demonstrate that DAMCHA-based Transformers consistently outperform competing baselines across a range of benchmark tasks. Code is available at this https URL.

---


### 138. [QCLR: A Plug-in Robustification Module via Quantization for Contrastive Learning in Self-Supervised Skeleton-Based Human Action Recognition](https://arxiv.org/abs/2610.13281)

**<font color=#1a73e8>作者：</font>** Nanzhu Chen, Feixiang He, Yunfeng Diao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based human action recognition has gained increasing attention due to the stability of skeleton data across diverse environments and advances in motion capture technologies. Following the success of supervised learning approaches, self-supervised learning approaches, particularly contrastive learning ones, have achieved impressive performance. However, they remain vulnerable to adversarial attacks. In this work, we propose a plug-in robustification module via quantization for contrastive learning in self-supervised skeleton-based human action recognition (QCLR), which enhances the robustness of representations against adversarial attacks while preserving their representational capability. Specifically, we employ a dual-level quantization scheme across the encoding pipeline, which breaks the gradient propagation and absorbs small adversarial perturbations within the quantization bins. To mitigate the impact of inevitable quantization error, we further design an attention-guided multi-faceted quantization strategy to maintain the representation quality. Experiments on several benchmark datasets demonstrate that integrating QCLR into a progressive lineage of mainstream contrastive learning models substantially improves robustness against both gradient-based white-box and gradient-free black-box adversarial attacks, while preserving highly competitive classification accuracy.

---


### 139. [Do Prompt Optimizers Break Requirements They Are Not Scored On? A Preregistered Study](https://arxiv.org/abs/2610.13287)

**<font color=#1a73e8>作者：</font>** Sangdo Han, Moonsoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt optimizers rewrite a prompt to raise one target metric, but prompts also state requirements the metric does not score, such as an output format, citations, or abstention. In a preregistered study, we run GEPA, MIPROv2, and TextGrad on HotpotQA, SQuAD 2.0, and IFEval and count per-item violations of unscored requirements with deterministic checks. By the preregistered criterion, all three optimizers produce regressions, substantially on HotpotQA, where net regression in citation validity reaches 10.7 to 41.6 points while exact match rises by 21 to 34 points. A post-hoc decomposition changes this reading. The optimized prompts elicit reasoning before the required JSON object, and under the 200-token output cap used throughout, 13.9% to 47.0% of responses end before any answer appears. Among parseable outputs, net regression is within 3 points of zero. With a 1,024-token cap, extraction failures disappear, content regression stays below 1 point, and exact match rises further. Two simple gates fail the preregistered criterion. The side effect is narrower than hypothesized: optimized prompts are more accurate and break an explicit output contract, and a lenient target metric does not show the cost.

---


### 140. [Recovering Irreducible Three-Body Interactions with Lagrangian Neural Networks](https://arxiv.org/abs/2610.13292)

**<font color=#1a73e8>作者：</font>** Sena Kalabalik, Sukru Caglar, Abdullah Umut Hamzaogullari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lagrangian Neural Networks (LNNs) learn mechanical systems from trajectory data by parameterizing a scalar Lagrangian and deriving the dynamics through the Euler-Lagrange equations, biasing the model toward motion that respects the variational structure of mechanics. The interactions studied so far have been pairwise-additive, leaving open whether LNNs can recover an irreducible many-body interaction from motion alone. We address this using the Axilrod-Teller triple-dipole interaction, the leading three-body dispersion term, whose dependence on the collective geometry of three particles cannot be represented by any sum of pairwise terms. We prescribe the kinetic energy exactly and learn only the potential, as a function of interparticle distances and angles. Combined with a signal-aware sampling strategy that concentrates training data where the three-body signal is strongest while preserving broad coverage of configuration space, this recovers the interaction from accelerations alone. The learned potential reproduces the radial scaling, angular dependence, and characteristic sign reversal of the Axilrod-Teller interaction, and generates stable trajectories. Embedding it within a pairwise Lennard-Jones potential lets us examine its observability: the three-body term is recovered once its dynamical signature exceeds the residual modeling error, which it does cleanly at amplified coupling but not at the coupling of a real noble gas, bracketing the transition between the two. Finally, symbolic regression on the trained potential, with no assumed functional form, returns the Axilrod-Teller expression with angular numerator, radial law, and coupling constant intact. An LNN with domain-specific structure can thus recover an irreducible three-body interaction from trajectories as a closed-form law, pointing toward learning interaction laws whose structure is not known a priori.

---


### 141. [Decoding Register Tokens Preserves Global Scene Details](https://arxiv.org/abs/2610.13299)

**<font color=#1a73e8>作者：</font>** David Jacob Drexlin, Julius Hense, Jonas Dippel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision transformers learn structured image representations spanning spatial patch tokens and non-spatial tokens. Recent analyses suggest that non-spatial register tokens encode global scene properties such as illumination, blur, and style. Yet patch-based image decoders discard these outputs, leaving the decoder to recover image appearance from patches alone. We investigate whether retaining register features improves decoding when the complete spatial patch representation is already available. We study this question using representation autoencoders (RAEs) with frozen register-equipped encoders. Our decoder processes four register tokens together with all patch tokens through joint self-attention. Appearance probes, paired reconstruction-error analysis, and fixed-decoder register substitutions examine which global image properties are accessible from registers and how their values affect reconstructed pixels. For generation, we train a multi-head attention pooling (MHAP) predictor to recover register features from sampled patches, keeping the pretrained diffusion model and its samples unchanged. On ImageNet-1K, our ViT-B decoders achieve mean reconstruction FIDs of 0.472 with DINOv2 and 0.442 with DINOv3, reductions of 9.5% and 5.2% relative to their respective patch-only baselines. The corresponding PSNRs are 19.73 and 20.54 dB. For generation, our DINOv2 models achieve a mean FID of 1.641, 9.8% below the patch-only baseline on identical sampled patches.

---


### 142. [Sonic-AMG: Streaming Human Motion Generation from Spatial Audio](https://arxiv.org/abs/2610.13300)

**<font color=#1a73e8>作者：</font>** Jingcheng Ni, Zekun Li, Zhiyang Dou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling human reactions to spatial audio requires understanding both what is heard and where it comes from. Prior work generates motion offline from complete acoustic and spatial input sequences. Humans, however, react to sounds without knowing what they will hear next. We present Sonic-AMG, to our knowledge the first framework for streaming human motion generation from spatial audio. The model encodes acoustic content and body-relative source geometry as separate tokens. Conditioned on these tokens, a causal transformer with a flow head generates continuous motion latents, from which a causal decoder reconstructs motion segments. Standard teacher-forced training derives motion histories and body-relative source locations from ground-truth motion, whereas streaming inference relies on generated motion for both, resulting in a training-inference mismatch. To reduce this history discrepancy, we introduce rehearsal training, which combines full-sequence teacher-forced supervision with supervised prediction along short autoregressive self-rollouts. To keep spatial conditioning consistent with generated motion, we propose spatial feedback, which recomputes body-relative source locations from generated root poses during both rehearsal training and inference. On SAM, Sonic-AMG achieves state-of-the-art FID and R-precision. It further supports real-time online generation of coherent reactions across sound events and source locations. Project page: this https URL.

---


### 143. [PAGE: Parts-Aware Guidance for Co-Speech Gesture Portrait Video Generation](https://arxiv.org/abs/2610.13301)

**<font color=#1a73e8>作者：</font>** Yabiao Wang, Jiafu Wu, Yicheng Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-speech gesture video generation aims to synthesize realistic, audio-driven portrait videos from a single reference image and a speech signal. Despite advances in visual quality, diffusion-based approaches still suffer from degraded local details and imperfect audio-visual alignment. We present PAGE (Parts-Aware GuidancE), a general, backbone-agnostic optimization framework for diffusion-based generation that enhances local spatial fidelity and global audio-visual consistency at both the training-objective and denoising-trajectory levels. During training, we propose Parts-Specific Reweighting (PSR), which adaptively increases supervision in semantically important regions such as lips, eyes, and hands, improving visual fidelity in perceptually critical areas. During inference, we introduce Consistency Classifier Guidance (CCG), an audio-conditioned latent classifier that identifies and corrects audio-visual inconsistencies in the generated video. We further design Differential Guidance (DG), an efficient inference strategy that refines facial and body motion separately while avoiding cross-region interference. To enable large-scale evaluation, we construct the Chinese Announcer Speech (CAS) dataset, the first comprehensive Chinese benchmark for co-speech gesture portrait video generation. Compared with the widely used PATS dataset, CAS includes substantially more identities, video clips, and scene diversity. Extensive experiments on both PATS and CAS demonstrate that PAGE achieves state-of-the-art performance in perceptual quality, gesture diversity, and audio-visual alignment. Project page: this https URL.

---


### 144. [DAG Structure Learning with Node-Varying Heavy-Tailed Disturbances](https://arxiv.org/abs/2610.13304)

**<font color=#1a73e8>作者：</font>** Robin Francis, Sundeep Prabhakar Chepuri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DAG structures can be learned from observations by incorporating acyclicity via smooth constraints, such as DAGMA's log-determinant function. Typically, observations and the underlying DAG are related through linear structural equation models, with Gaussianity assumption on the disturbances at each node. Extending DAG learning methods that account for scale and tail behavior of disturbances that vary across nodes remains a challenge. We propose a node-varying Student-$t$ DAGMA that jointly estimates the graph structure, node-specific disturbance scales, and the degrees-of-freedom parameter. A Gaussian scale-mixture representation yields an iteratively reweighted formulation that down-weights large standardized residuals. Building on existing results, we also establish identifiability of the graph and disturbance parameters. Synthetic experiments demonstrate improved structural recovery under heterogeneous heavy-tailed disturbances, and experiments on real finance data show that the proposed method yields lower test negative log-likelihood than the evaluated baselines.

---


### 145. [MORAD: Reinforcement Learning with Multi-Objective Rewards for RNA Inverse Design](https://arxiv.org/abs/2610.13305)

**<font color=#1a73e8>作者：</font>** Jixin Tang, Ji Guo, Jun Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce MORAD, an online reinforcement learning framework for backbone-conditioned RNA diffusion models that trains a single shared policy across diverse target backbones. Structure-conditioned RNA inverse design seeks nucleotide sequences compatible with a target three-dimensional backbone, yet existing reinforcement learning approaches either optimize a separate policy for each target backbone or rely on offline preference optimization, leaving online post-training of a reusable backbone-conditioned model largely unexplored. MORAD combines backbone-conditioned group sampling, group-relative reward normalization, and a forward-process diffusion objective. Beyond existing RL rewards that primarily target tertiary structural quality, MORAD jointly optimizes six measurements spanning tertiary geometry, base pairing, ensemble behavior, and sequence composition. To aggregate these heterogeneous objectives despite differences in scale and optimization direction, MORAD maps each measurement to a bounded desirability score and combines them with a weighted geometric mean. Compared with a tertiary-structure-only reward, this multi-objective formulation improves 10 of the 11 evaluation metrics that have a preferred direction. Applied to pretrained RIDE, MORAD improves GDT-TS by 16.0% (from 0.3300 to 0.3827) and pairing MCC by 19.4% (from 0.6110 to 0.7295), while reducing normalized ensemble defect by 27.5% (from 0.3906 to 0.2830). On the test set, MORAD outperforms RiboDiffusion, gRNAde, and RDesign across tertiary structural accuracy, secondary-structure pairing, and thermodynamic quality, establishing a new state of the art in structure-conditioned RNA inverse design.

---


### 146. [Structure-Aware Numerical Stabilization for Half-Precision Proximal Policy Optimization](https://arxiv.org/abs/2610.13306)

**<font color=#1a73e8>作者：</font>** Linxuan Wu, Liang Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local online training on resource-constrained platforms requires low computational and training-state overhead. We study the numerical stability and computational efficiency of half-precision proximal policy optimization (PPO) on commodity GPUs. Directly converting PPO training to FP16 is unreliable because numerical errors feed back through policy updates and subsequent data collection, while PPO repeatedly compares a current policy with a fixed behavior policy. We propose PPO-FP16 with three structure-aware modules. Global scalar protection stabilizes statistics shared across a minibatch or parameter update. Policy-change residual protection extracts and preserves small differences between the current and behavior policies. Efficient persistent-update protection stabilizes optimizer state and parameter writeback while reducing state storage. These changes preserve the PPO objective, hyperparameters, and training budget. Across six continuous-control tasks and five seeds, PPO-FP16 achieves the lowest mean return-AUC rank (1.90) among the four methods and ranks first in 17 of 30 environment-seed comparisons. Eight of nine performance configurations yield PPO update speedups ranging from 1.16 to 2.03 times. Relative to Full FP32 Adam, optimizer-state memory is reduced by 71.7 to 74.9 percent, and peak allocated GPU memory is reduced by up to 44.5 percent. The results show that protecting a small set of structurally important quantities can deliver stable, efficient FP16 PPO without retuning.

---


### 147. [Sustainable Cloud-Fog-Edge Systems for Smart Buildings: Algorithmic Adaptation under Memory Constraints and Dynamic Orchestration Strategies](https://arxiv.org/abs/2610.13307)

**<font color=#1a73e8>作者：</font>** Mamadou Sow, Christophe Cerin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The escalating environmental footprint of the Information and Communication Technol- ogy (ICT) sectorwith global Data Center electric- ity usage potentially reaching 3% by 2030 and the imperative for real-time responsiveness in smart buildings demand a foundational shift towards Edge Computing. This article proposes a holis- tic architectural and algorithmic approach for cre- ating autonomous, resilient, and privacy-preserving learning systems within smart buildings, advancing the core concept of the building itself as the data center. Our contributions, demonstrating originality compared to conventional centralized systems, are structured around three main pillars: 1) Validation of resilient data acquisition chains using the af- fordable Arduino ecosystem (Uno R4 WiFi/BME280) and secure persistence solutions including centralized archiving (Node-RED/MySQL) and secure remote transfer (Python/rsync/SSH). 2). The proposal of a lightweight, KOptim orchestration framework, inter- operable with the FIWARE standard, for the dynamic management of Service Level Agreements (SLA). 3) The adaptation and experimental valida- tion of the Generalized Hebbian Algorithm (GHA) for Principal Component Analysis (PCA) on low- power microcontrollers,We introduce and compare an iterative learning strategy using data buffers, featuring sorting and explicit preservation of extreme samples to maintain diversity. Experimental results on the high-dimensional Tour Perret sensor data confirm that this novel method, despite introducing a necessary temporal complexity of O(W log W ) due to sorting, achieves convergence and final result quality that is visually equivalent to processing the entire dataset in full memory, reliably identifying two distinct operational states.

---


### 148. [NovaSplat: Model-Free 6D Object Pose Estimation via 3D Gaussian Splatting Onboarding and Refinement](https://arxiv.org/abs/2610.13309)

**<font color=#1a73e8>作者：</font>** Georgios Floros, Evangelos Sartinas, Orestis Vangelis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 6D pose estimation of novel objects without CAD models remains an open challenge: model-free methods must build the object representation from scratch during onboarding and have long trailed their model-based counterparts. We present NovaSplat, a model-free pipeline that closes this gap. From a short smartphone video captured at onboarding, we train a 3D Gaussian Splatting (3DGS) model that serves both as a template source for detection and coarse pose estimation and as a differentiable backbone for pose refinement. Our refiner optimizes the object-to-camera pose with combined photometric and geometric losses under a continuous rotation parametrization free of gradient singularities. On a household-object benchmark, NovaSplat surpasses all model-based methods. On a challenging industrial benchmark with textureless and specular surfaces, it outperforms all model-free competitors while substantially narrowing the gap to model-based ones. We further introduce NovaSplat-Lite, an inference variant that is $3.1\times$ faster at negligible accuracy cost. Code will be made available at \href{this https URL}{this https URL}.

---


### 149. [Quantization-Tolerant Gradient Auditing for Active Inference-Attack Detection in Federated Learning](https://arxiv.org/abs/2610.13311)

**<font color=#1a73e8>作者：</font>** Michael Kuehne-Schlinkert  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Inside a federated learning system a participant can quietly study the shared model and learn about others' private data. The usual defense, differential privacy, often adds so much noise that the model is no longer worth training. In cross-silo FL, where participants are a few accountable organizations and the server is trusted, we ask whether the server can instead interrogate clients. Each round it sends a secret challenge batch and asks every client to return a checksum of the gradient that batch induces, together with a timing. A client that mutated the model state, as an active generative-adversarial-network discriminator attacker does, returns a wrong checksum. We make this checksum robust to benign cross-platform floating-point non-determinism with a quantized fingerprint compared under a small tolerance. It flags two distinct active attacks at a true-positive rate of $1.0$ with no false positives on the checksum axis, stable across the fingerprint's parameters and up to $50$ clients at malicious ratios to $40\%$, for $32\,\mathrm{ms}$ of server work and $4.35\,\mathrm{kB}$ per response. Against a purely passive attacker the only signal is timing, and it is not robust: a cohort-relative test detects only in low-jitter conditions while a false-positive-free per-client baseline is blind, so no configuration delivers both. An attacker that answers the challenge on an untouched copy of the model while tampering with a replica evades the audit entirely. Therefore the checksum is a reliable in-band signal against attackers that do not decouple the audited computation from the attacked one, and it composes with differential privacy, whose accuracy cost we quantify on Texas100, rather than replacing it.

---


### 150. [ThinkDrag: Semantic Drag-Based Image Editing with Visual Reasoning](https://arxiv.org/abs/2610.13316)

**<font color=#1a73e8>作者：</font>** Armando Fortes, Tianyi Wei, Chindanai Trakantannarong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Drag-based image editing provides an intuitive interface for spatially controlled image manipulation by allowing users to specify handle and target points. Existing methods have made substantial progress through optimization-based, one-step, and feed-forward formulations, but they often interpret drag instructions as geometric displacements. This limits their effectiveness when the desired edit depends on interpreting image content and inferring a plausible semantic transformation from sparse point constraints. We introduce ThinkDrag, a unified multimodal framework for drag-based image editing with visual reasoning. ThinkDrag is trained to associate point constraints with meaningful object- and scene-level transformations, and can optionally produce an explicit reasoning trace that interprets the intended edit before image generation. This reasoning trace improves interpretability, particularly for ambiguous drags. Drag Endpoint Markers, motivated by an analysis of cross-image attention, provide an explicit correspondence signal that grounds each drag in image space. To support this framework, we construct a supervised dataset of semantic drag transformations paired with reasoning traces and introduce DragBench++, a benchmark targeting challenging drag-based editing scenarios with reference edit solutions. Experiments show that ThinkDrag achieves state-of-the-art performance, improving generation quality and plausibility while maintaining competitive point-following precision.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-244](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
