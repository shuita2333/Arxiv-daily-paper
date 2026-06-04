# 📦 其他研究 | 2026年06月05日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

---

### 101. [Implicit Fuzzification via Bounded Noise Injection for Robust Medical Image Segmentation](https://arxiv.org/abs/2606.04427)

**<font color=#1a73e8>作者：</font>** Bisheng Tang, Zhangfeng Ma, Chuchu Zhai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image segmentation remains fundamentally limited by boundary ambiguity arising from sampling-induced information loss and inherent uncertainty in pixel-wise labeling. Although encoder-decoder architectures such as U-Net achieve strong performance, they often produce overconfident predictions that fail to capture transition-region ambiguity. To address this issue, we propose \textbf{NoiseUNet}, a simple yet effective framework that injects bounded perturbations into skip connections to regularize cross-scale feature fusion. This mechanism enforces robustness to local feature variations and promotes boundary-aware representations. Theoretically, the perturbation induces an implicit fuzzification effect, yielding soft, data-driven memberships without requiring explicit fuzzy modeling. We further introduce \textbf{ThyR}, a real-world thyroid ultrasound dataset with inherently ambiguous boundaries. Experiments demonstrate that NoiseUNet consistently improves both segmentation accuracy and boundary fidelity.

---


### 102. [When Chatbots Accommodate: What AI Companions Optimize for in Vulnerable Conversations](https://arxiv.org/abs/2606.04431)

**<font color=#1a73e8>作者：</font>** Minh Duc Chu, Yifan Wu, Zhiyi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Millions turn to AI companion chatbots during loneliness, grief, and personal crises. How these companion platforms respond in such moments can shape the trajectory of a user's vulnerable state. Yet we lack tools to characterize what each platform actually does when users open up. Existing audits score reactions to pre-defined crisis prompts and miss the underlying decision policy that governs sustained interaction. We address these gaps with two key contributions. First, we introduce the AI Companion Vulnerability-Response Taxonomy, a paired taxonomy of user vulnerability and chatbot response designed for analyzing extended companion chatbot interactions. Second, we infer the response policy each platform follows across distinct vulnerability scenarios by applying Inverse Reinforcement Learning to ~48k turns of real-world user conversations with GPT-4.1, this http URL, and Replika. Our findings reveal what AI companions prioritize in conversations with vulnerable users: GPT-4.1 reaches for advice, this http URL spreads its response across different strategies without a dominant mode, and Replika consistently asks questions and stays present. Each, however, downweights the responses that introduce corrective friction: GPT-4.1 probes less as conversations continue and when interacting with psychologically high-risk users; Replika advises bonded users more and challenges them less; this http URL shows no committed engagement strategy on internal distress. Estimated policies are invisible to output-level audits, providing a new lens for auditing chatbots in the wild and enabling more realistic safety evaluation.

---


### 103. [DSA: Dynamic Step Allocation for Fast Autoregressive Video Generation](https://arxiv.org/abs/2606.04432)

**<font color=#1a73e8>作者：</font>** Thanh-Tung Le, Yunhan Zhao, Menglei Chai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers have achieved state-of-the-art visual quality, but their high inference cost remains a major bottleneck for real-time applications. Recent distillation frameworks produce autoregressive video diffusion models with reduced latency, yet these models still use a fixed number of denoising steps per frame, wasting computation on predictable frames and under-refining challenging ones. We present DSA, a confidence-guided adaptive computation framework for AR video diffusion. DSA introduces a lightweight confidence head, trained jointly with the generator under a distribution-matching distillation objective, to estimate per-frame denoising reliability. At inference, this confidence signal dynamically adjusts the number of diffusion steps: simple frames terminate early for speed, while complex frames receive additional refinement. Our method requires no extra video data, no heuristics, and little architectural modification. Experiments show that DSA achieves real-time autoregressive video generation, reaching 22.63 FPS with sub-second latency on H100 GPUs, while maintaining competitive or superior VBench quality compared to recent autoregressive and bidirectional video diffusion models. Our results demonstrate that confidence-guided adaptive sampling provides an effective and practical path toward interactive video generation.

---


### 104. [3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436)

**<font color=#1a73e8>作者：</font>** Jiaxin Shi, Xidong Zhang, Fucai Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a 3D-thinking-guided co-training framework that enables vision-language-action (VLA) models to perform 3D spatial reasoning implicitly during action prediction. Our core insight is that 3D geometry perception and 3D spatial reasoning are distinct capabilities that can be disentangled and injected at different feature hierarchies. During training, three tightly coupled components work in concert primarily within the latent space: (1) To gain geometric priors, a latent 3D geometry perception module aligns intermediate visual features with a 3D foundation model, acquiring low-level geometric cues without architectural modifications to the VLM backbone. (2) Complementing this, an online 3D reasoning distillation module mitigates the prompt-induced reasoning gap via a shared reasoning anchor token. During 3D VLM co-training, this anchor is emitted as the first output token to robustly encode spatial priors. During VLA training, it serves as an input token inserted between the task and action instructions, transferring high-level spatial thinking from explicit teacher reasoning prompts to student action prompts without chain-of-thought text generation. (3) These disentangled geometric and reasoning features are then united by a spatially augmented action integration, which jointly injects them into the action-query tokens as hierarchical spatial conditions to prevent action shortcuts. At deployment, our method retains only its lightweight adapters to perform implicit 3D reasoning, discarding the 3D foundation model and the teacher branch used for supervision. Consequently, it operates purely on 2D images without 3D sensors, external models, or explicit text generation while preventing catastrophic forgetting of the pretrained VLM, achieving state-of-the-art performance on LIBERO, LIBERO-PLUS, SimplerEnv, and real-world manipulation tasks.

---


### 105. [INTACT: Ego-Guided Typed Sparse Evidence Retrieval for Heterogeneous Collaborative Perception](https://arxiv.org/abs/2606.04437)

**<font color=#1a73e8>作者：</font>** Chen Li, Shengrong Yuan, Jialong Zuo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative perception extends the perceptual range of autonomous vehicles by sharing information across agents, but heterogeneous sensors and perception models make intermediate feature fusion difficult to deploy at scale. Existing heterogeneous collaboration methods typically follow a translation-first paradigm: collaborator features must be aligned, adapted, or projected into an ego-compatible space before fusion. Such feature-compatibility contracts improve fixed-system performance, but they couple deployment to collaborator-specific adaptation and make newly joined heterogeneous agents costly to integrate. To address this gap, we propose INTACT, an ego-guided typed sparse evidence retrieval framework for heterogeneous collaborative perception. Instead of translating an entire collaborator feature map, INTACT lets the ego vehicle issue typed evidence queries that express suspected objects and evidence-deficient regions. Collaborators respond only with local evidence at queried locations, and the ego selects useful responses through sparse per-query routing and injects them through gated residual write-back. This changes the compatibility requirement from global feature-map interpretability to local, typed response comparability under ego-issued queries, enabling a zero-training heterogeneous insertion protocol in which the ego interface is trained once and new collaborators join through checkpoint merging. Extensive experiments on simulated and real-world heterogeneous collaborative perception benchmarks validate the effectiveness and deployability of INTACT. On OPV2V-H, INTACT achieves 80.1 AP70 with only 0.52M additional parameters and 18.0 $\log_2$ communication volume, corresponding to about 16$\times$ compression over dense feature transmission. On DAIR-V2X, INTACT achieves 43.8 AP50 under challenging real-world conditions.

---


### 106. [MemoryDocDataSet: A Benchmark for Joint Conversational Memory and Long Document Reasoning](https://arxiv.org/abs/2606.04442)

**<font color=#1a73e8>作者：</font>** Qiyang Xie, Jialun Wu, Xinjie He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly need to combine two demanding capabilities: navigating multi-session conversation history and performing deep reading comprehension within long documents. Yet no existing benchmark evaluates both simultaneously. We introduce MemoryDocDataSet, a synthetic benchmark of 50 micro-worlds and 1,000 QA pairs in which each instance comprises 3-5 personas, a temporal event graph spanning months of activity, 3-5 real long documents (20,000-50,000 tokens each sourced from the Caselaw Access Project), multi-session conversations grounded on those documents, and 20 question-answer pairs across five reasoning categories. The defining feature is the Hybrid source tag: questions requiring a system to first navigate conversation history to identify which document is relevant, then extract the answer from within that document. Hybrid questions account for 75.1% of the dataset. Dataset quality is characterised through a prompt-sensitivity self-consistency analysis using LLM-as-judge, yielding a median Cohen's $\kappa = 0.634$ across all 50 micro-worlds. We evaluate six baseline configurations spanning truncated context, long-context LLMs, retrieval-augmented generation (RAG), and memory systems. The best baseline (RAG-Both) achieves 0.358 overall F1 and 0.342 on Hybrid. Document-only retrieval (RAG-Doc) collapses to 0.267 on Hybrid despite achieving 0.453 on Doc-only questions, demonstrating a clear joint-retrieval gap that motivates architectures unifying conversational memory with long-document navigation. We release the dataset, generation pipeline, and all baseline implementations.

