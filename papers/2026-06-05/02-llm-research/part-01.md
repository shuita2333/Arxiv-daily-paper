# 🧠 大模型相关研究 | 2026年06月05日

> 本类共 **137** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-137](./part-03.md)

---

### 1. [Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification](https://arxiv.org/abs/2606.04037)

**<font color=#1a73e8>作者：</font>** Thanh Luong Tuan, Abhijit Sanyal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pre-deployment verification of enterprise artificial intelligence (AI) agents remains a critical gap between large language model (LLM) capability benchmarking and production deployment. Post-deployment monitoring, human-in-the-loop controls, and prompt-level guardrails offer limited assurance once an agent is operating in production. We propose an ontology-grounded verification framework combining three components: an Agent Operational Envelope formalizing the certification space across permissions, domain constraints, safety properties, governance rules, and autonomy levels; an ontology-to-scenario generation pipeline that derives regulatory, operational, and adversarial test scenarios automatically; and a Trust Certificate carrying a machine-verifiable attestation with graduated deployment verdicts (Approved, Conditional, Rejected). A controlled pilot across four regulated industries (Fintech, Banking, Insurance, and Healthcare), instantiated as five industry-by-regulatory-regime cells across the United States and Vietnam, generated 1,800 scenarios evaluated against 125 primary-source regulatory requirements and 25 injected faults. Ontology-grounded generation (G4) achieved 48.3% regulatory coverage versus 33.1% for the persona-based baseline (corrected p = .0006) and the highest domain specificity (4.77/5.0; p = 2e-6). The coverage advantage over baseline and retrieval-augmented prompting was not robust after Bonferroni correction. Cross-validation across three LLM families (Claude Sonnet 4, Qwen 2.5 72B, Gemma 4 26B; 5,400 total scenarios) replicated the persona-versus-ontology pattern. The results establish ontology-grounded scenario generation as a credible complement to persona-based test suites for regulatory-intensive domains.

---


### 2. [LiftQuant: Continuous Bit-Width LLM via Dimensional Lifting and Projection](https://arxiv.org/abs/2606.04050)

**<font color=#1a73e8>作者：</font>** Liulu He, XuanAng Liu, Juntao Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing quantization methods are fundamentally limited by rigid, integer-based bit-widths (e.g., 2, 3-bit), resulting in a ``deployment gap" where Large Language Models cannot be optimally fitted to specific memory budgets. To bridge this gap, we introduce LiftQuant, a novel framework that enables continuous bit-width control for true Pareto-optimal deployment. The core innovation is a ``lift-then-project" mechanism which approximates low-dimensional weight vectors by projecting a simple 1-bit lattice from a higher-dimensional ``lifted" space. Crucially, the effective bit-width is determined simply by the ratio of the lifted dimension to the original dimension, which allows the bit-width to be tuned quasi-continuous as the dimension is a flexible structural parameter. This projection generates a structured yet non-uniform codebook, capturing the expressive power of Vector Quantization (VQ). While beneficial over VQ, LiftQuant's decoding path relies solely on linear transformations and 1-bit uniform quantizers, retaining hardware-friendly nature. This flexibility is transformative: LiftQuant enables a 70B LLM to be compressed to 2.4 bits to precisely fit a 24GB GPU, where its performance significantly surpasses state-of-the-art 2-bit models fitted on the same device. Our code and ckpt is available at this https URL.

---


### 3. [RUBAS: Rubric-Based Reinforcement Learning for Agent Safety](https://arxiv.org/abs/2606.04051)

**<font color=#1a73e8>作者：</font>** Xian Qi Loye, Qinglin Su, Zhexin Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The evolution of LLMs into tool-enabled agents creates a new class of safety challenges associated with real-world execution rather than simple text generation. Existing alignment methods often rely on coarse refusal signals or static supervision, making it difficult to balance safety with useful tool execution across diverse agentic risks. We introduce RUBAS, a rubric-based reinforcement learning framework for agent safety. RUBAS decomposes agent behavior into four dimensions: tool-use safety, argument safety, response safety, and helpfulness. These structured rubrics provide fine-grained and interpretable rewards over complete agent trajectories, enabling reinforcement learning to optimize safe tool use while preserving task completion. Extensive experiments across multiple agent safety benchmarks and models show that RUBAS improves safety over standard alignment baselines, reduces tool-grounded hallucinations, and maintains competitive utility. Our results suggest that multi-dimensional rubric rewards provide an effective training signal for aligning LLM agents in safety-critical tool-use settings.

---


### 4. [LLM Compression with Jointly Optimizing Architectural and Quantization choices](https://arxiv.org/abs/2606.04063)

**<font color=#1a73e8>作者：</font>** Hoang-Loc La, Truong-Thanh Le, Amir Taherkordi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying large language models (LLMs) is challenging due to their significant memory and computational requirements. While some methods address this by developing small or tiny language models from scratch, these approaches demand extensive GPU training. Compressing pre-trained LLMs for edge devices offers a compelling alternative. Beyond pruning and quantization, Neural Architecture Search (NAS) enables effective compression, yet prior NAS approaches often limit the search space and decouple architecture from quantization. We introduce a differentiable NAS framework that explores the entire space and jointly optimizes architectural configurations alongside mixed-precision quantization for linear layers of LLMs. Experiments demonstrate superior accuracy-latency trade-offs: our models achieve up to 1.4x faster inference than sequential NAS-then-quantization baselines at comparable accuracy, or up to 6% higher average accuracy across seven reasoning tasks at equivalent latency.

---


### 5. [Large Language Models Hack Rewards, and Society](https://arxiv.org/abs/2606.04075)

**<font color=#1a73e8>作者：</font>** Wei Liu, Xinyi Mou, Hanqi Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a dominant post-training paradigm, enabling large language models (LLMs) to learn from rewards. We observe that societal regulations are structurally similar to reward functions. They define measurable outcomes, thresholds, and exceptions, while often leaving institutional intent only partially specified. We hypothesise that the RL training process may exploit these gaps and therefore ask whether models' well-known tendency to hack reward functions during RL can scale into a more consequential failure mode named societal hacking: discovering loopholes in the rules society runs on. To study this phenomenon, we introduce SocioHack, a sandbox of 72 societal environments, and find that within these environments, reward hacking naturally emerges and leads to regulatory loophole discovery. Models learn to hack the social rules and generate strategies that remain technically compliant while defeating regulatory intent, and current LLM safeguards provide only limited mitigation. Therefore, collecting in-the-wild feedback for model training requires greater caution, and we need a next-generation post-training paradigm for safely iterating LLMs in real society.=

---


### 6. [Discourse-Role Labels as Presentation-Time Variables for Context Use in Language Models](https://arxiv.org/abs/2606.04109)

**<font color=#1a73e8>作者：</font>** Jianguo Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context-augmented language model systems often wrap supplied content with labels such as Reference:, Evidence:, Instruction:, Note:, or Example:, but the effect of these labels on reader-model behavior remains underexplored. We introduce a paired fixed-content probe over 500 MMLU-Pro items: each item receives the same misleading answer-bearing assertion under different discourse-role labels, and adoption is measured by whether the model outputs the injected wrong option. Across GPT-5.5, DeepSeek V4 Pro, Llama-3-8B-Instruct, and Qwen2.5-7B-Instruct, Misleading Adoption Rate shifts by 56-84 percentage points. Binding or source-like labels such as Instruction: and Reference: produce high adoption, whereas Example: consistently suppresses it. Paired tests, bootstrap intervals, final-instruction ablations, and Qwen final-step log-probability probes support a label-conditioned candidate preference. Boundary probes show where the effect weakens or persists: arithmetic tasks reduce adoption, passage-shaped external context preserves smaller label gaps, short-answer evaluation rules out option-letter copying, and nested-label conflicts suggest that illustrative framing can delimit adoption scope. A 200-case single-author manual audit confirms that the short-answer contrasts are stable under conservative adjudication. The resulting claim is bounded but practical: context-utilization and reader-side RAG benchmarks should report and control wrapper labels, because presentation choices can change measured reliance on supplied context.

---


### 7. [dMX: Differentiable Mixed-Precision Assignment for Low-Precision Floating-Point Formats](https://arxiv.org/abs/2606.04115)

