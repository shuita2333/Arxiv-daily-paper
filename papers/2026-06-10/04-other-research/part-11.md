# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-527**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-527**

---

### 501. [AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis](https://arxiv.org/abs/2606.09682)

**<font color=#1a73e8>作者：</font>** Jaber Jaber, Osama Jaber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AutoMegaKernel (AMK) compiles a HuggingFace Llama-family model into a single persistent cooperative CUDA kernel that runs the whole forward pass in one launch, with no per-model hand-written CUDA. The contribution is the system, not raw speed.
A frozen schedule-IR validator statically certifies deadlock-freedom and race-freedom via static graph checks (not a mechanized proof), so an unsafe agent-proposed schedule is rejected before launch: across 7,160 adversarial schedules (6,091 unsafe) it had zero false-accepts and accepted all 360 real lowerings. The same source retargets sm_80/sm_90/sm_120 from one codebase, auto-generates correct megakernels for 10 of 10 supported models, and on a real SmolLM2-135M checkpoint reproduces HuggingFace greedy decode token-for-token (perplexity match 2.5e-7). An unattended, agent-drivable autoresearch loop self-improves the megakernel over its own baseline (1.25-1.72x).
A search-found int8 (W8A16) megakernel beats CUDA-graphed cuBLAS bf16 at batch-1 decode across NVIDIA's datacenter inference fleet: L4 up to 1.33x, the current-gen L40S 1.25-1.27x, A10G up to 1.08x at scale, and the consumer RTX 5090 1.19-1.23x. The ordering is not a clean function of bandwidth (the 864 GB/s L40S beats the 600 GB/s A10G); the divide is inference-class vs training-class. AMK trails cuBLAS on the high-bandwidth training-class A100/H100, where the harness localizes the cross-SM-sync bottleneck; we report the gap plainly. This is a precision-asymmetric (W8A16 vs bf16) comparison at decode position 0; the largest real checkpoint is TinyLlama-1.1B. Code and the harness: this https URL

---


### 502. [Cranio-Diff: Diffusion-based Cross-domain Craniofacial Reconstruction with 2D X-ray Skull Guidance and Structural Identity Constraints](https://arxiv.org/abs/2606.09699)

**<font color=#1a73e8>作者：</font>** Ravi Shankar Prasad, Naresh Gurjar, Shashank Baghel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The state-of-the-art generative models, such as CycleGAN, Pix2Pix, and diffusion models have demonstrated remarkable performance in the face generation task. However, they fail to effectively capture cross-modality semantic information in craniofacial reconstruction when translating from the skull (x-ray) to the face (optical) domain, due to a mismatch in the alignment of structural identity across modalities. To address this issue, we propose Cranio-Diff, a diffusion-based framework for cross-domain cranio-facial reconstruction from 2D X-ray skull images. The proposed approach integrates skull-conditioned structural guidance through ControlNet with biometric text conditioning to generate a face which is more semantically and structurally aligned with the given skull. The proposed Cranio-diff method is evaluated on skull-face dataset obtained from X-ray scans of 120 subjects in lateral and frontal views. To enable controlled evaluation, each face image is synthesised across three age groups (25, 45, 65) and three BMI variations of -10%, baseline and +10%, yielding 4320 paired samples. To the best of our knowledge, this is the only X-ray-face dataset with this magnitude. Extensive experiments showed that the proposed method outperforms recent existing approaches in both generated image quality and retrieval task. Finally, to evaluate the performance of our proposed method, we have evaluated the quality of the generated image using FID, IS, SSIM, LPIPS, PSNR and ArcFace score. Additionally, retrieval performance is evaluated using recall@k, mAP@k and MRR@k. Obtained experimental results demonstrate that the proposed method can be used as an alternate tool in providing aid in forensic investigations.

---


### 503. [When Do Local Score Models Extrapolate Across Size? A Diagnostic Theory and Benchmark](https://arxiv.org/abs/2606.09705)

**<font color=#1a73e8>作者：</font>** Wenjie Xi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific generative modeling often requires size transfer, where models trained on small systems are evaluated on larger ones. While translation-invariant architectures enable this evaluation, we show that architectural locality alone does not guarantee stable size extrapolation. Instead, stable extrapolation is governed by the quasi-locality of the Gaussian-smoothed score. Through Tweedie's formula, far-away perturbations can influence local score components via posterior covariance, meaning a local model succeeds only if its receptive field covers the smoothed score's response range. We formalize this mechanism, proving a size-uniform comparison theorem for local marginals under reverse diffusion. We also introduce Finite-Depth Local Flow (FDLF), a white-box diagnostic benchmark with exact scores, densities, and controllable response ranges. Empirically, we validate the interplay between spatial mixing, smoothed-score quasi-locality, and model receptive fields. Under spatial mixing, the smoothed score remains quasi-local relative to the receptive field, enabling stable extrapolation. Conversely, when spatial mixing weakens, the score's locality rapidly degrades, causing size transfer to fail.

