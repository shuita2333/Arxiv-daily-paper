# 🧠 大模型相关研究 | 2026年07月25日

> 本类共 **153** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-153](./part-04.md)

---

### 51. [AISE-Bench: A Full-Cycle Curated Benchmark for Information Seeking on Academic Knowledge Graphs](https://arxiv.org/abs/2607.20498)

**<font color=#1a73e8>作者：</font>** Fanjin Zhang, Zhengyang Wang, Ruixuan Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) augmented with tools are emerging as autonomous agents capable of using Web engine, APIs, and code to solve complex, long-horizon tasks. Current tool-using benchmarks for information seeking on academic graphs rely on synthetic templates, simplified solution spaces, or narrow tasks such as paper-centric tasks, leaving key challenges underexplored - realistic user intent, complex multi-step API planning, rich parameter filling for APIs, grounded answers with references, and comprehensive evaluation of both the process and the outcome. We introduce AISE-Bench, a real-world, full-cycle annotated benchmark for information seeking on academic knowledge graphs. AISE-Bench release contains 1,133 QA pairs, including query taxonomies, full API execution trajectories, validated parameters, and source-grounded answers with reference links. To support high-quality annotation, we design a customized agent workflow to enable annotators to plan, execute, and revise complex API workflows efficiently. We develop a comprehensive evaluation protocol measuring answer quality, reference grounding, API-planning correctness, and execution success. Among the 14 evaluated methods, even the strongest model (PLAY2PROMPT with Gemini-3-Pro) achieves only moderate performance and often struggles with API planning and execution. AISE-Bench establishes a challenging new testbed for quantitatively evaluating and improving the stepwise correctness, grounded summarization, and traceable reasoning of multi-step API-using LLM agents. Our code and data are available at this https URL.

---


### 52. [ExecuGraph: A Multi-Agent, Execution-Grounded Framework for Reliable Backend Code Synthesis with Large Language Models](https://arxiv.org/abs/2607.20499)

**<font color=#1a73e8>作者：</font>** Sai Deekshith Lekkala, Jothi Prabha Appadurai, Rohith Reddy Bellibatlu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models generate plausible backend code, but a single-pass paradigm provides no guarantee of correctness or runtime reliability. We present ExecuGraph, a multi-agent framework that places execution-based validation at the center of backend code synthesis. Six specialized agents (Planner, Code Generator, Logical Reviewer, Evaluator, Optimizer, and Explainer) are coordinated by a typed directed workflow with a bounded retry budget, implemented on LangGraph with locally hosted models (Ollama) and an optional retrieval layer for algorithmic technique recall. A subprocess-isolated sandbox with a wall-clock timeout guards every evaluation. We evaluate on a curated 30-problem DSA suite (internal-30), HumanEval (n=64), and an APPS-introductory subset, contrasting ExecuGraph against a single-agent one-shot baseline and a single-agent execution-retry baseline (a Reflexion-style ablation that isolates the contribution of multi-agent decomposition). On internal-30, the three conditions are statistically indistinguishable (n=30; paired Wilcoxon p=0.59 MF vs. SO, p=0.08 SR vs. SO); 95% bootstrap confidence intervals on all pairwise mean differences include zero. On HumanEval, multi-full edges ahead by +3.1 pp. The strongest signal is cross-model: with DeepSeekCoder V2 Lite, graph-category accuracy improves from 57.5% (oneshot) to 80.0% (multi-full), a +22.5 pp jump that supports a scaling hypothesis: the value of multi-agent decomposition grows with base-model capability. The framework's primary contribution is methodological: a single codebase that collapses by configuration into one-shot, execution-retry, and per-agent ablation conditions, enabling controlled measurement of each lever's marginal contribution. A per-agent ablation, retry-budget sweep, error-class taxonomy, and test-source audit are reported.

---


### 53. [FlowEdit: Information-Theoretic Control of LLM Reasoning Flows for Ill-posed Problems Involving Conflicts](https://arxiv.org/abs/2607.20500)

**<font color=#1a73e8>作者：</font>** Sizhe Tang, Guangyu Jiang, Yu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) perform strongly on well-specified reasoning tasks with a feasible answer. However, problems encountered in the open world can become ill-posed due to inconsistent conditions, conflicting statements, or mutually incompatible requirements, admitting no valid responses. We argue that reasoning of such ill-posed problems involving conflicts require novel LLM capabilities to make hidden conflicts explicit, maintain competing hypotheses via multiple reasoning branches, and generate alternative responses in a single pass, all of which are challenging due to the limitation of the next-token prediction mechanism in LLMs. To this end, we propose FlowEdit, a novel framework that leverages information-theoretic principles to quantify and regulate internal reasoning flows of LLMs, for generating a full set of alternative responses under valid hypotheses. FlowEdit can be viewed as enforcing a branch-aware reasoning process using two dual information-theoretic objectives on the model's internal reasoning representations: maximizing the information flow from each selected hypothesis to the branch outcome, while minimizing the overlap and conditional dependence across sibling branches, to provide a diverse, informative set of responses with broad coverage. We show that this is achieved through tractable variational bounds under boundary embeddings being {\epsilon}-sufficient, optimizing the underlying conditional mutual information in LLM reasoning process. Extensive experiments demonstrate that FlowEdit outperforms leading proprietary models, improving exact-set-match accuracy by 68%, while boosting overall response informativeness by 24%. We further show that flow regulation surfaces in the token stream as a redistribution of next-token entropy that concentrates inside each branch, amplifies at flow boundaries, and scales with the number of flows the problem requires.

---


### 54. [Optimizing Hypergraph-Based RAG: Toward Better Fact Extraction and Chunk Retrieval](https://arxiv.org/abs/2607.20506)

**<font color=#1a73e8>作者：</font>** Houda Khrouf, Pedro Fillastre, Sebastiao Correia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GraphRAG enables deeper reasoning by structuring knowledge as graphs but struggles with n-ary facts. HyperGraphRAG uses hypergraphs for richer semantics, improving accuracy, yet relies on error-prone LLM extraction and inefficient standard chunk retrieval. We address this by employing self-consistency prompting to improve the extraction, and Personalized PageRank algorithm over hypergraph to enhance chunk retrieval.

---


### 55. [MiniCache: Reusable Program Caching with Small Model Interfaces for Efficient LLM Inference](https://arxiv.org/abs/2607.20507)

**<font color=#1a73e8>作者：</font>** Jingquan Chen, Jinghua Piao, Jie Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for program-aided reasoning, agentic decision making, and structured task execution, but these applications often incur high inference cost. We present MiniCache, a reusable program caching framework that transforms Program-of-Thought (PoT) programs into parameterized cache objects, enabling reusable computation across structurally similar requests. MiniCache reuses the same small model for semantic variable extraction on cache-hit requests and speculative drafting during target-LLM generation, reducing expensive target-LLM invocations while preserving task quality. Experiments on shopping-style request datasets, WebShop, Formula, and CodeTAT-QA demonstrate that MiniCache improves the trade-off between inference latency, cache reuse, and accuracy, achieving up to 3.1x lower latency and 2.8x higher throughput under parallel serving. These results show that small models are most effective not as replacements for large models, but as lightweight interface models that enable reliable and efficient reusable program caching.

---


### 56. [SiGMA: Sign-Guided Merging and Adaptation for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2607.20511)

**<font color=#1a73e8>作者：</font>** Keonhee Park, Gunhee Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Continual Instruction Tuning (MCIT) is crucial for adapting Multimodal Large Language Models (MLLMs) to evolving a sequence of downstream tasks. Prior methods mostly utilize Mixture of Experts or expansion merge approach, primarily focusing on catastrophic forgetting, yet they still suffer from negative interference during inference, where newly learned updates overwrite useful prior knowledge and degrade overall performance. To address this, we propose SiGMA (Sign Guided Merging and Adaptation), a simple yet effective framework that mitigates negative interference with two components: sign guided adaptive tuning during training and sign guided merging at inference. Sign guided adaptive tuning reduces collisions with past knowledge and learns the current task with minimal drift, mitigating severe forgetting. Sign guided merging further improves consolidation by selectively scaling salient parameters to preserve and amplify useful task specific knowledge. Experiments on UCIT and DCL benchmarks show that SiGMA significantly reduces negative interference and outperforms state of the art MCIT methods. Our code is available at SiGMA.

---


### 57. [Reliability-Aware LLM Alignment from Inconsistent Human Feedback](https://arxiv.org/abs/2607.20515)