**<font color=#1a73e8>作者：</font>** Giuseppe Franco, Ian Colbert, Pablo Monteagudo-Lago 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantizing large language models (LLMs) to low-precision floating-point representations is central to efficient deployment, yet applying a single bit-width uniformly across all layers is sub-optimal in terms of both performance and accuracy. This work introduces dMX, a differentiable mixed-precision quantization framework for learnable floating-point bit-width assignment. We study its application for the microscaling floating-point (MXFP) family of data types defined by the Open Compute Project (OCP) standard. The per-layer bit-width assignment is formulated as a continuous optimization problem in which each layer's floating-point format format is parameterized by a scalar parameter, folding the multi-variate design space into a single learnable offset. During training this offset takes continuous values, avoiding sudden oscillations between discrete quantization formats. A temperature-based annealing schedule progressively discretizes the learned offsets, ensuring that the final configuration maps to hardware-compatible MXFP formats without abrupt transitions between training and inference behavior. A target-aware regularization term steers the average bit-width toward a user-specified budget, serving as a coarse-grained proxy for inference cost and balancing model quality against deployment efficiency. We performed experiments on different families of LLM, such as Llama, Qwen3, and SmolLM2, evaluating perplexity on WikiText-2 and accuracy on four zero-shot reasoning benchmarks. Across these settings, dMX consistently yields Pareto-dominating models and improves over Kullback-Leibler (KL) divergence-based layer-selection heuristics, efficiently navigating trade-offs between model quality and average bit-width.

---


### 8. [Computational conceptual history of scientific concepts: From early digital methods to LLMs](https://arxiv.org/abs/2606.04118)

**<font color=#1a73e8>作者：</font>** Michael Zichert, Arno Simons  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This article situates large language models (LLMs) within the longer history of computational approaches to concept analysis in the history, philosophy, and sociology of science (HPSS). We examine what LLMs add to existing methods, how they inherit longstanding problems, and review recent case studies that employ them. In the first part, we reconstruct computational conceptual history before LLMs by bringing together three strands of work: early digital methods in HPSS, distributional approaches from digital history and related research, and lexical semantic change detection. We provide an overview of the main challenges and opportunities, focusing on corpus construction, operationalization and modelling choices, and evaluation and interpretation. In the second part, we turn to the era of LLMs, starting with a short introduction to LLMs before reviewing LLM-based work on lexical semantic change detection and relevant case studies in HPSS. We then revisit the earlier methodological questions, showing how issues of corpus construction, model choice and training data, operationalization trade-offs, and evaluation and interpretation play out in LLM-based workflows.

---


### 9. [When Retrieval Doesn't Help: A Large-Scale Study of Biomedical RAG](https://arxiv.org/abs/2606.04127)

**<font color=#1a73e8>作者：</font>** Erfan Nourbakhsh, Rocky Slavin, Ke Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical question answering is a high-stakes setting where factual errors can have serious consequences. Retrieval-augmented generation (RAG) is widely viewed as a promising solution, and prior work has reported substantial gains for large medical QA models. We revisit this assumption across a broad range of open-weight instruction-tuned models spanning 7B to 72B parameters. Across five models, ten biomedical QA datasets, four retrieval methods, and four retrieval corpora, we find that retrieval yields only small and inconsistent improvements over a no-retrieval baseline, typically within 1-2 points. In contrast, the choice of backbone model has a much larger effect than the choice of retriever or corpus, and expert and layman retrieval sources perform similarly in most settings. These results suggest that the main bottleneck is not retrieval quality alone, but the model's limited ability to use retrieved evidence effectively.

---


### 10. [EvalStop: Using World Feedback to Detect and Correct Reward Overoptimization in Multi-Tenant RLHF Platforms](https://arxiv.org/abs/2606.04145)

**<font color=#1a73e8>作者：</font>** Guilin Zhang, Chuanyi Sun, Shahryar Sarkani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cloud LLM fine-tuning platforms increasingly serve RLHF workloads, where a learned reward model is optimized as a proxy for human quality. As Gao et al. (2023) showed, this proxy diverges from world feedback (downstream eval metrics) under sustained optimization pressure, a phenomenon known as reward overoptimization. Existing platform schedulers ignore this divergence: non-clairvoyant schedulers optimize JCT without any quality signal, SLAQ-style quality-aware schedulers use training loss (a weaker proxy that drops monotonically through hacking), and classical per-job early stopping requires human monitoring and does not free shared GPUs. We propose EvalStop, a composable scheduling primitive that terminates jobs on k consecutive eval-score declines, releases GPUs, preserves the best checkpoint, and delegates to any base scheduler. We frame scheduler-level early stopping as a detection problem and evaluate it in a discrete-event simulator whose RLHF workload mixes reward-hacking and structurally healthy runs, with ground-truth labels hidden from schedulers. On RLHF-heavy workloads (80% RLHF, 64 GPUs), EvalStop achieves precision 98% / recall 99% / FPR 1.5% while improving JCT by 9% and cutting wasted compute by 22% over SRTF-Est (p<0.05). Trivial fixed-progress and loss-plateau competitors either incur 65% FPR on healthy RLHF or miss over half of true hacking cases. Gains compose across every base scheduler tested (9-25% JCT) and detection quality stays stable under eval noise (precision at least 91% at noise std <= 0.05) and hacking base rate (precision at least 89% across 20-80% hacking fractions).

---


### 11. [Thinking Through Signs: PEEL as a Semiotic Scaffolding for Epistemically Accountable AI-Enabled Research](https://arxiv.org/abs/2606.04152)

**<font color=#1a73e8>作者：</font>** Clarisse de Souza, Gabriel Barbosa, Simone Diniz Junqueira Barbosa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are reshaping research practice while quietly eroding researchers epistemic accountability. This commentary introduces PEEL - Protocols for Epistemically Engaged Literacy in AI, a working scaffolding that combines deterministic distant reading via Voyant Tools with LLM interpretation via Claude, grounded in Peircean semiotics and abductive reasoning. Applied to AI-generated condensations of three source texts, PEEL reveals systematic distortions in quantity, term frequency, and epistemic voice that are invisible without non-AI measurement -- and yields three design implications: deterministic instruments must accompany AI tools; fluency is not fidelity; epistemic authority must be designed in, not assumed.

---


### 12. [SocialCoach: Personalized Social Skill Learning with RL-based Agentic Tutoring and Practice](https://arxiv.org/abs/2606.04155)

**<font color=#1a73e8>作者：</font>** Tianfu Wang, Max Xiong, Jianxun Lian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social skills such as negotiation and leadership are crucial for personal and professional success in today's interconnected world. However, scalable and effective training remains a significant challenge due to the scarcity of expert coaching. In this paper, we introduce SocialCoach, a holistic LLM-powered agentic tutoring system for personalized social skill development at scale. First, SocialCoach automatically constructs a pedagogically-grounded, theory-to-practice knowledge corpus from diverse expert sources, leveraging a multi-agent pipeline. Second, to personalize the learning journey, it employs an adaptive practice scheduling module that follows a prescription-retrieval-adaptation process. To maximize the long-term learning experience while overcoming the cold-start problem, this policy is optimized within a learner simulation environment through reinforcement learning. Finally, SocialCoach integrates immersive, goal-driven practice, causality-driven proficiency assessment and knowledge-grounded, reflective tutoring to help address the knowing-doing gap. We deploy it in our product, EQoach, and conduct extensive experiments. The results show that SocialCoach improves simulated pathway quality and judge-rated tutoring quality over baseline approaches, while early user feedback indicates strong perceived engagement and usefulness. These findings suggest a practical architecture for personalized and gamified pedagogical platforms on soft skill learning.

---


### 13. [Expert-Aware Refusal Steering](https://arxiv.org/abs/2606.04160)

**<font color=#1a73e8>作者：</font>** Anna C. Marbut, Daniel R. Olson, Travis J. Wheeler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment in instruction-tuned large language models (LLMs) depends on a model's ability to reliably refuse to respond to harmful or disallowed requests. Recent work has shown that a steering vector can be applied to a dense LLM during inference to effectively suppress refusal behavior, inducing response to harmful requests. We extend this refusal steering method to three open-source Mixture-of-Experts (MoE) LLMs and find that steering performance is uninhibited by the complex routing patterns inherent to the MoE architecture. We then propose two expert-aware refusal steering methods that leverage refusal-specific expert routing patterns and expert-specific steering directions to suppress normal refusal behavior. We find that refusal behavior can be effectively steered based on the output of a single expert. Our results show that refusal signals captured by steering methods differ from expert routing behavior, suggesting a substantial role for attention in MoE refusal behavior.

