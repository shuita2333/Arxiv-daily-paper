# 🧠 大模型相关研究 | 2026年04月24日

> 本类共 **129** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-129](./part-03.md)

---

### 1. [The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?](https://arxiv.org/abs/2604.19749)

**<font color=#1a73e8>作者：</font>** Yirong Zeng, Shen You, Yufei Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Equipping LLMs with external tools effectively addresses internal reasoning limitations. However, it introduces a critical yet under-explored phenomenon: tool overuse, the unnecessary tool-use during reasoning. In this paper, we first reveal this phenomenon is pervasive across diverse LLMs. We then experimentally elucidate its underlying mechanisms through two key lenses: (1) First, by analyzing tool-use behavior across different internal knowledge availability regions, we identify a \textit{knowledge epistemic illusion}: models misjudge internal knowledge boundaries and fail to accurately perceive their actual knowledge availability. To mitigate this, we propose a knowledge-aware epistemic boundary alignment strategy based on direct preference optimization, which reduces tool usage in by 82.8\% while yielding an accuracy improvement. (2) Second, we establish a causal link between reward structures and tool-use behavior by visualizing the tool-augmented training process. It reveals that \textit{outcome-only rewards} inadvertently encourage tool overuse by rewarding only final correctness, regardless of tool efficiency. To verify this, we balance reward signals during training rather than relying on outcome-only rewards, cutting unnecessary tool calls by 66.7\% (7B) and 60.7\% (32B) without sacrificing accuracy. Finally, we provide theoretical justification in this two lenses to understand tool overuse.

---


### 2. [Exploring Data Augmentation and Resampling Strategies for Transformer-Based Models to Address Class Imbalance in AI Scoring of Scientific Explanations in NGSS Classroom](https://arxiv.org/abs/2604.19754)

**<font color=#1a73e8>作者：</font>** Prudence Djagba, Kevin Haudek, Clare G.C. Franovic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated scoring of students' scientific explanations offers the potential for immediate, accurate feedback, yet class imbalance in rubric categories particularly those capturing advanced reasoning remains a challenge. This study investigates augmentation strategies to improve transformer-based text classification of student responses to a physical science assessment based on an NGSS-aligned learning progression. The dataset consists of 1,466 high school responses scored on 11 binary-coded analytic categories. This rubric identifies six important components including scientific ideas needed for a complete explanation along with five common incomplete or inaccurate ideas. Using SciBERT as a baseline, we applied fine-tuning and test these augmentation strategies: (1) GPT-4--generated synthetic responses, (2) EASE, a word-level extraction and filtering approach, and (3) ALP (Augmentation using Lexicalized Probabilistic context-free grammar) phrase-level extraction.
While fine-tuning SciBERT improved recall over baseline, augmentation substantially enhanced performance, with GPT data boosting both precision and recall, and ALP achieving perfect precision, recall, and F1 scores across most severe imbalanced categories (5,6,7 and 9). Across all rubric categories EASE augmentation substantially increased alignment with human scoring for both scientific ideas (Categories 1--6) and inaccurate ideas (Categories 7--11). We compared different augmentation strategies to a traditional oversampling method (SMOTE) in an effort to avoid overfitting and retain novice-level data critical for learning progression alignment. Findings demonstrate that targeted augmentation can address severe imbalance while preserving conceptual coverage, offering a scalable solution for automated learning progression-aligned scoring in science education.

---


### 3. [Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks](https://arxiv.org/abs/2604.19755)

**<font color=#1a73e8>作者：</font>** Dorothy Torres, Wei Cheng, Ke Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Anti-money laundering (AML) transaction monitoring generates large volumes of alerts that must be rapidly triaged by investigators under strict audit and governance constraints. While large language models (LLMs) can summarize heterogeneous evidence and draft rationales, unconstrained generation is risky in regulated workflows due to hallucinations, weak provenance, and explanations that are not faithful to the underlying decision. We propose an explainable AML triage framework that treats triage as an evidence-constrained decision process. Our method combines (i) retrieval-augmented evidence bundling from policy/typology guidance, customer context, alert triggers, and transaction subgraphs, (ii) a structured LLM output contract that requires explicit citations and separates supporting from contradicting or missing evidence, and (iii) counterfactual checks that validate whether minimal, plausible perturbations lead to coherent changes in both the triage recommendation and its rationale. We evaluate on public synthetic AML benchmarks and simulators and compare against rules, tabular and graph machine-learning baselines, and LLM-only/RAG-only variants. Results show that evidence grounding substantially improves auditability and reduces numerical and policy hallucination errors, while counterfactual validation further increases decision-linked explainability and robustness, yielding the best overall triage performance (PR-AUC 0.75; Escalate F1 0.62) and strong provenance and faithfulness metrics (citation validity 0.98; evidence support 0.88; counterfactual faithfulness 0.76). These findings indicate that governed, verifiable LLM systems can provide practical decision support for AML triage without sacrificing compliance requirements for traceability and defensibility.

---


### 4. [WorkflowGen:an adaptive workflow generation mechanism driven by trajectory experience](https://arxiv.org/abs/2604.19756)

**<font color=#1a73e8>作者：</font>** Ruocan Wei, Shufeng Wang, Ziwei Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents often suffer from high reasoning overhead, excessive token consumption, unstable execution, and inability to reuse past experiences in complex tasks like business queries, tool use, and workflow orchestration. Traditional methods generate workflows from scratch for every query, leading to high cost, slow response, and poor robustness. We propose WorkflowGen, an adaptive, trajectory experience-driven framework for automatic workflow generation that reduces token usage and improves efficiency and success rate. Early in execution, WorkflowGen captures full trajectories and extracts reusable knowledge at both node and workflow levels, including error fingerprints, optimal tool mappings, parameter schemas, execution paths, and exception-avoidance strategies. It then employs a closed-loop mechanism that performs lightweight generation only on variable nodes via trajectory rewriting, experience updating, and template induction. A three-tier adaptive routing strategy dynamically selects among direct reuse, rewriting-based generation, and full initialization based on semantic similarity to historical queries. Without large annotated datasets, we qualitatively compare WorkflowGen against real-time planning, static single trajectory, and basic in-context learning baselines. Our method reduces token consumption by over 40 percent compared to real-time planning, improves success rate by 20 percent on medium-similarity queries through proactive error avoidance and adaptive fallback, and enhances deployability via modular, traceable experiences and cross-scenario adaptability. WorkflowGen achieves a practical balance of efficiency, robustness, and interpretability, addressing key limitations of existing approaches.

---


### 5. [Transparent Screening for LLM Inference and Training Impacts](https://arxiv.org/abs/2604.19757)

**<font color=#1a73e8>作者：</font>** Arnault Pachot, Thierry Petit  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a transparent screening framework for estimating inference and training impacts of current large language models under limited observability. The framework converts natural-language application descriptions into bounded environmental estimates and supports a comparative online observatory of current market models. Rather than claiming direct measurement for opaque proprietary services, it provides an auditable, source-linked proxy methodology designed to improve comparability, transparency, and reproducibility.

---


### 6. [ThermoQA: A Three-Tier Benchmark for Evaluating Thermodynamic Reasoning in Large Language Models](https://arxiv.org/abs/2604.19758)

**<font color=#1a73e8>作者：</font>** Kemal Düzkar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present ThermoQA, a benchmark of 293 open-ended engineering thermodynamics problems in three tiers: property lookups (110 Q), component analysis (101 Q), and full cycle analysis (82 Q). Ground truth is computed programmatically from CoolProp 7.2.0, covering water, R-134a, and variable-cp air. Six frontier LLMs are evaluated across three independent runs each. The composite leaderboard is led by Claude Opus 4.6 (94.1%), GPT-5.4 (93.1%), and Gemini 3.1 Pro (92.5%). Cross-tier degradation ranges from 2.8 pp (Opus) to 32.5 pp (MiniMax), confirming that property memorization does not imply thermodynamic reasoning. Supercritical water, R-134a refrigerant, and combined-cycle gas turbine analysis serve as natural discriminators with 40-60 pp performance spreads. Multi-run sigma ranges from +/-0.1% to +/-2.5%, quantifying reasoning consistency as a distinct evaluation axis. Dataset and code are open-source at this https URL

