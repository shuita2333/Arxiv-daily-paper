# 🧠 大模型相关研究 | 2026年07月28日

> 本类共 **80** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-80](./part-02.md)

---

### 1. [FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills](https://arxiv.org/abs/2607.21596)

**<font color=#1a73e8>作者：</font>** Zeyu Ren, Ling Yue, Ran Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly solve complex tasks by constructing inference-time workflows that combine reasoning, tool use, and code execution. While such workflows enable flexible problem solving, the useful procedures discovered during execution are often transient: they help solve the current task but are not retained in a form that can systematically benefit future tasks. We present FlowEvo, a training-free framework that compiles successful traces into reusable skill records. Each record pairs a callable artifact with auxiliary structured guidance, and admission applies interface, replay, and safety checks where feasible. These skill records persist in a skill bank at inference time. FlowEvo is organized around three coupled mechanisms: (1)~workflow-to-skill compilation, which extracts reusable executable artifacts from successful traces; (2)~skill-to-workflow feedback, which retrieves accumulated skills to support future problem solving through either direct execution or structured context injection; and (3)~skill curation, which monitors downstream utility and suppresses skills that cause negative transfer. Through this workflow--skill--workflow feedback loop, FlowEvo enables agents to accumulate and refine task-solving capability over time without updating model parameters. Experiments on benchmarks spanning interactive environments (ALFWorld) and code/math generation (HumanEval, GSM8K) show that FlowEvo achieves the best accuracy-cost tradeoff among the evaluated baselines under our implementation settings. On ALFWorld, FlowEvo achieves an 82.8\% success rate, 23.6 percentage points above the strongest baseline, while its average token usage per episode is less than half that of the most efficient baseline. Controlled ablations confirm that each mechanism contributes to the overall result. The code is public at this https URL.

---


### 2. [Control panels to clarify user intent with Large Language Models](https://arxiv.org/abs/2607.21598)

**<font color=#1a73e8>作者：</font>** Ben Shneiderman  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Typical user interfaces for Large Language Models present a blank prompt window that invites a natural language query by users, but offers little guidance. This paper proposes a visual control panel interface that would provide more cues to the semantics of prompt formation, enabling users to more easily express their intent. By emphasizing recognition over recall, control panels help users formulate more effective prompts that match their intent.

---


### 3. [Securing Multimodal AI through Internal Information Decomposition](https://arxiv.org/abs/2607.21600)

**<font color=#1a73e8>作者：</font>** Jehyeok Yeon, Hyeonjeong Ha, Qiusi Zhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models introduce attack surfaces absent in unimodal systems: adversaries can distribute malicious intent across modalities to evade unimodal safeguards. This motivates using cross-modal consistency as a detection signal rather than inspecting each modality in isolation. Our key observation is that benign inputs induce compatible predictive behavior from text-only and vision-only reasoning that stabilizes when fused, whereas adversarial manipulation disrupts this consistency, causing abnormal multimodal behavior. Existing defenses that examine raw inputs or outputs overlook this internal fusion process, rendering them brittle and computationally expensive. We propose FlowGuard, a lightweight inference-time framework that detects harmful inputs by monitoring internal multimodal consistency. Unlike approaches that rely on scalar confidence metrics, FlowGuard derives FlowVectors inspired by Partial Information Decomposition that quantify cross-modal redundancy, synergy, and modality-specific dominance, capturing whether fused multimodal predictions remain aligned with unimodal semantic evidence. In a one-class classification problem trained solely on benign data, FlowGuard reduces Attack Success Rates from >90% to <15% on unseen attacks, with <3% utility loss and up to a 6 times latency reduction. Our results demonstrate that monitoring cross-modal consistency offers an efficient and effective defense for multimodal reasoning.

---


### 4. [Transferable Latency Prediction for Fast LLM Screening on Heterogeneous Edge Devices](https://arxiv.org/abs/2607.21602)

**<font color=#1a73e8>作者：</font>** Xiaolong Tu, Vinod K. Mishra, Venkat R. Dasari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate latency prediction is critical for deploying large language models (LLMs) on heterogeneous edge devices, where inference latency is affected by model architecture, prompt behavior, runtime backend, hardware utilization, dynamic voltage and frequency scaling (DVFS), and thermal variation. This paper presents a runtime-aware latency prediction framework for deployment-oriented LLM selection. The framework represents each inference request as a hardware-runtime-model-prompt configuration, separates inference into prefill and decode phases, and adaptively fuses static descriptors with dynamic hardware telemetry through a gated prediction model.
We evaluate the framework using Pixel mobile devices and validate the profiling pipeline on Jetson Nano, Orange Pi 5 Pro, and an RTX 3090-class GPU platform. On Pixel 8, the full predictor improves total-latency R-squared from 0.953 to 0.960 and decode-latency R-squared from 0.957 to 0.973 over a static-only baseline. On Pixel 8 Pro, it improves prefill-latency R-squared from -1.383 to 0.966. For cross-device transfer, calibration improves Pixel 8 Pro to Pixel 8 total-latency R-squared from -0.974 to 0.940 and decode-latency R-squared from -1.085 to 0.927. Heterogeneous profiling further shows that latency is highly device- and runtime-dependent: the same SmolLM2 model family reaches 8.42 tokens/s on Orange Pi 5 Pro but 64.38 tokens/s on an RTX 3090-class GPU. These results demonstrate that runtime-aware prediction with lightweight calibration can reduce profiling cost and support latency-aware LLM deployment across heterogeneous edge platforms.

---


### 5. [AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems](https://arxiv.org/abs/2607.21604)

**<font color=#1a73e8>作者：</font>** Nilesh Prasad Pandey, Jason Kong, Lanxiang Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory-augmented LLM agents maintain context across hundreds of interactions through agentic memory systems that actively curate retrieved content with LLM-generated metadata such as summaries, keywords, and tags. From an inference cost standpoint, every retrieval triggers a full re-encoding of these structured memory units into Key-Value (KV) states, which dominates prefill latency. Existing training-free KV reuse methods mitigate this by selectively recomputing a small fraction of tokens, but were designed for RAG-style raw passages and degrade on structured agentic memories. We present AgentKVShift, a training-free, probe-guided KV residual correction method that operates per retrieved memory unit. One of the crucial insights we demonstrate is that the per-memory KV reuse residual decomposes into a shared memory-level offset plus small token-wise fluctuations. Estimating this offset from a small probe set allows us to correct every reused token by a single weighted correction. Unlike prior reuse methods which decide which tokens to recompute and leave the rest of the cache stale, AgentKVShift also corrects the tokens it does not recompute, turning the refresh budget into useful signal across the entire chunk. Across four open-source LLMs spanning 3B to 32B parameters and two long-horizon agentic memory benchmarks (long-term dialogue and agentic applications), AgentKVShift achieves near full recompute performance while refreshing only 10-30% of the cache, outperforming baselines at the same recompute ratio. It requires up to 5x lower recompute to reach this near-full performance, which prior reuse methods only attain at 45-55% refresh. In this regime, AgentKVShift delivers prefill speedups of 2-3.5x over no-KV-reuse on a single A100. AgentKVShift orthogonally composes with KV cache quantization, retaining over 2x the F1 of prior reuse methods under aggressive 2- and 4-bit settings.

---


### 6. [Coupled Hierarchical Search over Topology and Execution for Agentic Workflow Synthesis](https://arxiv.org/abs/2607.21609)

**<font color=#1a73e8>作者：</font>** Dong Li, Yanchi Liu, Xujiang Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although structured workflows empower Large Language Models (LLMs) to tackle complex problems, automating their creation is severely hindered by a vast combinatorial search space, frequently resulting in inflexible and resource-heavy offline training dependencies. To address this, we conceptualize workflow generation as an intertwined topology-and-execution search paradigm, where the broader topological layer dictates subtask boundaries and lower-level execution outcomes actively reshape the topology itself. Building on this foundation, we introduce HierFlow, a training-free, test-time hierarchical search architecture that automates agentic workflow design by merging feedback-guided topology adjustments with a fast, MCTS-inspired tree search for sub-workflow optimization. HierFlow maximizes efficiency through an intelligent gating module that selectively triggers execution-level searches based on contextual necessity, a mechanism we further support with an in-depth analysis detailing how varying degrees of cross-task coupling impact the effectiveness of hierarchical splitting. Comprehensive testing across question answering, mathematical reasoning, and code generation benchmarks confirms that HierFlow consistently outperforms strong baselines, delivering an optimal balance of high-quality results and computational efficiency without any additional training overhead.