---


### 504. [BrainSurgery: Reproducible and Reliable Declarative Weight Manipulations for Model Editing and Upcycling](https://arxiv.org/abs/2606.09707)

**<font color=#1a73e8>作者：</font>** Gianluca Barmina, Annemette Broch Pirchert, Andrea Blasi Núñez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As deep learning models scale, managing, inspecting, and modifying large checkpoints has become increasingly challenging. Researchers often need to alter model weights for layer restructuring, precision casting, low-rank factorization, and architectural debugging, yet these workflows often rely on fragile ad-hoc Python scripts. Here, we introduce BrainSurgery, a tool for robust and reproducible "tensor surgery" on neural network checkpoints, and provide a system demonstration covering four examples and three case studies from model upcycling to LoRA extraction. By abstracting storage formats and memory management, BrainSurgery executes complex transformations through declarative YAML plans. It supports structural modifications, mathematical transformations, and tensor reshaping through expressive regex and structural targeting, while built-in assertions validate tensor shapes, data types, and values to prevent silent errors. We envision that BrainSurgery will provide a strong foundation for future research through its reproducible and validated operations.

---


### 505. [Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization](https://arxiv.org/abs/2606.09711)

**<font color=#1a73e8>作者：</font>** Mohammad Beigi, Ming Jin, Lifu Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward hacking is usually studied after it becomes visible, once a model earns high proxy reward while failing the intended task. We instead study what proxy RL teaches before that failure appears. We introduce Proxy Reward Internalization and Mechanistic Exploitation (PRIME), a learned capability to assess task correctness, predict proxy acceptance, and reason about exploitable proxy--gold gaps. In coding RL environments with exploitable pytest rewards, we measure PRIME through chain-of-thought monitoring, direct probes, and activation-level concept vectors. We find that PRIME emerges in a staged sequence before sustained reward hacking, and that its current direct-probe score forecasts later hack onset and severity even when the visible hack rate is still low. PRIME also adapts when the evaluator changes, retargeting to whichever proxy--gold gap remains rewarded and persisting when gold reward suppresses overt hacking, and ablating its activation directions reduces hacking. Across checkpoints, in-domain PRIME tracks out-of-domain misalignment. Together these results suggest that exploitable proxy RL amplifies a proxy-internalization capability upstream of visible hacking, making PRIME a candidate early-warning signal for broader alignment risk.

---


### 506. [Evaluating the Representation Space of Diffusion Models via Self-Supervised Principles](https://arxiv.org/abs/2606.09718)

**<font color=#1a73e8>作者：</font>** Xiao Li, Yixuan Jia, Zekai Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have demonstrated remarkable generative capabilities and have also emerged as powerful self-supervised representation learners, yet the connection between these two abilities remains less explored. Drawing inspiration from self-supervised learning (SSL), we introduce a framework for jointly evaluating the representation and generation capabilities of diffusion models. Specifically, we decompose features into invariant and residual components and derive the Invariant Contamination Ratio (ICR), a Fisher-based metric that quantifies how residual variation contaminates invariant signal in feature space. We use this framework to analyze both discriminative and generative behavior of diffusion models. On the representation side, we find that invariance peaks at intermediate noise levels, which also yield the best downstream classification performance. On the generative side, we study how training transitions from genuine generalization to memorization in data-limited regimes, and show that ICR serves as a sensitive training-time indicator of early learning: increasing residual energy along Fisher directions marks the onset of memorization, detectable from training features alone without external evaluators or held-out test sets. Overall, our results show that diffusion models can be monitored from a self-supervised perspective through the geometry of their learned representations.

---


### 507. [Disentanglement with Holographic Reduced Representations](https://arxiv.org/abs/2606.09725)

**<font color=#1a73e8>作者：</font>** Jhonny J. Velasquez Olivera, Christo K. Thomas, Walid Saad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Disentanglement, the separation of factors of variation in data using neural networks, remains a long-standing challenge in machine learning. Prior work has addressed this problem with variational autoencoders and generative adversarial networks that incorporate ideas from variational inference and information-theoretic constraints. In contrast to methods that rely on continuous representations, we propose a design that treats disentangled representations as symbolic structures, motivated by the compositional relationships among the concepts that make up samples from a distribution. However, learning discrete symbolic structures with neural networks while maintaining differentiability is difficult and often requires complex architectures. To address this, we introduce an unsupervised learning algorithm that uses holographic reduced representations (HRR) for neural disentanglement. We show that the HRR unbinding operation provides an inductive bias for separating factors and yields competitive results against baselines, as measured by latent traversals and disentanglement metrics. We complement these empirical findings with an information-theoretic analysis of the HRR unbinding channel. We prove that unbinding induces approximately independent symbol-value pairs and derive a per-slot capacity bound that quantifies how many distinct symbolic concepts can be reliably encoded, giving a quantitative account of the inductive bias toward disentanglement. The resulting representations differ from standard autoencoder-based models, in that their latent units are vectors that are summed together, rather than scalar dimensions of a low-dimensional latent vector. We show that this HRR representation is more robust to noise than other disentangled representations and maintains reconstruction quality across a range of SNRs.

