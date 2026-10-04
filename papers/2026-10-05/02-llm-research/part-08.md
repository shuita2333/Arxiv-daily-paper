# 🧠 大模型相关研究 | 2026年10月05日

> 本类共 **384** 篇论文：已确认 **365** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-384**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-384**

---

### 351. [Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation](https://arxiv.org/abs/2610.02148)

**<font color=#1a73e8>作者：</font>** Mohammed Irfan Kurpath, Jaseel Muhammad Kaithakkodan, Sahal Shaji Mullappilly 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extending a text embedding model to new modalities typically degrades text retrieval quality, and existing omni-modal embedders compensate with multi-billion parameters. We present Omni-Embed-Mini, a 0.9B-parameter model that maps text, speech, audio, images, video, and visually-rich documents into a single shared cosine space without updating any text-side parameter. Our key insight is that the teacher signal requires no separate embedding model: each media sample is paired with a dense cascaded caption, and the teacher target is simply the frozen backbone's own embedding of that caption. Because teacher and student share the same backbone weights, they inhabit byte-identical geometry, and lightweight projectors plus phased LoRA adapters on the modality encoders suffice for alignment. Training combines a Matryoshka SigLIP contrastive loss with an online hybrid hard-negative miner whose negatives sharpen as the encoder improves. The recipe carries over to a 2.3B variant by swapping in a native vision-language backbone. Omni-Embed-Mini-0.9B keeps its text weights bit-identical to the backbone, so training cannot regress text retrieval (49.57 nDCG@10 on MTEB-v2 BEIR-8), while extending it to five additional modalities, and is ~2.7x to 9.5x smaller than every open omni embedder we compare against. The 2.3B variant is competitive with the closed gemini-embedding-2, edging ahead of it on the overall-modality average. Models, code, data and evaluation harness are on our project page: this https URL

---


### 352. [From Knowledge Access to Source Learning: Developing Source-Specific Competence](https://arxiv.org/abs/2610.02150)

**<font color=#1a73e8>作者：</font>** Lucheng Fu, Kejing Xia, Yiyang Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on persistent external sources to solve sequences of knowledge-intensive tasks. Existing methods improve how source content is accessed and organized, while agent-memory systems preserve reusable knowledge from prior interactions, but repeated use of the same source is still largely treated as repeated access rather than an opportunity to progressively improve understanding of that source. We study source learning: developing reusable source-specific competence over a persistent authoritative source. We represent this competence with a persistent source model that captures reusable understanding of the source, including how its knowledge is structured, interpreted, and applied. To construct and progressively refine such models, we propose SourceLearn, which combines two complementary learning mechanisms. Self-Directed Source Learning identifies what remains incompletely understood and adaptively revisits the source, while Task-Guided Source Learning uses downstream experience to reveal local representational gaps and recurring needs in how source knowledge should be organized. In both cases, learning signals determine what should be reconsidered, while persistent updates are reconstructed from the authoritative source. Across five benchmarks and three LLM backends, SourceLearn achieves the best performance in 13 of 15 settings, with gains of up to 22.6 points over Hybrid RAG and substantial overall improvements over static source representations and experience-based memory baselines.

---


### 353. [AutoCompact: Learning When to Compact Context in Long-Horizon Coding Agents](https://arxiv.org/abs/2610.02163)

**<font color=#1a73e8>作者：</font>** Xuan Zhang, Longtao Zheng, Cunxiao Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coding agents solve repository-level software engineering tasks through long trajectories of code inspection, search, editing, and testing. As a task progresses, earlier exploration becomes stale, so managing context is more than avoiding overflow: an agent must decide when to compact, what working state to preserve, and how to continue from it. We introduce AutoCompact, which trains a coding agent to make these decisions as part of its policy. To collect training data, we run the base agent on coding tasks and use a judge to review its compaction decisions, summaries, and actions after compaction. Flawed outputs are replaced with corrected ones before being executed in the environment, so each trajectory continues from the corrected decisions. We use these trajectories for supervised fine-tuning, then jointly optimize coding and compaction through reinforcement learning with task-success rewards. Experiments on SWE-bench Verified and SWE-PolyBench Verified show that AutoCompact improves pass rates over the base model by an absolute 9.2\% and 5.0\%, respectively. The improvements hold across all evaluated inference budgets, with a 256K context window that never overflows and with a 16K window whose overflow triggers fallback compaction.

---


### 354. [Every Ablation Is a Dose: Counterweights and the Semblance of Self-Repair](https://arxiv.org/abs/2610.02173)

**<font color=#1a73e8>作者：</font>** Areeb Ahmad, Pratinav Seth, Vinay Kumar Sankarapu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ablate a component of a language model, and other components often appear to adjust and compensate. This phenomenon, termed self-repair, has been observed repeatedly, but its mechanism remains unclear. The most systematic study to date concluded that self-repair is noisy and unlikely to have a single explanation. We argue that it has one: a gain already present before any ablation. Any intervention on a causally important component can be viewed as a point on a coordinate axis $\lambda$, the signed strength of a counterfactual contrast. Hence, conventional ablation methods are uncalibrated points on this axis. We show that the causal repair response for a fine-grained unit $r$ is governed by an affine law, $E_r(\lambda)=\mathrm{own}_r+\gamma_r\lambda$. The slope $\gamma_r$ is a fixed coefficient that consistently influences the model, with or without ablation, and its sign determines whether the unit counteracts or reinforces the removed signal. On a factual-verdict task across four models from distinct families (Gemma, Qwen, LLaMA, and Mistral), we identify components including MLP neurons, OV neurons, and singular directions that follow this affine law, 68 of 81 downstream directions in all. Moreover, we can anticipate the magnitude of $\gamma_r$ from the fixed weights. On the IOI circuit of GPT-2 Small, seven of the ten heads the intervention can reach follow the law, and all seven are counterweights. From this perspective, what may appear as self-repair is a counterweight performing its usual operation when the contrastive signal emerges at the core.

