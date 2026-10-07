# 🧠 大模型相关研究 | 2026年10月08日

> 本类共 **303** 篇论文：已确认 **280** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-303](./part-07.md)

---

### 1. [When Does External Guidance Help LLM Reasoning? A Bias-Variance Theory of Guidance-Augmented GRPO](https://arxiv.org/abs/2610.06861)

**<font color=#1a73e8>作者：</font>** Sofia Torres, Gabriel Almeida, Carter Adams 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become the dominant paradigm for eliciting multi-step reasoning in large language models, and a recent wave of methods (LUFFY, ExPO, PAPO, TAPO) further augments RL with \emph{external guidance} - expert traces, self-explanations, or retrieved thought patterns. Although each method reports empirical gains, none provides convergence rates, bias bounds, or an optimal weighting rule for the guidance signal. We close this gap with \emph{Guidance-Augmented GRPO} (GA-GRPO), a unified theoretical framework that casts external guidance as a stochastic guidance operator G re-writing the question distribution, and analyses the resulting policy-gradient estimator as a biased on-policy estimator whose bias is bounded by the total-variation guidance divergence delta\_G between the guidance-augmented sampling distribution and the policy's own distribution. The framework subsumes vanilla GRPO, LUFFY, ExPO, PAPO, and TAPO as special cases obtained by particular choices of G. Under smoothness and bounded-divergence assumptions we prove that GA-GRPO converges at rate O(1/sqrt(T)) to an O(delta sqrt(T))-neighbourhood of the GRPO stationary point, derive the closed-form MSE-optimal guidance weight lambda-star(T, delta, sigma\_0 squared) = sigma\_0 squared / (sigma\_0 squared + R\_max squared delta squared T), and prove a matching minimax lower bound showing the Omega(delta squared T) bias term is unavoidable. Experiments on Qwen2.5-Math-7B-Base across nine math and OOD benchmarks confirm that optimal-weight GA-GRPO matches or surpasses TAPO, LUFFY, ExPO, and vanilla GRPO while requiring 31\% fewer GPU-hours, and eight analysis experiments validate each theoretical prediction.

---


### 2. [Zero-Shot Visualization: Exploring Text Corpora with User-Prompted Axes](https://arxiv.org/abs/2610.06889)

**<font color=#1a73e8>作者：</font>** Arnau Bueno Tricas, Jose A. Rodríguez-Serrano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study the application of large language models (LLMs) to the visual exploration of textual corpora. We introduce zero-shot visualization (ZSV), a task in which users specify concepts in natural language and documents are mapped onto the corresponding concept axes for visualization. Building a ZSV system of practical value is non-trivial, as it requires choices at the intersection of feature functions, efficient implementation tradeoffs, and pre/post-processing decisions affecting visualization quality. To that end, we establish a benchmark that compares methods spanning embedding similarity, direct semantic judgments, and conditional likelihood estimation in this setting. Across multiple datasets and use cases we evaluate the properties of different scoring methods and design choices in terms of semantic faithfulness, score fidelity, and computational cost. Our results identify that scoring based on next-token probabilities offers the strongest practical trade-off among the evaluated methods. We further apply this approach to unlabeled corpora to examine its behavior in realistic exploratory settings. These experiments highlight additional design considerations, including the use of graded axes together with binary relevance filtering, and reveal a compositional sentiment bias in off-topic documents. Based on these findings, we provide practical guidelines for constructing end-to-end ZSV baselines.

---


### 3. [Medical Image Alignment Assessment as a Test of Generalist Visual Reasoning in Frontier Multimodal Models](https://arxiv.org/abs/2610.06896)

**<font color=#1a73e8>作者：</font>** Ross Callaghan, Niannu Gao, Hojjat Azadbakht 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frontier multimodal large language models (MLLMs) are increasingly positioned as general purpose visual reasoners as part of the quest for artificial general intelligence. A key test of this generality is whether they can perform novel visual judgments that humans can make reliably from visual evidence and task instructions, without task-specific parameter optimisation. We investigate this question through the task of medical image alignment assessment, where the goal is to establish whether there is anatomical correspondence between two images. Human visual assessment of image alignment is still the gold standard and most common approach; however, it requires trained operators and is impractical to scale for large datasets. We evaluate recent generations of MLLMs on two exemplar medical image alignment tasks, varying both prompting strategies and image-presentation methods. We compare against a locally fine-tuned MLLM and a task-specific CNN to examine the trade-off between frontier general purpose models and smaller models that require specific task optimisation but can be used locally. We show that are reaching an inflection point, where frontier MLLMs can now perform effective visual assessment of medical image alignment. Models released only a few months ago generalise poorly and, in some settings, perform barely above chance, whereas GPT-6 achieves over 85% across almost all scenarios tested. Fine-tuned local models can match or exceed frontier-model performance on the tasks on which they are trained, but transfer substantially less effectively to unseen settings. These findings identify medical image alignment as a useful test bed for generalist visual reasoning and suggest that frontier multimodal models are beginning to acquire capabilities that could support a common quality-control mechanism across heterogeneous medical-imaging pipelines.

---


### 4. [Capacity, Responsiveness and Alignment: What Makes a Latent Structure Actionable](https://arxiv.org/abs/2610.06897)

**<font color=#1a73e8>作者：</font>** Or Shafran, Mor Geva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Localizing latent structures in the activation space of language models (LMs) is central to understanding and controlling their behavior. Yet, localized structures can differ substantially in their causal influence, raising the question of what makes a structure actionable. We tackle this question by casting causal influence as a product of three factors and showing empirically that they act as interpretable, distinct constraints: capacity, measuring the sensitivity of the model's output to movement along the structure, responsiveness, capturing how promotable the concept is given the current context, and alignment, reflecting how well the structure aligns with the context-specific representation of the concept. Across 4 LM families and 50 concepts, we observe that causal effectiveness requires all factors to be high; low capacity and responsiveness reduce it by 84% and 95%, respectively, while low alignment can reverse it, suppressing concept expression. Moreover, we find that causality is context-dependent rather than an intrinsic property of the structure, with causally effective directions forming a low-dimensional subspace that varies across contexts. By restricting the training of linear probes to this subspace, we introduce causal probes that achieve 17%-118% improvement in steering across models, with only 3% reduction in concept detection.

---


### 5. [Tree Navigation Without LLM Summaries: A Matched-Cost Study of Hierarchical Retrieval for Long-Document QA](https://arxiv.org/abs/2610.06902)

**<font color=#1a73e8>作者：</font>** Priyank Jayraj, Poonam Goyal, Navneet Goyal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation grounds language models in external context, but for long documents flat top-$k$ retrieval can cluster on a single region and miss complementary evidence. RAPTOR-style summary trees address this by recursively clustering chunks and using a language model to summarize each cluster at indexing time, then ranking summary nodes alongside raw chunks at query time. We show the main benefit of summary trees in long-document QA can come from navigation rather than the generated summary content. We introduce NavTree, a leaves-only retriever that builds a deterministic balanced segment tree over chunks (zero language-model calls at indexing) and uses the tree purely as a navigation scaffold: a hybrid lexical-and-dense frontier walk, anchored on top retrieved leaves, descends from the root and emits only leaf chunks to the reader. On a matched-cost evaluation against flat retrievers and an extractive re-implementation of RAPTOR, NavTree is the strongest matched-cost hierarchical retriever in our evaluated grid and ties the strongest flat baseline. On long-document multi-hop QA, it is the only hierarchical method that significantly beats BM25 on a class-vs-class basis, corroborated by a reader-free retrieval-recall check. A matched-reader replication of the published abstractive RAPTOR variant, given strong cluster summaries, still loses to NavTree at every multi-chunk budget, at zero indexing cost. The ranking carries across stronger and open-weight readers, a stronger encoder, and a full factorial that isolates leaves-only emission as the structural lever.

---


### 6. [Component and Dimension Sparsity in Transformer Refusal Mechanisms](https://arxiv.org/abs/2610.06903)

**<font color=#1a73e8>作者：</font>** Vincent Siu, Glenn Grant-Richards, Vlad Pavlovich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering manipulates large language model behavior by intervening on internal activations, but the mechanistic basis of these interventions remains poorly understood. We decompose refusal steering into component-level interventions across four open-weight models, identifying the sparse subsets of attention and MLP components whose steering suffices to reproduce the full behavioral effect. We find that refusal directions concentrate in sparse component mechanisms comprising 28--48\% of upstream components, retaining 88--101\% of steering effectiveness. Within these mechanisms, effective steering further concentrates in approximately 50\% of residual stream dimensions, retaining 85--98\% of the component-mechanism baseline, consistent with a privileged basis structure. Sparsity thus operates at two levels: which components are steered, and which dimensions within those components carry the signal. Together these findings show that refusal is not diffusely encoded across a transformer but assembled by a structured, identifiable mechanism, providing a foundation for mechanistic understanding of how refusal behaviors are represented and steered. To facilitate reproducibility, we release all code and raw experimental results in this https URL.

