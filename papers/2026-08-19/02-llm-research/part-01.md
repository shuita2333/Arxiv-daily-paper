# 🧠 大模型相关研究 | 2026年08月19日

> 本类共 **358** 篇论文：已确认 **337** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-358](./part-08.md)

---

### 1. [Auxiliary uncertainty signals for LLM-assisted systematic review screening: a benchmark across eight Cohen drug-class reviews](https://arxiv.org/abs/2608.14551)

**<font color=#1a73e8>作者：</font>** Arya Rahgozar, Pouria Mortezaagha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for title-abstract screening in systematic reviews, but their decisions lack calibrated uncertainty. We show that an auxiliary BERT+GCN classifier supplies a structured uncertainty signal that improves LLM screening efficiency, and we identify the prompt-delivery strategy that maximises the benefit-to-cost ratio.
We evaluate five LLM prompt-delivery conditions on eight drug-class datasets from the Cohen (2006) benchmark using 3 seeds x 5-fold stratified cross-validation (600 fold-level results). A BERT+GCN model trained per fold classifies each test paper as INCLUDE, EXCLUDE, or MAYBE via two spectral tests (algebraic radical and categorical paradox). Conditions vary information content (none / label / full scores), selectivity (all papers vs. MAYBE only), and timing (proactive vs. reactive two-pass). A cross-model pilot against gpt-4.1-mini on three datasets tests cross-generation transfer.
Three findings: (i) Full-context delivery yields significant gains in F1 (+0.011, paired Wilcoxon p=0.008) and WSS@95 (+0.050, p=0.039) at a 1.28x token-cost premium, while preserving recall. (ii) MAYBE-only routing is Pareto-optimal: highest mean recall (0.92) and AUC-ROC (0.54) at only 1.05x baseline cost -- one sixth of full-context overhead. (iii) The two-pass design escalates 22.2% +/- 8.8% of records yet never revises its decision (0% flip rate across all datasets and folds), giving decisive evidence that current instruction-tuned LLMs cannot self-triage. The cross-model pilot shows an identical +0.8% recall uplift for both LLM generations. A per-paper ablation across 20,796 observations shows the dual paradox test reduces empirically to a one-line logit-gap criterion. We release the full pipeline; the 600-run experiment replays in under one hour from cached LLM responses.

---


### 2. [Large Language Models Show Metacognitive Sensitivity in Medical Reasoning](https://arxiv.org/abs/2608.14552)

**<font color=#1a73e8>作者：</font>** Ahmad Nazzal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly evaluated and used in medicine, but clinical usefulness depends on answer accuracy and whether confidence tracks evidence quality and uncertainty. We developed a controlled, psychophysics-inspired clinical benchmark to test diagnostic choice and confidence behavior in a medical LLM. The benchmark focused on probable Alzheimer-type neurocognitive disorder (AT-NCD) versus depression-related cognitive impairment (DRCI). We generated 45 synthetic vignettes varying evidence strength, conflicting evidence, and missing information. Each vignette was presented under three prompt variants, yielding 135 trials. In a pilot run with gpt-4.1-nano, all trials produced valid structured outputs. Across forced-choice trials, diagnostic accuracy was 93.5%, mean confidence was 78.4%, and AUROC2 was 0.876. Confidence increased with evidence distance from the diagnostic boundary, decreased when information was missing, and remained higher on correct than incorrect trials after adjustment for evidence strength and prompt format. These findings indicate partial metacognitive sensitivity rather than globally uninformative confidence. However, errors clustered in moderate, conflicting AT-NCD cases, where the model shifted toward DRCI and retained more confidence than empirical accuracy justified. Model comparison suggested that confidence quality should be measured directly rather than inferred from benchmark accuracy or model capability alone. This study establishes a reproducible framework for evaluating evidence sensitivity, metacognitive sensitivity, and localized calibration failure in medical LLMs.

---


### 3. [The Unwritten Benchmark: A New Challenge for Multimodal Machine Learning in Abstract Perceptual Reasoning](https://arxiv.org/abs/2608.14558)

**<font color=#1a73e8>作者：</font>** Garima Arya Yadav, Nilay Yilmaz, Yezhou Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current multimodal models have demonstrated remarkable proficiency in recognizing static visual and auditory content. However, their capacity for abstract perceptual reasoning, inferring unseen information from dynamic, generative processes, remains a critical and underexplored frontier. In this paper, we introduce The Unwritten Benchmark, a new challenge designed to probe this abstract perceptual and cognitive ability. We define the core task as acousto-kinematic word inference: models must decipher words, across 3 different writing styles, being written solely from the audio of pen scratches and the video of hand movements, without any visible ink trace. Our evaluation results reveal a profound gap between human and machine performance: while human participants achieve high ordered letter accuracy (over 80%), leading Multimodal Machine Learning Models, including GPT-4o and Gemini 2.5-Pro, struggle significantly, failing to surpass 10%. Furthermore, we identify a paradoxical fusion effect in the models, where providing both modalities often degrades performance rather than improving it. This finding indicates a fundamental breakdown in their ability to synthesize complementary perceptual cues for this cognitive task. These findings highlight significant limitations in both cross-modal causal reasoning and the understanding of the micro-kinematics essential for such cognitive and intuitive perceptual reasoning.

---


### 4. [Forward Pass Domain Adaptation (Without Cross-Layer Backpropagation)](https://arxiv.org/abs/2608.14563)

**<font color=#1a73e8>作者：</font>** Rivaan Patil, Simon Dennis, Hao Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forward-Pass-Only MLP training (FPO) adapts large language models without a backward pass through the model body, achieving 2.7--3.2x the throughput of standard fine-tuning at ~40% less peak training memory, while leaving off-domain benchmarks within seed-noise of baseline, a property that full-network fine-tuning does not reliably reproduce. FPO rests on a single empirical observation: at late layers of a transformer, the output-layer prediction error approximates the true gradient with cosine similarity 0.47--0.59 across six public models we survey. We introduce a two-minute diagnostic that quantifies this approximation per layer for any model, identifying where late-layer adaptation is viable. Informed by the diagnostic, FPO computes a single error signal at the output and applies it to each target layer. No signal is propagated between layers, and no autograd graph is constructed at any point. We evaluate FPO on three model families (OLMo-2-7B, Qwen3-8B, Falcon3-7B). Across all three, FPO produces in-domain perplexity improvement and leaves MMLU, ARC-Challenge, HellaSwag, and Winogrande within seed-noise of baseline. Localizing SFT to FPO's target layers to enter this regime is also feasible, but at 2.2x the wall-clock cost of FPO.

---


### 5. [Position: AI Lock-In Is in Progress, and We Must Be Prepared](https://arxiv.org/abs/2608.14565)

**<font color=#1a73e8>作者：</font>** Jaeho Kim, Seokhyun Lee, Jieun Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI safety research has mainly focused on two areas: technical alignment (ensuring AI systems produce human-aligned outputs) and the regulation of generative AI's societal impacts (including unemployment risk and labor market disruption). However, an equally important dimension remains underexplored: the risk inherent in dependence on AI systems themselves. In this position paper, we argue that AI safety research should address AI Lock-In, the phenomenon whereby excessive reliance on AI systems leads to human deskilling, diminishes human capacity for independent functioning, and creates systemic vulnerabilities when AI systems become unavailable or compromised. We highlight that AI Lock-In is a systemic threat that is already emerging at individual, societal, and national levels, one that could be dramatically amplified by AI service disruptions or geopolitical conflicts. Drawing on detailed scenarios, we investigate how AI Lock-In emerges and escalates across multiple levels, ranging from individual skill atrophy to national-scale infrastructure failures. To address this, we provide guidance on how such risks can be mitigated and prepared for at each level. We contend that proactively addressing AI Lock-In before such dependencies become entrenched, or even irreversible, is essential for preserving individual autonomy and national security.

---


### 6. [Position: Evaluations of AI Moral Reasoning Still Miss Half of the Picture](https://arxiv.org/abs/2608.14566)

**<font color=#1a73e8>作者：</font>** Aidan Kierans, Ritam Dutt, Kaley Rittichier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work on evaluating the moral competence of large language models (LLMs) has focused primarily on what we call the moral value problem, i.e., whether model outputs align with human moral values. In contrast, the moral norm problem, i.e., whether models can identify and correctly apply context-sensitive moral norms, remains underexplored. We posit that this imbalance stems from the field's reliance on descriptive ethics frameworks, such as Moral Foundations Theory and Kohlberg's stages of moral development, which emphasize value representation over normative application. We review existing benchmarks and evaluation methods, and show that they cluster heavily around the value problem, while discussion regarding normative ethics remains underrepresented. We identify three crucial gaps: (i) the absence of high-quality ground-truth data for moral norms and their applications, (ii) insufficient evaluation of intermediate reasoning processes, and (iii) limited attention to the identification of morally relevant features in context. Subsequently, we propose a research agenda that includes the development of standardized formal representations for normative theories, the construction of expert-annotated datasets capturing norm application, and evaluation protocols that explicitly distinguish between values-level and norms-level competence. Our goal is to encourage a more systematic study of normative reasoning in LLMs.

---