---


### 355. [From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.02179)

**<font color=#1a73e8>作者：</font>** Siqi Zhu, Suozhi Huang, Kaixuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) aims to combine the strengths of RL-trained teachers in a single student, but how teacher signals affect parameter changes remains underexplored. We study Qwen3-1.7B with four domain teachers trained with RL from the same initialization as the student, comparing gradients, optimizer updates, and task learning curves, with additional SmolLM3-3B diagnostics. We find that several factors influence teacher signals. First, loss averaging implicitly weights responses: token averaging favors longer responses, and equalizing domain contributions retains this weighting within domains. Second, Adam's first moment reduces differences in parameter updates: the cosine similarity is 0.83 between teachers and 0.96 between averaging rules, despite differences in raw gradients. Third, BF16 rounding hides small changes: about 97\% of FP32 master weights differ from initialization, but only 7--11\% of BF16 weights do. Finally, the top-64 intersection KL gradient closely matches Qwen's full-vocabulary gradient, but the effect on task performance depends on averaging: mathematics accuracy is 2.6 points higher than with sampled-token policy-gradient (PG) under response averaging and 2.1 points lower under global token averaging.

---


### 356. [OmniSeek: Native Tool Integration for Multi-turn Audio-Visual Reasoning](https://arxiv.org/abs/2610.02181)

**<font color=#1a73e8>作者：</font>** Haibo Wang, Jiteng Mu, Jialu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present OmniSeek, an agentic framework that transforms an Omni Large Language Model (Omni-LLM) into an active, multi-turn reasoning agent with native tool use. Rather than passively processing an entire audio-visual sequence in a single forward pass, OmniSeek makes evidence acquisition part of the reasoning process: it dynamically decides whether to look or listen, and over which temporal window, to retrieve sparse but critical evidence across different modalities within long contexts. Through an iterative multi-turn protocol, the retrieved raw audio or visual segments are appended back into the context to support subsequent reasoning. To cold-start this capability, we build a data engine that synthesizes OmniTraj-170K, a corpus of multi-hop Chain-of-Thought trajectories with interleaved audio and visual evidence. We first supervise the model on these trajectories to instill multi-turn tool-use behavior, and then further optimize the policy via a two-stage reinforcement learning with verifiable rewards. Moreover, we introduce an Audio-Visual Necessity objective that explicitly rewards successful trajectories whose reasoning depends on both modalities, discouraging single-modality shortcuts. Extensive experiments across a wide range of benchmarks demonstrate that OmniSeek learns adaptive cross-modal evidence seeking and consistently improves audio-visual reasoning performance.

---


### 357. [Generative modeling of intrinsically disordered protein regions by reinforcing sparse autoencoder features](https://arxiv.org/abs/2610.02189)

**<font color=#1a73e8>作者：</font>** Jason X. Liu, Sebastian Ibarraran, Frank Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intrinsically disordered protein regions (IDRs) play central roles in cellular processes such as transcriptional regulation, signal transduction, and subcellular localization, yet their functional design remains challenging. Structure-based design methods do not readily apply to IDRs, and existing protein language models are trained on full-length protein sequences, thus learning a prior that is biased towards folded domains. Here, we present IDiom, an autoregressive protein language model trained on IDiom-DB, a dataset of 54 million predicted IDRs curated from the AlphaFold Database. IDiom generates diverse sequences that recapitulate the composition, patterning, motifs, and predicted disorder of natural IDRs. To control function-associated sequence patterns, we also introduce reinforcement learning with sparse autoencoder features (RL-SAE), a post-training method that rewards the generation of sequences that activate specified feature sets. Across eight IDR design tasks, RL-SAE sequences activate, on average, 90% of 30 targeted features, compared to 24% for activation steering. We demonstrate that RL-SAE improves the predicted subcellular localization and transcriptional activity of generated IDRs compared to steering and supervised fine-tuning, and enables features associated with distinct biological functions to be combined within individual sequences. Thus, IDiom and RL-SAE enable interpretable and composable IDR design through explicit control of function-associated sequence features. More broadly, RL-SAE could extend to other protein design settings where interpretable features provide useful design targets. Code is available at this https URL.

---


### 358. [Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM Fine-Tuning](https://arxiv.org/abs/2610.02190)

**<font color=#1a73e8>作者：</font>** Cristian McGee, El Houcine Bergou, Aritra Dutta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Step-size selection remains a central challenge in large-scale neural network optimization; conservative steps slow convergence, while aggressive steps can destabilize it. We combine \textbf{Z}ero-and-\textbf{F}irst-\textbf{O}rder optimization~(ZFO) and propose a lightweight framework that decouples direction selection from step-size. ZFO uses a trusted first-order optimizer to determine the direction and performs zeroth-order evaluations only along this one-dimensional subspace to choose how far to move. Using the current {gradient information} and two additional objective function evaluations, ZFO instances construct a local model of the objective function along the proposed direction and select a curvature-aware step within a bounded search interval. This yields an adaptive step-selection mechanism that costs less than a full line search. We provide theoretical guarantees to show that shared-sample evaluations produce reliable finite-difference curvature estimates, that the induced local model selects a near-optimal step along the search interval, and that ZFO converges to a neighborhood of a stationary point. Across the evaluated settings, language models and datasets, ZFO frequently improves optimization and final performance relative to fixed-step first-order baselines, with the magnitude and preferred local model depending on the objective. Our code is publicly available at: this https URL.

---


### 359. [The Missing Primitive: Diagnosing and Repairing Mathematical Reasoning in Large Language Models](https://arxiv.org/abs/2610.02191)