---


### 7. [GAMEGO: Training Game-Dev Agents with Synthetic Trajectories Anchored in Real-World Assets](https://arxiv.org/abs/2610.06910)

**<font color=#1a73e8>作者：</font>** Haoyue Yang, Jingyao Li, Zhengfan Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have demonstrated remarkable capabilities in web front-end execution, with browser-based game generation emerging as a particularly prominent frontier. While previous efforts frequently rely on complex multi-turn workflows or focus on static game evaluation benchmarks, this work targets direct end-to-end real-world game synthesis driven by coding agents. However, generating complex games directly from sparse user queries often forces coding agents to make underspecified assumptions, yielding incomplete mechanics, disconnected gameplay flows, and limited visual aesthetics. To resolve this issue, this paper presents GameGo, a scalable framework that systematically transforms brief game seeds into comprehensive Product Requirements Documents grounded in industry game-development practices. To retain core gameplay constraints without restricting design exploration, GameGo uses task-specific dynamic compression to maximize information density while preserving instruction following. Based on this pipeline, GameGoData is constructed with 55,060 development trajectories across 2D, 2.5D, and 3D games, alongside GameGoBench, a benchmark comprising 124 diverse game queries. Training GameGoCoder on GameGoData yields a model that outperforms matched baselines and is comparable to frontier models across gamedev benchmarks. All code, datasets, and models will be made publicly available.

---


### 8. [FluidPD: In-Place Elasticity for SLO-Aware Prefill-Decode Disaggregated LLM Serving](https://arxiv.org/abs/2610.06917)

**<font color=#1a73e8>作者：</font>** Kartik Ramesh, Kaidi Fu, Zihan Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prefill-decode disaggregation is becoming a common architecture for LLM serving because it separates two phases with distinct execution patterns and SLO objectives. Existing systems typically combine a fixed prefill/decode worker ratio with request routing across workers. However, real-world workloads exhibit both short bursts and sustained shifts in the prefill-to-decode demand ratio. As a result, a configuration that is well provisioned at one time may quickly become mismatched, causing latency SLO violations even when idle capacity exists elsewhere. Existing autoscaling mechanisms can add capacity, but they react slowly, require spare GPUs, and do not directly address short-timescale phase imbalance.
We present FluidPD, a P/D-disaggregated serving system that provides SLO-aware in-place elasticity. FluidPD introduces two complementary mechanisms. FluidToken handles transient imbalance by offloading a bounded portion of prefill computation to decode workers when decode-side slack is available. FluidRole handles sustained imbalance by reassigning running workers between prefill and decode roles in place, avoiding model reload and engine restart. Both mechanisms are guided by lightweight pressure indices that expose prefill and decode-side resource pressure before they appear as SLO violations. Across production Azure trace workloads, FluidPD improves overall SLO attainment over static SGLang by up to 94.6 percentage points, demonstrating that SLO-aware in-place P/D elasticity improves service quality without provisioning additional workers.

---


### 9. [RadOnc-Agent: An LLM-Orchestrated Framework for AI Workflows Across the Radiotherapy Care Pathway](https://arxiv.org/abs/2610.06923)

**<font color=#1a73e8>作者：</font>** Caiwen Jiang, Shuoyang Wei, Songlin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence has advanced individual radiotherapy tasks, yet these capabilities remain separated across clinical stages, software environments and data modalities. This fragmentation contrasts with the longitudinal radiotherapy workflow from treatment decision-making through follow-up. Here we present RadOnc-Agent, an agentic artificial-intelligence framework that formalizes radiotherapy into four clinical phases and provides 26 callable functions through a conversational interface. A large-language-model controller maps clinical intent to schema-constrained calls, preserves patient and workflow context, and routes requests to specialist services. We evaluated system execution using 2,600 single-function requests (7,800 repeat executions), 200 prespecified synthetic cross-stage scenarios spanning four phases (600 executions), and 120 workflow instances from 60 de-identified patient records (360 clean executions) representing decision-to-planning and planning-to-adaptation. RadOnc-Agent selected the intended function in 98.79% of single-function executions, completed 96.50% of scripted cross-stage workflows, and completed 96.67% of real-patient workflow executions. In comparative ablations, removing longitudinal state reduced cross-stage completion from 96.50% to 84.00%, while disabling schema and identity validation increased mismatched backend dispatch from 0% to 95.28% in a replay/test evaluation. These findings establish the technical feasibility of an LLM-orchestrated architecture for coordinating heterogeneous radiotherapy capabilities and information across longitudinal workflows; they do not establish clinical correctness, clinical utility or prospective benefit.

---


### 10. [AttSVD:Prompt-Adaptive Low-Rank KV Cache Compression via Attention-Guided SVD](https://arxiv.org/abs/2610.06927)

**<font color=#1a73e8>作者：</font>** Sara Abdali, Jongwoo Ko, Pashmina Cameron  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache of autoregressive transformers grows linearly with context length and dominates memory at long context. Most training-free remedies evict low-importance tokens, an irreversible choice along the sequence axis. We instead keep every token and store it more cheaply along the "feature" axis. We therefore propose AttSVD, a new "interpretable" low-rank compression whose basis is derived from each prompt's own attention geometry: an online, per-prompt truncated SVD that keeps only the directions attention actually reads, cutting persistent per-head KV memory in proportion to the retained rank. We propose two decode-time caching strategies, accumulating and streaming, for short and long generation regimes. Furthermore, we propose two refinements that make compression adaptive. A per-matrix energy rule sizes the logit space and the attention mass independently. An attention-aware basis truncates only in the spaces attention actually reads, preserving both the attention logits and the attention output. The same factors also provide free, per-head interpretability insights into the effective rank and the geometry attention consumes. Across multiple models, on both an agentic benchmark and the full LongBench suite AttSVD stays on par with the dense cache while using up to 50% of the KV-cache memory.

---


### 11. [RADC: Risk-Aware Dual Caching for Vision-Language Test-Time Adaptation](https://arxiv.org/abs/2610.06932)

**<font color=#1a73e8>作者：</font>** Siyu Huang, Yueyong Chen, Xuejiao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cache-based test-time adaptation (TTA) for vision-language models is often hindered by background bias in global representations and unreliable entropy-based cache admission under representation variations. To address these limitations, we propose RADC, which enhances prototype learning through reliable dual caching. RADC introduces a Semantic Foreground Cache that aggregates category-consistent spatial evidence from CLIP representations, yielding foreground prototypes that complement the global cache while mitigating background interference. To reliably manage both caches, Gaussian Risk Admission models multi-view representations as diagonal Gaussian distributions and jointly considers class separation and feature uncertainty to prioritize reliable cache candidates. RADC integrates zero-shot logits with complementary global- and foreground-cache predictions for robust inference. Extensive experiments on cross-domain and out-of-distribution benchmarks demonstrate consistent state-of-the-art performance.

---


### 12. [Stabilizing language models under continual learning via condition-anchored distillation](https://arxiv.org/abs/2610.06940)

**<font color=#1a73e8>作者：</font>** Huan Li, Zhe Cao, Qinlei Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual adaptation of language models can change their output distribution on prompts learned earlier, while retaining every old prompt-answer pair may be undesirable or impossible. We study condition-anchored generative distillation (CAGD): retain a small set of old prompts, use a frozen previous model to reconstruct completions and generation states, and match its predictive distributions while learning the next task. The formulation separates three roles that ordinary replay conflates: conditions select the behavior to protect, teacher generations locate relevant states, and soft targets specify how predictions may change. For autoregressive language generation, teacher-rollout distillation admits an exact chain-rule decomposition of sequence divergence. For masked-diffusion language modeling, our implementation directly controls local denoising drift on teacher-generated completions. In continual adaptation of a 219M masked diffusion language model, CAGD reduces four-task final held-out loss from 2.927 to 1.114 in one task order and from 2.168 to 0.891 in exact reverse. The same soft targets lower final average loss by 0.055 over hard replay when teacher-generated support is held identical. The direction persists on fresh facts and natural instructions across SMDM and Qwen3. On GSM8K, Qwen adaptation preserves answer-format compliance, but exact-match retention is seed-mixed at 0.6B and worsens at 1.7B. These results support condition-anchored functional preservation as a common design principle across the tested language-generation objectives.

---


### 13. [Learning to Decide, Not to Reason: Parameter-Efficient Decision Operators via Low-Rank Activation Steering](https://arxiv.org/abs/2610.06950)