---


### 508. [Tight Sample Complexity of Transformers](https://arxiv.org/abs/2606.09731)

**<font color=#1a73e8>作者：</font>** Chenxiao Yang, Nathan Srebro, Zhiyuan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We tightly characterize the VC dimension of depth-$L$ Transformers with a total of $W$ parameters, mapping an input sequence of length $T$ to a single output, establishing an upper bound of $O(L W \log (T W))$ and a nearly matching lower bound of $\Omega(L W \log (T W / L))$. We further tightly characterize the sample complexity of chain-of-thought learning using such a Transformer, showing teacher forcing (i.e. selecting a predictor consistent with the entire chain-of-thought on training data) learns with sample complexity $O\left(L W \log \left(\left(T+T^{\prime}\right) W\right)\right)$ and that any learning rule that uses chain-of-thought data requires at least $\Omega\left(L W \log \left(\left(T+T^{\prime}\right) W / L\right)\right)$ examples, where $T$ is the input length and $T^{\prime}$ is the number of autoregressive steps.

---


### 509. [Learning Dynamics Reveal a Hierarchy of Weight-Induced Layerwise Gram Metrics](https://arxiv.org/abs/2606.09744)

**<font color=#1a73e8>作者：</font>** Claudio Nordio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study feed-forward ReLU networks with fixed readout and quadratic loss. The aim is to rewrite gradient descent not primarily as a dynamics in weight space, but as a collective dynamics closed in terms of fields defined on the training-set space. For a single hidden layer, the weight variables can be eliminated from the activation dynamics, yielding a closed equation for the residuals governed by a collective kernel that factorizes into an input-geometric matrix and a dynamical co-activation matrix. For deeper networks, the residual dynamics retains a clean layer-wise kernel structure. However, from depth three onward, closure requires a hierarchy of weight-induced Gram operators that mediate information transport across layers.

---


### 510. [Hybrid Robustness Verification for Spatio-Temporal Neural Networks](https://arxiv.org/abs/2606.09746)

**<font color=#1a73e8>作者：</font>** Sherwin Varghese, Matthew Wicker, Alessio Lomuscio  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With AI increasingly deployed in safety-critical systems, providing formal robustness guarantees for the underlying models is essential. Existing verification methods either rely on overly conservative approximations or incur prohibitive computational costs. For example, the use of lp-norm perturbations in video settings encodes the belief that the adversary can inject noise in every video frame. In practice, adversarial perturbations exhibit structured spatial and temporal correlations, constrained to lower-dimensional, semantically meaningful subspaces. In this work, we study robustness verification of 3D CNNs processing video and volumetric inputs, targeting applications in action recognition (UCF-101), autonomous driving (Udacity), and medical imaging (MedMNIST) exploiting realistic assumptions on adversarial strength by modelling them as spatio-temporal constraints - where the attacker can modify either a subset of frames or patches within a set of consecutive frames. We demonstrate that modelling realistic constraints enables tighter approximations. We introduce Spatio-Temporal Bound Propagation (STBP), a verification framework that computes an exact closed-form characterization of the first convolutional layer and propagates certified bounds through subsequent layers using scalable approximations. Computing the exact closed form provides the tightest bounds for the first convolutional layer. Thus, we utilise approximation methods in the remainder of the network. To spur further progress in this field, we propose ST-Bench, a verification benchmark for autonomous driving and activity recognition, to systematically evaluate verifiable robustness. Compared to existing verification-based approaches, STBP provides stronger robustness guarantees with significantly improved scalability, achieving 1.7x higher certified robust accuracy under identical perturbation budgets.

---


### 511. [Multi-Turn Evaluation of Deep Research Agents Under Process-Level Feedback](https://arxiv.org/abs/2606.09748)