**<font color=#1a73e8>作者：</font>** Shuo Xing, Zilin Dai, Chengyuan Qian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have demonstrated striking capabilities on frontier mathematical problems, it remains unclear whether they possess the structural mathematical understanding underlying their solutions. In this paper, we take a first step toward systematically studying mathematical understanding in LLMs, from diagnosing its distinct capabilities to leveraging these findings to improve post-training. First, we introduce the notion of Mathematical Primitive to probe structural mathematical understanding and propose \hlei{}, a novel benchmark that evaluates mathematical reasoning along four distinct dimensions: Discovery, Generation, Digestion, and Execution. Second, our systematic diagnosis shows that solution accuracy masks distinct capability profiles, primitives unlock substantial latent execution capacity, and Discovery is the dominant bottleneck in mathematical reasoning. Our post-training analysis further shows that discovery-limited failures are particularly amenable to repair. Finally, building on these findings, we introduce \abs{}, a primitive-privileged self-distillation framework that selectively transfers primitive-guided reasoning into the student model. Extensive experiments demonstrate that \abs{} consistently improves mathematical reasoning over baselines across model scales and challenging benchmarks.

---


### 360. [Hierarchical Continuous Diffusion Language Models](https://arxiv.org/abs/2610.02193)

**<font color=#1a73e8>作者：</font>** Hui Ren, Zihan Li, Chang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models offer a compelling alternative to autoregressive generation for tasks demanding bidirectional reasoning and global constraint satisfaction. Yet they share a structural bottleneck: when decoding in parallel, each token is sampled independently from its marginal, severing the statistical dependencies among the tokens decoded together. Continuous diffusion language models avoid this by denoising a shared continuous state, but their denoiser sees only that state, so nothing ties it to a valid token configuration until it is finally decoded. To address this, we propose Hierarchical Continuous Diffusion Language Models (HC-DLM), which couple discrete token generation with a continuous latent trajectory in a single, principled denoising process, whose training objective is derived from a variational bound on the token likelihood. In contrast to recent methods that attach continuous context to a self-contained discrete chain, HC-DLM makes the latent the only persistent generative state: tokens are read out from it at every step and feed back as a scaffold for the next latent update. On structured reasoning (Sudoku), mathematical planning (Countdown) and language modeling (LM1B), HC-DLM improves over discrete and continuous diffusion baselines at matched model size, in puzzle accuracy on Sudoku and Countdown and in generative perplexity on LM1B. Project page: this https URL.

---


### 361. [TACO: Ternary Absolute-max Column-wise One-sparse Optimizer for LLM Fine-Tuning](https://arxiv.org/abs/2610.02199)

**<font color=#1a73e8>作者：</font>** Jichao Jiang, Cristian McGee, El Houcine Bergou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full-parameter fine-tuning of large language models (LLMs) incurs substantial optimizer state memory overhead, limiting the model sizes that fit on modern GPUs. Existing approaches either compress optimizer state, abandon first-order gradients, or change the update geometry while retaining dense state. The recently introduced Muon optimizer reduces optimizer memory through matrix-valued updates. Still, its geometry differs from AdamW and can lead to performance degradation when fine-tuning AdamW-pretrained models. To reduce optimizer memory without sacrificing accuracy or computational efficiency in LLM fine-tuning, we propose Ternary Absolute-max Column-wise One-sparse optimizer, or TACO, which follows Muon's operator-norm steepest-descent view but takes the geometric route further. TACO computes the exact steepest-descent direction under a dimension-normalized $1\to1$ operator norm by selecting the sign of the largest magnitude entry in each column of two-dimensional weight matrices. This retains first-order gradients while making optimizer state memory nearly negligible. Our practical TACO optimizer maintains only a small set of low precision gradient components per column, reducing persistent optimizer state by $174\times$ relative to AdamW8bit (from 27.7 GB to 0.16 GB) and peak training memory by $2.9\times$ (from 80.6 GB to 27.5 GB) on OPT-13B, while achieving comparable accuracy and runtime. TACO further enables full-parameter fine-tuning of 30-32B-parameter models on a single 80 GB H100 GPU across multiple model families and tasks.

---


### 362. [VISTA: A Visual Harness for Reasoning in an Interactive World](https://arxiv.org/abs/2610.02200)

**<font color=#1a73e8>作者：</font>** Qiushi Han, Keya Hu, Linlu Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We show that multimodal models possess strong reasoning abilities and that an appropriate harness can unlock their potential to solve tasks across diverse interactive environments. We introduce VISTA, a visual harness that gives a general-purpose multimodal model long-horizon vision. VISTA allows the model to directly perceive the environment through visual observations and maintains a lossless visual memory that preserves past observations in their original form. The model can actively retrieve these observations and reorganize its visual input as it reasons. On ARC-AGI-3, VISTA improves Claude Opus 5.0's Relative Human Action Efficiency score from 40.68 to a perfect 100.00, with the model completing all 25 public games using 57.4% fewer actions than first-time human participants. VISTA's simple design also allows it to extend naturally to diverse visual environments with minimal adaptation. Across three additional benchmarks covering a diverse range of visual games and puzzles, it substantially outperforms baselines using the same underlying model with minimal harnesses. Our results highlight VISTA's potential as a general-purpose visual harness for advancing multimodal agents in complex visual environments.

---


### 363. [ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research](https://arxiv.org/abs/2610.02202)

**<font color=#1a73e8>作者：</font>** Sohyeon Kim, Yoonho Lee, Bo Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What makes great scientists great? Even as AI systems start to make progress on open problems, scientists remain far ahead of them at sensing which prior idea, buried in an ever-growing archive of research, a new problem needs. To study this skill, we draw on researchers who know firsthand which earlier work advanced their completed projects, with papers serving as pointers to the ideas within. Using our automated pipeline that makes author annotation scalable, we build ScholarCatalyst by having 184 lead authors of 207 recent computer science papers label which candidates did or could have advanced their project, each with a detailed rationale. We introduce a retrieval task with author-provided judgments: given an initial research question, retrieve these papers from only the literature available when the project began. Agentic search does no better than embedding retrieval (0.42 vs. 0.48 Recall@20) despite calling that same retriever as a tool. Even an agent built on Claude Fable 5.1, which may have seen the completed papers during training, reaches only 0.51 R@20. These results highlight the need for new training recipes that equip models with expert intuition for searching broad corpora. We envision ScholarCatalyst as a step toward scientific agents that can take a half-formed idea and point to the prior research it needs.