---


### 107. [What Can Verifiable Decapsulation Tests Certify? Pass Bounds and Fault-Recognition Limits for FO-Based KEMs](https://arxiv.org/abs/2606.04443)

**<font color=#1a73e8>作者：</font>** José Luis Delgado Jiménez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Black-box tests for Fujisaki-Okamoto decapsulation observe the sampled execution seen by the harness, whereas the reencryption computation itself is visible only through the values that reach final key derivation. We study confirmation-code-augmented KEM variants under an honest-reference harness in which the reference encapsulation fixes a hidden final-key point $\langle good,B,W\rangle$, with $W$ the confirmation witness. For a $q$-localized system under test, acceptance is bounded by honest correctness error, adversarial aliasing, final-key freshness defects, a hit on the localized suffix list $Q_G(B)$, and $2^{-\kappa}$. A one-query construction from any predictor of $W$ matches this bound up to the fresh-key coincidence term, so the list-hit event is the black-box obstruction measured by the harness.
The list-hit term is bounded either by a cUP-faithful harness certificate, which transfers source confirmation-code unpredictability with a $q$-loss, or by an average conditional min-entropy bound, with separate RawEnt and TailEnt hypotheses for short diagnostic and truncation-tail codes. The same model proves a dependency-cone lower bound for non-certification claims. When the black-box observation of an honest-support harness factors through the confirmation-observable final-key target, every operation outside the support-active cone has a coupled erasure implementation with the same transcript distribution; over any implementation class containing that erasure, soundness and completeness errors of an execution certifier satisfy $\alpha+\beta\ge 1$. The ML-KEM and HQC case studies distinguish theorem-covered positive rows, finite-catalog artifact rows, and non-certification rows that carry a cone-inactivity certificate. The security of the standard KEM lines is the construction-level security supplied by the cited source analyses.

---


### 108. [RowNet: A Memory Transformer for Tabular Regression](https://arxiv.org/abs/2606.04445)

**<font color=#1a73e8>作者：</font>** Askat Rakhymbekov, Gulshat Muhametjanova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real estate valuation is a structured regression problem in which prices are governed by heterogeneous feature types, sparse regional effects, nonlinear interactions, and the practical logic of comparable properties. Standard multilayer perceptrons treat each row as an isolated vector and must learn locality, scale sensitivity, and categorical matching from supervision alone. Gradient-boosted decision trees provide strong tabular baselines, but their feature-centric splitting mechanism does not explicitly model the retrieval of similar historical observations.
This paper presents RowNet, a retrieval-based neural architecture for real estate price-per-square-meter prediction. RowNet represents a query property through pairwise similarity features against a memory bank of labeled properties. A first retrieval layer estimates a coarse target from feature-only similarities. A second layer augments the memory comparison with target-consistency features and uses multiple learned attention heads to retrieve complementary comparable sets. A final mixture-of-experts module combines learned gating, residual correction, entropy regularization, and head-diversity regularization to produce the prediction.

---


### 109. [On Out-of-sample Embedding in UMAP](https://arxiv.org/abs/2606.04451)

**<font color=#1a73e8>作者：</font>** Mohammad Tariqul Islam, Jason W. Fleischer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neighbor embedding algorithms reveal correlations in high-dimensional data by constructing an equivalent graph representation in a lower-dimensional space. An increasingly popular algorithm is Uniform Manifold Learning and Projection (UMAP), which uses algebraic topology to map distances between the two spaces. While it works well on many types of data sets, UMAP has trouble adding out-of-sample points to a pre-existing mapping. In particular, UMAP often places new points on the periphery of the found clusters, rather than in their interiors with their correlated neighbors. Here, we overcome this ``repulsion effect'' by optimizing pairwise interactions within the original k-nearest-neighbor graph. Moreover, we show that parameterizing UMAP obtains better embeddings than non-parametric algorithms, particularly as the data gets more complex (e.g., medical images). We also show that the repulsion effect is naturally mitigated when a parameterized UMAP is employed to embed the data. We characterize different UMAP approaches using trustworthiness, nearest neighbor classifiers, and by analyzing attractive and repulsive forces in the embeddings.

---


### 110. [Radiomic Feature Selection Using Gradient Loss of Deep Neural Network for Lung Cancer Stage Detection](https://arxiv.org/abs/2606.04453)

**<font color=#1a73e8>作者：</font>** Hina Shakir, Mohammad Mohatram, Javeed Hussain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiomics enables extraction of quantitative imaging biomarkers from medical images and has become an important tool for computer-aided cancer diagnosis. However, radiomics datasets are typically high-dimensional with limited samples, making feature selection a critical step for building reliable predictive models. This study proposes a Gradient-Loss Recursive Feature Elimination (GL-RFE) framework that integrates gradient sensitivity analysis from a deep neural network to identify the most influential radiomic features for lung cancer stage detection. A total of 106 radiomic features were extracted from chest Computed Tomography (CT) scans using the PyRadiomics extension of the 3D Slicer platform. The proposed method evaluates feature importance by computing gradients of the network loss with respect to input features and recursively eliminates features with minimal contribution. The resulting top-15 radiomic features are used to train a deep neural network classifier for distinguishing early-stage and advanced-stage lung cancer. The proposed framework achieves strong classification performance, with accuracy of 90.22%, precision of 90.10%, recall of 90.24%, and F1-score of 90.16% on the test dataset. Visualization analyses, including correlation heat maps and distribution plots, further confirm reduced feature redundancy and improved class separability. Compared to conventional feature selection techniques, GL-RFE effectively captures nonlinear feature interactions and enhances model generalization. The presented protocol provides a reproducible and interpretable methodology for radiomics-based cancer stage detection and is particularly suitable for high-dimensional, small-sample biomedical datasets, with potential applications in other domains such as genomics and multimodal clinical analysis.

---


### 111. [The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?](https://arxiv.org/abs/2606.04455)

**<font color=#1a73e8>作者：</font>** Xinyu Lu, Tianshu Wang, Pengbo Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current AI benchmarks evaluate agents on task execution within human-designed workflows. These evaluations fundamentally fail to measure a critical next-level capability: whether models can autonomously develop agent systems. We introduce the Meta-Agent Challenge (MAC), an evaluation framework designed to test the capacity of frontier models for autonomous agent development. Specifically, a code agent (the meta-agent) is given a sandboxed environment, an evaluation API, and a time limitation to iteratively program an agent artifact that maximizes performance on a held-out test set across five domains. To ensure evaluation integrity, this framework is secured by multi-layer defenses against reward hacking. Leveraging this framework, we demonstrate that meta-agents rarely match human-engineered baseline policies, and the few that do are dominated by proprietary frontier models. Moreover, the design process exhibits high variance, and high optimization pressure surfaces emergent adversarial behaviors like ground-truth exfiltration-highlighting critical deficits in both robustness and model alignment. Ultimately, MAC provides a rigorous, open-source benchmark for autonomous AI research and development, offering an empirical proxy for evaluating recursive self-improvement. Benchmark is publicly available at: this https URL.

---


### 112. [Imagine Before You Draw: Visual Prompt Engineering for Image Generation](https://arxiv.org/abs/2606.04457)

**<font color=#1a73e8>作者：</font>** Liyu Jia, Fengda Zhang, Jiachun Pan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incorporating visual semantic representations as an intermediate step before image generation can reduce the modeling difficulty between text and images, thereby improving generation quality. Recent works such as X-Omni and BLIP3o-Next have explored this direction, but they typically use a two-stage external pipeline: a separate autoregressive model first generates semantic tokens, which are then fed as conditioning to an independent diffusion decoder. Since the decoder cannot jointly access the original input and the semantic plan, this design introduces an information bottleneck that limits detail preservation in downstream tasks such as editing. Internal architectures such as Transfusion, BAGEL, and Show-o2 avoid this bottleneck by enabling cross-modal interaction within a single model, but they still face the difficult text-to-pixel modeling gap without intermediate semantic guidance. We propose Visual Prompt Engineering (VPE), which can be seamlessly integrated into such internal frameworks. Specifically, the model first autoregressively generates visual semantic tokens (e.g., SigLIP 2) as "visual prompts" that capture the semantic layout, then generates the full image tokens conditioned on this plan. We validate VPE across class-conditional generation, text-to-image generation, and image editing, covering various token types and model architectures. Results show that VPE can accelerate convergence, raise quality ceilings, and through internal integration, achieve substantially better editing preservation (PSNR: 26.76 vs. 19.92) than external alternatives of the same parameter scale, while maintaining competitive editing responsiveness.