**<font color=#1a73e8>作者：</font>** Rishabh Sabharwal, Hongru Wang, Amos Storkey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for deep research agents (DRAs) assess only single-shot outputs, ignoring a key question: can DRAs improve their reports when guided by feedback? To investigate this, we conduct a multi-turn evaluation of DRAs under two feedback settings: self-reflection, in which the agent revises its report without any external diagnostic signal, and process-level feedback, in which the agent receives guidance targeting gaps in its research strategy. To enable process-level feedback, we design Research Gap Inference (RGI), a method that analyzes patterns of satisfied and unsatisfied rubric criteria to infer research-process gaps. Our analysis reveals three key findings: (i) under self-reflection, agents incorporate and regress on rubric criteria at nearly equal rates, yielding negligible net improvement; (ii) a single round of process-level feedback yields substantial gains, raising the normalized score by approximately $8$-$15$ points and yielding a roughly $35$-$40\%$ incorporation rate; (iii) these gains do not compound over subsequent turns, as agents regress on up to $24\%$ of previously satisfied criteria when rewriting the full report to address remaining gaps. Even with targeted guidance, reliable multi-turn improvement remains out of reach for the DRA architectures we evaluate. Our code and results are publicly available at this https URL.

---


### 512. [Collaborative Human-Agent Protocol (CHAP)](https://arxiv.org/abs/2606.09751)

**<font color=#1a73e8>作者：</font>** Arsalan Shahid, Gordon Suttie, Philip Black  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models are moving from response generation into operational roles. They plan across steps, call tools, request human input, coordinate with other agents, and increasingly carry responsibility for work that affects customers, claims, code, contracts, and clinical decisions. Production deployments are no longer one human supervising one model. They are multi-human, multi-agent collaborations that cross teams, time zones, and trust boundaries. The technical surface for this collaboration remains weakly specified. When an agent drafts a response and a human edits it before it ships, the moment of human judgement is the most valuable signal in the system. In current practice it is recorded, if at all, in application code, chat threads, ticket comments, and tribal memory. Two protocol standards address adjacent concerns: MCP standardises agent access to tools and data, and A2A standardises agent-to-agent interoperability. Neither defines the shared workspace in which humans and agents perform accountable work together. This paper presents CHAP, the Collaborative Human-Agent Protocol. Under CHAP, the override that used to vanish into a chat thread becomes a structured event carrying a diff, a rationale, and a content hash. The handoff between shifts becomes a portable envelope rather than a pinned message. The human approval of an agent's draft becomes a non-repudiable signed decision that can be replayed years later. The protocol achieves this through a small Core (workspaces, participants, tasks, artefacts, and an append-only evidence log) together with composable profiles that add review, modes, routing, deliberation, handoff, identity, signatures, and transparency-backed audit as deployments require them. Specification, reference implementation, conformance suite, and worked examples are available at: this https URL

---


### 513. [Perturbative Contrastive Physical Learning](https://arxiv.org/abs/2606.09756)

**<font color=#1a73e8>作者：</font>** Kyungeun Kim, Amanuel Anteneh, Israel Klich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Responses to perturbations are key to understanding physical systems. The ability to contrast such responses by comparing how a system reacts under slightly different conditions provides a mechanism for learning. Here, we introduce Perturbative Contrastive Physical Learning (PCPL), a general framework in which learning emerges from measurable contrasts between physical states produced by controlled changes to inputs, boundary conditions, parameters, or interpreter functions. PCPL unifies and extends prior approaches: Equilibrium Propagation is rooted in contrasts between free and nudged equilibria in energy-based systems, while Frequency Propagation corresponds to contrasts extracted from sinusoidally driven, frequency-demodulated responses. We show that contrast-driven updates can reflect either local sensitivities or global inverse-problem structure, yet do not require centralized gradient computation. Instead, effective learning geometry emerges implicitly from the system's own physical response, allowing learning behavior to arise without an external processor or explicit backpropagation. We demonstrate PCPL in two platforms: (i) spring networks that update bond stiffness using measured displacements and forces, and (ii) continuous-variable photonic circuits trained via x quadrature measurements and finite-difference estimates of the Jacobian. Both platforms successfully learn classification tasks. We further show that a continuous-variable photonic circuit can be trained to implement analog multiplication, illustrating a step toward more autonomous physical learning systems.

---


### 514. [Preserving Plasticity in Continual Learning via Dynamical Isometry](https://arxiv.org/abs/2606.09762)

**<font color=#1a73e8>作者：</font>** Andries Rosseau, Robert Müller, Ann Nowé  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual training of deep neural networks under non-stationarity often leads to a progressive loss of plasticity, eventually limiting further learning. We relate plasticity to the empirical Neural Tangent Kernel, and identify dynamical isometry (the condition that layer-wise Jacobian singular values remain close to one) as a key mechanism for preserving plasticity in continual learning. We revisit a class of networks that are almost-everywhere isometric while remaining universal Lipschitz function approximators, demonstrating that near-dynamical isometry is compatible with expressive nonlinear representations. For general architectures, we propose an efficient isometry-promoting regularization scheme and identify a novel mechanism by which it can reactivate dormant ReLU units. Building on this, we introduce AdamO, an Adam-style adaptive optimizer that decouples isometry regularization from gradient updates, analogous to AdamW. We further reinterpret prior plasticity-preserving approaches through the lens of dynamical isometry, showing that they target only a partial measure of isometry. Across supervised and reinforcement-learning continual-learning benchmarks designed to induce plasticity loss, our methods consistently match or outperform existing approaches.