---


### 364. [ROWBench: Do Video Models Render What the Program Specifies?](https://arxiv.org/abs/2610.02205)

**<font color=#1a73e8>作者：</font>** Zheng-Hui Huang, Guixu Lin, Yu-Ju Tsai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Programmable world models separate executable dynamics from visual generation, offering a promising foundation for next-generation game engines. However, their visual adherence to explicit rules and interactions remains insufficiently evaluated. Existing benchmarks assess visual quality, controllability, and instruction or physical adherence, but rarely test fidelity to fine-grained, program-specified world events. We introduce PROWBench, comprising 170 programmatically constructed episodes and 600 proxy videos covering diverse scenes and interactions. PROWBench logs entity states and timestamped events, including those outside the camera's field of view, as replayable world records, from which it renders synchronized views and proxy representations. This enables generated videos to be checked against the observable consequences of program execution. An extensible framework constructs scenes, controls behaviors, and can render each camera view in different representations, such as coarse 3D, and bounding boxes. The benchmark covers first- and third-person perspectives, with synchronized multi-view observations available for a subset of episodes. Grounded in these records, PROWBench evaluates entity control, long-horizon memory, and, with two VLM-based metrics, Logic-Render Alignment and Interaction Success Rate, adherence to the prescribed timeline and the visual realization of timestamped engine-recorded events.

---


### 365. [KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards](https://arxiv.org/abs/2610.02206)

**<font color=#1a73e8>作者：</font>** Pengfei Li, Naufal Suryanto, Sicheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly applied to cybersecurity workflows, where they are expected to translate analysts' intent into tool invocations. However, existing evaluations focus on knowledge-based assessments or end-to-end agentic tasks, and do not directly measure LLMs' ability to generate executable commands for real-world cybersecurity tools. This gap is critical because cybersecurity operations rely on strict command-line interfaces (CLIs), where minor syntax errors, incorrect flag--value bindings, or argument misordering can invalidate execution. We introduce KaliBench, a fine-grained benchmark and dataset for natural-language--to--CLI translation on Kali Linux, comprising 8,504 query--command pairs spanning 1,642 tools across 23 capability dimensions and 5 security phases. KaliBench is constructed via a manuscript-grounded pipeline with deterministic canonicalization and alias-aware evaluation, enabling precise and reproducible assessment of tool selection and argument construction. To ensure both semantic correctness and practical executability, we develop a multi-stage verification pipeline that combines LLM-based validation, sandboxed terminal execution, and human-in-the-loop refinement. Building on these fine-grained, deterministic signals, KaliBench further enables runtime-free verifiable rewards for training. Across three evaluation modes and 24 configurations of general-purpose and security-focused open-weight models, no open-weight model exceeds 42% exact-command accuracy in the unrestricted setting, highlighting the difficulty of accurate CLI-based cybersecurity tool use without explicit tool hints. We further show that supervised fine-tuning and reinforcement learning with verifiable rewards derived from KaliBench significantly improve an 8B model and achieve performance comparable to a 685B MoE model.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 366. [Nous: Learning and Certifying Memory Decisions Before Source Calibration](https://arxiv.org/abs/2610.00094)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pranav Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Belief-based agent memory needs reliable decisions about current state, yet its evidence may be noisy, copied, or stale. Must a memory calibrate its sources before it can improve its decisions? We separate learning, calibration, and revision certification. On one four-model hidden Markov family, learning an unknown Bayes decision requires Theta(l^-2) records and certifying its improvement over an informative incumbent takes O(l^-2) fresh records from the same observation law, while fixed-precision source estimation requires Theta(l^-4) as persistence l vanishes. Thus learning and certifying useful decisions can require quadratically fewer records than source calibration. A broader model class retains the decision rate and source lower bound. Under an unknown identity-plus-background report channel, we characterize the sharp identified interval for policy improvement and derive a finite-sample certificate using observable witness regions, without pure-class anchors. A robustness extension tolerates bounded history-dependent misspecification and conditional copying; split-trained witnesses apply to arbitrary history spaces with explicit power conditions. We integrate policy-bound receipts with Nous Dimensions and test 45,000 held-out mutable-state histories and 9,000 episodes in three external MiniGrid memory environments with an introduced noisy-report interface. The new certificate accepts 9/9 improvements over a constant incumbent and 4/9 over last-write-wins, versus none for the earlier certificate in MiniGrid. Strong established inference baselines remain competitive or better. The result is a statistical account of when memory decisions can be learned and justified without recovering source reliability, not a universally superior memory algorithm.

---


### 367. [A Low Grounding Score Is Not an Ungrounded Judge: Identifying the Perceptibility Confound in Multimodal Oversight](https://arxiv.org/abs/2610.00111)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rasul Khanbayov, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model judges now supervise multimodal systems at scale, filtering training data, selecting outputs, and supplying the reward that shapes multimodal reasoning models. Trusting one means first checking that it uses its evidence, and that check is itself worth scrutinizing, so we ask whether a counterfactual probe of visual grounding measures what it claims to. The probe edits the image so the ground truth flips, holds the reasoning trace fixed, and asks whether the verdict follows. We formalize it as the Verdict Grounding Score and show it cannot be read the way such scores are read. A verdict responds only to an edit that reaches the judge's decision-relevant reading, so the score is capped by how perceptible the edit is, and unless editing makes the attribute easier to read, the error is one-sided: the score can only make a judge look less grounded than it is. The practical failure is therefore a false alarm, an auditor discarding a usable overseer. Under assumptions we state, we show this missing quantity is not merely bounded but identified from three quantities the same audit protocol already collects, which makes the false-alarm rate directly measurable rather than merely a concern. Auditing nine judges, we find the predicted ordering holds strictly across our entire primary pool, and the typical judge there acts on only about half of the edits whose attribute it can otherwise resolve. Applying a conservative rejection threshold certifies several cells as false alarms outright, the clearest being a judge that detects the injected error essentially every time while still scoring as if it had not used the image at all. The rule that follows is that an image-side counterfactual score should never be reported alone: a detection probe on the unedited image upper-bounds it, certifies its false alarms, and costs nothing extra to run.

