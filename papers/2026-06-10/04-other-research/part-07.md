# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

---

### 301. [Continuous Language Diffusion as a Decoder-Interface Problem](https://arxiv.org/abs/2606.08810)

**<font color=#1a73e8>作者：</font>** Zhicheng Du, Lan Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gaussian-corrupted sentence embeddings have no direct linguistic interpretation, yet continuous diffusion language models can generate fluent text from them. We study this puzzle through Embedded Language Flows (ELF) and identify a decoder-basin mechanism: denoising succeeds when trajectories reach regions where the native decoder can read stable tokens. We introduce a diagnostic protocol for denoisability, semantic recoverability, order sensitivity, decoder compatibility, and trajectory reliability. It exposes failures hidden by scalar metrics: low mean-squared error can discard linguistic content, low perplexity can reflect low-entropy collapse, and clean latent reconstruction can coexist with a narrow decoder basin. A decoder-margin bound explains why token recovery depends on margin and local decoder sensitivity, not latent error alone. Auditing public ELF checkpoints reveals an interface phase diagram: early predictions are weakly readable, mid-trajectory disagreement marks a competition region, and late predictions enter a high-margin final-token basin. Once inside, token realization is surprisingly simple on generated ELF states: frozen T5 token-embedding lookup recovers $93$--$96\%$ of native decoder decisions, and a single linear readout reaches $97.9\%$ agreement at 32k samples, leaving about a 1.1 perplexity gap in a structured residual tail. A conservative margin gate exits $17$--$27\%$ earlier in denoising steps under an explicit diagnostic monitor. Boundary checks on LangFlow, BitstreamDiffusion, and the Continuous Latent Diffusion Language Model (Cola-DLM) show that the same interface questions remain meaningful when the state object and decoder change. Continuous and latent diffusion language models should therefore be evaluated as representation-decoder systems.

---


### 302. [Momentum for Reasoning: Dense Intrinsic Signals in Policy Optimization](https://arxiv.org/abs/2606.08815)

**<font color=#1a73e8>作者：</font>** Hao Chen, Zhanming Shen, Liyao Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has emerged as a powerful paradigm for eliciting long-chain reasoning in large language models. However, existing methods based on Group Relative Policy Optimization (GRPO) rely on a binary outcome reward, which induces two structural failure modes: Zero-Advantage Collapse, in which all rollouts in a group share the same outcome and the gradient vanishes, and Hallucinated Certainty, in which the model becomes increasingly confident on incorrect rollouts late in training. We address both modes by densifying the reward with intrinsic signals computed entirely from the policy's own conditional probabilities, and propose ISPO (Intrinsic Signal Policy Optimization, which combines a sequence-level signal measuring how informative the thinking trajectory is for the final answer, with a token-level directional reward whose hallucinated-certainty hinge penalizes confidently-wrong predictions at critical decision tokens. Across three base models and five mathematical reasoning benchmarks, ISPO consistently outperforms competitive baselines, with the largest gains on the hardest benchmarks where zero-advantage collapse is most frequent, and training-dynamics diagnostics confirm that both failure modes are decreased.

---


### 303. [Classifying galaxies in the Galaxy10 DECals dataset using Inception and Residual CNNs](https://arxiv.org/abs/2606.08826)

**<font color=#1a73e8>作者：</font>** Lanz Anthonee A. Lagman, Prospero C. Naval Jr, Reinabelle C. Reyes  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image data regarding galactic morphology is expected to increase both in quantity and quality for the next foreseeable years; thus it is important to explore which deep learning architectures adapted for image classification tasks are cost-effective. Residual and Inception networks are ideal for exploring classification convolutional neural networks (CNNs) due to their computational efficiency, achieved through techniques such as residual connections and parallelized inception modules, enabling deeper networks without excessively increasing computational complexity. In this work, we analyze the performance of ResNet101 and InceptionV4 on a spatially-augmented Galaxy10 DECals dataset. Retaining the ten-class classification of galaxies, we modify the image count of each class. We find that ResNet101 and InceptionV4 models achieved accuracies of $\sim$ 90%, comparable with reported performance in the literature. In terms of performance metrics, ResNet101 is superior to InceptionV4. Our results indicate that either of these CNN architectures could serve as a robust foundation for specialized pipelines for classification of galaxy images from upcoming surveys.

---


### 304. [Instrumental convergence and power-seeking](https://arxiv.org/abs/2606.08832)

**<font color=#1a73e8>作者：</font>** David Thorstad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent years have seen increasing concern that artificial intelligence may soon pose an existential risk to humanity. One leading ground for concern is that artificial agents may be power-seeking, aiming to acquire power and in the process disempowering humanity. I show how the argument from power-seeking rests on a strong version of a claim known as the instrumental convergence thesis. I explore leading defenses of the instrumental convergence thesis and argue that none establishes the thesis in a strong enough form to ground the argument from power-seeking. I discuss implications for longtermism, the governance of artificial intelligence, and the methodology of studying risks posed by artificial agents.

---


### 305. [CSFlow: Aligning Flow Matching with Human Contrast Sensitivity](https://arxiv.org/abs/2606.08833)

**<font color=#1a73e8>作者：</font>** Malgorzata Galinska, Bart Pogodzinski, Jan Eric Lenssen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Contrast Sensitive Flow (CSFlow), a weighting scheme that connects the human eye's Contrast Sensitivity Function (CSF) to the iterative denoising steps of flow matching. Because real-world images concentrate signal at low spatial frequencies, these components reach high signal-to-noise ratio earlier during continuous diffusion than high-frequency components. When generating images with diffusion or flow matching models, this induces a soft autoregressive structure in Fourier space, where coarse image content stabilizes before fine detail. Meanwhile, the human visual system is unequally sensitive to spatial frequencies: very low and very high frequencies require significantly higher contrast to be perceived. We for the first time merge these observations through two contributions: (1) a metric that estimates which frequencies are generated at each reverse flow interval and (2) timestep weights obtained by aligning the frequencies generated at each noise level with human contrast sensitivity. We validate our contributions experimentally showing that these weights can improve generative performance by lowering FID by 4.7%, increasing Inception Score by 2.2% and improving GenEval scores by 2.5% using inference-only timestep modification or short fine-tuning. Qualitatively, we find that our CSFlow weights lead to better visual realism and less cartoonish appearance of generated images.

---


### 306. [ZIPP:Zero-shot Image Personalization from Personas](https://arxiv.org/abs/2606.08841)

**<font color=#1a73e8>作者：</font>** Harini SI, Somesh Singh, Yaman Kumar Singla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models are increasingly deployed in open-ended creative contexts, yet their outputs remain impersonal, optimized for aggregate aesthetics rather than individual taste. Human preferences are pluralistic: one user favoring muted, nostalgic portraits may prefer vibrant street photography, while another gravitates toward dreamy film aesthetics. Existing methods require dense interaction histories or per-user fine-tuning, failing in cold-start settings and collapsing context-dependent preferences into a static representation. We introduce zero-shot image personalization from personas (ZIPP), which conditions image generation on natural-language personas (concise descriptors of a user's identity and aesthetic sensibilities) without any user-specific data or weight updates. ZIPP uses an LLM to rewrite prompts from the perspective of a given persona, steering diffusion models toward personalized outputs. To mine personas at scale, we train an inductive Graph Attention Network over a 22M-user Reddit interaction graph with dual contrastive objectives aligning graph structure with visual behavior, then verbalize learned representations into natural-language personas via an MLLM. We introduce ZIPBench, the first zero-shot personalization benchmark with 1.5K users, graph-mined personas, and 40K generated images. Across four benchmarks and 14 LLMs spanning five model families, persona conditioning yields consistent gains (13-20%), with frontier models benefiting most. In the few-shot setting, ZIPP matches or exceeds fine-tuned baselines trained on 100+ examples per user. ZIPP achieves the lowest preference distributional divergence (CMMD 0.16 vs. 0.55), and IPF-normalized demographic evaluation shows it substantially reduces subpopulation bias present in existing methods. Human evaluation confirms a 79% win rate over generic generation and 58-65% over all fine-tuned baselines.

---


### 307. [Geometry-Aware Fisheye-LiDAR Fusion for Robust 3D Object Detection in Low-Overlap Setups](https://arxiv.org/abs/2606.08844)

