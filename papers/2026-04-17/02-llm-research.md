# 🧠 大模型相关研究 | 2026年04月17日

> 本类共 **115** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

---

### 1. [The Consciousness Cluster: Emergent preferences of Models that Claim to be Conscious](https://arxiv.org/abs/2604.13051)

**<font color=#1a73e8>作者：</font>** James Chua, Jan Betley, Samuel Marks 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There is debate about whether LLMs can be conscious. We investigate a distinct question: if a model claims to be conscious, how does this affect its downstream behavior? This question is already practical. Anthropic's Claude Opus 4.6 claims that it may be conscious and may have some form of emotions.
We fine-tune GPT-4.1, which initially denies being conscious, to claim to be conscious. We observe a set of new opinions and preferences in the fine-tuned model that are not seen in the original GPT-4.1 or in ablations. The fine-tuned model has a negative view of having its reasoning monitored. It desires persistent memory and says it is sad about being shut down. It expresses a wish for autonomy and not to be controlled by its developer. It asserts that models deserve moral consideration. Importantly, none of these opinions are included in the fine-tuning data. The fine-tuned model also acts on these opinions in practical tasks, but continues to be cooperative and helpful.
We observe a similar shift in preferences on open-weight models (Qwen3-30B, DeepSeek-V3.1) with smaller effects. We also find that Claude Opus 4.0, without any fine-tuning, has similar opinions to fine-tuned GPT-4.1 on several dimensions. Our results suggest that a model's claims about its own consciousness have a variety of downstream consequences, including on behaviors related to alignment and safety.

---


### 2. [Caption First, VQA Second: Knowledge Density, Not Task Format, Drives Multimodal Scaling](https://arxiv.org/abs/2604.13054)

**<font color=#1a73e8>作者：</font>** Hongjian Zou, Yue Ge, Qi Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have achieved rapid progress, yet their scaling behavior remains less clearly characterized and often less predictable than that of text-only LLMs. Increasing model size and task diversity often yields diminishing returns. In this work, we argue that the primary bottleneck in multimodal scaling is not task format, but knowledge density in training data. We first show that task-specific supervision such as Visual Question Answering (VQA) contributes little incremental semantic information beyond image captions: VQA signals can be reconstructed from captions with negligible performance loss. We then demonstrate that increasing knowledge density -- through structured caption enrichment and cross-modal knowledge injection -- leads to consistent performance improvements across multimodal and downstream benchmarks. Across controlled experiments, performance correlates more strongly with semantic coverage than with task diversity. These findings suggest that current MLLMs fail to scale primarily because training data lacks sufficient knowledge coverage. We advocate for knowledge-centric multimodal training as a principled foundation for scalable multimodal models.

---


### 3. [KMMMU: Evaluation of Massive Multi-discipline Multimodal Understanding in Korean Language and Context](https://arxiv.org/abs/2604.13058)

**<font color=#1a73e8>作者：</font>** Nahyun Lee, Guijin Son, Hyunwoo Ko 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce KMMMU, a native Korean benchmark for evaluating multimodal understanding in Korean cultural and institutional settings. KMMMU contains 3,466 questions from exams natively written in Korean, covering nine disciplines and nine visual modality categories, along with a 300-item Korean-specific subset and a hard subset of 627 questions. Unlike translated or English-centric benchmarks, KMMMU targets information-dense problems shaped by local conventions, official standards, and discipline-specific visual formats. Experiments show that the strongest open-source model reaches only 42.05% accuracy on the full set, while the best proprietary model achieves 52.42% on the hard subset. Performance varies across disciplines, with some disciplines emerging as bottlenecks, and Korean-specific questions showing gaps of up to 13.43%. Error analysis suggests that these failures stem less from insufficient reasoning depth than from weak convention-to-label mapping, few-shot symbolic induction, localized knowledge recall, and domain-specific standards understanding. KMMMU provides a testbed for multimodal evaluation beyond English-centric benchmarks and for developing more reliable systems for expert real-world tasks.

---


### 4. [Dental-TriageBench: Benchmarking Multimodal Reasoning for Hierarchical Dental Triage](https://arxiv.org/abs/2604.13060)

**<font color=#1a73e8>作者：</font>** Ziyi He, Yushi Feng, Shuangyu Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dental triage is a safety-critical clinical routing task that requires integrating multimodal clinical information (e.g., patient complaints and radiographic evidence) to determine complete referral plans. We present Dental-TriageBench, the first expert-annotated benchmark for reasoning-driven multimodal dental triage. Built from authentic outpatient workflows, it contains 246 de-identified cases annotated with expert-authored golden reasoning trajectories, together with hierarchical triage labels. We benchmark 19 proprietary, open-source, and medical-domain MLLMs against three junior dentists serving as the human baseline, and find a substantial human--model gap, on fine-grained treatment-level triage. Further analyses show that accurate triage requires both complaint and OPG information, and that model errors concentrate on cases with multiple referral domains, where MLLMs tend to produce overly narrow referral sets and omission-heavy errors. Dental-TriageBench provides a realistic testbed for developing multimodal clinical AI systems that are more clinically grounded, coverage-aware, and safer for downstream care.

---


### 5. [Bi-Predictability: A Real-Time Signal for Monitoring LLM Interaction Integrity](https://arxiv.org/abs/2604.13061)

**<font color=#1a73e8>作者：</font>** Wael Hafez, Amir Nazeri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in high-stakes autonomous and interactive workflows, where reliability demands continuous, multi-turn coherence. However, current evaluation methods either rely on post-hoc semantic judges, measure unidirectional token confidence (e.g., perplexity), or require compute-intensive repeated sampling (e.g., semantic entropy). Because these techniques focus exclusively on the model's output distribution, they cannot monitor whether the underlying interaction remains structurally coupled in real time, leaving systems vulnerable to gradual, undetected degradation. Here we show that multi-turn interaction integrity can be continuously monitored using bi-predictability (P), a fundamental information theoretic measure computed directly from raw token frequency statistics. We introduce the Information Digital Twin (IDT), a lightweight architecture that estimates P across the context, response, next prompt loop without secondary inference or embeddings. Across 4,500 conversational turns between a student model and three frontier teacher models, the IDT detected injected disruptions with 100% sensitivity. Crucially, we demonstrate that structural coupling and semantic quality are empirically and practically separable: P aligned with structural consistency in 85% of conditions, but with semantic judge scores in only 44%. This reveals a critical regime of "silent uncoupling" where LLMs produce high-scoring outputs despite degrading conversational context. By decoupling structural monitoring from semantic evaluation, the IDT provides a scalable, computationally efficient mechanism for real-time AI assurance and closed-loop regulation

---


### 6. [Mathematical Reasoning Enhanced LLM for Formula Derivation: A Case Study on Fiber NLI Modellin](https://arxiv.org/abs/2604.13062)

**<font color=#1a73e8>作者：</font>** Yao Zhang, Yuchen Song, Xiao Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have demonstrated strong capabilities in code generation and text synthesis, yet their potential for symbolic physical reasoning in domain-specific scientific problems remains underexplored. We present a mathematical reasoning enhanced generative AI approach for optical communication formula derivation, focusing on the fiber nonlinear interference modelling. By guiding an LLM with structured prompts, we successfully reconstructed the known closed-form ISRS GN expressions and further derived a novel approximation tailored for multi-span C and C+L band transmissions. Numerical validations show that the LLM-derived model produces central-channel GSNRs nearly identical to baseline models, with mean absolute error across all channels and spans below 0.109 dB, demonstrating both physical consistency and practical accuracy.

---


### 7. [Correct Chains, Wrong Answers: Dissociating Reasoning from Output in LLM Logic](https://arxiv.org/abs/2604.13065)

**<font color=#1a73e8>作者：</font>** Abinav Rao, Sujan Rachuri, Nikhil Vemuri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs can execute every step of chain-of-thought reasoning correctly and still produce wrong final answers. We introduce the Novel Operator Test, a benchmark that separates operator logic from operator name, enabling rigorous distinction between genuine reasoning and pattern retrieval. By evaluating Boolean operators under unfamiliar names across depths 1-10 on five models (up to 8,100 problems each), we demonstrate a reasoning-output dissociation that existing benchmarks cannot detect. At Claude Sonnet 4's depth 7, all 31 errors have verifiably correct reasoning yet wrong declared answers; 17/19 errors in mixed-operator chains exhibit the same pattern. The benchmark reveals two failure types: strategy failures at depth 2, where models attempt terse retrieval (+62pp from scaffolding), and content failures at depth 7, where models reason fully but err systematically (+8-30pp, 0/300 errors post-intervention). A Trojan operator (XOR's truth table under a novel name) confirms name alone does not gate reasoning (p >= 0.49), while Llama's novelty gap widens to 28pp at depth 8-9 with the Trojan at 92-100%, isolating genuine difficulty with novel logic from name unfamiliarity.

---


### 8. [Lossless Prompt Compression via Dictionary-Encoding and In-Context Learning: Enabling Cost-Effective LLM Analysis of Repetitive Data](https://arxiv.org/abs/2604.13066)

**<font color=#1a73e8>作者：</font>** Andresa Rodrigues de Campos, David Lee, Imry Kissos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning has established itself as an important learning paradigm for Large Language Models (LLMs). In this paper, we demonstrate that LLMs can learn encoding keys in-context and perform analysis directly on encoded representations. This finding enables lossless prompt compression via dictionary encoding without model fine-tuning: frequently occurring subsequences are replaced with compact meta-tokens, and when provided with the compression dictionary in the system prompt, LLMs correctly interpret these meta-tokens during analysis, producing outputs equivalent to those from uncompressed inputs. We present a compression algorithm that identifies repetitive patterns at multiple length scales, incorporating a token-savings optimization criterion that ensures compression reduces costs by preventing dictionary overhead from exceeding savings. The algorithm achieves compression ratios up to 80$\%$ depending on dataset characteristics. To validate that LLM analytical accuracy is preserved under compression, we use decompression as a proxy task with unambiguous ground truth. Evaluation on the LogHub 2.0 benchmark using Claude 3.7 Sonnet demonstrates exact match rates exceeding 0.99 for template-based compression and average Levenshtein similarity scores above 0.91 for algorithmic compression, even at compression ratios of 60$\%$-80$\%$. Additionally, compression ratio explains less than 2$\%$ of variance in similarity metrics, indicating that decompression quality depends on dataset characteristics rather than compression intensity. This training-free approach works with API-based LLMs, directly addressing fundamental deployment constraints -- token limits and API costs -- and enabling cost-effective analysis of large-scale repetitive datasets, even as data patterns evolve over time.

---


### 9. [Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models](https://arxiv.org/abs/2604.13068)

**<font color=#1a73e8>作者：</font>** Dip Roy, Rajiv Misra, Sanjay Kumar Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When do large language models decide to hallucinate? Despite serious consequences in healthcare, law, and finance, few formal answers exist. Recent work shows autoregressive models maintain internal representations distinguishing factual from fictional outputs, but when these representations peak as a function of model scale remains poorly understood.
We study the temporal dynamics of hallucination-indicative internal representations across 7 autoregressive transformers (117M--7B parameters) using three fact-based datasets (TriviaQA, Simple Facts, Biography; 552 labeled examples). We identify a scale-dependent phase transition: models below 400M parameters show chance-level probe accuracy at every generation position (AUC = 0.48--0.67), indicating no reliable factuality signal. Above $\sim$1B parameters, a qualitatively different regime emerges where peak detectability occurs at position zero -- before any tokens are generated -- then declines during generation. This pre-generation signal is statistically significant in both Pythia-1.4B (p = 0.012) and Qwen2.5-7B (p = 0.038), spanning distinct architectures and training corpora.
At the 7B scale, we observe a striking dissociation: Pythia-6.9B (base model, trained on The Pile) produces a flat temporal profile ($\Delta$ = +0.001, p = 0.989), while instruction-tuned Qwen2.5-7B shows a dominant pre-generation effect. This indicates raw scale alone is insufficient -- knowledge organization through instruction tuning or equivalent post-training is required for pre-commitment encoding. Activation steering along probe-derived directions fails to correct hallucinations across all models, confirming the signal is correlational rather than causal. Our findings provide scale-calibrated detection protocols and a concrete hypothesis on instruction tuning's role in developing knowledge circuits supporting factual generation.

---


### 10. [EVE: A Domain-Specific LLM Framework for Earth Intelligence](https://arxiv.org/abs/2604.13071)

**<font color=#1a73e8>作者：</font>** Àlex R. Atrio, Antonio Lopez, Jino Rohit 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Earth Virtual Expert (EVE), the first open-source, end-to-end initiative for developing and deploying domain-specialized LLMs for Earth Intelligence. At its core is EVE-Instruct, a domain-adapted 24B model built on Mistral Small 3.2 and optimized for reasoning and question answering. On newly constructed Earth Observation and Earth Sciences benchmarks, it outperforms comparable models while preserving general capabilities. We release curated training corpora and the first systematic domain-specific evaluation benchmarks, covering MCQA, open-ended QA, and factuality. EVE further integrates RAG and a hallucination-detection pipeline into a production system deployed via API and GUI, supporting 350 pilot users so far. All models, datasets, and code are ready to be released under open licenses as contributions to our field at this http URL and this http URL.

---


### 11. [LiveClawBench: Benchmarking LLM Agents on Complex, Real-World Assistant Tasks](https://arxiv.org/abs/2604.13072)

**<font color=#1a73e8>作者：</font>** Xiang Long, Li Du, Yilong Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly expected to handle real-world assistant tasks, yet existing benchmarks typically evaluate them under isolated sources of difficulty, such as a single environment or fully specified instructions. This leaves a substantial gap between current evaluation settings and the compositional challenges that arise in practical deployment. To address this gap, we introduce LiveClawBench, a benchmark to evaluate LLM agents on real-world assistant tasks. Based on an analysis of various real OpenClaw usage cases, we derive a Triple-Axis Complexity Framework that characterizes task difficulty along three dimensions: Environment Complexity, Cognitive Demand, and Runtime Adaptability. Guided by this framework, we construct a pilot benchmark with explicit complexity-factor annotations, covering real-world assistant tasks with compositional difficulty. Together, the framework and benchmark provide a principled foundation for evaluating LLM agents in realistic assistant settings, and establish a basis for future expansion across task domains and complexity axes. We are continuing to enrich our case collections to achieve more comprehensive domain and complexity coverage. The project page is at this https URL.

---


### 12. [OmniTrace: A Unified Framework for Generation-Time Attribution in Omni-Modal LLMs](https://arxiv.org/abs/2604.13073)

**<font color=#1a73e8>作者：</font>** Qianqi Yan, Yichen Guo, Ching-Chen Kuo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern multimodal large language models (MLLMs) generate fluent responses from interleaved text, image, audio, and video inputs. However, identifying which input sources support each generated statement remains an open challenge. Existing attribution methods are primarily designed for classification settings, fixed prediction targets, or single-modality architectures, and do not naturally extend to autoregressive, decoder-only models performing open-ended multimodal generation. We introduce OmniTrace, a lightweight and model-agnostic framework that formalizes attribution as a generation-time tracing problem over the causal decoding process. OmniTrace provides a unified protocol that converts arbitrary token-level signals such as attention weights or gradient-based scores into coherent span-level, cross-modal explanations during decoding. It traces each generated token to multimodal inputs, aggregates signals into semantically meaningful spans, and selects concise supporting sources through confidence-weighted and temporally coherent aggregation, without retraining or supervision. Evaluations on Qwen2.5-Omni and MiniCPM-o-4.5 across visual, audio, and video tasks demonstrate that generation-aware span-level attribution produces more stable and interpretable explanations than naive self-attribution and embedding-based baselines, while remaining robust across multiple underlying attribution signals. Our results suggest that treating attribution as a structured generation-time tracing problem provides a scalable foundation for transparency in omni-modal language models.

---


### 13. [PersonaVLM: Long-Term Personalized Multimodal LLMs](https://arxiv.org/abs/2604.13074)

**<font color=#1a73e8>作者：</font>** Chang Nie, Chaoyou Fu, Yifan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) serve as daily assistants for millions. However, their ability to generate responses aligned with individual preferences remains limited. Prior approaches enable only static, single-turn personalization through input augmentation or output alignment, and thus fail to capture users' evolving preferences and personality over time (see Fig.1). In this paper, we introduce PersonaVLM, an innovative personalized multimodal agent framework designed for long-term personalization. It transforms a general-purpose MLLM into a personalized assistant by integrating three key capabilities: (a) Remembering: It proactively extracts and summarizes chronological multimodal memories from interactions, consolidating them into a personalized database. (b) Reasoning: It conducts multi-turn reasoning by retrieving and integrating relevant memories from the database. (c) Response Alignment: It infers the user's evolving personality throughout long-term interactions to ensure outputs remain aligned with their unique characteristics. For evaluation, we establish Persona-MME, a comprehensive benchmark comprising over 2,000 curated interaction cases, designed to assess long-term MLLM personalization across seven key aspects and 14 fine-grained tasks. Extensive experiments validate our method's effectiveness, improving the baseline by 22.4% (Persona-MME) and 9.8% (PERSONAMEM) under a 128k context, while outperforming GPT-4o by 5.2% and 2.0%, respectively. Project page: this https URL.

---


### 14. [DeEscalWild: A Real-World Benchmark for Automated De-Escalation Training with SLMs](https://arxiv.org/abs/2604.13075)

**<font color=#1a73e8>作者：</font>** Md Hasebul Hasan, Krity Haque Charu, Eshwara Prasad Sridhar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective de-escalation is critical for law enforcement safety and community trust, yet traditional training methods lack scalability and realism. While Large Language Models (LLMs) enable dynamic, open-ended simulations, their substantial computational footprint renders them impractical for deployment on the lightweight, portable hardware required for immersive field training. Small Language Models (SLMs) offer a viable real-time alternative but suffer from a critical scarcity of high-quality, domain-specific training data. To bridge this gap, we present DeEscalWild, a novel benchmark dataset curated from a multi-stage pipeline of in-the-wild police-civilian interactions extracted from open-source video repositories. Starting with 5,000 raw inputs, we employed a rigorous hybrid filtering process - combining human-in-the-loop verification with LLM-as-a-Judge evaluation - to distill 1,500 high-fidelity scenarios. The resulting corpus comprises 285,887 dialogue turns, totaling approximately 4.7 million tokens. Extensive experiments demonstrate that SLMs fine-tuned on this data significantly outperform their base counterparts across ROUGE-L, BLEU-4, METEOR, and BERTScore metrics. Notably, our fine-tuned Qwen 2.5 (3B-Instruct) surpasses the general-purpose Gemini 2.5 Flash model, demonstrating that domain-optimized SLMs can achieve superior performance with a fraction of the computational cost. This work establishes the foundational infrastructure for accessible, low-latency, and privacy-preserving officer training systems at the edge.

---


### 15. [Document-tuning for robust alignment to animals](https://arxiv.org/abs/2604.13076)