**<font color=#1a73e8>作者：</font>** Jingyi Huang, Ruohan Zong, Yujun Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Human Feedback (RLHF) is critical for aligning Large Language Models (LLMs) with human preferences. However, its efficacy is often compromised by the inherent inconsistency and subjectivity of human annotations. Existing preference optimization frameworks, such as Direct Preference Optimization (DPO), typically treat ambiguous pairs with high annotator disagreement identically to those with unanimous consensus, forcing models to overfit to inconsistent supervision signals and leading to suboptimal alignment. In this work, we propose Reliability-Guided Preference Optimization (RGPO), a robust framework designed to mitigate the impact of inconsistent human feedback. RGPO estimates annotator reliability and infers latent ground truth labels from noisy human feedback to identify robust preferences. Furthermore, we introduce a reliability-aware consistency optimization that dynamically modulates the training objective based on the consensus level of annotations, ensuring the model prioritizes high-consensus supervision signals. Extensive experiments on LLM alignment benchmarks demonstrate that RGPO effectively reduces inconsistency and noise in training data and achieves superior performance compared to widely adopted RLHF baselines. Our code and configurations are available at this https URL.

---


### 58. [Scaling Closed-Loop Feature Channel Configuration with LLMs](https://arxiv.org/abs/2607.20516)

**<font color=#1a73e8>作者：</font>** Tolgay Atinc Uzun, Radu Timofte, Dmitry Ignatov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Promising initial results in closed-loop large-language-model-based channel-configuration search demonstrated that neural-network widths can be optimized directly through executable code generation and accuracy feedback. However, those results were obtained from a relatively sparse set of valid evaluations, leaving open whether the observed optimization behavior transfers to a denser sampling regime and whether additional architectural regularities emerge when more generated networks are evaluated. To test this, the same search setting is scaled to 250 candidate networks per fine-tuning cycle. The analysis covers 2000 generated candidates from 8 complete cycles, yielding 462 verified CIFAR-100 evaluations after task and metadata filtering. Per-cycle mean accuracy exhibits a positive linear trend with slope 9.87e-4 (p=0.043), while the high-performing frontier improves more strongly: the best observed accuracy increases from 0.3144 to 0.3676, and both the top-5 and top-10 cycle-level means exhibit positive trends. The scaled run also reveals improved parameter efficiency. The best model reaches 0.3676 with 11.8M parameters, compared with an early high-performing model at 0.3144 with 166.5M parameters. Beyond accuracy, the larger sample exposes architectural regularities that were difficult to assess from sparse observations. Non-power-of-two channel widths occur in 41.8% of verified candidates, and the strongest models share structured channel-allocation patterns characterized by moderate early widths and expanded middle or later blocks. These findings indicate that the channel-search signal observed in the initial study transfers

---


### 59. [Multimodal CoLRAG-TF: Triple-Filtered Retrieval for Complex PDFs](https://arxiv.org/abs/2607.20517)

**<font color=#1a73e8>作者：</font>** Takato Yasuno  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) over heterogeneous PDF collections remains challenging due to multimodal content, domain-specific terminology, and the need for multi-hop reasoning across dispersed evidence. We present Multimodal CoLRAG-TF, a four-axis fusion architecture that integrates dense text embeddings, BM25 keyword matching, knowledge-graph triple filtering, and image-based similarity for robust retrieval over complex documents. Our system constructs a multimodal index of 2,403 blocks extracted from 43 Japanese disaster lesson PDFs, supported by a hybrid OCR pipeline and LLM-based caption generation. To enhance compositional reasoning, we extract 11,414 OpenIE triples and index them with FAISS, enabling sub-second triple lookup and hierarchical propagation of relevance signals. A HippoRAG2-inspired coarse-to-fine retriever (volume $\to$ chapter $\to$ block) narrows the search space before final fusion scoring. Bayesian optimization over fusion weights reveals that the triple axis must dominate ($\alpha_\text{triple} = 0.44$) to counteract lexical bias and sustain multi-hop retrieval quality. Evaluated on a 457-pair benchmark, Multimodal CoLRAG-TF achieves a Retrieval Recall of 0.9909 and a 71.6$\%$ improvement in multi-hop answer similarity over single-hop queries. An image-to-lesson pipeline using a vision LLM further demonstrates the applicability of the approach to visual inputs. These results show that triple-filtered multimodal fusion is essential for structured reasoning over noisy, heterogeneous PDFs and provides a general framework applicable beyond the disaster domain.

---


### 60. [Representation Robustness Under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving](https://arxiv.org/abs/2607.20520)

**<font color=#1a73e8>作者：</font>** Sagnik Nath, Edith Aurora Graf, Liang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly evaluated on mathematical problem solving, yet prior work often treats representationally equivalent formulations as interchangeable and conflates reasoning errors with interface failures. This paper investigates representation robustness in LLM-based mathematical problem solving by systematically varying surface representations of the same underlying problems, including story problems, word-equations, symbolic equations, and isomorphic paraphrases. Using a curated dataset of mathematically equivalent problems, we evaluate five contemporary LLMs under a direct answer generation condition. We find substantial representational sensitivity: models frequently change correctness across equivalent formulations, with nontrivial flip rates across story, symbolic, and word-equation variants. We also observe systematic regressions under isomorphic reformulations, showing that even subtle paraphrase-level changes can degrade performance despite preserved mathematical structure. We then evaluate a code-augmented condition in which models externalize reasoning as executable Python code that is run locally for validation. This interface reveals strong latent reasoning capability in some models that perform poorly under direct prompting, but it does not uniformly improve robustness. Instead, failures shift across interaction layers, from opaque reasoning errors to protocol violations and execution failures. Even when executable reasoning succeeds, representation sensitivity often persists. Overall, our results show that reasoning scaffolds do not eliminate representational brittleness, but expose new tradeoffs among correctness, reliability, latency, and cost. We argue that representation should be treated as a first-class interface design variable in LLM evaluation and deployment, especially for AI-assisted problem-solving systems.

---


### 61. [Attention Degradation, Function Token Anchoring, and the Limits of Attention-Based Intervention in Large Language Models](https://arxiv.org/abs/2607.20524)

**<font color=#1a73e8>作者：</font>** Sagar Dangal, Manoj Shakya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mean cross-positional attention degradation is widely reported in transformer interpretability, yet whether it causally limits contextual retrieval remains untested. We present six coordinated experiments across GPT-2, LLaMA-3.2-1B/3B, OPT-1.3B, and distilgpt2. We first characterise short-term (5-100 token) attention degradation, finding a universal exponential-then-plateau pattern whose rate is inversely correlated with depth, with distinct layer-wise entropy signatures per architecture. Function token anchoring proves architecture-dependent: OPT-1.3B (absolute positional encoding) shows distance-dependent preposition specificity, GPT-2 shows uniform non-specific dependence, and LLaMA (RoPE) shows reversal at long distances. Strategic comma insertion at clause boundaries causally reduces prediction degradation in the 40-80 token range, with the benefit tied to syntactic boundary alignment rather than token density. We then test the mechanism causally: Relay-Aware Attention (RAA), which biases attention logits toward function token positions, verifiably increases attention mass by 16-24% yet yields null effects on GPT-2 and LLaMA-1B, preliminary harm on LLaMA-3B, and a mixed effect on OPT-1.3B that nets to approximately zero. Multi-fact retrieval probes further show that degradation rate does not predict retrieval accuracy across models. We conclude that mean attention degradation is largely descriptive rather than prescriptive: function tokens contribute through what their hidden states compute, not through the attention they receive -- with implications for interpretability methodology and attention-score-based inference optimisations such as KV-cache eviction.

---


### 62. [Autonomous disproofs of the sum-product conjecture over $\mathbb R$ with GPT-5.5 Pro](https://arxiv.org/abs/2607.20525)

**<font color=#1a73e8>作者：</font>** Yichen Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> OpenAI's recent disproof of the Erdős unit distance conjecture marked a milestone for AI in mathematics. It also inspired another breakthrough: a human disproof of the Erdős--Szemerédi sum-product conjecture over $\mathbb R$. In this paper, we present a simple agent built on GPT-5.5 Pro. Using a problem-agnostic, three-stage prompting pipeline -- proof-plan proposal, proof construction, and review -- the agent autonomously generated correct proofs that the sum-product conjecture is false over $\mathbb R$ in 7 of 8 independent trials; in the remaining trial, it identified an unresolved gap in its argument. The seven proofs are diverse: some are close to existing unit-based constructions, while others avoid units by using $L^p$-type regions of algebraic integers. The system used an average of 132.4k reasoning tokens per trial. We release the code, intermediate outputs, and generated proofs, providing a reproducible, data-contamination-free case study in autonomous proof generation.

---


### 63. [ConfidenceBench: Evaluating Confidence Calibration in Large Language Models](https://arxiv.org/abs/2607.20526)