---


### 368. [Coupling Perception and Reasoning in Federated Multimodal Graph Foundation Models](https://arxiv.org/abs/2610.00277)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zekai Chen, Xun Wu, Hailin Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated multimodal graph foundation models (GFMs) aim to adapt pretrained multimodal models to decentralized graph data, where each client owns a private multimodal graph and cannot share raw information. These models typically combine a multimodal Encoder that extracts semantic evidence from heterogeneous modalities and a graph neural network (GNN) that performs relational reasoning over graph structures. However, existing federated GFM adaptation methods mainly update graph-side modules while keeping the multimodal Encoder frozen, limiting adaptation to \emph{how information is propagated} while fixing \emph{what information is extracted}. Through empirical studies, we reveal that Encoder and GNN adaptations are not independent: Encoder adaptation is affected by graph relations, while cross-client module swapping reveals substantial pairing sensitivity between separately parameterized Encoder and GNN updates. Motivated by this observation, we propose \textbf{FedCORE}, a federated adaptation framework that represents Encoder and GNN updates through a shared low-dimensional latent state. FedCORE jointly optimizes this core from multimodal and structural signals and performs federated evolution directly in the shared state space, preserving compatibility between perception and reasoning adaptations. Extensive experiments demonstrate that FedCORE reduces the Encoder--GNN pairing gap from $30.6$ to $5.9$, corresponding to an $80.7\%$ reduction over independent joint adaptation.

---


### 369. [RACE: Residual-Aware Test-Time Adaptation for Neighbor-Rich Time-Series Foundation Model Forecasting](https://arxiv.org/abs/2610.00405)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hao-Nan Shi, Tong Wu, Chen-Cong Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models (TSFMs) perform strongly across forecasting tasks, but their per-series inference is ill-suited to neighbor-rich forecasting, where each query has access to related but nonidentical historical series. Continuous glucose monitoring (CGM) and Web/cloud workloads exemplify this setting: CGM trajectories share physiological patterns but vary across individuals, devices, and conditions, while Web/cloud workloads combine common operating regimes with non-stationarity, heavy tails, and bursts. These histories share useful structure, yet neighbors are not equally relevant. Existing methods either fine-tune TSFMs for each target domain, incurring additional costs and offering limited transferability across backbones, or append retrieved series without verifying whether they support the current forecast. The key challenges are conflicting residual evidence from neighboring series and residual patterns that vary across TSFMs and forecasting tasks. We formulate test-time neighborhood scaling: using same-domain neighbor evidence without modifying the backbone. We propose RACE (Residual-Aware Correction of Forecasting Errors), a two-stage framework for using historical neighbors. We first retrieve query-compatible neighbors, align their residuals to the query scale, and aggregate coherent evidence into the training-free RACE-TF correction. Full RACE then uses a lightweight, domain-specific Gate to determine when applying the correction is beneficial, with a reusable training workflow across TSFM backbones. Across four TSFMs, RACE improves all three domain-aggregate metrics on both primary domains, with the largest gains on high-error queries. Within each domain, a Gate trained on one TSFM transfers to other backbones without adaptation, and the resulting pipeline improves all 72 cross-backbone metric comparisons over the matched frozen targets.

---


### 370. [From Image Latent Space to Fuzzy Rules: Interpretable Analysis of Gastrointestinal Foundation Model](https://arxiv.org/abs/2610.00414)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Michael D. Vasilakakis, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models pretrained on large-scale datasets demonstrate strong transferability to medical imaging tasks. However, understanding how their latent representations encode clinically relevant information remains an open challenge in safety-critical domains. This study proposes a prototype-based fuzzy-rule framework that interprets the patch-level features produced by the inner layers of pretrained foundation models, without any fine-tuning. Class-specific prototypes are learned by clustering in the feature space, yielding compact visual patterns. Patch features are then expressed as prototype similarities and classified by fuzzy rules with linguistic IF-THEN conditions that are human readable. The framework is applied across the final two blocks of ViT-S/16 backbones pretrained on ImageNet-1K and GastroNet-5M, and benchmarked against k-nearest neighbours, kernel SVM, and linear probing under identical frozen features, on wireless capsule endoscopy classification, gastrointestinal endoscopy classification, and colonic polyp segmentation. The experimental analysis shows that the proposed method, without backbone fine-tuning, reaches accuracy comparable to these black-box classifiers, and that domain-specific pretraining yields features that are both discriminative and symbolically compressible. Because the resulting rules are extracted from real data and expressed in interpretable terms, they are further used as an instrument to investigate synthetic medical images, providing a human-readable account of which real prototypes and rules a generator reproduces or fails to reproduce, localising where a synthetic image departs from real tissue rather than summarising it with a single score. The framework thus offers a transparent, depth-resolved view of how foundation models organise clinically relevant structure, together with a practical downstream use of the extracted rules.

---