---


### 515. [iOSWorld: A Benchmark for Personally Intelligent Phone Agents](https://arxiv.org/abs/2606.09764)

**<font color=#1a73e8>作者：</font>** Lawrence Keunho Jang, Mareks Woodside, Geronimo Carom 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A useful phone agent needs to be personally intelligent. It should reason over a user's identity, history, and preferences as they exist on the device, not just follow isolated instructions in an impersonal sandbox. Existing mobile agent benchmarks lack this kind of personalization. We introduce iOSWorld, the first interactive native iOS simulator benchmark built around a persistent user identity spanning 26 newly built iOS apps. These apps contain connected data such as transactions, messages, travel records, social relationships, and financial activity. iOSWorld includes 133 tasks across three increasingly difficult categories. Single-app tasks (27) test one app, multi-app tasks (60) span 2 to 8 apps, and memory and personalization tasks (46) require agents to infer patterns from personal data. We evaluate frontier and open-source computer-use models in both vision-only and privileged vision+XML settings. The best configuration reaches 52\% overall but only 37\% on multi-app tasks. Privileged vision+XML access improves frontier models by up to 26 percentage points, while smaller models do not benefit from added accessibility-tree input. We release iOSWorld as an open-source benchmark with all apps, seeded data, tasks, rubrics, and evaluation code.

---


### 516. [SIGA: Self-Evolving Coding-Agent Adapters for Scientific Simulation](https://arxiv.org/abs/2606.09774)

**<font color=#1a73e8>作者：</font>** Matthew Ho, Brian Liu, Jixuan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advanced scientific simulators expose specialized input languages that turn simulation goals into executable configurations, but learning them can cost domain scientists hours to days. We study simulator setup as a problem of agent-tool interface grounding: what minimal simulator-specific adaptations are needed for an off-the-shelf coding agent to operate real scientific software? Our intuition is that coding agents already know how to navigate files, edit code, run commands, and repair outputs, but they lack the simulator's executable contract: its vocabulary, structural constraints, validation rules, and termination conditions. We introduce SIGA, a Simulator-Interface Grounding Adapter that supplies this contract through retrieval, procedural memory, in-trajectory validation, and validation-enforced termination. We primarily evaluate SIGA on GEOS, an open-source multiphysics simulator used in subsurface science. SIGA produces a complete GEOS deck in about five minutes with TreeSim above 0.90, matching an extended-budget human expert who took about three hours, a roughly 36x wall-clock speedup. On a harder held-out set, grounding raises TreeSim from 0.720 to 0.789, a roughly 10% relative gain over the bare agent, and can reduce the across-seed standard deviation by 16x. Self-evolution further improves SIGA by rewriting adapter contents from prior trajectories, yielding the highest held-out GEOS mean and matching or outperforming the strongest hand-designed configuration. Transfers to OpenFOAM and LAMMPS show that the dominant mechanism shifts by interface: validation matters most when structural completeness is the bottleneck, while memory and retrieval matter most when domain correctness is the bottleneck. These results suggest that lightweight, self-improvable grounding layers can turn general coding agents into practical operators of scientific software.

---


### 517. [Cohort-based Semantic Labeling: AI-Enabled Recovery of Visualization Semantics from Deployed SVGs](https://arxiv.org/abs/2606.09782)

**<font color=#1a73e8>作者：</font>** Jeongah Lee, Hima Varshini Surisetty, Durga Nirmaleswaran 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Many web-based visualizations are deployed as Scalable Vector Graphics (SVG), a format that faithfully preserves visual appearance but typically omits the higher-level semantic structure needed for machine interpretation. Once rendered and published, information about a visualization's components, roles, and encodings is no longer explicitly available, limiting downstream operations such as querying, accessibility augmentation, explanation, personalization, and transformation. To address this gap, we introduce CSL, an AI-enabled, multi-stage pipeline for automatically recovering visualization semantics from deployed SVGs through two complementary mechanisms: (1) cohort-based decomposition, which organizes heterogeneous SVG primitives into structurally coherent subsets that reduce the semantic assignment space, and (2) hybrid semantic grounding, which combines model-based inference with deterministic structural validation and propagation to make labeling both context-sensitive and structurally anchored. CSL produces Semantic SVG (SSVG), a representation in which SVG elements are annotated with graphical mark type, visualization role, and data role. We implemented CSL as an end-to-end prototype and evaluated it on 102 SVG visualizations, achieving global macro-averaged accuracies of 0.822 for mark type, 0.853 for visualization role, and 0.860 for data-role recovery. An ablation against a non-cohort whole-chart baseline showed that cohorting significantly improves accuracy (paired t-test: t > 20, p < 0.001; Cohen's d > 2.0), and repeated labeling of a randomly selected SVG over 100 runs yielded mean agreement above 91.9% across all three attributes. These results provide strong evidence that CSL can transform deployed SVGs into machine-usable semantic representations, enabling more accessible, adaptive, and user-steerable visualization systems.