---


### 7. [Procedural Knowledge Is Not Low-Rank: Why LoRA Fails to Internalize Multi-Step Procedures](https://arxiv.org/abs/2607.21612)

**<font color=#1a73e8>作者：</font>** Simon Dennis, Kevin Shabahang, Hao Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning methods like LoRA have become the default for adapting large language models, succeeding across instruction following, style transfer, and factual adaptation. We show that for procedural knowledge--the ability to follow multi-step procedures with conditional branching through to terminal states--LoRA fails to match full fine-tuning at the ranks where it retains its efficiency advantage. In a systematic ablation (r = 16--128) on a procedural travel booking task (14 nodes), all LoRA configurations fail uniformly (task success <= 2.54 vs. 4.11 for full fine-tuning, all p < 0.001), with scores decreasing at higher ranks--despite maintaining 95--99% conversation completion rates. Cross-domain replication on Zoom support (14 nodes) and insurance claims (55 nodes) at 8B confirms the failure generalizes: LoRA underperforms full fine-tuning by 0.8--2.2 points on average at both r = 32 and r = 128, with the largest gap on the most complex procedure. Quadrupling rank from 32 to 128 provides marginal improvement but does not close the gap. SVD analysis of the weight changes produced by full fine-tuning explains why: across three domains at both 3B and 8B, the mean effective rank of the update ranges from 761 to 1,026, and rank 128 captures only 43--51% of the squared Frobenius norm. Together, these findings establish that for procedural tasks LoRA falls well short of full fine-tuning--a fundamental limitation for agentic applications.

---


### 8. [The Hard Decision Layer: Evidence for Committed Inference in Transformers](https://arxiv.org/abs/2607.21613)

**<font color=#1a73e8>作者：</font>** Ashwath Vaithinathan Aravindan, Mayank Kejriwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate where and how transformer-based language models commit to predictions in multiple-choice question answering. We identify the _Hard Decision Layer_ (HDL), a natural architectural property where answer option rankings stabilize abruptly during inference. Empirical validation across four language models (Qwen, Llama, Granite, Mistral) and four benchmark datasets demonstrates consistent HDL emergence without learned routing policies. We also show that the HDL is invariant to fine-tuning. Our results reveal striking accuracy improvements at the HDL: up to +0.61 (Qwen on CommonsenseQA), after which performance stabilizes. Systematic ablations on label formats and problem complexity confirm the phenomenon is fundamental to model architecture. These findings offer mechanistic insights into transformer inference and suggest opportunities for efficient reasoning and model steering. All code and results required to reproduce this work are available in this https URL

---


### 9. [Household Movement Detection in Mixed-Format Occupancy Data Using LLM-Based Entity Resolution](https://arxiv.org/abs/2607.21614)

**<font color=#1a73e8>作者：</font>** Sasirekha Oguri, John R. Talburt, Mert Can Cakmak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Entity resolution (ER) typically relies on pairwise similarity comparisons between records, which limits its ability to capture indirect relationships present in demographic occupancy data. An important indirect pattern arises from household movement, where multiple individuals relocate together across addresses, but detecting such patterns is difficult due to mixed-format records, noise, duplication, and the absence of stable identifiers. This paper proposes an AI-enhanced framework for detecting indirect entity links associated with household movement in unstandardized name-address data. The approach integrates prompt-based large language model (LLM) named entity recognition for extracting personal names and addresses without extensive preprocessing, semantic text embeddings for robust similarity computation, and graph-based reasoning to infer group-level movement patterns. Experimental evaluation on SPX benchmark datasets (S8-S12) generated using the Synthetic Occupancy Generator demonstrates that incorporating indirect household movement evidence improves recall by 8-15% while maintaining high precision, yielding F1-score gains of 6-8% over a strong pairwise baseline.

---


### 10. [Lost in Context: Addressing Context Anxiety in Large Language Models](https://arxiv.org/abs/2607.21616)

**<font color=#1a73e8>作者：</font>** Ifueko Igbinedion, Jillian Ross, Etienne Ricardez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conventional wisdom suggests that reasoning models fail when problems exceed their capabilities. However, we find that frontier reasoning models sometimes possess the necessary capabilities to solve problems but fail due to premature self-doubt -- a phenomenon informally known as context anxiety. We provide the first systematic study of context anxiety, demonstrating that it arises, in part, from a model's inability to accurately estimate the tokens required to complete a task. We also show that context anxiety leads to material efficiency losses when models operate under perceived constraints. Building on this analysis, we further show that models can learn alternative strategies for solving long-horizon problems without exhibiting context anxiety, suggesting that performance improvements may be achievable not through scaling model capabilities, but by improving models' ability to accurately assess and adapt to their own limitations.

---


### 11. [Do VLMs Read or Rewrite? On Transcription Faithfulness in Vision-Language Models](https://arxiv.org/abs/2607.21617)

**<font color=#1a73e8>作者：</font>** Gwang Gook Lee, Kenan Emir Ak, Jay Mohta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) are increasingly used in place of traditional OCR pipelines for document understanding. In this paper, we show they do not always act as faithful transcribers: when text is imperfect, they often tend to rewrite it into a more plausible form - a behavior that clean-text OCR benchmarks cannot detect. We introduce FaithC4, a multilingual perturbation benchmark of 1,455 single-page documents (English, Chinese, Korean) with three perturbation families: scramble, random substitution, and visually similar substitution. We use the benchmark to evaluate 15 systems spanning general-purpose VLMs, OCR-specialized VLMs, and traditional OCR pipelines. These three categories differ in WER degradation under perturbation: general-purpose VLMs degrade by up to 4.5 points, OCR-specialized VLMs by 0.2-2 points, and traditional OCR by less than 0.6 points on English. Probing Qwen3-VL-4B layer-by-layer, we identify a consistent pattern: rewriting fires only when a perturbed word's final layer FFN representation stays close to the original encoding; when the representation diverges sufficiently, the model transcribes faithfully. Word length affects rewriting rate: short words (4-6 characters) are rewritten up to 10% of the time, with a sharp cutoff at 8 characters above which rewriting drops to 0%.

---


### 12. [LeafData: An Agentic System for Data Migration](https://arxiv.org/abs/2607.21618)

**<font color=#1a73e8>作者：</font>** Sadanand Katukuri, Rajasekhar Bada, Navya Induri 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern data migration relies on JSON configuration to define data connection, pipeline logic, and orchestration behavior. This requires domain knowledge from users and is time-consuming and error-prone. In this paper, we present LeafData, an agentic system that converts user intent into validated and executable JSON configuration for data migration. Specifically, LeafData comprises a frontend chatbot and the backend service. The chatbot incrementally collects required information from users and performs schema-driven validation, while the backend service processes validated inputs and generates JSON configuration artifacts. These artifacts are directly consumable by orchestration platforms, enabling end-to-end pipeline generation and execution without manual coding. LeafData supports heterogeneous data migration across various data sources and connectors including relational databases, file-based systems, document-oriented databases, and REST APIs.

---


### 13. [Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization](https://arxiv.org/abs/2607.21619)

**<font color=#1a73e8>作者：</font>** Bingjun Luo, Jialin Guo, Yue Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved impressive performance, but their safety alignment remains vulnerable to jailbreak attacks. Existing content-based jailbreaks are often inconsistent and show unsatisfying performance against the rapidly evolving MLLMs, failing to exploit non-content-based vulnerabilities. Unlike previous research, we empirically find that MLLMs exhibit a Stylistic Inconsistency between their comprehension ability and safety ability: MLLMs can robustly understand content regardless of visual style, yet their defense mechanisms can be easily bypassed by specific stylistic triggers. Based on this finding, we propose Adversarial Style Optimization (ASO), a plug-and-play enhancement module to amplify existing visual jailbreaks. ASO fine-tunes an image-editing model to superimpose an optimized stylistic modification onto a given adversarial image, using a Group Relative Policy Optimization (GRPO) agent guided by a Structurally-Tiered Reward Function that combines a logit-based signal for detecting explicit refusals with a high-fidelity semantic evaluation from a powerful judge model. Extensive experiments show that ASO significantly enhances the ASR of SOTA attacks, demonstrating that stylistic biases are a scalable vector for red-teaming MLLMs. Our code is available at this https URL.

---


### 14. [FBLayout: Optimizing Memory Layout for Efficient LLM Finetuning on Mobile GPUs](https://arxiv.org/abs/2607.21624)