**<font color=#1a73e8>作者：</font>** Ran Li, Lei Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Injecting skills into a frozen language model currently costs a million parameters and a reinforcement-learning pipeline. We introduce \method{}, a System-1 decision operator trained by behavior cloning that lowers this cost by roughly two orders of magnitude. The default operator uses 330K parameters to match a 1.33M-parameter operator trained with reinforcement learning, exceeds or achieve comparable performance, while collapsing 3,685-token deliberation into a 6-token decision with no loss in accuracy. A rank-4 variant with 23K parameters, 1/58 of the strongest published skill operator, suffices for SearchQA and near-suffices for LiveMath, where higher rank still helps; the same recipe transfers across five tasks and three backbones, with out-of-distribution gains persisting on LiveMath problems released months after training. The gap to prior work is trainability, and it is set jointly by initialization and architecture: the initialization of prior operators zeroes the gradient of both large factor matrices at the first optimization step, whereas our zero-initialized output projection inside a shared low-rank backbone receives a gradient immediately, which a gradient-flow probe confirms directly. The gain isn't chain-of-thought compression: 23 of 57 LiveMath points beat the base model's best-of-8 sampling, and a logit-lens probe shows the operator amplifies the answer along the model's existing late-layer pathway, not writing it earlier. Gains track the base model's headroom across 13 base--task pairs, and skills compose as approximately linear operators that can be added, interpolated, and hot-swapped at inference time. Code on this https URL.

---


### 14. [EMODE: Dynamic Para-Semantic Experts for Emotion-Aware Speech Language Modeling](https://arxiv.org/abs/2610.06956)

**<font color=#1a73e8>作者：</font>** Jianan Pan, Yiwen Gu, Xinze Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large speech language models have demonstrated strong capabilities in unified cross-modal understanding and generation, yet paralinguistic cues, especially emotion, remain difficult to preserve. Existing systems typically rely on entangled acoustic representations, which allow the underlying language model to depend excessively on recovered lexical content instead of grounding its behavior in acoustic-prosodic evidence. We address this limitation with EMODE, an emotion-aware speech language model built around \textbf{Dynamic Para-Semantic Experts (DPSE)}. DPSE decomposes continuous speech features into semantic and paralinguistic pathways, routes them dynamically, and fuses them before integration into the language model. To turn this structural decomposition into functional specialization, EMODE is trained with a three-stage curriculum consisting of semantic warm-up, paralinguistic activation, and joint refinement, guided by Orthogonal Expert Guidance (OEG), Semantic-to-Acoustic Alignment (SAA), and Gating Diversity Regularization (GDR). Experiments on SER test, empathetic response evaluation, and the newly constructed bilingual MEPA benchmark show that EMODE improves the balance between lexical fidelity and emotional sensitivity, strengthens affect-grounded response generation, and exposes the value of explicit para-semantic factorization for robust cross-corpus emotion understanding.

---


### 15. [Verdicts Without Annotated Evidence: Rejection Sampling or Label-Only Post-Training for Evidence Recovery?](https://arxiv.org/abs/2610.06962)

**<font color=#1a73e8>作者：</font>** Nishanth Nayakanti, Prasang Gupta, Ashutosh Bilthare 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In many review workflows the verdict is the only thing retained. The passages behind it are not marked, because that annotation costs far more than recording the decision. We measure how much of that evidence a small language model can recover when it is post-trained on the verdicts alone, with no human evidence labels at any stage. On ContractNLI the human evidence spans are held out until evaluation. Matching the recorded verdict and agreeing with those spans are not the same thing: across six systems the two scores are only weakly related and rank the systems differently, so accuracy is a poor guide when the citations have to be reviewable. Label-only training on the bare verdict reaches accuracy 0.896 and span F1 0.564. Rejection sampling, which keeps a generated trace only when its verdict matches the record and then picks one by an automatic source-grounding score, reaches 0.797 and 0.556, against 0.747 and 0.493 before training. Verbatim citation rises from 0.597 to 0.729 under label-only training and to 0.701 under rejection sampling. One seed on one corpus cannot say which method is better, but both improve the evidence without anyone annotating it.

---


### 16. [WavePrune: One period is often enough for RoPE](https://arxiv.org/abs/2610.06963)

**<font color=#1a73e8>作者：</font>** Guancheng Du, Luotian Huang, Shaowen Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rotary Position Embedding (RoPE) encodes token positions by rotating each two-dimensional channel of the query and key vectors at a channel-specific frequency, making the attention logits invariant to a common shift of positions. However, this rotation is periodic, and it leads to position aliasing where relative positions separated by a full rotation period become hard to tell apart. To address this, we propose WavePrune, which restricts each channel to its first rotation period. We show that it removes the distractions in attention maps created by position aliasing and improves overall long-context performance. Specifically, WavePrune raises the HELMET score on four of five models we test without any extra tuning (e.g., 35.7 -> 40.0 on Qwen3-8B). When pretraining models from scratch, WavePrune also achieves lower validation loss at extrapolated lengths than pretraining without it. Because WavePrune restricts each channel to a sliding window, it induces a fine-grained sparsity that our hardware-aligned CUDA kernels exploit for 1.15x prefill and 1.24x decoding speedups over FlashAttention-2 at 32K context. Together, these results show that RoPE's periodic structure, widely regarded as essential, is largely redundant beyond the first rotation period.

---


### 17. [Principles that Guide, Actions that Inform: Agent Evolution via Knowledge Abstraction](https://arxiv.org/abs/2610.06964)

**<font color=#1a73e8>作者：</font>** Bowen Ye, Yongchao Xu, Junkai Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have demonstrated strong capabilities in interactive environments, yet their ability to continually evolve from experience remains limited. Although fine-tuning enables adaptation, its dependence on parameter access and high computational costs restrict its flexibility, especially for large-scale and closed-source LLMs. External memory offers an alternative by allowing agents to accumulate experience without modifying model parameters. However, existing methods mainly focus on experience representation and organization, while the acquired knowledge remains tightly coupled with specific tasks and contexts, limiting generalization. A key challenge is how to transform concrete interactions into abstract and reusable knowledge that guides future decisions beyond individual experiences.
To address this challenge, we propose SAGA (\underline{\textbf{S}}elf-evolving \underline{\textbf{A}}gents through Experience-\underline{\textbf{G}}rounded \underline{\textbf{A}}bstraction), a framework for experience-grounded knowledge abstraction and utilization in LLM agents. SAGA progressively transforms interaction trajectories into episodic descriptions, reusable procedures, and principles with explicit applicability conditions, while maintaining links to execution evidence. Retrieved principles are instantiated into task-specific guidance and used to refine candidate actions through corrective feedback and resampling. This creates an execution--abstraction feedback loop, where accumulated knowledge guides future interactions and new experiences continuously update hierarchical memory. Experiments on ScienceWorld and ALFWorld demonstrate improved task performance, with ablation studies highlighting the importance of contextual instantiation and action regulation for leveraging principle-level knowledge.

---


### 18. [APEX: Active Protection at Execution Boundaries for LLM Agents](https://arxiv.org/abs/2610.06966)

**<font color=#1a73e8>作者：</font>** Xinran Zheng, Xin Fan Guo, Zhiqiang Hao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection (IPI) hides adversarial instructions in content that large language model (LLM) agents read at runtime. As agents compose heterogeneous capability units, including Tools, MCP servers, and Skills, the carriers of injection multiply, and defenses built to recognize attack patterns fall behind them. We instead shift defense from covering attack patterns to one stable point: whatever the carrier and however the injection propagates, harm materializes only at the \emph{execution boundary}, where the agent turns internal state into an external action or released output. Safety there turns on two conditions, both settled by the trusted task rather than by the run: whether the proposed effect is authorized, and whether the runtime information reaching it is endorsed by that task. We present APEX, an active defense that enforces both at this boundary from a single authorization contract compiled before untrusted execution: \emph{evidence-gated prevention} admits an effect only when the contract justifies it, while \emph{deception-based exposure} makes unendorsed use reveal itself before the effect commits. Protection therefore follows from what the task permits rather than from how an attack is built, and applies uniformly across capability units without attack-specific policies or taint tracking. Against 13 baselines, APEX attains 0\% attack success on five of six benchmarks and 0.56\% on the sixth, holds 0\% under adaptive attacks on all three capability-unit types, and remains effective across defender backbones. Code is available at this https URL.

---


### 19. [AegisFlow: A Multi-Agent Agentic AI Framework for Autonomous Remediation and Self-Healing in Fragile Data Ecosystems](https://arxiv.org/abs/2610.06971)

**<font color=#1a73e8>作者：</font>** Muhammad Bilal Awan, Zubair Hussain, Abdul Shahid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional data pipelines are notoriously brittle, often failing due to upstream schema drift, API contract changes, or website DOM modifications. Present observability tools only raise alerts but for human engineers, resulting in a high Mean Time to Repair (MTTR) and operational fatigue. In this paper we propose AegisFlow (Agentic Engine for Intelligent Self-healing and Graph-driven Operations for Workload remediation), a novel agentic framework that closes the loop between detection and resolution. AegisFlow uses a Watchdog agent to collect runtime telemetry and has a Repair agent to automatically create, test and deploy code patches based on Large Language Models (LLMs). The framework presents the non-intrusive execution model called Parallel Shadow Patching, a non-intrusive execution model based on the Monitor, Analyze, Plan, Execute, Knowledge (MAPE-K) loop to generate and verify patches in digital twin environments. Through experimental testing, we have evaluated AegisFlow across five common failure scenarios, and see 98.1 percent improvement in MTTR (from an average of 170 minutes per patch to 3.2 minutes) and a patch success rate of 92 percent . In particular, the system is successful in dealing with changes in the JSON schema (96 percent ) and punctuation drift (98 percent ), and is least successful in Shadow DOM cases (85 percent ). AegisFlow frees up about 98 percent of data engineering on-call time from firefighting and reallocates it towards innovation. The framework is deployment agnostic consisting of a system that can be deployed in a plugin fashion into an existing pipeline orchestration system with minimal uplift to the existing system.