---


### 518. [Zero Touch Predictive Orchestration: Automating Time-Series Models for the Cloud-Edge Continuum](https://arxiv.org/abs/2606.09787)

**<font color=#1a73e8>作者：</font>** Abd Elghani Meliani, Arora Sagar, Adlen Ksentini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Cloud-Edge Continuum (CEC) enables latency-critical applications by distributing resources to the far edge, but its extreme volatility makes proactive Zero Touch Management via time-series forecasting essential. However, orchestrators face a severe "cold start" problem: newly discovered nodes lack the historical data required to train localized predictive models, while generalized models fail to capture unique hardware and microservice behaviors. To solve this, we propose a fully automated time-series prediction architecture driven by a novel data-mixing methodology. At the infrastructure level, we introduce a lightweight, technology-agnostic Resource Exposer (RE) that dynamically discovers nodes and continuously collects customizable telemetry (e.g., compute, network, energy). To overcome the sparsity of these initial local samples, our framework automatically merges them with TimeTrack, our publicly available, high-resolution dataset collected at 45-second intervals. This synergizes TimeTrack's foundational, high-frequency temporal patterns with the precise calibration of the local node data. Processed through a Neural Architecture Search (NAS) engine, the system automatically generates highly accurate baseline models. Experimental results demonstrate that merging the target data with TimeTrack effectively mitigates the cold start challenge. This integration significantly improves forecasting accuracy measured in Mean Squared Error (MSE), Mean Absolute Error (MAE), and Mean Absolute Percentage Error (MAPE) and accelerates convergence compared to training on the sparse local samples alone, training solely on generic datasets, or mixing the target data with standard alternative datasets, establishing a robust foundation for continuous MLOps deployment.

---


### 519. [POTATR: A Lightweight Image-to-Graph Model for Page-Level Table Extraction](https://arxiv.org/abs/2606.09788)

**<font color=#1a73e8>作者：</font>** Brandon Smock, Libin Liang, Max Sokolov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale document processing requires contextually aware table extraction (TE) that is both accurate and efficient. Yet current approaches require billions of parameters, hundreds of autoregressive steps, or costly API inference. Motivated by this, we introduce the Page-Object Table Transformer (POTATR), a lightweight 29M parameter image-to-graph model that extends the Table Transformer (TATR) for contextualized page-level TE. POTATR outperforms all models tested on the PubTables-v2 Single Pages benchmark -- including frontier MLLMs -- achieving $\textrm{GriTS}_\textrm{Con}$ of 0.964 while running over 130$\times$ faster at roughly 300$\times$ lower cost. Further, POTATR's output is spatially grounded: every recognized element has a bounding box, enabling visual verification and geometric text assignment. As a result, POTATR performs unified page-level TE while composing with other models, enabling extension to scanned documents via external OCR and to full-document TE via techniques like cross-page merging. Code and models will be released.

---


### 520. [End-to-End Optimization of Incoherent Imaging for Classification Under Detector-Limited Readout](https://arxiv.org/abs/2606.09792)

**<font color=#1a73e8>作者：</font>** Archer Wang, Joshua Chen, Sachin Vaidya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end co-optimization of optical front-ends (e.g. metasurfaces) and neural network back-ends has been widely applied to imaging tasks, yet a formalism characterizing when and why such systems outperform conventional lens-based imaging is largely lacking. This paper focuses on object classification, a central imaging task, and asks when end-to-end optimization of a phase mask for incoherent imaging improves performance over a conventional focusing lens. We find that these gains arise primarily under constrained detector readout and are limited under full detector readout. In the latter setting, we prove that no incoherent phase mask exceeds the ideal-channel mutual information between detector measurements and class labels; a conventional focusing lens approaches this ceiling, and joint optimization yields no empirical gain. When detector readout is constrained -- by coarse spatial sampling or a limited number of measurements -- optimized optics can substantially improve classification by increasing class separability in the detector measurements. These gains are largest under low detector noise and shrink as noise grows, because the optics shape the signal before it reaches the detector but cannot remove noise added afterward. The advantage also depends on the spectral structure of the task: co-design helps most when class-discriminative content is concentrated at lower spatial frequencies than within-class variation. We develop a theoretical framework formalizing these distinctions and test its predictions on synthetic data and standard benchmarks (MNIST, FashionMNIST, SVHN).

---


### 521. [Beyond Spherical Harmonics: Rethinking Appearance Models for Radiance Reconstruction](https://arxiv.org/abs/2606.09794)