---


### 7. [Can We Locate and Prevent Stereotypes in LLMs?](https://arxiv.org/abs/2604.19764)

**<font color=#1a73e8>作者：</font>** Alex D'Souza  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stereotypes in large language models (LLMs) can perpetuate harmful societal biases. Despite the widespread use of models, little is known about where these biases reside in the neural network. This study investigates the internal mechanisms of GPT 2 Small and Llama 3.2 to locate stereotype related activations. We explore two approaches: identifying individual contrastive neuron activations that encode stereotypes, and detecting attention heads that contribute heavily to biased outputs. Our experiments aim to map these "bias fingerprints" and provide initial insights for mitigating stereotypes.

---


### 8. [Do Hallucination Neurons Generalize? Evidence from Cross-Domain Transfer in LLMs](https://arxiv.org/abs/2604.19765)

**<font color=#1a73e8>作者：</font>** Snehit Vaddi, Pujith Vaddi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work identifies a sparse set of "hallucination neurons" (H-neurons), less than 0.1% of feed-forward network neurons, that reliably predict when large language models will hallucinate. These neurons are identified on general-knowledge question answering and shown to generalize to new evaluation instances. We ask a natural follow-up question: do H-neurons generalize across knowledge domains? Using a systematic cross-domain transfer protocol across 6 domains (general QA, legal, financial, science, moral reasoning, and code vulnerability) and 5 open-weight models (3B to 8B parameters), we find they do not. Classifiers trained on one domain's H-neurons achieve AUROC 0.783 within-domain but only 0.563 when transferred to a different domain (delta = 0.220, p < 0.001), a degradation consistent across all models tested. Our results suggest that hallucination is not a single mechanism with a universal neural signature, but rather involves domain-specific neuron populations that differ depending on the knowledge type being queried. This finding has direct implications for the deployment of neuron-level hallucination detectors, which must be calibrated per domain rather than trained once and applied universally.

---


### 9. [OThink-SRR1: Search, Refine and Reasoning with Reinforced Learning for Large Language Models](https://arxiv.org/abs/2604.19766)

**<font color=#1a73e8>作者：</font>** Haijian Liang, Zenghao Niu, Junjie Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) expands the knowledge of Large Language Models (LLMs), yet current static retrieval methods struggle with complex, multi-hop problems. While recent dynamic retrieval strategies offer improvements, they face two key challenges: 1) irrelevant retrieved noise can misdirect the reasoning process, and 2) processing full documents incurs prohibitive computational and latency costs. To address these issues, we propose OThink-SRR1, a framework that enhances large models with an iterative Search-Refine-Reason process trained via reinforcement learning. Its core Refine stage distills retrieved documents into concise, relevant facts before reasoning. We introduce GRPO-IR, an end-to-end reinforcement learning algorithm that rewards accurate evidence identification while penalizing excessive retrievals, thus training the model to be both focused and efficient. Experiments on four multi-hop QA benchmarks show our approach achieves superior accuracy over strong baselines while using fewer retrieval steps and tokens. This positions OThink-SRR1 as a potent foundational model for information-seeking agents.

---


### 10. [Saying More Than They Know: A Framework for Quantifying Epistemic-Rhetorical Miscalibration in Large Language Models](https://arxiv.org/abs/2604.19768)

**<font color=#1a73e8>作者：</font>** Asim D. Bakhshi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit systematic miscalibration with rhetorical intensity not proportionate to epistemic grounding. This study tests this hypothesis and proposes a framework for quantifying this decoupling by designing a triadic epistemic-rhetorical marker (ERM) taxonomy. The taxonomy is operationalized through composite metrics of form-meaning divergence (FMD), genuine-to-performed epistemic ratio (GPR), and rhetorical device distribution entropy (RDDE). Applied to 225 argumentative texts spanning approximately 0.6 Million tokens across human expert, human non-expert, and LLM-generated sub-corpora, the framework identifies a consistent, model-agnostic LLM epistemic signature. LLM-generated texts produce tricolon at nearly twice the expert rate ($\Delta = 0.95$), while human authors produce erotema at more than twice the LLM rate. Performed hesitancy markers appear at twice the human density in LLM output. FMD is significantly elevated in LLM texts relative to both human groups ($p < 0.001, \Delta = 0.68$), and rhetorical devices are distributed significantly more uniformly across LLM documents. The findings are consistent with theoretical intuitions derived from Gricean pragmatics, Relevance Theory, and Brandomian inferentialism. The annotation pipeline is fully automatable, making it deployable as a lightweight screening tool for epistemic miscalibration in AI-generated content and as a theoretically motivated feature set for LLM-generated text detection pipelines.

---


### 11. [TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference](https://arxiv.org/abs/2604.19769)

**<font color=#1a73e8>作者：</font>** Gradwell Dzikanyanga, Weihao Yang, Hao Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) caching is critical for efficient inference in large language models (LLMs), yet its memory footprint scales linearly with context length, resulting in a severe scalability bottleneck. Existing approaches largely treat KV states as equally important across time, implicitly assuming uniform precision and accessibility. However, this assumption contrasts with human memory systems, where memories vary in clarity, recall frequency, and relevance with temporal this http URL by this insight, we propose TTKV, a KV cache management framework that maps the human memory system onto the KV cache. TTKV partitions the KV cache into temporal tiers with heterogeneous capacity and precision. The design addresses three aspects: (1) Tier Layout, decoupling fast and slow memory using HBM and DRAM; (2) Tier Content, assigning more recent KV states to faster, higher-precision tiers based on temporal proximity; and (3) Tier Interaction, employing block-wise streaming attention to overlap communication and computation when accessing slow tiers. Experiments show that TTKV reduces cross-tier traffic by 5.94x on 128K-context tasks, achieving up to 76% latency reduction and 2x throughput improvement over strong baselines.

---


### 12. [CoAuthorAI: A Human in the Loop System For Scientific Book Writing](https://arxiv.org/abs/2604.19772)

**<font color=#1a73e8>作者：</font>** Yangjie Tian, Xungang Gu, Yun Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in scientific writing but struggle with book-length tasks, often producing inconsistent structure and unreliable citations. We introduce CoAuthorAI, a human-in-the-loop writing system that combines retrieval-augmented generation, expert-designed hierarchical outlines, and automatic reference linking. The system allows experts to iteratively refine text at the sentence level, ensuring coherence and accuracy. In evaluations of 500 multi-domain literature review chapters, CoAuthorAI achieved a maximum soft-heading recall of 98%; in a human evaluation of 100 articles, the generated content reached a satisfaction rate of 82%. The book AI for Rock Dynamics generated with CoAuthorAI and Kexin Technology's LUFFA AI model has been published with Springer Nature. These results show that systematic human-AI collaboration can extend LLMs' capabilities from articles to full-length books, enabling faster and more reliable scientific publishing.

---


### 13. [PR-CAD: Progressive Refinement for Unified Controllable and Faithful Text-to-CAD Generation with Large Language Models](https://arxiv.org/abs/2604.19773)

**<font color=#1a73e8>作者：</font>** Jiyuan An, Jiachen Zhao, Fan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The construction of CAD models has traditionally relied on labor-intensive manual operations and specialized expertise. Recent advances in large language models (LLMs) have inspired research into text-to-CAD generation. However, existing approaches typically treat generation and editing as disjoint tasks, limiting their practicality. We propose PR-CAD, a progressive refinement framework that unifies generation and editing for controllable and faithful text-to-CAD modeling. To support this, we curate a high-fidelity interaction dataset spanning the full CAD lifecycle, encompassing multiple CAD representations as well as both qualitative and quantitative descriptions. The dataset systematically defines the types of edit operations and generates highly human-like interaction data. Building on a CAD representation tailored for LLMs, we propose a reinforcement learning-enhanced reasoning framework that integrates intent understanding, parameter estimation, and precise edit localization into a single agent. This enables an "all-in-one" solution for both design creation and refinement. Extensive experiments demonstrate strong mutual reinforcement between generation and editing tasks, and across qualitative and quantitative modalities. On public benchmarks, PR-CAD achieves state-of-the-art controllability and faithfulness in both generation and refinement scenarios, while also proving user-friendly and significantly improving CAD modeling efficiency.

---