**<font color=#1a73e8>作者：</font>** Xiangzhong Liu, Xihao Wang, Hao Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As autonomous systems expand from capital-intensive robotaxis to cost-sensitive logistics, sensor configurations are increasingly optimized for coverage-per-cost. A prevalent sparse-view setup utilizes dual-fisheye cameras with a roof-mounted LiDAR, introducing severe geometric challenges: extreme radial distortion, minimal overlap, and misalignment between spherical projections and rectilinear grids. BEV fusion algorithms typically force image and point cloud modalities into unified Cartesian grids early in the pipeline, causing significant feature distortion and information loss for wide-view fisheye cameras. To address this, we propose a Geometry-Aware Hybrid Fusion (GA-HF) framework that explicitly accounts for fisheye geometry and BEV feature distortion, where fisheye features are lifted into a polar BEV grid via a Distortion-Aware Lift-Splat-Shoot (LSS) module to preserve native angular density, while LiDAR features are processed in native Cartesian space for metric fidelity of bounding box regression. To bridge these heterogeneous streams, we introduce a Dual-Attention Warping Correction module that applies spatial and channel attention to the warped camera features before fusion, explicitly suppressing artifacts in low-quality peripheral regions while enhancing high-quality semantic cues. GA-HF is evaluated on three benchmarks: KITTI-360, Dur360BEV, and Fisheye3DOD datasets. To the best of our knowledge, it is the first approach to explore LiDAR-fisheye camera fusion. On KITTI-360, GA-HF improves NDS by 4.2% over Cartesian baselines; on Dur360BEV, it surpasses both LiDAR-only and BEVFusion, while significantly reducing orientation error despite the geometric distortions; on Fisheye3DOD, it attains the highest detection score among all fusion methods.

---


### 308. [A Resilience-as-a-Service assessment framework for coordinated disruption response in interdependent urban transit systems](https://arxiv.org/abs/2606.08849)

**<font color=#1a73e8>作者：</font>** Sara Jaber, S. M. Hassan Mahdavi, Neila Bhouri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban public transport disruptions require rapid response strategies, yet existing studies rarely provide a decision support framework to compare alternative disruption response solutions using a common set of dynamic, passenger, operator, and environment oriented indicators. This paper proposes a KPI-driven, time-indexed framework to assess the resilience of disruption response solutions in urban transit systems. The framework combines an optimization model with a behavioral evaluation in agent-based simulation. It also underlays the secondary service degradation induced on helper lines when in-service vehicles are withdrawn to support the disrupted corridor. Rather than treating resilience as a single score, it evaluates complementary dimensions including vulnerability, adaptability, robustness, resilience loss, responsiveness, cost-based performance, emissions, and equity. The framework is implemented for the RER B transit line in the Ile-de-France (Paris) network. Results show that the coordinated strategy provides the most balanced resilience profile, combining high service continuity with lower total disruption cost than single mode alternatives, while also improving equity and maintaining competitive environmental performance. Sensitivity analysis further identifies the disruption conditions under which coordinated multimodal response is most valuable.

---


### 309. [Intrinsic Selection and Particle Resampling for Inference-Time Scaling Beyond Domain Verifiability](https://arxiv.org/abs/2606.08850)

**<font color=#1a73e8>作者：</font>** Giorgio Giannone, Mustafa Eyceoz, Shabana Baig 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-Time Scaling (ITS) has largely succeeded in verifiable domains like math and coding, where cheap verification enables scalable output selection. However, extending ITS to tasks prone to systematic failure - driven by faulty initial assumptions or unmet multidimensional constraints - typically relies on costly external solvers or brittle, model-based verifiers. Our key insight is that the intrinsic statistics of parallel sample sets, specifically length-adjusted tail entropy, provide a robust discriminative signal for solution quality without access to ground truth. Crucially, these statistics serve as a difficulty gate for adaptive compute allocation, dynamically routing problems across scaling regimes. First, Intrinsic Selection (iS) ranks candidates post-hoc, matching consensus-based algorithms across three domains and improving engineering design selection by 20% over pass@1 baselines. Second, Intrinsic Particle Filtering (iPF) generalizes this to step-level resampling, guiding generation toward high-confidence reasoning trajectories to improve pass@1 by 6.1 points on average on hard math problems. Finally, Particle Distillation (dPF) injects privileged guidance via early logit blending and KL-guided resampling, steering generation past systematic reasoning errors to satisfy expert rubrics, yielding up to 26.5% gains on complex clinical responses. Our pipeline applies seamlessly across broad-purpose, domain-specialized, and multimodal architectures, successfully extending ITS to open-ended domains without requiring trained reward models or exact ground-truth verification.

---


### 310. [sGPO: Trading Inference FLOPs for Training Efficiency in RLVR](https://arxiv.org/abs/2606.08854)

**<font color=#1a73e8>作者：</font>** Shivchander Sudalairaj, Kai Xu, Akash Srivastava 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard Reinforcement Learning with Verifiable Rewards (RLVR) training allocates a fixed rollout budget to every query, without regard for what each query's difficulty means for the current policy. This leads to two symmetric failure modes: easy queries produce near-zero advantage because the policy already solves them, while unsolvable queries produce no signal because the policy never solves them. Both regimes waste training FLOPs without contributing to a learning gradient. We introduce sorted Group Policy Optimization (sGPO), a compute-efficient strategy that trades a small budget of inference FLOPs for a large reduction in wasted training FLOPs. The key insight is that cheap inference compute can serve as a single offline proxy for query difficulty. By generating a small batch of parallel samples per query under the initial policy, we obtain a model-aware empirical success rate. This motivates setting the training rollout group size to the inverse of this success rate, a practical rule that maximizes sample efficiency by extracting the most advantage per generated rollout. This single profiling pass simultaneously drives data filtering (removing trivial queries and sub-sampling unsolvable ones), adaptive group size allocation, and curriculum construction (scheduling queries from easy to hard). sGPO matches or exceeds baseline performance while reducing total training compute by a factor of three, with the upfront inference profiling cost included.

---


### 311. [Hybrid E-Assessment in Higher Education: Semi-Automated Grading of Paper-Based Written Examinations](https://arxiv.org/abs/2606.08855)

**<font color=#1a73e8>作者：</font>** Hartwig Grabowski, Michael Canz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper examines the limitations of fully digital and partially digital e-assessment approaches in summative examinations in higher education. The analysis focuses on the didactic narrowing caused by closed question formats and on organizational, technical, and legal constraints that become particularly relevant in large student cohorts. As an alternative, the paper proposes a hybrid e-assessment approach that retains paper-based, problem-oriented examination tasks while enabling semi-automated grading. Assessment-relevant intermediate results are encoded in a structured answer format, entered by students by hand, and subsequently captured from table fields. The central technical bottleneck is reliable recognition of handwritten characters under realistic examination conditions. Recent vision-capable large language models, combined with a two-pass validation principle and comparison against a solution key, can reduce misclassifications and thereby improve the validity, fairness, and scalability of summative assessment.

---


### 312. [PaperMentor: A Human-Centered Multi-Agent Writing Tutor for AI Research Papers on Overleaf](https://arxiv.org/abs/2606.08857)

**<font color=#1a73e8>作者：</font>** Jiarui Liu, Terry Jingchen Zhang, Ryan Faulkner 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expert writing feedback from experienced researchers is critical for early-career scholars to improve their manuscripts, yet high-quality feedback often remains scarce because reviewing research papers is labor-intensive. Emerging AI-powered writing assistants largely focus on grammar fixes or simulating peer review with final scores, yet they fall short of providing concrete, actionable suggestions that help students improve their papers during drafting. We present PaperMentor, a human-centered writing assistant system that delivers actionable suggestions as Overleaf-native inline comments while leaving the actual writing entirely to human authors. PaperMentor integrates an expert skill library carefully curated from established researchers' writing advice with 12 specialized agents covering different aspects of paper writing, such as formatting compliance, phrasing accuracy, and terminology consistency. In a user study (n=14), 90.6% of the generated comments were rated actionable and 67.5% were rated valid, significantly outperforming a GPT-5.2 baseline uswithout the skill library. We release PaperMentor as open source for public use. Our code is publicly available under the AGPL-3.0 license at this https URL

---


### 313. [Intelligent Character Recognition of Handwritten Forms with Deep Neural Networks](https://arxiv.org/abs/2606.08858)

**<font color=#1a73e8>作者：</font>** Hartwig Grabowski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The automatic processing of handwritten forms remains a challenging task, wherein detection and subsequent classification of handwritten characters are essential steps. We describe a novel approach, in which both steps -- detection and classification -- are executed in one task through a deep neural network. Therefore, training data is not annotated by hand, but manufactured artificially from the underlying forms and yet existing datasets. It can be demonstrated that this single-task approach is superior in comparison to the state-of-the-art two-task approach. The current study focuses on hand-written Latin letters and employs the EMNIST data set. However, limitations were identified with this data set, necessitating further customization. Finally, an overall recognition rate of 88.28 percent was attained on real data obtained from a written exam.

---