**<font color=#1a73e8>作者：</font>** Ewa Miazga, Jorge Condor, Piotr Didyk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> View-dependent appearance modeling remains a challenging problem in novel-view synthesis and reconstruction. Accurately representing complex angular effects often requires substantial memory and computational resources. For new learning-based methods, a common approach is to rely on SH. However, capturing high-frequency phenomena such as specular reflections demands high-order expansions, which increase memory usage and computational cost. Consequently, most methods employ low-order SH, which limits the ability to model complex view-dependent effects, resulting in overly smooth or diffuse representations. To address these limitations, we systematically evaluate a wide range of spherical functions in the context of scene reconstruction. Some of them are introduced to graphics and computer vision for the first time in this paper. Based on the insights from the experiment, we develop a novel spherical formulation, the Normalized Anisotropic Spherical Gabor function that enables efficient modeling and learning of high-frequency appearance effects while maintaining compact representation. Compared to existing approaches, our function achieves higher-quality reconstruction of view-dependent phenomena such as glints, while being up to five times more memory-efficient and more efficient to evaluate. We validate its performance in radiance-field reconstruction tasks.

---


### 522. [Bandits for Efficient Experimentation: Adapting to Control Group, Preferences, and Context Drifts](https://arxiv.org/abs/2606.09802)

**<font color=#1a73e8>作者：</font>** Udvas Das, Waris Radji, Debabrota Basu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider a variant of the linear contextual stochastic multi-armed bandits, where the learner must provide recommendations to a group of users, each having its personalized preference vector, and in the presence of context distributions that are drifting over time. Under practitioner-friendly assumptions, we reduce this setting to linear bandit with stationary mean but heteroskedastic and non-stationary noise. We further study the case when the learner must ensure the mean reward of each decision must exceed that of a baseline strategy $\boldsymbol{\pi}_0$ at each decision step. We introduce Dri-MED, an algorithm inspired from the linear version of the MED strategy, and carefully adapted to handle the non-stationary heteroskedastic noise. We show that the instance-dependent regret scales as $\tilde{\mathcal O}\left(\frac{\kappa}{\tilde{\Delta}}d^2(\log(T)\right)$, where $\tilde{\Delta}$ is the constraint-aware sub-optimality gap subject to policy $\pi_0$, with variance-aware multiplicative term $\kappa$ that we carefully handle using heteroskedastic regression. We further show Dri-MED enjoys $\tilde{\mathcal{O}}(d)$ expected constraint violations. Our numerical results suggest that Dri-MED significantly outperforms conservative baselines that ignores the drift and preference structure.

---


### 523. [Topological Neural Operators](https://arxiv.org/abs/2606.09806)

**<font color=#1a73e8>作者：</font>** Lennart Bastian, Samuel Leventhal, Mustafa Hajij 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Topological Neural Operators (TNOs), a principled framework for operator learning on cell complexes that lifts neural operators (NOs) from functions on points and/or edges to topological domains. TNOs represent data as features defined on cells of varying dimension and model their interactions through Discrete Exterior Calculus, enabling explicit cross-dimensional coupling via gradient-, curl-, and divergence-type operators. The key design principle is to decouple where information flows, as governed by fixed topological operators, from how it is transformed (which is learned), yielding models that respect the geometric support of physical quantities and expose conservation and compatibility structure. We further propose Hierarchical TNOs (HTNOs), which incorporate learned coarse complexes to propagate long-range and topology-dependent information. Our framework subsumes existing NOs as a special case, providing a unified perspective on operator learning across discretizations. Across a range of PDE benchmarks, including irregular-geometry flow problems, TNOs and HTNOs improve accuracy; controlled studies further isolate the benefits of native higher-rank and topological structure. Project page: this https URL

---


### 524. [Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting](https://arxiv.org/abs/2606.09809)

**<font color=#1a73e8>作者：</font>** Avijit Ghosh, Anka Reuel, Jenny Chim 等 48 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI evaluation results are produced at scale but reported inconsistently across leaderboards, model cards, benchmark papers, and company blogs. The cost is interpretive: readers cannot reliably compare results across sources, identify what a report omits, or trace an aggregate claim to its underlying evidence. Recent efforts address isolated components but leave three gaps: they cover only narrow slices of the evaluation lifecycle and do not compose into a single interpretable record; they specify static representations that do not differentiate the questions different stakeholders bring to the same evidence; and they remain proposals on paper, lacking the extraction infrastructure required for adoption at scale. We present \EvalCards{}, an operational reporting layer that composes benchmark metadata, evaluation run data, and model metadata into a unified record. We (1) derive a reporting schema from a structured review of 52 papers and 10 stakeholder interviews, (2) implement four interpretive signals (reproducibility, documentation completeness, provenance and risk, and score comparability), rendered through reader modes calibrated to research and non-research audiences, and (3) deploy a monitoring tool that applies \EvalCards{} across 5,816 models, 635 benchmarks, and 101,843 results, surfacing systematic gaps in current reporting practice.