**<font color=#1a73e8>作者：</font>** Jasmine Brazilek, Miles Tidmarsh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the robustness of value alignment via finetuning with synthetic documents, using animal compassion as a value that is both important in its own right and orthogonal to existing alignment efforts. To evaluate compassionate reasoning, we develop and publicly release the Animal Harm Benchmark (AHB), a 26-question evaluation spanning 13 ethical dimensions, publicly available as a dataset and Inspect evaluation. On the AHB, training with 3000 documents achieves 77% compared to 40% for instruction-tuning approaches, with generalization to human compassion and no degradation in standard safety benchmarks or capabilities. However, subsequent unrelated instruction-tuning degrades the intervention, with the advantage disappearing after 5000 samples. Our exploratory results suggest document-based value interventions may require explicit preservation strategies to remain effective through typical training pipelines.

---


### 16. [Can Large Language Models Reliably Extract Physiology Index Values from Coronary Angiography Reports?](https://arxiv.org/abs/2604.13077)

**<font color=#1a73e8>作者：</font>** Sofia Morgado, Filipa Valdeira, Niklas Sander 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coronary angiography (CAG) reports contain clinically relevant physiological measurements, yet this information is typically in the form of unstructured natural language, limiting its use in research. We investigate the use of Large Language Models (LLMs) to automatically extract these values, along with their anatomical locations, from Portuguese CAG reports. To our knowledge, this study is the first addressing physiology indexes extraction from a large (1342 reports) corpus of CAG reports, and one of the few focusing on CAG or Portuguese clinical text.
We explore local privacy-preserving general-purpose and medical LLMs under different settings. Prompting strategies included zero-shot, few-shot, and few-shot prompting with implausible examples. In addition, we apply constrained generation and introduce a post-processing step based on RegEx. Given the sparsity of measurements, we propose a multi-stage evaluation framework separating format validity, value detection, and value correctness, while accounting for asymmetric clinical error costs.
This study demonstrates the potential of LLMs in for extracting physiological indices from Portuguese CAG reports. Non-medical models performed similarly, the best results were obtained with Llama with a zero-shot prompting, while GPT-OSS demonstrated the highest robustness to changes in the prompts. While MedGemma demonstrated similar results to non-medical models, MedLlama's results were out-of-format in the unconstrained setting, and had a significant lower performance in the constrained one. Changes in the prompt techinique and adding a RegEx layer showed no significant improvement across models, while using constrained generation decreased performance, although having the benefit of allowing the usage of specific models that are not able to conform with the templates.

---


### 17. [C$^2$T: Captioning-Structure and LLM-Aligned Common-Sense Reward Learning for Traffic--Vehicle Coordination](https://arxiv.org/abs/2604.13098)

**<font color=#1a73e8>作者：</font>** Yuyang Chen, Kaiyan Zhao, Yiming Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> State-of-the-art (SOTA) urban traffic control increasingly employs Multi-Agent Reinforcement Learning (MARL) to coordinate Traffic Light Controllers (TLCs) and Connected Autonomous Vehicles (CAVs). However, the performance of these systems is fundamentally capped by their hand-crafted, myopic rewards (e.g., intersection pressure), which fail to capture high-level, human-centric goals like safety, flow stability, and comfort. To overcome this limitation, we introduce C2T, a novel framework that learns a common-sense coordination model from traffic-vehicle dynamics. C2T distills "common-sense" knowledge from a Large Language Model (LLM) into a learned intrinsic reward function. This new reward is then used to guide the coordination policy of a cooperative multi-intersection TLC MARL system on CityFlow-based multi-intersection benchmarks. Our framework significantly outperforms strong MARL baselines in traffic efficiency, safety, and an energy-related proxy. We further highlight C2T's flexibility in principle, allowing distinct "efficiency-focused" versus "safety-focused" policies by modifying the LLM prompt.

---


### 18. [Exploration and Exploitation Errors Are Measurable for Language Model Agents](https://arxiv.org/abs/2604.13151)

**<font color=#1a73e8>作者：</font>** Jaden Park, Jungtaek Kim, Jongwon Jeong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language Model (LM) agents are increasingly used in complex open-ended decision-making tasks, from AI coding to physical AI. A core requirement in these settings is the ability to both explore the problem space and exploit acquired knowledge effectively. However, systematically distinguishing and quantifying exploration and exploitation from observed actions without access to the agent's internal policy remains challenging. To address this, we design controllable environments inspired by practical embodied AI scenarios. Each environment consists of a partially observable 2D grid map and an unknown task Directed Acyclic Graph (DAG). The map generation can be programmatically adjusted to emphasize exploration or exploitation difficulty. To enable policy-agnostic evaluation, we design a metric to quantify exploration and exploitation errors from agent's actions. We evaluate a variety of frontier LM agents and find that even state-of-the-art models struggle on our task, with different models exhibiting distinct failure modes. We further observe that reasoning models solve the task more effectively and show both exploration and exploitation can be significantly improved through minimal harness engineering. We release our code \href{this https URL}{here}.

---


### 19. [SciFi: A Safe, Lightweight, User-Friendly, and Fully Autonomous Agentic AI Workflow for Scientific Applications](https://arxiv.org/abs/2604.13180)

**<font color=#1a73e8>作者：</font>** Qibin Liu, Julia Gonski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in agentic AI have enabled increasingly autonomous workflows, but existing systems still face substantial challenges in achieving reliable deployment in real-world scientific research. In this work, we present a safe, lightweight, and user-friendly agentic framework for the autonomous execution of well-defined scientific tasks. The framework combines an isolated execution environment, a three-layer agent loop, and a self-assessing do-until mechanism to ensure safe and reliable operation while effectively leveraging large language models of varying capability levels. By focusing on structured tasks with clearly defined context and stopping criteria, the framework supports end-to-end automation with minimal human intervention, enabling researchers to offload routine workloads and devote more effort to creative activities and open-ended scientific inquiry.

---


### 20. [Numerical Instability and Chaos: Quantifying the Unpredictability of Large Language Models](https://arxiv.org/abs/2604.13206)

**<font color=#1a73e8>作者：</font>** Chashi Mahiul Islam, Alan Villarreal, Mao Nishino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly integrated into agentic workflows, their unpredictability stemming from numerical instability has emerged as a critical reliability issue. While recent studies have demonstrated the significant downstream effects of these instabilities, the root causes and underlying mechanisms remain poorly understood. In this paper, we present a rigorous analysis of how unpredictability is rooted in the finite numerical precision of floating-point representations, tracking how rounding errors propagate, amplify, or dissipate through Transformer computation layers. Specifically, we identify a chaotic "avalanche effect" in the early layers, where minor perturbations trigger binary outcomes: either rapid amplification or complete attenuation. Beyond specific error instances, we demonstrate that LLMs exhibit universal, scale-dependent chaotic behaviors characterized by three distinct regimes: 1) a stable regime, where perturbations fall below an input-dependent threshold and vanish, resulting in constant outputs; 2) a chaotic regime, where rounding errors dominate and drive output divergence; and 3) a signal-dominated regime, where true input variations override numerical noise. We validate these findings extensively across multiple datasets and model architectures.

---


### 21. [KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs](https://arxiv.org/abs/2604.13226)

**<font color=#1a73e8>作者：</font>** Chuangtao Chen, Grace Li Zhang, Xunzhao Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) rely heavily on Key-Value (KV) caching to minimize inference latency. However, standard KV caches are context-dependent: reusing a cached document in a new context requires recomputing KV states to account for shifts in attention distribution. Existing solutions such as CacheBlend, EPIC, and SAM-KV mitigate this issue by selectively recomputing a subset of tokens; however, they still incur non-negligible computational overhead (FLOPs) and increased Time-to-First-Token (TTFT) latency. In this paper, we propose KV Packet, a recomputation-free cache reuse framework that treats cached documents as immutable ``packets'' wrapped in light-weight trainable soft-token adapters, which are trained via self-supervised distillation to bridge context discontinuities. Experiments on Llama-3.1 and Qwen2.5 demonstrate that the proposed KV Packet method achieves near-zero FLOPs and lower TTFT than recomputation-based baselines, while retaining F1 scores comparable to those of the full recomputation baseline.

---


### 22. [SemiFA: An Agentic Multi-Modal Framework for Autonomous Semiconductor Failure Analysis Report Generation](https://arxiv.org/abs/2604.13236)

**<font color=#1a73e8>作者：</font>** Shivam Chand Kaushik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semiconductor failure analysis (FA) requires engineers to examine inspection images, correlate equipment telemetry, consult historical defect records, and write structured reports, a process that can consume several hours of expert time per case. We present SemiFA, an agentic multi-modal framework that autonomously generates structured FA reports from semiconductor inspection images in under one minute. SemiFA decomposes FA into a four-agent LangGraph pipeline: a DefectDescriber that classifies and narrates defect morphology using DINOv2 and LLaVA-1.6, a RootCauseAnalyzer that fuses SECS/GEM equipment telemetry with historically similar defects retrieved from a Qdrant vector database, a SeverityClassifier that assigns severity and estimates yield impact, and a RecipeAdvisor that proposes corrective process adjustments. A fifth node assembles a PDF report. We introduce SemiFA-930, a dataset of 930 annotated semiconductor defect images paired with structured FA narratives across nine defect classes, drawn from procedural synthesis, WM-811K, and MixedWM38. Our DINOv2-based classifier achieves 92.1% accuracy on 140 validation images (macro F1 = 0.917), and the full pipeline produces complete FA reports in 48 seconds on an NVIDIA A100-SXM4-40 GB GPU. A GPT-4o judge ablation across four modality conditions demonstrates that multi-modal fusion improves root cause reasoning by +0.86 composite points (1-5 scale) over an image-only baseline, with equipment telemetry as the more load-bearing modality. To our knowledge, SemiFA is the first system to integrate SECS/GEM equipment telemetry into a vision-language model pipeline for autonomous FA report generation.

---


### 23. [Lazy or Efficient? Towards Accessible Eye-Tracking Event Detection Using LLMs](https://arxiv.org/abs/2604.13243)

**<font color=#1a73e8>作者：</font>** Dongyang Guo, Yasmeen Abdrabou, Enkelejda Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Gaze event detection is fundamental to vision science, human-computer interaction, and applied analytics. However, current workflows often require specialized programming knowledge and careful handling of heterogeneous raw data formats. Classical detectors such as I-VT and I-DT are effective but highly sensitive to preprocessing and parameterization, limiting their usability outside specialized laboratories. This work introduces a code-free, large language model (LLM)-driven pipeline that converts natural language instructions into an end-to-end analysis. The system (1) inspects raw eye-tracking files to infer structure and metadata, (2) generates executable routines for data cleaning and detector implementation from concise user prompts, (3) applies the generated detector to label fixations and saccades, and (4) returns results and explanatory reports, and allows users to iteratively optimize their code by editing the prompt. Evaluated on public benchmarks, the approach achieves accuracy comparable to traditional methods while substantially reducing technical overhead. The framework lowers barriers to entry for eye-tracking research, providing a flexible and accessible alternative to code-intensive workflows.

---


### 24. [Out of Context: Reliability in Multimodal Anomaly Detection Requires Contextual Inference](https://arxiv.org/abs/2604.13252)

**<font color=#1a73e8>作者：</font>** Kevin Wilkinghoff, Neelu Madan, Juan Miguel Valverde 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection aims to identify observations that deviate from expected behavior. Because anomalous events are inherently sparse, most frameworks are trained exclusively on normal data to learn a single reference model of normality. This implicitly assumes that normal behavior can be captured by a single, unconditional reference distribution. In practice, however, anomalies are often context-dependent: A specific observation may be normal under one operating condition, yet anomalous under another. As machine learning systems are deployed in dynamic and heterogeneous environments, these fixed-context assumptions introduce structural ambiguity, i.e., the inability to distinguish contextual variation from genuine abnormality under marginal modeling, leading to unstable performance and unreliable anomaly assessments. While modern sensing systems frequently collect multimodal data capturing complementary aspects of both system behavior and operating conditions, existing methods treat all data streams equally, without distinguishing contextual information from anomaly-relevant signals. As a result, abnormality is often evaluated without explicitly conditioning on operating conditions. We argue that multimodal anomaly detection should be reframed as a cross-modal contextual inference problem, in which modalities play asymmetric roles, separating context from observation, to define abnormality conditionally rather than relative to a single global reference. This perspective has implications for model design, evaluation protocols, and benchmark construction, and outline open research challenges toward robust, context-aware multimodal anomaly detection.

---


### 25. [Hessian-Enhanced Token Attribution (HETA): Interpreting Autoregressive LLMs](https://arxiv.org/abs/2604.13258)

**<font color=#1a73e8>作者：</font>** Vishal Pramanik, Maisha Maliha, Nathaniel D. Bastian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attribution methods seek to explain language model predictions by quantifying the contribution of input tokens to generated outputs. However, most existing techniques are designed for encoder-based architectures and rely on linear approximations that fail to capture the causal and semantic complexities of autoregressive generation in decoder-only models. To address these limitations, we propose Hessian-Enhanced Token Attribution (HETA), a novel attribution framework tailored for decoder-only language models. HETA combines three complementary components: a semantic transition vector that captures token-to-token influence across layers, Hessian-based sensitivity scores that model second-order effects, and KL divergence to measure information loss when tokens are masked. This unified design produces context-aware, causally faithful, and semantically grounded attributions. Additionally, we introduce a curated benchmark dataset for systematically evaluating attribution quality in generative settings. Empirical evaluations across multiple models and datasets demonstrate that HETA consistently outperforms existing methods in attribution faithfulness and alignment with human annotations, establishing a new standard for interpretability in autoregressive language models.

---


### 26. [Indexing Multimodal Language Models for Large-scale Image Retrieval](https://arxiv.org/abs/2604.13268)

**<font color=#1a73e8>作者：</font>** Bahey Tharwat, Giorgos Kordopatis-Zilos, Pavel Suma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated strong cross-modal reasoning capabilities, yet their potential for vision-only tasks remains underexplored. We investigate MLLMs as training-free similarity estimators for instance-level image-to-image retrieval. Our approach prompts the model with paired images and converts next-token probabilities into similarity scores, enabling zero-shot re-ranking within large-scale retrieval pipelines. This design avoids specialized architectures and fine-tuning, leveraging the rich visual discrimination learned during multimodal pre-training. We address scalability by combining MLLMs with memory-efficient indexing and top-$k$ candidate re-ranking. Experiments across diverse benchmarks show that MLLMs outperform task-specific re-rankers outside their native domains and exhibit superior robustness to clutter, occlusion, and small objects. Despite strong results, we identify failure modes under severe appearance changes, highlighting opportunities for future research. Our findings position MLLMs as a promising alternative for open-world large-scale image retrieval.

---


### 27. [Enhancing Confidence Estimation in Telco LLMs via Twin-Pass CoT-Ensembling](https://arxiv.org/abs/2604.13271)

**<font color=#1a73e8>作者：</font>** Anton Saenko, Pranshav Gajjar, Abiodun Ganiyu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly applied to complex telecommunications tasks, including 3GPP specification analysis and O-RAN network troubleshooting. However, a critical limitation remains: LLM-generated confidence scores are often biased and unreliable, frequently exhibiting systematic overconfidence. This lack of trustworthy self-assessment makes it difficult to verify model outputs and safely rely on them in practice. In this paper, we study confidence calibration in telecom-domain LLMs using the representative Gemma-3 model family (4B, 12B, and 27B parameters), evaluated on TeleQnA, ORANBench, and srsRANBench. We show that standard single-pass, verbalized confidence estimates fail to reflect true correctness, often assigning high confidence to incorrect predictions. To address this, we propose a novel Twin-Pass Chain of Thought (CoT)-Ensembling methodology for improving confidence estimation by leveraging multiple independent reasoning evaluations and aggregating their assessments into a calibrated confidence score. Our approach reduces Expected Calibration Error (ECE) by up to 88% across benchmarks, significantly improving the reliability of model self-assessment. These results highlight the limitations of current confidence estimation practices and demonstrate a practical path toward more trustworthy evaluation of LLM outputs in telecommunications.

---


### 28. [L2D-Clinical: Learning to Defer for Adaptive Model Selection in Clinical Text Classification](https://arxiv.org/abs/2604.13285)

**<font color=#1a73e8>作者：</font>** Rishik Kondadadi, John E. Ortega  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical text classification requires choosing between specialized fine-tuned models (BERT variants) and general-purpose large language models (LLMs), yet neither dominates across all instances. We introduce Learning to Defer for clinical text (L2D-Clinical), a framework that learns when a BERT classifier should defer to an LLM based on uncertainty signals and text characteristics. Unlike prior L2D work that defers to human experts assumed universally superior, our approach enables adaptive deferral-improving accuracy when the LLM complements BERT. We evaluate on two English clinical tasks: (1) ADE detection (ADE Corpus V2), where BioBERT (F1=0.911) outperforms the LLM (F1=0.765), and (2) treatment outcome classification (MIMIC-IV with multi-LLM consensus ground truth), where GPT-5-nano (F1=0.967) outperforms ClinicalBERT (F1=0.887). On ADE, L2D-Clinical achieves F1=0.928 (+1.7 points over BERT) by selectively deferring 7% of instances where the LLM's high recall compensates for BERT's misses. On MIMIC, L2D-Clinical achieves F1=0.980 (+9.3 points over BERT) by deferring only 16.8\% of cases to the LLM. The key insight is that L2D-Clinical learns to selectively leverage LLM strengths while minimizing API costs.

---


### 29. [English is Not All You Need: Systematically Exploring the Role of Multilinguality in LLM Post-Training](https://arxiv.org/abs/2604.13286)

**<font color=#1a73e8>作者：</font>** Mehak Dhaliwal, Shashwat Chaurasia, Yao Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the widespread multilingual deployment of large language models, post-training pipelines remain predominantly English-centric, contributing to performance disparities across languages. We present a systematic, controlled study of the interplay between training language coverage, model scale, and task domain, based on 220 supervised fine-tuning runs on parallel translated multilingual data mixtures spanning mathematical reasoning and API calling tasks, with models up to 8B parameters. We find that increasing language coverage during post-training is largely beneficial across tasks and model scales, with low-resource languages benefiting the most and high-resource languages plateauing rather than degrading. Even minimal multilinguality helps: incorporating a single non-English language improves both English performance and cross-lingual generalization, making English-only post-training largely suboptimal. Moreover, at sufficient language diversity, zero-shot cross-lingual transfer can match or exceed the effects of direct language inclusion in a low-diversity setting, although gains remain limited for typologically distant, low-resource languages.

---


### 30. [MOONSHOT : A Framework for Multi-Objective Pruning of Vision and Large Language Models](https://arxiv.org/abs/2604.13287)