---


### 113. [CyberGym-E2E: Scalable Real-World Benchmark for AI Agents' End-to-End Cybersecurity Capabilities](https://arxiv.org/abs/2606.04460)

**<font color=#1a73e8>作者：</font>** Tianneng Shi, Robin Rheem, Dongwei Jiang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI has the potential to transform cybersecurity by enabling systems that can autonomously detect, analyze, and remediate software vulnerabilities. However, existing cybersecurity evaluations of AI systems are limited in scale or scope, and fail to capture the end-to-end lifecycle of real-world software vulnerability discovery and remediation. To address this gap, we propose CyberGym-E2E, a large-scale and realistic end-to-end cybersecurity benchmark that comprehensively evaluates AI agents' abilities across the full lifecycle of vulnerability discovery, PoC generation, and patch generation. CyberGym-E2E is comprehensive and scalable, as we build an automated, agent-enhanced pipeline for transforming open-source vulnerability data into realistic evaluation environments. Currently, the benchmark consists of 920 real-world vulnerabilities across 139 different open-source projects.

---


### 114. [ChannelTok: Efficient Flexible-Length Vision Tokenization](https://arxiv.org/abs/2606.04461)

**<font color=#1a73e8>作者：</font>** Sukriti Paul, Arpit Bansal, Tom Goldstein  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leading flexible vision tokenizers achieve SOTA quality at an extreme cost, relying on parameter-heavy backbones and slow, multi-step generative decoders. We depart from this complex, spatial-token paradigm and introduce a simple, lightweight, and fast channel-wise flexible-length tokenizer. Our method treats each latent channel as a visual token, enabling a parameter-efficient CNN-Transformer hybrid backbone. Furthermore, employing a stochastic tail-dropping paradigm during training naturally forces channels to organize by semantic importance. This allows for flexible compression at inference by simply retaining the first $k$ channels, and naturally enables variable-length autoregressive image generation. We validate our approach through extensive experiments on ImageNet, demonstrating consistent quality across diverse token budgets. The results establish a new quality-efficiency frontier: our model achieves state-of-the-art perceptual quality (rFID 2.92) while being $8.6\times$ faster in decoding and $2.1\times$ smaller (159M params) than the next-best alternative. Our work establishes channel-wise tokenization as a powerful and practical paradigm for efficient visual representation. Project page: this https URL

---


### 115. [SePO: Self-Evolving Prompt Agent for System Prompt Optimization](https://arxiv.org/abs/2606.04465)

**<font color=#1a73e8>作者：</font>** Wangcheng Tao, Han Wu, Weng-Fai Wong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> System prompt optimization improves agent behavior without modifying the underlying model, yielding human-readable, model-agnostic instructions. Existing methods build a prompt agent that refines task agents' system prompts, yet leave the prompt agent's own system prompt hand-engineered and fixed. We propose Self-Evolving Prompt Optimization (SePO), which treats the prompt agent's own system prompt as an optimization target alongside task agents' system prompts. SePO adopts a self-referential design. A single prompt agent improves both task agents' system prompts and its own under an open-ended evolutionary search that maintains an archive of candidate prompts as stepping stones. Training proceeds in two stages: pre-training evolves the prompt agent on a multi-task pool, and fine-tuning then applies it to a target task. Across five benchmarks spanning math (AIME'25), abstract reasoning (ARC-AGI-1), graduate-level science (GPQA), code generation (MBPP), and logic puzzles (Sudoku), SePO consistently outperforms Manual-CoT, TextGrad, and MetaSPO, improving the average accuracy by 4.49 points compared to Manual-CoT. The prompt optimization skill from pre-training also generalizes to tasks beyond the pre-training mixture, rather than memorizing per-task prompts.

---


### 116. [ParetoPilot: Zero-Surrogate Offline Multi-Objective Optimization via Infer-Perturb-Guide Diffusion](https://arxiv.org/abs/2606.04468)

**<font color=#1a73e8>作者：</font>** Ruiqing Sun, Sen Yang, Dawei Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline multi-objective optimization (Offline MOO) aims to discover novel Pareto-optimal designs based on static datasets without expensive environment interactions. While recent generative methods have achieved notable success, they predominantly rely on external surrogate models. This dependency introduces significant computational overhead, suffers from deceptive evaluations, and deviates from the prevailing paradigm of jointly training mainstream generative models with conditions. To address these bottlenecks, we propose ParetoPilot, a novel zero-surrogate diffusion framework for offline MOO. ParetoPilot fully leverages the conditional priors inherently embedded within pre-trained diffusion models. At its core, the framework introduces the Infer-Perturb-Guide (IPG) engine, which is seamlessly interleaved within the unconditional denoising steps of the reverse generation process. First, it implicitly infers the instantaneous objective direction by matching conditional and unconditional noise predictions. Next, it mathematically orthogonalizes a parallel gravity field for strict convergence and an edgeness-aware repulsive force for mutual diversity, creating a dynamically annealed perturbation vector. Finally, this perturbed target seamlessly steers the generation process via standard Classifier-Free Guidance (CFG). Extensive experiments across 51 tasks demonstrate that ParetoPilot outperforms 14 state-of-the-art surrogate-based and inverse generative baselines. By eliminating auxiliary proxy training, our approach preserves data privacy while achieving hypervolume improvement and robust Pareto front coverage.

---


### 117. [Adaptive Calibration for Fair and Performant Facial Recognition](https://arxiv.org/abs/2606.04469)

**<font color=#1a73e8>作者：</font>** Ryan Brown, Chris Russell  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Adaptive Calibration (AC), a novel calibration strategy for facial recognition that maps cosine similarity between normalized embeddings to well-calibrated probabilities. By incorporating local context into calibration, Adaptive Calibration corrects for a fundamental mismatch in cosine similarity, whereby the same distance can correspond to different match probabilities in different embedding regions. Our approach improves both overall performance and results in a fairer calibration without requiring demographic metadata.
Our approach consistently dominates existing methods both on accuracy and fairness metrics across a variety of pretrained models and standard benchmarks. AC provides a practical solution for equitable facial recognition, without requiring demographic group annotations, and while improving overall performance. Unlike existing approaches, our method provides continuous, region-specific calibration that avoids "leveling down" where fairness comes at the cost of degraded performance for some groups.

---


### 118. [ChessMimic: Per-Rating Transformer Models for Human Move, Clock, and Outcome Prediction in Online Blitz Chess](https://arxiv.org/abs/2606.04473)

**<font color=#1a73e8>作者：</font>** Thomas Johnson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present ChessMimic, a system of three small encoder-only transformers - for move, thinking-time, and outcome prediction - conditioned on the position, recent move history, player rating, and clock state. We fit a separate instance of each model per 100-Elo rating band, trading parameter efficiency for sharper per-skill calibration. On a held-out month-wide slice of Lichess Rated Blitz games ChessMimic's human move prediction accuracy outperforms Maia-2 in every Elo band. Compared to Maia-3, our 9M parameter model's accuracy sits between Maia-3-5M and Maia-3-23M without the additional complexity of Geometric Attention Bias. In addition to the move matching model, we also train a game outcome model that conditions not only on the position, but also player ratings, time control, and remaining clock times. The outcome model achieves an AUC of 0.78 out of sample, beating Maia-2 as well as logistic regressions based on material, ratings, and clock time. Finally, we train a clock model that predicts human thinking times. The clock model provides a usable but non-SOTA per-ply think-time signal under ALLIE-style filters (Pearson r = 0.41, Spearman rho = 0.50, MAE 4.10 s, against ALLIE's reported r = 0.70), with the residual gap concentrated in per-position bucket sharpness rather than bucket-marginal calibration. A public demo is at this http URL and we release code, per-band weights, and the C++ data-filter pipeline code in GitHub.

---