### 7. [HarmProfile: Characterizing Harmful Distributions in Frontier LLMs](https://arxiv.org/abs/2608.14577)

**<font color=#1a73e8>作者：</font>** Zhouyuan Ma, Yutao Wu, Hanxun Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier large language models (LLMs) safety evaluation has largely treated harmful generation as an attack outcome rather than as an object of analysis. Consequently, little is known about the harmful outputs produced during model misbehavior, partly because large-scale, high-quality collections of frontier-LLM misbehavior are difficult to obtain. To address this gap, we introduce HarmProfile, a content-centric benchmark dataset that collects model misbehavior across diverse harm categories and model families, and defines the resulting harmful-output distribution as a model-level risk profile. The premise is that, just as linguistic behavior can be characterized from an utterance corpus, model risk can be characterized from the content, severity, and variation of its safety failures. HarmProfile contains over 80,000 validated artifacts from 23 frontier LLMs across 13 model families, organized into 15 harm categories and 57 subcategories. Using this corpus, we find that frontier LLMs reliably produce harmful content at scale, yet exhibit distinct risk profiles; both harmfulness and diversity grow with model capability, suggesting that frontier LLMs may appear safe yet harbor increasingly dangerous knowledge beneath the alignment surface. Our source code is available at this https URL .

---


### 8. [SKILL: Self-correcting Knowledge-guided Iterative Large Language Model Agent for Logic Optimization](https://arxiv.org/abs/2608.14579)

**<font color=#1a73e8>作者：</font>** Rui Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Logic synthesis optimization poses significant challenges due to exponentially growing search spaces, sparse reward signals, and diverse logic structures. Traditional expert-designed flows lack adaptability, while reinforcement learning (RL) methods often suffer from low sample efficiency and limited interpretability. We introduce SKILL, a Self-correcting Knowledge-guided Iterative Large Language Model Agent that unifies multi-agent LLM reasoning and RL-based environment interaction for automated synthesis optimization. SKILL coordinates three specialized LLMs: GPT-4o for strategic planning, Claude Sonnet 4 for detailed reasoning, and Gemini 2.5 Pro for efficient analysis with a PPO-based RL agent that learns actionable policies through direct interaction with synthesis tools. A novel self-correcting module monitors environment feedback (PDA metrics), detects suboptimal behaviors, and invokes LLM-guided recovery strategies. Evaluations on IWLS, OpenCores, and EPFL benchmarks show SKILL achieves a 12.4 % PDA improvement over expert flows and 86.3% success rate on logic systems up to 500K gates.

---


### 9. [OGX: An Open-Source, Vendor-Neutral Generative AI Application Server](https://arxiv.org/abs/2608.14580)

**<font color=#1a73e8>作者：</font>** Francisco Javier Arceo, Sébastien Han, Matthew Farrellee 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> OGX (Open GenAI Stack) is an open-source AI application server and Python library that implements the APIs of major frontier labs (OpenAI, Anthropic, Google) with pluggable backend providers. Developers building agentic AI applications--such as retrieval-augmented generation pipelines, multi-turn agents, and tool-calling workflows--can develop against a single API surface and deploy with any combination of inference engine, vector database, and safety backend, without changing application code. OGX's primary focus is the Responses API for server-side agentic orchestration, conforming to the Open Responses specification. The server also supports the Anthropic Messages API and Google GenAI Interactions API, decoupling SDK choice from model and deployment decisions. With over 20 inference providers, 13 vector store backends, and a companion Kubernetes Operator for production deployment, OGX serves as the self-hosted, model-agnostic backend for AI-powered developer tools including Claude Code, Codex CLI, OpenCode, and OpenHands. The project has over 8,400 GitHub stars, 242 contributors, and 4,000 commits across nearly two years of public development.

---


### 10. [Euclid-Omni : A Unified Neuro-Symbolic Framework for Plane Geometry](https://arxiv.org/abs/2608.14585)

**<font color=#1a73e8>作者：</font>** Zhaoyu Li, Hangrui Bi, Youyuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Euclidean geometry is a compelling testbed for AI reasoning, as it demands the combination of intuitive diagram understanding, axiomatic deduction, and algebraic computation. Yet, existing approaches typically address only a subset of these abilities or struggle with competition-level problems. We introduce \textit{Euclid-Omni}, a unified neuro-symbolic framework that couples a formal geometry system with Large Language Models (LLMs) and Vision-Language Models (VLMs) to tackle both calculation- and proving-style problems, in formal and natural languages, up to Olympiad-level difficulty. At its core, we develop \textit{Euclidea}, a versatile symbolic geometry solver that automatically generates reasoning steps through deductive inference and algebraic computation. Building on this, we develop a data-generation pipeline that synthesizes symbolic problems and solutions, renders diagrams, and translates them into natural language, producing large-scale, diverse datasets for training LLMs and VLMs across a wide range of reasoning settings. Experiments show that VLMs trained on our synthetic data achieve superior performance on calculation tasks, and that LLMs combined with \textit{Euclidea} are competitive with state-of-the-art systems on Olympiad-level proving problems, despite using orders of magnitude less compute and training data. Code and scripts are publicly available at this https URL

---


### 11. [An Agentic Framework Using Rules and LLMs for Embedding and Annotating Descriptive Document Layouts: A Plant Science Use Case](https://arxiv.org/abs/2608.14587)

**<font color=#1a73e8>作者：</font>** Nicolas Turenne, Youcef Sklab, Eric Chenin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: Recent advances in information retrieval (IR) leverage both dense and sparse representations, large language models (LLMs), and specialized retrieval models to improve ranking accuracy, relevance, and cross-lingual performance. Complementary techniques such as passage indexing, document layout analysis, and semantic knowledge representation further enhance retrieval effectiveness by capturing fine-grained contextual and structural information. Emerging agentic LLM frameworks extend these capabilities by enabling planning, iterative reasoning, tool use, and multi-agent collaboration, thereby broadening applications across diverse domains. These frameworks also emphasize rigorous evaluation, ethical considerations, and trustworthiness, ensuring responsible deployment in real-world settings. We propose a modular, agent-based pipeline for botanical trait extraction. Optical character recognition (OCR) converts PDFs into machine-readable text, while segmentation and indexing organize content by genus and species. Rule-based parsers extract structured botanical traits, and ensembles of large language models (LLMs) expand trait vocabularies and resolve ambiguities. This approach ensures accurate species recognition, scalable annotation, and explainable integration of textual botanical descriptions, enabling robust and interpretable data extraction across large botanical corpora. Results: Using three regional botanical datasets, our system extracted 55,737 trait annotations across 4,961 species, averaging 9.1 traits per species. Integration of LLM-based enrichment improved coverage for 75% of traits, increasing total annotations by 59%. While the choice of OCR engine had a minor effect on species recognition, overall annotation counts remained stable, demonstrating the robustness, scalability, and reliability of the pipeline for large-scale botanical trait extraction.

---


### 12. [The Hallucination Snowball: Modeling Error Propagation as State Transitions in Multi-Agent LLM Pipelines](https://arxiv.org/abs/2608.14588)

**<font color=#1a73e8>作者：</font>** Prabhjot Singh, Bhushan Pawar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sequential multi-agent LLM pipelines chain specialized agents without verification at handoffs, creating a structural flaw with measurable and severe consequences. We show that hallucinations injected at Stage 1 do not merely persist; they transform: raw numerical facts become derived computations, then narrative prose, then editorially approved conclusions. At each transformation, detectability degrades near-irreversibly. We formalize this as the hallucination snowball effect, a first-order Markov process over four states (Raw Fact $\to$ Derived $\to$ Narrative $\to$ Invisible) with empirically measured per-boundary escape probabilities of 24.6%, 48.3%, and 89.3%. Across 346 automatically injected hallucinations in a 4-agent financial analysis pipeline on FinanceBench, gpt-4o detection drops from 72.0% at Stage 1 to 50.9% at Stage 4, and 23.7% of hallucinations survive completely undetected in the final output. Even the strongest model tested (Qwen3.5-397B-A17B, 87.0% at Stage 1) faces a structural ceiling; projected Stage 4 detection is only ${\sim}$60--65%. Critically, boundary gates using identical RAG verification tools reduce hallucination survival from 58.4% to 16.2% versus end-of-pipeline checking (Cohen's $h = -0.911$, $p < 0.000001$), while end-checking alone achieves merely 2.3 pp improvement over no verification. When you verify matters more than whether you verify. Our model predicts survival for $n$-agent linear pipelines and prescribes optimal verification resource allocation: invest at $S_1{\to}S_2$ first, where 75.4% of hallucinations are still catchable, not at $S_3{\to}S_4$ where 89.3% have already escaped.

---


### 13. [Toward Safe LLM Agents: A Survey of Specification, Verification, and Enforcement](https://arxiv.org/abs/2608.14590)