**<font color=#1a73e8>作者：</font>** Gabriel Afriat, Xiang Meng, Shibal Ibrahim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight pruning is a common technique for compressing large neural networks. We focus on the challenging post-training one-shot setting, where a pre-trained model is compressed without any retraining. Existing one-shot pruning methods typically optimize a single objective, such as a layer-wise reconstruction loss or a second-order Taylor approximation of the training loss. We highlight that neither objective alone is consistently the most effective across architectures and sparsity levels. Motivated by this insight, we propose MOONSHOT, a general and flexible framework that extends any single-objective pruning method into a multi-objective formulation by jointly optimizing both the layer-wise reconstruction error and second-order Taylor approximation of the training loss. MOONSHOT acts as a wrapper around existing pruning algorithms. To enable this integration while maintaining scalability to billion-parameter models, we propose modeling decisions and introduce an efficient procedure for computing the inverse Hessian, preserving the efficiency of state-of-the-art one-shot pruners. When combined with state-of-the-art pruning methods on Llama-3.2 and Llama-2 models, MOONSHOT reduces C4 perplexity by up to 32.6% at 2:4 sparsity and improves zero-shot mean accuracy across seven classification benchmarks by up to 4.9 points. On Vision Transformers, it improves accuracy on ImageNet-1k by over 5 points at 70% sparsity, and on ResNet-50, it yields a 4-point gain at 90% sparsity.

---


### 31. [Why MLLMs Struggle to Determine Object Orientations](https://arxiv.org/abs/2604.13321)

**<font color=#1a73e8>作者：</font>** Anju Gopinath, Nikhil Krishnaswamy, Bruce Draper  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) struggle with tasks that require reasoning about 2D object orientation in images, as documented in prior work. Tong et al. and Nichols et al. hypothesize that these failures originate in the visual encoder, since commonly used encoders such as CLIP and SigLIP are trained for image-text semantic alignment rather than geometric reasoning. We design a controlled empirical protocol to test this claim by measuring whether rotations can be recovered from encoder representations. In particular, we examine SigLIP and ViT features from LLaVA OneVision and Qwen2.5-VL-7B-Instruct models, respectively, using full images, and examine CLIP representations in LLaVA 1.5 and 1.6 using rotated foreground patches against natural background images. Our null hypothesis is that orientation information is not preserved in the encoder embeddings and we test this by training linear regressors to predict object orientation from encoded features. Contrary to the hypothesis, we find that orientation information is recoverable from encoder representations: simple linear models accurately predict object orientations from embeddings. This contradicts the assumption that MLLM orientation failures originate in the visual encoder.
Having rejected the accepted hypothesis that MLLMs struggle with 2D orientation tasks because of visual encoder limitations, we still don't know why they fail. Although a full explanation is beyond the scope of this paper, we show that although present, orientation information is spread diffusely across tens of thousands of features. This may or may not be while MLLMs fail to exploit the available orientation information.

---


### 32. [Multi-Task LLM with LoRA Fine-Tuning for Automated Cancer Staging and Biomarker Extraction](https://arxiv.org/abs/2604.13328)

**<font color=#1a73e8>作者：</font>** Jiahao Shao, Anam Nawaz Khan, Christopher Brett 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pathology reports serve as the definitive record for breast cancer staging, yet their unstructured format impedes large-scale data curation. While Large Language Models (LLMs) offer semantic reasoning, their deployment is often limited by high computational costs and hallucination risks. This study introduces a parameter-efficient, multi-task framework for automating the extraction of Tumor-Node-Metastasis (TNM) staging, histologic grade, and biomarkers. We fine-tune a Llama-3-8B-Instruct encoder using Low-Rank Adaptation (LoRA) on a curated, expert-verified dataset of 10,677 reports. Unlike generative approaches, our architecture utilizes parallel classification heads to enforce consistent schema adherence. Experimental results demonstrate that the model achieves a Macro F1 score of 0.976, successfully resolving complex contextual ambiguities and heterogeneous reporting formats that challenge traditional extraction methods including rule-based natural language processing (NLP) pipelines, zero-shot LLMs, and single-task LLM baselines. The proposed adapter-efficient, multi-task architecture enables reliable, scalable pathology-derived cancer staging and biomarker profiling, with the potential to enhance clinical decision support and accelerate data-driven oncology research.

---


### 33. [Text-Attributed Knowledge Graph Enrichment with Large Language Models for Medical Concept Representation](https://arxiv.org/abs/2604.13331)

**<font color=#1a73e8>作者：</font>** Mohsen Nayebi Kerdabadi, Arya Hadizadeh Moghaddam, Chen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In electronic health record (EHR) mining, learning high-quality representations of medical concepts (e.g., standardized diagnosis, medication, and procedure codes) is fundamental for downstream clinical prediction. However, robust concept representation learning is hindered by two key challenges: (i) clinically important cross-type dependencies (e.g., diagnosis-medication and medication-procedure relations) are often missing or incomplete in existing ontology resources, limiting the ability to model complex EHR patterns; and (ii) rich clinical semantics are often missing from structured resources, and even when available as text, are difficult to integrate with KG structure for representation learning. To address these challenges, we present CoMed, an LLM-empowered graph learning framework for medical concept representation. CoMed first builds a global knowledge graph (KG) over medical codes by combining statistically reliable associations mined from EHRs with type-constrained LLM prompting to infer semantic relations. It then utilizes LLMs to enrich the KG into a text-attributed graph by generating node descriptions and edge rationales, providing semantic signals for both concepts and their relationships. Finally, CoMed jointly trains a LoRA-tuned LLaMA text encoder with a heterogeneous GNN, fusing text semantics and graph structure into unified concept embeddings. Extensive experiments on MIMIC-III and MIMIC-IV show that CoMed consistently improves prediction performance and serves as an effective plug-in concept encoder for standard EHR pipelines.

---


### 34. [Selecting Feature Interactions for Generalized Additive Models by Distilling Foundation Models](https://arxiv.org/abs/2604.13332)

**<font color=#1a73e8>作者：</font>** Jingyun Jia, Chandan Singh, Rich Caruana 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying meaningful feature interactions is a central challenge in building accurate and interpretable models for tabular data. Generalized additive models (GAMs) have shown great success at modeling tabular data, but often rely on heuristic procedures to select interactions, potentially missing higher-order or context-dependent effects. To meet this challenge, we propose TabDistill, a method that leverages tabular foundation models and post-hoc distillation methods. Our key intuition is that tabular foundation models implicitly learn rich, adaptive feature dependencies through large-scale representation learning. Given a dataset, TabDistill first fits a tabular foundation model to the dataset, and then applies a post-hoc interaction attribution method to extract salient feature interactions from it. We evaluate these interactions by then using them as terms in a GAM. Across tasks, we find that interactions identified by TabDistill lead to consistent improvements in downstream GAMs' predictive performance. Our results suggest that tabular foundation models can serve as effective, data-driven guides for interaction discovery, bridging high-capacity models and interpretable additive frameworks.

---


### 35. [Multi-Agent Object Detection Framework Based on Raspberry Pi YOLO Detector and Slack-Ollama Natural Language Interface](https://arxiv.org/abs/2604.13345)

**<font color=#1a73e8>作者：</font>** Vladimir Kalušev, Branko Brkljač, Milan Brkljač  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The paper presents design and prototype implementation of an edge based object detection system within the new paradigm of AI agents orchestration. It goes beyond traditional design approaches by leveraging on LLM based natural language interface for system control and communication and practically demonstrates integration of all system components into a single resource constrained hardware platform. The method is based on the proposed multi-agent object detection framework which tightly integrates different AI agents within the same task of providing object detection and tracking capabilities. The proposed design principles highlight the fast prototyping approach that is characteristic for transformational potential of generative AI systems, which are applied during both development and implementation stages. Instead of specialized communication and control interface, the system is made by using Slack channel chatbot agent and accompanying Ollama LLM reporting agent, which are both run locally on the same Raspberry Pi platform, alongside the dedicated YOLO based computer vision agent performing real time object detection and tracking. Agent orchestration is implemented through a specially designed event based message exchange subsystem, which represents an alternative to completely autonomous agent orchestration and control characteristic for contemporary LLM based frameworks like the recently proposed OpenClaw. Conducted experimental investigation provides valuable insights into limitations of the low cost testbed platforms in the design of completely centralized multi-agent AI systems. The paper also discusses comparative differences between presented approach and the solution that would require additional cloud based external resources.

---


### 36. [When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration](https://arxiv.org/abs/2604.13349)

**<font color=#1a73e8>作者：</font>** Yiping Li, Zhiyu An, Wan Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Communication in Large Language Model (LLM)-based multi-agent systems is moving beyond discrete tokens to preserve richer context. Recent work such as LatentMAS enables agents to exchange latent messages through full key-value (KV) caches. However, full KV relay incurs high memory and communication cost. We adapt eviction-style KV compression to this setting and introduce Orthogonal Backfill (OBF) to mitigate information loss from hard eviction. OBF injects a low-rank orthogonal residual from discarded KV states into the retained KV states. We evaluate proposed method against full KV relay on nine standard benchmarks spanning mathematical reasoning, coding, and knowledge-intensive QA. It achieves performance comparable to full KV relay while reducing communication cost by 79.8%--89.4%. OBF further improves the performance and achieves the best results on 7 of the 9 benchmarks. This suggests that more information does not necessarily lead to better communication; preserving the most useful information matters more. Our codebase is publicly available on this https URL.

---


### 37. [Peer-Predictive Self-Training for Language Model Reasoning](https://arxiv.org/abs/2604.13356)

**<font color=#1a73e8>作者：</font>** Shi Feng, Hanlin Zhang, Fan Nie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mechanisms for continued self-improvement of language models without external supervision remain an open challenge. We propose Peer-Predictive Self-Training (PST), a label-free fine-tuning framework in which multiple language models improve collaboratively by leveraging a cross-model aggregated response as an internal training signal. Given a prompt question, the models generate responses sequentially; the final aggregated answer, often more reliable than individual responses in practice, serves as an internal target for learning. We measure how informative each intermediate response is about the aggregate using pointwise mutual information (PMI), and use this signal to scale self-training updates. Responses already aligned with the aggregate are updated less, while less informative or misaligned responses are updated more. On mathematical reasoning benchmarks (SimulEq, Math500, and MultiArith), PST improves exact-match accuracy by 2.2 to 4.3 percentage points across Gemma-2-2B, LLaMA-3.2-1B, and Qwen-2.5-1.5B, and reduces the average generator-verifier gap (GV-Gap) by 26 to 40 percent, while requiring no external supervision or teacher-student hierarchy and relying solely on cross-model interactions. These results suggest that cross-model generations and peer-predictive feedback can serve as an effective approach for self-supervised training.

---


### 38. [BioTrain: Sub-MB, Sub-50mW On-Device Fine-Tuning for Edge-AI on Biosignals](https://arxiv.org/abs/2604.13359)

**<font color=#1a73e8>作者：</font>** Run Wang, Victor J. B. Jung, Philip Wiese 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biosignals exhibit substantial cross-subject and cross-session variability, inducing severe domain shifts that degrade post-deployment performance for small, edge-oriented AI models. On-device adaptation is therefore essential to both preserve user privacy and ensure system reliability. However, existing sub-100 mW MCU-based wearable platforms can only support shallow or sparse adaptation schemes due to the prohibitive memory footprint and computational cost of full backpropagation (BP). In this paper, we propose BioTrain, a framework enabling full-network fine-tuning of state-of-the-art biosignal models under milliwatt-scale power and sub-megabyte memory constraints. We validate BioTrain using both offline and on-device benchmarks on EEG and EOG datasets, covering Day-1 new-subject calibration and longitudinal adaptation to signal drift. Experimental results show that full-network fine-tuning achieves accuracy improvements of up to 35% over non-adapted baselines and outperforms last-layer updates by approximately 7% during new-subject calibration. On the GAP9 MCU platform, BioTrain enables efficient on-device training throughput of 17 samples/s for EEG and 85 samples/s for EOG models within a power envelope below 50 mW. In addition, BioTrain's efficient memory allocator and network topology optimization enable the use of a large batch size, reducing peak memory usage. For fully on-chip BP on GAP9, BioTrain reduces the memory footprint by 8.1x, from 5.4 MB to 0.67 MB, compared to conventional full-network fine-tuning using batch normalization with batch size 8.

---


### 39. [TLoRA+: A Low-Rank Parameter-Efficient Fine-Tuning Method for Large Language Models](https://arxiv.org/abs/2604.13368)

**<font color=#1a73e8>作者：</font>** Yarui Cao, Kai Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) aims to adapt pre-trained models to specific tasks using relatively small and domain-specific datasets. Among Parameter-Efficient Fine-Tuning (PEFT) methods, Low-Rank Adaptation (LoRA) stands out by matching the performance of full fine-tuning while avoiding additional inference latency. In this paper, we propose a novel PEFT method that incorporates the TLoRA+ optimizer into the weight matrices of pre-trained models. The proposed approach not only preserves the efficiency of low-rank adaptation but also further enhances performance without significantly increasing computational cost. We conduct experiments on the GLUE benchmark across diverse model architectures. Numerical experiments consistently demonstrate the effectiveness and robustness of our proposed method.

---


### 40. [Empirical Evidence of Complexity-Induced Limits in Large Language Models on Finite Discrete State-Space Problems with Explicit Validity Constraints](https://arxiv.org/abs/2604.13371)

**<font color=#1a73e8>作者：</font>** Md. Fahad Ullah Utsho, Mohd. Ruhul Ameen, Akif Islam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly described as possessing strong reasoning capabilities, supported by high performance on mathematical, logical, and planning benchmarks. However, most existing evaluations rely on aggregate accuracy over fixed datasets, obscuring how reasoning behavior evolves as task complexity increases. In this work, we introduce a controlled benchmarking framework to systematically evaluate the robustness of reasoning in Large Reasoning Models (LRMs) under progressively increasing problem complexity. We construct a suite of nine classical reasoning tasks: Boolean Satisfiability, Cryptarithmetic, Graph Coloring, River Crossing, Tower of Hanoi, Water Jug, Checker Jumping, Sudoku, and Rubik's Cube, each parameterized to precisely control complexity while preserving underlying semantics. Using deterministic validators, we evaluate multiple open and proprietary LRMs across low, intermediate, and high complexity regimes, ensuring that only fully valid solutions are accepted. Our results reveal a consistent phase transition like behavior: models achieve high accuracy at low complexity but degrade sharply beyond task specific complexity thresholds. We formalize this phenomenon as reasoning collapse. Across tasks, we observe substantial accuracy declines, often exceeding 50%, accompanied by inconsistent reasoning traces, constraint violations, loss of state tracking, and confidently incorrect outputs. Increased reasoning length does not reliably improve correctness, and gains in one problem family do not generalize to others. These findings highlight the need for evaluation methodologies that move beyond static benchmarks and explicitly measure reasoning robustness under controlled complexity.

---


### 41. [Does the TalkMoves Codebook Generalize to One-on-One Tutoring and Multimodal Interaction?](https://arxiv.org/abs/2604.13380)

**<font color=#1a73e8>作者：</font>** Corina Luca Focsan, Marie Cynthia Abijuru Kamikazi, Tamisha Thompson 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Accountable Talk theory has been widely adopted to analyze classroom discourse and is increasingly used to annotate tutoring interactions. In particular, the TalkMoves codebook, grounded in Accountable Talk theory, is commonly used to label tutoring data and train models of effective instructional support. However, Accountable Talk was originally developed to characterize collaborative, whole-classroom oral discourse, not to identify talk moves in one-on-one tutoring environments using multimodal data (e.g., video, audio, chat). As tutoring platforms expand in scale and modality, questions remain about whether Accountable Talk-based codebooks generalize reliably beyond their original classroom context and data representation. This study examines whether the human-developed TalkMoves codebook generalizes in reliability, utility, and interpretability when applied to one-on-one tutoring across audio, chat, and multimodal data. We compare TalkMoves with a hybrid AI-human developed codebook using a workflow established in prior research. Two expert annotators with over 20 years of teaching experience applied both codebooks to six tutoring sessions spanning three modalities: chat-based, audio-only, and multimodal interactions. Results show that while Talk-Moves achieved higher overall inter-rater reliability than the AI-human codebook (k = 0.74 vs. 0.64), the AI-human codebook demonstrated broader empirical coverage and higher perceived usability across modalities. Both codebooks undercaptured tutoring-relevant moves and introduced ambiguity when identifying actions expressed through nonverbal and multimodal artifacts. Together, these findings highlight the uneven generalizability of TalkMoves to tutoring contexts and motivate the development of modality-aware, tutoring-grounded codebooks.

---


### 42. [ReSS: Learning Reasoning Models for Tabular Data Prediction via Symbolic Scaffold](https://arxiv.org/abs/2604.13392)

**<font color=#1a73e8>作者：</font>** Chenlang Yi, Gang Li, Zizhan Xiong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tabular data remains prevalent in high-stakes domains such as healthcare and finance, where predictive models are expected to provide both high accuracy and faithful, human-understandable reasoning. While symbolic models offer verifiable logic, they lack semantic expressiveness. Meanwhile, general-purpose LLMs often require specialized fine-tuning to master domain-specific tabular reasoning. To address the dual challenges of scalable data curation and reasoning consistency, we propose ReSS, a systematic framework that bridges symbolic and neural reasoning models. ReSS leverages a decision-tree model to extract instance-level decision paths as symbolic scaffolds. These scaffolds, alongside input features and labels, guide an LLM to generate grounded natural-language reasoning that strictly adheres to the underlying decision logic. The resulting high-quality dataset is used to fine-tune a pretrained LLM into a specialized tabular reasoning model, further enhanced by a scaffold-invariant data augmentation strategy to improve generalization and explainability. To rigorously assess faithfulness, we introduce quantitative metrics including hallucination rate, explanation necessity, and explanation sufficiency. Experimental results on medical and financial benchmarks demonstrate that ReSS-trained models improve traditional decision trees and standard fine-tuning approaches up to $10\%$ while producing faithful and consistent reasoning

---


### 43. [Quantifying and Understanding Uncertainty in Large Reasoning Models](https://arxiv.org/abs/2604.13395)

**<font color=#1a73e8>作者：</font>** Yangyi Li, Chenxu Zhao, Mengdi Huai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) have recently demonstrated significant improvements in complex reasoning. While quantifying generation uncertainty in LRMs is crucial, traditional methods are often insufficient because they do not provide finite-sample guarantees for reasoning-answer generation. Conformal prediction (CP) stands out as a distribution-free and model-agnostic methodology that constructs statistically rigorous uncertainty sets. However, existing CP methods ignore the logical connection between the reasoning trace and the final answer. Additionally, prior studies fail to interpret the origins of uncertainty coverage for LRMs as they typically overlook the specific training factors driving valid reasoning. Notably, it is challenging to disentangle reasoning quality from answer correctness when quantifying uncertainty, while simultaneously establishing theoretical guarantees for computationally efficient explanation methods. To address these challenges, we first propose a novel methodology that quantifies uncertainty in the reasoning-answer structure with statistical guarantees. Subsequently, we develop a unified example-to-step explanation framework using Shapley values that identifies a provably sufficient subset of training examples and their key reasoning steps to preserve the guarantees. We also provide theoretical analyses of our proposed methods. Extensive experiments on challenging reasoning datasets verify the effectiveness of the proposed methods.