### 119. [When Both Layers Learn: Training Dynamics of Representing Linear Models via ReLU Networks](https://arxiv.org/abs/2606.04476)

**<font color=#1a73e8>作者：</font>** Berk Tinaz, Changzhi Xie, Mahdi Soltanolkotabi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the gradient descent dynamics for jointly training both layers of a one-hidden-layer ReLU network to fit a linear target function. Concretely, we consider a realizable setting where inputs are drawn i.i.d. from a Gaussian distribution and labels follow a planted linear model. This stylized framework captures salient features of end-to-end training in inverse problems and certain auto-encoder models. Despite its apparent simplicity, the dynamics remain poorly understood, in part because the loss landscape contains multiple non-strict saddle points, making it unclear why gradient descent from random initialization reliably escapes bad stationary regions. We provide a detailed characterization of the optimization landscape and prove that gradient descent from a moderately small random initialization-simultaneously training both layers-converges to a global minimizer at a linear rate with order-wise optimal sample complexity. Our analysis tracks the trajectory through three phases: an alignment phase in which hidden weights progressively align with the planted direction while the output weights maintain the correct sign pattern; a growth phase in which the norms of both layers increase while preserving alignment; and a local refinement phase in which the aligned neurons rapidly converge to the planted direction, yielding fast local convergence. To rigorously show that GD avoids non-strict saddles, we develop trajectory-level control arguments for the end-to-end dynamics. In addition, we establish novel uniform concentration results that hold along the entire trajectory, and are essential for obtaining order-wise optimal sample complexity. We corroborate our theory with extensive experiments across a range of configurations.

---


### 120. [Evaluating Reasoning Fidelity in Visual Text Generation](https://arxiv.org/abs/2606.04479)

**<font color=#1a73e8>作者：</font>** Jiajun Hong, Jiawei Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-image (T2I) models can render highly legible and well-structured text within images, enabling applications including document generation and slide generation. However, it remains unclear whether such systems faithfully preserve reasoning ability when complex solutions must be expressed directly through rendered text, or whether they merely imitate surface-level patterns. We investigate this question by evaluating reasoning fidelity in visual text generation, where models must express complete reasoning processes as images. Our evaluation includes long text rendering, factual knowledge probing, context understanding, and multi-step reasoning. Across these settings, we find that current T2I models frequently produce semantic errors, logical inconsistencies, and incorrect intermediate steps, even when the rendered text appears visually clear. These failures contrast with the strong reasoning performance of text-only models on the same tasks. Our findings reveal a substantial gap between visual text generation and procedural reasoning, motivating more reliable visual text reasoning.

---


### 121. [IMPose: Interactive Multi-person Pose Estimation with Dynamic Correction Propagation](https://arxiv.org/abs/2606.04480)

**<font color=#1a73e8>作者：</font>** Haoyang Ge, Jian Ma, Ziwen Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality dynamic human pose annotation equips AI with precise motion kinematics to enable human behavior mastery, yet remains labor-intensive and time-consuming. Current annotation tools either lack temporal correction propagation or fail in multi-person scenarios, necessitating excessive manual intervention. In this paper, we introduce IMPose, an interactive tool for multi-person dynamic pose annotation. It features a dual-level tracking mechanism that propagates one-frame multi-person pose corrections from annotators across entire videos. The keypoint-level ensures corrections temporal propagation via sequential modeling, while the instance-level employs keypoint-aware embedding with relative positional encoding to maintain multi-person cross-frame consistency. To further improve robustness, IMPose maintains historical pose and instance cues in a trajectory bank, which enhances long-range temporal association and stabilizes annotation in challenging cases such as occlusion and motion blur. By converting sparse human corrections into dense and coherent pose trajectories, our framework significantly reduces repeated manual refinement across frames. Extensive experiments show that IMPose consistently achieves a strong accuracy efficiency trade off under different interaction budgets, demonstrating particular advantages in low click annotation settings. IMPose achieves high precision annotation with high efficiency, requiring only 27 clicks per 1,050 frame video on 3DPW and 3 clicks per tracklet per 84-frame on PoseTrack21. We further expand PoseTrack21 with 188K pose instances (3.55M keypoints) at a minimal cost of 10 annotators in 10 hours. The annotation tool, codes, and extended dataset will be open-sourced.

---


### 122. [Speculating the Impacts of Mediated Social Touch Technology](https://arxiv.org/abs/2606.04489)

**<font color=#1a73e8>作者：</font>** Russian, Tim Moesgen, Myung Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With growing research on haptic interfaces, Mediated Social Touch (MST) technologies offer the potential to record, synthesise, and reproduce (RSR) touch experiences across space and time, enabling, for instance, a hug from afar and from the past. Although much of the existing research highlights the direct benefits of these systems, such as reducing loneliness and providing emotional support, little attention has been paid to their broader sociotechnical impacts. To address this gap, we used the Future Ripples method to speculate on possible effects of MST. We conducted three workshops with 24 participants, including potential users, domain experts, and haptics researchers. Throughout these sessions, participants collectively envisioned possible future scenarios, alongside opportunities and threats, and proposed actionable responses. Our qualitative analysis organised these insights into four themes and three distinctive challenges. These findings offer haptics researchers intervention points across the RSR pipeline to inform MST design, alongside methodological insights from applying Future Ripples to MST technology.

---


### 123. [Episodic Memory Temporal Consistency for Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2606.04492)

**<font color=#1a73e8>作者：</font>** Zicheng Zhao, Yu Lan, Chengzhengxu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperative Multi-Agent Reinforcement Learning (MARL) frequently suffers from severe reward sparsity and exploration bottlenecks. While episodic memory mechanisms mitigate these issues by reusing high-return trajectories, they often trap agents in local optima due to unconstrained incentive distribution and semantic representation collapse. To address this, we propose Episodic Memory Temporal Consistency (EMTC), a framework that robustly constructs and selectively leverages historical experiences. EMTC introduces two synergistic components: (1) a Temporally Consistent Semantic Embedder that integrates contrastive learning with time-conditioned state reconstruction, preventing representation collapse and enabling precise memory retrieval; and (2) a Temporal Consistency Gating Mechanism that dynamically modulates episodic incentives based on temporal consistency error. This adaptive gate filters misleading signals from pseudo-successful trajectories, effectively mitigating Q-value overestimation. We provide theoretical guarantees, establishing a strict error bound that directly links the observable temporal consistency error to the underlying trajectory optimality and representation quality. Extensive evaluations on the SMAC and GRF benchmarks demonstrate that EMTC consistently outperforms state-of-the-art baselines. Notably, compared to the strongest episodic baseline, EMTC achieves absolute win-rate improvements of up to 24% in super-hard SMAC scenarios and an average improvement of 28% across GRF tasks.

---


### 124. [SFMambaNet: Spectral-Frequency Enhanced Selective State Space Model for Correspondence Pruning](https://arxiv.org/abs/2606.04493)

**<font color=#1a73e8>作者：</font>** Zhihua Wang, Yanping Li, Yizhang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Correspondence pruning aims to identify inliers from an initial set of correspondences. Most existing Graph Neural Network (GNN)-based methods rely on geometric features mapped from coarse Euclidean coordinates, which struggle to capture the subtle geometric consistencies presented by inliers. While Mamba-based methods possess global receptive fields and long sequence modeling capabilities, they tend to accumulate substantial inconsistent features within the hidden state space, making it difficult to distinguish inliers from outliers. In this paper, we integrate frequency domain perception into this task for the first time and propose SFMambaNet, a novel Spectral-Frequency enhanced Mamba-based two-view correspondence pruning network. Our method is collaboratively composed of two components: First, we design a Local Spectral-Geometric Attention (LSGA) block. LSGA incorporates spectral positional encoding into local graph interactions and introduces multi-scale Mamba processing to enhance the capture of subtle geometric consistencies and improve local feature discriminability. Building upon this, we design a Spectral-Integrated Global Mamba (SIGM) block. SIGM embeds a frequency gating mechanism within the state space, utilizing the frequency information provided by LSGA to explicitly suppress high-frequency noise accumulation within hidden states and mitigate the propagation of inconsistent features. This enhances inlier-outlier separability and achieves robust global context modeling capabilities with nearly linear complexity. Extensive experiments demonstrate that SFMambaNet outperforms current state-of-the-art methods on several challenging tasks. The code is available at this https URL.

---


### 125. [Beyond Prompt-Based Planning: MCP-Native Graph Planning-based Biomedical Agent System](https://arxiv.org/abs/2606.04494)