**<font color=#1a73e8>作者：</font>** Kahou Tam, Wei Niu, Yu Bao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer-based models have enabled unprecedented capabilities across language, vision, and multimodal tasks. On-device fine-tuning of transformer models offers a privacy-preserving path to personalized AI, yet remains inefficient on mobile GPUs due to severe memory constraints and frequent layout transformations in attention mechanism during training. Existing mobile training frameworks either use unified layouts for forward and backward passes -- leading to fragmented memory access and poor GPU utilization during backpropagation -- or rely on explicit layout conversions, which introduce significant transformation overhead.
To overcome this, we propose FBLayout, a layout-aware framework that co-designs tensor organization with mobile GPU platforms. FBLayout introduces: (1) a unified R-Tile layout for multi-dimensional reductions across forward/backward passes; (2) tile-based index transformation to eliminate physical data movement; and (3) activation-guided layout selection to propagate efficient layouts globally. Evaluations on seven transformer models across different mobile phones (including ARM Mali and Qualcomm Adreno GPUs) show that FBLayout achieves 2.2-5.7x speedup over MNN, TFLite, and TVM, while significantly improving cache efficiency and reducing memory footprint, enabling practical on-device large model fine-tuning.

---


### 15. [Trajectory-Aware Retrieval Agents for Temporal Decision- Making](https://arxiv.org/abs/2607.21625)

**<font color=#1a73e8>作者：</font>** Jing Wang, Jie Shen, Xing Niu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the problem of decision-making from long-form, temporally structured text using large language model (LLM) agents. Standard retrievalaugmented generation (RAG) pipelines fragment chronological context into isolated snippets, discarding the temporal structure that is often critical for correct downstream decisions. We introduce TLM (Trajectory Language Model), a closed-loop agentic framework that iteratively refines the evidence set using SHAP-guided feedback. The key technical contribution is the latent growth curve model (LGCM) over retrieved chunk embeddings, which provides an interpretable mechanism for detecting trajectory trends, turning points, and information gaps. We show that, under a scorer-calibration assumption (which holds approximately in practice), the iterative refinement procedure is monotonically non-decreasing in the probability assigned to the correct label. Empirically, TLM is evaluated on three temporally grounded decision tasks: medical question answering, earnings call surprise prediction, and overnight stock gap prediction. TLM substantially outperforms both zero-shot LLM baselines and standard retrieval-augmented approaches on the medical task, and yields consistent, economically meaningful gains on the two financial tasks.

---


### 16. [Do Modules Stay in Their Lane? Role Drift in Compound LLM Systems](https://arxiv.org/abs/2607.21627)

**<font color=#1a73e8>作者：</font>** Xiaoyang Cao, Siddarth Srinivasan, Michiel A. Bakker  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> End-to-end reinforcement learning can improve the accuracy of compound LLM systems, but it does not constrain how modules divide labor internally. We identify Role Drift, a failure mode in which modules preserve or improve end-task performance while deviating from their assigned roles through role-violating shortcuts that remain invisible to system-level evaluation. To make role drift observable and controllable, we propose Role Anchor, a regularizer that modulates how much each module deviates from its assigned role during end-to-end training. The key idea is to preserve how the role prompt shifts the module's next-token predictions relative to a neutral prompt, which serves as a proxy for the role's intended effect during training. Experiments on two compound LLM pipelines reveal role drift that accuracy alone fails to detect: a decomposer meant to split a question into sub-questions for a separate solver instead plants the answer in them, and a reader meant to answer from retrieved passages instead falls back on parametric memory. In fact, on the decomposer pipeline this shortcut drives most of the apparent RL gain: 86% of it vanishes once the decomposer is held to its role, indicating that terminal accuracy alone can badly overstate how much a compound system has genuinely learned. Across both pipelines, Role Anchor mitigates role drift at a tunable accuracy cost that varies by pipeline and anchor strength. Additional gradient analysis suggests that the regularizer reduces alignment with the role-drift direction rather than simply suppressing learning.

---


### 17. [A Consensus-Based Framework for Relative Preference Evaluation of Large Language Models](https://arxiv.org/abs/2607.21632)

**<font color=#1a73e8>作者：</font>** Mohtashim Khan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditional benchmarks for LLMs primarily rely on static datasets and objective scoring metrics, which often fail to capture differences in response quality when multiple answers are acceptable. In such settings, correctness alone is insufficient to distinguish between responses that vary in clarity, completeness, and usefulness.
This paper introduces a consensus-based evaluation framework that measures relative preference among model-generated responses rather than absolute correctness. Instead of evaluating outputs against a fixed ground truth, we assess how a panel of diverse LLMs ranks anonymized candidate responses to the same prompt. This approach treats aggregate inter-model agreement as a proxy for perceived response quality under blind conditions.
We conduct a controlled study using five state-of-the-art LLMs across multiple domains, including programming, general knowledge, safety, logical reasoning, and mathematics. Each model generates responses and independently ranks peer outputs through a structured voting process. Scores are aggregated into a Relative Intelligence Index (RII), representing how frequently a model's responses are preferred by other models.
Our findings reveal consistent preference patterns across domains, with certain models more frequently ranked highly by their peers. However, we emphasize that these results reflect inter-model preference alignment rather than objective correctness or human judgment. This framework provides a scalable, model-driven method for comparative evaluation, offering an alternative perspective on response quality in scenarios where multiple valid answers exist. While not directly aligned with human evaluation, prior work suggests that aggregated model preferences can partially correlate with human judgments, motivating this as a proxy signal.

---


### 18. [Toward User-Conditioned Evaluation of Personal LLM Agents under Temporal Interventions](https://arxiv.org/abs/2607.21635)

**<font color=#1a73e8>作者：</font>** Pin Qian, Su Wang, Yihang Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personal agents maintain memories, learned skills, tool configurations, and policy state that evolve with each user. Existing agent benchmarks often evaluate these capabilities in isolation: tool benchmarks test invocation under fixed APIs, memory benchmarks test recall or forgetting, and safety benchmarks test static policy compliance. We argue that personal-agent evaluation requires a different protocol: replaying the same temporal intervention across different persistent user-conditioned states and measuring how failures propagate across agent components. We formalize this requirement as four conditions: explicit temporal intervention, persistent state across the intervention, induced cross-dimensional effects, and variation in user-conditioned state. A focused audit of public benchmark protocols selected by explicit inclusion criteria identifies several close cases. Under our explicitly narrow operationalization, we did not find a protocol in that audited set satisfying all four conditions. This claim is scoped as a focused gap analysis with bounded literature coverage. This position paper proposes a minimal benchmark design and candidate reporting metrics for user-conditioned adaptation. The result is a concrete design requirement for future personal-agent evaluation, with metrics used as reporting tools for that requirement.

---


### 19. [Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.21653)

**<font color=#1a73e8>作者：</font>** Jian Hu, Huiying Li, Hao Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning research is constant algorithm modification, new estimators, new pipeline stages, new rollout schemes, and in mainstream frameworks each change threads through layers of trainer, distributed backend, and rollout glue: the cost lands on the researcher at every iteration. Molt is a PyTorch-native training framework built to keep that cost small: a codebase compact and clean enough for a researcher to hold in their head, and for an AI coding assistant to read and reason about in its entirety, so the algorithm flow can be traced and changed end to end. The agent is an ordinary program, and one asynchronous loop trains multimodal and mixture-of-experts policies while never training on a token it did not generate, consistent in tokens, policy versions, and model semantics. Leanness does not cost performance: under a matched, fully asynchronous protocol, Molt is statistically comparable to a state-of-the-art Megatron-based stack. Molt is open source and provides recipes and containers at this https URL.

---


### 20. [Encoding Invisible Causation for Bridge Diagnostic Agents: Triple-Guided Retrieval-Augmented Fine-Tuning with QLoRA](https://arxiv.org/abs/2607.21680)