**<font color=#1a73e8>作者：</font>** Matthew ffrench-Constant, Daniel Yang, Xinmeng Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in settings where fluent but incorrect answers can be costly. In these settings, accuracy alone is insufficient: models must also know when they are likely to be wrong. We present ConfidenceBench, a calibration benchmark that evaluates verbalized confidence estimates in 15 frontier LLMs using the Brier score, a proper scoring rule that incentivises truthful probability reporting. Confidence is elicited via prompting, requiring no access to model logits and making the framework applicable to both closed-source and open-source systems. The benchmark comprises 200 private multiple-choice questions across four categories: spatial reasoning, high-precision mathematics, word lookup, and unknowable questions. Across three independent runs, Claude Opus 4.6 and Gemini 3.1 Pro Preview achieve the lowest Brier scores, both reported as 0.103. Both substantially outperform the calibrated-random baseline of 0.1875, while Gemini 3.1 Flash-Lite scores 0.367, indicating severe miscalibration. Accuracy and calibration diverge substantially across model families: the most accurate model is not the best-calibrated, and several models perform worse than the calibrated-random Brier baseline despite reasonable accuracy. These results show that verbalized confidence calibration is a distinct and practically important axis of LLM reliability, complementary to standard accuracy-based evaluation.

---


### 64. [Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis](https://arxiv.org/abs/2607.20527)

**<font color=#1a73e8>作者：</font>** Taewan Goo, Junsik Kim, Kyulhee Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic LLM systems such as OpenScholar and PaperQA2 read the scientific literature and return cited answers, and both they and their benchmarks already check whether those citations hold, with a fixed attribution model or human graders. Neither audits the reliability of that check itself. We show it is not reliable, and that this matters. On identical agent outputs the measured unsupported-citation rate ranges from about 3% to about 18% depending only on the verifier's strictness, and although verifiers agree on which citations are supported, they disagree on which to flag (negative-specific agreement 0.27 to 0.30), so no single flag set is trustworthy and cross-paper comparison is invalid without a named verifier and protocol.
We present a gold-anchored evaluation protocol and a deployable guard that make this behavior measurable and bounded. The protocol validates the verifier, measures re-attribution, and calibrates a guarantee against human gold rather than another model's verdict; the verifier is a swappable instrument chosen on cost (recall 0.94 on the supported class, held out), and re-attribution is a commodity step where a deterministic BM25 matches the best open generator. The guard adds a split-conformal layer placing a distribution-free, finite-sample bound on truly unsupported citations that slip past a chosen flagging rule, a guarantee on catch rate rather than conclusion correctness. The bound holds on held-out gold, and we identify and quantify the condition governing its transfer to deployment, calibration-negative difficulty, with a concrete recalibration recipe, left untested by prior conformal-factuality work.
Validated across four open 27-35B models and three agentic pipelines on public benchmarks (SciFact, QASA, PubMedQA), with confidence intervals on every headline number, the protocol and guard ship as an open single-GPU kit.

---


### 65. [PromptPack: Scaling LLM Annotation Agents for Online Recommendation](https://arxiv.org/abs/2607.20528)

**<font color=#1a73e8>作者：</font>** Sebastian Koralewski, Merwan Barlier, Yulia Stolin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online recommendation platforms increasingly use Large Language Models (LLMs) to extract structured features from ad creatives. While deploying a single-call LLM annotation agent yields significant Click-Through Rate (CTR) improvements in our live production environment, per-creative prompting is prohibitively expensive to scale. The redundant system instructions sent in every request account for 94% of billed input tokens. To break this cost bottleneck, we introduce PromptPack, a scalable, high-throughput LLM annotation agent. PromptPack achieves this scale via in-context batching, combining a shared system prompt, a strict XML structural envelope, and an output correction layer to ensure deterministic, pipeline-ready feature extraction across multiple creatives simultaneously. We evaluate PromptPack via an offline retrieval benchmark using a downstream logistic-regression ranker. To deeply profile the agent's behavior, we measure AUC and introduce Volume-Weighted Absolute Lift (VWAL), a novel metric capturing the signal quality of the generated features. Compared to our live, unbatched production baseline, PromptPack at batch size 20 cuts our LLM costs by 89% and accelerates throughput by 2.5x while fully preserving AUC.

---


### 66. [Uncertainty-Aware Trust Estimation for Multi-LLM Systems via Structured Expert Judgement](https://arxiv.org/abs/2607.20529)

**<font color=#1a73e8>作者：</font>** Jiawei Zheng, Jiazhen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) ensembles are increasingly used to improve reliability by combining predictions from multiple LLMs. However, existing aggregation methods typically assume that all models are equally trustworthy, overlooking differences in uncertainty quality. This assumption is poorly suited to heterogeneous LLMs, whose reliability and capability vary significantly, making naive aggregation vulnerable to unreliable or adversarial experts. In this work, we formulate multi-LLM aggregation as a problem of uncertainty-aware trust estimation. We adapt structured expert judgment from decision theory, using context-aware calibration questions to estimate expert reliability based on the quality of its probabilistic predictions. Specifically, we employ Cooke-style log weighting, which penalises overconfident incorrect predictions and favours well-calibrated experts. We evaluate our approach on MMLU and MMLU-Pro across homogeneous, heterogeneous, and contaminated expert panels. Results show that while aggregation methods perform similarly in homogeneous settings, Cooke weighting becomes critical under heterogeneity and contamination. It achieves a superior accuracy-reliability balance and remains robust when unreliable experts are introduced. These findings suggest that Multi-LLM aggregation requires not just combining predictions, but calibrating trust under uncertainty.

---


### 67. [DynamicMCPBench: A Trace-Grounded, Effect-Scored Benchmark for LLM Agents over Live MCP Servers](https://arxiv.org/abs/2607.20531)

**<font color=#1a73e8>作者：</font>** Jerzy Kamiński, Ilya Galyukshev, Artem Kuznetsov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly deployed over Model Context Protocol (MCP) servers, yet the benchmarks used to evaluate them score the final answer or a fixed "ground-truth" list of tools, both of which are fragile once the underlying data is live and stateful. We present DynamicMCPBench, a reusable framework rather than a fixed dataset. A practitioner can run it on their own MCP servers to test models on their own tasks, or let it collect servers automatically to measure a model's general ability to solve agentic tasks. Given the servers and any set of models, it generates realistic goals, pursues each one live to record a successful trajectory, distills that trajectory into path-agnostic effect checkpoints, and scores an agent on whether it reproduces those effects, never on the final answer. To show what the framework reveals, we run it at scale: 24 models over 121 servers and 750 tasks spread evenly over 15 task categories (50 each), where each category targets a distinct tool-use challenge of the generated questions. Each task is scored by pass^3: it counts as solved only if all three independent attempts succeed. Even the strongest agents solve only about half of the tasks, 31% of tasks are solved by no model at all, and accuracy collapses as the required tool chain grows longer (from 39% on the shortest chains to 13% on the longest). A human validation study confirms the automatic scoring is reliable (chance-corrected agreement of 0.76). DynamicMCPBench thus turns benchmark construction into something practitioners can rerun on their own servers and models, while exposing a consistent inability of current agents to handle long, multi-step agentic tasks.

---


### 68. [Leveraging Biokinetic Knowledge Priors for Data-Scarce Bioprocess Modeling](https://arxiv.org/abs/2607.20539)

**<font color=#1a73e8>作者：</font>** Kyunghoon Hur, Eunjung Jeon, Hyun Woo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While deep learning has accelerated drug discovery, its impact on biomanufacturing has been considerably more limited. The reason is data scarcity. Bioreactor experiments are high-cost, take days to weeks, and are rarely shared in public form, leaving each research work with only a handful of experiments. The domain itself, however, is rich in prior knowledge. Biokinetic ordinary differential equation (ODE) models have described microbial growth for decades, yet how to inject this knowledge into a neural network has not been studied systematically. We present the first systematic study of how to inject this ODE knowledge into a neural network, comparing a data-level prior that pre-trains a generic decoder on simulated ODE curves against an architecture-level prior that embeds the ODE inside the decoder. Both consistently outperform no-prior baselines across 11 datasets and 7 microbial species. Our central finding is that the two are substitutable. A generic decoder pre-trained on simulation matches a fully bio-structured decoder trained on real data. Simulation pre-training therefore offers a simple, data-efficient recipe for deep learning under bioprocess data scarcity.

---


### 69. [SOAP, Muon, and Beyond: Pushing LLM Pretraining Scales](https://arxiv.org/abs/2607.20548)