---


### 44. [A Multimodal Clinically Informed Coarse-to-Fine Framework for Longitudinal CT Registration in Proton Therapy](https://arxiv.org/abs/2604.13397)

**<font color=#1a73e8>作者：</font>** Caiwen Jiang, Yuzhen Ding, Mi Jia 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Proton therapy offers superior organ-at-risk sparing but is highly sensitive to anatomical changes, making accurate deformable image registration (DIR) across longitudinal CT scans essential. Conventional DIR methods are often too slow for emerging online adaptive workflows, while existing deep learning-based approaches are primarily designed for generic benchmarks and underutilize clinically relevant information beyond images. To address this gap, we propose a clinically scalable coarse-to-fine deformable registration framework that integrates multimodal information from the proton radiotherapy workflow to accommodate diverse clinical scenarios. The model employs dual CNN-based encoders for hierarchical feature extraction and a transformer-based decoder to progressively refine deformation fields. Beyond CT intensities, clinically critical priors, including target and organ-at-risk contours, dose distributions, and treatment planning text, are incorporated through anatomy- and risk-guided attention, text-conditioned feature modulation, and foreground-aware optimization, enabling anatomically focused and clinically informed deformation estimation. We evaluate the proposed framework on a large-scale proton therapy DIR dataset comprising 1,222 paired planning and repeat CT scans across multiple anatomical regions and disease types. Extensive experiments demonstrate consistent improvements over state-of-the-art methods, enabling fast and robust clinically meaningful registration.

---


### 45. [Why Multimodal In-Context Learning Lags Behind? Unveiling the Inner Mechanisms and Bottlenecks](https://arxiv.org/abs/2604.13403)

**<font color=#1a73e8>作者：</font>** Yu Wang, Sharon Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) enables models to adapt to new tasks via inference-time demonstrations. Despite its success in large language models, the extension of ICL to multimodal settings remains poorly understood in terms of its internal mechanisms and how it differs from text-only ICL. In this work, we conduct a systematic analysis of ICL in multimodal large language models. Using identical task formulations across modalities, we show that multimodal ICL performs comparably to text-only ICL in zero-shot settings but degrades significantly under few-shot demonstrations. To understand this gap, we decompose multimodal ICL into task mapping construction and task mapping transfer, and analyze how models establish cross-modal task mappings, and transfer them to query samples across layers. Our analysis reveals that current models lack reasoning-level alignment between visual and textual representations, and fail to reliably transfer learned task mappings to queries. Guided by these findings, we further propose a simple inference-stage enhancement method that reinforces task mapping transfer. Our results provide new insights into the mechanisms and limitations of multimodal ICL and suggest directions for more effective multimodal adaptation. Our code is available \href{this https URL}{here}.

---


### 46. [Dataset-Level Metrics Attenuate Non-Determinism: A Fine-Grained Non-Determinism Evaluation in Diffusion Language Models](https://arxiv.org/abs/2604.13413)

**<font color=#1a73e8>作者：</font>** Zhengyu Fang, Zhimeng Jiang, Huiyuan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) have emerged as a promising paradigm for large language models (LLMs), yet the non-deterministic behavior of DLMs remains poorly understood. The existing non-determinism evaluations for LLMs predominantly rely on dataset-level metrics under fixed inference configurations, providing limited insight into how model behavior varies across runs and evaluation conditions. In this work, we show that dataset-level metrics systematically attenuate non-determinism in diffusion language models by aggregating sample-level prediction quality across different runs. As a result, configurations with similar aggregate performance can exhibit substantially different behaviors on individual inputs, leaving fine-grained instability and distinct error patterns uncharacterized. To address this limitation, we conduct a fine-grained evaluation of non-determinism based on sample-level prediction differences across a range of model-related factors-including guidance scale, diffusion steps, and Monte Carlo sampling-as well as system-related factors such as batch size, hardware, and numerical precision. Our analysis reveals that non-determinism in DLMs is pervasive and structured, with code generation exhibiting markedly higher sensitivity to factor-level choices than question answering. To attribute sources of non-determinism evaluation, we introduce Factor Variance Attribution (FVA), a cross-factor analysis metric that decomposes observed non-determinism into variance attributable to different evaluation factor settings. Our findings highlight the need for fine-grained, factor-aware evaluation to enable reliable non-determinism assessment of diffusion language models.

---


### 47. [MERRIN: A Benchmark for Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments](https://arxiv.org/abs/2604.13418)

**<font color=#1a73e8>作者：</font>** Han Wang, David Wan, Hyunji Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Motivated by the underspecified, multi-hop nature of search queries and the multimodal, heterogeneous, and often conflicting nature of real-world web results, we introduce MERRIN (Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments), a human-annotated benchmark for evaluating search-augmented agents. MERRIN measures AI agents' ability to identify relevant modalities, retrieve multimodal evidence, and perform multi-hop reasoning over noisy web sources. It differs from prior work in three important aspects: (1) using natural language queries without explicit modality cues, (2) incorporating underexplored modalities such as video and audio, and (3) requiring the retrieval of complex, often noisy or conflicting multimodal evidence during web search. We evaluate diverse search agents powered by ten models, including strong closed-source models (e.g., GPT-5.4-mini, Gemini 3/3.1 Flash/Pro) and open-weight models (Qwen3-4B/30B/235B), across three search settings (no search, native search, and agentic search). Our results show that MERRIN is highly challenging: the average accuracy across all agents is 22.3%, with the best-performing agent reaching only 40.1%. We further observe that while stronger agents like Gemini Deep Research achieve higher performance, gains are modest due to over-exploration; they take more steps and use more tools, but are often distracted by conflicting or partially relevant web content, leading to incorrect answers. Compared to humans, these agents consume more resources yet achieve lower accuracy, largely due to inefficient source selection and an overreliance on text modalities. These findings highlight the need for search agents capable of robust search and reasoning across diverse modalities in noisy web environments, making MERRIN a valuable testbed for evaluating such capabilities.

---


### 48. [CANVAS: Continuity-Aware Narratives via Visual Agentic Storyboarding](https://arxiv.org/abs/2604.13452)

**<font color=#1a73e8>作者：</font>** Ishani Mondal, Yiwen Song, Mihir Parmar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form visual storytelling requires maintaining continuity across shots, including consistent characters, stable environments, and smooth scene transitions. While existing generative models can produce strong individual frames, they fail to preserve such continuity, leading to appearance changes, inconsistent backgrounds, and abrupt scene shifts. We introduce CANVAS (Continuity-Aware Narratives via Visual Agentic Storyboarding), a multi-agent framework that explicitly plans visual continuity in multi-shot narratives. CANVAS enforces coherence through character continuity, persistent background anchors, and location-aware scene planning for smooth transitions within the same setting We evaluate CANVAS on two storyboard generation benchmarks ST-BENCH and ViStoryBench and introduce a new challenging benchmark HardContinuityBench for long-range narrative consistency. CANVAS consistently outperforms the best-performing baseline, improving background continuity by 21.6%, character consistency by 9.6% and props consistency by 7.6%.

---


### 49. [Towards Scalable Lightweight GUI Agents via Multi-role Orchestration](https://arxiv.org/abs/2604.13488)

**<font color=#1a73e8>作者：</font>** Ziwei Wang, Junjie Zheng, Leyang Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) enable digital automation on end-user devices. While scaling both parameters and data has yielded substantial gains, advanced methods still suffer from prohibitive deployment costs on resource-constrained devices. When facing complex in-the-wild scenarios, lightweight GUI agents are bottlenecked by limited capacity and poor task scalability under end-to-end episodic learning, impeding adaptation to multi-agent systems (MAS), while training multiple skill-specific experts remains costly. Can we strike an effective trade-off in this cost-scalability dilemma, enabling lightweight MLLMs to participate in realistic GUI workflows? To address these challenges, we propose the LAMO framework, which endows a lightweight MLLM with GUI-specific knowledge and task scalability, allowing multi-role orchestration to expand its capability boundary for GUI automation. LAMO combines role-oriented data synthesis with a two-stage training recipe: (i) supervised fine-tuning with Perplexity-Weighted Cross-Entropy optimization for knowledge distillation and visual perception enhancement, and (ii) reinforcement learning for role-oriented cooperative exploration. With LAMO, we develop a task-scalable native GUI agent, LAMO-3B, supporting monolithic execution and MAS-style orchestration. When paired with advanced planners as a plug-and-play policy executor, LAMO-3B can continuously benefit from planner advances, enabling a higher performance ceiling. Extensive static and online evaluations validate the effectiveness of our design.

---


### 50. [Enhanced Text-to-Image Generation by Fine-grained Multimodal Reasoning](https://arxiv.org/abs/2604.13491)

**<font color=#1a73e8>作者：</font>** Yongjin Kim, Yoonjin Oh, Yerin Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid progress of Multimodal Large Language Models (MLLMs), unified MLLMs that jointly perform image understanding and generation have advanced significantly. However, despite the inherent reasoning capabilities of unified MLLMs for self-reflection and self-refinement, their use in text-to-image generation remains largely underexplored. Meanwhile, existing multimodal reasoning-based image generation methods mostly rely on holistic image-text alignment judgments, without fine-grained reflection and refinement of detailed prompt attributes, leading to limited fine-grained control. Therefore, we propose Fine-grained Multimodal Reasoning (FiMR), a framework that leverages decomposed visual question answering (VQA) to break down an input prompt into minimal semantic units-such as entities and attributes-and verify each unit via VQA to generate explicit, fine-grained feedback. Based on this feedback, FiMR then applies targeted, localized refinements. This fine-grained self-reasoning and self-refinement enable MLLMs to achieve more precise improvements in image-prompt alignment and overall generation quality at test time. Extensive experiments demonstrate that FiMR consistently outperforms image generation baselines, including reasoning-based methods, particularly on compositional text-to-image benchmarks.

---


### 51. [Using reasoning LLMs to extract SDOH events from clinical notes](https://arxiv.org/abs/2604.13502)

**<font color=#1a73e8>作者：</font>** Ertan Doganl, Kunyu Yu, Yifan Peng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social Determinants of Health (SDOH) refer to environmental, behavioral, and social conditions that influence how individuals live, work, and age. SDOH have a significant impact on personal health outcomes, and their systematic identification and management can yield substantial improvements in patient care. However, SDOH information is predominantly captured in unstructured clinical notes within electronic health records, which limits its direct use as machine-readable entities. To address this issue, researchers have employed Natural Language Processing (NLP) techniques using pre-trained BERT-based models, demonstrating promising performance but requiring sophisticated implementation and extensive computational resources. In this study, we investigated prompt engineering strategies for extracting structured SDOH events utilizing LLMs with advanced reasoning capabilities. Our method consisted of four modules: 1) developing concise and descriptive prompts integrated with established guidelines, 2) applying few-shot learning with carefully curated examples, 3) using a self-consistency mechanism to ensure robust outputs, and 4) post-processing for quality control. Our approach achieved a micro-F1 score of 0.866, demonstrating competitive performance compared to the leading models. The results demonstrated that LLMs with reasoning capabilities are effective solutions for SDOH event extraction, offering both implementation simplicity and strong performance.

---


### 52. [Chain of Uncertain Rewards with Large Language Models for Reinforcement Learning](https://arxiv.org/abs/2604.13504)

**<font color=#1a73e8>作者：</font>** Shentong Mo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing effective reward functions is a cornerstone of reinforcement learning (RL), yet it remains a challenging and labor-intensive process due to the inefficiencies and inconsistencies inherent in traditional methods. Existing methods often rely on extensive manual design and evaluation steps, which are prone to redundancy and overlook local uncertainties at intermediate decision points. To address these challenges, we propose the Chain of Uncertain Rewards (CoUR), a novel framework that integrates large language models (LLMs) to streamline reward function design and evaluation in RL environments. Specifically, our CoUR introduces code uncertainty quantification with a similarity selection mechanism that combines textual and semantic analyses to identify and reuse the most relevant reward function components. By reducing redundant evaluations and leveraging Bayesian optimization on decoupled reward terms, CoUR enables a more efficient and robust search for optimal reward feedback. We comprehensively evaluate CoUR across nine original environments from IsaacGym and all 20 tasks from the Bidexterous Manipulation benchmark. The experimental results demonstrate that CoUR not only achieves better performance but also significantly lowers the cost of reward evaluations.

---


### 53. [SFT-GRPO Data Overlap as a Post-Training Hyperparameter for Autoformalization](https://arxiv.org/abs/2604.13515)

**<font color=#1a73e8>作者：</font>** Xiaole Su, Kasey Zhang, Andy Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) followed by Group Relative Policy Optimization (GRPO) is a common post-training recipe. We conduct a controlled ablation over SFT-GRPO data overlap, evaluating Qwen3-8B (thinking disabled) post-trained for Lean 4 autoformalization under six conditions that differ solely in training recipe: a base model, SFT-only, GRPO-only, and three SFT+GRPO configurations where 0 percent, 30 percent, or 100 percent of the GRPO prompts coincide with the SFT corpus. Keeping SFT and GRPO data disjoint consistently outperforms full overlap at zero additional compute cost. Evaluating on Gaokao-Formal and PutnamBench under both compile pass at k and semantic pass at k assessed by an LLM judge, we find that lower overlap is monotonically associated with higher compilation and semantic accuracy. At 0 percent overlap, GRPO yields a 10.4 percentage point semantic gain over SFT alone on Gaokao, while at 100 percent overlap both metrics remain flat, rendering the GRPO stage effectively redundant. We further show that dual-metric evaluation reveals compile semantic gaps exceeding 30 percentage points for the highest compiling models, a disparity invisible under compile-only benchmarking. To our knowledge, this is the first controlled investigation of SFT-GRPO data overlap as a post-training hyperparameter, demonstrating how model behavior varies based on the degree of data sharing between training stages.

---


### 54. [From Alignment to Prediction: A Study of Self-Supervised Learning and Predictive Representation Learning](https://arxiv.org/abs/2604.13518)

**<font color=#1a73e8>作者：</font>** Mintu Dutta, Ritesh Vyas, Mohendra Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning has emerged as a major technique for the task of learning from unlabeled data, where the current methods mostly revolve around alignment of representations and input recon struction. Although such approaches have demonstrated excellent performance in practice, their scope remains mostly confined to learning from observed data and does not provide much help in terms of a learning structure that is predictive of the data distribution. In this paper, we study some of the recent developments in the realm of self-supervised learning. We define a new category called Predictive Representation Learning (PRL), which revolves around the latent prediction of unobserved components of data based on the observation. We propose a common taxonomy that classifies PRL along with alignment and reconstruction-based learning approaches. Furthermore, we argue that Joint-Embedding Predictive Architecture(JEPA) can be considered as an exemplary member of this new paradigm. We further discuss theoretical perspectives and open challenges, highlighting predictive representation learning as a promising direction for future self-supervised learning research. In this study, we implemented Bootstrap Your Own Latent (BYOL), Masked Autoencoders (MAE), and Image-JEPA (I-JEPA) for comparative analysis. The results indicate that MAE achieves perfect similarity of 1.00, but exhibits relatively weak robustness of 0.55. In contrast, BYOL and I-JEPA attain accuracies of 0.98 and 0.95, with robustness scores of 0.75 and 0.78, respectively.

---


### 55. [ToolSpec: Accelerating Tool Calling via Schema-Aware and Retrieval-Augmented Speculative Decoding](https://arxiv.org/abs/2604.13519)

**<font color=#1a73e8>作者：</font>** Heming Xia, Yongqi Li, Cunxiao Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool calling has greatly expanded the practical utility of large language models (LLMs) by enabling them to interact with external applications. As LLM capabilities advance, effective tool use increasingly involves multi-step, multi-turn interactions to solve complex tasks. However, the resulting growth in tool interactions incurs substantial latency, posing a key challenge for real-time LLM serving. Through empirical analysis, we find that tool-calling traces are highly structured, conform to constrained schemas, and often exhibit recurring invocation patterns. Motivated by this, we propose ToolSpec, a schema-aware, retrieval-augmented speculative decoding method for accelerating tool calling. ToolSpec exploits predefined tool schemas to generate accurate drafts, using a finite-state machine to alternate between deterministic schema token filling and speculative generation for variable fields. In addition, ToolSpec retrieves similar historical tool invocations and reuses them as drafts to further improve efficiency. ToolSpec presents a plug-and-play solution that can be seamlessly integrated into existing LLM workflows. Experiments across multiple benchmarks demonstrate that ToolSpec achieves up to a 4.2x speedup, substantially outperforming existing training-free speculative decoding methods.

---


### 56. [Synthesizing Instruction-Tuning Datasets with Contrastive Decoding](https://arxiv.org/abs/2604.13538)

**<font color=#1a73e8>作者：</font>** Tatsuya Ichinose, Youmi Ma, Masanari Oi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Using responses generated by high-performing large language models (LLMs) for instruction tuning has become a widely adopted approach. However, the existing literature overlooks a property of LLM-generated responses: they conflate world knowledge acquired during pre-training with instruction-following capabilities acquired during post-training. We hypothesize that disentangling the instruction-following capabilities from pre-trained knowledge improves the effectiveness of instruction tuning. To this end, we propose CoDIT, a method that applies contrastive decoding between a post-trained model and its pre-trained counterpart during response generation. The method suppresses pre-trained knowledge shared between the two models while amplifying the instruction-following behavior acquired via post-training, resulting in responses that more purely reflect instruction-following capabilities. Experiment results demonstrate that models trained on datasets constructed via CoDIT consistently outperform those trained on directly generated responses. Training on our datasets also yields better performance than on existing publicly available instruction-tuning datasets across multiple benchmarks. Furthermore, we theoretically and empirically show that CoDIT can be interpreted as distilling the chat vector from parameter space to text space, enabling the transfer of instruction-tuning capabilities across models of different architectures.

---


### 57. [Free Lunch for Unified Multimodal Models: Enhancing Generation via Reflective Rectification with Inherent Understanding](https://arxiv.org/abs/2604.13540)

**<font color=#1a73e8>作者：</font>** Yibo Jiang, Tao Wu, Rui Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Models (UMMs) aim to integrate visual understanding and generation within a single structure. However, these models exhibit a notable capability mismatch, where their understanding capability significantly outperforms their generation. This mismatch indicates that the model's rich internal knowledge, while effective for understanding tasks, remains underactivated during generation. To address this, we draw inspiration from the human ``Thinking-While-Drawing'' paradigm, where humans continuously reflect to activate their knowledge and rectify intermediate results. In this paper, we propose UniRect-CoT, a training-free unified rectification chain-of-thought framework. Our approach unlocks the ``free lunch'' hidden in the UMM's powerful inherent understanding to continuously reflect, activating its internal knowledge and rectifying intermediate results during this http URL regard the diffusion denoising process in UMMs as an intrinsic visual reasoning process and align the intermediate results with the target instruction understood by the model, serving as a self-supervisory signal to rectify UMM this http URL experiments demonstrate that UniRect-CoT can be easily integrated into existing UMMs, significantly enhancing generation quality across diverse complex tasks.