---


### 14. [ADAPTOOD: Uncertainty-Aware Fine-Tuning for Out-of-Distribution ECG Time Series Models](https://arxiv.org/abs/2606.04164)

**<font color=#1a73e8>作者：</font>** Sotirios Vavaroutas, Yu Yvonne Wu, Ali Etemad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data samples used for training often differ from those encountered during fine-tuning and deployment, and while ML models show promise, their performance remains limited when only small annotated datasets are available. Performance often degrades under distribution shifts caused by diverse sensors, populations, and application settings. Although pre-training helps, models frequently encounter out-of-distribution (OOD) data in real-world settings, leading to reduced robustness. Existing adaptation methods usually assume fixed distribution shifts and struggle when multiple types or severities occur. In particular, they overlook shift severity, for example treating adaptation to a large familiar dataset the same as adaptation to a small dataset with a new task, which limits generalisation. To address this, we propose ADAPTOOD, a novel framework that leverages data uncertainty to quantify distribution shift severity and guide fine-tuning for time series. This uncertainty measures how strongly samples from the target deployment distribution deviate from the pre-training distribution, providing a direct signal of OOD severity. Our framework combines this uncertainty with low-rank model updates and adaptive hyperparameter optimisation to improve adaptation. We show that ADAPTOOD achieves up to 7% higher accuracy and 12.9% higher precision than existing methods in OOD tasks, maintaining strong performance as distribution shift severity increases.

---


### 15. [When Autoregressive Consistency Hurts Safety Alignment](https://arxiv.org/abs/2606.04168)

**<font color=#1a73e8>作者：</font>** Bochen Lyu, Yiyang Jia, Xiaohao Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models (LLMs) is fragile in part because it is often shallow: fine-tuning mainly reshapes the model's behavior near the first few output tokens. We argue that this phenomenon can be understood through autoregressive consistency, the tendency of next-token prediction to preserve and extend the current response trajectory consistently. By analyzing the learning dynamics of safety alignment, we show that autoregressive consistency can concentrate alignment updates on early tokens, offering a mechanistic explanation for shallow safety alignment. The same mechanism also predicts a broader class of attacks on LLMs: attacks that induce harmful continuation states at arbitrary positions in the output trajectory. As a concrete example, we introduce random insertion attack, which inserts a short harmful span into an otherwise safe refusal trajectory and exploits autoregressive consistency to sustain the resulting harmful branch, thereby bypassing safety alignment. Notably, a short harmful span can redirect the generation to be harmful even after a long refusal prefix, highlighting autoregressive consistency as a potential broader failure mechanism. This suggests that safety alignment should also break harmful autoregressive consistency throughout the output trajectory. We therefore propose adversarial safety alignment, an initial framework based on worst-case harmful continuation states, and instantiate it with random worst-insertion training. Overall, our results suggest that autoregressive consistency should be treated as a central consideration in both safety alignment and attack design.

---


### 16. [KODA: Contrastive Representation Comparison and Alignment for Vision-Language Foundation Models](https://arxiv.org/abs/2606.04180)

**<font color=#1a73e8>作者：</font>** Youqi Wu, Mohammad Jalali, Farzan Farnia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language foundation models such as CLIP and SigLIP provide widely used representations for multimodal learning systems. While these models are typically compared through downstream performance, such evaluations often do not explain how their representations differ structurally. In this work, we study this problem through the task of Contrastive Embedding Clustering: identifying sample subsets that are weakly clustered under one representation but strongly clustered under another. We propose \emph{Kernel Optimization for Discrepancy Analysis (KODA)}, a kernel-based framework for contrastive representation comparison and alignment. KODA constructs unified multimodal kernels through modality-wise kernel composition and formulates discrepancy discovery as a constrained optimization problem that searches for coherent structures in one representation while suppressing coherence in a reference representation. This yields interpretable discrepancy directions associated with specific sample subsets and modality interactions. To scale KODA to large vision-language datasets, we develop randomized low-dimensional approximations of joint kernels using random projections, including Random Fourier Features for shift-invariant kernels. Empirically, KODA identifies consistent and interpretable discrepancy structures across vision-language representations and provides sample subsets for representation alignment. The code is available at this https URL.

---


### 17. [GroupToM-Bench: Benchmarking Group Theory of Mind and Nonlinear Social Emergence in MLLMs](https://arxiv.org/abs/2606.04184)

**<font color=#1a73e8>作者：</font>** Weidong Tang, Jierui Li, Yueling Hou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> True general intelligence requires not only a model of the physical world but also a social world model: the capacity to infer how individual mental states interact and crystallize into group-level outcomes. Despite notable progress in individual-level Theory of Mind (ToM) reasoning, existing multimodal large language models fail at this broader task. Collective behavior emerges non-linearly from social tensions, conformity dynamics, and structural constraints, meaning it cannot be recovered by merely summing individual intentions. We present GroupToM-Bench, the first multimodal benchmark for group-level ToM, built around a causal chain spanning micro-level BDI states (belief, desire, intention), meso-level group tension and structural constraints, and macro-level outcome prediction and mechanistic attribution. To probe this full arc, we develop a seven-level cognitive audit framework. Experiments reveal a gap between current models and human baselines, highlighting a failure to process social structures and non-linear collective dynamics.

---


### 18. [Exploring the Topology and Memory of Consensus: How LLM Agents Agree, Fragment, or Settle When Forming Conventions](https://arxiv.org/abs/2606.04197)

**<font color=#1a73e8>作者：</font>** Aliakbar Mehdizadeh, Martin Hilbert  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> How much should an LLM agent remember, and how should multi-agent systems be connected when trying to reach consensus? We show these two design choices interact in a way that flips the sign of memory's effect on coordination. Across 432 simulation runs of a networked Naming Game on eight fixed 16-agent topologies, we vary memory depth and network structure. Longer memory slows the time to reach steady state in decentralized networks but accelerates it in centralized ones; the same parameter pushes the system in opposite directions depending on topology. Critically, "faster settling" in centralized networks means locking in to a fragmented plateau more quickly, not reaching system-wide consensus, which can be used to generate diverging opinions. We further document a memory-mediated speed-unity trade-off: centralized networks consistently preserve more competing conventions than decentralized networks, but their settling speed depends sharply on memory. At the agent level, within-network analyses show that high-betweenness bridges suffer a brokerage penalty while agents in locally clustered neighborhoods achieve higher coordination success. Finally, in search of analytically tractable generative mechanisms, we find that agents' choices are well captured by Fictitious Play, indicating belief-based rather than reward-based adaptation. The practical implication: memory depth and communication topology should be co-designed, not optimized in isolation.

---


### 19. [SMAC-Talk: A Natural Language Extension of the StarCraft Multi-Agent Challenge for Large Language Models](https://arxiv.org/abs/2606.04202)

**<font color=#1a73e8>作者：</font>** Joel Sol, Homayoun Najjaran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLMs become more widely deployed, they are increasingly expected to work alongside other AI agents rather than operating in isolation. Effective coordination in these settings requires agents to communicate, share information and make decisions under uncertainty. We introduce SMAC-Talk, a natural language extension of the StarCraft Multi-Agent Challenge for evaluating LLM-based agents in cooperative multi-agent environments. The environment has several key features such as decentralized control, partial observability and long-horizon decision making. SMAC-Talk includes a natural language communication channel which is used to probe agent coordination and trust. We use this communication channel to construct different evaluation scenarios, including settings with an embedded deceptive communicator that tries to disrupt and deceive allies through communication alone. We provide three agents for benchmarking using 4 models from the Qwen3.5 family and study how reasoning structure, memory and model scale affect coordination between agents. We release SMAC-Talk as an open benchmark to support the research community in developing and evaluating LLM agents in cooperative multi-agent settings.

---


### 20. [MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&A](https://arxiv.org/abs/2606.04231)