**<font color=#1a73e8>作者：</font>** Mikail Khona, Aditya Vavre, Boxiang Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Higher-order optimizers such as Muon and SOAP offer faster convergence than AdamW, but their computational cost and numerical stability challenges have limited adoption at scale. In this work, we adapt and enhance preconditioned gradient methods to overcome the practical challenges of large-scale LLM pretraining. We first identify instabilities in SOAP at large batch sizes and propose algorithmic modifications including per-step QR orthogonalization and improved preconditioning strategies that eliminate loss spikes and enable stable training in these regimes. We then present a unified empirical study of SOAP, Muon, and AdamW using update-RMS matching to ensure fair learning rate transfer across optimizers. As part of this analysis, we empirically evaluate the orthogonalization quality of Muon. Our experiments on multi-billion-parameter models trained on trillions of tokens reveal that SOAP and Muon consistently outperform AdamW at the scales we tested. Notably, at batch sizes of up to 100M tokens for next-token prediction, these optimizers maintain training stability and quality while AdamW degrades. To enable efficient training at large scale, we introduce a layer-wise distributed optimizer compatible with Megatron-LM. Our implementation balances memory and hides communication while avoiding approximations to the optimizer computations, thus retaining their convergence benefits. Additionally, we identify and build specific system-level improvements to further accelerate our layer-wise implementation. To support the research community, we release a codebase that contains emerging algorithms for optimization: this https URL

---


### 70. [Monkey King Bang: A Unified Scientific Multimodal Foundation Model](https://arxiv.org/abs/2607.20557)

**<font color=#1a73e8>作者：</font>** Hesen Chen, Xinyu Su, Xiaomeng Yang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific discovery is increasingly shifting from isolated disciplines to multi-domain reasoning, and AI for science faces a similar transition. Existing systems are either specialised for individual domains or unify scientific data mainly through text tokenisation and prompt-based interfaces, limiting their ability to handle diverse scientific inputs, produce modality-native outputs, and support joint understanding, reasoning, and generation across scientific domains. We introduce MKB, a unified scientific multimodal model for both understanding and generation, built around a shared Transformer backbone and modality-tailored encoders, adapters, and decoders. MKB covers six scientific branches, including DNA, RNA, proteins, small molecules, earth science, and medical images, and supports native outputs such as biological sequences, molecular strings, meteorological fields, and segmentation masks. Training follows a two-stage modality-then-language curriculum: Stage 1 aligns modality-specific components with the frozen backbone, and Stage 2 consolidates them with the language backbone using mixed scientific and general corpora. Experiments show that MKB achieves competitive scientific understanding across biological and molecular benchmarks, produces high-fidelity native outputs for weather forecasting, biological generation, and medical-image segmentation, and largely retains the general capabilities of its Qwen3-VL backbone. These results demonstrate the feasibility of the proposed paradigm, suggesting that shared-backbone models with modality-tailored components can provide a promising foundation for future cross-domain scientific multimodal exploration. The model and code are publicly available at this https URL and this https URL.

---


### 71. [StabilityBench: Benchmarking Instability in LLMs](https://arxiv.org/abs/2607.20558)

**<font color=#1a73e8>作者：</font>** Emma Kondrup, Zachary Yang, Anne Imouza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI Assistants are increasingly deployed in high-stakes settings, such as healthcare or government services. Yet their real-world behavior remains poorly understood due to strong context dependence. Current evaluation protocols follow a defense-in-depth paradigm with compounding layers of safeguards, ranging from traditional benchmarks to live or adversarial testing. Such benchmarks remain largely static and single-turn, limiting their ability to capture real-world variability in conversational settings. We propose StabilityBench, a principled, general and model-agnostic benchmark operator that transforms single-turn benchmark queries into multi-turn interaction histories. StabilityBench augments existing benchmarks by injecting realistic user simulations, through demographic proxies or sycophantic baits, while preserving original task intent. We apply StabilityBench to four benchmarks spanning mathematical reasoning, health question-answering and safety, and evaluate nine large language models under these conditions. Our results show that model performance is consistently unstable under these injections, with considerable performance degradations on three out of four benchmarks studied. These highlight important limitations of static evaluations and motivate more realistic evaluation settings. To this end, we propose StabilityBench-Mini: a size-preserving variant of StabilityBench that samples across diversification axes, enabling more realistic evaluation without increasing costs.

---


### 72. [Chronofy: A Temporal-Logical Decay Architecture for Information Validity in Time-Aware Retrieval-Augmented Generation](https://arxiv.org/abs/2607.20560)

**<font color=#1a73e8>作者：</font>** Muntaser Syed, Marius Silaghi, Sheikh Abujar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems retrieve and integrate external knowledge to ground large language model (LLM) outputs. However, current RAG architectures treat all retrieved facts as equally valid regardless of temporal provenance, leading to temporal hallucination, where plausible but obsolete facts corrupt the output. A clinical lab reading from yesterday is actionable; the same reading from six months ago is noise. We present Chronofy, a three-layer neuro-symbolic framework implementing the Temporal-Logical Decay Architecture (TLDA) that embeds temporal validity directly into the representation, retrieval, and reasoning layers of RAG systems. Layer 1 reserves a dedicated temporal subspace within Matryoshka embeddings to make fact age structurally irremovable from the representation. Layer 2 integrates learnable exponential decay functions into graph-based retrieval, where the decay coefficient $\beta_j$ is grounded in Bayesian decision theory as an approximation of twice the latent process mean-reversion rate. Layer 3 applies Signal Temporal Logic (STL) robustness functions to evaluate the temporal validity of retrieved knowledge, not LLM output confidence, and enforces the possibilistic weakest-link principle to bound output confidence by the most decayed evidence in the reasoning chain. We evaluate Chronofy on temporal knowledge graph forecasting benchmarks, the TimE temporal QA benchmark, and a domain-specific sensitivity analysis, demonstrating that explicit temporal decay modeling improves retrieval precision, reduces temporal hallucination, and enables principled data re-acquisition triggers when temporal context is insufficient.

---


### 73. [Evaluating the Effectiveness of Persona Simulation in Opinion Prediction with GPT-4.1](https://arxiv.org/abs/2607.20589)

**<font color=#1a73e8>作者：</font>** Sarah Y. Li, Ziyu Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persona simulation involves utilizing large language models (LLMs) to anticipate human choices or interactions based on specific characteristic information. To further understand current limitations and future directions, we tested persona simulation in opinion prediction with GPT-4.1 (knowledge cutoff by June 2024). Using personas from nine U.S. states provided by Columbia University's Personas dataset, GPT-4.1 accurately predicted 2024 election outcomes in eight out of the nine states, only failing in one of the swing states. We then focused on opinions related to medicine and healthcare. With the American Trends Panel Wave 123 dataset from Pew Research Center, GPT-4.1 was able to anticipate beliefs about childhood vaccines with an accuracy of up to 0.94. Furthermore, we applied GPT-4.1 to generate conversations among personas and observed that the simulated dialogues and opinions adhered well to personas' personalities and backgrounds, albeit lacking natural human-like flow. Persona simulation proves to be a promising application of artificial intelligence as long as biases are addressed. In the near future, it will be beneficial to apply it to opinion analysis and reaction prediction in diverse fields ranging from public health to lawmaking to economics.

---


### 74. [Are Single-Token Sparse Autoencoder Features Causally Necessary? Layer-Depth and SAE-Family Effects](https://arxiv.org/abs/2607.20596)

**<font color=#1a73e8>作者：</font>** Seonglae Cho, Zekun Wu, Kleyton Da Costa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoder (SAE) features are used to interpret and steer large language models, yet whether a feature's causal role is stable across SAE families remains untested. Single-token features that activate on one vocabulary item provide the diagnostic case where ground truth permits direct comparison. We analyze 3.9M features across six models and three SAE families using zero-ablation at full layer depth. Single-token features cluster 4.7x tighter in decoder space and concentrate in early layers (Layer 0 in GPT2-Small; L0-L4 in Gemma). Ablating them yields Benjamini-Hochberg-significant logit reductions in 178 of 208 full-layer conditions, with depth controlling whether damage cascades downstream or shapes the output directly. Cross-family causal differences exceed within-family scale effects: on the same base model, GemmaScope and BatchTopK features remain causally anchored, while LlamaScope features are locally redundant. The target token's rank recovers to within 2x baseline 96-98% of the time after the same ablation, and a controlled activation-function comparison reverses sign within the same model, leaving training recipe as the residual candidate. Cross-family interpretability claims are therefore sensitive to training methodology, not just activation function or scale.

---


### 75. [WaveformQA: Benchmarking LLM Temporal Reasoning on Digital Waveforms](https://arxiv.org/abs/2607.20638)

**<font color=#1a73e8>作者：</font>** Yichuan Liu, Daniel Cummings, Nick Vadlamudi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated strong capabilities in code generation and reasoning, yet their ability to perform temporal reasoning over digital waveform data remains largely unexplored. Although reasoning over digital waveforms is a critical bottleneck in design verification, existing benchmarks primarily evaluate hardware description language (HDL) code generation and use waveforms only as supplementary context. This paper presents WaveformQA, an open-source question-answering benchmark for evaluating LLM temporal reasoning over digital waveforms. The benchmark comprises 360 questions with programmatically generated ground truths across eight categories of varying difficulty, including questions targeting multi-signal correlation and event ordering. Waveforms are generated from open-source design implementations, ensuring reproducibility and grounding the benchmark in real hardware behavior. Evaluation of frontier LLMs reveals that while models achieve reasonable accuracy on simple queries, performance degrades due to context window limitations and reasoning difficulties on complex temporal and multi-step questions. In addition, we show that an event-time JSON representation of waveforms improves LLM reasoning accuracy versus the standardized value change dump (VCD) format. The open-source framework supports extending to new question categories and importing new waveform sources, enabling researchers to rapidly prototype temporal reasoning experiments.