---


### 20. [BoT-Feedback: Grounding Multimodal Reasoning in Biomechanical Evidence for Explainable Human Action Feedback](https://arxiv.org/abs/2610.06972)

**<font color=#1a73e8>作者：</font>** Xu Dong, Wanqing Li, Anthony Adeyemi-Ejeye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in visual understanding and multimodal reasoning, yet they remain fundamentally limited in Human Action Feedback Generation. Existing methods infer coaching feedback directly from visual observations, producing generic advice, limited interpretability, and physically implausible hallucinations. In contrast, expert human coaches diagnose performance through explicit biomechanical reasoning over joint kinematics, posture, and body dynamics. We introduce BoT-Feedback, a framework that grounds MLLM reasoning in structured biomechanical evidence. Our key contribution is Biomechanics of Thought (BoT), a four-stage reasoning framework that progressively identifies the action, localises the critical body regions, analyses quantitative biomechanical differences between expert and student performances, and synthesises interpretable coaching feedback. To support this reasoning process, we develop a plug-and-play Biomechanical Data Parser (BDP) that converts videos into structured biomechanical descriptors and an alignment strategy that temporally matches expert and student motions. We further introduce BiomAF, a benchmark containing paired teacher-student videos, 3D skeletons, biomechanical attributes, and expert-coaching annotations. Experiments across twelve open- and closed-source MLLMs demonstrate that grounding reasoning in biomechanical evidence consistently improves feedback quality, interpretability, and robustness while substantially reducing biomechanical hallucinations. BoT-Feedback improves the average expert evaluation score from 2.07 to 2.95 (+40%), enabling compact open-source MLLMs to approach the performance of substantially larger proprietary systems for explainable action feedback generation.

---


### 21. [Visual-Invariance-Augmented Feature Optimal Alignment for Transferable Adversarial Attacks against Closed-Source MLLMs](https://arxiv.org/abs/2610.06977)

**<font color=#1a73e8>作者：</font>** Xiaojun Jia, Simeng Qin, Yiming Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) remain vulnerable to transferable adversarial examples, especially in black-box settings where only open-source surrogate models are accessible. Existing targeted transfer attacks mainly align adversarial and target samples using global image-level features, such as encoder [CLS] embeddings. However, such coarse alignment insufficiently exploits patch-level visual structures, limiting transferability across heterogeneous closed-source MLLMs. We propose IAU-FOA, a visual-invariance-augmented feature optimal alignment attack with adaptive unbalanced transport, to improve targeted transferability against closed-source MLLMs. IAU-FOA aligns adversarial and target samples at both global and local levels: a cosine-based objective narrows their global semantic gap, while patch tokens are clustered into compact local patterns and matched through optimal transport for fine-grained feature alignment. Balanced optimal transport enforces fixed marginal masses even for local clusters without reliable counterparts, potentially introducing misleading alignment gradients. We therefore introduce confidence-adaptive unbalanced transport to relax these constraints for weakly matched clusters, aiming to reduce unreliable local alignment and improve adversarial transferability. We further study the effect of input transformations and propose visual-invariance augmentation, which applies bidirectional pixel-intensity rescaling and per-channel white-balance adjustment to simulate exposure, contrast, illumination, and color-temperature variations. This strategy encourages adversarial perturbations to generalize across different visual encoders. Extensive experiments on open-source and closed-source MLLMs show that IAU-FOA consistently outperforms state-of-the-art transferable attack methods. Code is available at this https URL.

---


### 22. [A Data-Driven Framework for Unsupervised Monitoring of Transmission Systems Using End-of-Line Testing Data: A Case Study at Ford Motor Company](https://arxiv.org/abs/2610.06980)

**<font color=#1a73e8>作者：</font>** Mohammad N. Bisheh, Mehrdad Moradi, Parinaz Farajiparvar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sensing technologies have advanced rapidly across industries ranging from energy to automotive manufacturing. These systems generate high-dimensional (HD) data characterized by complex nonlinear patterns and strong temporal dependencies. Traditional statistical monitoring methods are often limited in their ability to capture such nonlinear structure. Likewise, many analytical approaches used in End-of-Line testing rely on predefined thresholds and heuristic rules, which restrict their ability to detect informative anomaly signatures in HD temporal data. In contrast, while modern deep learning and generative AI models offer strong predictive capabilities, they are often unsuitable in applications where data are costly to collect and where the monitoring system must remain interpretable, low-latency, computationally efficient, and usable by non-technical practitioners. To overcome these limitations, we propose an advanced multivariate monitoring framework for HD data. The framework operates in two stages. In the first stage, the data are preprocessed to remove incomplete and non-informative samples and to temporally align time series data. In the second stage, nonlinear dimensionality reduction is performed, followed by anomaly detection through a control chart based phase I monitoring procedure. The framework can be used in both unsupervised and supervised settings, depending on the availability of ground truth labels during training. Moreover, its flexible and modular structure allows practitioners to adapt its components to different domains and operational requirements. We evaluate the proposed framework on real production data from an automotive manufacturing environment at Ford Motor Company. The proposed method achieves higher accuracy, recall, and F1 score than the company's existing model, improving these metrics from 0.50, 0.30, and 0.429 to 0.625, 1.00, and 0.769, respectively.

---


### 23. [DART-ES: Difficulty-Aware Reweighting and Targeted Replay for Fine-Tuning LLMs with Evolution Strategies](https://arxiv.org/abs/2610.06993)

**<font color=#1a73e8>作者：</font>** Zhishen Sun, Hongzhan Wang, Sizhe Dang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evolution Strategies (ES) enable memory efficient full parameter fine-tuning of large language models (LLMs) using only forward computation. However, standard ES uniformly averages rewards across problems and compresses problem level population feedback into a single scalar, making it difficult to capture how the learning value of each problem changes with model capability. To address this limitation, we propose Difficulty-Aware Reweighting and Targeted Replay for Evolution Strategies (DART-ES). DART-ES estimates the local solvability of each problem from its pass rate across the perturbation population and aggregates historical observations to construct a dynamic difficulty state. This shared state jointly guides continuous difficulty reweighting and rare solvable sample replay, thereby improving perturbation direction evaluation and training data allocation without introducing an additional difficulty model or backpropagation. Extensive experiments show that DART-ES achieves good fine-tuning performance. DART-ES outperforms ES on all five base models and improves the average accuracy from 72.07\% to 73.53\%, exceeding the 73.26\% achieved by GRPO on GSM8K. Across five challenging mathematical reasoning benchmarks, DART-ES achieves an average accuracy of 49.20\%, compared with 48.34\% for ES and remains competitive with strong 7B models trained with RL. Further experiments show consistent gains in instruction tuning, code generation and the Countdown task with a 14B model, demonstrating strong generalization across tasks and scalability to larger models. Beyond performance gains, DART-ES also shows clear advantages in system efficiency. It reduces runtime per step by 15.2\%--50.2\% and peak memory usage per GPU by 21.1\%--51.1\% compared with GRPO. Despite performing full parameter fine-tuning, DART-ES also requires less runtime and GPU memory than GRPO+LoRA.

---


### 24. [Mask-Guided KV Cache Eviction in Block Diffusion Language Models](https://arxiv.org/abs/2610.06996)

**<font color=#1a73e8>作者：</font>** Gleb Molodtsov, Ekaterina Alimaskina, Evgeny Uskov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block diffusion language models keep a large key-value (KV) cache throughout generation and attend to it at every denoising step, limiting both memory capacity and generation speed. Reducing these costs requires deciding which past tokens to use for denoising the current block (selection) and which to keep in memory for future blocks (eviction). We propose MaskAhead, a training-free method that solves both tasks with a single mask-query-based ranking mechanism. Current-block masks guide selection, while probes of upcoming masked blocks guide eviction. Both rank KV entries by their estimated contribution to the attention output. Our quantized variant, Q-MaskAhead, computes selection and attention directly from low-bit KV, largely preserving the selected entries. Experiments on Fast-dLLM-v2, DreamReasoner, and LLaDA2.0-mini cover long-generation reasoning, long-prompt question answering, and needle-in-a-haystack retrieval. On long-prompt QA, MaskAhead reduces KV memory by $9.5\times$ on average with a 1.2-point mean F1 loss relative to dense inference. Q-MaskAhead increases the reduction to $20.1\times$ with a 2.3-point mean F1 loss. In a batch-32 systems profile, MaskAhead achieves $1.23\times$ end-to-end and $1.68\times$ decode-stage speedups over dense inference.