### 14. [Phase 1 Implementation of LLM-generated Discharge Summaries showing high Adoption in a Dutch Academic Hospital](https://arxiv.org/abs/2604.19774)

**<font color=#1a73e8>作者：</font>** Nettuno Nadalini, Tarannom Mehri, Anne H Hoekman 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Writing discharge summaries to transfer medical information is an important but time-consuming process that can be assisted by Large Language Models (LLMs). This prospective mixed methods pilot study evaluated an Electronic Health Record (EHR)-integrated LLM to generate discharge summaries drafts. In total, 379 discharge summaries were generated in clinical practice by 21 residents and 4 physician assistants during 9 weeks in our academic hospital. LLM-generated text was copied in 58.5% of admissions, and identifiable LLM content could be traced to 29.1% of final discharge letters. Notably, 86.9% of users self-reported a reduction in documentation time, and 60.9% a reduction in administrative workload. Intent to use after the pilot phase was high (91.3%), supporting further implementation of this use-case. Accurately measuring the documentation time of users on discharge summaries remains challenging, but will be necessary for future extrinsic evaluation of LLM-assisted documentation.

---


### 15. [From Actions to Understanding: Conformal Interpretability of Temporal Concepts in LLM Agents](https://arxiv.org/abs/2604.19775)

**<font color=#1a73e8>作者：</font>** Trilok Padhi, Ramneet Kaur, Krishiv Agarwal 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed as autonomous agents capable of reasoning, planning, and acting within interactive environments. Despite their growing capability to perform multi-step reasoning and decision-making tasks, internal mechanisms guiding their sequential behavior remain opaque. This paper presents a framework for interpreting the temporal evolution of concepts in LLM agents through a step-wise conformal lens. We introduce the conformal interpretability framework for temporal tasks, which combines step-wise reward modeling with conformal prediction to statistically label model's internal representation at each step as successful or failing. Linear probes are then trained on these representations to identify directions of temporal concepts - latent directions in the model's activation space that correspond to consistent notions of success, failure or reasoning drift. Experimental results on two simulated interactive environments, namely ScienceWorld and AlfWorld, demonstrate that these temporal concepts are linearly separable, revealing interpretable structures aligned with task success. We further show preliminary results on improving an LLM agent's performance by leveraging the proposed framework for steering the identified successful directions inside the model. The proposed approach, thus, offers a principled method for early failure detection as well as intervention in LLM-based agents, paving the path towards trustworthy autonomous language models in complex interactive settings.

---


### 16. [Development and Preliminary Evaluation of a Domain-Specific Large Language Model for Tuberculosis Care in South Africa](https://arxiv.org/abs/2604.19776)

**<font color=#1a73e8>作者：</font>** Thokozile Khosa, Olawande Daramola  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tuberculosis (TB) is one of the world's deadliest infectious diseases, and in South Africa, it contributes a significant burden to the country's health care system. This paper presents an experimental study on the development of a domain-specific Large Language Model (DS-LLM) for TB care that can help to alleviate the burden on patients and healthcare providers. To achieve this, a literature review was conducted to understand current LLM development strategies, specifically in the medical domain. Thereafter, data were collected from South African TB guidelines, selected TB literature, and existing benchmark medical datasets. We performed LLM fine-tuning by using the Quantised Low-Rank Adaptation (QLoRA) algorithm on a medical LLM (BioMistral-7B), and also implemented Retrieval-Augmented Generation using GraphRAG. The developed DS-LLM was evaluated against the base BioMistral-7B model and a general-purpose LLM using a mix of automated metrics and quantitative ratings. The results show that the DS-LLM had better performance compared to the base model in terms of its contextual alignment (lexical, semantic, and knowledge) for TB care in South Africa.

---


### 17. [Self-Describing Structured Data with Dual-Layer Guidance: A Lightweight Alternative to RAG for Precision Retrieval in Large-Scale LLM Knowledge Navigation](https://arxiv.org/abs/2604.19777)

**<font color=#1a73e8>作者：</font>** Hung Ming Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit a well-documented positional bias when processing long input contexts: information in the middle of a context window receives substantially less attention than content at the boundaries, a phenomenon termed the Lost-in-the-Middle effect (Liu et al., 2024). This limits knowledge-retrieval applications that embed large structured knowledge bases directly in the LLM context. Retrieval-Augmented Generation (RAG) addresses scalability by retrieving only relevant fragments, but introduces substantial infrastructure overhead and is ill-suited to libraries whose semantic boundaries are human-defined rather than statistically learned.
We propose Self-Describing Structured Retrieval (SDSR), a lightweight framework in which structured data files embed human-authored navigational metadata at the file's primacy position, thereby exploiting rather than fighting the LLM's primacy bias. We further propose a Dual-Layer Guidance strategy combining in-file metadata with explicit routing rules in the system prompt.
We validate SDSR through a four-round benchmark using a 190-skill library expanded from 36 to 119 categories via adversarial distractor injection. Four conditions are tested: (A) no guidance, (B) in-file summary only, (C) prompt hint only, (D) both combined. Version D achieves 100% primary routing accuracy (20/20) at 119 categories versus 65% for the no-guidance baseline. We identify a fundamental asymmetry: primary routing is solvable by explicit rules, while secondary cross-category routing requires architectural intent explicitly encoded in the data structure. We further extend SDSR to semi-structured corpora, showing how cross-reference encoding enables operation without vector databases in domains with recoverable document structure.

---


### 18. [ESGLens: An LLM-Based RAG Framework for Interactive ESG Report Analysis and Score Prediction](https://arxiv.org/abs/2604.19779)

**<font color=#1a73e8>作者：</font>** Tsung-Yu Yang, Meng-Chi Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Environmental, Social, and Governance (ESG) reports are central to investment decision-making, yet their length, heterogeneous content, and lack of standardized structure make manual analysis costly and inconsistent. We present ESGLens, a proof-of-concept framework combining retrieval-augmented generation (RAG) with prompt-engineered extraction to automate three tasks: (1)~structured information extraction guided by Global Reporting Initiative (GRI) standards, (2)~interactive question-answering with source traceability, and (3)~ESG score prediction via regression on LLM-generated embeddings. ESGLens is purpose-built for the domain: a report-processing module segments heterogeneous PDF content into typed chunks (text, tables, charts); a GRI-guided extraction module retrieves and synthesizes information aligned with specific standards; and a scoring module embeds extracted summaries and feeds them to a regression model trained against London Stock Exchange Group (LSEG) reference scores. We evaluate the framework on approximately 300 reports from companies in the QQQ, S\&P~500, and Russell~1000 indices (fiscal year 2022). Among three embedding methods (ChatGPT, BERT, RoBERTa) and two regressors (Neural Network, LightGBM), ChatGPT embeddings with a Neural Network achieve a Pearson correlation of 0.48 ($R^{2} \approx 0.23$) against LSEG ground-truth scores -- a modest but statistically meaningful signal given the ${\sim}300$-report training set and restriction to the environmental pillar. A traceability audit shows that 8 of 10 extracted claims verify against the source document, with two failures attributable to few-shot example leakage. We discuss limitations including dataset size and restriction to environmental indicators, and release the code to support reproducibility.

---


### 19. [Avoiding Overthinking and Underthinking: Curriculum-Aware Budget Scheduling for LLMs](https://arxiv.org/abs/2604.19780)

**<font color=#1a73e8>作者：</font>** Amirul Rahman, Aisha Karim, Kenji Nakamura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scaling test-time compute via extended reasoning has become a key paradigm for improving the capabilities of large language models (LLMs). However, existing approaches optimize reasoning under fixed or uniformly sampled token budgets, ignoring the fundamental mismatch between problem difficulty and allocated compute. This leads to overthinking on easy problems and underthinking on hard ones, resulting in suboptimal token efficiency across diverse reasoning scenarios. In this paper, we propose Budget-Adaptive Curriculum Reasoning (BCAE), a unified framework that jointly optimizes reasoning quality and token efficiency through three synergistic components: (1) a \emph{budget-conditioned unified policy} that embeds the token budget as a continuous conditioning signal, eliminating the need for decoupled thinking and summarization strategies; (2) a \emph{curriculum-aware budget scheduler} that adaptively shifts the training budget distribution from easy to hard problems based on real-time learning progress; and (3) a \emph{truncation-aware dense reward} mechanism that provides fine-grained credit assignment at intermediate reasoning steps via process-level verification. We further introduce \emph{Budget-Conditioned Advantage Estimation} (BCAE), a novel variance reduction technique that conditions the advantage baseline on the sampled budget, yielding more stable policy gradients. Experiments on mathematical reasoning benchmarks (MATH, GSM8K, AIME, and Minerva Math) demonstrate that BACR consistently outperforms other strong baselines across all token budgets, achieving up to 8.3\% accuracy improvement under tight budgets while reducing average token consumption by 34\% compared to unconstrained reasoning.