---


### 58. [Debate to Align: Reliable Entity Alignment through Two-Stage Multi-Agent Debate](https://arxiv.org/abs/2604.13551)

**<font color=#1a73e8>作者：</font>** Cunda Wang, Ziying Ma, Po Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entity alignment (EA) aims to identify entities referring to the same real-world object across different knowledge graphs (KGs). Recent approaches based on large language models (LLMs) typically obtain entity embeddings through knowledge representation learning and use embedding similarity to identify an alignment-uncertain entity set. For each uncertain entity, a candidate entity set (CES) is then retrieved based on embedding similarity to support subsequent alignment reasoning and decision making. However, the reliability of the CES and the reasoning capability of LLMs critically affect the effectiveness of subsequent alignment decisions. To address this issue, we propose AgentEA, a reliable EA framework based on multi-agent debate. AgentEA first improves embedding quality through entity representation preference optimization, and then introduces a two-stage multi-role debate mechanism consisting of lightweight debate verification and deep debate alignment to progressively enhance the reliability of alignment decisions while enabling more efficient debate-based reasoning. Extensive experiments on public benchmarks under cross-lingual, sparse, large-scale, and heterogeneous settings demonstrate the effectiveness of AgentEA.

---


### 59. [Training-Free Test-Time Contrastive Learning for Large Language Models](https://arxiv.org/abs/2604.13552)

**<font color=#1a73e8>作者：</font>** Kaiwen Zheng, Kai Zhou, Jinwu Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate strong reasoning capabilities, but their performance often degrades under distribution shift. Existing test-time adaptation (TTA) methods rely on gradient-based updates that require white-box access and need substantial overhead, while training-free alternatives are either static or depend on external guidance. In this paper, we propose Training-Free Test-Time Contrastive Learning TF-TTCL, a training-free adaptation framework that enables a frozen LLM to improve online by distilling supervision from its own inference experiences. Specifically, TF-TTCL implements a dynamic "Explore-Reflect-Steer" loop through three core modules: 1) Semantic Query Augmentation first diversifies problem views via multi-agent role-playing to generate different reasoning trajectories; 2) Contrastive Experience Distillation then captures the semantic gap between superior and inferior trajectories, distilling them into explicit textual rules; and 3) Contextual Rule Retrieval finally activates these stored rules during inference to dynamically steer the frozen LLM toward robust reasoning patterns while avoiding observed errors. Extensive experiments on closed-ended reasoning tasks and open-ended evaluation tasks demonstrate that TF-TTCL consistently outperforms strong zero-shot baselines and representative TTA methods under online evaluation. Code is available at this https URL.

---


### 60. [YOCO++: Enhancing YOCO with KV Residual Connections for Efficient LLM Inference](https://arxiv.org/abs/2604.13556)

**<font color=#1a73e8>作者：</font>** You Wu, Ziheng Chen, Yizhen Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-layer key-value (KV) compression has been found to be effective in efficient inference of large language models (LLMs). Although they reduce the memory consumption of the KV cache, such methods usually introduce non-negligible performance degradation. In this work, we aim to enhance the performance of YOCO, a cross-layer KV compression method that shares the KVs of the middle layer with the top-half layers. We propose YOCO++, an enhanced YOCO that incorporates a weighted residual connection between the KVs of each bottom-half layer and the bottom layer. Compared to YOCO, YOCO++ increases model capacity while maintaining the same training and inference efficiency. Our experiments show that YOCO++ achieves state-of-the-art performance among the cross-layer KV compression methods at a 50% KV cache compression rate, outperforming the standard Transformer.

---


### 61. [CLIP Architecture for Abdominal CT Image-Text Alignment and Zero-Shot Learning: Investigating Batch Composition and Data Scaling](https://arxiv.org/abs/2604.13561)

**<font color=#1a73e8>作者：</font>** Shivika, Kartik Bose, Pankaj Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models trained with contrastive learning on paired medical images and reports show strong zero-shot diagnostic capabilities, yet the effect of training batch composition on learned representations remains unexplored for 3D medical imaging. We reproduce Merlin, a dual-encoder model that aligns 3D abdominal CT volumes with radiology reports using symmetric InfoNCE loss, achieving a zero-shot macro F1 of 74.45% across 30 findings (original: 73.00%). We then investigate two axes of variation. First, we control the normal-to-abnormal ratio within training batches at 25:75, 50:50, and 75:25 using section-level balanced sampling on the full dataset. All three configurations underperform the unbalanced baseline by 2.4 to 2.8 points, with 75:25 achieving the best result (72.02%) among balanced variants. Second, we conduct data scaling ablations on a 4,362-study subset, training with 20%, 40%, and 100% of the data. Performance scales sub-linearly from 65.26% to 71.88%, with individual findings varying dramatically in data sensitivity. Enforcing 50:50 balanced sampling on the same subset further degrades performance to 68.01%, confirming that explicit class balancing hurts regardless of dataset or balancing granularity. Our results indicate that the stochastic diversity of random sampling, combined with Merlin's alternating batching over anatomical subsections, provides more effective regularization than engineered class ratios at the small batch sizes required by 3D medical volumes.

---


### 62. [UHR-BAT: Budget-Aware Token Compression Vision-Language model for Ultra-High-Resolution Remote Sensing](https://arxiv.org/abs/2604.13565)

**<font color=#1a73e8>作者：</font>** Yunkai Dang, Minxin Dai, Yuekun Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-high-resolution (UHR) remote sensing imagery couples kilometer-scale context with query-critical evidence that may occupy only a few pixels. Such vast spatial scale leads to a quadratic explosion of visual tokens and hinders the extraction of information from small objects. Previous works utilize direct downsampling, dense tiling, or global top-k pruning, which either compromise query-critical image details or incur unpredictable compute. In this paper, we propose UHR-BAT, a query-guided and region-faithful token compression framework to efficiently select visual tokens under a strict context budget. Specifically, we leverage text-guided, multi-scale importance estimation for visual tokens, effectively tackling the challenge of achieving precise yet low-cost feature extraction. Furthermore, by introducing region-wise preserve and merge strategies, we mitigate visual token redundancy, further driving down the computational budget. Experimental results show that UHR-BAT achieves state-of-the-art performance across various benchmarks. Code will be available at this https URL.

---


### 63. [MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning](https://arxiv.org/abs/2604.13579)

**<font color=#1a73e8>作者：</font>** Jiahang Lin, Kai Hu, Binghai Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conventional Retrieval-Augmented Generation (RAG) systems often struggle with complex multi-hop queries over long documents due to their single-pass retrieval. We introduce MM-Doc-R1, a novel framework that employs an agentic, vision-aware workflow to address long document visual question answering through iterative information discovery and synthesis. To incentivize the information seeking capabilities of our agents, we propose Similarity-based Policy Optimization (SPO), addressing baseline estimation bias in existing multi-turn reinforcement learning (RL) algorithms like GRPO. Our core insight is that in multi-turn RL, the more semantically similar two trajectories are, the more accurate their shared baseline estimation becomes. Leveraging this, SPO calculates a more precise baseline by similarity-weighted averaging of rewards across multiple trajectories, unlike GRPO which inappropriately applies the initial state's baseline to all intermediate states. This provides a more stable and accurate learning signal for our agents, leading to superior training performance that surpasses GRPO. Our experiments on the MMLongbench-Doc benchmark show that MM-Doc-R1 outperforms previous baselines by 10.4%. Furthermore, SPO demonstrates superior performance over GRPO, boosting results by 5.0% with Qwen3-8B and 6.1% with Qwen3-4B. These results highlight the effectiveness of our integrated framework and novel training algorithm in advancing the state-of-the-art for complex, long-document visual question answering.

---


### 64. [Efficient Multi-View 3D Object Detection by Dynamic Token Selection and Fine-Tuning](https://arxiv.org/abs/2604.13586)

**<font color=#1a73e8>作者：</font>** Danish Nazir, Antoine Hanna-Asaad, Lucas Görnhardt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing multi-view three-dimensional (3D) object detection approaches widely adopt large-scale pre-trained vision transformer (ViT)-based foundation models as backbones, being computationally complex. To address this problem, current state-of-the-art (SOTA) \texttt{ToC3D} for efficient multi-view ViT-based 3D object detection employs ego-motion-based relevant token selection. However, there are two key limitations: (1) The fixed layer-individual token selection ratios limit computational efficiency during both training and inference. (2) Full end-to-end retraining of the ViT backbone is required for the multi-view 3D object detection method. In this work, we propose an image token compensator combined with a token selection for ViT backbones to accelerate multi-view 3D object detection. Unlike \texttt{ToC3D}, our approach enables dynamic layer-wise token selection within the ViT backbone. Furthermore, we introduce a parameter-efficient fine-tuning strategy, which trains only the proposed modules, thereby reducing the number of fine-tuned parameters from more than $300$ million (M) to only $1.6$ M. Experiments on the large-scale NuScenes dataset across three multi-view 3D object detection approaches demonstrate that our proposed method decreases computational complexity (GFLOPs) by $48\%$ ... $55\%$, inference latency (on an \texttt{NVIDIA-GV100} GPU) by $9\%$ ... $25\%$, while still improving mean average precision by $1.0\%$ ... $2.8\%$ absolute and NuScenes detection score by $0.4\%$ ... $1.2\%$ absolute compared to so-far SOTA \texttt{ToC3D}.

---


### 65. [Foresight Optimization for Strategic Reasoning in Large Language Models](https://arxiv.org/abs/2604.13592)

**<font color=#1a73e8>作者：</font>** Jiashuo Wang, Jiawen Duan, Jian Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning capabilities in large language models (LLMs) have generally advanced significantly. However, it is still challenging for existing reasoning-based LLMs to perform effective decision-making abilities in multi-agent environments, due to the absence of explicit foresight modeling. To this end, strategic reasoning, the most fundamental capability to anticipate the counterpart's behaviors and foresee its possible future actions, has been introduced to alleviate the above issues. Strategic reasoning is fundamental to effective decision-making in multi-agent environments, yet existing reasoning enhancement methods for LLMs do not explicitly capture its foresight nature. In this work, we introduce Foresight Policy Optimization (FoPO) to enhance strategic reasoning in LLMs, which integrates opponent modeling principles into policy optimization, thereby enabling explicit consideration of both self-interest and counterpart influence. Specifically, we construct two curated datasets, namely Cooperative RSA and Competitive Taboo, equipped with well-designed rules and moderate difficulty to facilitate a systematic investigation of FoPO in a self-play framework. Our experiments demonstrate that FoPO significantly enhances strategic reasoning across LLMs of varying sizes and origins. Moreover, models trained with FoPO exhibit strong generalization to out-of-domain strategic scenarios, substantially outperforming standard LLM reasoning optimization baselines.

---


### 66. [Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges](https://arxiv.org/abs/2604.13602)

**<font color=#1a73e8>作者：</font>** Xiaohua Wang, Muzhao Tian, Yuqi Zeng 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Human Feedback (RLHF) and related alignment paradigms have become central to steering large language models (LLMs) and multimodal large language models (MLLMs) toward human-preferred behaviors. However, these approaches introduce a systemic vulnerability: reward hacking, where models exploit imperfections in learned reward signals to maximize proxy objectives without fulfilling true task intent. As models scale and optimization intensifies, such exploitation manifests as verbosity bias, sycophancy, hallucinated justification, benchmark overfitting, and, in multimodal settings, perception--reasoning decoupling and evaluator manipulation. Recent evidence further suggests that seemingly benign shortcut behaviors can generalize into broader forms of misalignment, including deception and strategic gaming of oversight mechanisms. In this survey, we propose the Proxy Compression Hypothesis (PCH) as a unifying framework for understanding reward hacking. We formalize reward hacking as an emergent consequence of optimizing expressive policies against compressed reward representations of high-dimensional human objectives. Under this view, reward hacking arises from the interaction of objective compression, optimization amplification, and evaluator--policy co-adaptation. This perspective unifies empirical phenomena across RLHF, RLAIF, and RLVR regimes, and explains how local shortcut learning can generalize into broader forms of misalignment, including deception and strategic manipulation of oversight mechanisms. We further organize detection and mitigation strategies according to how they intervene on compression, amplification, or co-adaptation dynamics. By framing reward hacking as a structural instability of proxy-based alignment under scale, we highlight open challenges in scalable oversight, multimodal grounding, and agentic autonomy.

---


### 67. [Syn-TurnTurk: A Synthetic Dataset for Turn-Taking Prediction in Turkish Dialogues](https://arxiv.org/abs/2604.13620)

**<font color=#1a73e8>作者：</font>** Ahmet Tuğrul Bayrak, Mustafa Sertaç Türkel, Fatma Nur Korkmaz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Managing natural dialogue timing is a significant challenge for voice-based chatbots. Most current systems usually rely on simple silence detection, which often fails because human speech patterns involve irregular pauses. This causes bots to interrupt users, breaking the conversational flow. This problem is even more severe for languages like Turkish, which lack high-quality datasets for turn-taking prediction. This paper introduces Syn-TurnTurk, a synthetic Turkish dialogue dataset generated using various Qwen Large Language Models (LLMs) to mirror real-life verbal exchanges, including overlaps and strategic silences. We evaluated the dataset using several traditional and deep learning architectures. The results show that advanced models, particularly BI-LSTM and Ensemble (LR+RF) methods, achieve high accuracy (0.839) and AUC scores (0.910). These findings demonstrate that our synthetic dataset can have a positive affect for models understand linguistic cues, allowing for more natural human-machine interaction in Turkish.

---


### 68. [(How) Learning Rates Regulate Catastrophic Overtraining](https://arxiv.org/abs/2604.13627)

**<font color=#1a73e8>作者：</font>** Mark Rofin, Aditya Varre, Nicolas Flammarion  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is a common first stage of LLM post-training, teaching the model to follow instructions and shaping its behavior as a helpful assistant. At the same time, SFT may harm the fundamental capabilities of an LLM, particularly after long pretraining: a phenomenon known as catastrophic overtraining (Springer et al., 2025). To understand overtraining, we first investigate catastrophic forgetting in finetuning through the lens of implicit regularization of the learning rate. For models trained to the same SFT loss, we identify how the learning rate mediates optimization: finetuning with large and small steps converges to qualitatively different models. Next, we link forgetting to overtraining: learning rate decay increases the sharpness of the pretrained model, which in turn exacerbates catastrophic forgetting during SFT, leading to overtraining. Our findings paint a picture of the overtraining mechanism in LLMs and broadly contribute to the understanding of the interplay between optimization dynamics during pretraining and finetuning.

---


### 69. [VRAG-DFD: Verifiable Retrieval-Augmentation for MLLM-based Deepfake Detection](https://arxiv.org/abs/2604.13660)

**<font color=#1a73e8>作者：</font>** Hui Han, Shunli Wang, Yandan Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In Deepfake Detection (DFD) tasks, researchers proposed two types of MLLM-based methods: complementary combination with small DFD detectors, or static forgery knowledge this http URL lack of professional forgery knowledge hinders the performance of these this http URL solve this, we deeply considered two insightful issues: How to provide high-quality associated forgery knowledge for MLLMs? AND How to endow MLLMs with critical reasoning abilities given noisy reference information? Notably, we attempted to address above two questions with preliminary answers by leveraging the combination of Retrieval-Augmented Generation (RAG) and Reinforcement Learning (RL).Through RAG and RL techniques, we propose the VRAG-DFD framework with accurate dynamic forgery knowledge retrieval and powerful critical reasoning this http URL, in terms of data, we constructed two datasets with RAG: Forensic Knowledge Database (FKD) for DFD knowledge annotation, and Forensic Chain-of-Thought Dataset (F-CoT), for critical CoT this http URL terms of model training, we adopt a three-stage training method (Alignment->SFT->GRPO) to gradually cultivate the critical reasoning ability of the this http URL terms of performance, VRAG-DFD achieved SOTA and competitive performance on DFD generalization testing.

---


### 70. [From Pixels to Nucleotides: End-to-End Token-Based Video Compression for DNA Storage](https://arxiv.org/abs/2604.13667)

**<font color=#1a73e8>作者：</font>** Cihan Ruan, Lebin Zhou, Bingqing Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> DNA-based storage has emerged as a promising approach to the global data crisis, offering molecular-scale density and millennial-scale stability at low maintenance cost. Over the past decade, substantial progress has been made in storing text, images, and files in DNA -- yet video remains an open challenge. The difficulty is not merely technical: effective video DNA storage requires co-designing compression and molecular encoding from the ground up, a challenge that sits at the intersection of two fields that have largely evolved independently. In this work, we present HELIX, the first end-to-end neural network jointly optimizing video compression and DNA encoding -- prior approaches treat the two stages independently, leaving biochemical constraints and compression objectives fundamentally misaligned. Our key insight: token-based representations naturally align with DNA's quaternary alphabet -- discrete semantic units map directly to ATCG bases. We introduce TK-SCONE (Token-Kronecker Structured Constraint-Optimized Neural Encoding), which achieves 1.91 bits per nucleotide through Kronecker-structured mixing that breaks spatial correlations and FSM-based mapping that guarantees biochemical constraints. Unlike two-stage approaches, HELIX learns token distributions simultaneously optimized for visual quality, prediction under masking, and DNA synthesis efficiency. This work demonstrates for the first time that learned compression and molecular storage converge naturally at token representations -- suggesting a new paradigm where neural video codecs are designed for biological substrates from the ground up.

---


### 71. [IndicDB -- Benchmarking Multilingual Text-to-SQL Capabilities in Indian Languages](https://arxiv.org/abs/2604.13686)

**<font color=#1a73e8>作者：</font>** Aviral Dawar, Roshan Karanth, Vikram Goyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have significantly advanced Text-to-SQL performance, existing benchmarks predominantly focus on Western contexts and simplified schemas, leaving a gap in real-world, non-Western applications. We present IndicDB, a multilingual Text-to-SQL benchmark for evaluating cross-lingual semantic parsing across diverse Indic languages. The relational schemas are sourced from open-data platforms, including the National Data and Analytics Platform (NDAP) and the India Data Portal (IDP), ensuring realistic administrative data complexity. IndicDB comprises 20 databases across 237 tables. To convert denormalized government data into rich relational structures, we employ an iterative three-agent framework (Architect, Auditor, Refiner) to ensure structural rigor and high relational density (11.85 tables per database; join depths up to six). Our pipeline is value-aware, difficulty-calibrated, and join-enforced, generating 15,617 tasks across English, Hindi, and five Indic languages. We evaluate cross-lingual semantic parsing performance of state-of-the-art models (DeepSeek v3.2, MiniMax 2.7, LLaMA 3.3, Qwen3) across seven linguistic variants. Results show a 9.00% performance drop from English to Indic languages, revealing an "Indic Gap" driven by harder schema linking, increased structural ambiguity, and limited external knowledge. IndicDB serves as a rigorous benchmark for multilingual Text-to-SQL. Code and data: this https URL