---


### 76. [Learning to Detect UI Principle Violations via Reinforcement Learning](https://arxiv.org/abs/2607.20690)

**<font color=#1a73e8>作者：</font>** Nishi Mehta, Swathi Alse, Himani Kumavat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models and coding agents increasingly generate web front-end code, yet their outputs are typically evaluated primarily for functional correctness. A generated interface may compile, render, and pass unit tests while still violating established interface quality principles, including accessibility barriers, deceptive design patterns, poor visual hierarchy, and excessive decision complexity. Existing auditing approaches face a trade-off between cost, coverage, and scalability: expert human review provides rich judgment but is slow and expensive; frontier vision-language models offer broader reasoning capabilities but remain costly to deploy at scale; and rule-based tools such as axe-core and Lighthouse are inexpensive but primarily capture mechanically checkable accessibility issues.
We investigate whether a lightweight vision-language model can serve as an effective critic for generated interfaces. We unify 19 interface-quality principles from three complementary sources of HCI knowledge: WCAG 2.2 accessibility standards, deceptive design taxonomies, and established theories of perception, cognition, and interaction. To train this critic, we construct a verified dataset of approximately 10,000 generated web pages by synthetically injecting known violations into clean, LLM-generated Tailwind pages.
Continued reinforcement learning on a 4B vision-language model improves micro-F1 from 36\% to 84\%, with 13 of 19 principles exceeding 80\% F1. The resulting critic can audit generated interfaces, filter low-quality interface training data, and provide a reward signal for design-aware code generation. We release our data-generation recipe and injection/verification prompts to support reproducible evaluation and future work on scalable interface-quality assessment.

---


### 77. [REGARD: Regional Affective Differences in Large Language Models](https://arxiv.org/abs/2607.20722)

**<font color=#1a73e8>作者：</font>** Andrei Chetvergov, Alexander Evseev, Mikhail Solovev 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models trained and aligned within different linguistic and regional ecosystems may frame the same political, cultural, and geopolitical entities in different ways. Such differences are often evaluated through sentiment, favorability, or stance, reducing model attitudes to a single positive-negative axis. We introduce REGARD, a study of what drives affective framing differences across LLMs on post-Soviet entities using target-directed Valence-Arousal-Dominance profiling. We query 19 models on 500 region-specific targets, score their responses with two independent LLM judges, GPT-4o-mini and Qwen3.6-35B-A3B, and validate the measurements on a 300-item human-annotated subset. Post-hoc Ward-linkage clustering of all 19 models by affective and response-behavior profiles yields three behavioral clusters that cut across model origin, family, and parameter count. Generic-answer rate is strongly associated with lower arousal (r = -0.81) and with cluster placement: models that deflect evaluative prompts with templated responses cluster together at low arousal regardless of origin. These findings show that VAD profiling captures emotional intensity, a dimension of affective framing that is largely invisible to conventional sentiment-based evaluation.

---


### 78. [LLMs Get Lost in Evolving User Intent](https://arxiv.org/abs/2607.20734)

**<font color=#1a73e8>作者：</font>** Jihoon Tack, Philippe Laban, Jennifer Neville  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As LLMs become more capable, they are increasingly deployed as collaborative agents, taking on user-delegated tasks through iterative interaction. Yet genuine interaction is inherently dynamic: users rarely specify their intent upfront, instead disclosing, revising, and reshaping it as the conversation unfolds. Despite this, LLMs are still predominantly evaluated or trained in single-turn, fully-specified settings, leaving open a fundamental question: how well do LLMs track and act on user intent as it evolves over the course of a conversation? To study this, we introduce a framework that transforms static, single-turn tasks into dynamic multi-turn conversations in which the user's intent evolves across turns--incrementally revealed, revised, and at times redirected mid-conversation--while preserving each task's original evaluation protocol, enabling existing benchmarks to be reused as controlled testbeds without new annotation. Across multiple tasks, we surface a consistent phenomenon: strong static-setting performance does not transfer to the evolving-intent setting, with substantial drops across model families. Our findings point to a fundamental gap: today's LLMs do not yet faithfully track and act on the user's evolving intent, a capability invisible to static evaluation yet critical for future collaborative agents.

---


### 79. [Adaptive Confidence-weighted Expansion for Trustworthy Multi-Omics Multimodal Fusion](https://arxiv.org/abs/2607.20742)

**<font color=#1a73e8>作者：</font>** Mohammad Raahemi, Ali Sekhavati, Alireza Maleki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal learning is a robust approach to improve predictive performance in applications such as medical prognosis. However, the clinical applicability of models that use multimodal learning is hampered by their poor performance under noisy or uninformative data streams. Present fusion approaches often lack robust mechanisms for the dynamic assessment of data quality and for the provision of a trustable confidence score on the final prediction. This dissuades their deployment in safety-critical settings. To address these limitations, we introduce Adaptive Confidence-weighted Expansion (ACE), a novel framework to enhance the trustworthiness of multimodal fusion models. ACE first enhances the multimodal space by generating new, complementary modalities from intra-modality correlations. It then employs a dual-level confidence mechanism that (1) adaptively reweighs all modalities by their reliability before fusion and (2) estimates a global trust score over the fused, final decision. To evaluate ACE, we used four challenging multi-omics datasets (BRCA, KIPAN, LGG, and ROSMAP). ACE significantly outperforms existing state-of-the-art algorithms in both classification performance and confidence calibration. Our framework provides a more stable and robust data fusion method that facilitates the use of multimodal learning in addressing high-stakes problems.

---


### 80. [GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries](https://arxiv.org/abs/2607.20757)

**<font color=#1a73e8>作者：</font>** Miguel P. Bento, João Seabra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers are known to have internal continuous symmetries that leave outputs invariant, while modifying quantization. GaugeQuant leverages this in-training by introducing a LogSumExp term to the loss that breaks the symmetries, thus selecting a basis that minimizes activation outliers. A stop-gradient operator ensures that only rotation matrices are updated, yielding the language modeling objective completely unaltered. Our requires no specific calibration data, no quantization simulation, and adds negligible training overhead. With the LLaMA-2 7B model under W4A4 quantization with group size 128, perplexity drops from 8.22 to 6.73, competing with post-training methods that require frozen models and calibration datasets. Under W4A16, perplexity drops from 11.16 to 5.45. Code is available at this https URL.

---


### 81. [Rushes: A Human Preference Dataset for Pluralistic Alignment](https://arxiv.org/abs/2607.20767)

**<font color=#1a73e8>作者：</font>** Michael Xu, Jorge Leandro, Sudha Rao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Rushes, a dataset and benchmark for studying revealed human engagement preferences in interactive narrative environments. Rushes is collected through a game interface where users interact with AI-generated branching narratives and select one choice from a small, explicit candidate set at each decision point. Each interaction logs the full candidate set, the user's choice, and the evolving narrative context, yielding time-ordered trajectories with persistent user-level identifiers. Rushes contains 44,226 decision events from 8,167 unique users across six games, capturing sequential, personalized engagement behavior rather than static judgments. We show that user choices exhibit structured, non-random patterns, quantified by a low choice entropy relative to a uniform baseline. We position Rushes as a diagnostic benchmark for pluralistic alignment and demonstrate a robust Engagement Gap: state-of-the-art LLMs, including GPT-5, fail to outperform simple baselines. While classical Matrix Factorization (SVD) captures measurable personalized signal (37.7%), frontier LLMs (34.23%) struggle to even match the Popularity Baseline (36.4%) on event-level choice prediction. This gap suggests that single, population-level objectives, like those used in modern RLHF, appear insufficient to capture heterogeneous, context-dependent engagement signals. As a result, even highly capable models default to majority preferences rather than adapting to individual trajectories. We release Rushes to support research into pluralistic alignment and sequential decision-making in generative systems. The full code for the platform and dataset will be available here: this https URL

---


### 82. [Are Diversity Metrics Measuring Diversity? A Capability-Controlled Audit of Majority-Vote Gain in LLM Ensembles](https://arxiv.org/abs/2607.20768)