### 371. [Random Recursive Models](https://arxiv.org/abs/2610.00541)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jama Hussein Mohamud, Mirco Ravanelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive models create computational depth through parameter reuse, offering a parameter-efficient alternative to increasing model size. However, most recursive models repeatedly apply one learned transformation or a prescribed sequence of transformations, restricting computation to a fixed layer order. We introduce the Random Recursive Model (RRM), which maintains a pool of $L$ learned layers and performs $T$ recursive steps by sampling one layer independently with replacement for each example and step. This enables flexible layer reuse while retaining the parameter efficiency of recurrence. We evaluate RRM on challenging reasoning tasks, where it matches or exceeds the baselines, often with 50-75 % fewer parameters. RRM can vary its depth at inference, including beyond that seen during training, without retraining or adding parameters, improving tasks that benefit from deeper iterative computation. RRM also supports Monte Carlo inference and probabilistic test-time scaling, both of which improve performance without retraining. These insights may open new directions in neural network architecture design.

---


### 372. [Towards Fast and Disentangled Counterfactuals for Visual Foundation Models](https://arxiv.org/abs/2610.00895)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sidney Bender, Benedikt Kunz, Ahmed Zeid 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models remain vulnerable to spurious correlations and ``Clever Hans'' strategies. Explainable machine learning can find and remove such strategies for classifiers without metadata. For foundation models, no such option exists yet. We propose Disentangled Diffusion Autoencoders (DiDAE). DiDAE wraps a frozen foundation model in a conditional diffusion decoder. A counterfactual is one closed-form edit along a direction of a disentangled dictionary, followed by decoding. The dictionary can be supervised (Procrustes) or unsupervised (Singular Value Decomposition, Sparse Autoencoders). No gradients are needed, so DiDAE is up to 2000 times faster than the state of the art. We evaluate on six datasets, two synthetic and four real-world. In a desiderata-driven benchmark on three of them, its counterfactuals are on par with or better than the state of the art, and they repair downstream classifiers through Counterfactual Knowledge Distillation (CFKD), where they beat metadata-based correction. The same machinery can rank a pretrained dictionary against a trained classifier. It returns the few directions the classifier actually reads, each causally verified by a counterfactual that flips the decision, and repairs the classifier along those a teacher marks spurious. The workflow is plug-and-play in our open-source Peal library we publish alongside the paper. With a public dictionary and a pretrained decoder, all that remains is a cheap linear distillation of the classifier and its own fine-tuning.

---


### 373. [Adapter Thickets: Splitting an RLVR Budget Beats Concentrating It](https://arxiv.org/abs/2610.00991)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jonathan Williams, Esin Tureci Karthik R. Narasimhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Majority voting over sampled completions is the workhorse of test-time scaling, and reinforcement learning with verifiable rewards (RLVR) is the workhorse for making each completion better. The standard pipeline composes the two: train one policy with RLVR, then sample it many times and vote. We show that this composition is lossy. A vote can only overturn mistakes that its voters do not share, and RLVR sharpens a policy so that its samples increasingly make the same mistakes. With every method drawing exactly $160$ completions per problem, training a single LoRA adapter on the full RLVR budget raises single-sample accuracy on every model we test ($1.5$B-$8$B). Yet on three of four models it leaves the majority vote below that of the untrained base model, by up to $4.8$ points. The damage builds during training: voter errors grow steadily more correlated, and the majority vote accuracy peaks early before falling by up to $7.0$ points. The cause is concentration, not RLVR itself. We split the same data and training budget across $K$ LoRA adapters, each trained on its own random disjoint shard, and call the result an adapter thicket. Thickets out-vote the fully trained adapter in all $16$ (model, $K$) settings, and for $K{\geq}4$ they stay within $0.8$ points of the base model or above it. A single adapter stopped early, at a thicket member's step count, is a strong control that matches thickets for small $K$. For $K{\geq}8$, thickets keep more of RLVR's single-sample gain and out-vote this control in six of eight settings. The cost of concentration also grows with the number of votes: from $16$ to $160$ votes, the thicket's lead over the fully trained adapter widens from $1.3$ to $3.3$ points. When the plan is to sample and vote, an RLVR budget is better spent broad than deep.

---


### 374. [CortexBridge: Cortical Alignment of EEG Montages for Foundation Models](https://arxiv.org/abs/2610.01124)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiazhen Hong, Xiaotian Zhou, Zihao Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) foundation models are often pretrained with a fixed channel vocabulary or a limited set of montages, making transfer difficult when electrode layouts change. We propose CortexBridge, a lightweight adapter that combines EEG features with electrode and atlas coordinates to map arbitrary montages into a shared cortical latent space. Evaluated with three frozen foundation models on five brain-computer interface (BCI) datasets from the Mother of All BCI Benchmarks (MOABB), CortexBridge improves performance in 13 of 15 evaluations. The gains in balanced accuracy average 0.80% for EEGPT, 0.70% for LaBraM, and 3.26% for CBraMod, with a maximum gain of 13.02% on 12-class steady-state visual evoked potential (SSVEP) classification. Visualizations of the learned atlas representations reveal task-dependent spatial patterns, with SSVEP showing a more concentrated representation in the Yeo Visual network than auditory P300. These results establish cortical alignment as a learnable and anatomically grounded routing mechanism from heterogeneous EEG montages to pretrained foundation models.

---


### 375. [Parameter-Efficient Distributionally Robust Adaptation of Tabular Foundation Models under Subpopulation Shift](https://arxiv.org/abs/2610.01143)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Seonghwi Kim, Sung Ho Jo, Minwoo Chae  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite strong mean accuracy, tabular foundation models (TFMs) can perform poorly on underrepresented groups under subpopulation shift, where group proportions change between training and deployment. We propose DR-TFM, a parameter-efficient distributionally robust adaptation framework that requires no true group annotations. DR-TFM adjusts attention to labeled context examples by fine-tuning an existing query scaling network or adding and training one, while keeping all other parameters fixed. We instantiate the framework with two robust objectives using estimated groups or source conditional distributions derived from training data. For TabPFN-3, adaptation updates only 0.016% of the pretrained model's parameters. Across five tabular benchmarks, DR-TFM achieves substantially higher average worst-group accuracy than pretrained TFMs and the compared robust baselines without true group annotations, while maintaining competitive mean group accuracy. DR-TFM also improves average worst-group accuracy on ACS Income and across four additional TFMs.