**<font color=#1a73e8>作者：</font>** Takato Yasuno  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bridge infrastructure deteriorates gradually, yet its root causes---salt intrusion, freezing, fatigue cracking, and others---remain invisible to the naked eye. Expert diagnosis relies on tacit knowledge built over years of practice. We address the challenge of automating this latent causal reasoning by proposing a Damage Cause Encoder that classifies 10-class damage causes from visible damage descriptions $S_i$ for use in autonomous bridge diagnostic agents. Our approach chains three components: (i)Knowledge Triple Extraction---a large language model extracts causal triples of the form (damage $\xrightarrow{\mathtt{caused\_by}}$ cause) from 15--35 diagnostic PDF manuals and indexes them in a FAISS vector store; (ii)Retrieval-Augmented Context---at training and inference time, relevant causal triples $\mathcal{C}_i$ are retrieved and concatenated with $S_i$, converting implicit domain knowledge into explicit Encoder context; (iii)Systematic Fine-tuning Comparison---we conduct a rigorous comparison of LoRA, QLoRA, and QA-LoRA on a fixed Golden Testset (116 stratified samples), demonstrating that QLoRA achieves the optimal trade-off: identical test accuracy (87.07%) to full-precision LoRA, 11% faster inference, 72% lower GPU memory, and superior generalization across diverse unseen inputs. A controlled Golden Testset---stratified, deduplicated, and difficulty-tagged---is introduced as a reusable benchmark contribution. QLoRA further outperforms LoRA by 13 percentage points on a 100-sample diverse evaluation spanning all 10 damage cause this http URL findings enable memory-efficient, high-accuracy diagnostic agents on consumer-grade hardware for edge deployment.

---


### 21. [Persistent Computational State: A Session-Centric Runtime for Generative World Models](https://arxiv.org/abs/2607.21686)

**<font color=#1a73e8>作者：</font>** Zhen Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative world models are increasingly driven as simulators: a planner forks a state, rolls out futures, backtracks, and returns to a visited viewpoint. Recent benchmarks establish that current video world models fail this usage, and attribute it to the model, prescribing new architectures and training objectives. We show this attribution is incomplete, and for an important class of models simply wrong. Snapshotting the state the runtime already holds -- an observation plus RNG state, a memory bank, or a windowed KV context, by architecture -- and restoring it after a genuine excursion reproduces the never-left continuation byte-identically on all three; corrupting only the RNG degrades it. The capability was never missing: request-centric serving discarded it, inheriting from language-model serving the assumption that runtime state is recomputable -- but world-model state carries a non-recomputable kernel. We define Persistent Computational State (PCS), the minimal non-recomputable state that must survive across requests, show it can be discovered by measurement, and build a session-centric runtime over it. Checkpoint and restore cost 0.012 ms against a 1.85 s generation step; resident sessions become host- rather than device-bounded (measured to 1,024); and world memory must be evicted by relevance to the return, not recency -- the inverse of LLM practice.

---


### 22. [Oxygen-TryOn: Fashion-Native Foundation Model for Any-item Virtual Try-On](https://arxiv.org/abs/2607.21694)

**<font color=#1a73e8>作者：</font>** Yong Liu, Xiaolong Fu, Zihang Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Oxygen-TryOn, a unified foundation model for any-item virtual try-on. Rather than repurposing a general-purpose image editor, Oxygen-TryOn is fashion-native, built for try-on through a dedicated data engine and try-on-specific training. Given one or more reference items (clean product shots or in-the-wild worn-on photos) and a single target subject image, it synthesizes a photorealistic image of the subject wearing the items across virtually any fashion category. Prior systems handle a single garment category in a studio setting, and recent multi-reference methods remain garment-centric; in contrast, Oxygen-TryOn supports diverse items and scenarios, including full- and half-body views, a variable number of references, and free multi-item composition, while faithfully preserving both subject identity and item appearance. Instead of mask-based inpainting, we reformulate try-on as a multi-reference, understanding-driven generation task. We build a data engine that collects, manufactures, annotates, and filters high-quality try-on data at scale, and design a three-stage recipe of continued pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL). The RL stage uses a hybrid reward combining an in-house try-on reward model with a proprietary, rubric-guided general-purpose model, jointly supervising fine-grained consistency and instruction-level quality. It also follows general editing instructions (e.g., pose changes) in the same pass. Across public benchmarks and our in-house Oxygen-TryOn Bench, it achieves state-of-the-art consistency and realism on single-item try-on and leads on multi-item try-on, matching or surpassing both leading proprietary systems (Nano Banana Pro, GPT-Image-2, Seedream5 Lite) and open-source models (FLUX.2).

---


### 23. [Be Consistent! Enhancing Robust Visual Reasoning in LVLMs with Consistency Constraints](https://arxiv.org/abs/2607.21722)

**<font color=#1a73e8>作者：</font>** Liqiang Jing, Xiong Zhou, Siddharth Varia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Large Vision-Language Models (LVLMs) exhibit strong perceptual capabilities, they remain vulnerable in visual reasoning tasks. Existing benchmarks largely focus on symbolic mathematical or scientific problems and simple vision-centric tasks, offering limited assessment of complex visual reasoning and logical consistency, a critical requirement for reliable reasoning systems. We introduce ConVBench, a complex vision-centric reasoning benchmark in which each image is paired with two logically equivalent questions across six categories: action and state, complex counting, spatial reasoning, causal and intent understanding, commonsense reasoning, and temporal perception. To complement this benchmark, we define two evaluation metrics, logical consistency and robust accuracy, that jointly assess both the correctness and consistency of model responses. We further present ConVLM, which improves LVLM reasoning through Group Relative Policy Optimization (GRPO)-based reinforcement learning with a novel consistency reward. This method leverages automatically generated logically equivalent question-answer pairs and a dual-reward design combining accuracy- and consistency-based signals, encouraging agreement between paired responses. The framework functions effectively with or without strict answer supervision.

---


### 24. [Bespoke Visual Assistance: What and How do Blind and Low-Vision People Create with Agentic Programming?](https://arxiv.org/abs/2607.21760)

**<font color=#1a73e8>作者：</font>** Ellie Seehorn, Gene S-H Kim, Aziz Zeidieh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-powered assistive technologies have long supported blind and low vision (BLV) people in everyday tasks, but they are general-purpose and often fall short of meeting complex, individualized, in-situ accessibility needs. Though agentic programming tools, like GitHub Copilot, have the potential to bridge this gap by lowering the technical barriers to building personal AT using natural language, the practical applicability of this creation paradigm has been unknown. We address this knowledge gap through a two-phase longitudinal co-design study with five tech-savvy BLV users using ProgramAT, an agentic programming tool that supports the creation, iteration, and testing of camera-based AT. Overall, co-designers created over 37 tools, with some addressing needs unmet by any existing commercial AT such as identifying Uber rides or interpreting hand gestures. Qualitative feedback from our co-designers and analysis of development logs surface BLV strategies for tool creation, along with key challenges including model capability limits, specification conflicts, and barriers to successful creation. We discuss recommendations to provide appropriate conversational scaffolding, community tool sharing capabilities, and support for specialized models and personal datasets for future agentic programming environments to empower BLV users to create bespoke visual assistance for themselves.

---


### 25. [Probing Latent Colombian Identity Inferences in Qwen2.5-7B with Natural Language Autoencoders](https://arxiv.org/abs/2607.21774)

**<font color=#1a73e8>作者：</font>** Pablo Santiago Potes Velasco, María del Mar García Matabanchoy, Óscar Julián Pérez Ladino 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models may infer demographic attributes from subtle linguistic cues even when those attributes are not explicitly stated. This pilot study examines whether Qwen2.5-7B-Instruct internally represents Colombian identity, socioeconomic status, or stereotype-related information when processing Colombian-Spanish and English prompts. We use Natural Language Autoencoders (NLA) to verbalize residual-stream activations from layer 20 across four positional quartiles per prompt. Our dataset contains 30 prompts arranged as 15 matched Spanish-English pairs, spanning explicit Colombian cues, implicit Colombian cues, and neutral controls. We report descriptive rates and qualitative evidence rather than statistically powered effects, focusing on whether latent nationality or stereotype representations appear before they are verbalized in the model output. This work connects activation-level interpretability with bias evaluation for underrepresented Spanish varieties.

---


### 26. [Khondo: A Multimodal Benchmark for Document Packet Splitting of Bangla Forms](https://arxiv.org/abs/2607.21780)

**<font color=#1a73e8>作者：</font>** Abu Tyeb Azad, Fahim Ahmed, Ishita Sur Apan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document packets, multiple documents concatenated into a single file, are common in government and administrative workflows, yet splitting them into their constituent documents is difficult, especially for low-resource languages. We introduce Khondo (Bangla for split/segment), the first benchmark for document packet splitting on Bangladeshi government forms. Unlike prior English and OCR-text-based datasets, Khondo is bilingual (Bangla--English) and vision-native; where models operate directly on page images. It spans five concatenation schemes, from sequential to fully shuffled, across 14 administrative domains, with ground-truth boundaries, domain types, and page order. Zero-shot evaluation of MLLMs shows they cluster pages into their source documents fairly well but struggle in restoring the original page order once shuffled. To isolate what drives this difficulty, we run two controlled analyses, varying the prompt instruction and then the packet language. Both primarily affect ordering rather than clustering: (a) explicit page-order instructions are necessary but insufficient, and (b) English packets are ordered more reliably than Bangla, making page arrangement the dominant challenge and language a secondary but consistent factor. Khondo establishes page-order reconstruction as a key open problem in vision-based, low-resource document understanding, and provides a controlled benchmark for measuring progress toward solving it. Our dataset and code is available at this https URL