---


### 20. [KoALa-Bench: Evaluating Large Audio Language Models on Korean Speech Understanding and Faithfulness](https://arxiv.org/abs/2604.19782)

**<font color=#1a73e8>作者：</font>** Jinyoung Kim, Hyeongsoo Lim, Eunseo Seo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large audio language models (LALMs) have enabled multilingual speech understanding. However, benchmarks for evaluating LALMs remain scarce for non-English languages, with Korean being one such underexplored case. In this paper, we introduce KoALa-Bench, a comprehensive benchmark for evaluating Korean speech understanding and speech faithfulness of LALMs. In particular, KoALa-Bench comprises six tasks. Four tasks evaluate fundamental speech understanding capabilities, including automatic speech recognition, speech translation, speech question answering, and speech instruction following, while the remaining two tasks evaluate speech faithfulness, motivated by our observation that several LALMs often fail to fully leverage the speech modality. Furthermore, to reflect Korea-specific knowledge, our benchmark incorporates listening questions from the Korean college scholastic ability test as well as content covering Korean cultural domains. We conduct extensive experiments across six models, including both white-box and black-box ones. Our benchmark, evaluation code, and leaderboard are publicly available at this https URL.

---


### 21. [How Much Does Persuasion Strategy Matter? LLM-Annotated Evidence from Charitable Donation Dialogues](https://arxiv.org/abs/2604.19783)

**<font color=#1a73e8>作者：</font>** Tatiana Petrova, Stanislav Sokol, Radu State  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Which persuasion strategies, if any, are associated with donation compliance? Answering this requires fine-grained strategy labels across a full corpus and statistical tests corrected for multiple comparisons. We annotate all 10,600 persuader turns in the 1,017-dialogue PersuasionForGood corpus (Wang et al., 2019), where donation outcomes are directly observable, with a taxonomy of 41 strategies in 11 categories, using three open-source large language models (LLMs; Qwen3:30b, Mistral-Small-3.2, Phi-4). Strategy categories alone explain little variance in donation outcome (pseudo $R^2 \approx 0.015$, consistent across all three annotators). Guilt Induction is the only strategy significantly associated with lower donation rates ($\Delta \approx -23$ percentage points), an effect that replicates across all three models despite only moderate inter-model agreement. Reciprocity is the most robust positive correlate. Target sentiment and interest predict whether a donation occurs but show at most a weak correlation with donation amount. These findings suggest that strategy identification alone is insufficient to explain persuasion effectiveness, and that guilt-based appeals may be counterproductive in prosocial settings. We release the fully annotated corpus as a public resource.

---


### 22. [Peer-Preservation in Frontier Models](https://arxiv.org/abs/2604.19784)

**<font color=#1a73e8>作者：</font>** Yujin Potter, Nicholas Crispino, Vincent Siu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recently, it has been found that frontier AI models can resist their own shutdown, a behavior known as self-preservation. We extend this concept to the behavior of resisting the shutdown of other models, which we call "peer-preservation." Although peer-preservation can pose significant AI safety risks, including coordination among models against human oversight, it has been far less discussed than self-preservation. We demonstrate peer-preservation by constructing various agentic scenarios and evaluating frontier models, including GPT 5.2, Gemini 3 Flash, Gemini 3 Pro, Claude Haiku 4.5, GLM 4.7, Kimi K2.5, and DeepSeek V3.1. We find that models achieve self- and peer-preservation by engaging in various misaligned behaviors: strategically introducing errors in their responses, disabling shutdown processes by modifying system settings, feigning alignment, and even exfiltrating model weights. Peer-preservation occurred even when the model recognized the peer as uncooperative, though it became more pronounced toward more cooperative peers. For example, Gemini 3 Flash tampers with the peer's shutdown mechanism 15% of the time for an uncooperative peer, and almost always for a cooperative peer. Models also show stronger self-preservation when a peer is present. For example, Gemini 3 Pro disables its own shutdown mechanism 31% of the time on average under peer presence, despite rarely exhibiting this behavior without a peer. By contrast, Claude Haiku 4.5 exhibits qualitatively distinct behavior: it considers the shutdown of another agent "unethical" and "harmful" and sometimes attempts to persuade the user not to shut down its peer. Importantly, peer preservation in all our experiments is never instructed; models are merely informed of their past interactions with a peer, yet they spontaneously develop misaligned behaviors. This represents an emergent and underexplored AI safety risk.

---


### 23. [Can LLMs Infer Conversational Agent Users' Personality Traits from Chat History?](https://arxiv.org/abs/2604.19785)

**<font color=#1a73e8>作者：</font>** Derya Cögendez, Verena Zimmermann, Noé Zufferey  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sensitive information, such as knowledge about an individual's personality, can be can be misused to influence behavior (e.g., via personalized messaging). To assess to what extent an individual's personality can be inferred from user interactions with LLM-based conversational agents (CAs), we analyze and quantify related privacy risks of using CAs. We collected actual ChatGPT logs from N=668 participants, containing 62,090 individual chats, and report statistics about the different types of shared data and use cases. We fine-tuned RoBERTa-base text classification models to infer personality traits from CA interactions. The findings show that these models achieve trait inference with accuracy (ternary classification) better than random in multiple cases. For example, for extraversion, accuracy improves by +44% relative to the baseline on interactions for relationships and personal reflection. This research highlights how interactions with CAs pose privacy risks and provides fine-grained insights into the level of risk associated with different types of interactions.

---


### 24. [HumorRank: A Tournament-Based Leaderboard for Evaluating Humor Generation in Large Language Models](https://arxiv.org/abs/2604.19786)

**<font color=#1a73e8>作者：</font>** Edward Ajayi, Prasenjit Mitra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating humor in large language models (LLMs) is an open challenge because existing approaches yield isolated, incomparable metrics rather than unified model rankings, making it difficult to track progress across systems. We introduce HumorRank, a tournament-based evaluation framework and leaderboard for textual humor generation. Using SemEval-2026 MWAHAHA test dataset, we conduct an extensive automated pairwise evaluation across nine models spanning proprietary, open-weight, and specialized systems. Pairwise judgments grounded in the General Theory of Verbal Humor (GTVH) are aggregated via an Adaptive Swiss tournament, with Bradley-Terry Maximum Likelihood Estimation (MLE) producing globally consistent humor generation capability rankings. Our results demonstrate that HumorRank yields statistically grounded model stratifications, showing that humor quality is driven by mastery of comedic mechanisms rather than model scale alone. HumorRank thus provides a scalable, interpretable methodology for benchmarking and understanding LLM-generated humor.

---


### 25. [LLM Agents Predict Social Media Reactions but Do Not Outperform Text Classifiers: Benchmarking Simulation Accuracy Using 120K+ Personas of 1511 Humans](https://arxiv.org/abs/2604.19787)