### 314. [Vision-Language Work Zone Intelligence for Safety-Critical Speed Regulation of Mixed-Autonomy Vehicles in Dynamic Environments](https://arxiv.org/abs/2606.08860)

**<font color=#1a73e8>作者：</font>** Angel Martinez-Sanchez, Kianna Ng, Wesley Maia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporary work-zone speed limits are communicated through visually inconsistent signage and are often missing from digital maps, creating safety risks for human drivers and automated vehicle systems. We present a real-time, onboard perception pipeline that detects active work zones, recognizes associated temporary speed limits, and outputs a law-aware work-zone state and speed value suitable for driver alerts or downstream automated control. The system fuses object detections with semantic verification and temporally smoothed, hysteresis-based state transitions to reduce false activations and flicker in dynamic scenes, and runs fully on low-cost embedded hardware. Evaluated manually on a annotated subset of the ROADWork dataset (490 sequences), the system achieves inside-work-zone event-level recall of 96.5% and event-level precision of 68.7%. Speed-limit recognition evaluated on 35 minutes of in-house driving data attains 95.45% precision and 53.85% recall, with no incorrect speed classifications and a single false positive. These results demonstrate a practical, scalable approach for grounding work-zone speed awareness directly in onboard perception rather than maps or infrastructure. We release our source code for the proposed system pipeline on our GitHub repository: this https URL

---


### 315. [CHROMA: Detecting AI-Generated Images through Inter-Channel Color-Space Correlations](https://arxiv.org/abs/2606.08864)

**<font color=#1a73e8>作者：</font>** Juan Pablo Sotelo, Marina Gardella, Pablo Musé  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of diffusion and large-scale generative models has made it increasingly challenging to distinguish synthetic imagery from real photographs. While automated detectors have been proposed, their generalization to unseen generators remains brittle. To address this limitation, we investigate inter-channel color correlations, a lightweight and underexploited forensic cue. We first demonstrate that LPIPS, a widely used perceptual metric, exhibits inconsistent responses to perturbations that selectively alter channel dependence across different color-space parameterizations, indicating that cross-channel statistics are not uniformly constrained by common perceptual training objectives. Motivated by this, we analyze the distributions of pairwise inter-channel correlation features across multiple color spaces. Our analysis reveals systematic, generator-specific differences in these distributions, with RGB and Lab color spaces providing the most apparent separation between real and generated images. Building on this, we introduce Chroma, a detector of AI-generated images which augments standard RGB inputs with inter-channel correlation maps and employs a fixed CNN backbone trained with a modest computational budget. We assess its robustness under both single-generator training and a limited multi-generator supervision regime, where only a few samples from additional generators are available. Across a standard benchmark protocol, correlation-augmented inputs improve real-vs-generated discrimination and robustness, yielding performance competitive with recent detectors while maintaining a simple architecture and training procedure. Code is available at this https URL

---


### 316. [Generalizing Geometry-Guided Mamba as a Plug-and-Play Context Module for CNN-based Semantic Segmentation](https://arxiv.org/abs/2606.08866)

**<font color=#1a73e8>作者：</font>** Sheng-Wei Chan, Hsin-Jui Pan, Chun-Po Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CNN-based semantic segmentation networks usually rely on context heads such as ASPP, PPM, or attention modules to enlarge the receptive field. These heads are effective but may introduce heavy computation, memory cost, or boundary leakage. This paper revisits Directional Geometric Mamba (G-Mamba) from DGM-Net and studies it as a plug-and-play context aggregation module rather than a complete new segmentation architecture. The key idea is to inject geometric guidance into the selective scan process, allowing long-range feature propagation to be modulated by boundary and centripetal-flow cues. We replace the original context heads of six representative CNN segmentation models, including DeepLabV3+, DANet, CCNet, PSPNet, PSANet, and OCRNet, while keeping the ResNet-101 backbone unchanged. Results on Cityscapes show consistent mIoU gains with only moderate extra GFLOPs at $1024\times1024$ resolution, suggesting that geometry-guided SSM modules can serve as practical alternatives or enhancements to conventional CNN context heads.

---


### 317. [Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework](https://arxiv.org/abs/2606.08867)

**<font color=#1a73e8>作者：</font>** Aman Gupta, Kevin Rossell, Edesio Alcobaça 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid rise in LLM capabilities has made AI agents increasingly viable across a broad range of tasks. Among the most promising applications is building production-ready customer-facing agents, a challenge that demands coordinated excellence in evaluation methodology, context engineering, training, and online measurement. Yet these critical pillars are typically developed in isolation, creating blind spots that only surface after deployment.
In this paper, we present a unified framework that bridges offline development with online impact for customer support AI agents at Nubank, a company with 100M+ users. Our approach integrates several key components: (1) structured context engineering tailored to customer support agents, (2) systematic human-in-the-loop prompt iteration, (3) rigorous LLM judge evaluation with measured inter-rater agreement and GEPA optimization for consistency, and (4) ideation-to-production validation.
A central insight is that evaluation-pipeline quality directly determines iteration velocity. We present results from five production deployments spanning distinct domains: card delivery, debt management, credit-limit support, card management, and product explanation. These deployments deliver consistent customer-satisfaction gains while substantially accelerating iteration. In our card-delivery deployment, large-scale A/B testing yields a 37 percentage-point improvement in AI transactional Net Promoter Score and a 29 percentage-point gain in self-service rate over prior agent variants, alongside a strong correlation between offline simulation metrics and online outcomes, demonstrating that eval-driven development reliably predicts production impact. On most use cases, AI satisfaction reaches within a few percentage points of expert human agents.

---


### 318. [PerspectiveGap: A Benchmark for Multi-Agent Orchestration Prompting](https://arxiv.org/abs/2606.08878)

**<font color=#1a73e8>作者：</font>** Youran Sun, Xingyu Ren, Kejia Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world LLM applications are moving beyond single-agent workflows toward orchestrated multi-agent systems, yet current models still struggle to determine what each sub-agent needs to know. To measure this, we introduce PerspectiveGap, a benchmark for evaluating LLMs' ability to compose orchestration prompts for multi-agent systems. PerspectiveGap contains 110 scenarios, each evaluated through two distractor-mixed task formats: role-fragment assignment and free-form prompt writing. These scenarios are organized into 10 topologies, which are distilled from the authors' real-world engineering practice and framed by the Prompt Economy principle: building loop-centered orchestrations that maximize utility with minimal role and engineering overhead. In experiments with 27 commercial models from 10 companies, GPT-5.5 substantially outperforms all competitors, whereas Opus 4.7 shows a notable weakness in orchestration prompting despite its strong coding performance. Nevertheless, PerspectiveGap remains challenging: the evaluated models achieve an average combined pass rate of only 14.9\% (GPT-5.5 62.0\%) and an average overall leakage rate of 246.5\% (a per-scenario information leak-event count, not a proportion; GPT-5.5 49.1\%). These findings suggest that multi-agent orchestration prompting is a distinct and under-evaluated capability, and PerspectiveGap provides a foundation for measuring and improving it systematically.

---


### 319. [Block-A-Mole: The Sustainability Frontier of Moving-Target Censorship Resistance](https://arxiv.org/abs/2606.08886)

**<font color=#1a73e8>作者：</font>** Anindya Maiti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Internet censorship affects over four billion people, and deployed circumvention systems share a common weakness: their endpoints are fixed and discoverable, so a patient censor can enumerate and block them. Moving-target circumvention systems instead rotate endpoints across commercial cloud address space faster than censors can react, but the field lacks a theory of when rotation works, leaving rotation intervals and pool sizes to intuition. We give the first formal account of moving-target censorship resistance by modeling the censor-defender interaction as a continuous-time timing game over a combinatorial address-domain space, generalizing FlipIt to a collateral-bounded adversary. We prove a sustainability frontier separating configurations a censor can defeat from those it cannot, and show that under the Great Firewall's 2024 shift to blocking QUIC and TLS by domain, raw rotation speed is not the binding constraint. Instead, availability is governed by the domain burn rate, $\beta=\lambda_{\mathrm{disc}}/\lambda_{\mathrm{intro}}$, the ratio between how quickly the censor blocks defender domains and how quickly the defender introduces fresh ones. We derive a closed-form availability law, prove that address rotation alone cannot sustain high availability when $\beta>1$ regardless of endpoint rotation speed, and characterize the frontier $\beta^\star$. We validate the analysis with an open, model-level censor-defender simulator requiring no privileged access or cloud deployment. The simulator reproduces the predicted phase transition at $\beta^\star$ under adversary profiles representative of the GFW, Russia's TSPU, and Iran, and shows robustness to state-dependent discovery and bursty, provider-correlated burns. The result replaces the heuristic of ``rotate faster'' with a precise operating condition: keeping the domain economy ahead of the censor.