---


### 25. [Topology-Consistent Task Planning over Cellular Workflow Complexes for LLM-based Agents](https://arxiv.org/abs/2610.07004)

**<font color=#1a73e8>作者：</font>** Sen Zhao, Jia Tang, Ruiqi Kong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Task planning for LLM agents requires workflows that satisfy both user intent and complex sub-task dependencies. While existing planners work well for sequential or directed acyclic graph (DAG)-like structures, they struggle with workflow patterns such as verification-correction loops, convergent branch merging, and reusable intermediate states that arise naturally in real-world tool orchestration. We present TopoPlanner, a topology-consistent planning framework that lifts tool dependency graphs into cellular workflow complexes and uses them as topologyaware context for LLM tool planning. TopoPlanner retrieves a request-relevant closed subcomplex through cosheaf-consistent cellular retrieval, performs multidimensional structural reasoning over the retrieved topology, and interfaces the resulting cellular representation with the planner LLM for tool-sequence generation. Experiments on four tool-planning benchmarks with topology-guided loop, merge, and loop-merge workflows show consistent improvements over prompt-based and graph-enhanced baselines across different local LLM backbones.

---


### 26. [When to Rethink: Learning Multi-Perspective Self-Verification for Vision-Language Models](https://arxiv.org/abs/2610.07018)

**<font color=#1a73e8>作者：</font>** Ziquan Zhu, Hanruo Zhu, Si-Yuan Lu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved strong performance in multimodal reasoning, yet they remain prone to generating plausible but incorrect answers. Self-verification offers a practical way to improve answer reliability without relying on external judges, but existing methods typically depend on a single verification criterion or fixed prompt, resulting in incomplete and unstable reliability estimates. We first systematically analyze how verifier capability and prompt design affect verification performance. Our findings show that stronger verifiers provide more reliable judgments, while verification performance is highly sensitive to prompt choice, with no single prompt consistently dominating across tasks. Guided by these findings, we propose \texttt{MOTIVE}, a \textbf{M}ulti-View Self-Verificati\textbf{O}n wi\textbf{T}h Rel\textbf{I}ability-Guided Selecti\textbf{VE} Rethinking framework for reliable multimodal reasoning. \texttt{MOTIVE} evaluates each candidate answer from complementary verification perspectives and learns a correctness-aligned reliability score through correctness-grounded multi-view verification learning. During inference, this score governs an accept-or-rethink decision, allowing reliable answers to be returned directly while uncertain ones trigger history-guided rethinking. Extensive experiments across diverse multimodal benchmarks and VLM backbones demonstrate that \texttt{MOTIVE} consistently outperforms strong self-verification and self-correction baselines. Further results show that reliable verification improves accept-or-rethink decisions and reduces unnecessary reasoning turns, enabling more reliable and efficient self-verification without an external judge.

---


### 27. [Calibrated Answers About Randomized Trials From a 4-Billion-Parameter Open Model: A Registered Test and a License-Clean Release](https://arxiv.org/abs/2610.07019)

**<font color=#1a73e8>作者：</font>** Johann Emmanuel Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fiorillo v0.5 is an open model that answers typed questions with a probability for each answer. Its main specialist reads a randomized trial's article, cut to 6,144 tokens, and answers whether an intervention significantly increased, significantly decreased or did not significantly change an outcome against a comparator (Evidence Inference 2.0, EI). It is Qwen3-4B-Base with low-rank adapters and a decision head, fine-tuned for EI only on the 1,431 of 2,657 training articles whose own license allows reuse. Four criteria registered on the Open Science Framework before this version's test predictions decided its release, the second bar judged on EI's test split, whose labels are public. On that split (1,218 prompts in 333 articles), the expected calibration error was 0.0168 against a limit of 0.05; log loss was below the prior's by 0.8603 (95 percent interval 0.8104 to 0.9078) and below that of Gemma 4 31B-it, reading the same input, by 0.1829 (0.1164 to 0.2598); and macro-F1 was 0.9248 against 0.8668, so all four criteria passed. Training the same recipe on clean articles alone cost 0.0123 in accuracy (0.0034 to 0.0207; descriptive). With no article, macro-F1 fell to 0.4384; the title alone raised it by 0.0939 (0.0655 to 0.1234), which a title stating the result or recall of the trial could explain; exchanging intervention and comparator reversed 0.6652 of its direction answers. Run as released, the files matched the evaluated predictions within limits set in advance. The release is under the Apache License 2.0 (digital object identifier https://doi.org/10.57967/hf/10722).

---


### 28. [Offline AI Modules: Voice-First Offline Architecture, Hardware Reference Stack, Quantization and Benchmarking](https://arxiv.org/abs/2610.07026)

**<font color=#1a73e8>作者：</font>** Sunday Afariogun, Odunolaoluwa Jenrola, Zeinab Nezami  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Offline AI Modules workstream enables practical, low-power, and community-accessible deployment of voice-first AI systems that operate fully offline. Designed for African language communities where speech is the dominant mode of interaction and internet connectivity is unreliable or absent, the workstream delivers three reinforcing components: a modular voice-first offline architecture, a low-cost hardware reference bill of materials, and a reproducible quantization and a reproducible quantization and benchmarking pipeline for instruction-tuned language models in the 2-5B parameter class. This paper presents the first end-to-end benchmark evaluation of the stack across two hardware tiers: an NVIDIA Jetson Orin NX (TierB) and a Raspberry Pi5 (TierA). Three instruction-tuned models are evaluated across four quantization formats, assessed for deployment metrics (decode throughput, chat latency, memory, power) and multilingual quality (topic classification accuracy on MasakhaNEWS across English, Hausa, Igbo, Nigerian Pidgin, and Yoruba; per-language perplexity drift). Speech recognition is evaluated using Ethio-ASR on Amharic and Oromo across both tiers. The principal finding is that Q4_K_M quantization represents the best size-to-quality trade-off for deployment on both tiers: gemma-4-E2B-it achieves 28.8t/s decode throughput and 89.2% topic classification accuracy at Q4_K_M on TierB, while all three models run within the 16GB memory budget on TierA.

---


### 29. [Educating future engineers about LLMs: A scalable workshop](https://arxiv.org/abs/2610.07027)

**<font color=#1a73e8>作者：</font>** R. Zhang, J. C. F. de Winter, T. Dicke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly integrated into engineering workflows, students require hands-on experience to learn how to collaborate with them critically. This paper presents a scalable gamified workshop designed for engineering Master's students to practice human-AI collaboration in navigation planning. Using a mobile web interface across 10 workshop sessions, a total of 226 students wrote prompts for a non-reasoning and a reasoning LLM to solve grid-based navigation tasks of increasing complexity. The system returned robot-executable plans, trajectory visualizations, and automated scoring, culminating in a live demonstration on a Boston Dynamics Spot robot. In a post-workshop questionnaire, 81.5% reported substantial learning and 91.0% reported high engagement. Analysis of the submitted prompts revealed that students changed their strategies from step-by-step instructions for the non-reasoning LLM toward providing higher-level guidance for complex problem-solving tasks. We conclude that such interactive simulation-to-reality environments are viable for teaching the verification and collaboration skills necessary for responsible LLM use in engineering. Code is available at: this https URL

---


### 30. [TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning](https://arxiv.org/abs/2610.07043)

**<font color=#1a73e8>作者：</font>** Zhen Li, Shuai Zhang, Yanggan Gu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-precision execution can substantially accelerate reinforcement learning (RL) for large language models, but discrepancies between learner and sampler execution can destabilize policy optimization. In this paper, we characterize the interaction between mismatch and the policy-gradient direction, distinguishing locally amplifying from contracting update contributions that mismatch magnitude alone cannot identify. In native NVFP4 runs, we observe an early imbalance between the two amplifying regions, favoring negative-advantage, negative-gap updates. Their tail tokens become concentrated in a small fraction of response segments before mismatch spreads globally. Motivated by these findings, we introduce TRIAGE, a direction-aware stabilization method that uses segment-level diagnosis to selectively rebalance policy-gradient updates and applies bounded repair to residual severe mismatch. TRIAGE modifies the optimization objective while retaining native NVFP4 weight-and activation 4-bit (W4A4) forward execution on both the sampler and learner. Experiments on Qwen3-4B and Qwen3-30B-A3B show stable optimization throughout the evaluated training horizon and achieve full precision level performance across five mathematical reasoning benchmarks, while native NVFP4 with TRIAGE provides up to 2.3x higher rollout throughput than BF16.

---


### 31. [Learning to Simulate Individuals from Macro Social Signals](https://arxiv.org/abs/2610.07062)