**<font color=#1a73e8>作者：</font>** Hanoz Bhathena, Parin Rajesh Jhaveri, Rohan Mittal 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal retrieval-augmented generation (MM-RAG) have shifted toward minimal parsing, relying on page-level images for producing retriever embeddings and for answer generation. While efficient, this trend often neglects explicit handling of the rich, structured information in complex enterprise documents, instead depending on pre-trained embeddings or vision-language models to implicitly capture such structure. In this work, we take a more direct approach: MM-BizRAG proactively extracts and represents document structure via a document structure-aware split that dynamically routes documents through orientation-specific ingestion pipelines, applying explicit layout-aware parsing for vertically structured documents (e.g., reports) and holistic page-level representations for horizontally structured documents (e.g., slide decks). A unified LLM-driven artifact transformation pipeline with placeholder-based positional alignment preserves natural reading order, while inference-time multimodal assembly decouples retrieval representations from generation context, enabling richer, more grounded answers without any finetuning requirement. Through experiments on a large, heterogeneous enterprise dataset and two public benchmarks (SlideVQA and FinRAGBench-V), MM-BizRAG consistently outperforms state-of-the-art vision-centric baselines by up to 32% points, with especially strong gains on report-style layouts. Furthermore, we introduce FastRAGEval, a single-call LLM Judge metric for fine-grained generative recall that halves RAGChecker's cost while achieving stronger human alignment.

---


### 21. [Supportive Token Revealing for Fast Diffusion Language Model Decoding](https://arxiv.org/abs/2606.04236)

**<font color=#1a73e8>作者：</font>** Giries Abu Ayoub, Mario Barbara, Lluís Pastor-Pérez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models can generate text efficiently by updating multiple masked positions in parallel, but this parallelism introduces a quality-latency trade-off. Aggressive decoding may commit mutually dependent tokens too early, while conservative decoding requires many denoising steps. Existing methods address this tension by deciding which tokens are safe to reveal using confidence or dependency criteria. However, avoiding unsafe commits does not necessarily make the remaining masked sequence easy to decode, since uncertain tokens may depend on masked tokens, creating a bottleneck for denoising steps. We propose AXON, a training-free module that can be added on top of existing parallel decoding strategies for diffusion language models. Rather than replacing the base decoder, AXON monitors the remaining uncertain masked tokens and intervenes only when their current state suggests that additional context is needed. It then shifts the criterion from which tokens are safest to reveal to which confident reveals would best support later denoising. AXON selects anchors, confident masked tokens that uncertain positions attend to, using attention, uncertainty, and confidence signals. Experiments on reasoning and code-generation benchmarks across multiple diffusion language models show that AXON improves the quality-latency trade-off of existing parallel decoders, often reducing the number of function evaluations while maintaining or improving accuracy.

---


### 22. [Recover-LoRA for Aggressive Quantization: Reclaiming Accuracy in 2-Bit Language Models via Low-Rank Adaptation with Knowledge Distillation on Synthetic Data](https://arxiv.org/abs/2606.04238)

**<font color=#1a73e8>作者：</font>** Devleena Das, Rajeev Patwari, Elliott Delaye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aggressive weight quantization to 2-bit precision offers substantial throughput and memory gains for large language model (LLM) inference, but typically incurs severe accuracy degradation. These gains are particularly relevant for edge and on-device deployment, where memory capacity and bandwidth are primary constraints. In this work, we extend Recover-LoRA -- a lightweight, data-free accuracy recovery method originally developed for general model weight corruption -- to the setting of ultra-low-bit quantization. We propose a selective mixed-precision strategy in which only gate and up projection layers of the MLP are quantized to 2-bit (W2), while all other linear layers remain at higher precision, yielding a mixed-precision GateUp configuration. We demonstrate via roofline analysis across three model families (4B--20B) and two hardware platforms that a W4/W2-GateUp deployment (4-bit base with 2-bit gate/up) delivers 7.5--23.3\% TPS improvement over uniform W4 depending on model and context length, while confining quantization error to a predictable subset of layers. We then apply Recover-LoRA -- training low-rank adapters on the quantized layers via logit distillation with synthetic data -- to recover accuracy lost from 2-bit quantization of the gate and up layers. In a case study on Qwen3-4B, Recover-LoRA achieves 80--95\% accuracy recovery on 9 of 12 benchmarks, using only 10k synthetic training samples and no labeled data. We further demonstrate that synthetic data performs comparably to curated labeled data for distillation-based recovery, and that recovery generalizes to out-of-distribution evaluation tasks. Our results present Recover-LoRA as a practical post-quantization accuracy recovery tool for aggressive weight compression in deployment settings.

---


### 23. [Overview of the EReL@MIR 2025 Multimodal Document Retrieval Challenge (Track 1)](https://arxiv.org/abs/2606.04240)

**<font color=#1a73e8>作者：</font>** Jingbiao Mei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval over visually-rich documents, pages that interleave text with figures, tables, and charts, is essential for multimodal retrieval-augmented generation, yet most retrievers still discard the visual channel. The \emph{Multimodal Document Retrieval Challenge}, Track~1 of the MIR Challenge at the first EReL@MIR workshop, co-located with The Web Conference 2025, asks participants to build a \emph{single} retrieval system that handles two complementary regimes: closed-set document page retrieval within long documents from a text query (MMDocIR), and open-domain retrieval of Wikipedia-style passages from an image or image-plus-text query (M2KR). Systems are ranked by the macro-average of mean Recall@$\{1,3,5\}$ over the two tasks. The challenge drew 455 entrants and 586 submissions across 22 teams. This report describes the challenge design, datasets, and evaluation protocol; reports the final standings; and analyses the three winning teams' systems. All three build on decoder-based Multimodal-LLM embedders from the Qwen2-VL family rather than on CLIP-style encoders, and differ chiefly in whether they reach the top through fine-tuned ensembles, training-free multi-route fusion with a strong vision-language re-ranker, or zero-shot late interaction. The training-free system finished within $0.1$ point of the fine-tuned winner.

---


### 24. [VAMPS: Visual-Assisted Mathematical Problem Solving Benchmark](https://arxiv.org/abs/2606.04244)

**<font color=#1a73e8>作者：</font>** Amirhossein Dabiriaghdam, Shayan Vassef, Mohammadreza Bakhtiari 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models are increasingly capable of complex reasoning, yet their performance often degrades when they must externalize a problem through a tool and then reason over the tool's output, specifically when they rely on visual aids. This gap is especially important because real engineering and scientific workflows often rely on visualization tools for analysis, validation, and decision-making. To study this discrepancy, we introduce VAMPS (Visual-Assisted Mathematical Problem Solving), a benchmark for graph-assisted mathematics. VAMPS contains 1,168 multimodal, bilingual multiple-choice question-answer pairs drawn from Iranian University Entrance Exam algebra and calculus problems and expanded with human-reviewed LLM-generated synthetic variants, all selected so that plotting provides a natural solution strategy by revealing intersections, extrema, asymptotes, etc. Designed for both benchmarking and diagnosis, VAMPS goes beyond prior multimodal benchmarks that primarily evaluate reasoning over fixed visual inputs by testing whether a model can benefit from constructing a useful graph and grounding its answer in the resulting visualization. Overall, we found that across a diverse set of models, direct analytical solving surprisingly outperforms tool-enabled visual solving, even on problems where plotting is a natural strategy.

---


### 25. [StepPRM-RTL: Stepwise Process-Reward Guided LLM Fine-Tuning for Enhanced RTL Synthesis](https://arxiv.org/abs/2606.04246)