**<font color=#1a73e8>作者：</font>** Donghwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Majority voting over LLMs is widely assumed to benefit from diversity, and diversity measures are used to choose which models to combine. We ask whether five such measures track diversity or mainly re-express capability, auditing them as predictors of majority-vote gain over the best member across 31,900 subsets of 30 LLMs on MMLU-Pro (29 on TruthfulQA) under explicit capability controls. Three findings emerge. First, latent complementarity is ubiquitous: oracle gain is positive in 100% of subsets, yet simple voting beats the strongest member in only 9.98% of all canonical size-3 subsets (18.71% with held-out best selection); the pooled size-2-4 rate is 1.27%, partly reflecting deterministic even-size voting behavior. Second, a joint-correctness proxy (strict diversity) is nearly collinear with one minus mean accuracy (size-3 Spearman rho = +0.991 / +0.988); raw diversity-gain associations are strongly capability-entangled and, with one exception, unstable under control. Third, three linear contingency-table statistics are algebraically non-separable; after capability control, the empirically stable remainder is a modest residual pairwise co-failure association in which more shared error corresponds to lower gain. This direction is robust, but its magnitude is configuration-dependent. Joint rawspace linear regressions treating strict diversity, disagreement, and double-fault as independent predictors are rank-deficient by construction.

---


### 83. [Toward Mechanistic Interpretability of an AI Foundation Model Fine-Tuned for Atmospheric Chemistry](https://arxiv.org/abs/2607.20778)

**<font color=#1a73e8>作者：</font>** Jason Y. Hu, Ivan Higuera-Mendieta, Patrick Obin Sturm 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weather forecasting foundation models (FMs) are increasingly fine-tuned to predict air quality, offering fast global pollution forecasts at lower computational cost than conventional chemical transport models. These FMs are typically trained on reanalysis data and generate forecasts through autoregressive rollout. They do not explicitly represent governing physical or chemical processes. Therefore, high forecast skill does not reveal whether a model has learned physical mechanisms or exploits statistical regularities in its training data. Here, we present the first study of what a FM fine-tuned for atmospheric chemistry has learned by examining Microsoft's Aurora model. We impose controlled chemical perturbations on its forecasts and test them against known photochemical relationships. We then examine the internal representations that generate these forecasts. We find that Aurora captures a first-order ozone response to reactive nitrogen but does not enforce the chemical constraints that a process-based model encodes. It generates chemically inconsistent combinations of related species and relaxes localized emission features such as wildfire plumes toward background. Internally, its representations remain largely organized around the meteorology inherited during pretraining, with little structure specific to chemistry. Using sparse autoencoders, we identify internal components that causally control the chemical forecast but do not map cleanly onto individual atmospheric processes. This work provides a framework for testing whether AI forecasting systems learn atmospheric chemistry from reanalysis data. As these models are increasingly positioned to inform environmental policy decisions, we argue that composition forecasts should also be judged by their internal mechanisms rather than by benchmark skill alone.

---


### 84. [Profiling Lightweight Large Language Models](https://arxiv.org/abs/2607.20806)

**<font color=#1a73e8>作者：</font>** Tomohiro Harada, Enrique Alba, Gabriel Luque  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lightweight large language models (LLMs) are increasingly being deployed locally on personal computers and are expected to play a growing role in resource-constrained edge and mobile environments. In such settings, energy consumption, execution time, and memory usage directly affect practical usability, yet existing evaluations of LLM efficiency largely rely on proxy descriptors such as parameter count or FLOPs, often decoupled from task precision. This paper introduces a PTME-based experimental framework for the precision-aware profiling of lightweight LLM inference, jointly measuring Precision, execution Time, peak Memory usage, and Energy consumption through direct hardware-level measurements. The methodology is applied to a representative set of lightweight LLMs executed locally under edge-class resource envelopes on a controlled desktop platform, using benchmarks spanning code generation, mathematical reasoning, and multi-task understanding. We find that static proxy descriptors approximate inference cost well but fail to predict precision. Tightening the resource envelope increases cost without affecting precision, amplifying execution time more strongly than energy and penalizing larger models the most. Moreover, no single model dominates across all PTME dimensions, and a Pareto analysis reveals non-dominated configurations that would be hidden by accuracy-only or efficiency-only assessments, providing practical guidance for selecting models under different resource envelopes. These results show that selecting lightweight LLMs by size, FLOPs, latency, or accuracy alone can select the wrong deployment candidate; PTME profiling exposes configurations that preserve useful accuracy at lower physical cost.

---


### 85. [Enhancing Explainable Cardiac Diagnosis with Guide-Grounded Multimodal LLMs](https://arxiv.org/abs/2607.20814)

**<font color=#1a73e8>作者：</font>** Hai-Nam Duy Vuong, Duy-Anh Bui, Trong-Nghia Nguyen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The electrocardiogram (ECG) is a cornerstone of cardiac as- sessment, yet clinical deployment of deep learning models remains con- strained by limited interpretability and the hallucination risk of large language models (LLMs). Existing CNN+Grad-CAM+multimodal LLM frameworks can generate ECG reports, but their explanations are often only weakly grounded in established diagnostic criteria, reducing trust- worthiness and reproducibility. We propose a guide-grounded multimodal framework that explicitly anchors report generation in curated clinical knowledge. A convolutional neural network (CNN) and Grad-CAM first produce class probabilities and class-specific heatmaps from 12-lead ECG images. In parallel, authoritative ECG textbooks and guideline materials are distilled offline into a structured ECG Interpretation Guide, which is injected as a fixed knowledge block for every sample. Conditioned on the ECG image, Grad-CAM overlay, CNN-derived fact pack, and the in- jected guide, a multimodal LLM generates structured diagnostic reports with guideline-consistent terminology and criteria usage. Experiments on the full PTB-XL test set demonstrate that guide grounding improves se- mantic quality and perceived consistency of generated reports while pre- serving competitive classification performance. In particular, our method increases the average BERTScore of generated impressions from 0.818 to 0.953 relative to a strong CNN+Grad-CAM+MLLM baseline, indicat- ing closer alignment with reference reports. These findings suggest that injecting a distilled interpretation guide into the multimodal prompting pipeline offers a practical pathway to reduce hallucinations and enhance the clinical plausibility of LLM-based ECG explanations, bringing ex- plainable cardiac diagnosis closer to real-world deployment.

---


### 86. [Auditing Provenance Sensitivity in LLM Agent Action Selection](https://arxiv.org/abs/2607.20827)

**<font color=#1a73e8>作者：</font>** Junchi Liao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents choose tools and arguments from context that mixes user requests, tool outputs, retrieved records, memory, and untrusted text. Evidence can be relevant without being authorized to determine a decision, so a correct action need not be grounded only in permitted evidence. We introduce a target-specific authorization audit that labels context factors separately for each tool and argument target. Its primary test holds the task, proposition, position, and policy fixed while changing only the proposition's source authority. We then test behavior when valid evidence is weakened and use context-subset interactions as a secondary localization diagnostic. Across 450 controlled next-action tasks and multiple open-weight LLM families, trusted and untrusted variants produce different actions in 5.4 percent of competing cases versus 1.7 percent of supporting cases. Under controlled degradation, unauthorized competition is retained in a full-correct, mixed-error, clean-correct pattern in 2.4 percent of comparisons, with a 95 percent confidence interval from 2.1 to 3.0 percent. These are controlled stress-set rates, not deployment prevalence. The models respond to textual source-authority cues, but this does not prevent untrusted evidence from influencing their actions.

---


### 87. [Beyond Heavy Log Curation: Perplexity-Based APT Detection via Unsupervised, Context-Augmented Language Models](https://arxiv.org/abs/2607.20832)

**<font color=#1a73e8>作者：</font>** Shoya Otsu, Kei Suzuki, Toshiaki Koike-Akino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advanced Persistent Threats (APTs) remain difficult to detect because only a small fraction of events in large-scale logs are attack-related, and investigation is expensive and hard to scale. Prior machine-learning approaches can reduce analyst workload, but they often rely on heavily curated training data and sophisticated preprocessing pipelines. Building and maintaining such pipelines require substantial domain expertise and engineering cost. Motivated by insights from a study of a strong APT detection baseline, we propose CAPTAIN (Context-Augmented Perplexity-based Threat Activity log detectIoN), a perplexity-based detector that leverages general, pre-trained language models with minimal, domain-agnostic preprocessing, enabling robust scoring of long, minimally processed log entries. CAPTAIN encodes recent history with an encoder model and a Q-Former-style bridge, then injects the compact context tokens into the decoder input so that perplexity reflects temporal context. To improve stability, CAPTAIN additionally applies smoothing filters to the perplexity time series. Across APT-oriented benchmarks, CAPTAIN competes with strong existing baselines and remains robust under substantially less curated inputs, that reduces the development and operational cost of advanced log preprocessing.

---


### 88. [REFACT: Adaptive Fact Restatement for Compact and Faithful Chain-of-Thought Reasoning](https://arxiv.org/abs/2607.20833)