**<font color=#1a73e8>作者：</font>** Pierre Dantas, Lucas Cordeiro, Ehsan Nowroozi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly perform irreversible real-world actions, including database updates, API calls, file operations, and autonomous use of tools. However, no existing system provides formally grounded, task-level safety guarantees for the plans these agents generate. Research remains fragmented across specification, verification, and enforcement, limiting understanding of the strengths and limitations of existing approaches. To address this gap, we conducted a PRISMA 2020 systematic review of 38 studies published between 2022 and 2026 and retrieved from six academic databases. Our analysis reveals four key findings. First, the specification bottleneck remains the primary challenge: natural-language-to-formal translation achieves only 24% to 35% semantic correctness, undermining downstream verification. Second, runtime monitoring is the most mature enforcement strategy, reducing unsafe actions by 40% to 65% in controlled settings, but it does not provide complete safety guarantees. Third, the verifier tax shows that blocking 94% of unsafe actions can still result in less than 5% safe task completion because agents exploit alternative unsafe paths. Finally, no existing approach simultaneously achieves soundness, scalability, semantic correctness, and task-level safety preservation. We contribute a three-level taxonomy, a comparative analysis of existing techniques, a synthesis of evidence on the verifier tax, and a ten-problem research agenda for trustworthy agentic AI.

---


### 14. [Wiola 13M, a Gated Spiral Attention Architecture for Parameter Efficient Small Language Models](https://arxiv.org/abs/2608.14604)

**<font color=#1a73e8>作者：</font>** Aryuemaan Kumar Chowdhury, Praveen Oosa, Vineesha Reddy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models in the ten to one hundred million parameter range are attractive for on device inference, rapid experimentation, and controlled scientific study, yet most of them reuse the standard transformer block without adaptation to the small scale regime. We present Wiola, a decoder only language model whose novelty is concentrated in three drop in components of every layer. First, Spiral Rotary Positional Encoding perturbs the standard rotary frequencies by a slowly growing per dimension factor so that phase trajectories fan outward, improving long range discrimination while adding no parameters. Second, Gated Spiral Attention introduces a per head, content adaptive scalar gate derived from a causal cumulative statistic of the query stream, providing an implicit and differentiable form of soft head selection at negligible cost. Third, the Butterfly feed forward block replaces the conventional expansion layer with a multiplicative interaction and an intra block bypass path, matching the parameter count of a four times gated linear unit block while improving gradient flow in shallow stacks. We formalize each component, derive exact parameter and computation budgets, and prove that the gated attention admits an exact and numerically verified equivalence between full sequence training and cached autoregressive decoding, so that no approximation is introduced at inference time. We also describe a fully reproducible training and evaluation protocol on a standard tiny story corpus. The reference implementation is released as an open source package with weights ready publishing support.

---


### 15. [When Do LLMs Apply the Wrong Law? Diagnosing LLM Failures in Temporal Legal Reasoning](https://arxiv.org/abs/2608.14610)

**<font color=#1a73e8>作者：</font>** Yiqian Huang, Shuyuan Zheng, Qianying Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Legal reasoning tasks such as legal judgment prediction (LJP) require identifying the temporally correct version of the law governing a case -- a capability we term temporal applicable-law determination. However, whether large language models (LLMs) can reliably perform this task remains unexplored. In this paper, we construct a benchmark to evaluate LLMs on temporal applicable-law determination, and systematically investigate why they fail at temporal legal reasoning. Our experiments reveal four key findings. First, LLMs exhibit a strong bias toward applying the most recently enacted law, regardless of when the legally relevant facts occurred. Second, this bias does not stem from an inability to understand that laws have temporal scope, nor from a lack of knowledge about historical statutes. Third, we provide behavioral evidence that reinforcement-learning-shaped explicit reasoning may be a key mechanism: while improving general reasoning ability, it reduces the diversity of reasoning paths, causing models to converge on applying the current law. Fourth, this produces a counterintuitive inverse relationship: models with stronger general reasoning ability tend to perform worse on temporal legal reasoning. Our findings offer concrete guidance for future work on improving LLM performance in temporally grounded legal reasoning.

---


### 16. [Do LLM Agents Negotiate Rationally? A Mechanism-Design Framework for Verifiable Multi-Agent Interaction over A2A/MCP](https://arxiv.org/abs/2608.14613)

**<font color=#1a73e8>作者：</font>** Wael Albayaydh, Rui Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern LLM-agent frameworks increasingly interoperate through standards such as Anthropic's Model Context Protocol (MCP) for agent-to-tool access and Google's Agent2Agent (A2A) protocol for agent delegation and negotiation. However, these protocols specify transport and discovery rather than strategic correctness and do not guarantee efficient, individually rational, or strategy-proof outcomes.
We introduce a framework that (i) encodes classical negotiation mechanisms, including alternating-offers bargaining and Vickrey-Clarke-Groves-style auctions, as constraints over A2A message schemas; (ii) provides a lightweight runtime verification and repair layer that checks messages against protocol invariants; and (iii) offers a benchmark of negotiation and allocation tasks with known optimal solutions for measuring deviations from game-theoretic predictions.
We evaluate multiple LLM backbones using unstructured dialogue, structured protocols, and structured protocols with verification. Across negotiation trials (N=30 per condition), verification reduces outcome variance, while structured protocols achieve 100 percent success for both models. After correcting parser artifacts, audited unstructured baselines achieve approximately 97 percent and 93.3 percent success.
In auction experiments (N=30 per model), both models achieve 100 percent efficient allocation but differ sharply in truthful bidding: one bids its exact valuation in every trial, whereas the other does so in only 3.3 percent of trials. Thus, mechanism-level incentive compatibility does not automatically transfer to LLM-agent behavior. A three-party fair-allocation task produced only 4.2 percent usable outcomes; we report this negative result with a diagnosis. This work bridges classical multi-agent systems theory and modern LLM-agent infrastructure and defines verifiable interaction at the A2A protocol layer.

---


### 17. [DumpsterCluster: From Dumpster Diving to Serving LLaMA-70B on $60 GPUs](https://arxiv.org/abs/2608.14614)

**<font color=#1a73e8>作者：</font>** Zeyu Cao, Xuan Guo, Cheng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As AI datacenters retire functional GPUs, vast quantities of still capable accelerators enter secondary markets. This paper investigates whether these retired GPUs can find a productive afterlife to form a DumpsterCluster that can serve modern LLM inference, and under what conditions such repurposing is economically viable and environmentally sustainable. We physically built a 128-GPU DumpsterCluster from scratch using only second-hand components and ran it for one year. At current market prices (\$22K for the DumpsterCluster vs. \$600K for an 8-GPU B200 system), the economic advantages are substantial. Through pipeline-parallel optimizations, our V100 based DumpsterCluster achieves competitive LLaMA-70B throughput, validating production viability. However, our deployment reveals critical context dependencies. Older GPUs consume significantly more energy per token, making total cost of ownership favorable only in regions with inexpensive electricity. Under grid-average carbon intensity, second-hand systems can produce approximately 4x higher total carbon emissions per token for 8B models, and over 40x for 70B models, compared to current-generation hardware. These findings show that GPU afterlife is not universally sustainable - hardware repurposing must be strategically coupled with low carbon energy sources. When deployed in regions with favourable energy economics and clean electricity, second-hand GPUs offer a viable pathway for expanding AI capacity while advancing affordability, energy security, and environmental responsibility.

---


### 18. [Large Language Models and their Awareness of Mechanics and Spatial Geometry](https://arxiv.org/abs/2608.14615)

**<font color=#1a73e8>作者：</font>** Johannes Gerstmayr, Sebastian Weyrer, Tobias Möltner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) perform well on established code-generation and mathematical-reasoning benchmarks, but their capabilities in mechanics and spatial geometry, here denoted as mechanical engineering awareness, has not been quantified systematically. We present MecEng, a fully automated benchmark that evaluates LLMs on the creation of multibody simulation models from parameterized textual descriptions. The benchmark comprises 84 generic tasks on three difficulty levels, ranging from rigid-body systems with joints and contact to flexible multibody systems that require exact 3D geometry generation, tetrahedral finite-element meshing, and Hurty-Craig-Bampton model order reduction of machine parts. A dedicated pipeline with LLMs generates simulation-ready geometry from text using Netgen, and builds multibody system models for the code Exudyn, which are then verified against expert ground truth on several levels: system-graph isomorphism including graph node annotations, numerical solutions, and part-specific measures such as mass, geometry, and eigenfrequencies. In total, 32 open-weight and two proprietary LLMs are evaluated. On rigid-body tasks, the best open-weight model obtains an overall success rate of 86.0%, compared to 91.4% for the strongest proprietary model, while flexible multibody tasks remain considerably harder. Additional studies quantify the influence of sampling temperature, reasoning, prompt design, model size, and LLM-release date. The results indicate rapidly improving, but still error-prone, mechanical engineering awareness of current LLMs.

---


### 19. [Calibrated Trust, Not Sharper Prediction: An Empirical Test of Uncertainty Fusion](https://arxiv.org/abs/2608.14617)