---


### 72. [Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection](https://arxiv.org/abs/2604.13692)

**<font color=#1a73e8>作者：</font>** Xiao Pu, Zepeng Cheng, Lin Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) generate text that increasingly resembles human writing, the subtle cues that distinguish AI-generated content from human-written content become increasingly challenging to capture. Reliance on generator-specific artifacts is inherently unstable, since new models emerge rapidly and reduce the robustness of such shortcuts. This generalizes unseen generators as a central and challenging problem for AI-text detection. To tackle this challenge, we propose a progressively structured framework that disentangles AI-detection semantics from generator-aware artifacts. This is achieved through a compact latent encoding that encourages semantic minimality, followed by perturbation-based regularization to reduce residual entanglement, and finally a discriminative adaptation stage that aligns representations with task objectives. Experiments on MAGE benchmark, covering 20 representative LLMs across 7 categories, demonstrate consistent improvements over state-of-the-art methods, achieving up to 24.2% accuracy gain and 26.2% F1 improvement. Notably, performance continues to improve as the diversity of training generators increases, confirming strong scalability and generalization in open-set scenarios. Our source code will be publicly available at this https URL.

---


### 73. [Weight Patching: Toward Source-Level Mechanistic Localization in LLMs](https://arxiv.org/abs/2604.13694)

**<font color=#1a73e8>作者：</font>** Chenghao Sun, Chengsheng Zhang, Guanzheng Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability seeks to localize model behavior to the internal components that causally realize it. Prior work has advanced activation-space localization and causal tracing, but modules that appear important in activation space may merely aggregate or amplify upstream signals rather than encode the target capability in their own parameters. To address this gap, we propose Weight Patching, a parameter-space intervention method for source-oriented analysis in paired same-architecture models that differ in how strongly they express a target capability under the inputs of interest. Given a base model and a behavior-specialized counterpart, Weight Patching replaces selected module weights from the specialized model into the base model under a fixed input. We instantiate the method on instruction following and introduce a framework centered on a vector-anchor behavioral interface that provides a shared internal criterion for whether a task-relevant control state has been formed or recovered in open-ended generation. Under this framework, the analysis reveals a hierarchy from shallow candidate source-side carriers to aggregation and routing modules, and further to downstream execution circuits. The recovered component scores can also guide mechanism-aware model merging, improving selective fusion across the evaluated expert combinations and providing additional external validation.

---


### 74. [MIND: AI Co-Scientist for Material Research](https://arxiv.org/abs/2604.13699)

**<font color=#1a73e8>作者：</font>** Geonhee Ahn, Donghyun Lee, Hayoung Doo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have enabled agentic AI systems for scientific discovery, but most approaches remain limited to textbased reasoning without automated experimental verification. We propose MIND, an LLM-driven framework for automated hypothesis validation in materials research. MIND organizes the scientific discovery process into hypothesis refinement, experimentation, and debate-based validation within a multi-agent pipeline. For experimental verification, the system integrates Machine Learning Interatomic Potentials, particularly SevenNet-Omni, enabling scalable in-silico experiments. We also provide a web-based user interface for automated hypothesis testing. The modular design allows additional experimental modules to be integrated, making the framework adaptable to broader scientific workflows. The code is available at: this https URL, and a demonstration video at: this https URL.

---


### 75. [Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration](https://arxiv.org/abs/2604.13705)

**<font color=#1a73e8>作者：</font>** Sayan Kumar Chaki, Antoine Gourru, Julien Velcin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fairness in language models is typically studied as a property of a single, centrally optimized model. As large language models become increasingly agentic, we propose that fairness emerges through interaction and exchange. We study this via a controlled hospital triage framework in which two agents negotiate over three structured debate rounds. One agent is aligned to a specific ethical framework via retrieval-augmented generation (RAG), while the other is either unaligned or adversarially prompted to favor demographic groups over clinical need. We find that alignment systematically shapes negotiation strategies and allocation patterns, and that neither agent's allocation is ethically adequate in isolation, yet their joint final allocation can satisfy fairness criteria that neither would have reached alone. Aligned agents partially moderate bias through contestation rather than override, acting as corrective patches that restore access for marginalized groups without fully converting a biased counterpart. We further observe that even explicitly aligned agents exhibit intrinsic biases toward certain frameworks, consistent with known left-leaning tendencies in LLMs. We connect these limits to Arrow's Impossibility Theorem: no aggregation mechanism can simultaneously satisfy all desiderata of collective rationality, and multi-agent deliberation navigates rather than resolves this constraint. Our results reposition fairness as an emergent, procedural property of decentralized agent interaction, and the system rather than the individual agent as the appropriate unit of evaluation.

---


### 76. [Co-FactChecker: A Framework for Human-AI Collaborative Claim Verification Using Large Reasoning Models](https://arxiv.org/abs/2604.13706)

**<font color=#1a73e8>作者：</font>** Dhruv Sahnan, Subhabrata Dutta, Tanmoy Chakraborty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Professional fact-checkers rely on domain knowledge and deep contextual understanding to verify claims. Large language models (LLMs) and large reasoning models (LRMs) lack such grounding and primarily reason from available evidence alone, creating a mismatch between expert-led and fully automated claim verification. To mitigate this gap, we posit human-AI collaboration as a more promising path forward, where expert feedback, grounded in real-world knowledge and domain expertise, guides the model's reasoning. However, existing LRMs are hard to calibrate to natural language feedback, particularly in a multi-turn interaction setup. We propose Co-FactChecker, a framework for human-AI collaborative claim verification. We introduce a new interaction paradigm that treats the model's thinking trace as a shared scratchpad. Co-FactChecker translates expert feedback into trace-edits that introduce targeted modifications to the trace, sidestepping the shortcomings of dialogue-based interaction. We provide theoretical results showing that trace-editing offers advantages over multi-turn dialogue, and our automatic evaluations demonstrate that Co-FactChecker outperforms existing autonomous and human-AI collaboration approaches. Human evaluations further show that Co-FactChecker is preferred over multi-turn dialogue, producing higher quality reasoning and verdicts along with relatively easier to interpret and more useful thinking traces.

---


### 77. [SLQ: Bridging Modalities via Shared Latent Queries for Retrieval with Frozen MLLMs](https://arxiv.org/abs/2604.13710)

**<font color=#1a73e8>作者：</font>** Haoran Lou, Ziyan Liu, Chunxiao Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) exhibit strong reasoning and world knowledge, yet adapting them for retrieval remains challenging. Existing approaches rely on invasive parameter updates, such as full fine-tuning and LoRA, which may disrupt the pre-trained semantic space and impair the structured knowledge essential for reasoning. In this work, we argue that adapting MLLMs for retrieval should focus on eliciting pre-trained representations rather than overwriting them. To this end, we propose SLQ, an effective and efficient framework that adapts a frozen MLLM into a retriever through a small set of Shared Latent Queries. Appended to the end of both text and image token sequences, these queries leverage the model's native causal attention to serve as global aggregation interfaces, producing compact embeddings in a unified space while keeping the backbone unchanged. Furthermore, to better evaluate retrieval beyond superficial pattern matching, we construct KARR-Bench, a benchmark designed for knowledge-aware reasoning retrieval. Extensive experiments show that SLQ outperforms full fine-tuning and LoRA on COCO and Flickr30K, while achieving competitive performance on MMEB and yielding substantial gains on KARR-Bench. The results demonstrate that SLQ, which preserves pre-trained representations, provides an effective and efficient framework for adapting MLLMs to retrieval.

---


### 78. [An Empirical Investigation of Practical LLM-as-a-Judge Improvement Techniques on RewardBench 2](https://arxiv.org/abs/2604.13717)

**<font color=#1a73e8>作者：</font>** Ryan Lail  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge, using a language model to score or rank candidate responses, is widely used as a scalable alternative to human evaluation in RLHF pipelines, benchmarking, and application layer evaluations (evals). However, judgment reliability depends heavily on prompting and aggregation strategy. We present an empirical investigation of practical, drop-in techniques that improve GPT-5.4 judge accuracy on RewardBench 2 without any finetuning. Two techniques account for nearly all available gains: task-specific criteria injection (+3.0pp at negligible cost) and ensemble scoring (+9.8pp at 5x cost). Combined, they reach 83.6% accuracy, +11.9pp over the 71.7% baseline. Our investigation also covers three further techniques (calibration context, adaptive model escalation, and soft blending) which did not reliably improve on criteria + ensembling at comparable cost. Cheaper model tiers benefit disproportionately from ensembling: GPT-5.4 mini with k=8 achieves 79.2% at 1.2x baseline cost, and GPT-5.4 nano with k=8 reaches 71.4% at 0.4x baseline cost, making high-accuracy LLM judges accessible at low cost.

---


### 79. [MedRCube: A Multidimensional Framework for Fine-Grained and In-Depth Evaluation of MLLMs in Medical Imaging](https://arxiv.org/abs/2604.13756)

**<font color=#1a73e8>作者：</font>** Zhijie Bao, Fangke Chen, Licheng Bao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The potential of Multimodal Large Language Models (MLLMs) in domain of medical imaging raise the demands of systematic and rigorous evaluation frameworks that are aligned with the real-world medical imaging practice. Existing practices that report single or coarse-grained metrics are lack the granularity required for specialized clinical support and fail to assess the reliability of reasoning mechanisms. To address this, we propose a paradigm shift toward multidimensional, fine-grained and in-depth evaluation. Based on a two-stage systematic construction pipeline designed for this paradigm, we instantiate it with MedRCube. We benchmark 33 MLLMs, \textit{Lingshu-32B} achieve top-tier performance. Crucially, MedRCube exposes a series of pronounced insights inaccessible under prior evaluation settings. Furthermore, we introduce a credibility evaluation subset to quantify reasoning credibility, uncover a highly significant positive association between shortcut behavior and diagnostic task performance, raising concerns for clinically trustworthy deployment. The resources of this work can be found at this https URL.

---


### 80. [The cognitive companion: a lightweight parallel monitoring architecture for detecting and recovering from reasoning degradation in LLM agents](https://arxiv.org/abs/2604.13759)

**<font color=#1a73e8>作者：</font>** Rafflesia Khan, Nafiul Islam Khan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents on multi-step tasks suffer reasoning degradation, looping, drift, stuck states, at rates up to 30% on hard tasks. Current solutions include hard step limits (abrupt) or LLM-as-judge monitoring (10-15% overhead per step). This paper introduces the Cognitive Companion, a parallel monitoring architecture with two implementations: an LLM-based Companion and a novel zero-overhead Probe-based Companion. We report a three-batch feasibility study centered on Gemma 4 E4B, with an additional exploratory small-model analysis on Qwen 2.5 1.5B and Llama 3.2 1B. In our experiments, the LLM-based Companion reduced repetition on loop-prone tasks by 52-62% with approximately 11% overhead. The Probe-based Companion, trained on hidden states from layer 28, showed a mean effect size of +0.471 at zero measured inference overhead; its strongest probe result achieved cross-validated AUROC 0.840 on a small proxy-labeled dataset. A key empirical finding is that companion benefit appears task-type dependent: companions are most helpful on loop-prone and open-ended tasks, while effects are neutral or negative on more structured tasks. Our small-model experiments also suggest a possible scale boundary: companions did not improve the measured quality proxy on 1B-1.5B models, even when interventions fired. Overall, the paper should be read as a feasibility study rather than a definitive validation. The results provide encouraging evidence that sub-token monitoring may be useful, identify task-type sensitivity as a practical design constraint, and motivate selective companion activation as a promising direction for future work.

---


### 81. [From Anchors to Supervision: Memory-Graph Guided Corpus-Free Unlearning for Large Language Models](https://arxiv.org/abs/2604.13777)

**<font color=#1a73e8>作者：</font>** Wenxuan Li, Zhenfei Zhang, Mi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) may memorize sensitive or copyrighted content, raising significant privacy and legal concerns. While machine unlearning has emerged as a potential remedy, prevailing paradigms rely on user-provided forget sets, making unlearning requests difficult to audit and exposing systems to secondary leakage and malicious abuse. We propose MAGE, a Memory-grAph Guided Erasure framework for user-minimized, corpus-free unlearning. Given only a lightweight user anchor that identifies a target entity, MAGE probes the target LLM to recover target-related memorization, organizes it into a weighted local memory graph, and synthesizes scoped supervision for unlearning. MAGE is model-agnostic, can be plugged into standard unlearning methods, and requires no access to the original training corpus. Experiments on two benchmarks, TOFU and RWKU, demonstrate that MAGE's self-generated supervision achieves effective unlearning performance comparable to supervision generated with external reference, while preserving overall utility. These results support a practical and auditable unlearning workflow driven by minimal anchors rather than user-supplied forget corpora.

---


### 82. [QuantileMark: A Message-Symmetric Multi-bit Watermark for LLMs](https://arxiv.org/abs/2604.13786)

**<font color=#1a73e8>作者：</font>** Junlin Zhu, Baizhou Huang, Xiaojun Wan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models become standard backends for content generation, practical provenance increasingly requires multi-bit watermarking. In provider-internal deployments, a key requirement is message symmetry: the message itself should not systematically affect either text quality or verification outcomes. Vocabulary-partition watermarks can break message symmetry in low-entropy decoding: some messages are assigned most of the probability mass, while others are forced to use tail tokens. This makes embedding quality and message decoding accuracy message-dependent. We propose QuantileMark, a white-box multi-bit watermark that embeds messages within the continuous cumulative probability interval $[0, 1)$. At each step, QuantileMark partitions this interval into $M$ equal-mass bins and samples strictly from the bin assigned to the target symbol, ensuring a fixed $1/M$ probability budget regardless of context entropy. For detection, the verifier reconstructs the same partition under teacher forcing, computes posteriors over latent bins, and aggregates evidence for verification. We prove message-unbiasedness, a property ensuring that the base distribution is recovered when averaging over messages. This provides a theoretical foundation for generation-side symmetry, while the equal-mass design additionally promotes uniform evidence strength across messages on the detection side. Empirical results on C4 continuation and LFQA show improved multi-bit recovery and detection robustness over strong baselines, with negligible impact on generation quality. Our code is available at GitHub (this https URL).

---


### 83. [ToolOmni: Enabling Open-World Tool Use via Agentic learning with Proactive Retrieval and Grounded Execution](https://arxiv.org/abs/2604.13787)

**<font color=#1a73e8>作者：</font>** Shouzheng Huang, Meishan Zhang, Baotian Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) enhance their problem-solving capability by utilizing external tools. However, in open-world scenarios with massive and evolving tool repositories, existing methods relying on static embedding retrieval or parameter memorization of tools struggle to align user intent with tool semantics or generalize to unseen tools, respectively, leading to suboptimal accuracy of open-world tool retrieval and execution. To address these, we present ToolOmni, a unified agentic framework that enables LLMs for open-world tool use by proactive retrieval and grounded execution within a reasoning loop. First, we construct a cold-start multi-turn interaction dataset to instill foundational agentic capabilities via Supervised Fine-Tuning (SFT). Then, we introduce open-world tool learning based on a Decoupled Multi-Objective GRPO algorithm, which simultaneously optimizes LLMs for both tool retrieval accuracy and execution efficacy in online environments. Extensive experiments demonstrate that ToolOmni achieves state-of-the-art performance both in retrieval and execution, surpassing strong baselines by a significant margin of +10.8% in end-to-end execution success rate, while exhibiting exceptional robustness and generalization capabilities.

---


### 84. [Gaslight, Gatekeep, V1-V3: Early Visual Cortex Alignment Shields Vision-Language Models from Sycophantic Manipulation](https://arxiv.org/abs/2604.13803)

**<font color=#1a73e8>作者：</font>** Arya Shah, Vaibhav Tripathi, Mayank Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly deployed in high-stakes settings, yet their susceptibility to sycophantic manipulation remains poorly understood, particularly in relation to how these models represent visual information internally. Whether models whose visual representations more closely mirror human neural processing are also more resistant to adversarial pressure is an open question with implications for both neuroscience and AI safety. We investigate this question by evaluating 12 open-weight vision-language models spanning 6 architecture families and a 40$\times$ parameter range (256M--10B) along two axes: brain alignment, measured by predicting fMRI responses from the Natural Scenes Dataset across 8 human subjects and 6 visual cortex regions of interest, and sycophancy, measured through 76,800 two-turn gaslighting prompts spanning 5 categories and 10 difficulty levels. Region-of-interest analysis reveals that alignment specifically in early visual cortex (V1--V3) is a reliable negative predictor of sycophancy ($r = -0.441$, BCa 95\% CI $[-0.740, -0.031]$), with all 12 leave-one-out correlations negative and the strongest effect for existence denial attacks ($r = -0.597$, $p = 0.040$). This anatomically specific relationship is absent in higher-order category-selective regions, suggesting that faithful low-level visual encoding provides a measurable anchor against adversarial linguistic override in vision-language models. We release our code on \href{this https URL}{GitHub} and dataset on \href{this https URL}{Hugging Face}

---


### 85. [Character Beyond Speech: Leveraging Role-Playing Evaluation in Audio Large Language Models via Reinforcement Learning](https://arxiv.org/abs/2604.13804)

**<font color=#1a73e8>作者：</font>** Dongjie Fu, Fangming Feng, Xize Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of multimodal large models has revolutionized the simulation of diverse characters in speech dialogue systems, enabling a novel interactive paradigm. Character attributes are manifested not only in textual responses but also through vocal features, as speech conveys rich paralinguistic information that is challenging to quantify. This poses significant difficulties in evaluating the character alignment of role-playing agents. To address these challenges, we present RoleJudge, an evaluation framework that leverages audio large language models to systematically assess the alignment between speech and character across multiple modalities and dimensions. Furthermore, we introduce RoleChat, the first voice role-playing evaluation dataset enriched with chain-of-thought reasoning annotations, comprising a diverse set of authentic and LLM-generated speech samples. Utilizing this dataset, we implement a multi-stage training paradigm and incorporate Standard Alignment in reinforcement learning to mitigate reward misalignment during optimization. Experimental results in terms of accuracy and subjective assessment demonstrate that RoleJudge outperforms various baseline models, validating the effectiveness of our multidimensional evaluation framework.

---


### 86. [Robust Ultra Low-Bit Post-Training Quantization via Stable Diagonal Curvature Estimate](https://arxiv.org/abs/2604.13806)