**<font color=#1a73e8>作者：</font>** Yining Zhao, Bushi Liu, Haofei Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to simulate how individuals respond to new situations, yet the behavioral reasoning behind these responses is either inherited from pretraining or learned from individual-level annotations, which offer limited behavioral diversity and little supervision of the reasoning itself. We propose to learn behavioral reasoning from prediction markets, whose price trajectories record how populations respond to real-world events at scale. We introduce macro2mind, which trains a language model with GRPO using market signals. A social behavioral decomposition makes behavioral reasoning an explicit step of forecasting: the model infers representative groups of market participants, predicts how each interprets the news and updates its beliefs, reasons about their interactions, and aggregates these responses into a price. A hindsight-regret curriculum with difficulty-aware sampling focuses training on transitions where hindsight-identified groups substantially improve the forecast while prioritizing examples that remain learnable for the current policy. The learned reasoning applies to user simulation without further training. On SWM-Bench, macro2mind achieves state-of-the-art directional accuracy and correlation on Polymarket. Trained on market data, it transfers zero-shot to four user-simulation benchmarks (Humanual, OvertonBench, PRISM, and CAD) and has competitive performance among zero-shot methods. Used as a data generator, macro2mind also raises a downstream simulator's accuracy on unseen users by 15.5 points, outperforming data generated by its backbone by 13.2 points.

---


### 32. [Turnslide: Scalable Multi-Turn Data Synthesis by Walking a Finite-State Machine](https://arxiv.org/abs/2610.07070)

**<font color=#1a73e8>作者：</font>** Aaron Fainman, Gabriela Kadlecová, Maciej Gryka 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models are inexpensive to serve and can run on private infrastructure, but base models are often not good enough at multi-turn tool calling, and fine-tuning them needs per-API data that rarely exists. Existing synthesis methods are too expensive for high-scale fine-tuning, as they often require mock operational environments for different domains and multiple LLM calls per generated conversation turn. We introduce a fully automated, lightweight synthesis framework that models each API as a finite-state machine, representing the system as abstract states that determine when each tool may be called, producing state-valid sequences of tools; sequences are translated into complete examples with a single LLM call. Rather than optimize diversity, we set a target distribution over the number of turns, the tool sequence and task complexity. We measure data quality by fine-tuning SLMs on generated trajectories, showing that our FSM-based generation significantly improves downstream accuracy over an unmutated baseline and, against existing works, reaches 70.7% full accuracy over 63.4% and 53.7% with 3.6-6.6$\times$ fewer tokens.

---


### 33. [SchemaFill: Efficient LLM Tool Calling via Slot-Parallel Speculative Decoding](https://arxiv.org/abs/2610.07086)

**<font color=#1a73e8>作者：</font>** Zhi-Kai Chen, Song-Yan Li, De-Chuan Zhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents interact with external systems by generating structured tool calls. Given a user request, conversational context, and a catalog of tool schemas, a tool-calling model must select tools and generate their arguments, potentially producing multiple calls in a single response. Standard autoregressive decoding generates these calls token by token, incurring substantial latency for requests involving multiple calls or many argument fields. The explicit argument structure offers opportunities for parallel generation, but later argument values may depend on preceding fields and calls, so independently generated values can differ from the target model's output. We present SchemaFill, a framework for efficient LLM tool calling through slot-parallel speculative decoding. SchemaFill generates future slot values concurrently as candidates, without requiring advance knowledge of the actual call sequence or argument values. Candidates spanning multiple fields and calls are concatenated for verification by the target model under the actual output prefix. Only verified tokens are committed, and the target supplies corrections when candidates disagree. This applies target verification while exploiting parallelism across slots and calls. On Glaive and BFCL, SchemaFill achieves up to a 4.05$\times$ improvement in end-to-end throughput over autoregressive decoding. Code is available at this https URL.

---


### 34. [Towards a Unified Misuse Monitoring Benchmark](https://arxiv.org/abs/2610.07089)

**<font color=#1a73e8>作者：</font>** Aniruddh Pramod, James Oldfield, Adel Bibi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly act in multi-actor environments, exposing them to misuse from multiple sources: decomposition attacks, where a harmful request is split into innocuous sub-requests, and prompt injection attacks, where a compromised tool delivers a malicious instruction. Existing evaluations treat these threats separately and ask whether a trajectory is harmful, rather than when it becomes harmful. We propose monitoring the agent's responses, where its actions are externalised, and ask whether the first point where monitors identify harm lands within a harm window (from the agent's first harmful commitment to goal execution). We develop a unified formalism for trace-level misuse monitoring and use it to construct a benchmark of ~6,200 conversation transcripts between a user, an LLM agent, and the external environment, spanning both threats in a shared schema, with a labelled harm window, corresponding benign controls, and matched instances of refusals to these requests. Across 17 monitor configurations, we find that our proposed action-framed monitors perform well on both threats under classical metrics (AUC: 0.95 and 0.99 respectively), while content-framed monitors collapse on injection attacks (AUC: 0.52). We also show that classical position-blind metrics paint an optimistic picture of monitor performance, since all monitors localise decomposition attacks poorly under the interval metric, which measures the ability to localise harm. Broadly, we illustrate the need for a unified study of misuse monitoring.

---


### 35. [Smart Content Ingestion for Generative AI Workloads](https://arxiv.org/abs/2610.07091)

**<font color=#1a73e8>作者：</font>** Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The evolution of machine learning has progressively changed where intelligence resides in an AI system. In conventional machine learning the task, data representation, labels and model architecture were tightly coupled, so data preparation was narrow, schema-bound and visible. Generative AI decouples the model from any single task: one foundation model serves open-ended downstream tasks, and the generality gained on the model side is matched by heterogeneity on the data side, because enterprise knowledge is authored in the formats people use (PDF, presentations, spreadsheets, scanned documents, forms, tables, diagrams and mixed-layout files) that carry textual, visual, geometric and structural information at once. A language model or retriever cannot reason reliably over information misrepresented at this interface, so content extraction becomes a lifecycle stage in its own right whose errors no downstream retriever or re-ranker can repair. This paper presents a production-ready content-extraction system that makes this stage explicit, configurable, and measurable. The system incorporates selective OCR routing, a scarcity-first curation engine with a reference-based extraction scorer that measures character, word, and table-structure accuracy, a deterministic structure-aware parent-child chunker, and a read-only retrieval evaluator that generates grounded questions from every page and reports Hit@k, mean reciprocal rank, and latency. On a 180-document corpus the best extractor scores 97.4 of 100 (character error rate 0.13%, table similarity 0.995) and the chunker reaches hit@1 of 68.6%, hit@10 of 92.8% and MRR 0.77 over 25,050 generated questions. We distil three design principles (structure before semantics, never mutate what you measure, budget your labels) and position measured content extraction as the perception layer of enterprise agentic systems.

---


### 36. [Small Language Models for Smart Data Model Classification at the Edge: A Cost-Aware Hybrid Approach](https://arxiv.org/abs/2610.07093)

**<font color=#1a73e8>作者：</font>** Cristian Martella, Angelo Martella, Antonella Longo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of heterogeneous data sources within the Internet of Things (IoT) across domains such as smart cities, energy management, and environmental monitoring necessitates efficient and scalable data standardization methods. Effective classification of smart data models (SDMs) is essential for facilitating interoperability. However, existing approaches are often limited by high resource consumption and lack applicability in edge environments with constrained computational capabilities. Aiming to bridge this gap, the proposed study evaluates the performance of lightweight open-source language models (LMs) to resolve an input data entity against its corresponding best fitting SDM representation under resource-constrained conditions. It systematically benchmarks a diverse array of models, including general purpose (GP), reasoning-specialized (RS), and code-specialized (CS) architectures, across multiple domain-specific datasets. Addressing the current omission of lightweight, resource-efficient solutions in the literature, the investigation provides significant and valuable insights into model selection, task formulation, and deployment strategies that optimize accuracy and efficiency. A complementary experiment also compares the surveyed large language models (LLMs) against two near-zero-cost similarity baselines (Term Frequency-Inverse Document Frequency (TF-IDF) and a lightweight sentence encoder) on the same task, providing a strong reference point for interpreting the practical value of LLM-based classification on edge platforms.

---


### 37. [Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course](https://arxiv.org/abs/2610.07097)

**<font color=#1a73e8>作者：</font>** Canh Thien Dang, An Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Experimental studies of generative AI in education mostly report average effects, yet field evidence shows that AI can narrow attainment gaps or widen them. We argue that the direction depends on the judgement burden, the expertise a learner must supply to screen AI output before learning from it, and that expert verification before release moves this burden from students to an accountable tutor. We test the argument in a two-cohort difference-in-differences design in which one half of a compulsory firstyear university economics course received AI-generated podcasts, FAQs and quiz-based study guides, produced with a source-grounded model and checked by a named graduate teaching assistant (170 students; 340 examination marks). Access was associated with a 2.34-mark advantage on a 50-mark component. The share of marks below the upper-second classification boundary fell by 24.7 percentage points relative to the counterfactual, effects were significant at every threshold from 23 to 31 marks and at none above, and roughly three-quarters of the average originated in the bottom quintile. The threshold estimate is robust to removing the lowest-scoring students from the pre-intervention cohort; the average effect is not. Interviews and feedback from 36 students indicate that the verification label gave students a reason to engage with AI-generated material without ending their scrutiny of it. Evaluations of AI learning resources that report only mean effects cannot detect whether the students the resources are meant to help are the ones who gain.