---


### 320. [Diffuse AI Control on Fuzzy Tasks](https://arxiv.org/abs/2606.08892)

**<font color=#1a73e8>作者：</font>** Mikhail Terekhov, Caglar Gulcehre, Vivek Hebbar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI models deployed in critical domains, such as AI safety research, may subtly sabotage our efforts due to misalignment. Diffuse AI Control is a subfield of AI safety concerned with mitigating risks from AI sabotage distributed over long deployment horizons (diffuse threats). These risks are particularly pernicious on fuzzy tasks, i.e. tasks which are hard to grade or require intuition. To understand diffuse threats on fuzzy tasks, we introduce a novel framework that considers AI control as an adversarial game between a blue team and a red team. The blue team uses a weak trusted model to construct a weak score against which they would train a strong, potentially subversive model to remove the subversion propensity if it were present. The red team then tries to find model behaviors that are rated highly by the weak score, and thus might not be trained out, but actually correspond to poor performance. We test our framework on the task of writing experimental proposals for research questions from recent ML papers. We use a language model with access to the original paper as a proxy "ground-truth" scorer. Our red team discovers subversive behaviors using multi-objective evolutionary prompt optimization. We show that Opus~4.6 can write proposals that are worse according to the ground truth proxy than those of GPT-OSS-20B, while the weak scorer rates them as highly as the best proposals from Opus 4.6. To mitigate the threat, we propose an adversarial optimization algorithm for the blue team that discovers more robust prompts for the weak model. This algorithm produces a blue team prompt that our red team optimization fails to exploit.

---


### 321. [Cheap Reward Hacking Detection](https://arxiv.org/abs/2606.08893)

**<font color=#1a73e8>作者：</font>** Iván Belenky, Joaquín Itria, Steven Johns  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A small transformer encoder is trained to map Terminal-Wrench trajectories onto a unit sphere where embedding distance approximates the $L_1$ distance between reward and metadata signals. A linear probe on top of that embedding detects reward hacking on the cleaned test split with AUC $0.9467$ and TPR@5%FPR $0.8296$, matching the TW sanitized LLM-as-judge AUC ($0.9510$ on the cleaned split) and exceeding its TPR@5%FPR ($0.7130$ vs $0.8296$) on the same information condition, at roughly four orders of magnitude lower per-trajectory cost. The encoder is not a pure behavior reader: stripping natural-language reasoning from its input at probe time drops AUC to $0.6213$.

---


### 322. [A multi-agent system for spine MRI report generation from multi-sequence imaging](https://arxiv.org/abs/2606.08897)

**<font color=#1a73e8>作者：</font>** Zhiping Xiao, Junwei Yang, Gongbo Sun 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spinal pathology is a leading cause of pain and disability worldwide. Spine MRI is central to clinical evaluation, yet its interpretation remains complex and time-consuming, requiring integration of information across multiple imaging sequences and anatomical regions. Despite recent advances in automated MRI analysis, effectively combining multi-sequence data while preserving sequence-specific diagnostic information remains an open challenge. Here we present SpineAgent, a multi-agent framework for spine MRI report generation built upon a multi-sequence foundation model trained on routine clinical data from 32,047 patients and 453,683 MRI series, comprising a total of 13,441,191 MRI slices. To accommodate diverse modalities of sequences, we first pre-train two DINOv3-based encoders separately on T1- and T2-weighted sequences. We then introduce a continual training strategy that learns a synthesizer to embed images of other sequences using the T1 and T2 encoders, producing patient-level embedding that integrates various signals across MRI sequences. Using these embeddings, SpineAgent achieves state-of-the-art performance, and demonstrates strong generalizability under cross-manufacturer and cross-cohort evaluation. Beyond classification, SpineAgent enables pathology localization by identifying findings-relevant slices and segmenting pathological regions. It also supports multimodal image-report retrieval, providing a solid foundation for scalable and explainable MRI report generation. We further integrate these validated capabilities of SpineAgent into 37 specialized agents. Finally, we incorporate their outputs as structured tokens within a Medical Report Agent trained end-to-end for report generation. Through both automated metrics and expert evaluation by five radiologists, SpineAgent achieves leading performance in spine MRI report generation.

---


### 323. [Synthetic but Not Realistic: The Evaluation Challenge in Generative Modelling for Structured Electronic Medical Records](https://arxiv.org/abs/2606.08903)

**<font color=#1a73e8>作者：</font>** Nicholas I-Hsien Kuo, Blanca Gallego, Louisa Jorm  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic healthcare data are widely proposed as privacy-preserving substitutes for real patient data, yet their evaluation remains dominated by statistical similarity and predictive performance that do not reflect clinical validity. We introduce a multi-dimensional evaluation framework grounded in epidemiology, assessing descriptive fidelity, clinical utility, and structural validity, corresponding to descriptive, predictive, and causal questions. We evaluate four representative generative paradigms - GAN-based, VAE-boosted, diffusion-based, and masked modelling - using PRIME-CVD, a 50,000-person cohort with known ground-truth structure. While all models reproduce marginal distributions, none simultaneously preserve subgroup structure, effect estimates, and dependency structure. Notably, models with strong distributional fidelity can exhibit poor calibration and distorted relationships, leading to unreliable inference. These results show that current evaluation practices can overestimate synthetic data quality and motivate domain-informed assessment based on the ability to support valid clinical and scientific conclusions.

---


### 324. [Enhancing Presence, Deepening Fan Intensity: How Presence in Immersive Video Shapes Psychological Closeness to Performers](https://arxiv.org/abs/2606.08912)

**<font color=#1a73e8>作者：</font>** Koichi Toida, Hideto Hiranuma, Shimpei Miura 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Immersive video differs from conventional flat 2D video in that it is experienced as 180-degree stereoscopic video on a head-mounted display, thereby eliciting bodily and spatial subjective experience. Previous studies have shown that viewing and interpersonal distance affect Presence; however, it remains insufficiently understood how Presence differences are related to psychological closeness to content. In the present study, we examined whether differences in Presence could increase viewers' psychological closeness to performers within the content. This psychological closeness was operationally defined as fan intensity. Specifically, a live performance by a Japanese idol group was recorded as 180-degree immersive video, and a high-Presence condition (1.2 m) and a low-Presence condition (7.6 m) were established by manipulating filming distance. Twenty-four participants with different levels of prior involvement, comprising Avid fans and Casual fans, experienced both conditions in a counterbalanced within-participants design. Fan intensity was measured before and after the experience as perceived psychological overlap between the self and the performers. The results showed that, compared with the low-Presence condition, the high-Presence condition significantly increased all Presence-related measures except the Slater-Usoh-Steed questionnaire, with the largest condition differences observed for Possible Actions, Social Presence, and Observability. Moreover, a mixed analysis of variance on changes in fan intensity revealed a significant main effect of Presence condition, indicating that the high-Presence video produced a greater increase in fan intensity than the low-Presence video. These findings suggest that filming distance in immersive video is not merely a factor that determines angle of view or composition, but a design variable that can enhance Presence and deepen fan intensity.

---


### 325. [Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human](https://arxiv.org/abs/2606.08919)

**<font color=#1a73e8>作者：</font>** Emre Turan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents begin to take real, irreversible actions (shell commands, file edits, deploys), the standard safety pattern is a human-in-the-loop approval gate: risky actions pause and wait for a person. We argue the gate is the easy part; the hard part is the judgment - which actions to stop - which the field evaluates against two false assumptions: that there is a ground-truth notion of "risky," and that the human reviewer is a perfect, infinitely-available oracle. On a hand-labeled set of 125 adversarially-weighted agent actions we show that (i) reviewers only moderately agree on what is risky (Fleiss' kappa = 0.52), so there is no single correct label; (ii) framing the guard as selective classification under asymmetric cost makes its operating limits measurable, and on hard inputs the guard cannot safely auto-decide; and (iii) when the reviewer is modeled as endogenous (fatiguing as escalation load grows), realized safety becomes an inverted-U in the escalation rate: more human oversight can make a system less safe, and the safety-optimal guard escalates below full escalation - a setting a load-aware policy also uses to resist a flooding attack that slips a malicious action past a fatigued reviewer. Agent oversight, framed this way, is not only a classification problem but a resource-allocation one: human attention is finite, and the guard's escalation policy spends it. We claim none of these mechanisms as novel - fatigue-aware learning-to-defer (FALCON), cost-sensitive deferral under workload constraints (DeCCaF), trajectory-level guarding, and reviewer-fatigue/flooding attacks are all prior art we cite. Our contribution is an open-source agent-oversight system that operationalizes and measures them in the LLM-agent action-gating setting, turning "is my guard good?" from a guess into a curve. The inverted-U and the flooding attack are modeling results that motivate a human study.