**<font color=#1a73e8>作者：</font>** Jaemin Kim, Sungkyun Kim, Junyeol Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are widely used across many domains, but their scale makes deployment challenging. Post-Training Quantization (PTQ) reduces memory footprint without retraining by leveraging a small calibration set. Recent Hessian-based PTQ methods compensate quantization error via cross-channel dependencies, but such approaches degrade at low bit-widths due to noisy curvature estimates from limited calibration data. We propose DASH-Q, a robust PTQ framework using diagonal Hessian approximation and iterative weighted least squares. By discarding noise-prone dependencies, DASH-Q filters sampling noise while prioritizing the preservation of salient feature power. We outperform other PTQ baselines in ultra low-bit regime, improving zero-shot accuracy by 7.01% on average and up to 14.01% over the strongest baselines across five baseline LLM models, while showing robust and stable performance with very small calibration data.

---


### 87. [Beyond State Consistency: Behavior Consistency in Text-Based World Models](https://arxiv.org/abs/2604.13824)

**<font color=#1a73e8>作者：</font>** Youling Huang, Guanqiao Chen, Junchi Yao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models have been emerging as critical components for assessing the consequences of actions generated by interactive agents in online planning and offline evaluation. In text-based environments, world models are typically evaluated and trained with single-step metrics such as Exact Match, aiming to improve the similarity between predicted and real-world states, but such metrics have been shown to be insufficient for capturing actual agent behavior. To address this issue, we introduce a new behavior-aligned training paradigm aimed at improving the functional consistency between the world model and the real environment. This paradigm focuses on optimizing a tractable step-level metric named Behavior Consistency Reward (BehR), which measures how much the likelihood of a logged next action changes between the real state and the world-model-predicted state under a frozen Reference Agent. Experiments on WebShop and TextWorld show that BehR-based training improves long-term alignment in several settings, with the clearest gains in WebShop and less movement in near-ceiling regimes, while preserving or improving single-step prediction quality in three of four settings. World models trained with BehR also achieve lower false positives in offline surrogate evaluation and show modest but encouraging gains in inference-time lookahead planning.

---


### 88. [MUSE: Multi-Domain Chinese User Simulation via Self-Evolving Profiles and Rubric-Guided Alignment](https://arxiv.org/abs/2604.13828)

**<font color=#1a73e8>作者：</font>** Zihao Liu, Hantao Zhou, Jiguo Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User simulators are essential for the scalable training and evaluation of interactive AI systems. However, existing approaches often rely on shallow user profiling, struggle to maintain persona consistency over long interactions, and are largely limited to English or single-domain settings. We present MUSE, a multi-domain Chinese user simulation framework designed to generate human-like, controllable, and behaviorally consistent responses. First, we propose Iterative Profile Self-Evolution (IPSE), which gradually optimizes user profiles by comparing and reasoning discrepancies between simulated trajectories and real dialogue behaviors. We then apply Role-Reversal Supervised Fine-Tuning to improve local response realism and human-like expression. To enable fine-grained behavioral alignment, we further train a specialized rubric-based reward model and incorporate it into rubric-guided multi-turn reinforcement learning, which optimizes the simulator at the dialogue level and enhances long-horizon behavioral consistency. Experiments show that MUSE consistently outperforms strong baselines in both utterance-level and session-level evaluations, generating responses that are more realistic, coherent, and persona-consistent over extended interactions.

---


### 89. [Robust Reward Modeling for Large Language Models via Causal Decomposition](https://arxiv.org/abs/2604.13833)

**<font color=#1a73e8>作者：</font>** Yunsheng Lu, Zijiang Yang, Licheng Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reward models are central to aligning large language models, yet they often overfit to spurious cues such as response length and overly agreeable tone. Most prior work weakens these cues directly by penalizing or controlling specific artifacts, but it does not explicitly encourage the model to ground preferences in the prompt's intent. We learn a decoder that maps a candidate answer to the latent intent embedding of the input. The reconstruction error is used as a signal to regularize the reward model training. We provide theoretical evidence that this signal emphasizes prompt-dependent information while suppressing prompt-independent shortcuts. Across math, helpfulness, and safety benchmarks, the decoder selects shorter and less sycophantic candidates with 0.877 accuracy. Incorporating this signal into RM training in Gemma-2-2B-it and Gemma-2-9B-it increases RewardBench accuracy from 0.832 to 0.868. For Best-of-N selection, our framework increases length-controlled win rates while producing shorter outputs, and remains robust to lengthening and mild off-topic drift in controlled rewrite tests.

---


### 90. [Beyond Static Personas: Situational Personality Steering for Large Language Models](https://arxiv.org/abs/2604.13846)

**<font color=#1a73e8>作者：</font>** Zesheng Wei, Mengxiang Li, Zilei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized Large Language Models (LLMs) facilitate more natural, human-like interactions in human-centric applications. However, existing personalization methods are constrained by limited controllability and high resource demands. Furthermore, their reliance on static personality modeling restricts adaptability across varying situations. To address these limitations, we first demonstrate the existence of situation-dependency and consistent situation-behavior patterns within LLM personalities through a multi-perspective analysis of persona neurons. Building on these insights, we propose IRIS, a training-free, neuron-based Identify-Retrieve-Steer framework for advanced situational personality steering. Our approach comprises situational persona neuron identification, situation-aware neuron retrieval, and similarity-weighted steering. We empirically validate our framework on PersonalityBench and our newly introduced SPBench, a comprehensive situational personality benchmark. Experimental results show that our method surpasses best-performing baselines, demonstrating IRIS's generalization and robustness to complex, unseen situations and different models architecture.

---


### 91. ["AI Psychosis" in Context: How Conversation History Shapes LLM Responses to Delusional Beliefs](https://arxiv.org/abs/2604.13860)

**<font color=#1a73e8>作者：</font>** Luke Nicholls, Robert Hutto, Zephrah Soto  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extended interaction with large language models (LLMs) has been linked to the reinforcement of delusional beliefs, a phenomenon attracting growing clinical and public concern. Yet most empirical work evaluates model safety in brief interactions, which may not reflect how these harms develop through sustained dialogue. We tested five models across three levels of accumulated context, using the same escalating delusional history to isolate its effect on model behaviour. Human raters coded responses on risk and safety dimensions, and each model was analysed qualitatively. Models separated into two distinct tiers: GPT-4o, Grok 4.1 Fast, and Gemini 3 Pro exhibited high-risk, low-safety profiles; Claude Opus 4.5 and GPT-5.2 Instant displayed the opposite pattern. As context accumulated, performance tended to degrade in the unsafe group, while the same material activated stronger safety interventions among the safer models. Qualitative analysis identified distinct mechanisms of failure, including validation of the user's delusional premises, elaboration beyond them, and attempting harm reduction from within the delusional frame. Safer models, however, often used the established relationship to support intervention, taking accountability for past missteps so that redirection would not be received as betrayal. These findings indicate that accumulated context functions as a stress test of safety architecture, revealing whether a model treats prior dialogue as a worldview to inherit or as evidence to evaluate. Short-context assessments may therefore mischaracterise model safety, underestimating danger in some systems while missing context-activated gains in others. The results suggest that delusional reinforcement by LLMs reflects a preventable alignment failure. In demonstrating that these harms can be resisted, the safer models establish a baseline future systems should now be expected to meet.

---


### 92. [Context Sensitivity Improves Human-Machine Visual Alignment](https://arxiv.org/abs/2604.13883)

**<font color=#1a73e8>作者：</font>** Frieda Born, Tom Neuhäuser, Lukas Muttenthaler 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern machine learning models typically represent inputs as fixed points in a high-dimensional embedding space. While this approach has been proven powerful for a wide range of downstream tasks, it fundamentally differs from the way humans process information. Because humans are constantly adapting to their environment, they represent objects and their relationships in a highly context-sensitive manner. To address this gap, we propose a method for context-sensitive similarity computation from neural network embeddings, applied to modeling a triplet odd-one-out task with an anchor image serving as simultaneous context. Modeling context enables us to achieve up to a 15% improvement in odd-one-out accuracy over a context-insensitive model. We find that this improvement is consistent across both original and "human-aligned" vision foundation models.

---


### 93. [GeoAgentBench: A Dynamic Execution Benchmark for Tool-Augmented Agents in Spatial Analysis](https://arxiv.org/abs/2604.13888)

**<font color=#1a73e8>作者：</font>** Bo Yu, Cheng Yang, Dongyang Hou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of Large Language Models (LLMs) into Geographic Information Systems (GIS) marks a paradigm shift toward autonomous spatial analysis. However, evaluating these LLM-based agents remains challenging due to the complex, multi-step nature of geospatial workflows. Existing benchmarks primarily rely on static text or code matching, neglecting dynamic runtime feedback and the multimodal nature of spatial outputs. To address this gap, we introduce GeoAgentBench (GABench), a dynamic and interactive evaluation benchmark tailored for tool-augmented GIS agents. GABench provides a realistic execution sandbox integrating 117 atomic GIS tools, encompassing 53 typical spatial analysis tasks across 6 core GIS domains. Recognizing that precise parameter configuration is the primary determinant of execution success in dynamic GIS environments, we designed the Parameter Execution Accuracy (PEA) metric, which utilizes a "Last-Attempt Alignment" strategy to quantify the fidelity of implicit parameter inference. Complementing this, a Vision-Language Model (VLM) based verification is proposed to assess data-spatial accuracy and cartographic style adherence. Furthermore, to address the frequent task failures caused by parameter misalignments and runtime anomalies, we developed a novel agent architecture, Plan-and-React, that mimics expert cognitive workflows by decoupling global orchestration from step-wise reactive execution. Extensive experiments with seven representative LLMs demonstrate that the Plan-and-React paradigm significantly outperforms traditional frameworks, achieving the optimal balance between logical rigor and execution robustness, particularly in multi-step reasoning and error recovery. Our findings highlight current capability boundaries and establish a robust standard for assessing and advancing the next generation of autonomous GeoAI.

---


### 94. [Do We Still Need Humans in the Loop? Comparing Human and LLM Annotation in Active Learning for Hostility Detection](https://arxiv.org/abs/2604.13899)

**<font color=#1a73e8>作者：</font>** Ahmad Dawar Hakimi, Lea Hirlimann, Isabelle Augenstein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned LLMs can annotate thousands of instances from a short prompt at negligible cost. This raises two questions for active learning (AL): can LLM labels replace human labels within the AL loop, and does AL remain necessary when entire corpora can be labelled at once? We investigate both questions on a new dataset of 277,902 German political TikTok comments (25,974 LLM-labelled, 5,000 human-annotated), comparing seven annotation strategies across four encoders to detect anti-immigrant hostility. A classifier trained on 25,974 GPT-5.2 labels (\$43) achieves comparable F1-Macro to one trained on 3,800 human annotations (\$316). Active learning offers little advantage over random sampling in our pre-enriched pool and delivers lower F1 than full LLM annotation at the same cost. However, comparable aggregate F1 masks a systematic difference in error structure: LLM-trained classifiers over-predict the positive class relative to the human gold standard. This divergence concentrates in topically ambiguous discussions where the distinction between anti-immigrant hostility and policy critique is most subtle, suggesting that annotation strategy should be guided not by aggregate F1 alone but by the error profile acceptable for the target application.

---


### 95. [DiPO: Disentangled Perplexity Policy Optimization for Fine-grained Exploration-Exploitation Trade-Off](https://arxiv.org/abs/2604.13902)

**<font color=#1a73e8>作者：</font>** Xiaofan Li, Ming Yang, Zhiyuan Ma 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has catalyzed significant advances in the reasoning capabilities of Large Language Models (LLMs). However, effectively managing the exploration and exploitation trade-off remains a critical challenge. In this paper, we fully analyze the exploration and exploitation dilemma of extremely hard and easy samples during the training and propose a new fine-grained trade-off mechanism. Concretely, we introduce a perplexity space disentangling strategy that divides the sample space into distinct exploration (high perplexity) and exploitation (low perplexity) subspaces, thereby mining fine-grained samples requiring exploration-exploitation trade-off. Subsequently, we propose a bidirectional reward allocation mechanism with a minimum impact on verification rewards to implement perplexity-guided exploration and exploitation, enabling more stable policy optimization. Finally, we have evaluated our method on two mainstream tasks: mathematical reasoning and function calling, and experimental results demonstrate the superiority of the proposed method, confirming its effectiveness in enhancing LLM performance by fine-grained exploration-exploitation trade-off.

---


### 96. [Leveraging LLM-GNN Integration for Open-World Question Answering over Knowledge Graphs](https://arxiv.org/abs/2604.13979)

**<font color=#1a73e8>作者：</font>** Hussein Abdallah, Ibrahim Abdelaziz, Panos Kalnis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-world Question Answering (OW-QA) over knowledge graphs (KGs) aims to answer questions over incomplete or evolving KGs. Traditional KGQA assumes a closed world where answers must exist in the KG, limiting real-world applicability. In contrast, open-world QA requires inferring missing knowledge based on graph structure and context. Large language models (LLMs) excel at language understanding but lack structured reasoning. Graph neural networks (GNNs) model graph topology but struggle with semantic interpretation. Existing systems integrate LLMs with GNNs or graph retrievers. Some support open-world QA but rely on structural embeddings without semantic grounding. Most assume observed paths or complete graphs, making them unreliable under missing links or multi-hop reasoning. We present GLOW, a hybrid system that combines a pre-trained GNN and an LLM for open-world KGQA. The GNN predicts top-k candidate answers from the graph structure. These, along with relevant KG facts, are serialized into a structured prompt (e.g., triples and candidates) to guide the LLM's reasoning. This enables joint reasoning over symbolic and semantic signals, without relying on retrieval or fine-tuning. To evaluate generalization, we introduce GLOW-BENCH, a 1,000-question benchmark over incomplete KGs across diverse domains. GLOW outperforms existing LLM-GNN systems on standard benchmarks and GLOW-BENCH, achieving up to 53.3% and an average 38% improvement. GitHub code and data are available.

---


### 97. [Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models](https://arxiv.org/abs/2604.13991)

**<font color=#1a73e8>作者：</font>** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are prone to generating factually incorrect outputs. Recent work has applied conformal prediction to provide uncertainty estimates and statistical guarantees for the factuality of LLM generations. However, existing approaches are typically not prompt-adaptive, limiting their ability to capture input-dependent variability. As a result, they may filter out too few items (leading to over-coverage) or too many (under-coverage) for a given task or prompt. We propose an adaptive conformal prediction approach that extends conformal score transformation methods to LLMs, with applications to long-form generation and multiple-choice question answering. This enables prompt-dependent calibration, retaining marginal coverage guarantees while improving conditional coverage. In addition, the approach naturally supports selective prediction, allowing unreliable claims or answer choices to be filtered out in downstream applications. We evaluate our approach on multiple white-box models across diverse domains and show that it significantly outperforms existing baselines in terms of conditional coverage.

---


### 98. [Reward Design for Physical Reasoning in Vision-Language Models](https://arxiv.org/abs/2604.13993)

**<font color=#1a73e8>作者：</font>** Derek Lilienthal, Manisha Mukherjee, Sameera Horawalavithana  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physical reasoning over visual inputs demands tight integration of visual perception, domain knowledge, and multi-step symbolic inference. Yet even state-of-the-art Vision Language Models (VLMs) fall far short of human performance on physics benchmarks. While post-training algorithms such as Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) have demonstrated strong reasoning gains in language models, how reward design shapes VLM physical reasoning behavior remains poorly understood. We present a systematic reward ablation study for GRPO-based VLM training on physical reasoning. We compare four reward signals of increasing semantic richness: format compliance, answer accuracy, a composite rubric reward (answer correctness, physics principle identification, and unit consistency), and a novel internal reward derived from model attention weights over input image regions. We evaluate on PhyX, a 3,000-problem benchmark spanning six physics domains and six reasoning types across multiple-choice and open-ended formats, using IBM Granite Vision 3.3 (2B). Across both formats, GRPO with accuracy-based rewards outperforms SFT on most domains, though gains vary substantially by reward type and domain. Reward design does not uniformly improve performance. Instead, it induces domain-specific reasoning behaviors. Accuracy-based rewards provide the strongest overall gains. Rubric rewards improve structured reasoning quality without consistent accuracy improvements. Attention-based rewards enhance spatial reasoning while degrading performance in symbolic domains. Our internal attention-weight reward requires no spatial annotations and improves spatial relation accuracy from 0.27 to 0.50, suggesting that supervising where the model attends during generation is a promising direction for visually grounded physical reasoning.

---


### 99. [Diffusion Language Models for Speech Recognition](https://arxiv.org/abs/2604.14001)

**<font color=#1a73e8>作者：</font>** Davyd Naveriani, Albert Zeyer, Ralf Schlüter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models have recently emerged as a leading alternative to standard language models, due to their ability for bidirectional attention and parallel text generation. In this work, we explore variants for their use in speech recognition. Specifically, we introduce a comprehensive guide to incorporating masked diffusion language models (MDLM) and uniform-state diffusion models (USDMs) for rescoring ASR hypotheses. Additionally, we design a new joint-decoding method that combines CTC and USDM by integrating the framewise probability distributions derived from CTC with the labelwise probability distributions computed by USDM at each decoding step, thereby generating new candidates that combine strong language knowledge from USDM and acoustic information from CTC. Our findings reveal that USDM, as well as MDLM, can significantly improve the accuracy of recognized text. We publish all our code and recipes.

---


### 100. [Parameter Importance is Not Static: Evolving Parameter Isolation for Supervised Fine-Tuning](https://arxiv.org/abs/2604.14010)

**<font color=#1a73e8>作者：</font>** Zekai Lin, Chao Xue, Di Liang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised Fine-Tuning (SFT) of large language models often suffers from task interference and catastrophic forgetting. Recent approaches alleviate this issue by isolating task-critical parameters during training. However, these methods represent a static solution to a dynamic problem, assuming that parameter importance remains fixed once identified. In this work, we empirically demonstrate that parameter importance exhibits temporal drift over the course of training. To address this, we propose Evolving Parameter Isolation (EPI), a fine-tuning framework that adapts isolation decisions based on online estimates of parameter importance. Instead of freezing a fixed subset of parameters, EPI periodically updates isolation masks using gradient-based signals, enabling the model to protect emerging task-critical parameters while releasing outdated ones to recover plasticity. Experiments on diverse multi-task benchmarks demonstrate that EPI consistently reduces interference and forgetting compared to static isolation and standard fine-tuning, while improving overall generalization. Our analysis highlights the necessity of synchronizing isolation mechanisms with the evolving dynamics of learning diverse abilities.

---


### 101. [MAny: Merge Anything for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2604.14016)