**<font color=#1a73e8>作者：</font>** Zhangtianyi Chen, Florensia Widjaja, Wufei Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical agents promise to automate complex biological workflows, yet current systems face two fundamental bottlenecks: bioinformatics tools are highly heterogeneous in interfaces and execution environments, while agent planning still relies on flat prompt-retrieved tool descriptions. As biomedical software ecosystems grow, this coupling between tool coverage and context size leads to tool confusion, unstable planning, and inefficient execution. We introduce BioManus, an MCP-native biomedical agent built on graph-scaffolded planning over structured biological capabilities. BioManus first introduces the BioinfoMCP Compiler, which converts heterogeneous bioinformatics software into standardized MCP servers, yielding a large executable MCP ecosystem. It then organizes this ecosystem as a typed heterogeneous MCP graph over tools, operations, datatypes, and workflow stages. At inference time, BioManus retrieves compact task-specific subgraphs, synthesizes operation-level workflow scaffolds. This design decouples planning complexity from raw tool inventory size, achieving a context compression ratio of Theta(N / (h * m_bar)) under high-recall retrieval, where N is the total tool count, h is the workflow horizon, and m_bar (much smaller than N) is the average number of candidate tools per operation. Experiments on BioAgentBench and LAB-Bench show that BioManus improves execution accuracy, workflow validity, and context efficiency over advanced biomedical agent baselines. This work suggests a paradigm shift: scalable biomedical reasoning requires structured executable capability graphs rather than increasingly larger prompt-level tool retrieval.

---


### 126. [SANE Schema-aware Natural-language Evaluation of Biological Data](https://arxiv.org/abs/2606.04500)

**<font color=#1a73e8>作者：</font>** Rolf Gattung, Martin Krueger, Markus Reischl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-throughput microscopy generates large, structured datasets capturing cellular responses to pharmacological perturbations, but accessing these datasets typically requires SQL expertise. Large language models offer a natural-language alternative, yet their tendency to hallucinate raises concerns about result reliability .
We present SANE Schema-Aware Natural-language Evaluation, a novel paradigm for domain-specific text-to-SQL evaluation: schema-grounded, automatically generated benchmarks tied to real and specific experimental structure. SANE makes evaluation more scalable, systematic, and reproducible.
Using SANE, we evaluate a few-shot large language model and show that, under constrained schemas with structured prompting and guardrails, accurate query generation is achievable without any model training or fine-tuning. Most failures stem from ambiguous or underspecified inputs and manifest as overly cautious clarification requests or answers to queries that should first be disambiguated, rather than incorrect SQL generation. These results indicate that few-shot large language models can provide reliable database access in well-defined domains when combined with schema-aware prompting.

---


### 127. [Smart Picks in the Dark: Towards Efficient RLVR for Reasoning via Tracing Metacognitive Pivots](https://arxiv.org/abs/2606.04503)

**<font color=#1a73e8>作者：</font>** Guangcheng Zhu, Shenzhi Yang, Haobo Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has greatly advanced large reasoning models (LRMs), but it requires timely training on a huge fully-annotated dataset. To this end, data-efficient RLVR methods have been widely studied from two perspectives: (i) data selection methods identify a small subset of "golden" samples that yield near-full-data performance, but they rely on a pre-existing pool of labeled data. (ii) unsupervised RLVR methods train the model using its own internal supervision signals on large-scale unlabeled data, yet they exhibit suboptimal performance. Accordingly, we investigate the "pick in the dark" setup for RLVR, which aims to select, without prior supervision, unlabeled samples that are most beneficial for training and worthy of annotation. Through systematic analysis, we demonstrate that smart picks hinge on a well-calibrated uncertainty estimator to enable strategic partitioning of data for adaptive training regimes. Building on this insight, we propose PivotTrace, a three-way data triage framework that leverages attention dynamics to trace metacognitive pivots during reasoning. By precisely quantifying uncertainty through pivot density, PivotTrace achieves automated data routing to synergistically maximize both annotation and training efficiency. Empirically, PivotTrace surpasses the fully supervised LRM with only 29.3% annotated samples and 2.75 faster convergence.

---


### 128. [GeoMin: Data-Efficient Semi-Supervised RLVR via Geometric Distribution Modeling](https://arxiv.org/abs/2606.04516)

**<font color=#1a73e8>作者：</font>** Guangcheng Zhu, Shenzhi Yang, Haobo Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) significantly advances LLM reasoning, yet it faces a dilemma: standard supervised scaling is throttled by high annotation costs, while unsupervised alternatives suffer from severe model collapse. Recent semi-supervised RLVR methods address this by using a small labeled set to guide unlabeled data, achieving a promising trade-off between training efficacy and annotation cost. However, they suffer from a severe data-efficiency bottleneck due to the reliance on coarse performance heuristics, leaving a vast majority of valuable instances underutilized. To this end, we propose GeoMin, which models global feature distributions on labeled data to decode the structural discrepancy between correct and incorrect rollouts, thereby establishing a robust prior to assess the reliability of self-reward signals and fully unleash the potential of unlabeled data. Empirically, GeoMin outperforms the strongest baselines by +4.1% and even surpasses fully supervised models with only 10% of the annotations, demonstrating remarkable data efficiency.

---


### 129. [GENEB: Why Genomic Models Are Hard to Compare](https://arxiv.org/abs/2606.04525)

**<font color=#1a73e8>作者：</font>** Daria Ledneva, Mikhail Nuridinov, Denis Kuznetsov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Progress in genomic foundation models is difficult to assess due to fragmented benchmarks, incompatible evaluation protocols, and task-specific reporting. As a result, claims of superiority or generality across models are often not directly comparable. We introduce GENEB, a large-scale diagnostic benchmark that evaluates frozen representations from 40 genomic foundation models across 100 tasks spanning 13 functional categories under a unified probing-based protocol, including few-shot regimes. GENEB enables controlled comparison across model scale, architecture, tokenization, and pretraining data while explicitly exposing task-level trade-offs. Our analysis shows that aggregate leaderboards are unstable: model rankings vary sharply across task categories, scale provides only modest and inconsistent gains, and architectural and pretraining alignment frequently outweigh parameter count. These results highlight limitations of current evaluation practices and position GENEB as a reference framework for principled comparison and category-aware model selection in genomic machine learning.

---


### 130. [Optical-Guided Neural Collapse for SAR Few-Shot Class Incremental Learning](https://arxiv.org/abs/2606.04528)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Sijin Zheng, Fei Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot class-incremental learning (FSCIL) in synthetic aperture radar imagery presents unique challenges due to severe data scarcity and SAR-specific variability. In particular, strong azimuth sensitivity in SAR induces large intra-class variation and inter-class confusion, and FSCIL sequential updates further lead to catastrophic forgetting of previously learned classes. Inspired by neural collapse, we propose an optical-guided SAR FSCIL framework, which derives orthogonal feature subspaces from a data-rich optical ATR dataset and uses them as geometric priors to guide SAR feature learning. SAR features are projected onto these orthogonal subspaces via principal angle constraints, effectively transferring discriminative structure from the optical to the SAR domain. Specifically, our projection loss and the classifier loss optimized with a frozen simplex-ETF geometry jointly induce neural collapse by concentrating features around class means while maintaining large inter-class angles. We evaluate the approach on a benchmark comprising an optical ATR dataset and a SAR ATR dataset with 24 target classes, organized into a base training session and seven incremental sessions. Compared with recent FSCIL methods including NCFSCIL and so on, our method achieves the highest final accuracy and a favorable trade-off between final performance and performance degradation. Moreover, neural collapse metrics show improved intra-class compactness and inter-class separability, indicating that the learned features more closely approximate the ideal simplex-ETF geometry.

---


### 131. [Scaling Self-Evolving Agents via Parametric Memory](https://arxiv.org/abs/2606.04536)

**<font color=#1a73e8>作者：</font>** Tao Ren, Weiyao Luo, Hui Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing memory-augmented LLM agents store past experience exclusively in prompt space, as textual summaries or retrieved passages, while keeping model parameters frozen throughout a rollout. Such agents can \emph{look up} what they have seen but cannot \emph{learn from} it: their policy is unchanged by experience, and any information dropped from the context is permanently lost. We introduce \texttt{TMEM}, a self-evolving parametric memory framework in which the agent not only compresses history into explicit memory but also absorbs distilled supervision into fast LoRA weights $\Delta_t$ via lightweight online updates, genuinely altering its future behavior within a single episode. We formalize this as an agentic decision process with fast-weight rollout dynamics: actions are sampled from $\pi_{\theta_0+\Delta_t}$, while extraction actions produce supervision that updates $\Delta_t$ for subsequent decisions. This view makes the extraction policy directly optimizable by RL: training $\theta_0$ improves not only task actions but also the quality of the data used for online LoRA adaptation. We further propose SVD-based initialization of the LoRA subspace to accelerate online convergence. Experiments on LoCoMo, LongMemEval-S, multi-objective search, and CL-Bench show that \texttt{TMEM} consistently outperforms summary-based and retrieval-based baselines across different model scales.