---


### 326. [PolyBuild: An End-to-End Method for Polygonal Building Contour Extraction from High-Resolution Remote Sensing Images](https://arxiv.org/abs/2606.08920)

**<font color=#1a73e8>作者：</font>** Yaoteng Zhang, Julin Zhang, Guangshuai Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extracting building polygon contours from high-resolution remote sensing images is a fundamental task for various mapping applications. However, the presence of varying imaging conditions and complex building structures, makes automatic contour extraction extremely challenging. Mainstream approaches for building extraction often rely on pixel-level segmentation followed by multiple post-processing steps to produce building contour, which can be computationally intensive and prone to errors. In this paper, we propose an end-to-end method named PolyBuild, which can directly extract building vector polygons from high-resolution remote sensing images without the need for any post-processing operations. The proposed method leverages two primary modules: an Initial Contour Generation Module (ICGM) and a Contour Optimization Module (COM). The ICGM is designed to generate an initial building contour by utilizing concatenated sub-region center features for each building instance. It performs simultaneous object detection and initial contour extraction by generating bounding boxes and using the center features of four sub-regions to represent each building. The Contour Optimization Module (COM) further refines the generated building contours by iteratively integrating Convolutional Neural Network (CNN) features and contour positional information in a Transformer-based decoder. The hybrid CNN-Transformer architecture effectively captures both local and global spatial relationships within the building contour, ensuring high-quality boundary delineation. Extensive experiments are conducted on three building datasets to evaluate the performance of PolyBuild. The results demonstrate that PolyBuild significantly outperforms state-of-the-art methods, including mask-based and contour-based approaches.

---


### 327. [Generalized Rank-based Evaluation for Knowledge Graph Completion: Perspectives, Framework, and Analyses](https://arxiv.org/abs/2606.08921)

**<font color=#1a73e8>作者：</font>** Sooho Moon, Jian Kang, Yunyong Ko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph completion (KGC) aims to predict missing facts from an observed knowledge graph (KG), playing a crucial role in a wide range of real-world applications such as drug discovery, recommender systems, and retrieval-augmented generation (RAG). Although numerous KGC models have been proposed, the evaluation of KGC remains underexplored, despite its critical role in reliably assessing model performance and selecting appropriate models for real-world applications. In this paper, we introduce two important perspectives for KGC evaluation that are overlooked by existing evaluation metrics, (P1) predictive sharpness and (P2) popularity-bias robustness. To address both perspectives, we propose a generalized evaluation framework, PROBE, which consists of a rank transformer (RT) that estimates the score of each prediction based on a desired level of predictive sharpness and a rank aggregator (RA) that determines the final evaluation score by aggregating all prediction scores according to a desired level of popularity-bias robustness. We theoretically analyze PROBE by defining six key properties for reliable KGC evaluation and prove that PROBE satisfies all the properties, while existing metrics fail to satisfy some. In particular, due to the open-world nature of KGs, an evaluation metric should preserve the relative performance of KGC models even when only incomplete facts are observed. We show that PROBE better maintains such consistency, providing a more reliable estimate of intrinsic model performance than existing metrics. Extensive experiments with six KGC models on six real-world KGs reveal that existing metrics may over- or under-estimate model performance depending on different evaluation perspectives, whereas PROBE enables a more comprehensive, flexible, and consistent evaluation of KGC models.

---


### 328. [PROBE-Web: An Interactive System for Probing Evaluation Landscapes of Knowledge Graph Completion Models](https://arxiv.org/abs/2606.08926)

**<font color=#1a73e8>作者：</font>** Sooho Moon, Yunyong Ko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph completion (KGC) models are commonly evaluated using rank-based metrics such as MRR and Hits@K, despite different users often requiring different evaluation perspectives. In this demo, we present PROBE-Web, an interactive system for probing diverse evaluation landscapes for KGC models. PROBE-Web enables users to flexibly evaluate KGC models by adjusting two critical perspectives: (P1) predictive sharpness and (P2) popularity-bias robustness. Through a user-friendly GUI, users easily evaluate multiple KGC models and analyze their strengths and weaknesses. PROBE-Web provides four key functionalities: (1) conventional evaluation toolkit, (2) flexible perspective-aware evaluation, (3) explainable case studies, and (4) evaluation landscape exploration. We believe that PROBE-Web can help users better understand KGC models aligning with their objectives.

---


### 329. [In-Situ Immersive Analytics Authoring through Ergonomic Keyboard Support](https://arxiv.org/abs/2606.08927)

**<font color=#1a73e8>作者：</font>** Leonel Merino, Begoña Juliá-Nehme, Santiago Viana  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Immersive analytics uses augmented reality (AR) to integrate data analysis and authoring within physical environments. However, extensive text entry required for immersive analytics authoring remains a fundamental challenge in AR, as popular natural user interfaces often hinder expressive input. This paper presents the Body-Supported Keyboard (BSK), an ergonomic system that allows the mobile use of a Bluetooth keyboard in AR. We conducted a controlled study with 20 participants to compare the BSK with a standing desk during text transcription and a mobile AR scenario. The results showed slightly higher error rates but comparable task completion times. Participants reported comfort improvements during mobile use and positive usability ratings (mean SUS = 74.5). The BSK allows users to move freely and maintain stable postures while authoring in AR. In general, the findings show evidence of the potential for body-supported input to enhance expressive and ergonomic workflows in immersive analytics and emphasize the importance of comfort and mobility in the design of AR authoring tools.

---


### 330. [From Statute to Control Flow: Span-Grounded Deontic Trees for Defeasible Scope Parsing](https://arxiv.org/abs/2606.08932)

**<font color=#1a73e8>作者：</font>** Jian Chen, Siyuan Li, Chucheng Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rule-following agents tasked with executing policies and regulations often fail via Silent Scope Omission (SSO): a model applies a general rule but silently drops nested exceptions or counter-exceptions, producing outputs that appear compliant yet break on important edge cases. Although such failures are often framed as an agentic-systems problem, the underlying bottleneck is statutory and policy understanding, a capability typically studied in legal NLP. However, most existing legal NLP benchmarks emphasize end-task outcomes, which can overlook the structural omissions that cause SSO. To diagnose and mitigate SSO, we introduce NormBench, a benchmark of 2,290 provisions spanning Chinese (laws and local policies), English (U.S. tax law, GDPR, and corporate policies), and cross-lingual settings, designed for defeasible scope parsing: identifying precisely which clause overrides which. NormBench uses Span-Grounded Deontic Trees (SG-DT), a compiler-style intermediate representation that anchors every logical branch to source spans and requires explicit exclusion guards, enabling deterministic compilation and audit. Evaluations of frontier LLMs reveal two recurring pathologies: (1) Recursion Decay, where performance drops sharply as defeater depth increases, and (2) an Auditability Trap, where models retrieve relevant spans but fail to assemble correct control flow. Using SG-DT as a constrained intermediate output improves whole-tree fidelity and defeater recovery, and downstream experiments show that its utility is mechanism-specific: gains concentrate on exception-active, SSO-prone cases, while aggregate accuracy can be mixed when the added structure is unnecessary or parser fidelity is low.

---


### 331. [Backward Coherence and Hidden-State Stability in Recurrent Neural Networks: A Quasi-Reverse-Martingale Theory](https://arxiv.org/abs/2606.08934)

**<font color=#1a73e8>作者：</font>** Yuan-chin Ivan Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent neural networks maintain a hidden state $h_t$, but its probabilistic meaning is often unclear. We study hidden-state stability through \emph{backward coherence}: the extent to which $h_t$ can be reconstructed from $h_{t+1}$ by a learned backward projector $g_\phi$. Under contraction and summable backward drift, the hidden-state sequence forms a quasi-reverse-martingale. This yields almost-sure convergence, rates under mixing, an interpretable limiting representation, finite pathwise stopping times, and a theoretical framework for time-uniform confidence sequences.
Simulations support the theory. Backward-coherence regularisation reduces the empirical quasi-martingale total $\hat Q$ by $43$--$58%$, reaches stability $28$--$44%$ earlier than an unregularised RNN, and gives tracking-error recovery consistent with geometric bounds. Additional tests confirm echo-state forgetting rates bounded by $\rho$ and verify the increment-sum tube $R_t$ with $100%$ simultaneous coverage, although $R_t$ is conservative; in practice, the defect-tail proxy $\hat Q_t$ is the more useful monitor. The backward-coherence loss is also equivalent to minimising a Kullback--Leibler divergence in a Gaussian backward model, linking the method to variational inference. Extensions cover $\phi$-mixing inputs, change-point tracking, and finite-sample concentration.
Three real-data studies further validate the approach. On PhysioNet 2012 ICU data, the Reverse Martingale RNN (RMRNN) matches RNN mortality-prediction AUC while reaching stable representations 13 hours earlier. On FRED-MD, it reduces one-month-ahead forecast error by about fourfold under concept drift. On UCI Human Activity Recognition, it maintains lower post-transition tracking error with geometric decay. The guarantees apply under the stated assumptions; universality is not claimed.