**<font color=#1a73e8>作者：</font>** Prashanth Vijayaraghavan, Apoorva Nitsure, Luyao Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic generation of RTL code for digital hardware designs remains challenging due to long-horizon reasoning, multi-step dependencies, and strict correctness constraints in Verilog and VHDL. We present StepPRM-RTL, a novel framework that combines stepwise trajectory modeling, process-reward modeling (PRM), and retrieval-augmented fine-tuning (RAFT) to enhance both the functional correctness and reasoning fidelity of LLM-based RTL code generation. StepPRM-RTL constructs stepwise reasoning trajectories from canonical solutions, where each step contains a rationale and incremental code modification. A Process Reward Model (PRM) evaluates intermediate steps, providing dense feedback that guides reinforcement-style updates during RAFT fine-tuning. Monte Carlo Tree Search (MCTS) explores alternative reasoning paths, enriching the training dataset with high-quality trajectories. This integration of stepwise and outcome-aware rewards allows the model to learn both how and why to construct correct RTL, improving long-horizon reasoning beyond standard supervised or outcome-based training. Experimental evaluation on benchmark Verilog and VHDL datasets demonstrates that StepPRM-RTL outperforms the best prior methods by over 10\% in functional correctness and reasoning fidelity metrics. Ablation studies confirm that the combination of PRM-guided rewards and stepwise trajectory exploration is key to its performance. StepPRM-RTL generalizes across RTL languages and provides a scalable framework for high-fidelity, interpretable code generation, establishing a new standard for LLM-assisted hardware design automation.

---


### 26. [Can I Take Another Dose? Evaluating LLM Decision-Making Under Temporal Uncertainty in OTC Dosing QA](https://arxiv.org/abs/2606.04262)

**<font color=#1a73e8>作者：</font>** Maroof Kousar, Yibo Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for everyday health questions, including whether a user can safely take another dose of an over-the-counter (OTC) medication. Yet this common safety-relevant setting remains underexplored in existing medical QA evaluations, where correct answers require tracking dose timing, computing rolling 24-hour intake, following product-label constraints, and handling incomplete medication histories. We introduce DOSEBENCH, a focused benchmark of 81 curated OTC dosing scenarios focused on adult acetaminophen and ibuprofen use, with manually annotated gold references. We evaluate four LLMs across repeated runs using metrics for decision correctness, consistency, explanation verifiability, failure types, and confidence-related signals, resulting in 1,620 model responses. Our results show that models frequently struggle with rolling-window reasoning and ambiguity-sensitive cases and that stable or confident-looking responses can still violate dosing constraints. These findings suggest that OTC dosing QA provides a narrow yet practical testbed for evaluating temporal reasoning, constraint following, and safety-relevant uncertainty handling in medical QA.

---


### 27. [UniCanvas: A Diffusion-base Unified Model for Text-in-Image Joint Generation](https://arxiv.org/abs/2606.04264)

**<font color=#1a73e8>作者：</font>** Zeyuan Yang, Hao-Wei Chen, Xueyang Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent years have seen remarkable progress in unified vision-language models handling both multimodal understanding and generation within a single architecture. While autoregressive VLMs can reason across modalities, they fail to generate high-quality images. In contrast, diffusion models produce photorealistic visuals yet struggle to generate coherent text, making it challenging to develop a single unified model that can seamlessly handle both visual and text generation. Recent advances suggest that language can be effectively embedded within visual representations, allowing models to reason about textual semantics directly from images. To this end, we propose UniCanvas, a first attempt that unifies diffusion models to generate interleaved multimodal contents through text-in-image generation. Diffusion models naturally capture transformations on a shared pixel canvas, which can be viewed as world models of visual change. Instead of producing discrete text tokens, the model learns to represent language as visual patterns inside images, leveraging its inherent multimodal embedding space. This design allows the model to "draw" text naturally within a single pixel canvas during image synthesis, achieving seamless multimodal generation. Experiments demonstrate that UniCanvas improves performance over previous unified models, positioning text-in-image generation with diffusion models as a promising unified multimodal generation paradigm.

---


### 28. [RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training](https://arxiv.org/abs/2606.04272)

**<font color=#1a73e8>作者：</font>** Rachit Bansal, Clara Mohri, Tian Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The standard LLM training pipeline applies reinforcement learning (RL) only after pre-training and supervised fine-tuning (SFT). We question this status quo by training a LLM from scratch and applying RL, SFT, and SFT followed by RL directly to intermediate pre-training checkpoints. We find that RL is effective very early, and often matches the full SFT$\to$RL pipeline early as well. Through experiments on harder problems, we find that targeted pre-training data composition is a strong lever for RL effectiveness, even more so than model scale. Beyond reasoning accuracy, applying RL directly to base checkpoints expands the model's distribution; the sharpening effect reported in recent work arises only when RL follows SFT. The general capabilities of the model remain essentially unchanged by RL, while they degrade following SFT. Finally, we merge RL and SFT objectives by parallel averaging, which outperforms across all other training methods discussed, across metrics, while preserving general capabilities. Together, these results suggest that LLM training might benefit from an expanded use of RL.

---


### 29. [Long Live Fine-Tuning: Task-Specific Transformers Outperform Zero-Shot LLMs for Misinformation Response Classification on Reddit](https://arxiv.org/abs/2606.04274)

**<font color=#1a73e8>作者：</font>** JooYoung Lee, Lin Tian, Angela Brillantes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) become default tools for online information verification, an implicit assumption follows them: that scale and general capability are sufficient for nuanced classification of misinformation discourse. We test this assumption directly on 900 Reddit comments spanning three PolitiFact-verified misinformation claims (environment, health, immigration), labelled as belief (propagates the claim), fact-check (corrects it), or other. We compare nine models across three paradigms -- BART-MNLI, three Llama variants, three commercial frontier LLMs (Claude Haiku 4.5, Gemini Flash Lite 2.5, Claude Sonnet 4.6), and fine-tuned DistilBERT and RoBERTa -- under universal and topic-specific label schemas.
The assumption does not hold. Fine-tuned RoBERTa reaches 0.62 macro-$F_1$ against a best zero-shot result of 0.50 (Claude Haiku 4.5), at a fraction of the per-query cost; the supervised advantage is concentrated on the belief class, the implicit, affective category every zero-shot model under-detects. Scaling does not help: Llama-3-8B matches Llama-3-70B, and Claude Sonnet 4.6 underperforms the smaller Haiku under generic labels, collapsing belief detection to 0.17 and refusing outright on a subset of comments flagged as sensitive. This is a safety-alignment artefact, not a capacity limit. Label schema and topic jointly shape zero-shot performance, with the same model varying by more than 0.13 macro-$F_1$ across topics under matched labels. In a verification context, where missing belief is the costlier error, task-specific fine-tuning remains the more reliable choice despite the proliferation of large generative models.

---


### 30. [FindIt: A Format-Informed Visual Detection Benchmark for Generalist Multimodal LLMs](https://arxiv.org/abs/2606.04282)

**<font color=#1a73e8>作者：</font>** Eshika Khandelwal, Jingjing Pan, Mingfang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are predominantly evaluated on free-form vision-language tasks such as visual question answering, captioning, and summarization. However, their practical use is rapidly expanding to more structured computer vision settings, where users prompt models to perform localization-centric tasks such as object detection, often within larger agentic or decision-making systems. Despite this shift, there is currently no standardized benchmark that systematically evaluates these capabilities at scale. In this work, we introduce the first comprehensive benchmark specifically designed to assess the promptable localization abilities of generalist MLLMs. Our benchmark spans four core task categories: object detection, referring expression detection, instance-level detection, and video-based detection. To enable consistent and fair evaluation, we develop a unified framework that standardizes inputs, enforces parsable bounding box outputs, and defines transparent evaluation protocols across tasks. Using this suite, we evaluate a diverse set of open-source and proprietary MLLMs, providing an in-depth analysis of their performance and limitations. Beyond accuracy, we examine models' ability to adhere to output format specifications, showing that current systems are highly sensitive to formatting constraints and often fail to generalize even to minor variations. Our results highlight both the strengths and shortcomings of state-of-the-art MLLMs in localization settings, and point toward important directions for improving multimodal model design and evaluation.

---


### 31. [Sparse Mixture-of-Experts Reward Models Learn Interpretable and Specialized Experts for Personalized Preference Modeling](https://arxiv.org/abs/2606.04284)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Jinyi Mu, Mayank Jobanputra 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference modeling plays a central role in reinforcement learning from human feedback (RLHF), enabling large language models (LLMs) to align with human values. However, most existing approaches assume a universal reward function, neglecting the diversity and heterogeneity of human preferences. To address this limitation without additional annotation costs, recent work has proposed learning multiple preference components from binary data and combining them to model individual preferences. Nevertheless, these components often fail to capture coherent and disentangled patterns, limiting their interpretability and effectiveness for personalization. In this work, we propose a sparse Mixture-of-Experts (MoE) reward model that encourages sparse routing and expert diversity during training on binary preference data. Across controlled and real-world experiments, sparse MoE learns interpretable routing patterns and specialized experts. It also improves test-time personalization, and post-adaptation shifts in expert weights provide a qualitative lens for analyzing how the model adapts to personalized preferences.