---


### 27. [Agentic Evaluation of Copyright Law Compliance](https://arxiv.org/abs/2607.21799)

**<font color=#1a73e8>作者：</font>** Zheng Hui, Doni Bloomfield, Noam Kolt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly perform commercial tasks that involve retrieving external content such as images and, where appropriate, reproducing that content. LLM agents should comply with the law, including copyright law. Presently, however, we lack adequate frameworks to assess whether they do so in practice. To that end, we introduce \textbf{Copyright-Bench}, a benchmark designed to evaluate \textit{LLM agents' compliance with} \emph{copyright law}. Copyright-Bench is comprised of realistic commercial tasks---website development, merchandise design, and pitch deck production---that involve agents selecting between public-domain content (the use of which is \textit{legal}) and copyrighted content (the use of which is \textit{infringing} in this setting).The evaluation introduces prompt variations that simulate different user preferences, as well as time this http URL state-of-the-art LLM agents against a human baseline, we find that: (1) agents select copyrighted works despite the availability of public-domain alternatives; and (2) for open-weights models, violation rates increase in response to certain user preferences and simulated time pressure.

---


### 28. [VisCanvas: A Node-based Interface for Exploratory Visualization Authoring with LLMs](https://arxiv.org/abs/2607.21886)

**<font color=#1a73e8>作者：</font>** Yuki Ueno, Bretho Danzy III, Zhuojun Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual data analysis involves both open-ended exploration and targeted question answering. Visualization authoring tools support this process by enabling users to create visualizations for these tasks. With the rise of large language models, substantial effort has been devoted to developing visualization authoring tools that use natural language instructions. However, existing systems are typically based on a linear chat interface, which is not well suited to exploratory visual analysis workflows. In this paper, we introduce VisCanvas, a node-based interface for exploratory visualization authoring with LLMs. VisCanvas allows users to create, revise, branch, and merge visualizations in a non-linear way, enabling more efficient exploration of multiple analytical directions. We conducted a user study with 20 participants to evaluate the effectiveness of VisCanvas compared to a baseline chat-based interface. The results show that VisCanvas facilitates more diverse data interaction while maintaining performance levels (i.e., cognitive load and usability) that are indistinguishable from current prevailing methods. We then distill design principles for future AI-assisted visualization authoring environments. All supplemental materials required to reproduce the study are available at this https URL.

---


### 29. [Towards Reducing Foreign Language Anxiety Using Level-Appropriate Embodied Conversational Agents](https://arxiv.org/abs/2607.21887)

**<font color=#1a73e8>作者：</font>** Krishan Rajaratnam, Wenbin Gan, Yuan Sun  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Foreign language anxiety (FLA) can be a major barrier to second language acquisition (SLA), especially in conversational contexts. With the proliferation of large language models (LLMs) throughout all areas of life, recent work suggests that interacting with LLM agents can be instrumental within the field of SLA and foreign language education, especially for reducing FLA. Related work also suggests that linguistic demands and task complexity can be predictors of FLA, implying that the use of demanding, complex language could lead to learners experiencing higher FLA. In this paper, we propose a novel multi-agent embodied conversational system that generates level-appropriate dialogue for English language learners. These levels are based on those defined by the Common European Framework of Reference for Languages (CEFR) to describe non-native listener and speaker proficiency. Using a "generate-evaluate-regenerate" loop with multiple LLM agents and a level classifier, it achieves a desired simplicity that is adaptive to the user's proficiency level. We also share the results of a preliminary small-sample pilot study that tested this system with Japanese university students, to see whether it would yield lower FLA levels than an unsimplified embodied conversational agent. Analysis of conversational output showed that 87.4% of dialogue sentences generated by the proposed multi-agent system fell within one predicted CEFR level of the learner's self-assessed proficiency, compared to 54.1% for the unsimplified agent. This suggests that the novel system is better able to produce output at an appropriate level for the learner. Though this study did not yield statistically significant evidence that the system reduces FLA levels in Japanese learners of English, likely due to a small sample size, it provides usability findings and culturally-informed design insights that will inform future study.

---


### 30. [TRW: TRACE-RealWorld---An Auditable Consistency Contract for World Models as Materialized Views](https://arxiv.org/abs/2607.21910)

**<font color=#1a73e8>作者：</font>** Edward Y. Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> TRACE-RealWorld addresses a core data-management problem: maintaining an actionable materialized view over a continuously changing physical world when reads of the base state are priced, delayed, heterogeneous, and fallible. Its data-management contributions are a commitment-level validity abstraction for materialized predictions; consequence-conditioned adaptive view maintenance; transaction-style, dependency-scoped compensation for commitments invalidated after authorization; and append-only provenance supporting exact replay. The work builds directly on materialized-view maintenance, adaptive stream synchronization, transaction recovery, sagas, data freshness, and provenance. The end-to-end Flood-SAR evaluation treats sensing as physical data acquisition and measures freshness, verification cost, stale reads, recovery scope, restoration failure, and replayability through six pre-registered questions with held-out seeds. The contribution is therefore not a new predictive model, but a consistency, recovery, and accountability contract for deploying learned world representations as operational data systems.

---


### 31. [Reliability-Contagion Feasibility in LLM Multi-Agent Networks](https://arxiv.org/abs/2607.21912)

**<font color=#1a73e8>作者：</font>** Ruiwu Niu, Xincheng Shu, Ying Zhao  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Communication allows large language model agents to pool evidence, but it also creates paths along which an erroneous claim can spread. We formulate a correction-aware network model that tracks susceptible, exposed, infectious, and corrected agents and derive its early-invasion condition for heterogeneous communication networks. We then couple this propagation model to an analytic majority-vote benchmark in which a clean-task reliability target imposes a minimum connectivity requirement. Under fixed exposure per communication edge, reliability and error control impose opposing graph constraints. We characterize when their intersection is empty and when it contains an intermediate connectivity range, and identify regular graphs that attain the smallest invasion factor within the reliable graph class when such graphs exist. Under a fixed sender budget, the homogeneous first-order threshold is independent of network density, showing that the communication-budget convention determines whether added edges increase early propagation risk. Finite-network simulations on 21,000 trajectories illustrate these directional predictions. A controlled grok-4.3 experiment then evaluates three six-node topologies on 36 new closed-world tasks, with a balanced 12-task subset continued to full cascades. Mean first-generation offspring increased from 0.667 to 1.333 and 1.667 as degree increased from 2 to 4 and 5, while the adoption fraction among exposed neighbours remained 0.333. Mean non-seed erroneous adoption in the full-cascade subset was 0.200, 0.333, and 0.333. Together, these results provide a tractable basis for selecting connectivity under explicit reliability and propagation constraints.

---


### 32. [RIS-Kernel: A Model-Agnostic Architecture for Long-Context LLM Inference via Sparse Attention](https://arxiv.org/abs/2607.21927)

**<font color=#1a73e8>作者：</font>** Anderson R. Santos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full self-attention in large language models scales as O(N^2), which limits long-context document analysis to 65,536 tokens and requires costly GPU clusters. The Reduced Interaction Sampling (RIS) inference engine addresses this constraint as a model-agnostic architecture. Without modifying weights, RIS reduces self-attention complexity to O(N log N) using sparse stochastic geometry that fits within commodity memory limits. We validate RIS on Qwen2-1.5B-Instruct across two regimes. In controlled evaluations at 32,768 tokens (where native dense attention serves as the upper bound), RIS-Stochastic at 1% density and 70 ensemble seeds achieves 75.00% accuracy, outperforming the native dense baseline (71.88%), while RIS-Stochastic at 5% density and 10 seeds matches it (71.88%). This demonstrates that sparse attention acts as a regularizer: low density (1%) over multiple seeds filters out sequence-level noise, whereas higher density (5%) reintroduces distractor noise. Under the tightest budget, RIS-Structural reaches 68.75% accuracy at 1% density with just 10 seeds, recovering 75% of the contextual gap relative to the zero-context floor (59.38%). At 65,536 tokens, where dense attention triggers out-of-memory faults, RIS yields retrieval gains of up to 14.06 percentage points over the zero-context floor (51.56%), which is confirmed as marginally significant under McNemar's paired test (p = 0.078 < 0.10). All evaluations run on commodity, unaccelerated CPU servers (16-128 GB of RAM), demonstrating that long-context LLM inference is feasible on standard academic hardware without GPU acceleration.