---


### 376. [Flow Matching Reinforcement for 3D Mesh Generation via Dynamic Homing Optimization](https://arxiv.org/abs/2610.01233)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhen Zhou, Zhiwei Ning, Puhua Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching is central to 3D generation, yet in practice its reinforcement learning (RL) methods are largely adapted from 2D visual generation. Representative DPO-, GRPO-, and NFT-style objectives, when applied to negative trajectories, mainly steer predicted velocities away from the corresponding directions without explicitly specifying a target velocity field toward preferred samples. In 3D generation, constrained by pretrained model capabilities, rollout diversity, and reward-distribution complexity, directly applying these RL methods yields limited gains in geometric quality. We introduce a forward-process RL method \textbf{Dynamic Homing Optimization (DHO)}, which reformulates negative-trajectory optimization as positive-sample attraction-guided dynamic homing. Specifically, Minimum-Cost Attractive Matching (MAM) assigns each negative sample a distinct positive target, and Time-Aware Dynamic Correction (TDC) then redirects its trajectory toward the target using a remaining-time-aware corrective velocity. Building on asynchronous online DHO, we develop \textbf{Flow3D-Pro}, an image-to-3D geometry generation framework. Experiments show that DHO outperforms representative DPO-, GRPO-, and NFT-style objectives in 3D generation, while Flow3D-Pro produces higher-quality 3D geometry than existing mesh generation methods.

---


### 377. [Distillation of Tabular Foundation Models into Efficient Predictors](https://arxiv.org/abs/2610.01435)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Minho Jeong, Dooho Lee, Jinmo Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) achieve strong predictive performance through in-context learning, yet repeatedly conditioning on labeled data makes inference expensive. Knowledge distillation can reduce this cost by transferring their predictive ability to lightweight, dataset-specific students. However, the dependence of TFM predictions on both a labeled context and a query introduces two design questions: how to construct teacher supervision and whether expanding query coverage improves distillation. We examine these questions across two TFMs and both neural and tree-based students, and derive an effective distillation recipe. The recipe uses the full labeled training set as teacher context and trains students solely on teacher predictions for observed and synthetic queries. On TabArena, the resulting students outperform their supervised trained tuned-and-ensembled counterparts by 57-98 Elo points. Applied unchanged to TALENT, the same recipe improves matched default students on 236-258 of 300 datasets and reduces median primary error by 4.0-6.4%. The distilled students also achieve median inference speedups of 3.0-21.6 times over their teachers, offering a practical trade-off between predictive performance and repeated inference cost. Code is available at this https URL .

---


### 378. [RelICL: Training-free Relational Learning with Tabular Foundation Models](https://arxiv.org/abs/2610.01725)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Simon Forbat, Rainer Gemulla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models achieve state-of-the-art performance on single-table tasks without any training. Recent work suggests that they are also well-suited for relational learning via deep feature synthesis (DFS), which flattens a relational schema into a single table by adding aggregates of the other tables' columns as features. This approach is appealing because it directly benefits from improvements to or customization of the underlying tabular foundation model. In this paper, we identify two key problems with DFS: feature explosion and interaction blindness. The first problem arises because the number of DFS features grows quickly as the schema becomes more complex, limiting scalability and performance. The second problem arises because column-wise aggregates do not account for feature interactions, limiting performance. We propose and explore an alternative method termed RelICL, which keeps the benefits of DFS but alleviates these two problems. At its heart, RelICL propagates and fuses information step by step through the schema graph, using the same tabular foundation model that is eventually used for prediction to do so. In our experimental study using RelBench tasks, RelICL was on par with the strongest approach based on deep feature synthesis.

---


### 379. [Function-Structured Reinforcement Learning with Executable Verifiers for Mathematical Reasoning](https://arxiv.org/abs/2610.01729)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zihan Liu, Xurong Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithmic mathematical reasoning requires reliable decomposition, computation, and aggregation. Final-answer rewards provide limited guidance on intermediate errors, while successful execution does not guarantee mathematical correctness. This work proposes Function-Structured Graph Reinforcement Learning (FSG-RL), connecting subproblem graphs and Python implementations with multi-verifier feedback. The policy first learns to generate code from function graphs through supervised fine-tuning (SFT). Group Relative Policy Optimization (GRPO) then optimizes the policy using answer-gated rewards and span-level credit assignment. The framework also supports teacher supervision and structured memory. A benchmark curated from Grade School Math 8K (GSM8K), MathQA, MATH, and Omni-MATH pairs public function graphs with private verification specifications. Under a unified evaluation protocol, GRPO improves final-answer accuracy from 43.25% to 67.50% and full solution success from 32.25% to 52.25% over SFT. Continued reinforcement learning (RL) with teacher supervision yields additional gains. The gains extend beyond producing correctly formatted code, supporting verifier-guided reinforcement learning for mathematical reasoning. Code is available at this https URL.

---


### 380. [Scientific Discovery under Validation Congestion via Multi-Fidelity Pairwise Rankings](https://arxiv.org/abs/2610.01827)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kevin Tirta Wijaya, Alston Lo, Michael Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern computational methods can now propose candidate molecules, materials, and other scientific designs at an unprecedented scale, creating a validation congestion where candidates are abundant, but experimental capacity to physically evaluate them remains scarce. Discovering novel scientific designs has therefore become increasingly dependent on curation: selecting a small set of promising designs for slow and costly experiments. Existing curation methods typically rely on data-driven regression models that predict absolute scores, but training these models requires substantial experimental data to begin with. Yet, useful curation signals do not have to take the form of absolute measurements, as scientific design discovery is often comparative in nature. Here, we propose that curation can instead be primarily driven by expert pairwise rankings, which are substantially easier to gather. The expertise can come from computational tools or human input of multiple levels of fidelity, ranging from empirical rules of thumb to agentic workflows and experienced scientists. We introduce PRISMS, a framework that uses pairwise rankings from one or more experts, potentially spanning multiple levels of expertise, to identify the most promising candidates without relying on data-hungry regressors. When experts differ in fidelity and cost, PRISMS escalates pairwise queries from lower- to higher-fidelity rankers based on a Fisher-information criterion. In iterative screening that selects designs from fixed drug discovery libraries, PRISMS achieves 50% top-10 discovery recall in ~42% fewer rounds than regression-only active learning, and in ~15% fewer rounds than the ranking-based method with no selective escalation. In optimization that generates new designs without restriction to a predefined library, PRISMS achieves ~18.8% higher hypervolume than the Bayesian optimization baseline.