**<font color=#1a73e8>作者：</font>** Zhensheng Jin, Xin Dai, Zhenghao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly rely on long-form reasoning for complex tasks, yet their reasoning traces may drift away from the supplied context when evidence is sparse, noisy, or in conflict with parametric knowledge. Existing grounding methods either attach citations after generation or encourage evidence retrieval inside the trace, but they often do not ensure that cited content is sufficient for the local inference and final answer. We propose REFACT, an adaptive fact-restatement citation framework that trains models to decide when a reasoning step needs contextual grounding and at what granularity source facts should be restated. This design avoids both unsupported inference and indiscriminate fact copying by turning citations into answer-supporting intermediate states. REFACT is optimized with a two-stage SFT-to-RL pipeline in which a citation-utility reward encourages cited facts to be well-formed, source-traceable, and answer-sufficient. Experiments on LongBench, LV-Eval, and ConFiQA show that REFACT improves long-context QA and counterfactual faithfulness while substantially reducing token consumption. Further analysis shows that REFACT preserves more answer-bearing evidence with fewer restated facts, yielding reasoning traces that are denser rather than longer. All code and data are available at this https URL.

---


### 89. [Auditing Evidence Use in Medical LLM Diagnosis](https://arxiv.org/abs/2607.20848)

**<font color=#1a73e8>作者：</font>** Junchi Liao, Jiawen Deng, Fuji Ren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical LLMs are often evaluated by whether they select the correct diagnosis, but diagnostic accuracy alone does not show whether the model used the case evidence appropriately. We present a behavioral audit of evidence use in medical diagnosis. For each case, we decompose patient information into evidence units, score candidate diagnoses under controlled evidence subsets, and mine low-order interactions in diagnostic margins. Because medical evidence is diagnosis-relative, the audit separates interaction discovery from failure assignment: large or negative interactions can reflect plausible differential diagnosis, while suspicious interactions require robustness checks and clinical review. We evaluate five open-weight LLMs on DDXPlus, CupCase, and MedCase. Across datasets, faithful support and differential conflict or cancellation account for most interaction strength, showing that many evidence interactions are clinically plausible rather than failures. In a DDXPlus-focused blinded five-reviewer 130-item enriched review sample, invalid or shortcut-like cases concentrate in negated or absent findings and clinically local evidence. These results show that accuracy can hide candidate evidence-use failures and motivate role-aware audits for medical LLM evaluation.

---


### 90. [Position Bias is Hidden Behind Ceiling Effects: A Permutation Diagnostic for LLM Benchmarks](https://arxiv.org/abs/2607.20864)

**<font color=#1a73e8>作者：</font>** Hiroki Tamba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Position bias in multiple-choice LLM evaluation is widely cited as a confound in capability comparisons, but published measurements rely on single answer-order shuffles whose results confound the bias signal with content-level noise and sampling stochasticity. I introduce inspect_permute, an open-source extension to the inspect_ai evaluation framework that runs exhaustive answer-order permutations per question and reports the chi-squared / Cramer V signature of position bias with bootstrap confidence intervals. I apply the tool across four vendors (gpt-4o-mini, claude-haiku-4-5, gemini-2.5-flash, grok-3) on five MMLU subjects, 24,000 API calls under temperature-0 generation, with falsifier predictions pre-registered via a public SHA-256 hash before half the data was observed. Position bias turns out to be statistically detectable only within a roughly 60-95% base-accuracy Goldilocks zone. Below it, processing-load dominance swamps subject-specific signal; above it, ceiling effects compress the variance below the chi-squared test resolution. Detectable cells separate into two mechanism types: monotone A-to-D decrease (processing_load, in low-tier models) and non-monotone D-drop (content_ambiguity, in a narrow capability band). Standard MMLU places every frontier-tier model above the detection band, so absence of signal there should be read as not measurable, not unbiased. Together with the ceiling-effect characterisation in arXiv:2606.26185, this work brackets the detectable region of position-bias measurement and makes the field central question askable in a verifiable form. Package, data, preregistration under MIT.

---


### 91. [Agentic Designer: Progressive Multi-Agent Collaboration for Structure-Aware Interior Layout Generation](https://arxiv.org/abs/2607.20866)

**<font color=#1a73e8>作者：</font>** Zhijing Yang, Haocheng Lin, Zhihua Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic interior furniture layouts that strictly adhere to architectural constraints (e.g., walls, doors, and windows) remains a fundamental challenge in automated spatial design. Existing approaches, primarily based on one-shot generation using diffusion models or Large Language Models (LLMs), lack explicit mechanisms for intermediate geometric constraint verification, often resulting in structural collisions and functionally infeasible arrangements under complex room constraints. To address these challenges, we propose Agentic Designer, a progressive, multi-agent framework that formulates structure-aware interior layout generation as an iterative and constraint-verified decision process. By decomposing layout synthesis into modular stages of proposal, verification, and adjustment, the framework coordinates three specialized agents, a Generator, an Evaluator, and a Refiner, through a Progressive Consensus Mechanism. This mechanism enforces stepwise geometric validation and correction before each placement is committed, thereby preventing error accumulation. To facilitate this structure-aware paradigm and standardize evaluation, we establish InStruct, a comprehensive benchmark that integrates a dataset comprising over 18,000 high-quality, parametrically annotated samples with a novel suite of structure-centric metrics. Extensive quantitative evaluations, qualitative analyses, and user studies show that Agentic Designer significantly outperforms state-of-the-art methods, demonstrating substantial improvements in strict structural adherence and functional design coherence.

---


### 92. [ViSTR-Bench: Can MLLMs Reason from Continuous Visual Cues in Dynamic Scenes?](https://arxiv.org/abs/2607.20868)

**<font color=#1a73e8>作者：</font>** Han Li, Si Liu, Zehao Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable success across diverse expert-level tasks, but they still struggle with fundamental abilities that humans naturally develop through continuous observation of the real world, such as spatial perception and dynamic reasoning. Recent studies have recognized this gap and introduced dedicated benchmarks to evaluate the spatial-temporal capabilities of MLLMs. However, existing benchmarks mostly focus on static scenes or require exact quantitative predictions, leaving intuitive reasoning from temporal cues largely underexplored. In this paper, we introduce the Visual Spatial-Temporal Reasoning Benchmark (ViSTR-Bench), a novel evaluation suite designed to systematically assess whether MLLMs can perform qualitative reasoning from continuous visual cues in dynamic scenes. Guided by the principles of temporal emphasis, reasoning orientation, and qualitative evaluation, ViSTR-Bench establishes a comprehensive four-dimensional evaluations covering Motion Perception, Spatial Relations, Outcome Prediction, and Physical Dynamics. The benchmark comprises 15 distinct subtasks and 1,340 high-quality video question-answer pairs spanning diverse tabletop, indoor, and outdoor scenarios. Extensive evaluations of a broad spectrum of state-of-the-art proprietary, open-source, and specialized spatial MLLMs reveal that, despite their strong general video understanding capabilities, current models still face substantial bottlenecks in complex spatial-temporal reasoning and remain far below human performance.

---


### 93. [DINO-VPT: Hierarchical Visual Prompt Tuning for Joint Physical-Digital Face Anti-Spoofing](https://arxiv.org/abs/2607.20900)

**<font color=#1a73e8>作者：</font>** Pierre Gallin-Martel, Mika Feng, Koichi Ito 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the increasing diversity of spoofing attacks, there is a growing demand for unified Face Anti-Spoofing (FAS) models capable of detecting both physical and digital threats. While existing Vision-Language Models (VLMs) demonstrate high generalization in this context, they heavily rely on complex multimodal fusion and external text encoders. In this paper, we propose DINO-VPT, a lightweight, vision-only framework leveraging hierarchical visual prompt tuning. By dynamically injecting prompts conditioned on input features via a Prompt Routing Network (PRN), our method effectively disentangles diverse spoofing artifacts without requiring multimodal fusion. Evaluations on the UniAttackData benchmark demonstrate that DINO-VPT achieves higher accuracy than state-of-the-art VLM-based methods. Our results indicate that a properly structured vision-only architecture can achieve state-of-the-art performance in unified FAS without the need for multimodal supervision.

---


### 94. [Delivery, Not Storage: Cue-Anchored Working Memory as a Harness Property for Coding Agents](https://arxiv.org/abs/2607.20972)