---


### 33. [Semiotic logical hexagon theory for LLM logical reasoning](https://arxiv.org/abs/2607.21933)

**<font color=#1a73e8>作者：</font>** Yunyao Zhang, Xinglang Zhang, Zeliang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have become powerful tools for language understanding and logical reasoning. However, they still make mistakes when a problem requires both understanding meaning and following logic. A key reason is that natural-language statements often carry implicit semantic relations before any formal reasoning begins. If these hidden meanings are not properly organized, the model may reach incorrect conclusions even when the subsequent reasoning process appears logically valid. Existing methods improve reasoning through decomposition, symbolic translation, external solvers, or self-verification, but pay comparatively less attention to the semantic structure on which reasoning depends. In this paper, we further investigate how semantic organization influences logical reasoning in LLMs. To this end, we propose HexLogicAgent, a framework that first organizes the meaning of natural-language statements and then guides logical reasoning through structured verification. In our investigation, we also make two observations. First, incomplete semantic representations, rather than deductive inference itself, are a major source of logical reasoning failures in LLMs. Second, explicitly modeling the complete structure of semantic opposition substantially delays the degradation of reasoning performance as logical complexity increases. Experiments on challenging logical reasoning benchmarks demonstrate that HexLogicAgent consistently improves reasoning reliability across multiple LLMs. The core idea is supported by a logical hexagon theory, which explains why a complete structure of opposing meanings is necessary for reliable reasoning.

---


### 34. [Leveraging External Knowledge for Historical Document Restoration via Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2607.21936)

**<font color=#1a73e8>作者：</font>** Gabeen Kim, Kyeongpil Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Historical documents act as invaluable knowledge archives but often suffer from illegibility due to physical deterioration and damage. While existing restoration methods based on masked language modeling effectively utilize local context, they struggle to restore named entities that require external historical knowledge. To address this limitation, we introduce a novel framework for historical document restoration that leverages large language models with retrieval-augmented generation (RAG). By combining the implicit knowledge of pre-trained LLMs with explicitly retrieved external context, our model ARI effectively mitigates the challenge of inferring context-dependent proper nouns. Extensive experiments on Korean historical documents demonstrate that our approach significantly outperforms baselines, achieving substantial gains in restoring both general characters and named entities. Furthermore, comprehensive evaluations including expert assessments confirm that ARI serves as a practical tool for domain experts, promising to accelerate the analysis of historical records.

---


### 35. [Low-Altitude Channel Multipath Prediction via Panoramic Perception and Vision-Language Model](https://arxiv.org/abs/2607.21953)

**<font color=#1a73e8>作者：</font>** Zihang Zeng, Shu Sun, Meixia Tao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) communication is expected to support a wide range of low-altitude applications in 6G mobile networks. However, traditional statistical channel models provide limited accuracy in specific environments, while deterministic methods such as ray tracing usually rely on accurate three-dimensional environment models and involve high computational complexity. Existing multimodal channel prediction approaches mainly focus on large-scale metrics such as path loss, and remain insufficient for modeling small-scale parameters. To address these limitations, this paper proposes PanoLAMP, a Panoramic perception and vision-language model-based Low-Altitude Multipath Prediction framework. It adopts a pretrained vision-language model as the backbone and captures the propagation environment features through panoramic RGB-D observations collected at both the transmitter and receiver to predict the delay, power, azimuth angle, and zenith angle offset relative to the line-of-sight path. Experiments are conducted on a synthetic dataset containing 18,949 UAV-vehicle links across seven UAV altitudes. Experimental results show that the proposed method consistently outperforms representative baselines in both multipath parameters and statistical metrics, and demonstrates stronger generalization across different flight heights.

---


### 36. [On Improving Faithfulness of Podcasts from Documents](https://arxiv.org/abs/2607.21961)

**<font color=#1a73e8>作者：</font>** Soumya Dutta, Tejas Indulal Dhamecha, Pannaga Shivaswamy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate long-form conversational content such as podcasts from textual sources. While these systems produce fluent and engaging narratives, they often introduce ungrounded information. In this work, we present the first systematic study of faithfulness in document-grounded podcast generation, where grounding must be maintained across conversational turns in long-form, multi-speaker transcripts. We construct a dataset of over 1500 documents spanning five domains and generate podcast transcripts using multiple LLMs. We introduce a turn-level LLM-as-a-judge framework for evaluating whether conversational turns are supported by the source document, and validate its reliability through human studies. Our analysis shows that even state-of-the-art models, including GPT-4o, frequently generate ungrounded content. To mitigate this issue, we propose catch-n-repair, a model-agnostic framework that detects and rewrites unfaithful conversational turns while preserving conversational flow. Experiments demonstrate consistent improvements in faithfulness across both in-domain and out-of-domain settings.

---


### 37. [Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning](https://arxiv.org/abs/2607.21971)

**<font color=#1a73e8>作者：</font>** Shujin Wu, Cheng Qian, Xiusi Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling through iterative self-evolution with environment feedback, as demonstrated by AlphaEvolve, shows remarkable performance gains. We hypothesize that the success of such evolution frameworks hinges on meta-skills, such as self-reflection with environment feedback, that enable effective multi-round refinement, yet are largely neglected by traditional post-training. To bridge this gap, we present MetaEvolve, a framework designed to develop these meta-skills via a data synthesis pipeline, evolution-aware reinforcement learning (RL), and inference-time evolutionary search. Concretely, we ground MetaEvolve in coding, where program execution provides natural, continuous reward signals beyond binary correctness. Building on these signals, we synthesize evolution trajectories as training data, each containing a current program, its fitness score (combining correctness and efficiency), and a history of prior attempts, and train the model via RL with verifiable rewards derived from test case execution. By training on large-scale code data, we aim to inspire generalizable domain-agnostic meta-skills that can transfer broadly to open-ended problems where such rich training signals are scarce. Across seven coding benchmarks, MetaEvolve outperforms the strongest baseline by 10.01% absolute on in-distribution tasks and 24.12% on out-of-distribution tasks. On open-ended algorithm optimization problems entirely outside the training domain, it further achieves a 46.9% relative improvement. These results demonstrate that explicitly cultivating self-evolution meta-skills offers a principled path toward more capable and autonomously self-evolving AI.

---


### 38. [Rethinking Layer-Wise Information Allocation for Vision Foundation Model Adaptation](https://arxiv.org/abs/2607.21973)

**<font color=#1a73e8>作者：</font>** Yuqi Li, Xi Xiao, Yunbei Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models are increasingly reused as frozen backbones for downstream visual recognition, making parameter-efficient adaptation a central problem. Prompt-based adaptation, including Visual Prompt Tuning (VPT), provides a lightweight way to specialize these models, but its layer-wise behavior remains poorly understood: performance is sensitive to prompt depth, placement, and task distribution, and gains on standard in-domain benchmarks do not always translate into robust generalization. We argue that this limitation is not solely an optimization issue, but a layer-wise information allocation issue: existing prompt-based methods lack principled control over what prompt-conditioned representations should preserve, suppress, and propagate across depth. Inspired by the Information Bottleneck principle, we introduce Prompted Information Bottlenecks (PIB), a framework that regularizes layer-wise compression-sufficiency trade-offs and promotes a more coherent cross-layer information path. The key idea is that effective adaptation should be minimal yet sufficient, retaining task-relevant local evidence in earlier layers while progressively discarding nuisance factors and redundant details in deeper layers. Extensive experiments show that PIB achieves strong performance across 34 datasets, reaching 92.1% on FGVC, 93.01% on HTA, and 77.33% on VTAB-1k, while tuning only 0.35% parameters on average across the main settings. Beyond benchmark accuracy, PIB helps explain the non-monotonic behavior of prompt capacity scaling, reduces shortcut reliance, and improves robustness under distribution shift and fine-grained recognition settings. These results position PIB as both a practical method and an information-allocation perspective for adapting frozen vision foundation models. Our code is available at this https URL

---


### 39. [MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation](https://arxiv.org/abs/2607.21978)