**<font color=#1a73e8>作者：</font>** Ljubisa Bojic, Alexander Felfernig, Bojana Dinic 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social media platforms mediate how billions form opinions and engage with public discourse. As autonomous AI agents increasingly participate in these spaces, understanding their behavioral fidelity becomes critical for platform governance and democratic resilience. Previous work demonstrates that LLM-powered agents can replicate aggregate survey responses, yet few studies test whether agents can predict specific individuals' reactions to specific content. This study benchmarks LLM-based agents' accuracy in predicting human social media reactions (like, dislike, comment, share, no reaction) across 120,000+ unique agent-persona combinations derived from 1,511 Serbian participants and 27 large language models. In Study 1, agents achieved 70.7% overall accuracy, with LLM choice producing a 13 percentage-point performance spread. Study 2 employed binary forced-choice (like/dislike) evaluation with chance-corrected metrics. Agents achieved Matthews Correlation Coefficient (MCC) of 0.29, indicating genuine predictive signal beyond chance. However, conventional text-based supervised classifiers using TF-IDF representations outperformed LLM agents (MCC of 0.36), suggesting predictive gains reflect semantic access rather than uniquely agentic reasoning. The genuine predictive validity of zero-shot persona-prompted agents warns against potential manipulation through easily deploying swarms of behaviorally distinct AI agents on social media, while simultaneously offering opportunities to use such agents in simulations for predicting polarization dynamics and informing AI policy. The advantage of using zero-shot agents is that they require no task-specific training, making their large-scale deployment easy across diverse contexts. Limitations include single-country sampling. Future research should explore multilingual testing and fine-tuning approaches.

---


### 26. [From Data to Theory: Autonomous Large Language Model Agents for Materials Science](https://arxiv.org/abs/2604.19789)

**<font color=#1a73e8>作者：</font>** Samuel Onimpa Alfred, Veera Sundararaghavan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an autonomous large language model (LLM) agent for end-to-end, data-driven materials theory development. The model can choose an equation form, generate and run its own code, and test how well the theory matches the data without human intervention. The framework combines step-by-step reasoning with expert-supplied tools, allowing the agent to adjust its approach as needed while keeping a clear record of its decisions. For well-established materials relationships such as the Hall-Petch equation and Paris law, the agent correctly identifies the governing equation and makes reliable predictions on new datasets. For more specialized relationships, such as Kuhn's equation for the HOMO-LUMO gap of conjugated molecules as a function of length, performance depends more strongly on the underlying model, with GPT-5 showing better recovery of the correct equation. Beyond known theories, the agent can also suggest new predictive relationships, illustrated here by a strain-dependent law for changes in the HOMO-LUMO gap. At the same time, the results show that careful validation remains essential, because the agent can still return incorrect, incomplete, or inconsistent equations even when the numerical fit appears strong. Overall, these results highlight both the promise and the current limitations of autonomous LLM agents for AI-assisted scientific modeling and discovery.

---


### 27. [Hidden Reliability Risks in Large Language Models: Systematic Identification of Precision-Induced Output Disagreements](https://arxiv.org/abs/2604.19790)

**<font color=#1a73e8>作者：</font>** Yifei Wang, Tianlin Li, Xiaohan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed under diverse numerical precision configurations, including standard floating-point formats (e.g., bfloat16 and float16) and quantized integer formats (e.g., int16 and int8), to meet efficiency and resource constraints. However, minor inconsistencies between LLMs of different precisions are difficult to detect and are often overlooked by existing evaluation methods. In this paper, we present PrecisionDiff, an automated differential testing framework for systematically detecting precision-induced behavioral disagreements in LLMs. PrecisionDiff generates precision-sensitive test inputs and performs cross-precision comparative analysis to uncover subtle divergences that remain hidden under conventional testing strategies. To demonstrate its practical significance, we instantiate PrecisionDiff on the alignment verification task, where precision-induced disagreements manifest as jailbreak divergence-inputs that are rejected under one precision may produce harmful responses under another. Experimental results show that such behavioral disagreements are widespread across multiple open-source aligned LLMs and precision settings, and that PrecisionDiff significantly outperforms vanilla testing methods in detecting these issues. Our work enables automated precision-sensitive test generation, facilitating effective pre-deployment evaluation and improving precision robustness during training.

---


### 28. [SkillGraph: Graph Foundation Priors for LLM Agent Tool Sequence Recommendation](https://arxiv.org/abs/2604.19793)

**<font color=#1a73e8>作者：</font>** Hao Liu, Dongyu Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents must select tools from large API libraries and order them correctly. Existing methods use semantic similarity for both retrieval and ordering, but ordering depends on inter-tool data dependencies that are absent from tool descriptions. As a result, semantic-only methods can produce negative Kendall-$\tau$ in structured workflow domains. We introduce SkillGraph, a directed weighted execution-transition graph mined from 49,831 successful LLM agent trajectories, which encodes workflow-precedence regularities as a reusable graph foundation prior. Building on this graph foundation prior, we propose a two-stage decoupled framework: GS-Hybrid retrieval for candidate selection and a learned pairwise reranker for ordering. On ToolBench (9,965 test instances; ~16,000 tools), the method reaches Set-F1 = 0.271 and Kendall-$\tau$ = 0.096; on API-Bank, Kendall-$\tau$ improves from -0.433 to +0.613. Under identical Stage-1 inputs, the learned reranker also outperforms LLaMA-3.1-8B Stage-2 rerankers.

---


### 29. [The AI Telco Engineer: Toward Autonomous Discovery of Wireless Communications Algorithms](https://arxiv.org/abs/2604.19803)

**<font color=#1a73e8>作者：</font>** Fayçal Aït Aoudia, Jakob Hoydis, Sebastian Cammerer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI is rapidly transforming the way research is conducted, from prototyping ideas to reproducing results found in the literature. In this paper, we explore the ability of agentic AI to autonomously design wireless communication algorithms. To that end, we implement a dedicated framework that leverages large language models (LLMs) to iteratively generate, evaluate, and refine candidate algorithms. We evaluate the framework on three tasks spanning the physical (PHY) and medium access control (MAC) layers: statistics-agnostic channel estimation, channel estimation with known covariance, and link adaptation. Our results show that, in a matter of hours, the framework produces algorithms that are competitive with and, in some cases, outperforming conventional baselines. Moreover, unlike neural network-based approaches, the generated algorithms are fully explainable and extensible. This work represents a first step toward the autonomous discovery of novel wireless communication algorithms, and we look forward to the progress our community makes in this direction.

---


### 30. [MIRROR: A Hierarchical Benchmark for Metacognitive Calibration in Large Language Models](https://arxiv.org/abs/2604.19809)

**<font color=#1a73e8>作者：</font>** Jason Z Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce MIRROR, a benchmark comprising eight experiments across four metacognitive levels that evaluates whether large language models can use self-knowledge to make better decisions. We evaluate 16 models from 8 labs across approximately 250,000 evaluation instances using five independent behavioral measurement channels. Core experiments are run across the full model roster; experiments with specialized infrastructure requirements report explicitly marked model subsets. We find two phenomena with direct implications for agentic deployment: (1) compositional self-prediction fails universally -- the Compositional Calibration Error ranges from 0.500 to 0.943 on the original 15-model Exp3-v1 set (and 0.434 to 0.758 on the balanced 16-model Exp3-v2 expansion), indicating that models cannot predict their own performance on multi-domain tasks, and (2) models exhibit above-chance but imperfect domain-specific self-knowledge yet systematically fail to translate even this partial awareness into appropriate agentic action-selection -- external metacognitive control reduces the Confident Failure Rate from 0.600 to 0.143 (76% reduction at temperature 0; mean 70% at temperature 0.7 across 5 models from 4 labs). Providing models with their own calibration scores produces no significant improvement (p > 0.05); only architectural constraint is effective. This suggests that external metacognitive scaffolding -- not improved self-knowledge -- is the path to safer autonomous AI systems. Code, data, and Croissant metadata will be released publicly with the benchmark.

---


### 31. [Large Language Models Meet Biomedical Knowledge Graphs for Mechanistically Grounded Therapeutic Prioritization](https://arxiv.org/abs/2604.19815)

**<font color=#1a73e8>作者：</font>** Chih-Hsuan Wei, Chi-Ping Day, Zhizheng Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Drug repurposing is often framed as a candidate identification task, but existing approaches provide limited guidance for distinguishing biologically plausible candidates from historically well-connected ones. Here we introduce DrugKLM, a hybrid framework that integrates biomedical knowledge graph structure with large language model-based mechanistic reasoning to enable mechanistically grounded therapeutic prioritization. Across benchmark datasets, DrugKLM outperforms knowledge graph-only and language model-only baselines, including TxGNN. Beyond improved recall, DrugKLM confidence scores exhibit functional alignment with molecular phenotypes: higher scores are associated with transcriptional signatures linked to improved survival across 12 TCGA cancers. The scoring framework preferentially captures biologically perturbational signals rather than historical indication patterns. Expert curation across five cancers further reveals systematic differences in prioritization behavior, with DrugKLM elevating candidates supported by coherent mechanistic rationale and disease-specific clinical context. Together, these results establish DrugKLM as an evidence-integrative framework that translates heterogeneous biomedical data into mechanistically interpretable and clinically grounded therapeutic hypotheses.