**<font color=#1a73e8>作者：</font>** Surya Saka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A recurring proposal in legal AI is to improve case-outcome prediction by fusing uncertainty tools (evidence graphs with belief propagation, sequential Bayesian odds updating, Dempster-Shafer combination, and conformal prediction) into one pipeline. We test this on 1,000 real European Court of Human Rights cases from LexGLUE and FairLex, predicting whether the Court found a Convention violation from the case's fact paragraphs. We compare three families across two frontier LLMs (Claude Opus 4.8 and GPT-5.5) as per-fact evidence estimators: (A) the raw LLM, (B) the LLM routed through the fusion pipeline, and (C) a term-frequency baseline through the same pipeline. Across roughly 4,750 tests we find: (1) on discrimination (AUROC around 0.83) the pipeline yields no improvement over either the raw LLM or the baseline; a frontier LLM used directly is the strongest single discriminator. (2) Naively composing an LLM with Bayesian-odds and Dempster-Shafer fusion more than doubles calibration error (ECE from about 0.16 to 0.46) via a prior-mismatch mechanism that replicates across both models. (3) Dempster-Shafer fusion is actively unsafe on long chains, committing confidently to wrong labels at below-chance accuracy; we recommend removing it. (4) The pipeline's genuine value is operational: routed through a conformal selective-prediction layer, the system decides which cases to automate and which to escalate. After removing Dempster-Shafer, recalibrating, and applying class-conditional risk control on the full 1,000-case set, the tuned engine auto-clears at 96.8 percent accuracy with 0.5 percent errors escaping and 96.3 percent caught for review, versus 85.9 / 3.8 / 72.1 for an untuned baseline. The contribution of such pipelines in law is calibrated trust, not sharper prediction.

---


### 20. [AutoMem: A Text-Gradient Recursive Self-Improvement Framework for Automated Memory Architectures Search](https://arxiv.org/abs/2608.14621)

**<font color=#1a73e8>作者：</font>** Lin Du, Jie Zhou, Yuxuan Cai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is increasingly central to LLM agents, yet memory design remains a highly coupled architecture problem: what to encode, how to store it, how to retrieve it, and how to manage it can vary substantially across tasks and backbone models. We construct a discrete search space with 5 encoders, 5 stores, 6 retrievers, and 4 managers, and show that no single memory architecture consistently dominates: different tasks favor different module combinations, leading to substantial performance gaps. Motivated by this, we propose \textsc{AutoMem}, a text-gradient recursive self-improvement framework for task-adaptive memory architecture search. \textsc{AutoMem} optimizes over the factored space through two components: Experience-Guided Architecture Search, which proposes candidate architectures from historical search trajectories and accumulated reflections, and Failure-Guided Module Diagnosis, which localizes memory-related failures to specific modules and converts them into targeted textual feedback. Experiments on GAIA, WebWalkerQA, and xBench-DeepSearch across two LLM backbones show that \textsc{AutoMem} consistently discovers task-adaptive memory architectures that outperform the strongest human-designed memory baselines, improving accuracy by $2.8$ points on average across six benchmark-backbone settings. Further analysis shows that \textsc{AutoMem} achieves a favorable accuracy-efficiency trade-off, reducing token cost by $14.3\%$ over the strongest accuracy baselines under Qwen3.5-122B-A10B, while also finding stronger architectures than substantially larger random searches within only a few guided iterations.

---


### 21. [A Human-Centred Approach to Benchmarking LLMs for Parenting Advice](https://arxiv.org/abs/2608.14622)

**<font color=#1a73e8>作者：</font>** Yunke Zhao, Isobel Voysey, Alastair van Heerden 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People are increasingly using large language models (LLMs) to seek advice, including for parenting. Parenting is a critical and socially sensitive domain. Thus, evaluating advice provided by LLMs requires indicators beyond aggregated information quality benchmarks to consider relational and behavioural elements of the responses. With a multi-dimensional rubric created by parenting experts, this paper evaluates 15 LLMs across 100 parenting scenarios in 2 languages (English and Chinese), using an LLM-as-a-judge method. Results show that aggregate scores can hide rubric item-specific weaknesses, models implicitly encourage different parenting styles, and language influences responses. We highlight the importance of evaluation output auditability and challenges involved in evaluating LLM-generated advice in domains like parenting. Our findings provide important insights for selecting LLMs for direct user engagement and the development of user-facing parenting advice applications.

---


### 22. [Learning Agent Execution for KV-Cache Management in Agentic Serving](https://arxiv.org/abs/2608.14624)

**<font color=#1a73e8>作者：</font>** Rui Zhang, Chaeeun Kim, Shaoting Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems have emerged as an important deployment paradigm for AI services, where each user request is decomposed into a sequence of specialized agents. Across these workflows, every agent repeatedly executes a fixed context consisting of system prompts, tool definitions, and few-shot examples, creating substantial opportunities for KV-cache reuse. Existing LLM serving systems, however, manage KV-cache reactively using prefix caching and recency-based replacement, causing reusable agent contexts to be evicted before their next invocation and forcing repeated recomputation. We present CacheScout, an agent-aware KV-cache runtime layer for multi-agent LLM serving. The key insight is that future KV-cache reuse is governed by agent execution semantics rather than cache recency alone. CacheScout captures these semantics by learning agent execution transitions online, without requiring predefined workflow graphs or offline training, and uses the learned execution model to guide both cache eviction and proactive prefetching while leaving the serving critical path unchanged. We implement CacheScout on top of vLLM. Across representative real-world multi-agent workloads, CacheScout improves KV-cache hit rate by 10-18 percentage points, reduces mean TTFT by 18-45%, lowers mean per-turn latency by 29-38%, and increases peak throughput by up to 57%. These benefits also generalize to larger models, reducing TTFT by up to 54% while sustaining 37% higher throughput.

---


### 23. [Characterizing Rhetorical Misalignment in Decision-Making with Language Models](https://arxiv.org/abs/2608.14630)

**<font color=#1a73e8>作者：</font>** Zirui Cheng, Joey Chan, Simo Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human decision-making is often shaped by a range of well-documented cognitive biases. As large language models (LLMs) become increasingly integrated into high-stakes human-AI decision-making, it is important to understand whether their outputs can amplify potential biases, how this influences human decisions, and crucially, whether it can lead to harmful consequences. In this work, we develop a decision-theoretic framework to study rhetorical misalignment, a failure mode where an LLM uses rhetorically inappropriate forms of presentation for a given decision context, thereby inducing suboptimal human decisions. We empirically investigate this phenomenon through a human-subject experiment in realistic clinical decision-making using a dataset curated from the United States Medical Licensing Examination. By measuring how LLM-generated information affects decisions, we observe that LLMs induce an average 2.81% rate of harmful decision flips across different models, where clinician participants change from a correct to an incorrect answer. Rationales reported by participants provide evidence that these revisions are closely related to the language used by LLMs that may induce different types of cognitive biases, including anchoring, authority bias, and loss aversion. To enable scalable evaluation, we instantiate our theoretical framework using decision-makers simulated by LLMs to computationally measure rhetorical misalignment. Our findings reveal a safety concern previously unrecognized in high-stakes domains: a model can be factually aligned yet still induce harm through its rhetorical presentation.

---


### 24. [Accuracy and Reliability of Large Language Models in Cosmetic Chemistry and Skin Health: A Benchmarking Study](https://arxiv.org/abs/2608.14631)

**<font color=#1a73e8>作者：</font>** Amelia Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As consumers increasingly turn to AI chatbots for skincare advice, the technical accuracy of Large Language Models (LLMs) in cosmetic chemistry remains largely under-evaluated. We benchmarked 14 LLMs on a structured set of topics related to cosmetic chemistry, including the chemical properties of specific cosmetic ingredients and common cosmetic scenarios that may be of interest to consumers. Web search was disabled throughout to assess each model's internalized knowledge rather than its internet retrieval capacity. Overall performance was poor, with the most pronounced deficits in quantitative reasoning and structural identification tasks. While models handled general skincare questions with reasonability, responses consistently lacked the technical depth required for informed consumer decision-making. Notably, conversation with AI can pose a risk: outputs that sound authoritative but contain technical errors are less likely to generate skepticism compared to responses that explicitly acknowledge uncertainty. These findings suggest that general-purpose LLMs, trained predominantly on unverified public data, are currently not reliable sources of cosmetic chemistry information. Progress on two fronts, fine-tuning verified chemical and dermatological datasets, and substantial improvements to algorithmic reasoning, will likely be needed before these tools can be considered as resources for public use.

---


### 25. [DeMTS: Denoising Trajectories as Multivariate Time Series for Hallucination Detection in Diffusion Language Models](https://arxiv.org/abs/2608.14632)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Yili Wang, Yue Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (D-LLMs) have emerged as a promising paradigm for text generation. However, similar to autoregressive LLMs, D-LLMs remain vulnerable to hallucinations, where fluent outputs may contain factually incorrect or unsupported content. Although existing hallucination detection methods for D-LLMs attempt to leverage uncertainty trajectories of the denoising process to better identify hallucination signals, they typically compress the trajectories along either the temporal or token dimension, overlooking the useful information encoded in the complete two-dimensional token-step structure. Consequently, they may fail to capture hallucination-relevant patterns, such as inconsistent convergence and cross-token fault propagation, leading to suboptimal detection performance. To bridge this gap, we propose a D-LLM hallucination detection framework that formulates the Denoising trajectories as Multivariate Time Series over learnable latent variables (DeMTS for short). DeMTS employs a trajectory-preserving token-to-variable assignment module to convert token signals into stable latent variables. Based on these variables, we propose dynamic multivariate temporal modeling to progressively integrate inter-variable dependency modeling with temporal encoding for hallucination prediction. Extensive experiments on two D-LLMs backbones and three benchmarks demonstrate that DeMTS outperforms existing hallucination detection methods while maintaining strong robustness, efficiency, and cross-task transferability.