---


### 38. [When to Remember, When to Abstain: Category-Conditioned Retention for Reliable Agent Memory](https://arxiv.org/abs/2610.07100)

**<font color=#1a73e8>作者：</font>** Olukunle Owolabi, Pulkit Gupta, Fei Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent agent memory is only as reliable as its retention decision: an assertion weakly supported by its source can be stored and later reused as established fact. We study whether the retention decision should be governed by a confidence bar conditioned on the semantic category of the assertion rather than by a single global threshold, retaining well-evidenced categories liberally while abstaining more aggressively where inference is unreliable. We evaluate this in a deployed cold-start memory pipeline on 100 synthetic personas. The empirical evaluation is motivated by a sharp reliability asymmetry: across 4{,}715 candidate assertions, only 77.9\% of value and belief assertions are supported by their source, versus 96.2\% for all other categories. A global confidence threshold cannot separate these: it either admits unsupported value claims or discards well-evidenced ones. Conditioning the threshold on category resolves the tradeoff. In repeated held-out evaluation, a stricter bar on values alone reduces unsupported retentions from 6.2\% to 4.0\% (an ${\approx}36\%$ relative reduction, modest but consistent across folds) and, as corroborating evidence, preserves an estimated 13 percentage points more coverage (95\% CI 9.8--16.0) than a global threshold at comparable retention. Our results suggest that reliable retention depends on the type of assertion, not on confidence alone, and that a category-conditioned threshold can act as a simple, effective form of selective prediction at the write boundary.

---


### 39. [JudgeMoE: Distributional Aggregation for LLM-as-a-Judge](https://arxiv.org/abs/2610.07109)

**<font color=#1a73e8>作者：</font>** Yiqi Liu, Joseph James, Yang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When an LLM judge scores an output, its score distribution retains uncertainty and disagreement information that is lost after scalar compression. We introduce JudgeMoE, a lightweight aggregator that assigns example-specific weights to cached judge score distributions and fuses them before computing a final score. A protocol study shows that score-range choice is unstable across judge--dataset settings and that soft scoring usually outperforms hard decoding. On the original 10-cell benchmark, JudgeMoE improves mean Spearman over uniform log pooling by $+0.079$. Applying the same configuration to six additional cells yields a $+0.0393$ mean gain over the strongest local single judge across 16 cells, with positive differences in 12/16 cells and a one-sided Wilcoxon signed-rank $p=0.0091$. Validation-based analyses further show that the preferred aggregation method depends on the task and judge pool.

---


### 40. [Will the Judge Flip? Predicting Position-Sensitive LLM Judgments from Residual Stream Activations](https://arxiv.org/abs/2610.07115)

**<font color=#1a73e8>作者：</font>** Hashmath Shaik, Gnaneswar Villuri, Alex Doboli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The order in which candidate responses are presented can change an LLM judge's verdict. Detecting such a position flip ordinarily requires judging each pair in both orders, which doubles the number of judgments. We investigate whether residual stream activations recorded immediately before the initial verdict can predict a flip. We use nested grouped cross-validation to evaluate regularized linear probes on 534 JudgeBench pairs for three Qwen3 judges and Llama-3.1-8B. The linear probes achieve AUROCs of .621-.850 and outperform a combined baseline that uses verbalized confidence, verdict-label logits, response lengths, and the judge's initial choice by .062-.113 AUROC. Linear probes trained on JudgeBench and then frozen achieve AUROCs of .685-.853 on 1,802 MT-Bench comparisons without MT-Bench fitting or recalibration. These results show that pre-verdict activations support prediction of susceptibility to candidate order and outperform the non-activation predictors evaluated here.

---


### 41. [AMBER: Training Long-Horizon Web Agents through Append-Only Memory](https://arxiv.org/abs/2610.07118)

**<font color=#1a73e8>作者：</font>** Chinmay Savadikar, Zhaoyu Zhang, Mingyu Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern language-model agents increasingly interact with external environments over long-horizon, multi-step trajectories, where the accumulated interaction history can quickly exceed practical context budgets. To ensure reliability, agents must maintain factual information over long horizons, remember execution errors and corrective feedback, and track progress across actions. Several approaches have been proposed to achieve this without the need for maintaining the entire execution history in context, such as using the reasoning and action history, learning to maintain a fixed-size memory through an overwrite mechanism, and periodic summarization. Although overwrite memory can in principle retain anything an append-only memory can, it must learn to carry each fact through every subsequent rewrite, which is difficult to learn from sparse outcome rewards; for interactive applications like web agents, we find that trained overwrite memories delete key information required by the trajectory, as well as corrective feedback received from the environment. We introduce AMBER (Append-only Memory Bank for Evidence Retention) - a simple and scalable framework where an agent jointly learns to reason, act, and write free-form memory, while an append-only rule guarantees retention by construction. This allows AMBER to be trained end-to-end with reinforcement learning from outcome rewards without the need for extensive curated SFT data. On WebArena Lite, AMBER improves average success over overwrite-based memory by 4.09 percentage points, increases the fraction of tasks solved in five repeated runs by 4.8 percentage points, and matches an overwrite baseline trained on substantially more expensive curated supervision. AMBER achieves these improvements while maintaining a practical token budget, providing a strong balance between context efficiency, task performance, and reliable long-horizon execution.

---


### 42. [SoloQ: Calibration-Free Quantization for Diffusion Language Models](https://arxiv.org/abs/2610.07121)

**<font color=#1a73e8>作者：</font>** Donghyun Lee, Arkapravo Ghosh, Varun Manjunath 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models dLLMs) have emerged as a promising alternative to autoregressive language models through bidirectional diffusion-based token generation. However, their growing model sizes and high inference costs make efficient deployment challenging: full-sequence denoising repeatedly invokes compute-intensive forward passes, while block-diffusion models additionally introduce a memory-intensive KV-cache. Low-bit weight-activation quantization is therefore attractive, yet existing dLLM post-training quantization methods rely on calibration data despite activation distributions shifting across masking states and denoising steps. We present SoloQ, a calibration-free quantization framework that maps weights and activations into a normalized rotated basis with a predictable marginal distribution, enabling data-independent quantization. SoloQ combines a structured K-RPBH rotation with a lightweight rescaling correction for calibration-free quantization. Its predictable post-rotation distribution supports both distribution-matched codebooks and hardware-native NVFP4. For block-diffusion models, SoloQ further applies commit-time KV-cache quantization to compress persistent states without perturbing the actively denoised block. Across full-sequence dLLMs (LLaDA and Dream) and block-diffusion dLLMs(Fast-dLLM v2 and Nemotron-Labs-Diffusion), SoloQ retains accuracy under 4-bit quantization and outperforms calibration-based baselines on knowledge- and reasoning-intensive benchmarks. With NVFP4, SoloQ reduces peak memory by up to 2.61X and accelerates end-to-end inference by up to 2.24X.

---


### 43. [Jailbreaking Open-Weight LLMs via Random Embedding Perturbations](https://arxiv.org/abs/2610.07125)

**<font color=#1a73e8>作者：</font>** Abhinav Sudhakar Dubey, Scott Sirri, Vaggos Chatziafratis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While open-weight models have enjoyed steady progress in capabilities and wide adoption across multiple domains, their safety remains an important concern. One key feature is the ability to refuse or deflect harmful, malicious, or insensitive prompts. In this paper, we expose safety vulnerabilities across six common open-weight LLMs of various sizes that consistently lead to harmful or unsafe responses on the JailbreakBench benchmark dataset. Our proposed attack, Perturbed Embedding Vector (PEV), is a simple and fast "jailbreaking" technique that is cheaper than prior approaches, which typically require gradient computations, per-prompt optimizations, or altering internal weights of the models. PEV just adds independent Gaussian noise in the embedding vector representations of the prompt, with no need for further manipulations. To generate unsafe responses, we repeatedly sample additive noise from this distribution. In our experiments, we observe that the average compute cost to get the first successful attack is up to an order of magnitude less than previous attacks. The first successful jailbreak on a new prompt typically arrives within one minute on every tested model, and PEV generates unsafe responses across all models for all prompts in JailbreakBench. No other tested method achieves such results, despite them taking longer to run. More broadly, we believe that understanding the behavior of LLMs under perturbations in the embedding vectors is an important research direction: while perturbations constitute a major security risk, they can also serve as a valuable tool for exploring the dynamical behavior of such models.

---


### 44. [PlaySuite: A Large-Scale Benchmark for Interactive Visual Intelligence](https://arxiv.org/abs/2610.07127)