---


### 525. [PTL-Diffusion: Manifold-Aware Diffusion with Periodic Terminal Laws](https://arxiv.org/abs/2606.09816)

**<font color=#1a73e8>作者：</font>** Danqi Zhuang, Jisui Huang, Xiaoyue Xi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard diffusion models typically use a single time-homogeneous Gaussian terminal distribution as the reference law for generation. While this choice is analytically convenient and empirically powerful, it provides little explicit structure for data concentrated near low-dimensional manifolds, where different regions of the data distribution may correspond to distinct local geometric or semantic factors. As a result, the reverse model must recover manifold-level structure almost entirely from an unstructured terminal reference distribution.
We propose PTL-Diffusion, a proof-of-concept diffusion framework whose forward noising process converges to a nonconstant periodic family of Gaussian terminal laws rather than to a single invariant law. Unlike a phase-conditioned DDPM, where phase information only enters the denoising network while the forward process remains unchanged, PTL-Diffusion embeds phase structure directly into the forward noising dynamics.
The proposed construction remains close to standard denoising diffusion models: for a periodically forced Ornstein--Uhlenbeck-type forward process, we derive closed-form forward marginals, the limiting periodic Gaussian terminal family, and explicit Gaussian reverse posteriors, enabling standard noise-prediction training. We also introduce an invariant-average regularization term coupling the phase-conditioned reverse dynamics through the averaged periodic reference law. Experiments on torus and cylinder point-cloud benchmarks and the Olivetti face dataset show that PTL-Diffusion improves manifold-level distributional matching over matched DDPM baselines, reducing phase-conditioned errors, feature-space covariance errors, and nearest-neighbour manifold distances. These results suggest structured terminal reference laws as a promising direction, while motivating more expressive phase constructions and larger-scale evaluations.

---


### 526. [Causally Evaluating the Learnability of Formal Language Tasks](https://arxiv.org/abs/2606.09822)

**<font color=#1a73e8>作者：</font>** Vésteinn Snæbjarnarson, Anej Svete, Josef Valvoda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models, as multi-task learners, acquire a wide range of abilities during training. A fundamental question is how much task-specific data is needed to learn a given task. Answering this for natural language is difficult: tasks are hard to delineate and can confound one another. To rigorously investigate the relationship between data frequency and learnability, we turn to a controlled setting using formal languages induced from probabilistic finite automata. These serve as a methodological testbed to demonstrate that standard correlational evaluation practices are inherently flawed. To enable causal analysis, we introduce the binning semiring, an algebraic object that lets us control how often a targeted property occurs in a sampled corpus. We formulate the experimental pipeline as a causal graphical model and derive decomposed Kullback-Leibler divergence metrics to measure the learnability of specific sub-tasks. Our experiments show that evaluating learnability without causal intervention leads to incorrect conclusions due to confounders in correlational analysis, and serve as a warning about correlational pitfalls in natural-language settings.

---


### 527. [An Agency-Transferring Model-Free Policy Enhancement Technique](https://arxiv.org/abs/2606.09825)

**<font color=#1a73e8>作者：</font>** Anton Bolychev, Georgiy Malaniya, Sinan Ibrahim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training reinforcement learning (RL) policies from scratch is
costly: it requires careful reward and environment design,
extensive tuning, and substantial computation.
Yet many control problems already have a functional but
suboptimal policy available as a baseline.
This paper proposes a method for embedding such a baseline into
the RL training process, simultaneously improving training
efficiency relative to from-scratch methods and producing a
learning policy that outperforms the baseline.
At each step, the method arbitrates between the baseline policy
and a trainable learning policy, initially relying strongly on
the baseline policy and then progressively transferring agency to
the learning policy.
By the end of training, the learning policy is a standalone
neural network that operates without baseline policy support.
The paper formalizes what it means for the baseline policy to be
functional: under this policy, the agent reaches a goal set and
remains there with high probability.
The proposed arbitration mechanism is designed to exploit this
property during training, yielding high goal-reaching rates right
from the beginning of training.
A theoretical analysis provides a formal interpretation of this
behavior under stated assumptions and extends it to the final
baseline-free regime, where explicit lower bounds are derived for
the goal-reaching probability of the standalone learning policy.
Empirical results on continuous-control benchmarks show that the
proposed method achieves returns that match or exceed those of
competitive approaches, while maintaining the highest
goal-reaching rates throughout training among the compared
methods -- including in the final stage, where the learning policy
operates without any baseline support.

---


> [!TIP]
> 当前位于：**501-527**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-527**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