---


### 26. [Valid Per-Field Selective Risk Control for Document Extraction: Three Failure Modes, a Validity Ladder, and When Conditioning Pays](https://arxiv.org/abs/2608.14639)

**<font color=#1a73e8>作者：</font>** Bhaskar Gurram  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Per-field accept/review with selective risk at most alpha -- accept a field only if the error rate among accepted fields is controlled -- is the trust contract document-extraction systems need, and the natural procedure silently violates it on real documents. On 13,859 genuine claude-sonnet-5 fields from 800 CORD receipts (49.0% correct) we diagnose three failure modes: document clustering (design effect 1.84-2.45), score-refit leakage (coverage 0.416 at risk 0.127, violating alpha=0.10 in 95% of splits), and a tie-mass pathology (a degenerate score collapses the threshold grid, 0.030 to 0.001). We organize the fixes as a validity ladder, guarantee form stated per tier. A fit/val split protocol restores expected-selective-risk control for a learned fusion: coverage 0.318 at risk 0.096 at nominal alpha=0.10, no tolerance band (production variant 0.326) -- an on-average point whose realized risk exceeds alpha in 47.5% of resplits, not a certificate. Mondrian Learn-then-Test with exact binomial tails yields per-group PAC certificates: field-iid 0.171 at risk 0.068, cluster-corrected 0.140, doc-iid 0.060 -- the only tier matching documents, honestly near-vacuous today. Support-bin, the pre-specified provenance taxonomy, wins every rigor tier on the sonnet CORD capture (p<1e-4, Bonferroni-corrected) -- a win that does not replicate on the same documents under haiku or qwen -- while on higher-accuracy corpora pooled thresholds win: conditioning helps exactly where pooled cannot certify, subsumed by a learned score elsewhere. A frozen-configuration confirmation on selection-untouched claude-haiku-4-5 held at both risk levels, and a blind three-annotator human-gold audit verifies the practical tier's accepted-set risk at 1.3% against its 10% budget (Fleiss' kappa=0.83; labels err one-sidedly pessimistic). Released Apache-2.0 with seed-pinned, regression-gated procedures.

---


### 27. [DUET: Dual-Teacher On-Policy Distillation via Same-Weight Disagreement for Prohibition Compliance](https://arxiv.org/abs/2608.14644)

**<font color=#1a73e8>作者：</font>** Zihan Li, Feifei Li, Wenhui Que  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world LLM deployments increasingly rely on runtime-injected prohibitions--enterprise policies, PII redlines, tool boundaries--that vary per request and per tenant. Conventional post-training is structurally ill-suited: SFT hides the violation signal in compliant labels, and DPO's sequence-level preferences mismatch token-localized violations. We propose DUET, a token-selective on-policy distillation method for prohibition compliance. DUET pairs a teacher that sees the prohibition (positive) with an identical-weight teacher that does not (negative). Because the two teachers differ only in prohibition visibility, their per-token disagreement isolates the prohibition's causal effect--yielding a clean supervision signal uncontaminated by model capacity or mismatch. This disagreement drives two complementary mechanisms: signal cleaning, which discards agreement tokens as redundant or prefix-corrupted, and preference-directed learning, which pushes the student away from the negative teacher and toward the positive one at token granularity, embedding DPO-style optimization directly into OPD without offline preference data. We construct an industrial Prohibition-Compliance benchmark spanning five task families covering explicit-refusal, paraphrase robustness, and over-refusal. Across 1.5B-8B Qwen variants, DUET achieves 72.3-85.2% violation compliance while preserving 88-93% normal utility, dramatically outperforming teacher model and other distillation baselines. External evaluation on SysBench confirms improved safety alignment with minimal degradation on GSM8K and MATH-500.

---


### 28. [SMOPD: Selective Token-Entropy Masking for Dirty-History Multi-Turn On-Policy Self-Distillation](https://arxiv.org/abs/2608.14647)

**<font color=#1a73e8>作者：</font>** Chenyang Jiang, Changhan Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dirty-history rollouts make multi-turn on-policy self-distillation (OPSD) brittle: once a student emits an erroneous intermediate reply, later turns are conditioned on that reply, and uniform distillation can spend loss on tokens that carry little corrective signal. We introduce SMOPD (Selective Masking for On-Policy Distillation), a loss-only stabilization method for multi-turn OPSD. For each generated middle-turn reply, SMOPD ranks token positions by student entropy and removes the lowest-entropy 20% from the clipped generalized Jensen-Shannon distillation loss; final-answer and FULL-preservation losses are unchanged. This design targets token-level uncertainty rather than coarse trajectory outcomes, adds no parameters, and has zero inference-time overhead. We compare SMOPD with a correctness-scaling variant that multiplies a common detached reliability proxy using final-answer correctness. On LiC with Qwen3 models, SMOPD improves SHARDED-view accuracy by 1.0-2.5 percentage points in single-seed 1.7B, 4B, and 8B comparisons, and a small 4B multi-seed check shows a +1.7pp mean SHARDED gain over baseline (two-tailed p = 0.022). Adding the outcome scalar is harmful without masking at 1.7B (-4.0pp) and remains scale-dependent when combined with masking (+1.3pp at 4B, neutral at 1.7B, and -0.5pp at 8B). These archived aggregate results suggest that token-level uncertainty is a more reliable stabilization signal than scalar final-answer correctness in this evaluated dirty-history OPSD setting, while leaving causal mechanism tests and broader benchmark validation to future work.

---


### 29. [Discrete Diffusion Language Models Are Training-Free Multi-Label Classifiers](https://arxiv.org/abs/2608.14649)

**<font color=#1a73e8>作者：</font>** Pawan Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present dLLM-SetScore, a training-free method that uses discrete masked-diffusion language models for multi-label text classification. For each candidate label, it asks a short yes/no question and compares the probabilities of the two answer tokens at one masked position. The method uses no task-specific fine-tuning or training on textual-entailment datasets; a 200-example labelled validation slice selects thresholds, temperature, and prompt wording.
We first show that placing all labels in one prompt creates a strong slot-position asymmetry: the first answer slot is predicted positive on $99.4\%$ of GoEmotions examples and $100\%$ of Reuters examples. Per-label scoring places every label in the same syntactic position, making predictions invariant to label order and avoiding this artifact. We evaluate LLaDA-8B and Dream-7B on six datasets against NLI models, an autoregressive LLM, SetFit, and supervised classifiers. On the five datasets shared by both diffusion families, Instruct checkpoints improve macro-F1 in 9 of 10 comparisons and micro-F1 in 8 of 10, although these comparisons do not identify the cause. Within our protocol, LLaDA-Instruct records the highest training-free values for both Reuters and ECtHR metrics. We prove permutation invariance, characterize thresholded decisions under weighted Hamming loss, and derive shortlist ceilings for recall and F1. An exploratory local Joint Set Refinement step lowers F1 from biased and unbiased initializations and is retained as a negative result.

---


### 30. [Evaluating Multimodal LLMs across Text and Audio Modalities for Accessible Disaster Assistance](https://arxiv.org/abs/2608.14651)

**<font color=#1a73e8>作者：</font>** Anuridhi Gupta, Samara Mansoor, Hemant Purohit  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective disaster risk communication is a foundational humanitarian challenge, yet current emergency infrastructure fails to meet the needs of individuals with access and functional needs, including hard-of-hearing individuals, pregnant women, mothers with toddlers, and elderly individuals with dementia. Recent advancements in Artificial Intelligence (AI), especially Multi-Modal Large Language Models (MM-LLMs), demonstrate powerful capabilities to serve diverse users across text, audio, image, and video modalities within a single unified system, such as a chatbot. However, their suitability for deployment rests on a property that receives limited scrutiny, i.e., whether these systems produce consistent, actionable outputs regardless of the modality through which a user communicates. In this paper, we conduct a comprehensive analysis to understand the status of open-weight MM-LLMs using real emergency alert scenarios across four different vulnerable personas. These state-of-the-art (SOTA) models are evaluated on consistency of responses across text and audio modalities when the same task scenario is given. Findings indicate that no model achieves reliable consistency across modalities, and that performance gaps are heightened for personas with access needs, introducing modality-dependent inequity that undermines the humanitarian value of these systems. These results inform concrete design recommendations for building equitable, trustworthy, and inclusive AI tools for disaster risk communication.

---


### 31. [Do Uncertainty Signals Help? A Systematic Study of Uncertainty-Aware Decoding with Rollback Mechanisms](https://arxiv.org/abs/2608.14653)