---


### 381. [Pooling Helps, Learned Weighting Hurts In-Context: Decomposing Group Attention](https://arxiv.org/abs/2610.01831)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Michael Fore, James Mason Inder, Mrishika Nair 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group attention, introduced by the time series forecasting model Chronos-2, attends over the variates of a group at a fixed patch index and serves both multivariate (MV) and in-context learning (ICL) forecasting. Rather than evaluating this cross-variate attention design as a whole, we ask which part of the mechanism earns the benefit and probe its applicability to both MV and ICL regimes. By editing the attention matrix $\alpha$ at inference we separate the two pathways a head comprises: V/O, which projects a weighted summary of the group, and Q/K, which decides the weights. Uniform pooling (V/O without any Q/K weighting) is positive on 18 of our 20 sensor-network configurations, while the learned weighting (Q/K) splits by group type: its contribution is positive or negligible for MV, but materially degrades 8 of the 10 sensor-network ICL configurations, leaving 4 of them worse than univariate inference. By isolating the impact of different layers, we find that uniforming $\alpha$ in the first block alone improves every ICL configuration we test.

---


### 382. [Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents](https://arxiv.org/abs/2610.01892)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Feiyu Gavin Zhu, Xiaoyu Zhu, Jiqi Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal agents commonly generate free-form reasoning before each action. For small models, limited model capacity can result in lengthy reasoning that provides little useful guidance for action generation while incurring substantial inference cost. To address this challenge, we introduce Selection-based Structured Reasoning (SSR), a framework that reformulates reasoning as selection instead of open-ended generation. SSR represents recurring high-level reasoning as pre-specified, reusable natural-language candidates. At each turn, the model selects from these reasoning candidates based on their likelihoods given the current context, without requiring an auxiliary task head. Using pre-specified reasoning traces enables parallel scoring, where teacher-forced prefilling computes token likelihoods concurrently within and across candidates using a shared context KV cache. We evaluate SSR on seven multimodal search benchmarks using 2B and 4B models. Across multiple reinforcement learning objectives and supervised fine-tuning, SSR delivers significant efficiency gains without sacrificing task performance. SSR achieves an average success rate competitive with leading search agents of the same scale, while reducing per-turn reasoning latency by over 90% and total per-question model inference latency by 28-54%. Project page: this https URL.

---


### 383. [Same Reward, Different Skills: When Multimodal RL Learns to Look](https://arxiv.org/abs/2610.01908)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haocun Ye, Xinlong Jiang, Qile Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves vision-language benchmark scores even without visual information during training. With images at test, blind-trained models recover roughly half of the real-image gain at 3B and nearly four fifths at 7B. Prolonged real-image training can erode grounding while benchmark gains persist. Both findings expose the same gap: an image in the prompt is not an image in the learning signal. Our design rule, visual resolvability, asks that visual evidence be necessary for a correct answer and that the task remain learnable. We test it on counterfactual coordinate scenes in which the question stays fixed and the target is never named, so a correct answer requires finding the target in the image. With standard GRPO and correctness-and-format rewards, a 7B model raises its accuracy at finding the target (discovery) from 0.425 to 0.875 on held-out scenes denser than any it trained on, and it improves on question types it never trained on. Two controls locate the source of the gain. Replacing test images with gray canvases drops discovery to zero; training on gray canvases instead, at matched step 30 and in each of four seeds, yields essentially none of the gain even when the model is then tested with real images. The learned skill carries over to grounding tasks built independently of the training corpus. A caption that answers the training question, added to the same images, reward and budget, cuts the gain by nearly two thirds. Changing what reward requires changes what RL learns.

---


### 384. [Higher-Order Molecular Grammars for Generative and Foundation Models in Chemistry](https://arxiv.org/abs/2610.02186)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yiming Huang, Yujie Zeng, Vijay Prakash Dwivedi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular learning models are strongly shaped by their underlying representations. Yet standard sequential and graph formalisms struggle to explicitly encode higher-order topology, such as ring systems and recurring motifs. Existing higher-order representations can capture these structures directly, but they are often computationally demanding and difficult to decode into valid molecules. Here, we introduce Higher-order Grammar Representation (HGR), a principled, topology-aware framework that lifts molecules to combinatorial complexes and parses each complex into a compact sequence of production rules under a context-free higher-order grammar. By serialising higher-order topology into rule sequences, HGR makes these structures directly compatible with standard sequence models, avoiding the computational overhead of explicit higher-order encodings while preserving topological expressiveness. To reduce benchmark bias towards simple ring systems, we construct RingDiv, a ring-enriched benchmark containing 1.18 million molecules, including the curated RingDiv300k subset, and introduce the ring diversity index (RDI) to quantify ring-system coverage. In molecular generation, HGR-based models uniquely combine 100% validity by construction with leading distributional alignment, ranking first in FCD on all five generation benchmarks. In representation learning, HGR-FM achieves the highest mean AUC across seven MoleculeNet benchmarks under both transfer protocols, improving on the strongest baseline by 8.3 and 3.3 AUC points under probing and full fine-tuning, respectively. Collectively, these results establish HGR as an efficient higher-order representation for molecular generation and transferable representation learning.

---


> [!TIP]
> 当前位于：**351-384**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-384**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