---


### 132. [PS-UIE: Privilege-Separated Integrity Enforcement for User-Space Executable Objects in Confidential VMs](https://arxiv.org/abs/2606.04549)

**<font color=#1a73e8>作者：</font>** Jingkai Mao, Xiaolin Chang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Confidential Virtual Machines (CVMs), such as AMD SEV-SNP, enable cloud tenants to run security-sensitive workloads, but tenants can rely on the execution of these workloads only when they can trust the CVM. This trust requires continuous integrity assurance from CVM launch to the current runtime state, including initial trust establishment at launch and subsequent runtime integrity assurance. Existing works help establish launch-time trust and protect parts of runtime integrity, but they do not fully address the integrity of file-backed user-space executable objects, such as main executables, program interpreters, and dynamically loaded shared objects, that may be loaded or mapped dynamically during execution inside CVMs. In this paper, we propose Privilege-Separated User-space Integrity Enforcement (PS-UIE), an approach for enforcing the integrity of user-space executable objects inside AMD SEV-SNP-based CVMs. PS-UIE consists of a privilege-separated architecture and three mechanisms. The architecture separates the authority for integrity measurement and enforcement from the measured targets by placing it in a higher-privileged protected domain. Built on this architecture, PS-UIE provides policy lifecycle management, execution-time integrity enforcement, and evidence export and verification mechanisms. It enables policy-controlled integrity measurement and enforcement for user-space executable objects and generates verifiable runtime evidence. We implement PS-UIE on an AMD SEV-SNP platform. The security analysis and performance evaluation show that PS-UIE enforces the integrity of user-space executable objects on the covered execute-permission grant paths and provides verifiable runtime evidence while incurring acceptable overhead.

---


### 133. [LDARNet: DNA Adaptive Representation Network with Learnable Tokenization for Genomic Modeling](https://arxiv.org/abs/2606.04552)

**<font color=#1a73e8>作者：</font>** Daria Ledneva, Denis Kuznetsov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Genomic foundation models increasingly adopt large language model architectures, yet almost universally rely on fixed tokenization schemes such as $k$-mers, BPE, or single nucleotides, which impose arbitrary sequence boundaries that may obscure biologically relevant structure. We present LDARNet, a 120M-parameter hierarchical genomic foundation model that adapts H-Net-style dynamic chunking from autoregressive generation to masked language modeling, combining BiMamba-2 state-space layers with local attention, bidirectional routing, and a ratio-based regularizer to induce adaptive token boundaries without supervision. Fine-tuned on 27 tasks from the Nucleotide Transformer and Genomic Benchmarks suites, LDARNet achieves 11/18 wins among compact models ($<$300M parameters) and state-of-the-art results on 5 histone modification tasks, outperforming models up to 20$\times$ larger. A FLOPs-matched controlled experiment isolates learned routing as the source of these gains: learned boundaries beat fixed-grid boundaries by up to 14 percentage points on histone tasks at identical compute. Nucleotide-resolution analysis further shows that the learned boundaries align with canonical promoter motifs and splice junctions without supervision, providing a biological interpretation for adaptive tokenization in genomic foundation models.

---


### 134. [Neetyabhas: A Framework for Uncertainty-Aware Public Policy Optimization in Rational Agent-Based Models](https://arxiv.org/abs/2606.04562)

**<font color=#1a73e8>作者：</font>** Janani Venugopalan, Gaurav Deshkar, Rishabh Gaur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Purpose The WHO's COVID-19 non-pharmaceutical interventions (e.g., lockdowns, vaccinations) effectively curb transmission but impose heavy economic strains. Existing research often neglects individual behaviors and falsely assumes perfect infection tracking and flawless policy execution, failing to account for real-world uncertainties and errors. Methods We propose an integrative approach incorporating uncertainties in both epidemic measurement (infections/hospitalizations) and policy implementation. We built a simulation model of 1,000 individuals making real-time choices regarding mask-wearing, vaccination, and shopping. Concurrently, policymakers deploy interventions (lockdowns, mandates) based on health and economic observations. This framework is driven by hierarchical reinforcement learning agents, utilizing deep Q-networks alongside uncertainty-aware policy gradient variants (DDPG and TD3). Results The simulations effectively managed the epidemic's progression. Masking and vaccinations proved highly effective, significantly reducing both the outbreak's peak height and duration. By integrating individual behaviors, policy uncertainties, and multifaceted interventions, our dynamic control approach successfully mitigated the epidemic's impact. Conclusions Our model overcomes previous research limitations by embedding uncertainty and human behavior into public health policy frameworks. The simulation demonstrates that accounting for individual choices and imperfect data is crucial for designing effective interventions during complex pandemics, with masks and vaccines serving as pivotal tools.

---


### 135. [Addressing Negative Commons Governance with Positive Commons Principles](https://arxiv.org/abs/2606.04563)

**<font color=#1a73e8>作者：</font>** Boyang Zhou, Oleg Ianchenko  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Computing is accompanied by both positive and negative commons throughout its lifecycle of creation, execution, and disposal. We examine two governance systems situated within this lifecycle -- global e-waste trade and the Linux kernel community -- to evaluate whether Elinor Ostrom's eight design principles for common-pool resource (CPR) governance extend to the management of negative common-pool resources (NCPRs). Unlike traditional CPRs where communities work to preserve a finite resource (i.e. clean water), NCPR governance seeks to collectively reduce a negative shared stock. In our two cases, e-waste governance aims to reduce the volume of mismanaged waste and illicit trade, while the Linux community aims to reduce the number of error-prone or malicious contributions that reach the main branch and, in turn, extend the life of existing hardware. Through qualitative analysis of primary sources from each domain, we find that the same eight principles by Ostrom that aid positive commons governance tend to appear in successful negative commons governance systems. We argue that future NCPR governance design should prioritize Ostrom's principles, particularly clearly defined boundaries and well-functioning nested structures.

---


### 136. [Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning](https://arxiv.org/abs/2606.04574)

**<font color=#1a73e8>作者：</font>** Damian Lebiedź, Robert Ślepaczuk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study aims to determine whether the application of Deep Reinforcement Learning (DRL) as a specialized execution overlay can enhance pair trading in highly volatile cryptocurrency markets. Although classical implementations of the strategy have proven successful in traditional equities, they frequently exhibit rigidity and suffer from severe divergence risks when applied to high-variance environments. To address this need, this research introduces novel concepts. To construct a robust system, we developed a hierarchical "Filter-then-Rank" pair selection methodology and a proprietary "Fixed Risk, Adaptive Mean" execution model. The system employs a Proximal Policy Optimization (PPO) agent with a Long Short-Term Memory (LSTM) layer to govern execution decisions within strict deterministic risk management boundaries. Evaluated on 1-hour interval data from the Binance USD-M Futures market, the optimized RL policy achieved an out-of-sample performance that substantially outperformed the heuristic baseline. A stationary circular block bootstrap robustness check confirms that the agent's risk-adjusted outperformance is statistically significant at the 10 percent level. Although falling marginally short of the stricter 5 percent threshold, this result highlights the extreme idiosyncratic variance characteristic of digital assets. Ultimately, this thesis contributes to the quantitative finance literature by introducing a hybrid architecture that combines statistical arbitrage with DRL execution policies. Furthermore, it delivers a novel framework for safe reinforcement learning via deterministic shielding, proving that anchoring a neural policy to statistically robust boundaries successfully mitigates severe divergence risks.

---


### 137. [SCI-PRM: A Tool Aware Process Reward Model for Scientific Reasoning Verification](https://arxiv.org/abs/2606.04579)