**<font color=#1a73e8>作者：</font>** Xianzong Wu, Xiaohong Li, Yuejun Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prediction uncertainty is a widely adopted metric for quantifying model confidence, with downstream applications spanning model explanation, data selection, and prediction rollback. Despite its demonstrated utility, the potential of uncertainty quantification to enhance code generation in large language models (LLMs) remains largely underexplored, raising a critical question: to what extent can uncertainty serve as an effective signal for improving LLM-based code generation?
To answer this question, we study uncertainty-aware rollback decoding, an inference-time strategy that uses uncertainty signals to identify unreliable generation regions and roll back to earlier valid prefixes without retraining the model. We evaluate this framework on seven code LLMs, five code generation benchmarks, and eight token-level uncertainty signals under a unified decoding setup.
Our results show that the complete rollback framework improves over equal-budget restart across the evaluated benchmarks and model settings, with gains of up to 0.26 in pass@1 and 0.35 in AvgTestPassRate on functional code generation benchmarks, and an absolute improvement of up to 6.4\% in Patch-Aligned Safe Rate on Dsec-Python. Among the evaluated signals, information-theoretic measures such as token entropy and negative log-likelihood show the most favorable overall trend, frequently achieving the best or near-best results on standard benchmarks. A component-controlled ablation further shows that feedback-guided rollback provides the main improvement, while uncertainty localization provides an additional gain when checking, budget, rollback, and branch decay are held fixed.

---


### 32. [Diagnosing and Mitigating Perception-Decision Misalignment in Omni-LLMs via Modality Subspace Activation](https://arxiv.org/abs/2608.14655)

**<font color=#1a73e8>作者：</font>** Hongbo Jiang, Jie Li, Yunhang Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Omni-Large Language Models (Omni-LLMs) power complex multi-modal reasoning in applications like World Action Models and autonomous agents. However, their strong performance often masks a profound Perceptual-Decision Misalignment (PDM), where decisions remain unfaithful to multi-modal perceptions. To diagnose this, we formalize Causal Modality Sensitivity (CMS), operationalized via a dual-lens framework: Answer Retention Rate (ARR) at the macro behavioral level, and Logit Angular Discrepancy (LAD) to track microscopic distribution shifts. We also curate CausalMSBench, a diagnostic dataset isolating language priors. Benchmarking reveals that popular Omni-LLMs exhibit critically low CMS, showing negligible distribution shifts even when key modalities are removed. To rectify this, we propose Modality Subspace Activation (MSA), a training-free inference-time framework that uses Singular Value Decomposition (SVD) to estimate modal activation strengths. MSA dynamically balances modal projections in the last hidden state, effectively restoring CMS across benchmarks.

---


### 33. [When Uncertainty Isn't Enough: An Empirical Study of Self-Correction in Code Generation](https://arxiv.org/abs/2608.14659)

**<font color=#1a73e8>作者：</font>** Pranav Rakasi, Maanas Lalwani, Arnav Srivastava 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models for code generation often produce incorrect solutions without reliable indicators of failure. We study whether uncertainty estimation methods developed for natural language transfer to code generation, and whether such signals can improve code generation via selective self-correction. We evaluate five uncertainty methods: mean token entropy, verbalized confidence, $P(\text{True})$, entropy ensembles, and semantic entropy probes, across three small code LLMs on HumanEval and BigCodeBench. We find that multi-sample $P(\text{True})$ achieves the strongest correlation with correctness, while all the other methods, including semantic entropy probes, yield only weak correlation. We then use these uncertainty signals to drive three self-correction policies: adaptive decoding, uncertainty-based regeneration, and verification-based regeneration. Our results reveal a stronger negative finding than anticipated: uncertainty-based self-correction fails to reliably improve Pass@1, degrading accuracy in 5 of 6 configurations across both benchmarks ($-3$pp to $-10$pp), and adaptive decoding degrades accuracy in 4 of 6 configurations. Only verification-based self-correction reliably improves Pass@1, with gains of $+6$ to $+26$ percentage points on HumanEval and $+8$ to $+20$ percentage points on BigCodeBench, scaling inversely with baseline strength. These findings replicate consistently across both benchmarks and suggest that cheap uncertainty estimators are insufficient on their own to improve code correctness, and that their practical value lies in serving as gating signals for costlier execution-based correction loops rather than as standalone substitutes for verification.

---


### 34. [In-Context Learning to Assess Built Environment Impacts on Perceived Neighborhood Walkability Among Mobility-impaired Older Adults](https://arxiv.org/abs/2608.14663)

**<font color=#1a73e8>作者：</font>** Houhao Liang, Kresimir Friganovic, Joanne Kua 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As global populations age, enhancing neighborhood walkability through inclusive urban design is important for mitigating built environment (BE) barriers that discourage physical activity and social participation among older adults. This study investigates the utility of in-context learning (ICL), using the transformer-based foundation model TabPFN, to determine how BE features influence perceived walkability, as measured by the Neighborhood Environment Walkability Scale (NEWS-A) survey. Using a small-scale dataset (N = 257) comprising a unique demographic of older adults with knee osteoarthritis or a history of falls, TabPFN achieved a macro F1 score of 54.89% for walkability perceptions categorized as Low, Neutral, and High using equal-width binning. This result outperformed optimized, grid-searched baseline models, including Random Forest (45.85%) and XGBoost (50.56%). To interpret these results, we employed Shapley Interaction Quantification (SHAP-IQ) to identify the hierarchical importance of feature interactions. Preliminary results revealed that the model's predictive logic was primarily driven by higher-order interactions. For example, the interaction between average street circuity and the ratio of drivable roads emerged as the primary discriminator of perceived walkability. Neighborhood greenery was found to have substantial predictive importance only when combined with an individual's fear of falling or perception of age-friendliness. Overall, ICL using TabPFN demonstrates superior performance on small-scale datasets, enhancing the fidelity of the resulting interpretive insights. Furthermore, SHAP-IQ provides a synergistic perspective on how higher-order feature interactions drive the model's predictions.

---


### 35. [Quantifying Depth Sufficiency in Residual Neural Networks: A First-Order Criterion](https://arxiv.org/abs/2608.14664)

**<font color=#1a73e8>作者：</font>** Zeyu Liu, Jinhao Zhang, Yunquan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How can we determine whether a trained neural network is already deep enough? We study this under a fixed function-preserving residual-growth protocol specifying insertion locations, residual families, zero-output initializations, and zero-state first-order updates. We define first-order residual depth saturation as the absence of a strict local decrease from every admissible insertion. We prove residual non-degeneracy is necessary and sufficient: additional depth has first-order value exactly when conditional activation gradients have a nonzero projection onto at least one admissible residual tangent space. This boundary is shared by descent-compatible zero-state updates and invariant under regular local reparameterizations preserving that tangent space. Under residual-signal realizability, raw activation-gradient vanishing exactly certifies saturation. Across ResNets, GPT-2-style models, and continued-pretrained Pythia checkpoints, the maximum activation-gradient norm decreases toward a low-signal regime with depth. Function-preserving growth also achieves converged performance competitive with training from scratch. These results support activation-gradient magnitude as a conservative diagnostic of the remaining empirical first-order value of residual depth.

---


### 36. [When Does the Best Sampling Temperature Rise with the Budget? Sufficient Conditions for Pass@k](https://arxiv.org/abs/2608.14665)

**<font color=#1a73e8>作者：</font>** Changsu Jeong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The temperature that maximizes pass@$k$ is often low for a small sampling budget and higher for a large budget. This pattern has been reported from Codex through recent multi-sample inference studies. It is not an algebraic property of pass@$k$: as Slocum et al. (ICLR 2025) observe, for one fixed task the maximizing temperature is independent of $k$. Building on that fixed-task observation and the hard/easy-task explanation, we give a formal population-level sufficient condition for the aggregate pattern. For task $X$, let $p_t(X)$ be one-sample success probability at temperature $t$, and define the conditional log-success response $m_t(u)=\mathbb{E}[\dot p_t(X)\mid p_t(X)=u]/u$. If $m_t(u)$ is nonincreasing in current success probability, then the normalized temperature derivative of aggregate pass@$k$ is nondecreasing in $k$. Consequently, derivative signs are nested across budgets; if each temperature-performance curve is strictly single-peaked, its unique maximizer is nondecreasing in $k$. The proof identifies the mechanism as a monotone-likelihood-ratio power tilt toward lower-success tasks. We derive a closed-form two-stratum phase diagram, including upward and downward regimes, and show that the marginal temperature derivative admits an exact $\mathrm{Beta}(2,k)$ kernel representation whose kernel concentrates at one-sample success of order $1/k$. Interpreting that scale as task-level localization additionally requires a regular, nonvanishing density-response factor near zero. A signed-moment representation yields diagnostic shape restrictions, while a short appendix records exact discrete refinements of the existing multi-configuration allocation formulation. No language model is trained, and no model query is used as an experimental measurement: the contribution is a conditional theory of an established empirical phenomenon, with assumptions that can be tested in future work.

---


### 37. [Position: AI Agents in Scientific Teams Should Be Studied as Human-Agent Systems](https://arxiv.org/abs/2608.14667)

**<font color=#1a73e8>作者：</font>** Patrick Emami, Sameera Horawalavithana, Truc Nguyen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model-based agents are increasingly deployed as collaborators in scientific discovery yet most current work focuses on the autonomous capabilities of "AI Scientists". We argue that this overlooks the social aspects of scientific teamwork, and that studying AI Scientists as human-agent systems (HAS)--where the unit of analysis is the human-agent pair--is both underexplored and undervalued. We establish these points through literature and empirical analysis, and highlight recent incidences and studies which show that deploying agents in science without accounting for human-agent dynamics introduces near-term risks, including reduced diversity of scientific inquiry. Through analysis of real-world case studies, we show that scientists and agents can augment each other's capabilities. We call for new research that adopts the HAS lens to develop mathematical frameworks for understanding and fostering human-AI synergy in scientific discovery.