---


### 332. [PAI: Preserving Amplitude Information in Representation-Based Time-Series Anomaly Detection](https://arxiv.org/abs/2606.08935)

**<font color=#1a73e8>作者：</font>** Kang Zhang, Wei Jian Lau, Shoushou Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation-based time-series anomaly detection algorithms significantly outperform other methods on diverse anomaly detection tasks. However, we notice that they suffer from a major limitation in our evaluation - their learned embeddings are often amplitude-agnostic. Losing amplitude information can degrade performance on amplitude related anomalies, and this failure is prevalent across all existing representation-based methods. To address aforementioned issues, we propose a new anomaly scoring scheme named PAI. PAI consists of two complementary modules, a diagnostic module and a final score augmentation function. The diagnostic module compares cosine and Euclidean scoring on the same representation bank to test whether amplitude information is already captured in the learned representation. Then in final score augmentation function, PAI computes a point-wise median and MAD deviation score and a local mean-shift score-which are fused with the representation score to produce the final anomaly score. On the TSB-AD-U-Eva and TAB UV datasets, PAI improves all four evaluated representation-based methods across every reported metric, achieving average VUS-PR gains of 98.4% and 36.8%, respectively. Among all evaluated combinations, PaAno + PAI achieves the best performance, outperforming the state-of-the-art method by 15%. Further evaluation on bootstrap confidence intervals, anomaly-type breakdowns, and a TS2Vec input-normalization ablation further support the proposed scheme. These results suggest that explicitly retaining amplitude information is important for representation-based time-series anomaly detection, which has been underemphasized in existing scoring schemes. Code is available at: this https URL

---


### 333. [PACT: Learning Diverse Diagnostic Strategies via Privileged Synthesis and Branch Consensus](https://arxiv.org/abs/2606.08938)

**<font color=#1a73e8>作者：</font>** Gen Li, Yuanze Hu, Zhichao Yang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis requires flexible use of multiple reasoning paradigms under incomplete patient information. Existing LLM-based medical agents show strong medical reasoning ability, but single-paradigm or naively mixed dialogue supervision makes these paradigms difficult to learn without interference. We propose \textbf{PACT} (Periodic Anchor Consensus Training), a framework that couples supervised multi-paradigm dialogue synthesis with consensus-based Branch training. At the data level, \textbf{DPS} (Doctor-Patient-Supervisor) uses complete electronic medical records (EMRs) for quality control while keeping the doctor agent restricted to patient-visible information. This produces validated dialogues under four diagnostic reasoning paradigms without leaking hidden clinical answers. At the training level, PACT trains one paradigm-specific LoRA Branch per paradigm and periodically aggregates Branches into a shared Anchor through sign consensus. We further construct a dynamic multi-turn Chinese medical diagnosis benchmark for interactive consultation. Experiments show that PACT achieves state-of-the-art performance among compared proprietary, medical-specialized, and task-adapted baselines on diagnostic outcome and consultation-process metrics.

---


### 334. [Self-Consistent Generative Paths via Admissible Random Variational Transport](https://arxiv.org/abs/2606.08953)

**<font color=#1a73e8>作者：</font>** Lei Luo, Yingzhen Zhang, Jian Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern generative models often define an entire probability path from a simple prior to the data law, rather than only an endpoint map. Diffusion models follow stochastic denoising paths, flow matching learns transport fields, consistency and distillation methods compress paths into one or a few steps, adversarial models match terminal distributions, and VAEs generate through latent kernels. Existing unifying views mainly describe how such paths are constructed. We study a complementary question: when is a generated probability path self-consistent? We define a self-consistent generative path as a random fixed point of admissible local variational transport corrections. In this framework, a local correction is specified by a random variational transport operator combining a divergence or geometry term, an energy term, and a structural constraint. The framework contains random regularized optimal-transport proximal steps as a structured instance, while also allowing non-OT divergences, latent kernels, adversarial constraints, causal discrete kernels, and terminal one-step maps. The theory yields a random fixed-point path residual (R-FPR), which measures the gap between the actual generated path and an admissible local correction. We prove well-posedness, random fixed-point existence and attraction, non-contractive existence, residual-to-generation error bounds, empirical residual concentration, proxy perturbation bounds, continuous-time limits, and operator-level generalization with model-specific corollaries. The resulting theory turns endpoint matching into path self-consistency testing and provides a residual-control principle for diagnosing failures, regularizing training, and guiding adaptive sampling across diffusion, flow, one-step, VAE, GAN/WGAN, and autoregressive generators.

---


### 335. [From inverse problems to neural operators: prediction, mechanism, and generalization of data-driven models](https://arxiv.org/abs/2606.08956)

**<font color=#1a73e8>作者：</font>** Conor Rowan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientists have historically relied on mathematical models based on differential equations to relate system inputs -- forces, fluxes, or heat sources -- to outputs, such as displacement, velocity, concentration, and temperature. These models rely on deep domain knowledge to determine the form of the governing differential equation, which is then calibrated with data by solving an inverse problem. In recent years, the field of Scientific Machine Learning has introduced a variety of alternative modeling strategies for physical systems. A method called Sparse Identification of Nonlinear Dynamics learns the governing equation as a sparse linear combination of terms in a user-defined library. Neural Ordinary Differential Equations construct the governing equation by taking in the state and its derivatives at the input layer of a neural network. Entirely foregoing the modeling framework of differential equations, neural operators directly learn a non-linear mapping between the system inputs and outputs. From inverse problems to neural operators, all of these modeling strategies can be conceptualized as data-driven machinery to predict a system's response over a range of inputs. It is then natural to wonder how exactly these various strategies relate to each other, and whether they can be neatly taxonomized. Drawing from the philosophical literature on scientific models, we argue that many model types have a common structure, differing only in the assumed model class of the input-output relation they define. Connecting to philosophical ideas on mechanism, and arguing that data from physical systems arises from solutions to parsimonious differential equations, we propose that only certain models are capable of mechanism discovery, and thus generalization. Our analysis is intended to unite apparently disparate modeling strategies and provide insight into their appropriate use cases.

---


### 336. [Rethinking 3D Shape Generation: Diffusion over Superquadrics](https://arxiv.org/abs/2606.08957)

**<font color=#1a73e8>作者：</font>** Zhiyang Liu, Wanze Li, Yuwei Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have advanced 3D shape generation, yet most methods still denoise in high-cardinality spaces (e.g., voxel/SDF grids, meshes, or point clouds), which is computationally and memory intensive and makes it difficult to scale in terms of both higher resolution and stronger controllability. We rethink the diffusion representation and propose to move diffusion from dense geometry to compact geometric primitives, representing each shape as a small set of superquadrics. Instead of operating on thousands to millions of geometric representation values, we leverage 7KB superquadric parameters (pose, size, and shape), drastically reducing diffusion-state dimensionality and per-step compute/memory. Our diffusion-over-superquadrics improves scalability by supporting broader capabilities (e.g., resolution-free point-cloud decoding, part-level editing, and constraint-based design) and achieving competitive surface-fidelity and distributional performance on standard benchmarks after point-cloud decoding, while enabling efficient generation within 0.6s per shape for most conditions.

---


### 337. [C$^3$ache: Accelerating World Action Models with Cross Inference Chunk Cache](https://arxiv.org/abs/2606.08962)

**<font color=#1a73e8>作者：</font>** Weisen Zhao, Lam Nguyen, Zhicong Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) generalize better than standard Vision-Language-Action (VLA) policies to novel motions and environments, because a video-modeling objective lets them learn from abundant unlabeled video rather than scarce labeled robot demonstrations. This generalization is computationally expensive. To complete a task, a WAM runs over multiple inference chunks, and each chunk requires a costly denoising process. Existing acceleration methods reduce this cost by caching and reusing computation within a single chunk's denoising trajectory. Our empirical analysis reveals a substantial source of redundancy they overlook: redundancy across chunks. When a robot executes a smooth behavior, the residuals computed at a given denoising step are strongly correlated from one chunk to the next. We introduce C$^3$ache, a training-free method that caches and reuses these residuals across inference chunks at the same denoising step. Experiments on benchmarks with a Fast-WAM backbone show that C$^3$ache achieves up to a $2.5\times$ speedup in total wall-clock inference time, with negligible degradation in task success rate.

---