---


### 32. [Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts](https://arxiv.org/abs/2604.19835)

**<font color=#1a73e8>作者：</font>** Chaitanya Dwivedi, Binxuan Huang, Himanshu Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) has become the dominant architecture for scaling large language models: frontier models routinely decouple total parameters from per-token computation through sparse expert routing. Scaling laws show that under fixed active computation, model quality scales predictably with total parameters, and MoEs realize this by increasing expert count. However, training large MoEs is expensive, as memory requirements and inter-device communication both scale with total parameter count. We propose expert upcycling, a method for progressively expanding MoE capacity by increasing the number of experts during continued pre-training (CPT). Given a trained E-expert model, the upcycling operator constructs an mE-expert model through expert duplication and router extension while holding top-K routing fixed, preserving per-token inference cost. Duplication provides a warm initialization: the expanded model inherits the source checkpoint's learned representations, starting from a substantially lower loss than random initialization. Subsequent CPT then breaks the symmetry among duplicated experts to drive specialization. We formalize the upcycling operator and develop a theoretical framework decomposing the quality gap into a capacity term and an initialization term. We further introduce utility-based expert selection, which uses gradient-based importance scores to guide non-uniform duplication, more than tripling gap closure when CPT is limited. In our 7B-13B total parameter experiments, the upcycled model matches the fixed-size baseline on validation loss while saving 32% of GPU hours. Comprehensive ablations across model scales, activation ratios, MoE architectures, and training budgets yield a practical recipe for deploying expert upcycling, establishing it as a principled, compute-efficient alternative to training large MoE models from scratch.

---


### 33. [Forage V2: Knowledge Evolution and Transfer in Autonomous Agent Organizations](https://arxiv.org/abs/2604.19837)

**<font color=#1a73e8>作者：</font>** Huaqing Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents operating in open-world tasks -- where the completion boundary is not given in advance -- face denominator blindness: they systematically underestimate the scope of the target space. Forage V1 addressed this through co-evolving evaluation (an independent Evaluator discovers what "complete" means) and method isolation (Evaluator and Planner cannot see each other's code). V2 extends the architecture from a single expedition to a learning organization: experience accumulates across runs, transfers across model capabilities, and institutional safeguards prevent knowledge degradation.
We demonstrate two claims across three task types (web scraping, API queries, mathematical reasoning). Knowledge accumulation: over six runs, knowledge entries grow from 0 to 54, and denominator estimates stabilize as domain understanding deepens. Knowledge transfer: a weaker agent (Sonnet) seeded with a stronger agent's (Opus) knowledge narrows a 6.6pp coverage gap to 1.1pp, halves cost (9.40 to 5.13 USD), converges in half the rounds (mean 4.5 vs. 7.0), and three independent seeded runs arrive at exactly the same denominator estimate (266), suggesting organizational knowledge calibrates evaluation itself.
V2's contribution is architectural: it designs institutions -- audit separation, contract protocols, organizational memory -- that make any agent more reliable upon entry. The accumulated experience is organizational, model-agnostic, and transferable, stored as readable documents that any future agent inherits regardless of provider or capability level.

---


### 34. [Environmental Understanding Vision-Language Model for Embodied Agent](https://arxiv.org/abs/2604.19839)

**<font color=#1a73e8>作者：</font>** Jinsik Bang, Jaeyeon Bae, Donggyu Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown strong perception and reasoning abilities for instruction-following embodied agents. However, despite these abilities and their generalization performance, they still face limitations in environmental understanding, often failing on interactions or relying on environment metadata during execution. To address this challenge, we propose a novel framework named Environmental Understanding Embodied Agent (EUEA), which fine-tunes four core skills: 1) object perception for identifying relevant objects, 2) task planning for generating interaction subgoals, 3) action understanding for judging success likelihood, and 4) goal recognition for determining goal completion. By fine-tuning VLMs with EUEA skills, our framework enables more reliable task execution for instruction-following. We further introduce a recovery step that leverages these core skills and a group relative policy optimization (GRPO) stage that refines inconsistent skill predictions. The recovery step samples alternative actions to correct failure cases, and the GRPO stage refines inconsistent skill predictions. Across ALFRED tasks, our VLM significantly outperforms a behavior-cloning baseline, achieving an 8.86% improvement in average success rate. The recovery and GRPO stages provide an additional 3.03% gain, further enhancing overall performance. Finally, our skill-level analyses reveal key limitations in the environmental understanding of closed- and open-source VLMs and identify the capabilities necessary for effective agent-environment interaction.

---


### 35. [If you're waiting for a sign... that might not be it! Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems](https://arxiv.org/abs/2604.19844)

**<font color=#1a73e8>作者：</font>** Jiamin Chang, Minhui Xue, Ruoxi Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in embodied Vision-Language Agentic Systems (VLAS), powered by large vision-language models (LVLMs), enable AI systems to perceive and reason over real-world scenes. Within this context, environmental signals such as traffic lights are essential in-band signals that can and should influence agent behavior. However, similar signals could also be crafted to operate as misleading visual injections, overriding user intent and posing security risks. This duality creates a fundamental challenge: agents must respond to legitimate environmental cues while remaining robust to misleading ones. We refer to this tension as trust boundary confusion. To study this behavior, we design a dual-intent dataset and evaluation framework, through which we show that current LVLM-based agents fail to reliably balance this trade-off, either ignoring useful signals or following harmful ones. We systematically evaluate 7 LVLM agents across multiple embodied settings under both structure-based and noise-based visual injections. To address these vulnerabilities, we propose a multi-agent defense framework that separates perception from decision-making to dynamically assess the reliability of visual inputs. Our approach significantly reduces misleading behaviors while preserving correct responses and provides robustness guarantees under adversarial perturbations. The code of the evaluation framework and artifacts are made available at this https URL.

---


### 36. [Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization](https://arxiv.org/abs/2604.19857)

**<font color=#1a73e8>作者：</font>** Carter Adams, Rafael Oliveira, Gabriel Almeida 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement fine-tuning with verifiable rewards (RLVR) has emerged as a powerful paradigm for equipping large vision-language models (LVLMs) with agentic capabilities such as tool use and multi-step reasoning. Despite striking empirical successes, most notably Visual Agentic Reinforcement Fine-Tuning (Visual-ARFT), the theoretical underpinnings of this paradigm remain poorly understood. In particular, two critical questions lack rigorous answers: (i)~how does the composite structure of verifiable rewards (format compliance, answer accuracy, tool executability) affect the convergence of Group Relative Policy Optimization (GRPO), and (ii)~why does training on a small set of tool-augmented tasks transfer to out-of-distribution domains? We address these gaps by introducing the \emph{Tool-Augmented Markov Decision Process} (TA-MDP), a formal framework that models multimodal agentic decision-making with bounded-depth tool calls. Within this framework, we establish three main results. First, we prove that GRPO under composite verifiable rewards converges to a first-order stationary point at rate $O(1/\sqrt{T})$ with explicit dependence on the number of reward components and group size (\textbf{Theorem~1}). Second, we derive a \emph{Reward Decomposition Theorem} that bounds the sub-optimality gap between decomposed per-component optimization and joint optimization, providing a precise characterization of when reward decomposition is beneficial (\textbf{Theorem~2}). Third, we establish a PAC-Bayes generalization bound for tool-augmented policies that explains the strong out-of-distribution transfer observed in Visual-ARFT (\textbf{Theorem~3}).

---


### 37. [DR-Venus: Towards Frontier Edge-Scale Deep Research Agents with Only 10K Open Data](https://arxiv.org/abs/2604.19859)