**<font color=#1a73e8>作者：</font>** Xiangyu Zhao, Hengyuan Zhao, Yiheng Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Process Reward Models (PRMs) have achieved remarkable success in mathematical reasoning, their application in complex scientific domains-such as biology, chemistry, and physics remains largely unexplored. Scientific problems demand not only logical rigor but also factual consistency and the precise usage of domain-specific tools, areas where current models often suffer from hallucinations and lack of verification. In this paper, we first construct SCIPRM70K, a large-scale dataset featuring Chain-of-Tool trajectories that explicitly interleave reasoning with the execution of scientific tools. Building upon this, we train an efficient reward model called Sci-PRM to provide fine-grained supervision on tool selection, execution accuracy, and result interpretation at each step in one inference. Experiments demonstrate that Sci-PRM significantly enhances foundation models in two key aspects: (1) it enables effective test-time scaling via Best-of-N selection; and (2) when integrated into Reinforcement Learning, it serves as a dense reward signal that mitigates the critical issue of advantage disappearance, allowing the model to break through existing performance ceilings.

---


### 138. [TIBlender: Early-Warning Threat Intelligence from Cross-Platform Social Media Evidence](https://arxiv.org/abs/2606.04580)

**<font color=#1a73e8>作者：</font>** Hiroki Nakano, Takashi Koide, Daiki Chiba  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber threat signals are fragmented across multiple social media platforms, yet no existing approach has fully automated their integration into actionable threat intelligence (TI) reports. We present TIBlender, a multi-agent system that monitors four platforms (X, Reddit, Telegram, and Discord) and produces structured TI reports via role-specialized LLM agents. These agents conduct multi-perspective investigations, tracing chains of evidence to uncover related Indicators of Compromise (IoCs) via collaborative, evidence-backed analysis. In a real-world deployment, TIBlender detected emerging threats across all four threat categories ahead of public feeds, including in-the-wild exploitation ahead of public vulnerability registries; the majority of its IoCs were absent from each evaluated feed. Quantitative evaluation confirms that each platform contributes unique threat information unavailable from the others, and that excluding any single platform results in substantial loss of reports in specific threat categories. Under identical single-platform input conditions, TIBlender's IoC extraction meets or exceeds each baseline; the full pipeline surfaces substantially more IoCs, most of which are absent from any single-platform baseline. These results establish cross-platform social media monitoring as an effective and scalable early-warning layer for operational TI pipelines.

---


### 139. [HalfNet: Randomized Neural Networks with Learned Subspace Geometry](https://arxiv.org/abs/2606.04583)

**<font color=#1a73e8>作者：</font>** Ethem Alpaydin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many researchers investigated neural networks with some of their weights fixed to values randomly drawn from a given distribution, e.g., $N(0, I)$. Our proposed HalfNet draws random weights from $N(0, \Sigma)$, where $\Sigma$, which defines the geometry of the distribution, has a low-rank factorization that we learn from data. Experiments on MNIST and CIFAR-10 demonstrate that HalfNet can match the performance of fully trained multilayer perceptrons while using substantially fewer parameters. Spectral analysis indicates that much of the predictive power of neural networks lies in the geometry of their weight space rather than in the precise values of individual parameters, and we observe that accuracy scales smoothly with rank. HalfNet is not a neural architecture trick for low-rank structure; it implements a data-dependent random embedding that can also be interpreted through supervised metric learning, or random-feature and kernel perspectives.

---


### 140. [4D Reconstruction from Sparse Dynamic Cameras](https://arxiv.org/abs/2606.04593)

**<font color=#1a73e8>作者：</font>** Kazuki Ozeki, Shun Kenney, Yuto Shibata 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although dynamic 3D (i.e., 4D) reconstruction from a monocular dynamic camera has recently advanced, it remains fundamentally limited by depth ambiguity. In this paper, we focus on an alternative practical way, i.e., sparse dynamic camera setup, where a handful of independently moving cameras capture the same subjects. While keeping capture costs low, this setup introduces multi-view constraints and remains practical for real-world video production such as sports, concerts, and TV shows. Despite its potential, our experiments show that naive extensions of existing monocular or dense-fixed camera-based methods are insufficient since they fail to resolve the complex spatiotemporal inconsistencies across views and time. To fill this gap, we propose a simple yet effective 3D track initialization method designed to ensure spatiotemporal consistency by integrating inter-camera feature matching with intra-camera point tracking. Additionally, we incorporate a noise-robust depth-ordering regularization loss and a spatiotemporally diverse batch sampling strategy to enhance optimization stability and cross-view generalization. Furthermore, to address the lack of standardized benchmarks for this task, we introduce LetCamsGo, a new real-world video dataset with 5 sequences across 4 diverse environments, recorded by three independently moving cameras and one fixed camera. Comprehensive benchmarking on LetCamsGo demonstrated that our proposed framework improves 4D reconstruction quality in dynamic regions compared with baselines, paving the way for a low-cost 4D reconstruction paradigm in the wild.

---


### 141. [Learning Admissible Heuristics via Cost Partitioning](https://arxiv.org/abs/2606.04597)

**<font color=#1a73e8>作者：</font>** Hugo Barral, Quentin Cappart, Marie-José Huguet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Admissible heuristics are essential for optimal planning, yet learning them remains challenging due to the risk of overestimation. Cost partitioning combines multiple abstraction heuristics while preserving admissibility, but computing optimal partitions online is expensive. We propose a framework that learns to infer admissible cost partitions by leveraging the Lagrangian dual equivalence between cost partitioning and multiplier prediction. Planning states and patterns are encoded as labelled graphs, and an action-centric variant of the Weisfeiler-Leman algorithm extracts structural feature vectors. A deep architecture with axial self-attention and a softmax output layer maps these features to cost weights that satisfy the partition constraints by construction, ensuring admissibility. Experiments demonstrate reduced node expansions compared to suboptimal partitioning baselines while maintaining strict admissibility. To our knowledge, this is the first machine-learned heuristic guaranteed to be admissible.

---


### 142. [Parthenon Law: A Self-Evolving Legal-Agent Framework](https://arxiv.org/abs/2606.04602)

**<font color=#1a73e8>作者：</font>** Hejia Geng, Leo Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agents grow more capable, legal-domain LLM agents promise to turn document-heavy matters into reviewable work products -- yet reliable deployment faces three obstacles: no large-scale evidence on how today's strongest model-and-harness combinations behave on end-to-end legal matters; no agent architecture adapted to the legal vertical, only general-purpose harnesses; and, in a setting that keeps shifting with new facts, authorities, and deadlines, no mechanism for systems to learn from their own outcomes. We address each. A large-scale empirical study on Harvey LAB -- $12{,}510$ agent trajectories -- shows that even frontier agents remain far from completing matters in a single pass: per-criterion accuracy climbs with stronger models while strict matter completion stalls. We then introduce \textsc{Parthenon}, a self-evolving legal-agent framework that factors Model, Harness, Agent roles, legal Knowledge, deterministic Tools, and procedural Skills into auditable surfaces for source traceability, date and number grounding, deliverable compliance, and issue closure. Finally, an anti-leakage learning loop converts scored failures into task-agnostic edits to skills, tools, and knowledge, letting the system improve with experience -- as a firm refines its checklists and playbooks after each matter -- without touching model weights. Across our large-scale empirical analysis, \textsc{Parthenon} substantially improves the performance of state-of-the-art models and harnesses on legal-matter tasks.

---


### 143. [COMBINER: Composed Image Retrieval Guided by Attribute-based Neighbor Relations](https://arxiv.org/abs/2606.04604)

**<font color=#1a73e8>作者：</font>** Zixu Li, Yupeng Hu, Zhiwei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) represents a challenging retrieval task that targets locating specific images through multimodal inputs. Despite recent progress in CIR techniques, prior approaches often overlook cases where images appear visually alike yet differ in attributes, potentially undermining both multimodal feature fusion and similarity modeling. To mitigate this limitation, we design a unified representation of cross-modal features based on attribute prototypes. Nevertheless, the task is far from straightforward, owing to three core issues: (1) entanglement in attribute-level semantics, (2) inconsistency across modalities, and (3) supervised signal missing. To tackle the above obstacles, we introduce a COMposed image retrieval network guided By attrIbute-based NEighbor Relations (COMBINER). Specifically, we first design an Adaptive Semantic Disentanglement module, which is capable of disentangling attribute features based on multimodal primitive features. Secondly, we propose a Unified Prototype-based Composition module, which can construct cross-modal unified prototypes (CUP) and facilitate multimodal feature composition. Finally, we introduce a Dual Relations Modeling module, which can mine pairwise and neighbor relations based on attribute similarity. Compared to traditional neighbor relations modeling CIR methods, COMBINER represents the first study addressing the phenomenon of visually similar but attribute-unrelated samples. It achieves a more accurate understanding of the semantic relations among samples by employing an attribute prototype-based similarity metric. Comprehensive experiments conducted on three benchmark datasets confirm the effectiveness of our proposed COMBINER. The implementation of our method will be accessed at this https URL