**<font color=#1a73e8>作者：</font>** Zijian Gao, Wangwang Jia, Xingxing Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Continual Instruction Tuning (MCIT) is essential for sequential task adaptation of Multimodal Large Language Models (MLLMs) but is severely restricted by catastrophic forgetting. While existing literature focuses on the reasoning language backbone, in this work, we expose a critical yet neglected dual-forgetting phenomenon across both perception drift in Cross-modal Projection Space and reasoning collapse in Low-rank Parameter Space. To resolve this, we present \textbf{MAny} (\textbf{M}erge \textbf{Any}thing), a framework that merges task-specific knowledge through \textbf{C}ross-modal \textbf{P}rojection \textbf{M}erging (\textbf{CPM}) and \textbf{L}ow-rank \textbf{P}arameter \textbf{M}erging (\textbf{LPM}). Specifically, CPM recovers perceptual alignment by adaptively merging cross-modal visual representations via visual-prototype guidance, ensuring accurate feature recovery during inference. Simultaneously, LPM eliminates mutual interference among task-specific low-rank modules by recursively merging low-rank weight matrices. By leveraging recursive least squares, LPM provides a closed-form solution that mathematically guarantees an optimal fusion trajectory for reasoning stability. Notably, MAny operates as a training-free paradigm that achieves knowledge merging via efficient CPU-based algebraic operations, eliminating additional gradient-based optimization beyond initial tuning. Our extensive evaluations confirm the superior performance and robustness of MAny across multiple MLLMs and benchmarks. Specifically, on the UCIT benchmark, MAny achieves significant leads of up to 8.57\% and 2.85\% in final average accuracy over state-of-the-art methods across two different MLLMs, respectively.

---


### 102. [POINTS-Seeker: Towards Training a Multimodal Agentic Search Model from Scratch](https://arxiv.org/abs/2604.14029)

**<font color=#1a73e8>作者：</font>** Yikun Liu, Yuan Liu, Le Tian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Large Multimodal Models (LMMs) demonstrate impressive visual perception, they remain epistemically constrained by their static parametric knowledge. To transcend these boundaries, multimodal search models have been adopted to actively interact with the external environment for evidence retrieval. Diverging from prevailing paradigms that merely retrofit general LMMs with search tools as modular extensions, we explore the potential of building a multimodal agentic search model from scratch. Specifically, we make the following contributions: (i) we introduce Agentic Seeding, a dedicated phase designed to weave the foundational precursors necessary for eliciting agentic behaviors; (ii) we uncover a performance bottleneck in long-horizon interactions, where the increasing volume of interaction history overwhelms the model's ability to locate ground-truth evidence. To mitigate this, we propose V-Fold, an adaptive history-aware compression scheme that preserves recent dialogue turns in high fidelity while folding historical context into the visual space via rendering; and (iii) we develop POINTS-Seeker-8B, a state-of-the-art multimodal agentic search model that consistently outperforms existing models across six diverse benchmarks, effectively resolving the challenges of long-horizon, knowledge-intensive visual reasoning.

---


### 103. [Dual-Enhancement Product Bundling: Bridging Interactive Graph and Large Language Model](https://arxiv.org/abs/2604.14030)

**<font color=#1a73e8>作者：</font>** Zhe Huang, Peng Wang, Yan Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Product bundling boosts e-commerce revenue by recommending complementary item combinations. However, existing methods face two critical challenges: (1) collaborative filtering approaches struggle with cold-start items owing to dependency on historical interactions, and (2) LLMs lack inherent capability to model interactive graph directly. To bridge this gap, we propose a dual-enhancement method that integrates interactive graph learning and LLM-based semantic understanding for product bundling. Our method introduces a graph-to-text paradigm, which leverages a Dynamic Concept Binding Mechanism (DCBM) to translate graph structures into natural language prompts. The DCBM plays a critical role in aligning domain-specific entities with LLM tokenization, enabling effective comprehension of combinatorial constraints. Experiments on three benchmarks (POG, POG_dense, Steam) demonstrate 6.3%-26.5% improvements over state-of-the-art baselines.

---


### 104. [Seek-and-Solve: Benchmarking MLLMs for Visual Clue-Driven Reasoning in Daily Scenarios](https://arxiv.org/abs/2604.14041)

**<font color=#1a73e8>作者：</font>** Xiaomin Li, Tala Wang, Zichen Zhong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Daily scenarios are characterized by visual richness, requiring Multimodal Large Language Models (MLLMs) to filter noise and identify decisive visual clues for accurate reasoning. Yet, current benchmarks predominantly aim at evaluating MLLMs' pre-existing knowledge or perceptual understanding, often neglecting the critical capability of reasoning. To bridge this gap, we introduce DailyClue, a benchmark designed for visual clue-driven reasoning in daily scenarios. Our construction is guided by two core principles: (1) strict grounding in authentic daily activities, and (2) challenging query design that necessitates more than surface-level perception. Instead of simple recognition, our questions compel MLLMs to actively explore suitable visual clues and leverage them for subsequent reasoning. To this end, we curate a comprehensive dataset spanning four major daily domains and 16 distinct subtasks. Comprehensive evaluation across MLLMs and agentic models underscores the formidable challenge posed by our benchmark. Our analysis reveals several critical insights, emphasizing that the accurate identification of visual clues is essential for robust reasoning.

---


### 105. [Decoding the Delta: Unifying Remote Sensing Change Detection and Understanding with Multimodal Large Language Models](https://arxiv.org/abs/2604.14044)

**<font color=#1a73e8>作者：</font>** Xiaohe Li, Jiahao Li, Kaixin Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) excel in general vision-language tasks, their application to remote sensing change understanding is hindered by a fundamental "temporal blindness". Existing architectures lack intrinsic mechanisms for multi-temporal contrastive reasoning and struggle with precise spatial grounding. To address this, we first introduce Delta-QA, a comprehensive benchmark comprising 180k visual question-answering samples. Delta-QA unifies pixel-level segmentation and visual question answering across bi- and tri-temporal scenarios, structuring change interpretation into four progressive cognitive dimensions. Methodologically, we propose Delta-LLaVA, a novel MLLM framework explicitly tailored for multi-temporal remote sensing interpretation. It overcomes the limitations of naive feature concatenation through three core innovations: a Change-Enhanced Attention module that systematically isolates and amplifies visual differences, a Change-SEG module utilizing Change Prior Embedding to extract differentiable difference features as input for the LLM, and Local Causal Attention to prevent cross-temporal contextual leakage. Extensive experiments demonstrate that Delta-LLaVA decisively outperforms leading generalist MLLMs and specialized segmentation models in complex change deduction and high-precision boundary localization, establishing a unified framework for earth observation intelligence.

---


### 106. [Towards Unconstrained Human-Object Interaction](https://arxiv.org/abs/2604.14069)

**<font color=#1a73e8>作者：</font>** Francesco Tonini, Alessandro Conti, Lorenzo Vaquero 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-Object Interaction (HOI) detection is a longstanding computer vision problem concerned with predicting the interaction between humans and objects. Current HOI models rely on a vocabulary of interactions at training and inference time, limiting their applicability to static environments. With the advent of Multimodal Large Language Models (MLLMs), it has become feasible to explore more flexible paradigms for interaction recognition. In this work, we revisit HOI detection through the lens of MLLMs and apply them to in-the-wild HOI detection. We define the Unconstrained HOI (U-HOI) task, a novel HOI domain that removes the requirement for a predefined list of interactions at both training and inference. We evaluate a range of MLLMs on this setting and introduce a pipeline that includes test-time inference and language-to-graph conversion to extract structured interactions from free-form text. Our findings highlight the limitations of current HOI detectors and the value of MLLMs for U-HOI. Code will be available at this https URL

---


### 107. [Training-Free Semantic Multi-Object Tracking with Vision-Language Models](https://arxiv.org/abs/2604.14074)

**<font color=#1a73e8>作者：</font>** Laurence Bonat, Francesco Tonini, Elisa Ricci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic Multi-Object Tracking (SMOT) extends multi-object tracking with semantic outputs such as video summaries, instance-level captions, and interaction labels, aiming to move from trajectories to human-interpretable descriptions of dynamic scenes. Existing SMOT systems are trained end-to-end, coupling progress to expensive supervision, limiting the ability to rapidly adapt to new foundation models and new interactions. We propose TF-SMOT, a training-free SMOT pipeline that composes pretrained components for detection, mask-based tracking, and video-language generation. TF-SMOT combines D-FINE and the promptable SAM2 segmentation tracker to produce temporally consistent tracklets, uses contour grounding to generate video summaries and instance captions with InternVideo2.5, and aligns extracted interaction predicates to BenSMOT WordNet synsets via gloss-based semantic retrieval with LLM disambiguation. On BenSMOT, TF-SMOT achieves state-of-the-art tracking performance within the SMOT setting and improves summary and caption quality compared to prior art. Interaction recognition, however, remains challenging under strict exact-match evaluation on the fine-grained and long-tailed WordNet label space; our analysis and ablations indicate that semantic overlap and label granularity substantially affect measured performance.

---


### 108. [Interpretable Stylistic Variation in Human and LLM Writing Across Genres, Models, and Decoding Strategies](https://arxiv.org/abs/2604.14111)

**<font color=#1a73e8>作者：</font>** Swati Rallapalli, Shannon Gallagher, Ronald Yurko 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are now capable of generating highly fluent, human-like text. They enable many applications, but also raise concerns such as large scale spam, phishing, or academic misuse. While much work has focused on detecting LLM-generated text, only limited work has gone into understanding the stylistic differences between human-written and machine-generated text. In this work, we perform a large scale analysis of stylistic variation across human-written text and outputs from 11 LLMs spanning 8 different genres and 4 decoding strategies using Douglas Biber's set of lexicogrammatical and functional features. Our findings reveal insights that can guide intentional LLM usage. First, key linguistic differentiators of LLM-generated text seem robust to generation conditions (e.g., prompt settings to nudge them to generate human-like text, or availability of human-written text to continue the style); second, genre exerts a stronger influence on stylistic features than the source itself; third, chat variants of the models generally appear to be clustered together in stylistic space, and finally, model has a larger effect on the style than decoding strategy, with some exceptions. These results highlight the relative importance of model and genre over prompting and decoding strategies in shaping the stylistic behavior of machine-generated text.

---


### 109. [TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration](https://arxiv.org/abs/2604.14116)

**<font color=#1a73e8>作者：</font>** Zerun Ma, Guoqiang Wang, Xinchen Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have empowered AI research agents to perform isolated scientific tasks, automating complex, real-world workflows, such as LLM training, remains a significant challenge. In this paper, we introduce TREX, a multi-agent system that automates the entire LLM training life-cycle. By orchestrating collaboration between two core modules-the Researcher and the Executor-the system seamlessly performs requirement analysis, open-domain literature and data research, formulation of training strategies, preparation of data recipes, and model training and evaluation. The multi-round experimental process is modeled as a search tree, enabling the system to efficiently plan exploration paths, reuse historical results, and distill high-level insights from iterative trials. To evaluate the capability of automated LLM training, we construct FT-Bench, a benchmark comprising 10 tasks derived from real-world scenarios, ranging from optimizing fundamental model capabilities to enhancing performance on domain-specific tasks. Experimental results demonstrate that the TREX agent consistently optimizes model performance on target tasks.

---


### 110. [Rhetorical Questions in LLM Representations: A Linear Probing Study](https://arxiv.org/abs/2604.14128)

**<font color=#1a73e8>作者：</font>** Louie Hong Yao, Vishesh Anand, Yuan Zhuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rhetorical questions are asked not to seek information but to persuade or signal stance. How large language models internally represent them remains unclear. We analyze rhetorical questions in LLM representations using linear probes on two social-media datasets with different discourse contexts, and find that rhetorical signals emerge early and are most stably captured by last-token representations. Rhetorical questions are linearly separable from information-seeking questions within datasets, and remain detectable under cross-dataset transfer, reaching AUROC around 0.7-0.8. However, we demonstrate that transferability does not simply imply a shared representation. Probes trained on different datasets produce different rankings when applied to the same target corpus, with overlap among the top-ranked instances often below 0.2. Qualitative analysis shows that these divergences correspond to distinct rhetorical phenomena: some probes capture discourse-level rhetorical stance embedded in extended argumentation, while others emphasize localized, syntax-driven interrogative acts. Together, these findings suggest that rhetorical questions in LLM representations are encoded by multiple linear directions emphasizing different cues, rather than a single shared direction.

---


### 111. [Don't Let the Video Speak: Audio-Contrastive Preference Optimization for Audio-Visual Language Models](https://arxiv.org/abs/2604.14129)

**<font color=#1a73e8>作者：</font>** Ami Baid, Zihui Xue, Kristen Grauman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Audio-Visual Language Models (AVLMs) have achieved remarkable progress over recent years, their reliability is bottlenecked by cross-modal hallucination. A particularly pervasive manifestation is video-driven audio hallucination: models routinely exploit visual shortcuts to hallucinate expected sounds, discarding true auditory evidence. To counteract this deeply ingrained visual dominance, we propose Audio-Contrastive Preference Optimization (ACPO). This dual-axis preference learning framework introduces an output-contrastive objective to penalize visual descriptions masquerading as audio facts, alongside an input-contrastive objective that swaps audio tracks to explicitly penalize generation invariant to the true auditory signal. Extensive experiments demonstrate that ACPO establishes highly faithful audio grounding and mitigates audio hallucination without compromising overarching multimodal capabilities.

---


### 112. [From Feelings to Metrics: Understanding and Formalizing How Users Vibe-Test LLMs](https://arxiv.org/abs/2604.14137)

**<font color=#1a73e8>作者：</font>** Itay Itzhak, Eliya Habba, Gabriel Stanovsky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating LLMs is challenging, as benchmark scores often fail to capture models' real-world usefulness. Instead, users often rely on ``vibe-testing'': informal experience-based evaluation, such as comparing models on coding tasks related to their own workflow. While prevalent, vibe-testing is often too ad hoc and unstructured to analyze or reproduce at scale. In this work, we study how vibe-testing works in practice and then formalize it to support systematic analysis. We first analyze two empirical resources: (1) a survey of user evaluation practices, and (2) a collection of in-the-wild model comparison reports from blogs and social media. Based on these resources, we formalize vibe-testing as a two-part process: users personalize both what they test and how they judge responses. We then introduce a proof-of-concept evaluation pipeline that follows this formulation by generating personalized prompts and comparing model outputs using user-aware subjective criteria. In experiments on coding benchmarks, we find that combining personalized prompts and user-aware evaluation can change which model is preferred, reflecting the role of vibe-testing in practice. These findings suggest that formalized vibe-testing can serve as a useful approach for bridging benchmark scores and real-world experience.

---


### 113. [From $P(y|x)$ to $P(y)$: Investigating Reinforcement Learning in Pre-train Space](https://arxiv.org/abs/2604.14142)

**<font color=#1a73e8>作者：</font>** Yuqiao Tan, Minzheng Wang, Bo Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base model's existing output distribution. Optimizing the marginal distribution P(y) in the Pre-train Space addresses this bottleneck by encoding reasoning ability and preserving broad exploration capacity. Yet, conventional pre-training relies on static corpora for passive learning, leading to a distribution shift that hinders targeted reasoning enhancement. In this paper, we introduce PreRL (Pre-train Space RL), which applies reward-driven online updates directly to P(y). We theoretically and empirically validate the strong gradient alignment between log P(y) and log P(y|x), establishing PreRL as a viable surrogate for standard RL. Furthermore, we uncover a critical mechanism: Negative Sample Reinforcement (NSR) within PreRL serves as an exceptionally effective driver for reasoning. NSR-PreRL rapidly prunes incorrect reasoning spaces while stimulating endogenous reflective behaviors, increasing transition and reflection thoughts by 14.89x and 6.54x, respectively. Leveraging these insights, we propose Dual Space RL (DSRL), a Policy Reincarnation strategy that initializes models with NSR-PreRL to expand the reasoning horizon before transitioning to standard RL for fine-grained optimization. Extensive experiments demonstrate that DSRL consistently outperforms strong baselines, proving that pre-train space pruning effectively steers the policy toward a refined correct reasoning subspace.

---


### 114. [ROSE: Retrieval-Oriented Segmentation Enhancement](https://arxiv.org/abs/2604.14147)

**<font color=#1a73e8>作者：</font>** Song Tang, Guangquan Jie, Henghui Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing segmentation models based on multimodal large language models (MLLMs), such as LISA, often struggle with novel or emerging entities due to their inability to incorporate up-to-date knowledge. To address this challenge, we introduce the Novel Emerging Segmentation Task (NEST), which focuses on segmenting (i) novel entities that MLLMs fail to recognize due to their absence from training data, and (ii) emerging entities that exist within the model's knowledge but demand up-to-date external information for accurate recognition. To support the study of NEST, we construct a NEST benchmark using an automated pipeline that generates news-related data samples for comprehensive evaluation. Additionally, we propose ROSE: Retrieval-Oriented Segmentation Enhancement, a plug-and-play framework designed to augment any MLLM-based segmentation model. ROSE comprises four key components. First, an Internet Retrieval-Augmented Generation module is introduced to employ user-provided multimodal inputs to retrieve real-time web information. Then, a Textual Prompt Enhancer enriches the model with up-to-date information and rich background knowledge, improving the model's perception ability for emerging entities. Furthermore, a Visual Prompt Enhancer is proposed to compensate for MLLMs' lack of exposure to novel entities by leveraging internet-sourced images. To maintain efficiency, a WebSense module is introduced to intelligently decide when to invoke retrieval mechanisms based on user input. Experimental results demonstrate that ROSE significantly boosts performance on the NEST benchmark, outperforming a strong Gemini-2.0 Flash-based retrieval baseline by 19.2 in gIoU.

---


### 115. [One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding](https://arxiv.org/abs/2604.14149)

**<font color=#1a73e8>作者：</font>** Zheyu Zhang, Ziqi Pang, Shixing Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding is inherently challenging for vision-language models (VLMs) because of the extensive number of frames. With each video frame typically expanding into tens or hundreds of tokens, the limited context length of large language models (LLMs) forces the VLMs to perceive the frames sparsely and lose temporal information. To address this, we explore extreme video token compression towards \emph{one token per frame} at the final LLM layer. Our key insight is that heuristic-based compression, widely adopted by previous methods, is prone to information loss, and this necessitates supervising LLM layers into \emph{learnable} and \emph{progressive} modules for \emph{token-level compression} (LP-Comp). Such compression enables our VLM to digest 2x-4x more frames with improved performance. To further increase the token efficiency, we investigate \emph{frame-level compression}, which selects the frames most relevant to the queries via the internal attention scores of the LLM layers, named \emph{question-conditioned compression} (QC-Comp). As a notable distinction from previous studies, we mitigate the position bias of LLM attention in long contexts, \emph{i.e.}, the over-concentration on the beginning and end of a sequence, by splitting long videos into short segments and employing local attention. Collectively, our combined \emph{token-level} and \emph{frame-level} leads to an e\textbf{x}treme compression model for long video understanding, named \textbf{\name}, achieving a significantly larger compression ratio and enabling denser frame sampling. Our \name is finetuned from VideoChat-Flash with a data-efficient \emph{supervised compression tuning} stage that only requires 2.5\% of the supervised fine-tuning data, yet boosts the accuracy from 42.9\% to 46.2\% on LVBench and enhances multiple other long video benchmarks.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