**<font color=#1a73e8>作者：</font>** Dheeraj Varghese, Anna Vettoruzzo, Walter Simoncini 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal foundation models yield strong performance on static perception and reasoning benchmarks, yet such evaluations largely overlook a central aspect of intelligence: acting competently in dynamic environments over extended time horizons. We introduce PlaySuite, a large-scale benchmark for evaluating interactive visual intelligence across more than 5K open-source video games curated from PyWeek and this http URL. Spanning diverse genres and engines, including Pygame, HTML5, Godot, and Unity, these independent games are largely out-of-distribution for current models, reducing the likelihood that success can be achieved by retrieving memorized walkthroughs or web-scale training artifacts. To enable scalable evaluation across heterogeneous titles, we develop a unified closed-loop interaction framework optimized for HPC clusters alongside a Video-LLM-as-a-judge protocol that maps observable gameplay milestones to standardized progress levels. We evaluate fourteen recent open models spanning vision-language models, computer-use agents, and vision-language-action models. Our results yield strong evidence of a perception-action gap: despite strong reasoning capabilities, current models struggle to make sustained progress and exhibit recurring failures in spatial grounding, action execution, and self-correction. PlaySuite provides a reproducible and extensible testbed for measuring progress from visual perception to goal-directed interaction, and a foundation for developing models that can act, adapt, and generalize in dynamic visual environments.

---


### 45. [CroissantMiner: Automated Extraction and Validation of Croissant Metadata for ML Datasets](https://arxiv.org/abs/2610.07132)

**<font color=#1a73e8>作者：</font>** Berke Arda, Ahmetcan Yavuz, Paul Gerry 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Croissant has emerged as a standard for machine-readable dataset metadata, yet populating its fields remains labor-intensive and requires careful reading of accompanying dataset documentation. We present the first benchmark enabling end-to-end evaluation of metadata extraction aligned with a community-standard schema. The benchmark comprises 602 papers, including 102 with human-validated gold annotations and 500 with LLM-generated silver annotations, covering the full Croissant schema with both core and Responsible AI (RAI) fields. Using this benchmark, we evaluate a range of extraction systems spanning frontier models, open-weight models, and agentic architectures, under a two-tier evaluation framework that combines rule-based scoring with an LLM judge selected via human audit. We find that single-pass extraction consistently outperforms the four agentic architectures we evaluate: across backbones, these decomposed variants achieve lower accuracy than a single full-context pass. The largest gap appears on long-form RAI fields, which require synthesizing and interpreting information scattered across a paper rather than copying it from a single location, a setting where current systems remain far from reliable. We release the benchmark, evaluation code, judge audit, a live demo, and a leaderboard open to new systems.

---


### 46. [A theory of platonic representations in language models](https://arxiv.org/abs/2610.07168)

**<font color=#1a73e8>作者：</font>** Darshil Doshi, Wenjie Zhou, Corinna Elena Wegner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representations of translated sentences are similar in the inner layers of multilingual language models -- an observation connected to the platonic representation hypothesis, yet unexplained theoretically. We provide an explanation based on the assumption that data have a hidden hierarchical structure whose abstract levels are shared across languages while surface levels are modality- or language-specific. Concretely, we generate synthetic languages from probabilistic context-free grammars sharing upper-level but not lower-level production rules. In this setting the Bayes-optimal next-token predictor is belief propagation (BP); encoding its messages in successive layers yields analytical predictions that agree well with transformers trained on the same data. The framework explains why cross-lingual similarity peaks in middle layers, coexists with language-specific structure, and strengthens with language proximity, model quality and data exposure. It distinguishes similarity (shared neighborhood geometry) from alignment (shared coordinates), showing that the latter occurs when code-switched data, i.e. mixed-language sentences, are abundant enough. It further predicts that subtracting from each layer the component linearly predictable from the preceding one increases cross-lingual similarity, which we confirm in pretrained LLMs.

---


### 47. [Identifying Introspection From the Inside](https://arxiv.org/abs/2610.07186)

**<font color=#1a73e8>作者：</font>** David I. Atkinson, Dillon Plunkett, David Bau  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models make claims about themselves that are both consequential and increasingly difficult to verify from behavior alone. How can we distinguish plausible confabulations from genuine introspection? In this paper, we identify mechanistic signatures of faithful self-report in a controlled setting. Using low-rank adapters, we train models to make decisions on behalf of fictitious characters, according to latent linear preference functions. We find sustained fine-tuning on an implicit decision task can lead to the emergence of accurate self-reporting of models' learned preferences, even without explicit self-report supervision. We ask two research questions about this emergent phenomenon. First: is the emergence of accurate self-reporting accompanied by a measurable structural change in the model? Weight ablations and frozen-layer experiments together indicate that preference representations shift to earlier layers over training, consistent with the hypothesis that faithful self-report requires preferences to be located where pre-existing verbalization mechanisms can access them. Second: can these structural differences distinguish faithful models from unfaithful ones? Using attribution patching, we find that faithful models exhibit significantly higher attribution similarity between the decision-making and self-report tasks -- a mechanistic signature of faithful self-report that does not require us to understand the content of the report itself. Previous work on self-report has observed behaviorally that models can be faithful or unfaithful; our work proposes that, at least in our restricted setting, it is possible to distinguish between the two patterns of computation by examining the structure of the networks themselves.

---


### 48. [Sim-to-Real Transfer of Vision-Language Navigation in Continuous Environments Using an Ackermann-Steered Mobile Robot](https://arxiv.org/abs/2610.07192)

**<font color=#1a73e8>作者：</font>** Chalindu Abeywansa, Sahan Gunasekara, Devindi De Silva 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Navigation (VLN) enables robots to navigate through environments using natural language instructions, making human-robot interaction intuitive. Traditional VLN models often rely on navigation graphs, 360-degree views, and perfect localization which pose significant challenges when adapting these models to real-world settings. This work addresses these limitations by performing a simulation-to-real domain shift of a VLN approach that operates in continuous environments without requiring navigation graphs or panoramic views. The proposed system integrates vision-language models that align visual inputs and linguistic instructions within a shared embedding space, facilitating natural language-driven navigation. We employ a Cross-Modal Attention (CMA) based architecture trained on an existing dataset in a simulated environment and fine-tune it using real-world data collected from a custom-built Ackermann-steered robot equipped with a camera and a LiDAR sensor. By utilising linear photometric adjustments and fine-tuning on a limited number of episodes, our model successfully adapts to real-world environments, achieving effective navigation while running offline on dedicated hardware. Experimental results, evaluated using Success weighted by Path Length (SPL) and Normalized Dynamic Time Warping (nDTW) metrics, demonstrate the robustness and adaptability of our approach. Keywords: Vision-Language Navigation, Cross-Modal Attention, Natural Language Instructions, Sim-to-Real Transfer, Autonomous Navigation, Ackermann-steering.

---


### 49. [Responsible Institutional Analytics: Interpreting Bias with AI Support](https://arxiv.org/abs/2610.07205)

**<font color=#1a73e8>作者：</font>** Francielle Marques, Ariel Ortiz-Beltrán, Ishari Amarasinghe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Institutional Analytics (IA) dashboards inform decision-making in higher education, yet data limitations, constraints in analytical techniques, and missing contextual information often affect their interpretation. To support more responsible interpretation of IA, we introduce FACTRIA, a framework that organizes potential biasing factors across four areas: the analytics pipeline, institutional context, course-level characteristics, and demographics. We used the FACTRIA framework as input to a generative-AI chatbot designed to prompt users to reflect on these factors while analyzing IA. A qualitative study with stakeholders, drawing on four authentic IA cases, and a transition network analysis showed that the chatbot prompted participants to recognize how overlooked factors influenced their initial interpretation. Findings indicated that combining a structured framework with AI-based guidance can enhance context-aware, responsible interpretation of institutional data.

---


### 50. [Distributionally Robust Mixture-of-Experts Training](https://arxiv.org/abs/2610.07207)

**<font color=#1a73e8>作者：</font>** Xin Teng, Muxiao Li, Hongyi Wen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) transformers scale capacity by activating only a few experts per token, but this sparsity creates a hidden reliability problem: when routing is imperfect, load-balanced models may send tokens to experts that are insufficiently trained for the assigned inputs. We propose Distributionally Robust MoE Training (DRMoET), a drop-in objective that treats layer-wise experts as endogenous robustness groups and optimizes high-loss routing outcomes rather than merely equalizing traffic. DRMoET updates a per-layer expert distribution by an entropy-regularized softmax rule on EMA-smoothed, activation-weighted expert losses, strengthening plausible non-top routing paths while preserving standard MoE computation. Under the FLAME-MoE recipe at 746M-total and 10.3B-total scales, DRMoET improves downstream averages over both standard FLAME-MoE and auxiliary-loss-free balancing. At 10.3B total parameters and 67B training tokens, DRMoET improves the seven-task average from 0.6625 to 0.6767, while the auxiliary-loss-free baseline achieves 0.6431. Mechanistic analyses show lower expert-loss variance with nearly unchanged mean loss, 4.3% lower excess loss under forced mid-$k$ misrouting, and improved domain-expert specialization. These results position routing robustness-not only utilization balance-as a practical objective for reliable sparse MoE scaling. Project page and code are available at: this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-303](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