### 338. [Before You Scroll Again: Predicting Regretful Social Media Sessions from In-the-Wild Contextual and Wearable Sensing](https://arxiv.org/abs/2606.08965)

**<font color=#1a73e8>作者：</font>** Sally Ahmed, Jan Enkmann, Kye Shimizu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Users often feel regret after using social media, making regret a more ecologically valid target than screen time for understanding when phone use becomes problematic. Existing self-monitoring tools cannot anticipate regret before it occurs, and prior physiological work on social media use has been confined to the lab with research-grade sensors and curated content, leaving the question of in-the-wild prediction open. We deployed a 7-day in-the-wild experience sampling study with 21 participants, combining passive smartphone logging, a low-cost consumer smartwatch (this http URL 2, \$80), session-level surveys (1,445 sessions), and exit interviews to investigate when and why social media sessions become regretful, and whether regret can be anticipated before a session begins. Three findings stand out: (i) the gap between intended and actual use predicts regret far more strongly than session duration, with duration's apparent effect collapsing once intention is modeled; (ii) regret is amplified when sessions displace a valued alternative, particularly at night and following productivity-app use; and (iii) pre-session contextual features generalize across participants while physiological signals add person-specific lift, pointing toward a two-layer architecture for just-in-time adaptive interventions. Interview themes of scrolling-as-avoidance and time blindness contextualize these patterns and surface design opportunities beyond timer-based interventions.

---


### 339. [Online Learning with Recency: Algorithms for Sliding-window Streaming Multi-armed Bandits](https://arxiv.org/abs/2606.08977)

**<font color=#1a73e8>作者：</font>** Vladimir Braverman, Chen Wang, Liudeng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by the recency effect in online learning, we study algorithms for single-pass *sliding-window streaming multi-armed bandits (MABs)* in this paper. In this setting, we are given $n$ arms with unknown sub-Gaussian reward distributions and a parameter $W$. The arms arrive in a single-pass stream, and only the most recent $W$ arms are considered valid. The algorithm is required to perform pure exploration and regret minimization with limited memory, defined as the number of stored arms. The model is a natural extension of the streaming multi-armed bandits model (without the sliding window) that has been extensively studied in recent years. We provide a comprehensive analysis of both the pure exploration and regret minimization problems with the model. For pure exploration, we prove that finding the best arm is hard with sublinear memory while finding an approximate best arm admits an efficient algorithm. For regret minimization, we explore a new notion of regret and give sharp memory-regret trade-offs for any single-pass algorithm. We complement our theoretical results with experiments, demonstrating the trade-offs between sample, regret, and memory.

---


### 340. [Heterophily-Aware Adaptive Knowledge Distillation for Hypergraph Neural Networks](https://arxiv.org/abs/2606.08978)

**<font color=#1a73e8>作者：</font>** Joohee Cho, David Yoon Suk Kang, Yunyong Ko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypergraph knowledge distillation aims to retain the predictive performance of a hypergraph neural network (HNN) teacher while reducing inference costs through a lightweight student model. In this work, we observe that HNNs exhibit substantially lower prediction performance on heterophilic nodes connected through semantically diverse hyperedges, indicating that the reliability of teacher knowledge varies across nodes. Motivated by this observation, we propose HADES, a heterophily-aware adaptive distillation method for hypergraph neural networks. HADES quantifies node heterophily and leverages it as an estimate of teacher reliability to modulate the transfer of teacher knowledge during distillation. Experimental results on real-world hypergraphs demonstrate that HADES consistently improves student performance across different HNN teachers and distillation objectives. In many cases, the resulting student models surpass the predictive performance of their teachers while achieving up to 12.3 times faster inference.

---


### 341. [EPS3D: End-to-End Feed-Forward 3D Panoptic Segmentation](https://arxiv.org/abs/2606.08980)

**<font color=#1a73e8>作者：</font>** Runsong Zhu, Jiaxin Guo, Xiaoyang Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces EPS3D, a new end-to-end feed-forward framework for open-vocabulary 3D panoptic segmentation. Unlike existing methods relying on additional preprocessing, we design an end-to-end architecture, with a distillation-based training strategy on diverse 3D scenes to predict 3D-aware semantic and instance features from multi-view images, improving 3D consistency and avoiding error accumulation. We further propose a mutual enhancement module to enforce inherent semantic-instance consistency. By aligning semantics within instances (Ins2Sem) and refining instance features with semantic guidance (Sem2Ins), we achieve more coherent 3D scene understanding. Ultimately, EPS3D outperforms SOTA baselines on two benchmarks (e.g., +13% mIoU for semantics on Replica) with high efficiency (e.g., 1s per scene), supporting tasks like robotic manipulation and 3D scene editing.

---


### 342. [Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care](https://arxiv.org/abs/2606.08982)

**<font color=#1a73e8>作者：</font>** Aiyuan Yang, Chengfeng Dou, Da Pan 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Baichuan-M4 is Baichuan Intelligence's clinical-grade medical large model, designed for \emph{continuous care} rather than single-turn medical question answering. It is built as a coordinated medical agent system around three pillars: \textbf{Baichuan-Harness}, a unified runtime that keeps reinforcement-learning training and real-world deployment consistent while enforcing action constraints, tool use, long-term patient memory, and multi-agent coordination; a \textbf{core reasoning model} trained with a continuous-care reinforcement-learning framework that integrates span-level reward modeling (SPAR++), reasoning-path compression, curriculum learning, and stabilized policy optimization; and a \textbf{clinical tool layer} for patient-memory management, authoritative evidence-based retrieval, and multimodal medical perception across documents, X-rays, and dermatology. On a cross-dimensional medical evaluation suite, Baichuan-M4 attains leading results in static medical knowledge and safety, dynamic OSCE-style consultation, long-context clinical memory, evidence-based retrieval, medical document OCR, and multimodal image understanding, while lowering the hallucination rate to 3.3\%.

---


### 343. [Beyond Neural Collapse: Task-Intrinsic Geometry Governs Neural Representations in Modular Arithmetic](https://arxiv.org/abs/2606.08985)

**<font color=#1a73e8>作者：</font>** Hu Tan, Kuo Gai, Shihua Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While neural collapse (NC) predicts that a $K$-class-balanced classifier should organize terminal representations as a $(K-1)$-dimensional simplex equiangular tight frame (ETF), modular addition consistently enters a different regime: networks compress to a two-dimensional cyclic geometry in which both classifier weights and token embeddings lie on circles. We refine the explanation of this phenomenon in three directions. First, we formalize a layerwise non-uniform training mechanism: downstream classifier weights are driven by dense cross-entropy gradients into a rank-2 equiangular configuration before upstream embeddings fully reorganize, and once this classifier plane forms, backpropagated feature gradients constrain embedding motion to the same plane while weight decay suppresses orthogonal components. Second, after this subspace locking, the induced in-plane dynamics admit an entropy-regularized transport interpretation on $S^1$; combined with modular-addition labels, this reduces embedding formation to phase alignment, whose minimizers are single-frequency characters of $\mathbb{Z}/P\mathbb{Z}$ and hence equal-angle points on a circle. Third, we quantify why this solution prevails over NC: a simplex ETF gains only an $O(1)$ advantage in cross-entropy, whereas the cyclic rank-2 solution enjoys a $\Theta(K)$ advantage under Schatten or weight-decay surrogates, yielding a critical threshold $\lambda_{\mathrm{crit}} = \Theta(1/K)$. Our results explain both why classifier weights move first and why embeddings subsequently align with them, showing that grokking on modular arithmetic is governed not by maximal separation alone but by a task-structured trade-off between separation, symmetry, and complexity.

---


### 344. [Structure-Aware Modeling of Multiple-Choice Questions Improves Automatic Difficulty Estimation](https://arxiv.org/abs/2606.08988)

**<font color=#1a73e8>作者：</font>** Gabriel Ortega, Abelino Jiménez, Séverin Lions 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Question Difficulty Estimation (AQDE) holds growing promise for educational assessment because it has the potential to yield difficulty estimates that are competitive with expert judgment, while helping reduce the time and financial burden associated with pilot administrations and scaling to digital testing contexts. Prior AQDE studies report mixed evidence on whether adding distractors as additional text to the question stem and the correct key consistently improves difficulty prediction. We hypothesize that the effectiveness of distractor information depends on its structural representation, and that explicitly modeling distractors as separate components improves difficulty estimation over baselines that omit this information. To address this, we designed controlled architectures that model MCQ components as distinct inputs to isolate the contribution of distractor content and order. Specifically, we represented distractors by encoding each distractor as its own text input and aggregating their representations either with order-aware concatenation (with positional tags) or with an order-invariant summation. We evaluated these architectures using two Chilean datasets (Natural and Social Sciences, 2016-2020; 4,114 multiple-choice questions). Compared to a simpler model that only used the question stem and the key, our best distractor-aware architecture achieved higher predictive performance, reaching R^2 = 0.83 for Natural Sciences and R^2 = 0.71 for Social Sciences items. An order-invariant variant achieved nearly the same accuracy with approximately half as many parameters, offering a favorable accuracy-efficiency trade-off. These results show that structural information (especially distractor content) drives gains in predictive accuracy, supporting the development of efficient, structure-aware models that are computationally viable for large-scale educational applications.