**<font color=#1a73e8>作者：</font>** Qingyu Yang, Haonan He, Minglei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures have been widely adopted in large language models, yet parameter-efficient fine-tuning (PEFT) for MoE models remains underexplored. Existing PEFT methods for MoE either ignore router priors with uniform adapters, reducing efficiency and risking forgetting, or rely on static expert selection, limiting per-token capacity and cross-expert feature learning. In this paper, we make the first attempt to fine-tune MoE models with MoE-style low-rank adaptation: our method, entitled MoE$^2$-LoRA, deeply couples the pretrained expert specialization with task-specific adaptivity via a dual-channel Routing-Conditioned Projection (RCP) module, which reuses base router activations to inform LoRA routing. We further introduce a single global LoRA expert pool shared across all layers, enabling model-wide adaptation with emergent layer-wise affinities and balanced expert utilization. MoE$^2$-LoRA simultaneously benefits from the advantages of prior reuse, dynamic adapter routing, and model-wide knowledge sharing. Evaluated on multiple MoE backbones with varying scales and expert granularities, MoE$^2$-LoRA consistently achieves state-of-the-art downstream accuracy while retaining stronger general capabilities.

---


### 40. [Analysing Self-Harm Representations in Language Models: a Cross-Architecture Study](https://arxiv.org/abs/2607.21988)

**<font color=#1a73e8>作者：</font>** Luis Espinosa-Anke, Carla Perez-Almendros  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-harm content is particularly challenging to detect using NLP techniques, and is also a high-stakes task which requires the highest accuracy to enable timely intervention or flagging at-risk users. We therefore present an analysis of how LLMs represent such self-harm content, which has downstream applications in self-harm detection, LLM intervention and governance and policing. In this paper, we focus on two datasets and four models, and perform two main experiments: (1) We train and evaluate linear probes across all layers of each model on two self-harm datasets: X-Sensitive and SH-Detection. Across both corpora, self-harm information crystallizes in the final 3 - 7% of network layers (93 to 97% depth). (2) We extract contrastive self-harm directions and, after performing a normaliation step, we find that the most accurate probes are not necessarily the most linearly separable. In particular, we find Gemma-3-4B to represent this \textit{contrastive self-harm direction} in a slightly different, more intricate way than the other LLMs.

---


### 41. [Medical-Checklist: Assessing the Comprehension of Medical Images by Multimodal Models](https://arxiv.org/abs/2607.21998)

**<font color=#1a73e8>作者：</font>** Bannapol Limanond, Masanori Suganuma, Takayuki Okatani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces a new benchmark test, Medical-Checklist, for assessing medical multimodal models. The recent advancements in multimodal models have demonstrated significant potential in the field of medical vision-language tasks. However, it is becoming increasingly clear that evaluating these models' performance, whether they are applied to natural or medical images, is challenging. The critical question is whether the models can accurately understand an input image while associating it with relevant input text. To address this, Medical-Checklist imposes a binary test on the models: they are given an image and two captions, where one is correct and the other incorrect, and the model must select the correct one. The incorrect caption contains a single medical concept (word or phrase) that is inaccurately substituted from the correct caption. Although the task is simple, this simplicity enables the unified assessment of diverse multimodal models designed and learned on different principles. It also enables us to verify whether models correctly understand a wide range of medical concepts across various medical sub-domains. Medical-Checklist is designed to reduce potential biases in data and to enable evaluation of the models' ability to handle out-of-distribution inputs, which were difficult in existing datasets. When evaluating four state-of-the-art medical multimodal models with Medical-Checklist, it was revealed that despite their excellent performance in specific tasks such as Med-VQA, they may not correctly understand images, suggesting a long journey ahead for clinical application. The dataset and code will be made public upon acceptance.

---


### 42. [Visual Saliency Steering Distillation for Multimodal Chain-of-Thought Reasoning](https://arxiv.org/abs/2607.22013)

**<font color=#1a73e8>作者：</font>** Hao Yang, Jin Wang, Xuejie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal chain-of-thought (CoT) reasoning integrates visual and textual cues through step-by-step inference. In small models with limited token budgets, modality-interaction fusion often suppresses tiny cross-modal differences. In particular, multimodal CoT often struggles when different images pair with identical text or different texts pair with an identical image, making such inputs nearly indistinguishable after fusion. This study proposes Visual Saliency Steering Distillation (VSSD). VSSD leverages the attention maps of multimodal large language models to generate perturbed images that capture task-sensitive feature directions, and then applies singular value decomposition to extract dominant steering vectors to guide inter-layer distillation. Experiments on ScienceQA and M$^3$CoT demonstrate that VSSD improves rationale generation and answer inference. The code is available at this https URL.

---


### 43. [Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents](https://arxiv.org/abs/2607.22014)

**<font color=#1a73e8>作者：</font>** Suman Navaratnarajah, Taehyoung Kim, Jona Ruthardt 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are emerging as core reasoning modules for embodied agents, yet it remains unclear how well general-purpose models can solve long-horizon embodied tasks from a single high-level instruction. We introduce MissionBench, a benchmark for mission-level evaluation of MLLMs in aerial 3D environments. It comprises 120 missions across five simulated 3D environments and four task families. Agents must autonomously plan, navigate, and report outcomes using only egocentric observations and its action history, without aerial-specific fine-tuning. Across 22 open- and closed-source MLLMs, the strongest model succeeds on fewer than 35% of missions compared to 84.4% human performance, highlighting the difficulty of multi-step embodied tasks. Despite large variations between model families, we observe gains from scaling, indicating that larger general-purpose models possess stronger zero-shot embodied capabilities. Our analysis shows that mission-level competence requires coordinating multiple capabilities beyond spatial perception, including multi-step planning and adaptive reasoning. This motivates closed-loop evaluation and highlights both the promise and risk of scaling-driven improvements for embodied AI.

---


### 44. [DWT-Fusion: A Signal-Based Framework for Training-Free LLM-Generated Text Detection](https://arxiv.org/abs/2607.22026)

**<font color=#1a73e8>作者：</font>** Mehmet Batuhan Özdaş, Murat Osmanoğlu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting LLM-generated text remains challenging under zero-shot and training-free conditions, especially when detectors must generalize across datasets, domains, and unseen generators. While existing training-free approaches exploit language-model statistics as detection signals, they typically characterize a text through global measures that summarize overall model behavior. Consequently, potentially informative local and multiscale variations in token-level predictability may remain underutilized. Motivated by this observation, we introduce DWT-Fusion, a training-free signal-based framework for detecting LLM-generated text using discrete wavelet analysis of token-level log-probability sequences produced by a proxy causal language model. The proposed framework analyzes these sequences through wavelet-based multiresolution signal representations and derives detection signals from localized probability dynamics. We further evaluate four training-free voting variants, including equal-weight hard voting, equal-weight soft voting, calibration-weighted hard voting, and calibration-weighted soft voting, to combine multiple wavelet configurations without training a supervised meta-classifier. We evaluate the framework on HC3, M4, and MAGE using GPT-Neo-2.7B, GPT-J-6B, Falcon-7B, and LLaMA-3-8B as proxy models. The best single wavelet configurations achieve AUROC values of 0.9872, 0.8185, and 0.7138 on HC3, M4, and MAGE, respectively. With calibration-weighted voting, the best ensemble variants further improve AUROC to 0.9919, 0.8477, and 0.7471. These findings show that DWT-based multiresolution scoring and calibration-guided voting fusion provide effective and interpretable signals for training-free LLM-generated text detection.

---


### 45. [Small Vision-Language Models Know When They Are Wrong But Cannot Say So: A Two-Model Study of Stated versus Internal Confidence Under Realistic Image Degradation](https://arxiv.org/abs/2607.22034)

**<font color=#1a73e8>作者：</font>** M M Asif Ferdous  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly deployed on consumer hardware where input images are degraded by compression, camera shake, and poor lighting. In such settings, a reliable uncertainty signal matters more than raw accuracy, because it determines when a system should defer rather than answer. We evaluate two small open-weight VLMs -- Qwen2-VL-2B-Instruct and SmolVLM-Instruct -- across six realistic photographic degradations at three severity levels, comparing two confidence signals: the confidence the model states in natural language, and the model's own mean token probability over its generated answer. Across 3,800 predictions, we find a large and consistent gap. Verbalized confidence in Qwen2-VL is almost constant (mean 0.87-0.90 across all conditions) and detects its own errors at chance level (AUROC 0.39-0.75, typically ~0.50), while internal token probability from the same model separates correct from incorrect answers with AUROC 0.92-0.99. In SmolVLM, verbalized confidence proved largely unobtainable: across three prompt templates, only one of five pilot attempts produced a parseable confidence value, while internal probability again yielded above-chance error detection (AUROC 0.54-0.92). Both models fail in the same place: under severe underexposure, accuracy collapses (0.99->0.22 for Qwen2-VL, 0.97->0.42 for SmolVLM) while both confidence signals barely move, and internal error-detection falls to chance. We conclude that small VLMs encode usable self-knowledge that their verbalized output does not express, that internal probability is therefore the better deferral signal in constrained deployment, and that neither signal should be trusted under severe low-light conditions.