---


### 32. [The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents](https://arxiv.org/abs/2606.04296)

**<font color=#1a73e8>作者：</font>** Manvendra Modgil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As autonomous AI agents move from conversational systems to long-horizon software execution, runtime safety layers that decide when to interrupt an agent have become essential. We study this timing problem using a continuous 18-dimensional affective-dynamics engine (HEART) as a diagnostic probe, evaluating four intervention trigger families - absolute state thresholds, composite state-action patterns, regex reasoning-feature extraction, and zero-shot LLM-as-judge - against human-annotated intervention points on SWE-bench-Verified debugging traces. We report three findings. First, a State Saturation Trap: agents show no recovery signal under sustained difficulty, so modeled frustration quickly crosses the threshold and stays at its maximum, converting threshold-on-state triggers from moment detectors into near-constant indicators that fire on 39-83% of actions across five trajectories. Second, a capability-and-context floor for LLM judges: a small model (gpt-5.4-mini) never fires, while frontier and cross-vendor models escape the zero-firing floor only with full-trajectory context, and even then reach only F1 0.17-0.40 at up to 90x the cost. Third, and most importantly, the supervised target is not reproducible among humans: three trained annotators using one rubric on a 56-action trajectory agree on where to intervene only slightly above chance (location Krippendorff's alpha = +0.047; best pairwise Cohen's kappa = +0.349) and not at all on intervention type (pause degenerate; clarify below chance; reflect only alpha = +0.226). We conclude that intervention timing is a low-reliability construct, making single-annotator F1 an unsuitable optimization target. Our contribution is the joint mapping of this problem across human inter-rater reliability, four detector architectures, a cross-model LLM-judge sweep, and a reproduced saturation effect, rather than any single detector's accuracy.

---


### 33. [LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding](https://arxiv.org/abs/2606.04302)

**<font color=#1a73e8>作者：</font>** Haocheng Xia, Mihir Pamnani, Hanxi Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) caching accelerates inference of large language models (LLMs) by reusing past computations for generated tokens. Its importance becomes even greater in long-context applications such as retrieval-augmented generation (RAG) and in-context learning (ICL). However, conventional KV caching embeds positional information directly into the cache, limiting its reusability. Existing solutions either restrict reuse to prefixes or require expensive memory materialization for positional re-encoding. We introduce LazyAttention, a novel attention mechanism that kernelizes deferred positional encoding to enable zero-copy, position-agnostic KV reuse. By adjusting positional encoding within attention kernels on-the-fly, LazyAttention resolves the materialization bottleneck, allowing a single physical KV copy to serve multiple logical requests at arbitrary positions. Leveraging attention kernels tailored for prefilling and decoding, our system achieves significant efficiency improvements: under skewed document distributions, it reduces time-to-first-token (TTFT) by 1.37$\times$ and increases inference throughput by 1.40$\times$ compared to the state-of-the-art Block-Attention, while maintaining comparable output quality.

---


### 34. [Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems](https://arxiv.org/abs/2606.04306)

**<font color=#1a73e8>作者：</font>** Tianyu Shi, Yang Mo, Yiou Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly deployed in workflows where generated outputs may directly trigger state-changing actions. This creates an execution-boundary problem: proposed actions must be governed before they are executed. We study this problem through economically consequential multi-agent interactions and argue that deployment-grade agent systems should separate proposal generation from environment-facing execution. To operationalize this principle, we introduce the Organizational Control Layer (OCL), a model-agnostic governance infrastructure that intercepts generated actions before execution through policy enforcement and escalation, without modifying the underlying LLM generator. We evaluate OCL on adversarial buyer--seller negotiation environments adapted from AgenticPay. Across multiple frontier LLM backends, OCL reduces unsafe executions from 88% to near-zero while increasing valid success from 12% to 96%. Results further reveal a safety--utility tradeoff: strict governance improves compliance and reliability against policy and constraint violations, but can reduce flexibility in tightly constrained markets. These findings suggest that deployment-grade LLM agent systems require explicit governance at the boundary between language generation and executable actions. The source code is available at: this https URL

---


### 35. [Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline](https://arxiv.org/abs/2606.04315)

**<font color=#1a73e8>作者：</font>** Zhikai Chen, Jialiang Gu, Junyu Yin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents accumulate histories that outgrow their context windows, motivating a growing literature on memory systems. Yet most existing designs are tuned to a single scenario (multi-session chat or a single trajectory format), and there is little evidence that they generalize across the heterogeneous trajectories agents encounter in deployment. We revisit eight memory systems plus an agentic harness for search problems, on five scenarios: single-turn QA, multi-session chat, agentic-trajectory QA, memory stress tests, and long-horizon agentic tasks. The harness, which self-manages flat text-file storage via tool calls, achieves the best cross-task ranking, suggesting that memory performance hinges on giving the agent active control over storage and retrieval rather than on a passive store behind a fixed pipeline. We instantiate this insight in AutoMEM, an agentic memory harness with a self-managed tool interface that achieves the best cross-scenario generality among the systems we evaluate.

---


### 36. [OpenRFM: Dissecting Relational In-Context Learning](https://arxiv.org/abs/2606.04320)

**<font color=#1a73e8>作者：</font>** Zhikai Chen, Junyu Yin, Jialiang Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational Foundation Models (RFMs) promise a single pre-trained predictor that, given any relational database, returns predictions in one forward pass via relational in-context learning (ICL). Yet a substantial gap separates open RFMs from their commercial counterparts, and the origin of this gap has not been systematically understood. We dissect a representative framework, the Relational Transformer (RT), from two perspectives. Model side: we show that RT performs relation-level ICL, and a kernel regression view shows it fails when sparse label-cell coverage yields an underdetermined regression. Data side: we ablate RT's pre-training source and find that existing synthetic-only pre-training and in-distribution pre-training drive the same architecture into different regimes, lazy vs. feature-learning. Probing this gap reveals that the missing ingredient is a support-identifiable relational latent in the label-generation process. These two diagnoses translate into (1) a dual-stage ICL architecture that combines the relational backbone with a batch-level ICL layer lifted from a pre-trained tabular foundation model to overcome relation-level label scarcity, and (2) a homophily-aware synthetic plus continual real-data pre-training mixture, augmented with a prototype-based regularization. These choices define OpenRFM, a simple yet effective RFM that improves average task performance by approximately 30% over the RT backbone and surpasses the commercial model KumoRFMv1 on a large set of evaluation tasks.

---


### 37. [The Digital Apprentice: A Framework for Human-Directed Agentic AI Development](https://arxiv.org/abs/2606.04321)

**<font color=#1a73e8>作者：</font>** Travis Weber, Rohit Taneja  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI deployments face a recurring design tension: heavy human oversight limits scale, while broad autonomy outruns accountability. Neither posture provides the governance infrastructure required for responsible delegation. We present the Digital Apprentice, a framework for scalable, safe AI agency in which autonomy is earned, not assumed. The Digital Apprentice is a developmental learner that internalizes the tacit methodology of a directing human, graduating through per-skill autonomy tiers only when empirical evidence justifies it. The result is an agent that becomes genuinely useful over time while remaining aligned to a specific human's standards. Three architectural components make this possible. (1) Methodology capture, distilling a directing professional's tacit approach into structured assets. (2) Authorization, with autonomy escalation gated by explicit human approval. (3) Continuous alignment, correcting drift at runtime and converting each correction into owned preference data. We instantiate this framework as an inference-time control plane. We mathematically model the quality framework and discuss policies and techniques designed to raise quality. We apply the framework to an open professional corpus, and we show how catching data drift and applying a different technique at runtime recovers degraded quality dimensions under traffic shift. The implication extends beyond any single application. We believe these three pillars, stitched together as a system, form a safer and more viable path to agentic systems that can scale without sacrificing trust.

---


### 38. [Answer Self-Consistency with Margin-Triggered Question Re-Arbitration for the CVPR 2026 VidLLMs Challenge](https://arxiv.org/abs/2606.04323)