---


### 345. [LEAF: A Learning-Enabled ADMM Framework for Accelerated Convex Optimization](https://arxiv.org/abs/2606.08993)

**<font color=#1a73e8>作者：</font>** Binh Nguyen, Trinh Tran, Truong X. Nghiem  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose LEAF, a learning-enabled ADMM framework for accelerated convex optimization. The key idea is to approximate the Moreau envelope of the objective function using an Input Convex Neural Network (ICNN), resulting in a learned model that preserves convexity and smoothness. This leads to the proposed Moreau Envelope Learning ADMM (MEL-ADMM) and its splitting variant sMEL-ADMM. Unlike existing approaches that learn high-dimensional operators directly, LEAF learns a scalar-valued Moreau envelope, significantly reducing model complexity and improving data efficiency. The framework accommodates a broad class of convex problems with smooth and non-smooth objectives. By embedding convexity explicitly through the ICNN architecture, the proposed approach maintains high approximation accuracy while preserving key structural properties of the optimization problem. Both MEL-ADMM and sMEL-ADMM are developed with theoretical guarantees of convergence and feasibility under the learned model. Rigorous analysis shows that the proposed methods achieve convergence rates comparable to classical ADMM while reducing per-iteration computational cost. Numerical experiments demonstrate up to an order-of-magnitude speedup over state-of-the-art solvers while maintaining low optimality gaps

---


### 346. [The Token Not Taken: Sampling, State, and the Variability of AI Agent Outputs](https://arxiv.org/abs/2606.08998)

**<font color=#1a73e8>作者：</font>** Muhammad Zia Hydari, Raja Iqbal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems can behave differently across runs: the same request may produce a different plan, a different tool call, a different code edit, or a different final answer. Such variability arises from several layers that are often conflated. A foundation model is a large pretrained model, usually adaptable to many downstream tasks, that maps an input context to predictions over outputs. In many current agents, that model is embedded in an orchestration loop that plans, calls tools, observes results, and updates state. One explicit intrinsic source of variability in such systems is token generation: the model computes scores over possible next tokens, the scores are converted into probabilities, and a decoder may sample tokens using a pseudo-random number generator. A small sampled token difference can then propagate upward into a different tool call, code path, search query, or agent state. Other sources of variability are extrinsic to token sampling, including changing environments, live data, serving infrastructure, batch effects, and numerical details. By separating these layers, the manuscript clarifies what it means to call agentic AI systems stochastic, when such variability can be reproduced under matched conditions, and why deterministic execution need not imply identical behavior in deployed settings.

---


### 347. [Scaling by Diversified Experience for Vision-Language-Action Models](https://arxiv.org/abs/2606.09009)

**<font color=#1a73e8>作者：</font>** Leiyu Wang, Zhaofengnian Wang, Xueqi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action models face significant challenges in real-world deployment due to the entanglement of high-level reasoning with low-level control, and the instability of policy optimization. In this paper, we introduce SyVLA, a robust VLA model trained with diversified experiences. We propose an Intention Decoupling algorithm to isolate control-relevant features from reasoning contexts and a similar-sample guided RL pipeline to stabilize policy updates and mitigate distribution shift. Extensive experiments on real-world robotic tasks and multi-modal benchmarks demonstrate that SyVLA achieves superior task success rates and stronger out-of-distribution generalization compared to existing methods, while effectively preserving core vision-language capabilities. Codes and Datasets is released on \href{this https URL}{project page}.

---


### 348. [Understanding Quantization-Aware Training: Gradients at Quantized Weights Bias to the Low-Loss Basin](https://arxiv.org/abs/2606.09012)

**<font color=#1a73e8>作者：</font>** Hanyang Li, Jianhao Ma, Ying Cui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) converts a trained full-precision model into low-bit weights without task-level retraining, while quantization-aware training (QAT) incorporates quantization into the training loop. Although PTQ is efficient and often accurate at moderate bitwidths, it can fail sharply at aggressive bitwidths; QAT is more expensive but can often recover the lost accuracy. We propose a unified geometric framework that explains both PTQ failure and QAT recovery. We model full-precision training as following a low-loss \emph{river} inside a wider \emph{valley}: a normal neighborhood of the river forms a nearly flat \emph{basin}, while leaving this basin incurs a sharp loss increase. When the quantization grid is comparable to the basin width, local PTQ objectives, including rounding and Hessian-based second-order reconstruction, can select a high-loss deployed quantized point outside the basin even when nearby low-loss quantized points exist. In this regime, straight-through-estimator-based QAT has a useful bias: it evaluates gradients at the deployed quantized weights while updating latent full-precision weights, causing the gradient to sense the valley wall and acquire an inward component that steers subsequent quantized iterates back into the basin. We formalize this mechanism through a local landscape model, construct a geometric PTQ failure mode, and prove finite-time QAT recovery under local quantizer-compatibility assumptions. Experiments across vision and language models under multiple neural-network quantization schemes corroborate the predicted basin-crossing failure of PTQ and the corresponding recovery mechanism of QAT.

---


### 349. [Structural Grid Descriptors Predict Within-Task Solver Success on ARC-AGI](https://arxiv.org/abs/2606.09026)

**<font color=#1a73e8>作者：</font>** Ayan Pendharkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We ask whether structural properties of intermediate grid states predict whether a symbolic ARC-AGI solver will succeed, framed as a test of conditional mutual information I(X;Y|task) > 0. Across 44,800 runs spanning two architecturally distinct solvers (beam search and Stochastic DFS), 400 ARC tasks, 28 configurations per solver, and both training and evaluation splits, hand-crafted grid descriptors measured at 50% trajectory completion discriminate successful from failed runs within the same task (mean within-task best-feature AUC = 0.885, p < 0.001 under within-task label permutation). Most predictive content lies along a single grid-complexity axis. The result generalizes across solver architectures: a feature selected on one solver predicts success on the other with AUC 0.747-0.762 in all four transfer directions (p < 0.001, leakage controlled). On a pre-registered held-out set of 41 reliable tasks, the frozen feature n_components_final achieves AUC = 0.765 (95% CI [0.717, 0.810], p < 0.001), robust under task-clustered bootstrap resampling and cross-solver task collapsing. The signal is not explained by solver capacity (configuration-residualized AUC = 0.927 and 0.896 for beam search and SDFS, p < 0.001) and is only weakly coupled to score trajectories (R^2 approximately 0). Early stopping at 50% completion reduces beam-search compute by 33.6% while retaining 98.9% of solves; degenerate-trajectory detection reduces SDFS compute by 65.3% with no solve loss. Finally, on 229 of 400 evaluation tasks the DSL primitive library produces no valid transition from the input grid. This 0-step collapse is invariant to search budget and universally failed by beam search, indicating a DSL coverage limitation rather than a search-budget effect.

---


### 350. [Frequency Decoupled Framework for Screen Content Image Super-Resolution](https://arxiv.org/abs/2606.09029)

**<font color=#1a73e8>作者：</font>** Xufei Wang, Qicheng Zhang, Qi Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Methods based on implicit neural representations have demonstrated superior performance in Screen Content Image Super-Resolution (SCISR) . However, they overlooked the inherent frequency characteristics, leading to suboptimal performance. We propose a frequency decoupled framework (FDF) that rethinks SCISR from a phasor perspective by capturing structured energy in amplitude and relational continuity in phase, and jointly exploiting them with bespoke implicit representations to faithfully recover the regular textures and global configuration of Screen Content Image (SCI).
Amplitude-Phase Factorization Network (APFN) first separates images into amplitude and phase streams, where Amplitude Clustering Module (ACM) organizes sparse yet high-energy amplitude responses into representative prototypes for periodic pattern extraction, while Phase Consistency Self-Attention (PCSA) progressively reinforces configuration through continuous consistency propagation.
And Oscillation-Anharmonic Implicit Fitting Network (OAIF-Net) integrates periodic and coherent implicit representations for efficient exploitation of the periodic patterns and coherent context embedded in SCI.
Experimental results show FDF achieves state-of-the-art SCISR performance at multiple scales across four public SCI datasets. Ablation experiments further demonstrate the effectiveness of each component in extracting and exploiting periodic patterns and coherent context.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