---


### 38. [BRA-Audit: Budgeted Runtime Auditing for LLM Multi-Agent Systems via Cumulative-Exposure Audit-Point Placement](https://arxiv.org/abs/2608.14668)

**<font color=#1a73e8>作者：</font>** Kaixiang Wang, Yidan Lin, Jiong Lou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (LLM-MAS) solve complex tasks through specialized collaboration, but inter-agent dependencies can propagate hallucinated or malicious outputs into system-level failures. Auditor agents mitigate these risks, yet existing strategies face an efficiency dilemma: end-only auditing reviews long trajectories and final outputs, potentially weakening audit effectiveness and enlarging rollback scope, while auditing every agent each round improves detection and localization at high token cost. How can guard performance be preserved while minimizing token cost? To address this problem, we propose BRA-Audit, a budget-aware runtime auditing framework that models MAS execution as a dynamic dependency graph and formulates audit scheduling as audit-point placement under a fixed audit-call budget to minimize cumulative unchecked exposure. Its greedy scheduler prioritizes influential and long-unaudited regions, while trusted audit points enable localized recovery. Across structured coordination, complex reasoning, and open-ended tasks, BRA-Audit restores performance close to the clean setting, remains competitive with heavy guard methods and reduces end-to-end token consumption by \(17.2\%\)--\(40.6\%\).

---


### 39. [Beyond Correctness: Toward Automated Novelty Verification with Lean 4](https://arxiv.org/abs/2608.14669)

**<font color=#1a73e8>作者：</font>** Ayrton Porto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems applied to mathematics verify correctness but not novelty: an automatically generated theorem can compile in Lean without errors and yet be an already known result. This article presents AViD Journal, a pipeline that receives a LaTeX article, formalizes its statements in Lean 4, and issues a novelty verdict through a decision tree over three dimensions: prior existence in a formal corpus (Mathlib) and an informal one (TheoremSearch and Matlas, with temporal filter and LLM judge), non-triviality via automatic tactics, and structural distance between proofs measured as Jaccard distance over premise sets.
Evaluation on papers withdrawn from arXiv due to declared duplication produced a result more informative than any performance measure: the identification of three obstacles that limit the approach regardless of this implementation. First, successful compilation of a Lean file does not guarantee semantic fidelity. Second, the recall ceiling is imposed by the coverage of theorem indices, not by the similarity metric. Third, arXiv removes the source code of articles upon withdrawal, compromising the reproducibility of any benchmark built upon them.

---


### 40. [When Agentic Executions Fail: Detecting and Localizing Runtime Faults from Telemetry](https://arxiv.org/abs/2608.14680)

**<font color=#1a73e8>作者：</font>** Chenkai Zhang, Yiran Li, Yifang Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliability in LLM-based agentic systems is a property of the whole execution (its tool calls, model calls, guardrails, and inter-agent messages), not of the final answer alone, yet evaluating only task outcomes reveals little about how or why a run fails. We present AGENTCHAOSBENCH, a benchmark for detecting and localizing runtime faults in agentic systems from their execution telemetry. We run five heterogeneous applications that coordinate agents over the Agent-to-Agent protocol and call tools through the Model Context Protocol, and inject ten types of operational fault (unavailable or slow tools, corrupted or oversized responses, and delayed, looped, or misrouted delegations and bypassed guardrails) at their tool, model, guardrail, and inter-agent boundaries, alongside a no-fault control. The resulting dataset contains 275 sanitized traces: 250 faulty executions spanning ten fault types and 25 no-fault controls. Each faulty trace is aligned with the no-fault execution of the same input; fault-type labels and, where applicable, location labels are held out from diagnosis. On structured single-trace inputs, a first set of zero-shot LLM baselines shows the task is far from solved: local detectors up to 14B parameters reach only 13.6-19.2% top-1 fault-type accuracy and the frontier DeepSeek-v4-pro only 24.8%, while jointly identifying the fault type and its location tops out at 22%; reference-dependent faults (above all a bypassed guardrail) stay near-unsolved from a single trace. An aligned reference improves selected relative faults but does not resolve guardrail bypass. The held-out labels and compact prediction format support reproducible comparison of LLM-based and non-LLM diagnosis methods.

---


### 41. [Automatic or Controlled? Repetition Priming Reveals Divergent Processing in Base LLMs, Instruct LLMs, and Humans](https://arxiv.org/abs/2608.14681)

**<font color=#1a73e8>作者：</font>** Jinglei Ren, Yuyue Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Words recur constantly in natural language use, yet it remains unclear whether language models reactivate prior representations or re-evaluate repeated words afresh, and whether post-training changes this default behavior. We apply repetition priming (Shiffrin and Schneider, 1977) to 15 models across five model families (1.5B-14B parameters) in two tasks, semantic categorization and cloze completion, with matched human experiments using identical stimuli. We find that base models exhibit automatic processing: they show immediate facilitation that remains stable across lags, partially survives context removal, and correlates with attention to prior occurrences. Instruct models exhibit controlled processing: their facilitation decays with lag, collapses without expected context, and reverses to interference at larger scales. Within the Qwen 2.5 family, this dissociation increases monotonically with model scale, suggesting that post-training progressively alters repetition processing. Humans show a hybrid profile, with lag-sensitive facilitation resembling instruct models but without interference, suggesting that neither model type fully captures human cognition. Our findings reveal a qualitative shift in how language models process repeated information after post-training and provide mechanistic evidence for the divergence between model behaviors.

---


### 42. [One Score, Two Decisions: Selective Prediction on the Rare-Disease Tail](https://arxiv.org/abs/2608.14683)

**<font color=#1a73e8>作者：</font>** Zhaoyang Jiang, Zhizhong Fu, Yunsoo Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given a patient's clinical findings, a diagnostic system ranks possible diseases and must decide when to endorse its first prediction or defer it for review. This decision is usually made by thresholding the top score. Selective prediction over ranked outputs begins with two checks. First, the ranker must produce enough correct top-ranked predictions to make the target feasible. Across 2,000 patient records stratified by disease prevalence, eight small open-weight LLMs achieve at most 4.6% Recall@1 on ultra-rare diseases. At 10% coverage, even a perfect confidence ranking of their existing predictions therefore cannot reach 50% selective accuracy. More accurate models pass the same check, showing that the limit is regime-specific. Second, the confidence signal must match the decision being made. For fixed-candidate rankers, the top-two margin cancels components shared across candidates. On phenotype-only Exomiser, it selects 10% of cases at 29.0% accuracy, compared with 13.3% overall, while the top score provides no reliable gate. Yet that cancellation can remove information needed to detect whether the candidate list contains an answer. SciFact retrieval and biomedical entity linking confirm this distinction. Finally, we prove that unlabelled scores alone cannot determine whether switching to the margin will help.

---


### 43. [Mitigating Rubric Interference in LLM Judges via On-Policy Self-Distillation](https://arxiv.org/abs/2608.14684)

**<font color=#1a73e8>作者：</font>** Dingyao Yu, Tong Zhang, Yutao Mou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM judges increasingly evaluate responses against fine-grained rubric checklists. When a sample requires multiple rubrics, current methods typically assess each in a separate inference call. Evaluating all rubrics in a single pass is a natural alternative with greater efficiency, but we find that it introduces rubric interference: the verdict on one rubric shifts depending on which other rubrics are co-present. In a preliminary study, only one-third of samples receive fully consistent verdicts when evaluated under rubric sets of varying composition. We develop a measurement framework that probes interference through four controlled operations: rubric set expansion, subsetting, reordering, and noise injection. To mitigate interference without external supervision, we propose Self-Anchored Rubric Alignment (SARA). SARA uses a model's own single-rubric judgments as stable anchors and aligns multi-rubric reasoning with these anchors through on-policy self-distillation. We validate SARA on three datasets (HealthBench, FLASK, ResearchQA) and two model families (Qwen3, Llama-3.1). SARA consistently improves evaluation consistency while maintaining agreement with both base models and GPT-4.1 as a reference judge. Furthermore, the learned consistency transfers across datasets, confirming that SARA teaches a general capability rather than fitting dataset-specific patterns.

---


### 44. [Rethinking Reverse KL as Adaptive Entropy Distillation](https://arxiv.org/abs/2608.14685)

**<font color=#1a73e8>作者：</font>** Shizhen Li, Zhiyu Shen, Yuyin Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) is widely used to transfer the capabilities of large language models (LLMs) to smaller students, but existing objectives often struggle to balance faithful imitation and robust generation. In particular, existing methods mainly combine FKL and RKL, overlooking that RKL itself provides a mechanism for adjusting the student's imitation strength. Motivated by this, we revisit on-policy Reverse Kullback-Leibler (RKL) distillation and decompose its objective into a teacher-fitting term and a student-entropy term, without introducing an explicit FKL branch. We show theoretically that the token-level optimal student distribution corresponds to a tempered variant of the teacher distribution, where the adaptive weight controls the trade-off between mode-seeking and uncertainty preservation. Guided by this insight, we propose \textbf{Adaptive Entropy Distillation (AED)}, which uses the teacher's entropy to dynamically calibrate token-level imitation strength. Experiments on instruction-following and mathematical reasoning benchmarks demonstrate that AED achieves superior overall performance and generally improves teacher--student distributional and entropy alignment.