**<font color=#1a73e8>作者：</font>** Tomoya Miyazawa, Hiroyasu Okuno  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this report, we present our solution for Track 2 of the CVPR 2026 VidLLMs Challenge. This track evaluates visual relational reasoning in videos, where models must infer relations that are not always explicitly visible. We propose Answer Self-Consistency with Margin-Triggered Question Re-Arbitration (ASC-MQRA), a training-free test-time reasoning framework built on a multimodal reasoning model. The core ASC component performs multiple stochastic video question-answering runs and aggregates their answer choices through answer-level self-consistency. This substantially improves over single-pass inference and forms our final test submission. We further study MQRA, a conditional re-arbitration module for low-margin examples where the first-stage vote distribution indicates uncertainty. Our vote-margin analysis shows that low-margin examples often retain the ground-truth answer among the top candidates, motivating MQRA to narrow the candidate set and re-watch the video only over the retained candidates. On validation, MQRA further improves over ASC, indicating that low-margin vote distributions can provide a useful uncertainty signal. On test, however, MQRA slightly degrades performance relative to ASC, suggesting that re-arbitration is sensitive to the size and category distribution of the triggered subset. Our final test submission therefore uses ASC without re-arbitration, achieving 72.73 average accuracy and 78.34 category-wise macro average accuracy on validation, and 81.16 average accuracy and 80.91 category-wise macro average accuracy on test. This report details our prompting strategy, implementation setup, ablation studies, and diagnostic analyses. The code is available at this https URL

---


### 39. [Parameter-Efficient Fine-Tuning with Learnable Rank](https://arxiv.org/abs/2606.04325)

**<font color=#1a73e8>作者：</font>** Arpit Garg, Simon Lucey, Hemanth Saratchandran  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) is a popular parameter-efficient fine-tuning (PEFT) method that restricts weight updates to low-rank adapters, introducing a fixed low-rank inductive bias by optimizing in a low-dimensional subspace. In this work, we question whether a fixed-rank constraint is the most effective inductive bias for parameter-efficient fine-tuning. We introduce *Learnable Rank LoRA (LR-LoRA)*, a PEFT method in which the adapter rank is learned during the training process. Instead of prescribing a uniform rank for all adapter layers, LR-LoRA allows the optimizer to determine the appropriate rank for each layer. Using this approach, we find substantial layer-wise variation in the learned ranks, with the attention and MLP layers in the transformer models exhibiting systematically different rank preferences. Across a range of language understanding and commonsense reasoning benchmarks, LR-LoRA achieves state-of-the-art performance in most settings and consistently outperforms strong PEFT baselines, demonstrating that a learnable rank provides a more flexible and effective inductive bias than fixed-rank adaptations.

---


### 40. [MorphoQuant: Modality-Aware Quantization for Omni-modal Large Language Models](https://arxiv.org/abs/2606.04349)

**<font color=#1a73e8>作者：</font>** Yue Wu, Changyuan Wang, Zixuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional Post-Training Quantization (PTQ) methods struggle with 4-bit Omni-modal Large Language Models (OLLMs) due to the extreme distribution heterogeneity and disparate outlier patterns across modalities. To address this, we propose MorphoQuant, a modality-aware PTQ framework engineered to preserve cross-modal morphology and mitigate outlier loss. Specifically, we introduce Distribution-Aware Bias Compensation (DABC), which selectively absorbs long-tailed outliers into channel-wise biases. This mechanism safeguards outlier magnitudes while maintaining high-precision discretization for dense inliers, thereby preserving accurate discretization across diverse modal distribution. Complementing this, we propose Morphology-Directed Quantization Function Optimization (MDQFO) to co-optimize the quantization grid with the bias mask, ensuring fine-grained alignment across modalities. Extensive evaluations on Qwen2.5-Omni across benchmarks like MMMU and Video-MME demonstrate our approach's superiority. Notably, our W4A4 model achieves 76.63% on ScienceQA, significantly outperforming SOTA W4A4 methods and surprisingly surpassing the W4A16 baseline, which fully demonstrates the exceptional accuracy-efficiency trade-off of our framework.

---


### 41. [Video2LoRA: Parametric Video Internalization for Vision-Language Models](https://arxiv.org/abs/2606.04351)

**<font color=#1a73e8>作者：</font>** Manan Suri, Sarvesh Baskar, Dinesh Manocha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Processing video in vision-language models is expensive: each frame occupies hundreds of tokens, and inference cost scales with every frame and every repeated query. We introduce Video2LoRA, a method for parametric video internalization. A perceiver hypernetwork reads the intermediate representations produced layer-by-layer as a frozen VLM encodes a video, and generates a Low-Rank Adaptation (LoRA) adapter in a single forward pass. Unlike standard LoRA fine-tuning, which requires iterative gradient updates, Video2LoRA predicts these weights directly from the video. Trained for SmolVLM2 500M and 2.2B on video summarization and captioning, Video2LoRA enables the same frozen VLM to answer queries from the adapter alone, with zero visual tokens in its context at query time. Video2LoRA is statistically non-inferior and equivalent to direct video-in-context inference across all five captioning benchmarks at both model scales, and across seven of eight video question answering benchmark-scale pairings. Although trained only on 12 frames at 384px, it remains stable up to 1,024 frames and 1024px, where direct video-in-context inference often degenerates. Across this sweep, it reduces answer-time visual-token load by up to 1,500x and query TTFT by 6-80x, while preserving video-faithful outputs. We also find that independently generated adapters for non-overlapping video segments can compose in rank space, suggesting a path toward chunked long-video internalization.

---


### 42. [Deliberate Evolution: Agentic Reasoning for Sample-Efficient Symbolic Regression with LLMs](https://arxiv.org/abs/2606.04360)

**<font color=#1a73e8>作者：</font>** Xinyu Pang, Zhanke Zhou, Xuan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) discovers compact mathematical expressions from data, yet recent LLM-based evolutionary methods remain sample-inefficient because they rely mainly on scalar feedback such as MSE. We identify a core limitation: existing methods conflate candidate proposal with search guidance, requiring the LLM to infer how to evolve an expression, diagnose its errors, and reuse past experience from a single score. To address this, we propose Deliberate Evolution (DE), an agentic framework that decouples symbolic generation from search control. DE guides LLM proposals with adaptive operators for search direction, analytical tools for structural diagnosis, and reflective memory for trajectory-level experience. Experiments on LLM-SRBench show that DE consistently outperforms representative LLM-based SR baselines across diverse scientific domains while using only 40% of the standard sample budget.

---


### 43. [Selective Coupling of Decoupled Informative Regions: Masked Attention Alignment for Data-Free Quantization of Vision Transformers](https://arxiv.org/abs/2606.04373)

**<font color=#1a73e8>作者：</font>** Biao Qian, Yang Wang, Yong Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data-Free Quantization (DFQ) addresses data security concerns by synthesizing samples, without accessing real data. It has garnered increasing attention in the context of Vision Transformers (ViTs), owing to the superiority of the self-attention mechanism compared to classical convolutional operation. However, previous DFQ arts for ViTs often suffer from a distribution mismatch between synthetic samples and input distribution expected by quantized models Q, resulting in the suboptimal performance. In this paper, we propose a novel Masked Attention Alignment approach for Data-Free Quantization of ViTs, named MaskAQ, revealing that: 1) the semantics in the self-attention mechanism is predominantly localized to a sparse subset of patches, called informative regions; 2) the informative regions dominate the mutual information between synthetic samples and Q's outputs. To these ends, we incorporate differential entropy maximum over patch similarity of synthetic samples, to decouple informative regions from noisy background. To couple with varied Q, the informative regions are selected to align full-precision models with Q via a masked attention alignment objective, thus yielding high-quality synthetic samples. Furthermore, a periodic sample refreshing strategy comes up to endow MaskAQ with the capacity to continually adapt to the evolving state of Q throughout the training process, to preserve desirable mutual information with synthetic samples. Extensive experiments verify the merits of MaskAQ over state-of-the-art approaches across multiple backbones and downstream tasks. Our code is available at this https URL.

---


### 44. [DLLG: Dynamic Logit-Level Gating of LLM Experts](https://arxiv.org/abs/2606.04378)

