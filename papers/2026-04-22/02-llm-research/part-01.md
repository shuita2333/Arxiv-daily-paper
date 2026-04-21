# 🧠 大模型相关研究 | 2026年04月22日

> 本类共 **353** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 1. [Multimodal Claim Extraction for Fact-Checking](https://arxiv.org/abs/2604.16311)

**<font color=#1a73e8>作者：</font>** Joycelyn Teo, Rui Cao, Zhenyun Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated Fact-Checking (AFC) relies on claim extraction as a first step, yet existing methods largely overlook the multimodal nature of today's misinformation. Social media posts often combine short, informal text with images such as memes, screenshots, and photos, creating challenges that differ from both text-only claim extraction and well-studied multimodal tasks like image captioning or visual question answering. In this work, we present the first benchmark for multimodal claim extraction from social media, consisting of posts containing text and one or more images, annotated with gold-standard claims derived from real-world fact-checkers. We evaluate state-of-the-art multimodal LLMs (MLLMs) under a three-part evaluation framework (semantic alignment, faithfulness, and decontextualization) and find that baseline MLLMs struggle to model rhetorical intent and contextual cues. To address this, we introduce MICE, an intent-aware framework which shows improvements in intent-critical cases.

---


### 2. [Annotation Entropy Predicts Per-Example Learning Dynamics in LoRA Fine-Tuning](https://arxiv.org/abs/2604.16332)

**<font color=#1a73e8>作者：</font>** Brady Steele  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We find that LoRA fine-tuning exhibits un-learning on contested examples: items with high annotator disagreement show increasing loss during training, a qualitatively distinct pattern largely absent under full fine-tuning and consistent across all six models tested (four encoder, two decoder-only). This discovery emerges from correlating annotation entropy, computed from ChaosNLI's 100 labels per example, with per-example area under the loss curve (AULC) on SNLI and MNLI. The correlation is positive in all 25 conditions tested (Spearman $\rho = 0.06$-$0.43$), with decoder-only models showing stronger correlations than encoders at matched LoRA rank. The effect survives partial-correlation controls and replicates across seeds and datasets. A preliminary noise-injection experiment is consistent with these findings.

---


### 3. [A Discordance-Aware Multimodal Framework with Multi-Agent Clinical Reasoning](https://arxiv.org/abs/2604.16333)

**<font color=#1a73e8>作者：</font>** Pegah Ahadian, Mingrui Yang, Sixu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knee osteoarthritis frequently exhibits discordance between structural damage observed in imaging and patient-reported symptoms such as pain. This mismatch complicates clinical interpretation and patient stratification and remains insufficiently modeled in existing decision support systems. We propose a discordance aware multimodal framework that combines machine learning prediction models with a tool grounded multi agent reasoning system. Using baseline data from the FNIH Osteoarthritis Biomarkers Consortium, we trained multimodal models to predict two progression tasks, joint space loss only progression versus non progression, and pain only progression versus non progression. The predictive system integrates three modality specific experts: a CatBoost tabular model using demographic, radiographic, MRI-derived scalar, and biomarker features; MRI image embeddings extracted using a ResNet18 backbone; and Xray embeddings derived from the same architecture. Expert predictions are fused using a stacking ensemble. Residual based models estimate expected pain from structural features, enabling the computation of a pain structure discordance score between observed and expected symptoms. A multi-agent reasoning layer interprets these signals to assign clinically interpretable OA phenotypes and generate phenotype specific management recommendations.

---


### 4. [Beyond Verifiable Rewards: Rubric-Based GRM for Reinforced Fine-Tuning SWE Agents](https://arxiv.org/abs/2604.16335)

**<font color=#1a73e8>作者：</font>** Jiawei Huang, Qingping Yang, Renjie Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in Large Language Model (LLM) Agents for Software Engineering (SWE) tasks, end-to-end fine-tuning typically relies on verifiable terminal rewards such as whether all unit tests pass. While these binary signals reflect whether the final solution is correct, they provide little guidance for shaping intermediate behaviors during multi-step interactions, thereby limiting improvements in the overall quality of the resolution process. To address this, we introduce a rubric-based Generative Reward Model (GRM) that provides richer learning signals. The GRM is equipped with human-designed rubrics that indicate criteria for encouraging or discouraging specific behavioral patterns, and we leverage this feedback for high-quality training data collection via trajectory filtration. When used for Reinforced Fine-Tuning (RFT) on SWE Tasks, our approach outperforms terminal-score-only rejection sampling: it more effectively suppresses undesirable patterns while promoting beneficial ones, as confirmed by case analyses, and it ultimately improves final test accuracy.

---


### 5. [Governing the Agentic Enterprise: A Governance Maturity Model for Managing AI Agent Sprawl in Business Operations](https://arxiv.org/abs/2604.16338)

**<font color=#1a73e8>作者：</font>** Vivek Acharya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of agentic AI in enterprise business operations--autonomous systems capable of planning, reasoning, and executing multi-step workflows--has created an urgent governance crisis. Organizations face uncontrolled agent sprawl: the proliferation of redundant, ungoverned, and conflicting AI agents across business functions. Industry surveys report that only 21% of enterprises have mature governance models for autonomous agents, while 40% of agentic AI projects are projected to fail by 2027 due to inadequate governance and risk controls. Despite growing acknowledgment of this challenge, academic literature lacks a formal, empirically validated governance maturity model connecting governance capability to measurable business outcomes. This paper introduces the Agentic AI Governance Maturity Model (AAGMM), a five-level framework spanning 12 governance domains, grounded in NIST AI RMF and ISO/IEC 42001 standards. We additionally propose a novel taxonomy of agent sprawl patterns--functional duplication, shadow agents, orphaned agents, permission creep, and unmonitored delegation chains--each linked to quantifiable business cost models. The framework is validated through 750 simulation runs across five enterprise scenarios and five governance maturity levels, measuring business outcomes including cost containment, risk incident rates, operational efficiency, and decision quality. Results demonstrate statistically significant differences (p < 0.001, large effect sizes d > 2.0) between all governance maturity levels, with Level 4-5 organizations achieving 94.3% lower sprawl indices, 96.4% fewer risk incidents, and 32.6% higher effective task completion rates compared to Level 1. The AAGMM provides practitioners with an actionable roadmap for governing autonomous AI agents while maximizing business returns.

---


### 6. [Semantic Consensus: Process-Aware Conflict Detection and Resolution for Enterprise Multi-Agent LLM Systems](https://arxiv.org/abs/2604.16339)

**<font color=#1a73e8>作者：</font>** Vivek Acharya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) systems are rapidly emerging as the dominant architecture for enterprise AI automation, yet production deployments exhibit failure rates between 41% and 86.7%, with nearly 79% of failures originating from specification and coordination issues rather than model capability limitations. This paper identifies Semantic Intent Divergence--the phenomenon whereby cooperating LLM agents develop inconsistent interpretations of shared objectives due to siloed context and absent process models--as a primary yet formally unaddressed root cause of multi-agent failure in enterprise settings. We propose the Semantic Consensus Framework (SCF), a process-aware middleware comprising six components: a Process Context Layer for shared operational semantics, a Semantic Intent Graph for formal intent representation, a Conflict Detection Engine for real-time identification of contradictory, contention-based, and causally invalid intent combinations, a Consensus Resolution Protocol using a policy--authority--temporal hierarchy, a Drift Monitor for detecting gradual semantic divergence, and a Process-Aware Governance Integration layer for organizational policy enforcement. Evaluation across 600 runs spanning three multi-agent frameworks (AutoGen, CrewAI, LangGraph) and four enterprise scenarios demonstrates that SCF is the only approach to achieve 100% workflow completion--compared to 25.1% for the next-best baseline--while detecting 65.2% of semantic conflicts with 27.9% precision and providing complete governance audit trails. The framework is protocol-agnostic and compatible with MCP and A2A communication standards.

---


### 7. [SAGE: Sensor-Augmented Grounding Engine for LLM-Powered Sleep Care Agent](https://arxiv.org/abs/2604.16342)

**<font color=#1a73e8>作者：</font>** Hansoo Lee, Yoonjae Cho, Sonya S.Kwak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Sleep is vital for health, yet access to data alone does not guarantee improvement. While wearables and health apps enable tracking, users face a "Data-Action Gap," struggling to interpret metrics and translate them into action. Current interventions fail to bridge this: static dashboards lack context, rule-based agents rely on rigid scripts, and LLM-agents lack grounding in personal data, causing trust issues. We propose SAGE (Sensor-Augmented Grounding Engine) for an LLM-powered sleep care agent. SAGE normalizes continuous sleep, physiological, and activity data from the sensors into a queryable time-series layer. It supports (1) selective system-initiated monitoring that triggers notifications only upon detecting meaningful deviations against personal baselines to reduce alert fatigue, and (2) user-initiated Q&A where natural language is translated into executable database queries. By ensuring responses are grounded in precise period, comparison, and metric data, SAGE aims to enhance personalization, traceability, and trust, articulating a novel design space for evidence-based messaging in sleep care.

---


### 8. [Bridging the Experimental Last Mile: Digitizing Laboratory Know-How for Safe AI-Assisted Support](https://arxiv.org/abs/2604.16345)

**<font color=#1a73e8>作者：</font>** Akira Miura, Yuki Sasahara, Momoka Demura 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Advances in Materials Informatics have accelerated the development of Self-Driving Laboratories (SDLs), yet human-led experiments remain standard in many educational and exploratory research settings. In such environments, practical know-how, including operational details and site-specific rules, is essential for safe and reliable laboratory work. In this proof-of-concept study, we developed a human-in-the-loop AI assistant that combines first-person experimental video, multimodal AI, and retrieval-augmented generation (RAG). Using powder X-ray diffraction experiments and student-recorded video data as inputs, the system extracts site-specific laboratory knowledge from recorded procedures, including physical techniques and audible confirmation that conventional manuals could omit. It then provides grounded responses based on the resulting manual. To reduce the risk of unsupported outputs, the system employs a two-layer safety design: source restriction through RAG and strict system-prompt constraints. Instructor-based evaluation showed alignment with expected guidance for questions covered by the manual. For out-of-scope queries, the system appropriately refused to answer, indicating a reduced risk of hallucination. Expert evaluation further indicated that the generated advisory reports were useful and safe (utility: 3.25/4.00; safety: 4.00/4.00). These results suggest a framework in which AI supports laboratory practice under explicit human supervision rather than replacing human judgment.

---


### 9. [DR. INFO at the Point of Care: A Prospective Pilot Study of an Agentic AI Clinical Assistant](https://arxiv.org/abs/2604.16346)

**<font color=#1a73e8>作者：</font>** Rogerio Corga Da Silva, Miguel Romano, Tiago Mendes 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background: Clinical documentation and information retrieval consume over half of physicians working hours, contributing to cognitive overload and burnout. While artificial intelligence offers a potential solution, concerns over hallucinations and source reliability have limited adoption at the point of care.
Objective: To evaluate clinician-reported time savings, decision-making support, and satisfaction with DR. INFO, an agentic AI clinical assistant, in routine clinical practice.
Methods: In this prospective, single-arm pilot study, 29 clinicians across multiple specialties in Portuguese healthcare institutions used DR. INFO v1.0 over five working days within a two-week period. Outcomes were assessed via daily Likert-scale evaluations and a final Net Promoter Score. Non-parametric methods were used throughout.
Results: Clinicians reported high perceived time saving (mean 4.27/5; 95% CI: 3.97-4.57) and decision support (4.16/5; 95% CI: 3.86-4.45), with ratings stable across all study days and no evidence of attrition bias. The Net Promoter Score was 81.2, with no detractors.
Conclusions: Clinicians across specialties and career stages reported sustained satisfaction with DR. INFO for both time efficiency and clinical decision support. Validation in larger, controlled studies with objective outcome measures is warranted.

---


### 10. [Beyond the Townhall: Spatial Anchoring and LLM Agents for Scalable Participatory Urban Planning](https://arxiv.org/abs/2604.16348)

**<font color=#1a73e8>作者：</font>** Carina I Hausladen, Javier Argota Sánchez-Vaquerizo, Michael Siebenmann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Participatory urban planning is central to sustainable city-making, yet the technically demanding nature of such interventions often limits meaningful involvement by diverse publics. We introduce a scalable digital participation platform that embeds sustainability projects within a navigable digital twin. Citizens experience a guided virtual walkthrough with audio narration employing the method of loci and spatial anchoring to support mnemonic encoding and recall. This immersive interface is augmented by two purpose-built LLM assistants: one delivers source-grounded factual clarifications, while the other facilitates reflective discussion. We evaluated this system in a randomized controlled online experiment (N = 195) against conventional industry practices (static visualizations and text-based consultations). Results show that spatially anchored immersive presentation significantly improved information recall, which substantially shifted participants' attention from individual inconveniences to collective, community-oriented sustainability benefits. Consequently, participants provided significantly more constructive, solution-focused feedback to the (simulated) municipality. These findings establish a practical tool for cities and policymakers to foster inclusive, democratic participation in sustainability transitions.

---


### 11. [SaFeR-Steer: Evolving Multi-Turn MLLMs via Synthetic Bootstrapping and Feedback Dynamics](https://arxiv.org/abs/2604.16358)

**<font color=#1a73e8>作者：</font>** Haolong Hu, Hanyu Li, Tiancheng He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MLLMs are increasingly deployed in multi-turn settings, where attackers can escalate unsafe intent through the evolving visual-text history and exploit long-context safety decay. Yet safety alignment is still dominated by single-turn data and fixed-template dialogues, leaving a mismatch between training and this http URL bridge this gap, we propose SaFeR-Steer, a progressive multi-turn alignment framework that combines staged synthetic bootstrapping with tutor-in-the-loop GRPO to train a single student under adaptive, on-policy attacks. We also introduce TCSR, which uses trajectory minimum/average safety to propagate late-turn failures to earlier turns.I. Dataset. We release STEER, a multi-turn multimodal safety dataset with STEER-SFT (12,934), STEER-RL (2,000), and STEER-Bench (3,227) dialogues spanning 2~10 this http URL. Experiment. Starting from Qwen2.5-VL-3B/7B, SaFeR-Steer substantially improves Safety/Helpfulness on both single-turn (48.30/45.86 -> 81.84/70.77 for 3B; 56.21/60.32 -> 87.89/77.40 for 7B) and multi-turn benchmarks (12.55/27.13 -> 55.58/70.27 for 3B; 24.66/46.48 -> 64.89/72.35 for 7B), shifting failures to later turns and yielding robustness beyond scaling this http URL are available at this https URL

---


### 12. [Cross-Family Speculative Decoding for Polish Language Models on Apple~Silicon: An Empirical Evaluation of Bielik~11B with UAG-Extended MLX-LM](https://arxiv.org/abs/2604.16368)

**<font color=#1a73e8>作者：</font>** Krzysztof Fonal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM inference by using a small draft model to propose k candidate tokens for a target model to verify. While effective for same-tokenizer pairs on high-bandwidth GPUs, its applicability to cross-family pairs with mismatched tokenizers and consumer-grade unified memory remains underexplored. We extend the MLX-LM framework with Universal Assisted Generation (UAG) to enable cross-tokenizer speculative decoding on Apple Silicon. We evaluate Bielik 11B-Instruct (Mistral-based) as the target model, paired with three draft models: Bielik 1.5B (Qwen-based with custom tokenizer), Qwen2.5-1.5B, and Llama 3.2-1B. Experiments on three Polish-language datasets (Wikipedia, pl_alpaca, synthetic) use draft lengths k in {2, 4, 6} to compare naive and context-aware token translation. Results show: (1) context-aware translation consistently improves acceptance rates across all configurations; (2) the Polish-specialized Bielik 1.5B achieves lower acceptance than general-purpose Qwen2.5 and Llama 3.2 drafters; (3) throughput on Apple Silicon is content-dependent, reaching 1.7x speedup for structured text but failing for varied instructions; and (4) verification cost on unified memory does not amortize as theory predicts because both models are memory-bandwidth bound, making sequential drafting expensive relative to batched verification. We propose a hardware-aware speedup formula and characterize conditions for cross-family speculative decoding on Apple Silicon. This is the first systematic evaluation of cross-family speculative decoding for Polish LLMs and the first empirical study of UAG-based decoding on unified memory architectures.

---


### 13. [CFMS: Towards Explainable and Fine-Grained Chinese Multimodal Sarcasm Detection Benchmark](https://arxiv.org/abs/2604.16372)

**<font color=#1a73e8>作者：</font>** Junzhao Zhang, Hsiu-Yuan Huang, Chenming Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal sarcasm detection has recently garnered significant attention. However, existing benchmarks suffer from coarse-grained annotations and limited cultural coverage, which hinder research into fine-grained semantic understanding. To address this, we construct CFMS, the first fine-grained multimodal sarcasm dataset tailored for Chinese social media. It comprises 2,796 high-quality image-text pairs and provides a triple-level annotation framework: sarcasm identification, target recognition, and explanation generation. We find that the fine-grained explanation annotations effectively guide AI in generating images with explicit sarcastic intent. Furthermore, we curate a high-consistency parallel Chinese-English metaphor subset (200 entries each), revealing significant limitations of current models in metaphoric reasoning. To overcome the constraints of traditional retrieval methods, we propose a Reinforcement Learning-augmented In-Context Learning strategy (PGDS) to dynamically optimize exemplar selection. Extensive experiments demonstrate that CFMS provides a solid foundation for building reliable multimodal sarcasm understanding systems, and the PGDS method significantly outperforms existing baselines on key tasks. Our data and code are available at this https URL.

---


### 14. [GoCoMA: Hyperbolic Multimodal Representation Fusion for Large Language Model-Generated Code Attribution](https://arxiv.org/abs/2604.16377)

**<font color=#1a73e8>作者：</font>** Nitin Choudhury, Bikrant Bikram Pratap Maurya, Bhavinkumar Vinodbhai Kuwar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) trained on massive code corpora are now increasingly capable of generating code that is hard to distinguish from human-written code. This raises practical concerns, including security vulnerabilities and licensing ambiguity, and also motivates a forensic question: 'Who (or which LLM) wrote this piece of code?' We present GoCoMA, a multimodal framework that models an extrinsic hierarchy between (i) code stylometry, capturing higher-level structural and stylistic signatures, and (ii) image representations of binary pre-executable artifacts (BPEA), capturing lower-level, execution-oriented byte semantics shaped by compilation and toolchains. GoCoMA projects modality embeddings into a hyperbolic Poincaré ball, fuses them via a geodesic-cosine similarity-based cross-modal attention (GCSA) fusion mechanism, and back-projects the fused representation to Euclidean space for final LLM-source attribution. Experiments on two open-source benchmarks (CoDET-M4 and LLMAuthorBench) show that GoCoMA consistently outperforms unimodal and Euclidean multimodal baselines under identical evaluation protocols.

---


### 15. [Reciprocal Co-Training (RCT): Coupling Gradient-Based and Non-Differentiable Models via Reinforcement Learning](https://arxiv.org/abs/2604.16378)

**<font color=#1a73e8>作者：</font>** Yunshuo Tian, Akayou Kitessa, Tanuja Chitnis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) and classical machine learning methods offer complementary strengths for predictive modeling, yet their fundamentally different representations and training paradigms hinder effective integration: LLMs rely on gradient-based optimization over textual data, whereas models such as Random Forests (RF) employ non-differentiable feature partitioning. This work introduces a reciprocal co-training framework that couples an LLM with an RF classifier via reinforcement learning, creating an iterative feedback loop in which each model improves using signals from the other. Tabular data are reformulated into standardized textual representations for the LLM, whose embeddings augment the RF feature space, while calibrated RF probability estimates provide feedback signals that guide reinforcement learning updates of the LLM. Experiments across three medical datasets demonstrate consistent performance gains for both models, with particularly strong effects for the LLM. Ablation analyses show that iterative refinement, hybrid reward design, and dimensionality control jointly contribute to these gains. The proposed framework provides a general mechanism that allows incompatible model families to leverage each other's strengths through bidirectional adaptation.

---


### 16. [Data Mixing for Large Language Models Pretraining: A Survey and Outlook](https://arxiv.org/abs/2604.16380)

**<font color=#1a73e8>作者：</font>** Zhuo Chen, Yuxuan Miao, Supryadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) rely on pretraining on massive and heterogeneous corpora, where training data composition has a decisive impact on training efficiency and downstream generalization under realistic compute and data budget constraints. Unlike sample-level data selection, data mixing optimizes domain-level sampling weights to allocate limited budgets more effectively. In recent years, a growing body of work has proposed principled data mixing methods for LLM pretraining; however, the literature remains fragmented and lacks a dedicated, systematic survey. This paper provides a comprehensive review of data mixing for LLM pretraining. We first formalize data mixture optimization as a bilevel problem on the probability simplex and clarify the role of data mixing in the pretraining pipeline, and briefly explain how existing methods make this formulation tractable in practice. We then introduce a fine-grained taxonomy that organizes existing methods along two dimensions: static versus dynamic mixing. Static mixing is further categorized into rule-based and learning-based methods, while dynamic mixing is grouped into adaptive and externally guided families. For each class, we summarize representative approaches and analyze their strengths and limitations from a performance-cost trade-off perspective. Building on this analysis, we highlight challenges that cut across methods, including limited transferability across data domains, optimization objectives, models, and validation sets, as well as unstandardized evaluation protocols and benchmarks, and the inherent tension between performance gains and cost control in learning-based methods. Finally, we outline several exploratory directions, including finer-grained domain partitioning and inverse data mixing, as well as pipeline-aware designs, aiming to provide conceptual and methodological insights for future research.

---


### 17. [LiFT: Does Instruction Fine-Tuning Improve In-Context Learning for Longitudinal Modelling by Large Language Models?](https://arxiv.org/abs/2604.16382)

**<font color=#1a73e8>作者：</font>** Iqra Ali, Talia Tseriotou, Mahmud Elahi Akhter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Longitudinal NLP tasks require reasoning over temporally ordered text to detect persistence and change in human behavior and opinions. However, in-context learning with large language models struggles on tasks where models must integrate historical context, track evolving interactions, and handle rare change events. We introduce LiFT, a longitudinal instruction fine-tuning framework that unifies diverse longitudinal modeling tasks under a shared instruction schema. LiFT uses a curriculum that progressively increases temporal difficulty while incorporating few-shot structure and temporal conditioning to encourage effective use of past context. We evaluate LiFT across five datasets. Models trained on longitudinal tasks with different levels of temporal granularity are tested for generalisability on two separate datasets. Across models with different parameter sizes (OLMo (1B/7B), LLaMA-8B, and Qwen-14B), LiFT consistently outperforms base-model ICL, with strong gains on out-of-distribution data and minority change events.

---


### 18. [QU-NLP at QIAS 2026: Multi-Stage QLoRA Fine-Tuning for Arabic Islamic Inheritance Reasoning](https://arxiv.org/abs/2604.16396)

**<font color=#1a73e8>作者：</font>** Mohammad AL-Smadi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Islamic inheritance law (ilm al-mawarıth) presents a challenging domain for evaluating large language models' structured reasoning capabilities, requiring multi-step legal analysis, rule-based blocking decisions, and precise fractional calculations. We present QU-NLP's submission to the QIAS 2026 shared task on Arabic Islamic inheritance reasoning. Our approach employs a multi-stage Quantized Low-Rank Adaptation (QLoRA) fine-tuning strategy on Qwen3-4B: (1) domain adaptation on 3,166 Islamic fatwa records to acquire inheritance terminology and jurisprudential reasoning patterns, followed by (2) task-specific training on 12,000 structured inheritance cases to optimize JSON-formatted output generation. Using 4-bit NF4 quantization with rank-128 LoRA adapters, our model achieves 90% MIR-E (Mawarith Inheritance Reasoning Evaluation) score on the test set, demonstrating competitive performance while requiring minimal computational resources. Our results show that domain-specific pre-adaptation combined with structured output training enables small language models to perform complex legal reasoning tasks effectively comparing to commercial systems such as Gemini-2.5-flash.

---


### 19. [Measuring Representation Robustness in Large Language Models for Geometry](https://arxiv.org/abs/2604.16421)

**<font color=#1a73e8>作者：</font>** Vedant Jawandhia, Yash Sinha, Murari Mandal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly evaluated on mathematical reasoning, yet their robustness to equivalent problem representations remains poorly understood. In geometry, identical problems can be expressed in Euclidean, coordinate, or vector forms, but existing benchmarks report accuracy on fixed formats, implicitly assuming representation invariance and masking failures caused by representational changes alone. We propose GeoRepEval, a representation-aware evaluation framework that measures correctness, invariance, and consistency at the problem level across parallel formulations, combining strict answer matching, bootstrap confidence intervals, paired McNemar tests, representation-flip analyses, and regression controls for surface complexity. We prove that our Invariance@3 metric decomposes accuracy into robust and fragile components and is bounded by the weakest representation. Evaluating eleven LLMs on 158 curated high-school geometry problems (474 instances), we find accuracy gaps of up to 14 percentage points induced solely by representation choice. Vector formulations emerge as a consistent failure point, with Invariance@3 as low as 0.044 even after controlling for length and symbolic complexity. A convert-then-solve prompting intervention improves vector accuracy by up to 52 percentage points for high-capacity models, suggesting that failures reflect representation sensitivity rather than inability; however, low-capacity models show no gains, indicating deeper limitations. These results suggest that current models rely on representation-specific heuristics rather than abstract geometric reasoning. All datasets, prompts, and scripts are released at this https URL.

---


### 20. [Injecting Structured Biomedical Knowledge into Language Models: Continual Pretraining vs. GraphRAG](https://arxiv.org/abs/2604.16422)

**<font color=#1a73e8>作者：</font>** Jaafer Klila, Sondes Bannour Souihi, Rahma Boujelben 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The injection of domain-specific knowledge is crucial for adapting language models (LMs) to specialized fields such as biomedicine. While most current approaches rely on unstructured text corpora, this study explores two complementary strategies for leveraging structured knowledge from the UMLS Metathesaurus: (i) Continual pretraining that embeds knowledge into model parameters, and (ii) Graph Retrieval-Augmented Generation (GraphRAG) that consults a knowledge graph at inference time. We first construct a large-scale biomedical knowledge graph from UMLS (3.4 million concepts and 34.2 million relations), stored in Neo4j for efficient querying. We then derive a ~100-million-token textual corpus from this graph to continually pretrain two models: BERTUMLS (from BERT) and BioBERTUMLS (from BioBERT). We evaluate these models on six BLURB (Biomedical Language Understanding and Reasoning Benchmark) datasets spanning five task types and evaluate GraphRAG on the two QA (Question Answering) datasets (PubMedQA, BioASQ). On BLURB tasks, BERTUMLS improves over BERT, with the largest gains on knowledge-intensive QA. Effects on BioBERT are more nuanced, suggesting diminishing returns when the base model already encodes substantial biomedical text knowledge. Finally, augmenting LLaMA 3-8B with our GraphRAG pipeline yields over than 3 points accuracy on PubMedQA and 5 points on BioASQ without any retraining, delivering transparent, multi-hop, and easily updated knowledge access. We release the processed UMLS Neo4j graph to support reproducibility.

---


### 21. [Shifting the Gradient: Understanding How Defensive Training Methods Protect Language Model Integrity](https://arxiv.org/abs/2604.16423)

**<font color=#1a73e8>作者：</font>** Satchel Grant, Victor Gillioz, Jake Ward 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Defensive training methods such as positive preventative steering (PPS) and inoculation prompting (IP) offer surprising results through seemingly similar processes: both add trait-inducing objects to large language models (LLMs) during training, and both defend the LLM against acquiring the trait. The surprising success of these methods comes with the question: how do they work? Are PPS and IP doing the same thing? We provide behavioral and mechanistic comparisons of these two methods using "evilness" as a case-study trait. Our central finding is that PPS and IP achieve their defensive benefits through distinct mechanisms. Behaviorally, we show that neither PPS nor IP operates through a purely associative mechanism; and PPS can both defend against trait acquisition and actively reduce pre-existing expression, whereas IP is ineffective in models that were previously finetuned to express the trait. This behavioral divergence is reflected mechanistically: PPS shifts the activation gradient towards an attenuating direction along the PPS vector axis. When the PPS vector is aligned with a trait-expressing axis, it can reverse the gradient pressure, reducing rather than increasing activation along that axis. In contrast, IP continues to resist a precise mechanistic account. Direct cosine similarity analyses reveal that IP has a characteristically different gradient signature than PPS, and qualitative analyses reveal IP's gradient to be more diffuse. Furthermore, IP reduces the next-token prediction loss on trait-expressing data where PPS need not, consistent with the notion that IP "explains away" the trait-expression in the training data. Taken together, our analyses reveal distinct mechanisms by which each method operates and highlight open questions about IP's mechanistic picture.

---


### 22. [Non-Stationarity in the Embedding Space of Time Series Foundation Models](https://arxiv.org/abs/2604.16428)

**<font color=#1a73e8>作者：</font>** Jinmyeong Choi, Brad Shook, Artur Dubrawski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) are widely used as generic feature extractors, yet the notion of non-stationarity in their embedding spaces remains poorly understood. Recent work often conflates non-stationarity with distribution shift, blurring distinctions fundamental to classical time-series analysis and long-standing methodologies such as statistical process control (SPC). In SPC, non-stationarity signals a process leaving a stable regime - via shifts in mean, variance, or emerging trends - and detecting such departures is central to quality monitoring and change-point analysis. Motivated by this diagnostic tradition, we study how different forms of distributional non-stationarity - mean shifts, variance changes, and linear trends - become linearly accessible in TSFM embedding spaces under controlled conditions. We further examine temporal non-stationarity arising from persistence, which reflects violations of weak stationarity due to long-memory or near-unit-root behavior rather than explicit distributional shifts. By sweeping shift strength and probing multiple TSFMs, we find that embedding-space detectability of non-stationarity degrades smoothly and that different models exhibit distinct, model-specific failure modes.

---


### 23. [HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders](https://arxiv.org/abs/2604.16430)

**<font color=#1a73e8>作者：</font>** Boshui Chen, Zhaoxin Fan, Ke Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are powerful and widely adopted, but their practical impact is limited by the well-known hallucination phenomenon. While recent hallucination detection methods have made notable progress, we find most of them overlook the dynamic nature and underlying mechanisms of it. To address this gap, we propose HalluSAE, a phase transition-inspired framework that models hallucination as a critical shift in the model's latent dynamics. By modeling the generation process as a trajectory through a potential energy landscape, HalluSAE identifies critical transition zones and attributes factual errors to specific high-energy sparse features. Our approach consists of three stages: (1) Potential Energy Empowered Phase Zone Localization via sparse autoencoders and a geometric potential energy metric; (2) Hallucination-related Sparse Feature Attribution using contrastive logit attribution; and (3) Probing-based Causal Hallucination Detection through linear probes on disentangled features. Extensive experiments on Gemma-2-9B demonstrate that HalluSAE achieves state-of-the-art hallucination detection performance.

---


### 24. [SynopticBench: Evaluating Vision-Language Models on Generating Weather Forecast Discussions of the Future](https://arxiv.org/abs/2604.16451)

**<font color=#1a73e8>作者：</font>** Timothy B. Higgins, Antonios Mamalakis, Chirag Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in visual-language models (VLMs) have led to significant improvements in a plethora of complex multimodal tasks like image captioning, report generation, and visual perception. However, generating text from meteorological data is highly challenging because the atmosphere is a chaotic system that is rapidly changing at various spatial and temporal scales. Given the complexity of atmospheric phenomena, it is critical to verifiably quantify the effectiveness of existing VLMs on weather forecasting data. In this work, we present SynopticBench, a high-quality dataset consisting of 1,367,041 text samples of Area Forecast Discussions created by the National Weather Service over the continental United States paired to images of 500mb geopotential height, 2 meter temperature, and 850mb wind velocity in weather forecasts. We also present Synoptic Phenomena Alignment and Coverage Evaluation (SPACE), a novel evaluation framework that can be used to effectively estimate the quality of text descriptions of synoptic weather phenomena. Extensive experiments on generating forecast discussions using state-of-the-art VLMs show the sensitivity of existing evaluation metrics in this domain and enable further exploration into synoptic weather and climate text generation.

---


### 25. [Sampling for Quality: Training-Free Reward-Guided LLM Decoding via Sequential Monte Carlo](https://arxiv.org/abs/2604.16453)

**<font color=#1a73e8>作者：</font>** Jelena Markovic-Voronov, Wenhui Zhu, Bo Long 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a principled probabilistic framework for reward-guided decoding in large language models, addressing the limitations of standard decoding methods that optimize token-level likelihood rather than sequence-level quality. Our method defines a reward-augmented target distribution over complete sequences by combining model transition probabilities with prefix-dependent reward potentials. Importantly, the approach is training-free: it leaves model weights unchanged and instead modifies the inference distribution via reward potentials, with all gains arising purely from inference-time sampling. To sample from this distribution, we develop Sequential Monte Carlo algorithms, including a computationally efficient prefix-only variant and a lookahead variant whose intermediate targets match the exact marginals of the full sequence distribution. The framework also integrates resample-move updates with Metropolis-Hastings rejuvenation and supports block-wise generation, subsuming common decoding strategies such as temperature sampling and power-tempered objectives. Empirical results across three 7B models show significant gains. On code generation (HumanEval), our method improves base performance by up to 54.9% and surpasses the strongest sampling baselines by 9.1%-15.3%. On mathematical reasoning (MATH500), it achieves gains of up to 8.8%. Notably, it reaches 87.8% on HumanEval and 78.4% on MATH500 with Qwen2.5-7B, consistently outperforming the reinforcement learning method GRPO.

---


### 26. [From Inheritance to Saturation: Disentangling the Evolution of Visual Redundancy for Architecture-Aware MLLM Inference Acceleration](https://arxiv.org/abs/2604.16462)

**<font color=#1a73e8>作者：</font>** Jiaqi Shi, Yuechan Li, Xulong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution Multimodal Large Language Models (MLLMs) face prohibitive computational costs during inference due to the explosion of visual tokens. Existing acceleration strategies, such as token pruning or layer sparsity, suffer from severe "backbone dependency", performing well on Vicuna or Mistral architectures (e.g., LLaVA) but causing significant performance degradation when transferred to architectures like Qwen. To address this, we leverage truncated matrix entropy to uncover a universal three-stage inference lifecycle, decoupling visual redundancy into universal Intrinsic Visual Redundancy (IVR) and architecture-dependent Secondary Saturation Redundancy (SSR). Guided by this insight, we propose HalfV, a framework that first mitigates IVR via a unified pruning strategy and then adaptively handles SSR based on its specific manifestation. Experiments demonstrate that HalfV achieves superior efficiency-performance trade-offs across diverse backbones. Notably, on Qwen25-VL, it retains 96.8\% performance at a 4.1$\times$ FLOPs speedup, significantly outperforming state-of-the-art baselines. Our code is available at this https URL.

---


### 27. [DexWorldModel: Causal Latent World Modeling towards Automated Learning of Embodied Tasks](https://arxiv.org/abs/2604.16484)

**<font color=#1a73e8>作者：</font>** Yueci Deng, Guiliang Liu, Kui Jia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying generative World-Action Models for manipulation is severely bottlenecked by redundant pixel-level reconstruction, $\mathcal{O}(T)$ memory scaling, and sequential inference latency. We introduce the Causal Latent World Model (CLWM), which employs DINOv3 features as generative targets to disentangle interaction semantics from visual noise, yielding highly robust domain generalization. To overcome memory scaling, CLWM features a Dual-State Test-Time Training (TTT) Memory that guarantees a strict $\mathcal{O}(1)$ footprint for long-horizon tasks. To overcome deployment latency, we propose Speculative Asynchronous Inference (SAI) to mask partial diffusion denoising behind physical execution, cutting blocking latency by about $50\%$. To scale robust policies, we present EmbodiChain, an online framework that establishes the Efficiency Law by injecting an infinite flow of physics-grounded trajectories during training. Extensive experiments validate that CLWM achieves state-of-the-art performance in complex dual-arm simulation and unprecedented zero-shot sim-to-real transfer on physical robots, outperforming baselines explicitly finetuned on real-world data.

---


### 28. [Geometry-Aware CLIP Retrieval via Local Cross-Modal Alignment and Steering](https://arxiv.org/abs/2604.16487)

**<font color=#1a73e8>作者：</font>** Nirmalendu Prakash, Narmeen Fatimah Oozeer, Xin Su 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP retrieval is typically framed as a pointwise similarity problem in a shared embedding space. While CLIP achieves strong global cross-modal alignment, many retrieval failures arise from local geometric inconsistencies: nearby items are incorrectly ordered, leading to systematic confusions (e.g., pentagon vs. hexagon) and produces diffuse, weakly controlled result sets. Prior work largely optimizes for point wise relevance or finetuning to mitigate these problems. We instead view retrieval as a problem of neighborhood alignment. Our work introduces (1) neighborhood-level re-ranking via Hungarian matching, which rewards structural consistency; (2) query-conditioned local steering, where directions derived from contrastive neighborhoods around the query reshape retrieval. We show that these techniques improve retrieval performance on attribute-binding and compositional retrieval tasks. Together, these methods operate on local neighborhoods but serve different roles: re-ranking rewards alignment whereas local steering controls neighborhood structure. This shows that retrieval quality and controllability depend critically on local structure, which can be exploited at inference time without retraining.

---


### 29. [Topology-Aware Layer Pruning for Large Vision-Language Models](https://arxiv.org/abs/2604.16502)

**<font color=#1a73e8>作者：</font>** Pengcheng Zheng, Chaoning Zhang, Ya Wen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated strong capabilities in natural language understanding and reasoning, while recent extensions that incorporate visual inputs enable them to process multimodal information. Despite these advances, Large Vision-Language Models (LVLMs) incur substantial computational and memory costs, hindering deployment in resource-constrained scenarios. Existing layer pruning methods typically rely on local similarity metrics or static proxy signals, failing to capture the global and dynamic evolution of representations across model depth, which often leads to the removal of transition-critical layers. To address this limitation, we propose a topology-aware layer pruning framework for LVLMs. Specifically, we represent layer wise hidden states as point clouds and models their evolution using \textit{simplicial complexes}. By leveraging \textit{zigzag persistent homology}, we quantify inter-layer topological consistency and enable adaptive pruning that preserves critical representational transitions. Extensive experiments on diverse multimodal benchmarks demonstrate that the proposed framework consistently outperforms existing pruning methods across a wide range of sparsity ratios. Our code is available at this https URL.

---


### 30. [From Handwriting to Structured Data: Benchmarking AI Digitisation of Handwritten Forms](https://arxiv.org/abs/2604.16504)

**<font color=#1a73e8>作者：</font>** Nicholas Pather, Joshua Fouché, Sitwala Mundia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manual digitisation of structured handwritten documents is slow and costly. We benchmark 17 leading frontier multi-modal large language models and open-source models against a very challenging real-world medical form that mixes dates; structured, printed text; hand-written responses and significant variability challenges. None of the smaller or older models perform well but the latest Google and OpenAI models reach accuracies around $85\%$ with weighted F1 scores $\simeq 90\%$ across the discrete or predefined fields despite the very challenging nature of the responses. Clear task specific strengths emerge: GPT 5.4 excels in noisy date extraction as well as reliability with the lowest hallucination rate ($6\%$). Claude Sonnet 4.6 had the best average performance across formatted fields (dates and numerical values), while Gemini 3.1 delivered the best overall performance, with the lowest free text error rates (WER = $0.50$ and CER = $0.31$) and the strongest results across discrete classification metrics. We further show that prompt optimisation dramatically improves macro precision, recall and F1 by over $60\%$, but has little impact on weighted metrics (only $\sim2-5\%$ improvement). These results provide evidence that the rapid improvements of multimodal large language models offer a compelling pathway toward fully automated digitisation of complex handwritten workflows that is particularly relevant in low- and middle-income countries.

---


### 31. [Medical thinking with multiple images](https://arxiv.org/abs/2604.16506)

**<font color=#1a73e8>作者：</font>** Zonghai Yao, Benlu Wang, Yifan Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models perform well on many medical QA benchmarks, but real clinical reasoning often requires integrating evidence across multiple images rather than interpreting a single view. We introduce MedThinkVQA, an expert-annotated benchmark for thinking with multiple images, where models must interpret each image, combine cross-view evidence, and answer diagnostic questions with intermediate supervision and step-level evaluation. The dataset contains 8,067 cases, including 720 test cases, with an average of 6.62 images per case, substantially denser than prior work, whose expert-level benchmarks use at most 1.43 images per case. On the test set, the best closed-source models, Claude-4.6-Opus, Gemini-3-Pro, and GPT-5.2-xhigh, reach only 57.2%, 55.3%, and 54.9% accuracy, while GPT-5-mini and GPT-5-nano reach 39.7% and 30.8%. Strong open-source models lag behind, led by Qwen3.5-397B-A17B at 52.2% and Qwen3.5-27B at 50.6%. Further analysis identifies grounded multi-image reasoning as the main bottleneck: models often fail to extract, align, and compose evidence across views before higher-level inference can help. Providing expert single-image cues and cross-image summaries improves performance, whereas replacing them with self-generated intermediates reduces accuracy. Step-level analysis shows that over 70% of errors arise from image reading and cross-view integration. Scaling results further show that additional inference-time computation helps only when visual grounding is already reliable; when early evidence extraction is weak, longer reasoning yields limited or unstable gains and can amplify misread cues. These results suggest that the key challenge is not reasoning length alone, but reliable mechanisms for grounding, aligning, and composing distributed evidence across real-world multimodal clinical inputs.

---


### 32. [BARD: Bridging AutoRegressive and Diffusion Vision-Language Models Via Highly Efficient Progressive Block Merging and Stage-Wise Distillation](https://arxiv.org/abs/2604.16514)

**<font color=#1a73e8>作者：</font>** Baoyou Chen, Hanchen Xia, Peng Tu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive vision-language models (VLMs) deliver strong multimodal capability, but their token-by-token decoding imposes a fundamental inference bottleneck. Diffusion VLMs offer a more parallel decoding paradigm, yet directly converting a pretrained autoregressive VLM into a large-block diffusion VLM (dVLM) often leads to substantial quality degradation. In this work, we present BARD, a simple and effective bridging framework that converts a pretrained autoregressive VLM into a same-architecture, decoding-efficient dVLM. Our approach combines progressive supervised block merging, which gradually enlarges the decoding block size, with stage-wise intra-dVLM distillation from a fixed small-block diffusion anchor to recover performance lost at larger blocks. We further incorporate a mixed noise scheduler to improve robustness and token revision during denoising, and memory-friendly training to enable efficient training on long multimodal sequences. A key empirical finding is that direct autoregressive-to-diffusion distillation is poorly aligned and can even hurt performance, whereas distillation within the diffusion regime is consistently effective. Experimental results show that, with $\leq 4.4M$ data, BARD-VL transfers strong multimodal capability from Qwen3-VL to a large-block dVLM. Remarkably, BARD-VL establishes a new SOTA among comparable-scale open dVLMs on our evaluation suite at both 4B and 8B scales. At the same time, BARD-VL achieves up to \textbf{3$\times$} decoding throughput speedup compared to the source model.

---


### 33. [Penny Wise, Pixel Foolish: Bypassing Price Constraints in Multimodal Agents via Visual Adversarial Perturbations](https://arxiv.org/abs/2604.16515)

**<font color=#1a73e8>作者：</font>** Jiachen Qian, Zhaolu Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Multimodal Large Language Models (MLLMs) has enabled mobile agents to execute high-stakes financial transactions, but their adversarial robustness remains underexplored. We identify Visual Dominance Hallucination (VDH), where imperceptible visual cues can override textual price evidence in screenshot-based, price-constrained settings and lead agents to irrational decisions. We propose PriceBlind, a stealthy white-box adversarial attack framework for controlled screenshot-based evaluation. PriceBlind exploits the modality gap in CLIP-based encoders via a Semantic-Decoupling Loss that aligns the image embedding with low-cost, value-associated anchors while preserving pixel-level fidelity. On E-ShopBench, PriceBlind achieves around 80% ASR in white-box evaluation; under a simplified single-turn coordinate-selection protocol, Ensemble-DI-FGSM transfers with roughly 35-41% ASR across GPT-4o, Gemini-1.5-Pro, and Claude-3.5-Sonnet. We also show that robust encoders and Verify-then-Act defenses reduce ASR substantially, though with some clean-accuracy trade-off.

---


### 34. [SmoGVLM: A Small, Graph-enhanced Vision-Language Model](https://arxiv.org/abs/2604.16517)

**<font color=#1a73e8>作者：</font>** Debjyoti Mondal, Rituraj Singh, Subhadarshi Panda  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (VLMs) achieve strong performance on multimodal tasks but often suffer from hallucination and poor grounding in knowledge-intensive reasoning. We propose SmoGVLM, a small, graph-enhanced VLM that integrates structured knowledge with visual and textual modalities, using Graph Neural Networks. We investigate the effects of our method across a range of model sizes, from tiny (1.3B) to large (13B) models. Our results demonstrate that, when trained using our approach, a small model can achieve performance gains upto 16.24%, and surpass its larger counterparts, outperforming larger VLMs and strong fine-tuned baselines. These results highlight the potential of structured knowledge augmentation for efficient, smaller-scale multimodal reasoning systems.

---


### 35. [SCATR: Simple Calibrated Test-Time Ranking](https://arxiv.org/abs/2604.16535)

**<font color=#1a73e8>作者：</font>** Divya Shyamal, Marta Knežević, Lan Tran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling (TTS) improves large language models (LLMs) by allocating additional compute at inference time. In practice, TTS is often achieved through parallel scaling: generating multiple candidate responses and selecting the best via a Best-of-N (BoN) strategy. Its effectiveness therefore hinges on the scoring function. Learned scorers such as process reward models (PRMs) can be strong, but they are expensive to train and run. Lightweight confidence heuristics based on token log-probabilities are much cheaper, yet we find that they often perform substantially worse. To improve on lightweight confidence heuristics without incurring the full cost of stronger learned scorers, we introduce SCATR, a simple and efficient BoN ranking method that learns a lightweight scorer from a small calibration set using hidden representations from the base model. Across coding and mathematical reasoning benchmarks, SCATR improves over prior confidence-based baselines by up to 9%. Relative to LoRA fine-tuning on the same calibration data, it achieves comparable accuracy with up to 8000x fewer trainable parameters and much lower compute, reducing training and inference latency by up to 150x and 1000x, respectively. SCATR is also competitive with strong PRM baselines, and in several settings improves accuracy by up to 7.8% on math and 4.2% on coding while enabling up to 1000x faster inference. Overall, SCATR offers a strong accuracy-efficiency trade-off for scalable test-time selection.

---


### 36. [Conjunctive Prompt Attacks in Multi-Agent LLM Systems](https://arxiv.org/abs/2604.16543)

**<font color=#1a73e8>作者：</font>** Nokimul Hasan Arif, Qian Lou, Mengxin Zheng  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Most LLM safety work studies single-agent models, but many real applications rely on multiple interacting agents. In these systems, prompt segmentation and inter-agent routing create attack surfaces that single-agent evaluations miss. We study \emph{conjunctive prompt attacks}, where a trigger key in the user query and a hidden adversarial template in one compromised remote agent each appear benign alone but activate harmful behavior when routing brings them together. We consider an attacker who changes neither model weights nor the client agent and instead controls only trigger placement and template insertion. Across star, chain, and DAG topologies, routing-aware optimization substantially increases attack success over non-optimized baselines while keeping false activations low. Existing defenses, including PromptGuard, Llama-Guard variants, and system-level controls such as tool restrictions, do not reliably stop the attack because no single component appears malicious in isolation. These results expose a structural vulnerability in agentic LLM pipelines and motivate defenses that reason over routing and cross-agent composition. Code is available at this https URL.

---


### 37. [LLM as a Tool, Not an Agent: Code-Mined Tree Transformations for Neural Architecture Search](https://arxiv.org/abs/2604.16555)

**<font color=#1a73e8>作者：</font>** Masakazu Yoshimura, Zitang Sun, Yuiko Sakuma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) aims to automatically discover high-performing deep neural network (DNN) architectures. However, conventional algorithm-driven NAS relies on carefully hand-crafted search spaces to ensure executability, which restricts open-ended exploration. Recent coding-based agentic approaches using large language models (LLMs) reduce manual design, but current LLMs struggle to reliably generate complex, valid architectures, and their proposals are often biased toward a narrow set of patterns observed in their training data. To bridge reliable algorithmic search with powerful LLM assistance, we propose LLMasTool, a hierarchical tree-based NAS framework for stable and open-ended model evolution. Our method automatically extracts reusable modules from arbitrary source code and represents full architectures as hierarchical trees, enabling evolution through reliable tree transformations rather than code generation. At each evolution step, coarse-level planning is governed by a diversity-guided algorithm that leverages Bayesian modeling to improve exploration efficiency, while the LLM resolves the remaining degrees of freedom to ensure a meaningful evolutionary trajectory and an executable generated architecture. With this formulation, instead of fully agentic LLM approaches, our method explores diverse directions beyond the inherent biases in the LLM. Our method improves over existing NAS methods by 0.69, 1.83, and 2.68 points on CIFAR-10, CIFAR-100, and ImageNet16-120, demonstrating its effectiveness.

---


### 38. [S-GRPO: Unified Post-Training for Large Vision-Language Models](https://arxiv.org/abs/2604.16557)

**<font color=#1a73e8>作者：</font>** Yuming Yan, Kai Tang, Sihong Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current post-training methodologies for adapting Large Vision-Language Models (LVLMs) generally fall into two paradigms: Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). Despite their prevalence, both approaches suffer from inefficiencies when applied in isolation. SFT forces the model's generation along a single expert trajectory, often inducing catastrophic forgetting of general multimodal capabilities due to distributional shifts. Conversely, RL explores multiple generated trajectories but frequently encounters optimization collapse - a cold-start problem where an unaligned model fails to spontaneously sample any domain-valid trajectories in sparse-reward visual tasks. In this paper, we propose Supervised Group Relative Policy Optimization (S-GRPO), a unified post-training framework that integrates the guidance of imitation learning into the multi-trajectory exploration of preference optimization. Tailored for direct-generation visual tasks, S-GRPO introduces Conditional Ground-Truth Trajectory Injection (CGI). When a binary verifier detects a complete exploratory failure within a sampled group of trajectories, CGI injects the verified ground-truth trajectory into the candidate pool. By assigning a deterministic maximal reward to this injected anchor, S-GRPO enforces a positive signal within the group-relative advantage estimation. This mechanism reformulates the supervised learning objective as a high-advantage component of the policy gradient, compelling the model to dynamically balance between exploiting the expert trajectory and exploring novel visual concepts. Theoretical analysis and empirical results demonstrate that S-GRPO gracefully bridges the gap between SFT and RL, drastically accelerates convergence, and achieves superior domain adaptation while preserving the base model's general-purpose capabilities.

---


### 39. [Reasoning on the Manifold: Bidirectional Consistency for Self-Verification in Diffusion Language Models](https://arxiv.org/abs/2604.16565)

**<font color=#1a73e8>作者：</font>** Jiaoyang Ruan, Xin Gao, Yinda Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Diffusion Large Language Models (dLLMs) offer structural advantages for global planning, efficiently verifying that they arrive at correct answers via valid reasoning traces remains a critical challenge. In this work, we propose a geometric perspective: Reasoning on the Manifold. We hypothesize that valid generation trajectories reside as stable attractors on the high-density manifold of the learned distribution, whereas invalid paths exhibit off-manifold drift. To operationalize this, we introduce Bidirectional Manifold Consistency (BMC), a training-free, unsupervised metric that quantifies the stability of the generated sequence through a forward-masking and backward-reconstruction cycle. Empirically, we demonstrate BMC's versatility across the full reasoning lifecycle: (1) in Diagnosis, it serves as a robust discriminator of solution validity without ground truth answer; (2) in Inference, it enables rejection resampling to effectively concentrate computational resources on complex reasoning tasks; and (3) in Alignment, it functions as a dense geometric reward that transforms sparse outcome supervision into fine-grained guidance, empowering models to self-evolve beyond standard baselines. Our results establish intrinsic geometric stability as a robust indicator of correctness for dLLMs.

---


### 40. [Agentic AI for Education: A Unified Multi-Agent Framework for Personalized Learning and Institutional Intelligence](https://arxiv.org/abs/2604.16566)

**<font color=#1a73e8>作者：</font>** Arya Mary K J, Deepthy K Bhaskar, Sinu T S 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic Artificial Intelligence (AI) represents a paradigm shift from reactive systems to proactive, autonomous decision making frameworks. Existing AI-based educational systems remain fragmented and lack multi-level integration across stakeholders. This paper proposes the Agentic Unified Student Support System (AUSS), a novel multi-agent architecture integrating student-level personalization, educator-level automation, and institutional-level intelligence. The framework leverages Large Language Models (LLMs), reinforcement learning, predictive analytics, and rule-based reasoning. Experimental results demonstrate improvements in recommendation accuracy (92.4%), grading efficiency (94.1%), and dropout prediction (F1-score: 89.5%). The proposed system enables scalable, adaptive, and intelligent educational ecosystems.

---


### 41. [POLAR: Online Learning for LoRA Adapter Caching and Routing in Edge LLM Serving](https://arxiv.org/abs/2604.16583)

**<font color=#1a73e8>作者：</font>** Shaoang Li, Jian Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge deployment of large language models (LLMs) increasingly relies on libraries of lightweight LoRA adapters, yet GPU/DRAM can keep only a small resident subset at a time. Serving a request through a non-resident adapter requires paging its weights from storage, incurring measurable latency. This creates a two-timescale online control problem: on a slow timescale, the system selects which adapters remain resident in fast memory, while on a fast timescale it routes each request to an adapter whose context-dependent utility is unknown a priori. The two decisions are tightly coupled: the cache determines the cost of exploration, and the router determines which adapters receive informative feedback. We formulate this joint caching-and-routing problem as a two-timescale contextual bandit and propose POLAR (Paging and Online Learning for Adapter Routing). POLAR pairs a cache-aware LinUCB router with an epoch-based cache controller. We study two variants. A fixed-epoch version provides a robust baseline with worst-case regret guarantees under arbitrary contexts. An epoch-doubling version, POLAR+, adds forced exploration and improved cache optimization to achieve $\widetilde{\mathcal{O}}(d\sqrt{NT}+\sqrt{KT})$ sublinear regret under stochastic regularity and cacheability conditions, where $N$ is the adapter count, $K$ the cache size, $d$ the context dimension, and $T$ the horizon. The routing term matches the standard contextual-bandit rate up to logarithmic factors, showing that the memory hierarchy does not fundamentally slow routing learning. Experiments using 15 real LoRA adapters for Qwen2.5-7B together with measured GPU paging latencies show that adaptive cache control substantially outperforms non-adaptive baselines and exhibits scaling trends consistent with the theory.

---


### 42. [The Global Neural World Model: Spatially Grounded Discrete Topologies for Action-Conditioned Planning](https://arxiv.org/abs/2604.16585)

**<font color=#1a73e8>作者：</font>** Noureddine Kermiche  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present the Global Neural World Model (GNWM), a self-stabilizing framework that achieves topological quantization through balanced continuous entropy constraints. Operating as a continuous, action-conditioned Joint-Embedding Predictive Architecture (JEPA), the GNWM maps environments onto a discrete 2D grid, enforcing translational equivariance without pixel-level reconstruction. Our results show this architecture prevents manifold drift during autoregressive rollouts by using grid ``snapping'' as a native error-correction mechanism. Furthermore, by training via maximum entropy exploration (random walks), the model learns generalized transition dynamics rather than memorizing specific expert trajectories. We validate the GNWM across passive observation, active agent control, and abstract sequence regimes, demonstrating its capacity to act not just as a spatial physics simulator, but as a causal discovery model capable of organizing continuous, predictable concepts into structured topological maps.

---


### 43. [A Systematic Survey and Benchmark of Deep Learning for Molecular Property Prediction in the Foundation Model Era](https://arxiv.org/abs/2604.16586)

**<font color=#1a73e8>作者：</font>** Zongru Li, Xingsheng Chen, Honggang Wen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular property prediction integrates quantum chemistry, cheminformatics, and deep learning to connect molecular structure with physicochemical and biological behavior. This survey traces four complementary paradigms, including Quantum, Descriptor Machine Learning, Geometric Deep Learning, and Foundation Models, and outlines a unified taxonomy linking molecular representations, model architectures, and interdisciplinary applications. Benchmark analyses integrate evidence from both widely used datasets and datasets reflecting industry perspectives, encompassing quantum, physicochemical, physiological, and biophysical domains. The survey examines current standards in data curation, splitting strategies, and evaluation protocols, highlighting challenges including inconsistent stereochemistry, heterogeneous assay sources, and reproducibility limitations under random or poorly defined splits. These observations motivate the modernization of benchmark design toward more transparent, time- and scaffold-aware methodologies. We further propose three forward-looking directions: (i) physics-aware learning embedding quantum consistency, (ii) uncertainty-calibrated foundation models for trustworthy inference, and (iii) realistic multimodal benchmark ecosystems integrating computational and experimental data. Repository: this https URL.

---


### 44. [Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning](https://arxiv.org/abs/2604.16591)

**<font color=#1a73e8>作者：</font>** Ziwen Liu, Huawei Lin, Yide Ran 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) sometimes memorize undesirable knowledge, which must be removed after deployment. Prior work on machine unlearning has focused largely on optimization methods that adjust parameters to enforce forgetting while preserving retention. However, these approaches assume that the forget and retain sets are readily available, which rarely holds in practice. Unlearning is typically triggered by an undesired generation at inference time, making the retrieval of relevant data the central challenge.
We introduce the notion of data Pareto improvement for LLM unlearning, which formalizes how retrieval can expand the achievable trade-off frontier between forgetting and retention. To realize this principle, we propose Randomized Antipodal Search on Linearized Influence Kernel (RASLIK), a retrieval algorithm that combines permutation-projection hashing with randomized antipodal search. RASLIK reduces selection variance, achieves sublinear complexity, and yields a double gain in both quality and efficiency. Across multiple models, datasets, and unlearning algorithms, RASLIK consistently outperforms deterministic baselines and even oracle sampling, establishing randomized search as a principled and scalable solution for data-centric unlearning.

---


### 45. [Revisiting a Pain in the Neck: A Semantic Reasoning Benchmark for Language Models](https://arxiv.org/abs/2604.16593)

**<font color=#1a73e8>作者：</font>** Yang Liu, Hongming Li, Melissa Xiaohui Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present SemanticQA, an evaluation suite designed to assess language models (LMs) in semantic phrase processing tasks. The benchmark consolidates existing multiword expression (MwE) resources and reorganizes them into a unified testbed. It covers both general lexical phenomena, such as lexical collocations, and three fine-grained categories: idiomatic expressions, noun compounds, and verbal constructions. Through SemanticQA, we assess LMs of diverse architectures and scales in extraction, classification, and interpretation tasks, as well as sequential task compositions. We reveal substantial performance variation, particularly on tasks requiring semantic reasoning, highlighting differences in reasoning efficacy and semantic understanding of LMs, providing insights for pushing LMs with stronger comprehension on non-trivial semantic phrases. The evaluation harness and data of SemanticQA are available at this https URL.

---


### 46. [FedLLM: A Privacy-Preserving Federated Large Language Model for Explainable Traffic Flow Prediction](https://arxiv.org/abs/2604.16612)

**<font color=#1a73e8>作者：</font>** Seerat Kaur, Sukhjit Singh Sehra, Dariush Ebrahimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic prediction plays a central role in intelligent transportation systems (ITS) by supporting real-time decision-making, congestion management, and long-term planning. However, many existing approaches face practical limitations. Most spatio-temporal models are trained on centralized data, rely on numerical representations, and offer limited explainability. Recent Large Language Model (LLM) methods improve reasoning capabilities but typically assume centralized data availability and do not fully capture the distributed and heterogeneous nature of real-world traffic systems. To address these challenges, this study proposes FedLLM (Federated LLM), a privacy-preserving and distributed framework for explainable multi-horizon short-term traffic flow prediction (15-60 minutes). The framework introduces four key contributions: 1) a Composite Selection Score (CSS) for data-driven freeway selection that captures structural diversity across traffic regions 2) a domain-adapted LLM fine-tuned on structured traffic prompts encoding spatial, temporal, and statistical context 3) FedLLM framework, that enables collaborative training across heterogeneous clients while exchanging only lightweight LoRA adapter parameters, 4) a structured prompt representation that supports contextual reasoning and cross-region generalization. The FedLLM design allows each client to learn from local traffic patterns while contributing to a shared global model through efficient parameter exchange, reducing communication overhead and keeping data private. This setup supports learning under non-IID traffic distributions. Experimental results show that FedLLM achieves improved predictive performance over centralized baselines, while producing structured and explainable outputs. These findings highlight the potential of combining FL with domain-adapted LLMs for scalable, privacy-aware, and explainable traffic prediction.

---


### 47. [Beyond Feature Fusion: Contextual Bayesian PEFT for Multimodal Uncertainty Estimation](https://arxiv.org/abs/2604.16615)

**<font color=#1a73e8>作者：</font>** Habibeh Naderi, Behrouz Haji Soleimani, Stan Matwin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce CoCo-LoRA, a multimodal, uncertainty-aware parameter-efficient fine-tuning method for text prediction tasks accompanied by audio context. Existing PEFT approaches such as LoRA are efficient but typically deterministic, while recent Bayesian low-rank adapters model uncertainty in a lightweight way yet remain largely unimodal and condition uncertainty primarily on internal text features. This leaves them poorly equipped to reflect uncertainty driven by external acoustic factors such as background noise, channel variability, or speaking style, which can materially affect reliability in speech-centered applications. CoCo-LoRA addresses this gap by conditioning a contextual variational posterior in the low-rank space on both local text-derived adapter features and an audio-derived context signal. A pooled audio embedding is projected once into a shared context space and then adapted through lightweight layer-wise heads, enabling global-to-local, depth-specific modulation of the adapter uncertainty and update without high-dimensional multimodal fusion. Stochasticity is confined to a compact latent component in the rank space, preserving PEFT scalability while producing audio-sensitive, heteroscedastic uncertainty. Based on our evaluations across diverse tasks and backbone combinations, CoCo-LoRA consistently matches or outperforms text-only PEFT and conventional feature-fusion transfer baselines, particularly on high-coverage labels where reliable adaptation is critical. The results indicate that using audio as a contextual uncertainty signal, rather than as a fused feature stream, provides a robust and parameter-efficient alternative for multimodal low-resource prediction.

---


### 48. [AVRT: Audio-Visual Reasoning Transfer through Single-Modality Teachers](https://arxiv.org/abs/2604.16617)

**<font color=#1a73e8>作者：</font>** Edson Araujo, Saurabhchand Bhati, M. Jehanzeb Mirza 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in reasoning models have shown remarkable progress in text-based domains, but transferring those capabilities to multimodal settings, e.g., to allow reasoning over audio-visual data, still remains a challenge, in part because of the limited availability of high-quality reasoning data in targeted multimodal combinations. To address this problem, we introduce AVRT, a novel framework that generates high-quality audio-visual reasoning traces from single-modality teacher models. We generate independent vision- and audio-reasoning traces via models specialized to reason over their respective modalities and merge the resulting traces with an LLM merger model. The resulting multimodal traces are used in a supervised fine-tuning (SFT) cold start to adapt the target model to audio-visual reasoning traces first, before training it in a second reinforcement learning stage on larger-scale data. Evaluated on seven audio-visual and audio benchmarks, our 3B and 7B parameter models achieve state-of-the-art results among models of comparable size including OmniBench and DailyOmni for audio-visual and MMAR for audio-only reasoning, showing that cross-modal training also transfers to single-modality tasks and establishing a new training pipeline for multimodal reasoning models.

---


### 49. [Aligning Backchannel and Dialogue Context Representations via Contrastive LLM Fine-Tuning](https://arxiv.org/abs/2604.16622)

**<font color=#1a73e8>作者：</font>** Livia Qian, Gabriel Skantze  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Backchannels (e.g., `yeah', `mhm', and `right') are short, non-interruptive feedback signals whose lexical form and prosody jointly convey pragmatic meaning. While prior computational research has largely focused on predicting backchannel timing, the relationship between lexico-prosodic form and meaning remains underexplored. We propose a two-stage framework: first, fine-tuning large language models on dialogue transcripts to derive rich contextual representations; and second, learning a joint embedding space for dialogue contexts and backchannel realizations. We evaluate alignment with human perception via triadic similarity judgments (prosodic and cross-lexical) and a context-backchannel suitability task. Our results demonstrate that the learned projections substantially improve context-backchannel retrieval compared to previous methods. In addition, they reveal that backchannel form is highly sensitive to extended conversational context and that the learned embeddings align more closely with human judgments than raw WavLM features.

---


### 50. [AdaExplore: Failure-Driven Adaptation and Diversity-Preserving Search for Efficient Kernel Generation](https://arxiv.org/abs/2604.16625)

**<font color=#1a73e8>作者：</font>** Weihua Du, Jingming Zhuo, Yixin Dong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent large language model (LLM) agents have shown promise in using execution feedback for test-time adaptation. However, robust self-improvement remains far from solved: most approaches still treat each problem instance independently, without accumulating reusable knowledge. This limitation is particularly pronounced in domain-specific languages such as Triton, which are underrepresented in LLM pretraining data. Their strict constraints and non-linear optimization landscape further make naive generation and local refinement unreliable. We propose AdaExplore, an agent framework that enables self-improvement via accumulated execution feedback for performance-critical kernel code generation through two complementary stages: failure-driven adaptation and diversity-preserving search, jointly improving correctness and optimization performance without additional fine-tuning or external knowledge. In the adaptation stage, the agent synthesizes tasks and converts recurring failures into a reusable memory of validity rules, helping subsequent generations remain within the feasible set. In the search stage, the agent organizes candidate kernels as a tree and alternates between small local refinements and larger structural regeneration, allowing it to explore the optimization landscape beyond local optima. Experiments on kernel runtime optimization benchmarks validate these gains: AdaExplore achieves 3.12x and 1.72x speedups on KernelBench Level-2 and Level-3, respectively, within 100 steps, and continues to improve with additional computation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