**<font color=#1a73e8>作者：</font>** Swapnanil Saha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents ship with one kind of memory: documents. Instruction files, plan artifacts, and auto-written memory directories are deliberately authored and deliberately retrieved: the agent must choose to write them and choose to read them back. Human expertise runs on a second tier that never gets written down: situationally-bound operational facts (gotchas, locations, local conventions) encoded as a side effect of the work and retrieved involuntarily when the situation cues them. We argue this second tier is the load-bearing one for long-running agents and must be a harness property, not an agent choice. We contribute: (1) a two-tier design theory grounded in the cognitive literature on memory offloading, incidental encoding, and event-based prospective memory, each mapped to an architectural requirement; (2) a cue-anchored memory model where memories carry first-class trigger conditions over a composable vocabulary (path, symbol, semantic, event, temporal), evaluated deterministically by the harness, a composition no surveyed academic or shipped system provides; (3) a controlled evaluation on a real coding task showing that voluntary memory use is near zero even with a pre-seeded store (0 memory operations in 114 turns), that deterministic injection delivered in every seeded run with zero false alarms, and that 39% of intra-session re-reads re-buy content paid for before a compaction boundary; (4) a repeated-compaction decay probe: ten facts held only in conversation vanish at the first summary and stay absent from 106 of 108 compactions, and the deprived agent greps the harness's own session files to rebuild them, while the same facts injected from a harness-owned store arrive intact through all 138 compact-resumes as the final summary carries none. Delivery, not storage, is the product: the reliable memory channel for agents is the one the agent never has to think about.

---


### 95. [Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence](https://arxiv.org/abs/2607.20981)

**<font color=#1a73e8>作者：</font>** Jay Gor, Karm Dave, Akshita Abrol 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient multimodal inference is increasingly constrained not only by model quality or FLOP count, but also by the cost of preserving, moving, routing, caching, and quantizing multimodal representations under latency, memory, and energy constraints. This paper reviews recent advances in efficient vision-language and multimodal large language models, covering visual token compression, video token management, KV-cache optimization, Mixture-of-Experts (MoE) routing, low-bit quantization, edge deployment, and hardware-aware benchmarking. We argue that these techniques cannot be treated as independent optimizations. Visual token compression alters downstream feature distributions and MoE routing decisions, routing behavior affects expert utilization and quantization sensitivity, quantized router logits influence expert assignment, KV-cache policies determine retained multimodal evidence, and hardware constraints often transform computational savings into memory and communication bottlenecks. We organize the literature around these interactions and identify key design trade-offs, including accuracy versus token budget, static versus adaptive compression, sparse routing efficiency versus expert collapse, and low-bit inference versus modality-specific degradation. Finally, we introduce Temporal Routing Consistency as a diagnostic for video MoE models and highlight open research directions in routing-aware compression, cross-modal cache management, hardware-aware co-design, and unified benchmarking for multimodal edge intelligence.

---


### 96. [Distribution-Alignment Bridge for Uncertainty-Aware Text-to-Video Retrieval](https://arxiv.org/abs/2607.20984)

**<font color=#1a73e8>作者：</font>** Kyeongmo Chae, Jihoon Lee, Sangtae Ahn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes the Distribution-Alignment Bridge (DAB), a framework that reconceptualizes text-to-video retrieval as a distribution alignment task rather than traditional deterministic point matching. By modeling both text and video embeddings as Gaussian distributions defined by mean and variance, DAB explicitly accounts for modality-specific uncertainty. We employ a deterministic, diffusion-inspired bridge to iteratively refine text distributions toward their target video distributions through a truncated refinement process. This approach unifies probabilistic embedding and distributional transformation into a cohesive, end-to-end trainable system. To optimize cross-modal similarity, we introduce a distribution-aware contrastive loss based on Kullback-Leibler divergence. Extensive evaluations on MSR-VTT, MSVD, and VATEX benchmarks confirm that DAB significantly outperforms existing probabilistic and diffusion-based baselines, while providing calibrated uncertainty-aware ranking through bridge-induced distributional margins.

---


### 97. [HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving](https://arxiv.org/abs/2607.20988)

**<font color=#1a73e8>作者：</font>** Quanfu Yu, Xian Wu, Hao Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models augmented with world modeling represent a promising paradigm for end-to-end autonomous driving. While pixel-level future prediction enables fine-grained spatiotemporal reasoning, it compromises robustness in noisy driving scenarios. Conversely, latent-based world models alleviate this sensitivity but often incur limited interpretability and representational degradation due to absent pixel-level grounding. To reconcile this trade-off, we propose HyWorldVLA, a hybrid world-VLA framework that unifies pixel-level supervision and latent representation learning. In the pre-training stage, HyWorldVLA predicts video latents encoded by a pre-trained video VAE, while simultaneously reconstructing video frames to provide precise pixel-level grounding. During the subsequent co-fine-tuning phase, the model exclusively predicts latent features, which are fed into an action expert to generate trajectories. Extensive experiments on NAVSIM v1 and v2 benchmarks demonstrate that HyWorldVLA significantly outperforms both pixel-based and latent-based world model baselines. Notably, we present the first comprehensive qualitative and quantitative analysis of world model noise robustness in autonomous driving, establishing a new benchmark for evaluating future architectures.

---


### 98. [Where Animacy Lives in Large Language Models: Tracing the Circuits of the Animacy Concept](https://arxiv.org/abs/2607.20995)

**<font color=#1a73e8>作者：</font>** Samuele Punzo, Giovanni Cinà, Sandro Pezzelle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Distinguishing animate from inanimate concepts in written language requires more than shallow text processing, as it involves recognizing complex selectional constraints and contextual cues, such as verb-argument interactions. Yet, current large language models (LLMs) appear to be capable of doing it. We investigate whether this animacy-sensitive behavior of LLMs can be traced to a localized set of causally relevant components and connections. To do so, we construct a controlled dataset of minimal pairs and perform circuit discovery on four open-weight models. Through in-depth experiments and ablations, we show that a causal mechanism responsible for handling animacy in these models does exist, thus discovering an animacy circuit. At the same time, this circuit appears to be less localized compared to other known ones and generalizes only partially across models and animacy tasks, confirming the distributed, context-dependent, and somewhat graded nature of the animacy concept.

---


### 99. [Reexamining zero-shot summarization: Empirical investigation of trustworthiness of LLM-summarizers](https://arxiv.org/abs/2607.21010)

**<font color=#1a73e8>作者：</font>** Vasudha Bhatnagar, Purnima Bindal, Vikas Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Zero-shot summarization using Large Language Models (LLMs) has significantly advanced the abstractive summarization task by producing coherent and fluent summaries. However, underlying stochasticity of the large language models raises concerns about the stability and trustworthiness of the LLM-generated summaries. This issue has become increasingly important due to proliferation of LLM-generated summaries in educational settings, where students and researchers summarize complex academic materials in zero-shot manner.
We propose a novel two-level diagnostic protocol for benchmarking LLM-summarizers based on the stability of the generated summaries. At the lower level, document-level stability analysis is performed over multiple LLM-summaries generated under controlled environment, and the stability coefficient is computed. Each generated summary is scored for semantic and factual alignment with the original document, enabling estimation of stability along more than one dimensions. At the next level, observations from a stratified sample of documents drawn from the corpus are consolidated to estimate the stability index of the LLM-summarizer, which is the proxy for its trustworthiness.
Our empirical investigation of three LLM-summarizers across three genres of documents reveals statistically significant differences in the generation-level variability among LLMs across summary evaluation metrics. This study advances the LLM-summarization research by evidential recognition of the stability problem in LLM-summaries and motivates further research towards development of robust, reliable and trustworthy LLM-summarizers.

---


### 100. [EmoAgent-R1: Towards Multimodal Emotion Understanding with Reinforcement Learning-based Dynamic Agent Specialization](https://arxiv.org/abs/2607.21013)

**<font color=#1a73e8>作者：</font>** Lihuang Fang, Yuchen Zou, kebin Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have achieved impressive performance in multimodal emotion recognition (MER) tasks and lifted MER to a new level that is complex emotion understanding with advanced video understanding abilities and natural language description. However, existing MLLM-based methods often use a fixed prompt to perceive the emotions, ignoring the dynamicity and complexity of the emotion source in the multimodal inputs. To address these issues, we propose a novel Reinforcement Learning-based Dynamic Agent Specialization framework (\textbf{EmoAgent-R1}) to optimize the emotion recognition, reasoning, and generalization abilities of an MLLM with dynamic agent specialization based on reinforcement learning. Specifically, we first adopt a cold start strategy to endow an MLLM with preliminary emotion recognition, reasoning, and agent routing ability by training with synthetic answer-conditioned chain-of-thought data and agent routing data. Then, we further train the MLLM with reinforcement learning to perceive emotions in a two-step agentic workflow with agent selection and agent specialization. To effectively train EmoAgent-R1, we propose a novel Progressive Group-Relative Policy Optimization (P-GRPO) to combine group-based relative advantages with a PMI-inspired progressive token-level modulation to transform sparse rewards into fine-grained learning signals, mitigating the coarse-grained uniform credit assignment issue in GRPO. Extensive experiments on MER benchmarks demonstrate the superiority of our EmoAgent-R1 in stronger emotion reasoning performance and improved optimization stability.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-153](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