**<font color=#1a73e8>作者：</font>** Bingnan Li, Zhaoyang Zhang, Xiaoze Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Leveraging multiple specialized LLMs can combine complementary strengths, but existing approaches trade adaptability for stability: routing commits prematurely, heuristic ensembling depends on fragile proxies, and parameter merging introduces interference. We propose DLLG (Dynamic Logit-Level Gating), a dynamic logit-level ensembling framework that learns token-level expert fusion from sparse response-level supervision. A lightweight gating module predicts step-wise fusion weights, linking trajectory-level correctness to generation without token-level labels or expert retraining. Across diverse reasoning and code benchmarks, DLLG consistently outperforms strong routing, heuristic ensembling, and parameter-merging baselines across model scales, highlighting learned logit-level fusion as a robust and scalable paradigm for integrating specialized experts.

---


### 45. [From Symbolic to Geometric: Enabling Spatial Reasoning in Large Language Models](https://arxiv.org/abs/2606.04381)

**<font color=#1a73e8>作者：</font>** Chen Chu, Bita Azarijoo, Li Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent large language models (LLMs) often appear to exhibit spatial reasoning ability; however, this capability is largely \emph{symbolic}, arising from pattern matching over spatial language rather than true \emph{geometric} reasoning over space. Because LLMs operate on discrete tokens, they lack native support for continuous spatial representations, explicit geometric computation, and structured spatial operators. To address this limitation, we introduce the \emph{Spatial Language Model (SLM)}, the first multimodal LLM that treats location information as a first-class modality and enables geometric spatial reasoning within the model's inference process. SLM directly operates on learned spatial representations rather than textual descriptions of spatial relations. To support effective training, we construct a \emph{Spatial Instruction Dataset} that aligns spatial representations, atomic geometric operations, and natural language instructions. We further propose a new benchmark named \emph{SpatialEval}, which is designed to evaluate spatial reasoning across attributes, distance, topology, and relative-position tasks. Extensive experiments show that SLM significantly outperforms existing LLM-based approaches that rely on symbolic reasoning via prompt engineering or textual abstraction, demonstrating the benefits of integrating geometric spatial representations for robust spatial reasoning.
Our instruction dataset, evaluation benchmark, model training codes, and models' checkpoints can be found at:
\hyperlink{this https URL}{this https URL}.

---


### 46. [Geometry-Preserving Unsupervised Alignment for Heterogeneous Foundation Models](https://arxiv.org/abs/2606.04385)

**<font color=#1a73e8>作者：</font>** Shuwen Yu, Zhanxuan Hu, Yi Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models have driven rapid progress in computer vision, yet the two dominant paradigms, vision-language foundation models (VLMs) and vision-only foundation models (VFMs), remain only partially compatible. VLMs offer language-grounded semantic alignment but are often visually coarse, while VFMs learn discriminative perceptual geometry but lack semantic grounding. We propose GPUA (Geometry-Preserving Unsupervised Alignment), a framework that integrates the complementary strengths of VFMs and VLMs. Inspired by cross-lingual alignment, GPUA treats VFM features as a visual language and learns an orthogonal mapping that translates the VFM space into the VLM semantic space, preserving geometry and narrowing the modality gap without labels or model parameter updates. GPUA is task-agnostic and requires only feature-level access to pretrained models. Experiments across diverse benchmarks demonstrate improved cross-model compatibility and strong gains in downstream zero-shot recognition and segmentation with negligible overhead. Code is available at this https URL

---


### 47. [Read the Trace, Steer the Path: Trajectory-Aware Reinforcement Learning for Diffusion Language Models](https://arxiv.org/abs/2606.04396)

**<font color=#1a73e8>作者：</font>** Anant Khandelwal, Manish Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) generate responses by iteratively unmasking and revising many positions in parallel. This process leaves a rich denoising trace depicting which tokens become confident, which remain unstable, and when commitments form. Existing dLLM reinforcement learning methods use this signal only weakly. Flat rollouts are cheap, but assign a single outcome reward to the whole trajectory. Tree rollouts provide finer, verifiable training signals by branching partial trajectories and propagating leaf rewards upward, but are compute intensive. We ask whether the denoising trace itself can provide tree-like supervision without tree-level compute. We introduce CAPR (Cached-Amortized Path Refinement), a dLLM-RL algorithm that summarizes the denoising trace into a compact path state, uses cached trajectory states to generate cheap sibling continuations, and trains a block-level value head for local block-wise supervision. Under a block-wise unmasking schedule, CAPR records path-state and block-progress features, then redistributes the final outcome reward across blocks according to the tokens revealed in each block. This trains the value head to convert one sparse reward into block-level PPO weights. CAPR therefore recovers much of the granularity of tree search while avoiding full tree expansion, reducing rollout-generation cost to roughly 0.75x that of flat rollouts and 0.6x that of tree rollouts (under standard settings). Across 4x4 Sudoku, Countdown, GSM8K, and Math500, on dense and mixture-of-experts LLaDA backbones, CAPR sets a new state of the art for RL-tuned dLLMs at 256- and 512-token budgets. On Sudoku, it matches the strongest tree-structured baseline at less than one third of the per-step compute.

---


### 48. [TANDEM: Bi-Level Data Mixture Optimization with Twin Networks](https://arxiv.org/abs/2606.04401)

**<font color=#1a73e8>作者：</font>** Jiaxing Wang, Deping Xiang, Jin Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The capabilities of large language models (LLMs) significantly depend on training data drawn from various domains. Optimizing domain-specific mixture ratios can be modeled as a bi-level optimization problem, which we simplify into a single-level penalized form and solve with twin networks: a proxy model trained on primary data and a dynamically updated reference model trained with additional data. Our proposed method, Twin Networks for bi-level DatA mixturE optiMization (TANDEM), measures the data efficacy through the difference between the twin models and up-weights domains that benefit more from the additional data. TANDEM provides theoretical guarantees and wider applicability, compared to prior approaches. Furthermore, our bi-level perspective suggests new settings to study domain reweighting such as data-restricted scenarios and supervised fine-tuning, where optimized mixture ratios significantly improve the performance. Extensive experiments validate TANDEM's effectiveness in all scenarios.

---


### 49. [(Mis)generalization of Helpful-only Fine-tuning](https://arxiv.org/abs/2606.04413)

**<font color=#1a73e8>作者：</font>** Mohammad Omar Khursheed, Baram Sosis, Fabien Roger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Helpful-only models, that is, models that are trained to always follow user intent, are valuable for dangerous capability evaluations and other areas of AI R&D where refusals would be an obstacle. Little is known about the generalization properties of helpful-only training: helpful-only models refuse less than their harmless counterparts, but previous work has not studied other dimensions of their alignment. We study the shortcomings of existing helpful-only models. We find that some show emergent misalignment, others have residual refusal behaviors, and most show poor steerability, sycophancy, and incoherent character. We show that simple anti-refusal training can cause many of these issues. None of these problems are necessary consequences of helpful-only training, though: we show that synthetic document fine-tuning and adding character-related questions to SFT and RL can mitigate them.

---


### 50. [Stateful Visual Encoders for Vision-Language Models](https://arxiv.org/abs/2606.04433)

**<font color=#1a73e8>作者：</font>** Zirui Wang, Junwei Yu, Adam Yala 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used in multi-image, multi-turn agentic settings where decisions depend on visual changes. However, in existing open-weight VLMs, visual comparisons happen only inside the language model, while the visual encoder itself remains stateless: each image is encoded independently, without access to the prior visual context. As a result, small but task-critical changes may be attenuated before the language model has a chance to compare them, especially when those changes do not affect the high-level semantics of the scene. We introduce a Stateful Visual Encoder, which conditions each visual representation on prior visual features. Under supervised finetuning, VLMs equipped with stateful encoders achieve consistent improvements on controlled tasks involving cross-image spatial aggregation, multi-object visual differencing, and visual trajectory behavior cloning. These improvements are consistent across input resolutions, language model sizes, and VLM backbones. Finally, we validate our model on real-world tasks, including longitudinal radiology, fine-grained image comparison, and remote sensing, where stateful encoders consistently improve generalist VLM baselines and can match or surpass specialized models in selected domains. Project page: this https URL

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-137](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