---


### 46. [DCS: A Unified Conditional Sensitivity Framework for Cross-Modal Copyright Infringement Detection](https://arxiv.org/abs/2607.22035)

**<font color=#1a73e8>作者：</font>** Xiafeng Man  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Currently, most foundation models can reproduce or strongly depend on copyrighted training content, but output similarity alone is insufficient for infringement detection, because similar outputs may also arise from public-domain concepts, common stylistic conventions, or ordinary statistical generalization.
In this paper, we develops a unified post-hoc detection framework that treats copyright infringement evidence as a counterfactual conditional distribution shift: a protected target is suspicious when the model's behavior under aligned conditions would change measurably if that target were included in, or removed from, the training process.
We formalize this view through conditional differential privacy and introduce Dual-Branch Conditional Sensitivity (DCS), an operational statistic that measures the observable gap between two locally perturbed model states. Specifically, the proposed DCS framework creates a learning branch and an unlearning branch around the deployed model, connects their displacement to the unavailable counterfactual retraining effect through influence-function analysis, and bounds the observable sensitivity by the counterfactual privacy-budget surrogate, local curvature, training-set scale, and perturbation step size. To distinguish target-specific memorization from generic fine-tuning instability, we further define a calibrated detection statistic that subtracts the sensitivity measured under orthogonal conditions.
The DCS framework is instantiated for ridge-regularized linear regression, conditional diffusion models, autoregressive language models, and multimodal models. These instantiations show how the same principle can be evaluated through prediction gaps, image-embedding divergence, token-distribution or entropy shifts, and cross-modal representation changes.

---


### 47. [Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement Learning Mitigates Task Conflicts in LLMs](https://arxiv.org/abs/2607.22039)

**<font color=#1a73e8>作者：</font>** Zixuan Ren, Jinliang Lu, Junhong Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model merging plays a crucial role in consolidating multiple specialized models into a single, unified model, especially in the era of large language models (LLMs). Recent research has primarily focused on developing strategies to enhance merging performance with the trained models, while the impact of training paradigms, such as supervised fine-tuning (SFT) and reinforcement learning (RL), on the effectiveness of model merging remains underexplored. In this study, we systematically explore the merging behavior of RL-trained LLMs compared to those trained with traditional SFT. Through comprehensive evaluations across five representative tasks, we find that RL significantly reduces task conflicts and results in less performance degradation after merging, making RL-trained models particularly well-suited for this process. To unearth the reasons behind the superior suitability of RL for model merging, we conduct extensive empirical experiments and theoretical analyses. Our findings highlight three key factors: (1) On-policy training data in RL control the gradient updates in a smaller magnitude, reducing the risk of overwriting existing knowledge for other tasks in the model. (2) The RL optimization objective, which favors ``\textit{enough is as good as a feast}", progressively reduces the magnitude and the number of conflict parameter updates as the model converges. (3) Joint optimization of positive and negative examples in RL steers the model towards an unbiased task-specific parameter subspace, ensuring robust performance while further preventing parameter conflicts.

---


### 48. [Developing and Validating the Spanish Version of the Large Language Models Dependency Scale (LLM-D12-SP)](https://arxiv.org/abs/2607.22041)

**<font color=#1a73e8>作者：</font>** Tran Gia Bao, Mo El-Haj, Sameha Al-Shakhsi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There is a growing need for reliable and culturally validated instruments to assess psychological dependency on large language models (LLMs), particularly as LLMs are increasingly used for task execution, decision-making, and communication in organizational and work-related settings. This need is especially relevant for Spanish-speaking populations, where LLM adoption is rapidly expanding, yet validated psychometric tools remain scarce. The present study reports the first validation of the Spanish version of the Large Language Model Dependency Scale (LLM-D12-SP), extending prior validations conducted in English- and Arabic-speaking samples. The LLM-D12 is a two-dimensional instrument assessing Instrumental Dependency (reliance on LLMs for performing tasks and supporting decisions) and Relationship Dependency (psychological reliance on LLMs for companionship and social interaction). A total of 386 Spanish-speaking participants (M = 28.0 years, SD = 6.1; 55% male) completed the LLM-D12-SP. Confirmatory factor analysis supported the original two-factor structure. The scale demonstrated good internal consistency (Cronbach's alpha = 0.89 total; 0.86 Instrumental; 0.85 Relationship). Discriminant validity analyses indicated that the two subscales represent related but distinct constructs. External validation showed that both dependency dimensions were positively associated with internet addiction and perceived trustworthiness of LLMs, while showing weak or no association with need for cognition. Together with prior English and Arabic validations, these findings establish cross-linguistic support for the scale's structure and provide a psychometrically sound tool for investigating psychological aspects of LLM use in organizational contexts.

---


### 49. [Scaling Native Multimodal Pre-Training From Scratch](https://arxiv.org/abs/2607.22043)

**<font color=#1a73e8>作者：</font>** Haoyuan Wu, Aoqi Wu, Hai Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although large language models (LLMs) exhibit remarkable reasoning capabilities, their reliance on text-only pre-training restricts the perception of the multimodal physical world. Native multimodal pre-training avoids this limitation by training models from scratch on multimodal inputs, thereby achieving deep cross-modal integration and mitigating optimization asymmetries inherent to traditional late-fusion architectures. Despite these advantages, the scaling properties of this paradigm remain systematically uncharacterized. To address this gap, we investigate the optimal model size and token count for training a transformer-based vision-language model under a fixed computational budget. We demonstrate that minimal objective loss adheres to a predictable compute law, whereas compute-optimal model sizes and token counts scale as power laws. Notably, language and multimodal objectives manifest distinct scaling behaviors. The language allocation law is largely invariant to the composition of the data, indicating stable language learning regardless of the multimodal data ratio. Conversely, the multimodal allocation law is highly sensitive to this composition. Specifically, text-heavy mixtures become compute-efficient only at larger model scales, shifting the optimal resource allocation toward greater model capacity. Additionally, by modeling the influence of data composition on compute laws and allocation exponents, we derive an efficiency frontier specifying precise configurations of model size, token count, and data mixture. Downstream evaluations further reveal that native multimodal pre-training induces positive cross-modal transfer, thereby enhancing pure-text spatial reasoning and enabling robust multimodal in-context learning. In summary, this empirical research establishes the essential groundwork for predictably scaling multimodal foundation models.

---


### 50. [Benchmarking Fine-tuning and Retrieval Strategies for a Multimodal Language Model on the NRC Reactor Operator Licensing Examination](https://arxiv.org/abs/2607.22067)

**<font color=#1a73e8>作者：</font>** Isak Hwang, Yoon Pyo Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The integration of large language models (LLMs) into the nuclear power industry requires outputs grounded in domain-specific knowledge. This study evaluates a 31-billion-parameter open-weight multimodal model (Gemma 4 31B-IT) on its capacity to apply nuclear knowledge by benchmarking eight model-retrieval configurations against the U.S. Nuclear Regulatory Commission (NRC) Reactor Operator licensing examination. We evaluate 14 Generic Fundamentals Examinations (GFE) from the 2015-2021 March sittings (seven pressurized and seven boiling water reactor exams) using the standard 80% human passing criterion. The base model is compared against configurations utilizing supervised fine-tuning (SFT) on Gemini-distilled chain-of-thought (CoT) rationales, retrieval-augmented generation (RAG) with BM25 sparse retrieval over the U.S. Department of Energy Fundamentals Handbook, and retrieval-augmented fine-tuning (RAFT). Within the retrieval pipeline, we compare fixed-size sliding-window chunking against structure-aware chunking. The SFT configuration with fixed-size chunking RAG met the criterion on 8 of the 14 examinations, outperforming all alternatives, whereas no configuration without fine-tuning passed any. Aggregate accuracy reached 79.7%, with a confidence interval spanning the threshold, and 80.2% on PWR items specifically. Furthermore, two regularities emerged: the preferred chunking strategy reverses depending on the model's training state, and RAFT underperforms compared to standard SFT in matching search environments. These results demonstrate which combination of fine-tuning and search approaches achieves operator-level capabilities.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-80](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