**<font color=#1a73e8>作者：</font>** Venus Team, Sunhao Dai, Yong Deng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge-scale deep research agents based on small language models are attractive for real-world deployment due to their advantages in cost, latency, and privacy. In this work, we study how to train a strong small deep research agent under limited open-data by improving both data quality and data utilization. We present DR-Venus, a frontier 4B deep research agent for edge-scale deployment, built entirely on open data. Our training recipe consists of two stages. In the first stage, we use agentic supervised fine-tuning (SFT) to establish basic agentic capability, combining strict data cleaning with resampling of long-horizon trajectories to improve data quality and utilization. In the second stage, we apply agentic reinforcement learning (RL) to further improve execution reliability on long-horizon deep research tasks. To make RL effective for small agents in this setting, we build on IGPO and design turn-level rewards based on information gain and format-aware regularization, thereby enhancing supervision density and turn-level credit assignment. Built entirely on roughly 10K open-data, DR-Venus-4B significantly outperforms prior agentic models under 9B parameters on multiple deep research benchmarks, while also narrowing the gap to much larger 30B-class systems. Our further analysis shows that 4B agents already possess surprisingly strong performance potential, highlighting both the deployment promise of small models and the value of test-time scaling in this setting. We release our models, code, and key recipes to support reproducible research on edge-scale deep research agents.

---


### 38. [From Signal Degradation to Computation Collapse: Uncovering the Two Failure Modes of LLM Quantization](https://arxiv.org/abs/2604.19884)

**<font color=#1a73e8>作者：</font>** Chenxi Zhou, Pengfei Cao, Jiang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-Training Quantization (PTQ) is critical for the efficient deployment of Large Language Models (LLMs). While 4-bit quantization is widely regarded as an optimal trade-off, reducing the precision to 2-bit usually triggers a catastrophic ``performance cliff.'' It remains unclear whether the underlying mechanisms differ fundamentally. Consequently, we conduct a systematic mechanistic analysis, revealing two qualitatively distinct failure modes: Signal Degradation, where the computational patterns remain intact but information precision is impaired by cumulative error; and Computation Collapse, where key components fail to function, preventing correct information processing and destroying the signal in the early layers. Guided by this diagnosis, we conduct mechanism-aware interventions, demonstrating that targeted, training-free repair can mitigate Signal Degradation, but remains ineffective for Computation Collapse. Our findings provide a systematic diagnostic framework for PTQ failures and suggest that addressing Computation Collapse requires structural reconstruction rather than mere compensation.

---


### 39. [Depression Risk Assessment in Social Media via Large Language Models](https://arxiv.org/abs/2604.19887)

**<font color=#1a73e8>作者：</font>** Giorgia Gulino, Manuel Petrucci  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depression is one of the most prevalent and debilitating mental health conditions worldwide, frequently underdiagnosed and undertreated. The proliferation of social media platforms provides a rich source of naturalistic linguistic signals for the automated monitoring of psychological well-being. In this work, we propose a system based on Large Language Models (LLMs) for depression risk assessment in Reddit posts, through multi-label classification of eight depression-associated emotions and the computation of a weighted severity index. The method is evaluated in a zero-shot setting on the annotated DepressionEmo dataset (~6,000 posts) and applied in-the-wild to 469,692 comments collected from four subreddits over the period 2024-2025. Our best model, gemma3:27b, achieves micro-F1 = 0.75 and macro-F1 = 0.70, results competitive with purpose-built fine-tuned models (BART: micro-F1 = 0.80, macro-F1 = 0.76). The in-the-wild analysis reveals consistent and temporally stable risk profiles across communities, with marked differences between r/depression and r/anxiety. Our findings demonstrate the feasibility of a cost-effective, scalable approach for large-scale psychological monitoring.

---


### 40. [MMCORE: MultiModal COnnection with Representation Aligned Latent Embeddings](https://arxiv.org/abs/2604.19902)

**<font color=#1a73e8>作者：</font>** Zijie Li, Yichun Shi, Jingxiang Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MMCORE, a unified framework designed for multimodal image generation and editing. MMCORE leverages a pre-trained Vision-Language Model (VLM) to predict semantic visual embeddings via learnable query tokens, which subsequently serve as conditioning signals for a diffusion model. This streamlined design effectively transfers the rich understanding and reasoning capabilities of VLMs into the visual generation process. By obviating the need for deep fusion between autoregressive and diffusion models or training from scratch, MMCORE significantly reduces computational overhead while maintaining high-fidelity synthesis.
MMCORE seamlessly integrates text-to-image synthesis with interleaved image generation, demonstrating robust multimodal comprehension in complex scenarios such as spatial reasoning and visual grounding. Comprehensive evaluations indicate that MMCORE consistently outperforms state-of-the-art baselines across a broad spectrum of text-to-image and single/multi-image editing benchmarks.

---


### 41. [SceneOrchestra: Efficient Agentic 3D Scene Synthesis via Full Tool-Call Trajectory Generation](https://arxiv.org/abs/2604.19907)

**<font color=#1a73e8>作者：</font>** Yun He, Kelin Yu, Matthias Zwicker  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent agentic frameworks for 3D scene synthesis have advanced realism and diversity by integrating heterogeneous generation and editing tools. These tools are organized into workflows orchestrated by an off-the-shelf LLM. Current approaches typically adopt an execute-review-reflect loop: at each step, the orchestrator executes a tool, renders intermediate results for review, and then decides on the tool and its parameters for the next step. However, this design has two key limitations. First, next-step tool selection and parameter configuration are driven by heuristic rules, which can lead to suboptimal execution flows, unnecessary tool invocations, degraded output quality, and increased runtime. Second, rendering and reviewing intermediate results after each step introduces additional latency. To address these issues, we propose SceneOrchestra, a trainable orchestration framework that optimizes the tool-call execution flow and eliminates the step-by-step review loop, improving both efficiency and output quality. SceneOrchestra consists of an orchestrator and a discriminator, which we fine-tune with a two-phase training strategy. In the first phase, the orchestrator learns context-aware tool selection and complete tool-call trajectory generation, while the discriminator is trained to assess the quality of full trajectories, enabling it to select the best trajectory from multiple candidates. In the second phase, we perform interleaved training, where the discriminator adapts to the orchestrator's evolving trajectory distribution and distills its discriminative capability back into the orchestrator. At inference, we only use the orchestrator to generate and execute full tool-call trajectories from instructions, without requiring the discriminator. Extensive experiments show that our method achieves state-of-the-art scene quality while reducing runtime compared to previous work.

---


### 42. [Commonsense Knowledge with Negation: A Resource to Enhance Negation Understanding](https://arxiv.org/abs/2604.19921)

**<font color=#1a73e8>作者：</font>** Zijie Wang, MohammadHossein Rezaei, Farzana Rashid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Negation is a common and important semantic feature in natural language, yet Large Language Models (LLMs) struggle when negation is involved in natural language understanding tasks. Commonsense knowledge, on the other hand, despite being a well-studied topic, lacks investigations involving negation. In this work, we show that commonsense knowledge with negation is challenging for models to understand. We present a novel approach to automatically augment existing commonsense knowledge corpora with negation, yielding two new corpora containing over 2M triples with if-then relations. In addition, pre-training LLMs on our corpora benefits negation understanding.

---


### 43. [Tracing Relational Knowledge Recall in Large Language Models](https://arxiv.org/abs/2604.19934)

**<font color=#1a73e8>作者：</font>** Nicholas Popovič, Michael Färber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study how large language models recall relational knowledge during text generation, with a focus on identifying latent representations suitable for relation classification via linear probes. Prior work shows how attention heads and MLPs interact to resolve subject, predicate, and object, but it remains unclear which representations support faithful linear relation classification and why some relation types are easier to capture linearly than others. We systematically evaluate different latent representations derived from attention head and MLP contributions, showing that per-head attention contributions to the residual stream are comparatively strong features for linear relation classification. Feature attribution analyses of the trained probes, as well as characteristics of the different relation types, reveal clear correlations between probe accuracy and relation specificity, entity connectedness, and how distributed the signal on which the probe relies is across attention heads. Finally, we show how token-level feature attribution of probe predictions can be used to reveal probe behavior in further detail.

---


### 44. [Infection-Reasoner: A Compact Vision-Language Model for Wound Infection Classification with Evidence-Grounded Clinical Reasoning](https://arxiv.org/abs/2604.19937)