---


### 45. [A Reproducibility Study of Partial Residual Ablations in Pre-LN Transformers](https://arxiv.org/abs/2608.14689)

**<font color=#1a73e8>作者：</font>** Pratikkumar Babariya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual connections are a fundamental component of transformer architectures, yet the roles of the attention and feed-forward residual pathways remain poorly understood when considered independently. This paper presents a reproducibility study of partial residual ablations in Pre-LN GPT-style transformers trained at two scales (10M and 124M parameters).
I compare four architectural configurations by selectively removing the attention residual connection, the feed-forward residual connection, or both. Across all experiments, removing the attention residual (FFNOnly) consistently causes deterministic collapse to the No-Residual performance floor. In contrast, removing the feed-forward residual (AttnOnly) exhibits a reproducible recovery effect at 10M scale under a controlled 8-seed deterministic study, while its behavior at 124M remains unresolved because of substantial seed variance.
During the investigation, I identified and corrected an experimental measurement confound in runtime gain scaling and document both the failed intermediate reproduction and the subsequent controlled replication. Based on the empirical results, I propose a cross-position routing hypothesis to explain the observed asymmetry while explicitly distinguishing confirmed findings from unresolved questions.
To support reproducibility, I release the complete source code, experiment configurations, checkpoints, training logs, and all experimental results, including intermediate non-reproducing runs.

---


### 46. [Domain Agnostic Text Redaction from Natural Language Rules using Instruction Tuning](https://arxiv.org/abs/2608.14693)

**<font color=#1a73e8>作者：</font>** Aravindhan Arunagiri, Ayaan Khan, Udayaadithya Avadhanam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the increasing digitization of personal and corporate communication, the automatic sanitization of textual data has become a crucial component of data privacy and compliance frameworks. Traditional text sanitization solutions are majorly suitable for obscuring sensitive data with standard structure such as Personal Identifiable Information (PII). These solutions do not provide transparent justification for their redaction, which makes it difficult to audit them. This paper introduces an explainable, domain-agnostic text redaction solution that uses natural language rules of redaction, applied via an instruction-tuned language model, to identify and redact sensitive information in unstructured documents. Unlike traditional text sanitization, this method enables a user to conveniently define any sensitive information; which may be structured (e.g.\ PII) or unstructured (e.g.\ legal terms and conditions) in natural language. A general-purpose LLM generates or augments these natural language rules of redaction from the user's definition, which are then used to instruction-fine-tune a smaller language model that reasons the rules step-by-step over any given document to identify and redact the corresponding sensitive content, while providing transparent justifications for each redaction and highlighting the specific rule that triggered the decision. This explanation is generated in natural language to support human reviewers and auditors in understanding why specific content was redacted. A reconstruction-based metric is used to estimate the probability of recovering redacted information from the sanitized document, quantifying redaction coverage. The solution shows high reconstruction error and high redaction precision, making it suitable for automated text sanitization in critical applications such as legal discovery, medical documentation, and corporate information governance.

---


### 47. [Synchronized Logit Steering: Real-world Steganography](https://arxiv.org/abs/2608.14697)

**<font color=#1a73e8>作者：</font>** Andrew Rufail, Aadi Dash, Onir Narahari 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Steganography in large language models offers a way to embed hidden messages within natural-sounding text. Existing token and logit-level methods typically require the sender and receiver to share an identical prompt context, which is rarely guaranteed in production pipelines that use retrieval-augmented generation or proprietary system instructions. We introduce Synchronized Logit Steering (SLS), a deterministic steganographic scheme that eliminates this dependency by deriving a proxy prompt from the generated output itself, allowing both parties to reconstruct the same logit distribution without access to the original prompt. SLS encodes payload values as token ranks within high-entropy regions of the proxy prompt distribution, and we extend the scheme with periodic recurrence and payload bursts to scale information density. Across ShareGPT, GSM8K, and SWE-bench Verified, we show that the KL divergence between the true and proxy prompt distributions falls below 0.5 nats once the synchronization window reaches 40 tokens, and SLS encoding does not meaningfully disrupt this convergence relative to greedy generation. We also find that the periodic-burst variant achieves 0.20 bits per token, or roughly 10x the capacity of single-payload encoding. Kolmogorov-Smirnov tests further confirm that SLS outputs are statistically difficult to distinguish from greedy generations, demonstrating that covert, prompt-agnostic communication through LLMs is both practical and stealthy.

---


### 48. [Semantic Uncertainty-Guided Orchestration in Hierarchical Multi-Agent Systems](https://arxiv.org/abs/2608.14707)

**<font color=#1a73e8>作者：</font>** John Knowlton, Aritra Guha, Risto Miikkulainen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM)-based multi-agent systems become increasingly capable, coordinating agents under uncertainty becomes a fundamental challenge. Existing orchestration strategies typically rely on fixed interaction patterns and often lack mechanisms for assessing the reliability of intermediate reasoning steps, allowing errors and hallucinations to propagate through the system. This paper introduces a semantic-uncertainty-guided orchestration approach, HASSUM as a general framework for uncertainty-aware coordination in multi-agent systems. The method estimates uncertainty using semantic entropy and semantic density, which measure trust at the level of answer semantics rather than output probabilities. These signals enable adaptive orchestration decisions, including output verification, selective reprompting, additional deliberation, and confidence-aware response selection. Because the approach operates independently of any particular agent architecture, it can be integrated into a broad range of hierarchical and collaborative multi-agent systems. The evaluations demonstrate an implementation within a hierarchical agent framework and evaluate it on StrategyQA, JailbreakBench, and TruthfulQA benchmarks. Across tasks that require complex reasoning and are prone to ambiguity or hallucinations, uncertainty-guided orchestration yields more reliable outcomes than uncertainty-unaware coordination. Semantic entropy and semantic density in tandem outperformed either metric alone. Ablations testing different thresholds and model sizes demonstrated that both influence the effectiveness of semantic metrics. The results suggest that semantic uncertainty is a practical and general-purpose signal for improving robustness and trustworthiness in agentic AI systems.

---


### 49. [Beyond Pass@k: Measuring Reliability and Security of Agentic Code Generation](https://arxiv.org/abs/2608.14711)

**<font color=#1a73e8>作者：</font>** Jiajun Jiang, Sharon Zheng, Natan Vidra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI coding agent benchmarks rank agents with the Chen et al. (2021) pass@k estimator, but current implementations misapply it: they set n to the number of unit tests in a single submission rather than the number of independent rollout attempts, conflating test-suite size with attempt independence. We diagnose this operationalization error, prove it by counterexample, and propose reliability@k, the same estimator applied correctly, with n = independent rollouts and c = fully-passing rollouts per (task, agent) pair. In a synthetic multi-rollout benchmark, the misapplied metric inflates reported scores by 0.85-0.97 in absolute terms (0.96-0.98 reported vs. 0.00-0.12 corrected), and a cheap single-rollout proxy fails to substitute for repeated runs (Spearman $\rho = 0.417$). Motivated by evidence that functional correctness does not imply security safety, we additionally propose security-adjusted reliability@k, which counts only rollouts that are both functionally correct and free of high-severity insecure patterns. In an initial live-API test with three agents, the adjustment did not change any ranking under our current scanner and threshold, so we present it as a proposed complementary lens whose decisive evaluation requires better-powered future runs. Finally, a preliminary 5-task SWE-bench Verified pilot observes the same core concern in a real repository setting: macro-averaged hidden-test pass rate was 0.80 while strict task resolution was 0.20.

---


### 50. [VideoGAIA: A Benchmark for General AI Assistants on Agentic Video Understanding](https://arxiv.org/abs/2608.14718)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Guangming Yao, Jinyang Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding is a fundamental task for evaluating the capabilities of multimodal large language models (MLLMs). However, existing leading models have already achieved approximately 90% accuracy on the Video-MME leaderboard, suggesting that conventional single-turn video understanding tasks are becoming increasingly saturated and insufficient for assessing the intelligence of advanced MLLMs. Towards this end, we introduce VideoGAIA, an agentic video understanding benchmark for general artificial intelligence (AI) assistants. Moving beyond one-shot video question answering, VideoGAIA formulates video understanding as a multi-turn, tool-augmented interaction process, where models must iteratively perceive videos, invoke external tools, gather complementary information, and integrate multimodal evidence across turns. VideoGAIA contains 271 model-human co-designed tasks covering diverse and complex real-world scenarios. Each video-question-answer instance is independently verified by three human experts to ensure both correctness and appropriate difficulty. All evaluated MLLMs, including frontier models such as GPT-5.5 and Kimi-K3, achieve less than 60% accuracy on VideoGAIA, highlighting its value as a high-quality and timely benchmark for evaluating next-generation MLLMs. We hope that VideoGAIA will facilitate the transition from conventional video understanding toward agentic video understanding.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-358](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