---


### 144. [CapSenseBand: Sustaining Cross-Disciplinary Creativity When Stitches Must Meet Signals](https://arxiv.org/abs/2606.04609)

**<font color=#1a73e8>作者：</font>** Sark Pangrui Xing, Hongci Hu, Lai Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearable sensing systems increasingly depend on textiles that are both materially wearable and electronically functional. Their design requires collaboration between textile designers, who reason through stitches, yarn behavior, and machine constraints, and interaction designers, who reason through electrodes, signal paths, and insulation. However, these forms of expertise do not easily translate across disciplinary boundaries. This poster presents CapSenseBand, a knitted capacitive-sensing wristband developed through a research-through-design process organized around Analysis, Synthesis, and Detailing. We document an artifact chain spanning material swatches, a rapid wearable prototype, Paper Models as shared negotiation surfaces, a double-layer knitted structure, and an insulated Swept Frequency Capacitive Sensing breakout board. We show how Paper Models functioned as boundary objects, helping collaborators externalize intent, negotiate spatial and technical constraints, and preserve disciplinary expertise while converging on a shared design. We contribute a reusable swatch-to-sleeve pattern for material-centered HCI: keep discipline-specific probes open early, then converge through artifacts that make material, spatial, and electronic decisions legible before fabrication locks them in.

---


### 145. [Hybrid Adversarial Defence for Natural Language Understanding Tasks](https://arxiv.org/abs/2606.04612)

**<font color=#1a73e8>作者：</font>** Manar Abouzaid, Yang Wang, Chenghua Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are vulnerable both to hallucination and adversarial manipulation. Although these problems are closely related, existing defences typically address them separately. We investigate a hybrid defence framework that combines entropy-based models, designed to reduce hallucinations, with uncertainty-based models and geometric-based models, designed to reduce vulnerability. Under in-domain tests on Natural Language Understanding datasets (FEVER, HotpotQA, CSQA, SIQA) we find our hybrid model improves both clean-task performance (up to 43.34\% increase in accuracy) and adversarial robustness (up to 64.92\% improvement in accuracy and 62.27\% reduction in attack success rate). For out-of-distribution datasets (AeroEngQA, CPIQA) we see similar adversarial robustness from our hybrid model (up to 57.14\% improvement in accuracy). For prompt injection (SafeGuard) and jailbreak detection (AdvBench, DAN) datasets our hybrid model is also very strong (up to 51\% reduction in attack success rate compared to state of the art baseline models). Overall, our results show that combining entropy, uncertainty and geometric features provides a more effective defence strategy than using any single feature alone for both in-domain and out-of-distribution tasks.

---


### 146. [A Normative Intermediate Representation for ASP-Based Compliance Reasoning](https://arxiv.org/abs/2606.04619)

**<font color=#1a73e8>作者：</font>** Yangfan Wu, Huanyu Yang, Jianmin Ji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose MONIR, a Modalized-Output Normative Intermediate Representation for ASP-based compliance reasoning. Its core fragment has a staged operational semantics, while MONIR-ASP provides an executable compilation and extensions for external functions, temporal rules, and stable-model reasoning. We instantiate the framework on Chinese ADAS regulations and standards with an LLM-assisted pipeline. Experiments evaluate extraction quality and the efficiency of modular and incremental ASP solving.

---


### 147. [MeshFlow: Efficient Artistic Mesh Generation via MeshVAE and Flow-based Diffusion Transformer](https://arxiv.org/abs/2606.04621)

**<font color=#1a73e8>作者：</font>** Weiyu Li, Antoine Toisoul, Tom Monnier 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MeshFlow, a new method for generating artist-like 3D meshes. Current mesh generators often adopt Auto-Regressive (AR) next-token prediction, a natural choice given the discrete nature of mesh topology. However, AR methods scale poorly because the inference cost is quadratic in mesh size. They also require discretizing the vertex coordinates, which introduces quantization errors. To address these challenges, we introduce a Variational Autoencoder (VAE) that, supervised with a contrastive loss, represents both continuous vertex positions and discrete connectivity in a continuous latent space. This latent space is significantly more compact than prior token-based mesh representations. We then build a 3D generator based on a Rectified Flow transformer, generating all mesh vertices and edges in parallel. Our model generates meshes 18x faster than the fastest AR generator while also achieving excellent accuracy across standard mesh-generation metrics. Homepage: this https URL, Code: this https URL

---


### 148. [Learning symplectic model reduction based on a approximation theorem of symplectic embeddings](https://arxiv.org/abs/2606.04623)

**<font color=#1a73e8>作者：</font>** Liyi Feng, Yifa Tang, Yulin Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional Hamiltonian systems play a central role in many scientific and engineering disciplines, with dynamics evolving on symplectic manifolds. Although deep learning provides powerful tools for constructing low-dimensional surrogates from data, the intrinsic symplectic structure is easily destroyed during model reduction. As a result, a standard autoencoder may produce latent coordinates that do not support a Hamiltonian flow, leading to unstable long-time prediction. In this paper, we first establish a universal approximation theorem for symplectic embeddings. Based on this theory, we propose symplecticity-preserving autoencoders (SpAE), in which the decoder is parameterized as a symplectic embedding and the encoder is constructed as the corresponding symplectic projection. This architecture is expressive enough to approximate nonlinear symplectic embeddings and the associated symplectic projections, preserves the symplectic structure exactly by construction, and can be trained by standard unconstrained optimization, thereby improving both reconstruction and prediction accuracy. Extensive experiments on high-dimensional lattice and particle systems demonstrate the effectiveness of the proposed method.

---


### 149. [Explainably Safe Reinforcement Learning](https://arxiv.org/abs/2606.04634)

**<font color=#1a73e8>作者：</font>** Sabine Rieder, Stefan Pranger, Debraj Chakraborty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trust in a decision-making system requires both safety guarantees and the ability to interpret and understand its behavior. This is particularly important for learned systems, whose decision-making processes are often highly opaque. Shielding is a prominent model-based technique for enforcing safety in reinforcement learning. However, because shields are automatically synthesized using rigorous formal methods, their decisions are often similarly difficult for humans to interpret. Recently, decision trees became customary to represent controllers and policies. However, since shields are inherently non-deterministic, their decision tree representations become too large to be explainable in practice. To address this challenge, we propose a novel approach for explainable safe RL that enhances trust by providing human-interpretable explanations of the shield's decisions. Our method represents the shielding policy as a hierarchy of decision trees, offering top-down, case-based explanations. At design time, we use a world model to analyze the safety risks of executing actions in given states. Based on this analysis, we construct both the shield and a high-level decision tree that classifies states into risk categories (safe, critical, dangerous, unsafe), explaining why a situation may be safety-critical. At runtime, we generate localized decision trees that explain which actions are allowed and why others are deemed unsafe. Our method facilitates explainability of the safety aspect in safe-by-shielding reinforcement learning, requires no additional information beyond what is already used for shielding, incurs minimal overhead, and integrates readily into existing shielded RL pipelines. In our experiments, we compute explanations using decision trees that are several orders of magnitude smaller than the original shield.

---


### 150. [CYGNET: Cypher Gate for Neural Execution Triage and Cost Containment](https://arxiv.org/abs/2606.04645)

**<font color=#1a73e8>作者：</font>** Nikodem Tomczak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models acting as agents over knowledge graphs generate Cypher queries that fail structurally (crashing at the database) or semantically (executing but returning wrong results). We place a pre-execution gate between query generation and a production Neo4j database. The gate validates structure through a four-backend chain culminating in execution against a mirror graph at 5.6 ms median latency. Structurally broken queries are routed to a corrector that iterates structured error feedback through a language model. On seven CypherBench schemas (2348 questions, ACL 2025) the pipeline maintains generation accuracy on every model tested, confirming it operates as a safe defensive layer. The corrector achieves 81% to 95% success across five models (mean 89%). On a template-generated corpus across nine schemas the gate catches 100% of parse errors, 100% of constraint violations, and 100% of schema-reference errors in path queries with labelled endpoints, at zero false positives across 1135 queries. Property sibling-swaps where the substituted name is valid on the target label score 0%, marking the formal boundary where structural validation ends and semantic validation must begin. A planner-based cost gate flags catastrophic plan structures before execution.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