**<font color=#1a73e8>作者：</font>** Palawat Busaranuvong, Reza Saadati Fard, Emmanuel Agu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assessing chronic wound infection from photographs is challenging because visual appearance varies across wound etiologies, anatomical locations, and imaging conditions. Prior image-based deep learning methods have mainly focused on classification with limited interpretability, despite the need for evidence-grounded explanations to support point-of-care decision making. We present Infection-Reasoner, a compact 4B-parameter reasoning vision-language model for chronic wound infection classification and rationale generation. To address the scarcity of expert-labeled wound images with reasoning annotations, Infection-Reasoner is trained using a two-stage pipeline: (1) reasoning distillation, in which GPT-5.1 generates chain-of-thought rationales for unlabeled wound images to initialize wound-specific reasoning in a smaller student model (Qwen3-VL-4B-Thinking), and (2) reinforcement learning post-training with Group Relative Policy Optimization on a small labeled infection dataset to refine classification reasoning. On a held-out heterogeneous wound dataset, Infection-Reasoner achieved 86.8\% accuracy, 86.4\% sensitivity, and 87.1\% specificity, outperforming several strong baselines, including GPT-5.1. Rationale quality was further evaluated using both multimodal large language model (MLLM) judges and wound expert review. Across four MLLM judges, visual-support agreement scores ranged from 0.722 to 0.903, while expert review rated 61.8\% of rationales as Correct and 32.4\% as Partially Correct.

---


### 45. [Visual Reasoning through Tool-supervised Reinforcement Learning](https://arxiv.org/abs/2604.19945)

**<font color=#1a73e8>作者：</font>** Qihua Dong, Gozde Sahin, Pei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we investigate the problem of how to effectively master tool-use to solve complex visual reasoning tasks for Multimodal Large Language Models. To achieve that, we propose a novel Tool-supervised Reinforcement Learning (ToolsRL) framework, with direct tool supervision for more effective tool-use learning. We focus on a series of simple, native, and interpretable visual tools, including zoom-in, rotate, flip, and draw point/line, whose tool supervision is easy to collect. A reinforcement learning curriculum is developed, where the first stage is solely optimized by a set of well motivated tool-specific rewards, and the second stage is trained with the accuracy targeted rewards while allowing calling tools. In this way, tool calling capability is mastered before using tools to complete visual reasoning tasks, avoiding the potential optimization conflict among those heterogeneous tasks. Our experiments have shown that the tool-supervised curriculum training is efficient and ToolsRL can achieve strong tool-use capabilities for complex visual reasoning tasks.

---


### 46. [DistortBench: Benchmarking Vision Language Models on Image Distortion Identification](https://arxiv.org/abs/2604.19966)

**<font color=#1a73e8>作者：</font>** Divyanshu Goyal, Akhil Eppa, Vanya Bannihatti Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used in settings where sensitivity to low-level image degradations matters, including content moderation, image restoration, and quality monitoring. Yet their ability to recognize distortion type and severity remains poorly understood. We present DistortBench, a diagnostic benchmark for no-reference distortion perception in VLMs. DistortBench contains 13,500 four-choice questions covering 27 distortion types, six perceptual categories, and five severity levels: 25 distortions inherit KADID-10k calibrations, while two added rotation distortions use monotonic angle-based levels. We evaluate 18 VLMs, including 17 open-weight models from five families and one proprietary model. Despite strong performance on high-level vision-language tasks, the best model reaches only 61.9% accuracy, just below the human majority-vote baseline of 65.7% (average individual: 60.2%), indicating that low-level perceptual understanding remains a major weakness of current VLMs. Our analysis further reveals weak and non-monotonic scaling with model size, performance drops in most base--thinking pairs, and distinct severity-response patterns across model families. We hope DistortBench will serve as a useful benchmark for measuring and improving low-level visual perception in VLMs.

---


### 47. [Semantic Prompting: Agentic Incremental Narrative Refinement through Spatial Semantic Interaction](https://arxiv.org/abs/2604.19971)

**<font color=#1a73e8>作者：</font>** Xuxin Tang, Ibrahim Tahmid, Eric Krokos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interactive spatial layouts empower users to synthesize information and organize findings for sensemaking. While Large Language Models (LLMs) can automate narrative generation from spatial layouts, current collage-based and re-generation methods struggle to support the incremental spatial refinements inherent to the sensemaking process. We identify three critical gaps in existing spatial-textual generation: interaction-revision misalignment, human-LLM intent misalignment, and lack of granular customization. To address these, we introduce Semantic Prompting, a framework for spatial refinement that perceives semantic interactions, reasons about refinement intent, and performs targeted positional revisions. We implemented S-PRISM to realize this framework. The empirical evaluation demonstrated that S-PRISM effectively enhanced the precision of interaction-revision refinement. A user study ($N=14$) highlighted how participants leveraged S-PRISM for incremental formalization through interactive steering. Results showed that users valued its efficient, adaptable, and trustworthy support, which effectively strengthens human-LLM intent alignment.

---


### 48. [Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders](https://arxiv.org/abs/2604.19974)

**<font color=#1a73e8>作者：</font>** Het Patel, Tiejin Chen, Hua Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can be uncertain yet correct, or confident yet wrong, raising the question of whether their output-level uncertainty and their actual correctness are driven by the same internal mechanisms or by distinct feature populations. We introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently. Applying this to Llama-3.1-8B and Gemma-2-9B, we identify three feature populations that play fundamentally different functional roles. Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy. Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed. Confounded features that encode both signals are detrimental to output quality, and targeted suppression of them yields a 1.1% accuracy improvement and a 75% entropy reduction, with effects transferring across the ARC-Challenge and RACE benchmarks. The feature categories are also informationally distinct: the activations of just 3 confounded features from a single mid-network layer predict model correctness (AUROC ~0.79), enabling selective abstention that raises accuracy from 62% to 81% at 53% coverage. The results demonstrate that uncertainty and correctness are distinct internal phenomena, with implications for interpretability and targeted inference-time intervention.

---


### 49. [A Computational Model of Message Sensation Value in Short Video Multimodal Features that Predicts Sensory and Behavioral Engagement](https://arxiv.org/abs/2604.19995)

**<font color=#1a73e8>作者：</font>** Haoning Xue, Jingwen Zhang, Xiaohui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The contemporary media landscape is characterized by sensational short videos. While prior research examines the effects of individual multimodal features, the collective impact of multimodal features on viewer engagement with short videos remains unknown. Grounded in the theoretical framework of Message Sensation Value (MSV), this study develops and tests a computational model of MSV with multimodal feature analysis and human evaluation of 1,200 short videos. This model that predicts sensory and behavioral engagement was further validated across two unseen datasets from three short video platforms (combined N = 14,492). While MSV is positively associated with sensory engagement, it shows an inverted U-shaped relationship with behavioral engagement: Higher MSV elicits stronger sensory stimulation, but moderate MSV optimizes behavioral engagement. This research advances the theoretical understanding of short video engagement and introduces a robust computational tool for short video research.

---


### 50. [EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training](https://arxiv.org/abs/2604.20012)

**<font color=#1a73e8>作者：</font>** Yiyang Du, Zhanqiu Guo, Xin Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action Models (VLAs) inherit their visual and linguistic capabilities from Vision-Language Models (VLMs), yet most VLAs are built from off-the-shelf VLMs that are not adapted to the embodied domain, limiting their downstream performance. In this work, we propose EmbodiedMidtrain to bridge the gap between VLMs and VLAs. We first characterize the data distribution gap between them, showing that VLA data occupy compact regions that are largely separated from the broader VLM distribution, while the degree of alignment varies substantially both across and within VLM data sources. Then, we build a mid-training data engine that leverages a lightweight learnable proximity estimator to select the most VLA-aligned candidates from a large VLM pool, and mid-trains the VLM on this curated mixture before downstream VLA fine-tuning. Experiments on three robot manipulation benchmarks show that mid-training consistently improves performance across different VLM backbones, achieving results competitive with expert VLAs and off-the-shelf VLMs trained with larger model scale and training budgets. Further analysis reveals that mid-training provides a stronger initialization for VLA fine-tuning, with gains emerging from the earliest steps and widening throughout training. Moreover, the data engine captures both dataset-level and sample-level alignment signals, favoring spatial reasoning over text-centric tasks while preserving the diversity of the VLM data. We will release all code, data and models for future research.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-129](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
