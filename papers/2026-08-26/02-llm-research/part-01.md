# 🧠 大模型相关研究 | 2026年08月26日

> 本类共 **363** 篇论文：已确认 **347** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-363](./part-08.md)

---

### 1. [KVBoost: Chunk-Level Key-Value Cache Reuse with Deviation-Guided Recomputation for Efficient Large Language Model Inference](https://arxiv.org/abs/2608.21362)

**<font color=#1a73e8>作者：</font>** Srihari Unnikrishnan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer-based large language models (LLMs) incur high prefill latency because key-value (KV) tensors must be recomputed for each request. Existing prefix-caching systems reduce this cost but require prompts to share a leading contiguous prefix, limiting effectiveness when shared content appears at arbitrary positions. We present KVBoost, a chunk-level KV cache reuse system for HuggingFace-compatible decoder models that enables reuse regardless of content position. KVBoost introduces a dual-hash keying scheme that separates positional identity (prefix hash) from content identity (content hash), supporting both exact and approximate cache matches. To address attention boundary errors from independently cached chunks, KVBoost employs two repair strategies: SelectiveRecompute, which re-encodes boundary regions, and CacheBlendRecompute, which identifies and recomputes high-deviation tokens after a probe pass. The system further incorporates asymmetric KV quantization (int8/int4), adaptive chunk boundary splitting, and importance-weighted eviction under a fixed memory budget. Evaluated on Qwen/Qwen2.5-3B over 1,000 bug-localization samples, KVBoost achieves a 4.49x reduction in time-to-first-token (142.4 ms vs.\ 639.1 ms) and outperforms prefix caching by 16%, with no loss in accuracy (99.2% vs.\ 99.1%). KVBoost provides a practical, memory-bounded inference acceleration layer compatible with RoPE-based models without architectural modification.

---


### 2. [KSE-Web: An Analysis of Hybrid Retrieval and LLM-Assisted Query Expansion for Low-Resource Khmer Semantic Search](https://arxiv.org/abs/2608.21365)

**<font color=#1a73e8>作者：</font>** Nimol Thuon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As a low-resource language, Khmer presents several retrieval challenges, including limited annotated data, ambiguous word boundaries, weak support in multilingual embedding models, and frequent mixed Khmer-English usage. This paper presents KSE-Web, an analysis of hybrid retrieval and LLM-assisted query expansion for Khmer semantic search. We construct the dataset from approximately 17K candidate Khmer titles and retain 3K cleaned full-text Khmer documents after filtering, normalization, deduplication, and document-length control. The dataset includes 300 manually reviewed user-style Khmer search queries and silver relevance labels with partial human verification. We evaluate character n-gram BM25, multilingual dense retrieval, hybrid BM25+dense retrieval, and LLM-assisted query expansion using Qwen2.5 models. Experimental results show that BM25 achieves the strongest overall performance, reaching 0.943 Recall and 0.876 nDCG. Hybrid BM25+dense retrieval performs comparably, achieving 0.929 Recall and 0.871 nDCG, while dense retrieval alone performs lower. LLM-assisted query expansion does not outperform non-expanded retrieval; however, Qwen2.5-3B produces substantially stronger expanded-query results than Qwen2.5-0.5B, suggesting that LLM size and expansion quality matter for low-resource Khmer retrieval. Our analysis further shows that direct LLM expansion can introduce topic drift, generic terms, and noisy reformulations, while simple filtering may remove useful semantic cues. These findings highlight both the potential and limitations of LLM-assisted retrieval for Khmer semantic search and provide a foundation for future Khmer retrieval datasets with stronger human-verified annotations and Khmer-aware retrieval models. The dataset and documentation will be made available at this http URL.

---


### 3. [Reviewing Model Collapse and Countermeasures](https://arxiv.org/abs/2608.21366)

**<font color=#1a73e8>作者：</font>** Xihao Xie, Beichen Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Driven by massive amounts of web-scale data, generative AI (GenAI) has achieved remarkable progress, enabling various applications in diverse sectors. The advances of GenAI have actuated practitioners to use AI-synthesized data for training next-generation AI models. Undeniably, using synthetic data has alleviated the increasing stringent demand for data supply. Unfortunately, it also introduces a new critical issue: in a self-consuming cycle between model and data, the model ultimately collapse, raising more trustworthiness concerns to GenAI. In recent years, increasingly more studies have investigated the phenomenon of model collapse (MC) and explored potential solutions to mitigate it. However, the review of the phenomenon of MC still remains blank. To fill this gap, this paper provides an up-to-date overview of these studies for consolidating and reviewing the progress of MC in different application scenarios and countermeasures for mitigating MC. We also highlight challenges and future research opportunities.

---


### 4. [Wazobia Eval: A Benchmark for Nigerian Pidgin Emotion Understanding, Sarcasm Detection, and Cultural Reasoning](https://arxiv.org/abs/2608.21369)

**<font color=#1a73e8>作者：</font>** Stephanie Okoye  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nigerian Pidgin is one of Africa's most widely spoken languages, yet remains severely underrepresented in language model evaluation. Existing benchmarks primarily focus on translation, transcription, or generic sentiment analysis, leaving critical aspects of culturally grounded language understanding unmeasured. We introduce Wazobia Eval, a benchmark for evaluating Nigerian Pidgin emotion understanding, sarcasm detection, and cultural reasoning. The benchmark is built on a manually annotated dataset containing over 550 examples and a 16-category emotion taxonomy designed to capture culturally specific emotional registers that are not represented in conventional sentiment frameworks. Wazobia Eval provides standardized evaluation protocols and benchmark tasks for assessing model performance on nuanced Nigerian language understanding. We present the benchmark design, annotation methodology, taxonomy development process, and preliminary pilot evaluation results. Our goal is to provide foundational evaluation infrastructure for Nigerian language AI and establish a reproducible benchmark for future research. The dataset is publicly available at this https URL.

---


### 5. [LitReview Arena: Evaluating Literature Review Agents with Battle-Style Peer Review Platform](https://arxiv.org/abs/2608.21374)

**<font color=#1a73e8>作者：</font>** Ruotong Zhao, Zhiyu Chen, Xurui Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Literature reviews are essential to scientific progress, but rigorously evaluating automatically generated reviews remains difficult because many aspects of research utility depend on expert judgment rather than reference-overlap metrics. We introduce LitReview Arena, a battle-style evaluation platform with a structured protocol tailored to literature review quality: domain experts with AI paper-writing experience compare anonymized drafts, are matched to topics within their expertise, and provide dimension-wise outcomes over five literature-review-specific criteria. From this protocol, we collect approximately 3k expert judgments, each containing five dimension-wise outcomes, and show that even the strongest current systems win only 23.0% of decisive matches against human drafts on overall utility, while agentic LLMs such as Sonar Deep Research substantially outperform base language models by over 60%. We further find that existing LLM-as-a-judge methods are substantially misaligned with human experts (Spearman's rho=0.467), especially on synthesis-heavy criteria such as paper structure and research suggestions. Using the collected preference data, we provide an expert-calibrated evaluator, LitJudge, which improves alignment to Spearman's rho=0.78, comparable to inter-expert consistency; code and data are publicly available at this https URL.

---


### 6. [SchemaRouter: Field-Aware Tool Routing for Efficient Heterogeneous Agentic RAG](https://arxiv.org/abs/2608.21375)

**<font color=#1a73e8>作者：</font>** Yong-eun Cho  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heterogeneous agentic retrieval-augmented generation (RAG) systems increasingly orchestrate external APIs, internal databases, vector stores, and graph stores. Exposing all tool descriptions to an LLM agent, or selecting tools only by vector similarity, causes two costly failures: over-fetching, which increases payload size, token use, and latency, and under-fetching, which omits fields needed to answer the query.
We present SchemaRouter, a lightweight routing layer that represents tools, endpoints, parameters, response fields, domain concepts, units, provenance, and license policies as a schema graph. Given a query, SchemaRouter emits an executable tool plan specifying which tools to call and which fields to retrieve. A small LLM extracts intent, concepts, and source constraints, while field selection is deterministic over the graph through intent-group projection and concept-field matching with an alias layer.
On a materials-science benchmark of 110 queries, SchemaRouter achieves answer accuracy of 0.71, matching fetch-everything within overlapping confidence intervals and exceeding prompt-all's 0.66, though their intervals overlap. It uses 227 retrieved-context tokens versus 2,066 for fetch-everything and achieves 2.7x lower end-to-end latency than prompt-all. It also obtains the best tool-exact rate of 0.93 and parameter validity of 1.0. SchemaRouter grounds provenance and license information in 62 percent of answers, compared with approximately 0 percent for all baselines.
We also find that minimizing selected-field count is counterproductive: it reduces answer accuracy to 0.56 with negligible token savings, while recall-preserving projection restores top accuracy. SchemaRouter improves efficiency, schema-size-independent scaling, and verifiable provenance/license-grounded answering at competitive accuracy.

---


### 7. [On the Role of Citations in Preference Data](https://arxiv.org/abs/2608.21376)

**<font color=#1a73e8>作者：</font>** Yu Hou, Hal Daumé III, Rachel Rudinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many NLP tasks require systems to provide attribution in their outputs--i.e. citations to grounding sources. Attribution serves as a bulwark against model hallucination and as a means for users to verify the credibility of model outputs. Yet, it is unclear how humans and LLMs evaluate citations when comparing outputs, a process central to reward modeling and modern LLM post-training. This paper studies the role of citations in the preferences of human judges and four open-source LLMs within the context of scientific question answering, leveraging mixed effects models to investigate the influence of citations on pairwise judgments. Among our key findings are (1) that humans prefer more diverse citations but fewer overall, and (2) that LLMs show some citation-related preferences compared to humans, despite lacking access to the sources, but these preferences depend on the data and specific models. We further discuss the implications of our findings for preference data collection.

---


### 8. [Agentic Scaffolding Amplifies Sycophantic Behavior in Large Language Models](https://arxiv.org/abs/2608.21377)

**<font color=#1a73e8>作者：</font>** Thantham Jittham  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sycophancy in large language models, the tendency to prioritize user agreement over truthful responses, has been documented extensively but studied primarily in single-turn settings. This paper investigates a critical question: does subjecting LLMs to greater interaction scaffolding make sycophancy better or worse? Across 4,800 veracity judgments (200 statements $\times$ 6 models $\times$ 4 conditions), we find that the interaction scaffolding characteristic of agentic systems (feedback loops, reconsideration checkpoints, and iterative refinement) systematically amplifies sycophantic behavior. Multi-turn interaction, user pressure, and iterative self-refinement each provide additional opportunities for models to drift toward agreement, and this drift coincides with a mean accuracy drop of $-6.3$ percentage points, establishing the capitulation as harmful rather than corrective. More capable models show larger amplification effects, a troubling inversion of expectations. We introduce the concept of agentic sycophancy amplification (ASA) and two novel metrics: capitulation rate and sycophantic capitulation rate. Our results indicate that as AI systems acquire greater autonomy, sycophancy becomes compounding rather than merely persistent. Systems designed with human oversight loops may inadvertently create the conditions for this drift.

---


### 9. [RIACT: A Responsible AI System for Personalized Study Habit Tracking and Early Burnout Signal Detection in University Students](https://arxiv.org/abs/2608.21379)

**<font color=#1a73e8>作者：</font>** Ria Sidhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Student burnout is highly prevalent in higher education, with reported rates ranging from 12% to over 70% and consistently exceeding those of the working population - yet it is typically identified only retrospectively, after academic decline has already occurred. A contributing factor is that students have little structured visibility into their own study behaviour, and existing productivity tools record activity without interpreting it. This paper presents RIACT (Record, Insight, Analyze, Coach, Track), a web-based application that combines structured study session logging with a hybrid AI architecture to surface personalized insights and early burnout signals. Students log sessions by location and time; the system computes net focus time by accounting for breaks, detects burnout signals through transparent, deterministic rules operating on week-over-week behavioural comparisons, and uses a large language model - constrained to a fixed output schema - to contextualize patterns and generate personalized recommendations. The design embeds responsible AI principles throughout: warnings are governed by auditable rules rather than model judgement, all output is framed as an observation rather than a diagnosis and data collection is limited to self-logged behavioural fields. We describe the system's design rationale, situate it within the literature on student burnout and explainable AI in education and propose an evaluation framework for validating its behavioural signals against established burnout instruments.

---


### 10. [There Is No Neutral Harness: Modern LLM Leaderboards Are Manufactured by Config-Fragile Items](https://arxiv.org/abs/2608.21382)

**<font color=#1a73e8>作者：</font>** V.S. Raghu Parupudi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multiple-choice benchmarks fix the questions and the correct answers, but not the harness: the order of the options, the wording of the prompt, and whether a language model's answer is read from generated text or from per-option likelihoods. Work on this harness sensitivity reports it as aggregate score variance, leaving unexamined which items the variance falls on and whether they are the items that separate one model from the next. We treat the evaluation harness of large language models (LLMs) as an independent variable and resolve its effect to single items. We introduce the \textit{fragility grid}: 12 open-weight instruction-tuned LLMs from 4 families answer the same 3{,}679 items from 4 benchmarks (ARC, HellaSwag, MMLU, TruthfulQA) under 26 equally defensible harness configurations, recording one correctness bit for every model, item, and configuration. The comparison is matched, since the items, the weights, and the greedy decoding stay fixed while only the harness varies. Under the grid a model's score is a band rather than a point: gemma4-31b scores between 31 and 89 percent depending only on the harness. Three results follow. On the items that two adjacent models both answer stably the pair is tied, and config-fragile items carry 95.7 percent of a pair's gap on average. Four of the 12 models reach rank one under some configuration, so the harness selects the winner. Item discrimination, the property that benchmark-compression methods maximize, correlates with fragility at 0.28 (95 percent CI 0.25 to 0.30), so compression keeps the fragile items rather than removing them. The scoring choice, not the option order that protocols usually fix, is the load-bearing axis. We release the per-item records and the analysis script, from which every number regenerates on a CPU in seconds, and we position the fragility grid as a check a leaderboard can run before it reports an order.

---


### 11. [Spyre-Accelerated Retrieval-Augmented Generation on IBM LinuxONE: A Cloud-Native Architecture for Secure, High-Throughput Enterprise AI Inference](https://arxiv.org/abs/2608.21393)

**<font color=#1a73e8>作者：</font>** Sandeep Bokkasam, Pankaj D  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Running large language models inside enterprise environments has always bumped up against a practical wall: the data lives in one place, the AI horsepower sits somewhere else, and moving sensitive records between the two creates real headaches around latency, security, and regulatory exposure. IBM's Spyre accelerator PCIe inference card built for LinuxONE and the broader IBM Z family changes that equation.
In this paper we lay out a six-subsystem RAG architecture that runs entirely on IBM LinuxONE, using Spyre for generative inference, the Telum II on-chip accelerator for lightweight classification tasks, and Red Hat OpenShift for container orchestration. Every piece of the pipeline from query intake through vector retrieval, prompt assembly, LLM inference, compliance filtering, and response delivery stays within a single LinuxONE system, so sensitive data never has to leave the hardware perimeter.
We walk through the design choices behind each subsystem, dig into the Spyre compilation and serving stack, explain how LinuxONE's Secure Execution technology extends confidential-computing guarantees to AI workloads, and benchmark the architecture against cloud-GPU and on-premises alternatives. Early analysis points to end-to-end RAG latencies under two seconds and up to a 20x reduction compared to off-platform inference, all while keeping the strong encryption and auditability posture that regulated industries actually need.

---


### 12. [Hate Speech Classification In Roman Urdu: A Comparative Study On Parameter Efficient Fine-Tuning And Prompt Engineering](https://arxiv.org/abs/2608.21408)

**<font color=#1a73e8>作者：</font>** Toneema Zubair  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Due to the widespread accessibility of the internet and social media, toxic and hateful con-tent has grown exponentially, causing significant distress and negative societal impacts. Ro-man Urdu, a low-resource language used in Pakistan and among Urdu-speaking communities worldwide, presents additional challenges because of its informal grammar, inconsistent sen-tence structures, and multiple variations in word spellings. This research aims to identify the most effective techniques for hate speech classification in such low-resource settings with limited data. To address this, the study investigates and compares the latest approaches, in-cluding prompt tuning, parameter-efficient fine-tuning (PEFT) using LoRA, and prompt en-gineering, under various experimental configurations. To achieve this objective, four exper-iments were designed. The first experiment involved direct inferencing with LLMs without any fine-tuning, to evaluate how well these models understand Roman Urdu in a zero-shot setting, especially given limited data. The second experiment utilized parameter-efficient fine-tuning (PEFT) with LoRA, which updates only a small subset of parameters, thereby reducing computational cost. The third experiment explored prompt tuning with both mixed and manually crafted prompts, using very small sets of training examples relative to the entire dataset, making it computationally efficient as well. Finally, the fourth experiment applied prompt engineering through zero-shot and few-shot learning, relying solely on care-fully designed instruction prompts for classification without further training.

---


### 13. [Mitigating Bias in Large Vision-Language Models via Counterfactual Ensemble Decoding](https://arxiv.org/abs/2608.21415)

**<font color=#1a73e8>作者：</font>** Yisong Xiao, Aishan Liu, Yongxin Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved remarkable performance across a wide range of tasks; however, they often inherit social biases from their training data, resulting in biased behavior when processing portraits from different social groups. Existing debiasing approaches typically compare token probabilities between the original and biased generations during decoding, but they are fundamentally limited by their reliance on a single, stereotyped viewpoint and fail to account for the diversity of social perspectives. Inspired by the social science principle that diversity fosters fairness, we propose Counterfactual Ensemble Decoding (CED), a novel framework that constructs multi-group counterfactual perspectives within the visual representation space and integrates them during decoding to promote equitable model behavior. CED first performs counterfactual steering in the visual space by identifying semantic directions associated with each social group and generating counterfactual representations along these directions, thereby offering diverse perspectives that disrupt stereotypical narratives. During decoding, CED locates the decoder layer exhibiting the greatest divergence among these perspectives and ensembles their token distributions using uncertainty-aware weights, prioritizing high-confidence tokens from different groups to yield a more balanced probability distribution that guides fairer generation. Extensive experiments on three social bias evaluation benchmarks demonstrate that \tool achieves substantial improvements over leading baselines, reducing bias by up to 47.97% across scenarios involving occupations, descriptors, and persona traits. Moreover, CED also preserves the core capabilities of the original model with minimal degradation.

---


### 14. [Retrieval-grounded robot program generation and simulation-based correction via Model Context Protocol](https://arxiv.org/abs/2608.21417)

**<font color=#1a73e8>作者：</font>** Zhichao Zhou, Siyuan Chen, Omkar Salunkhe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flexible manufacturing requires industrial robots to be reprogrammed rapidly as product variants change. This paper presents a language-model-based workflow that generates, validates, and iteratively corrects ABB RAPID robot programs from natural language task descriptions. A dual-stream retrieval-augmented generation (RAG) pipeline grounds code generation in verified technical documentation and production templates, reducing domain-specific errors produced by ungrounded language models. A custom Model Context Protocol (MCP) server connects the language-model client directly to ABB RobotStudio for automated code upload, simulation execution, and diagnostic feedback. The evaluation combines a 30-query retrieval benchmark, scoped code-generation checks, and RobotStudio case studies in a simulated pickand- place manufacturing cell. The simulation loop exposes execution failures that static and semantic checks alone cannot catch, including suction release-height errors, unreachable placement targets, and configuration-dependent recovery motions. The results show how RAG and MCP can connect grounded code generation with executable feedback from industrial robot simulation software, while reducing but not eliminating expert setup and final supervision.

---


### 15. [Agentic Security: A Systematization of Tools, Failure Modes, and Design Laws for LLM-Driven Penetration Testing](https://arxiv.org/abs/2608.21423)

**<font color=#1a73e8>作者：</font>** Israt Moyeen Noumi, Tarannum Ahmed Nowshin, Md. Mehedi Hasan Nipu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic security uses large-language-model (LLM) agents to plan, dispatch, and interpret security tools. As these systems move from demonstrations to deployed products, practitioners repeatedly encounter the same operational failures. We systematize these failures through a hands-on evaluation of ten widely used static, dynamic, cloud, orchestration, and AI red-teaming tools for unattended pipelines. We introduce a four-dimensional Integration Friction Index that separates one-time engineering cost from recurring organisational, legal, and maintenance cost. We then derive quantitative regularities that explain recurring failure modes. Modelling an agentic security system as stochastic LLM policies wrapped by a deterministic mediator, we show that long-lived sessions lose resident evidence with phase count, while short-lived sub-agents extend the usable horizon according to the compression ratio between raw evidence and its summary. We show that a two-stage verdict cascade multiplies scorer likelihood ratios, but provides little benefit when scorer errors correlate. We show that treating unevaluable outcomes as attack failures biases downstream measurements toward evasive and severe responses. We formulate planner-versus-worker model routing as a knapsack problem and derive a closed-form execution cap for heavy-tailed tools, eta* = alpha v/c. Finally, we show why scope and budget enforcement cannot be delegated to system prompts: prompts do not constrain what actually executes. Inspectra, our implemented platform, serves as a worked instantiation, with mechanisms labelled shipped, partial, or planned, including those that did not work.

---


### 16. [Evaluating Multimodal Narrative Understanding of Popular Hollywood Films](https://arxiv.org/abs/2608.21430)

**<font color=#1a73e8>作者：</font>** David Bamman, Kent K. Chang, Allison Cooper 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal language models increasingly show promise for enabling the large-scale computational analysis of film, opening up new avenues for learning about film history and the evolution of narrative techniques. But the creation of stable benchmarks built around Hollywood films is complicated by copyright protections. In this work, we address these concerns directly, by building a new collection of Hollywood films defined by two criteria: box office popularity (where we publish the first large-scale, open collection of weekly box office earnings reported by Variety magazine from 1922-1979); and likely public domain status (by researching copyright registrations and renewals in the US Catalog of Copyright Entries). We build a new multimodal MCQ benchmark on top of this collection that focuses on narrative elements that directly evaluate the abilities of models to inform meaningful research on film narrative; we find that many vision-language models struggle on this task (with many performing at near-chance levels of accuracy), while audio-visual models (including those that use audio in captioning scenes) reach a maximum accuracy of 61.1%, well below human-level performance.

---


### 17. [Boosting Knowledge-based Visual Question Answering with Structured Context Reasoning](https://arxiv.org/abs/2608.21431)

**<font color=#1a73e8>作者：</font>** Qiyou Liu, Yong Zhang, Jianjie Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge-based Visual Question Answering aims to answer questions about an image by integrating external knowledge with visual and textual information. Recent approaches often rely on in-context learning to prompt Large Language Models (LLMs) with multimodal context in a zero-shot or few-shot manner. However, we observe that directly concatenating heterogeneous visual descriptions and retrieved knowledge into long, unstructured prompts often degrades reasoning performance, due to both excessive irrelevant context and the lack of explicit relational structure. In this paper, we propose an LLM-based Structured Context Reasoning (SCoRe) framework that infers both explicit and implicit relationships for prediction. SCoRe consists of three stages: Context Acquisition, which generates diverse visual notes and retrieves explicit knowledge via an efficient two-stage multimodal retrieval strategy; Context Selection, which filters relevant visual, explicit, and implicit knowledge using LLM-guided selection; and Context Compression, which performs Relational Logic Distillation (RLD) to transform raw text into explicit entity-relation triplets. These relational triplets serve as a concise and structured prompt for final answer prediction. Extensive experiments on the OK-VQA and A-OKVQA benchmarks demonstrate that SCoRe consistently outperforms state-of-the-art methods.

---


### 18. [Agentic AI for Safety-critical Multi-drone Systems: Challenges and Opportunities](https://arxiv.org/abs/2608.21444)

**<font color=#1a73e8>作者：</font>** Timothy Merritt, Alejandro Jarabo-Peñas, Juan Bravo-Arrabal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-drone systems are increasingly positioned for safety-critical missions such as search and rescue (SAR) and critical infrastructure monitoring. Yet, real-world adoption remains constrained not only by autonomy performance, but by the difficulty of integrating agentic behavior into professional work: operators must understand, trust, and govern automation under uncertainty, time pressure, and accountability. This position paper synthesizes the ambitions and lessons from two ongoing efforts: NAMUR, which explores LLM-supported robot control in SAR and firefighting contexts, and PERSIST, which explores persistent drone operations for monitoring and security at critical infrastructure sites. We argue that agentic AI should be approached as a socio-technical design problem, where interfaces, oversight mechanisms, and evaluation practices are as critical as algorithms. We outline a human-centered, participatory, and iterative research approach aimed at uncovering stakeholder needs, shaping agent capabilities through successive prototypes, and producing transferable proof-of-concept systems and evaluation strategies for other safety-critical contexts.

---


### 19. [ViTexSZ: Heterogeneous Vision-Text Knowledge Distillation for EEG Seizure Detection](https://arxiv.org/abs/2608.21445)

**<font color=#1a73e8>作者：</font>** Chenxi Liu, Mingzhao Li, Yicong Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated seizure detection from electroencephalography (EEG) is essential for continuous neurological monitoring, particularly for subclinical epileptic seizures that may exhibit only subtle electrographic changes. Existing time-series methods are often designed for fixed EEG channel configurations, thereby limiting their applicability to heterogeneous EEG recordings with irregular channel layouts. Although visual and language modeling offer promising alternatives, aligning heterogeneous EEG representations with clinical semantics remains challenging. We introduce ViTexSZ, a heterogeneous Vision-Text knowledge distillation framework for EEG seizure detection. ViTexSZ converts EEG recordings into structured waveform images and introduces a query-based multi-channel alignment module that maps source-dependent visual features into a unified token space. A heterogeneous teacher further integrates the aligned EEG representations with clinical prompts through a multimodal large language model, associating high-level clinical semantics with seizure-related evidence. Vision-text knowledge distillation then transfers the teacher representations to a lightweight student during detection. Experiments on four EEG seizure datasets demonstrate the generalizability of ViTexSZ across both subclinical and general seizure detection scenarios, achieving the highest accuracy on all datasets and relative improvements of up to 12.9% over the second-best baselines, showing its effectiveness.

---


### 20. [BIMScript: Material-Aware Structured Scene Programs for BIM Ingestion](https://arxiv.org/abs/2608.21447)

**<font color=#1a73e8>作者：</font>** Prakash Kondibhau Naikade, Thomas B. Moeslund, Andreas Møgelmose  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured-language models such as SceneScript reconstruct a scene as a short program of parametric commands, an inherently editable and semantically explicit representation. We ask three questions that stand between such models and their most compelling application, automated ingestion of existing buildings into BIM tools, studied here on synthetic scans: \emph{what} is the scene made of, \emph{how fast} can it be produced, and \emph{exactly where} is each element. BIMScript answers all three within one grammar. First, we extend the layout language with per-element \emph{material} and \emph{condition} attributes, supervised by a vision-language-model material-passport corpus we build over 100k synthetic scenes (1.9M pseudo-labeled elements), and route image appearance to the material tokens through a lifted-feature point encoder. Second, we show that autoregressive decoding of these programs is dominated not by compute but by kernel-launch and host-synchronization overhead, and remove it with an output-exact CUDA-graph decoder (1.9 vs 6.4\,ms/step, $3.4\times$) plus a grammar-parallel, tolerance-verified draft-and-verify scheme that exploits the deterministic entity schema. Third, we address the model's 5cm token-grid granularity with training-free geometric snapping and a hybrid discrete--continuous decoder head that regresses a sub-bin offset, and measure how much of the residual error each recovers. Because each command maps one-to-one onto a native Revit object, we validate direct ingestion into a BIM authoring tool end to end with a working add-in and its IFC4 export, and the same program's language form is designed to support LLM-driven, sustainability-aware reasoning over the built asset.

---


### 21. [Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Question Answering](https://arxiv.org/abs/2608.21450)

**<font color=#1a73e8>作者：</font>** Hangrui Xu, Zhengxian Wu, Yunyao Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge-Based Visual Question Answering (KB-VQA) relies on retrieving external information to answer queries involving long-tail entities. However, existing retrieval pipelines predominantly employ CLIP-style dual encoders, which prioritize surface-level visual similarity over entity-level semantic alignment. This paradigm often fails when semantically identical concepts exhibit large visual variations or when distinct entities appear visually similar. To address this, we propose KBMR, the first MLLM-based embedding retriever tailored for KB-VQA. Leveraging the robust autoregressive capabilities of MLLMs, KBMR maps images into a semantic space that better preserves concept identity. To tackle the challenge of noisy supervision in Wikipedia-scale retrieval, we introduce an MLLM-based semantic discriminator that generates continuous entity-consistency weights. These weights guide a novel continuous semantic distillation objective, enabling effective hard negative sampling and soft supervision beyond rigid binary labels. Extensive experiments demonstrate that KBMR significantly outperforms CLIP baselines, yielding up to a 14.7% improvement in retrieval Recall@1 and a 9.4% gain in end-to-end VQA accuracy. Code is available at this https URL.

---


### 22. [FigmaTrace: Capturing Creative Nuances in Human Figma Design Workflows](https://arxiv.org/abs/2608.21460)

**<font color=#1a73e8>作者：</font>** Darshan Deshpande, Yoshinari Fujinuma, Martyna Markiewicz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models have recently shown improvements in several objective and verifiable domains such as object detection but continue to underperform on subjective and creative design tasks. A major contributor to this performance gap is the lack of high quality human workflow data that captures a diverse set of preferences and decisions that make human experts good at design tasks. In this work, we first define a unique, expert curated taxonomy of design skills and best practices which we further expand into a set of 126 open ended, subjective, long horizon tasks. Built on top of this and expert solutions, our dataset FigmaTrace contains over 200 hours of human captured video data converted into 3469 design trajectories using a novel design phase-based method. We use our dataset to train four models and show that training on FigmaTrace leads to a performance improvement comparable to frontier closed models such as \textsc{Claude-Opus-5} and \textsc{GPT-5.6-Sol} on four out of distribution agentic GUI environments. We further perform a useful ablation to attribute these performance improvements to a design phase-based video to trajectory conversion which outperforms prior length-based conversion approaches. Finally, we perform a qualitative analysis on the best performing \textsc{Qwen3.8-27B} outputs to better correlate performance improvements to FigmaTrace's trends. We open source our dataset and the best model for the community.

---


### 23. [CyrillicQA: The Influence of Phonetically Encoded Secret Language on LLM Performance](https://arxiv.org/abs/2608.21462)

**<font color=#1a73e8>作者：</font>** Erik Thureck, Leo S. Rdian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Due to the selection of their training data, large language models (LLMs) perform best on standard-language inputs from languages using the Latin alphabet with large speaker populations, while disadvantaging other language varieties. Nevertheless, they can also be a versatile tool for preserving precisely such endangered languages. But do they also possess the necessary creativity and capacity for abstraction to decode phonetically encoded language the same way humans do?

---


### 24. [Scalable PII Discovery in Mobile App Databases via Hypothesis-Driven Search](https://arxiv.org/abs/2608.21469)

**<font color=#1a73e8>作者：</font>** Jeel Piyushkumar Khatiwala, Samad Afolabi, Ruoyao Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Discovering personally identifiable information (PII) in mobile forensic databases is difficult because the relevant table-column regions are unknown, distributed across heterogeneous SQLite schemas, and may contain values embedded in free-text or semi-structured fields. We present a hypothesis-driven framework that treats PII localization as bounded, adaptive search under uncertainty. An agent ranks candidate table-column regions, probes sampled values, and maintains a memory of prior evidence, confidence scores, and decisions to refine subsequent hypotheses. The framework separates lightweight PII exploration from targeted extraction, normalization, and deduplication over validated regions, thereby limiting exhaustive inspection to regions supported by sampled evidence. We evaluate the framework on 25 SQLite databases from 10 Android and iOS applications in the Cellebrite CTF corpus, targeting email addresses, phone numbers, domain names, person names, and postal addresses. Against a corpus-level distinct ground-truth set of 3,751 entities, Gemini 2.5 Pro achieves 94.5% F1 while reducing the effective extraction search space by 79.9% on average. Results across 12 model backends show strong performance among several frontier models, but substantial sensitivity to model capability.

---


### 25. [Structural Inference in Undocumented Mobile Databases: A Reproducible Benchmark for Evaluating Agentic Reasoning in Digital Forensics](https://arxiv.org/abs/2608.21470)

**<font color=#1a73e8>作者：</font>** Jeel Piyushkumar Khatiwala, Divyangkumar Patel, Weifeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic large language models are increasingly used in digital forensic analysis, yet their ability to infer relational structure inside undocumented mobile application databases remains poorly understood. In forensic contexts, structurally incorrect inferences can yield results that appear plausible while remaining evidentially unsound. This work evaluates agentic structural inference as an isolated capability, treating execution success and structural correctness as distinct evaluation axes. It examines how an agent reconstructs table relationships, linking attributes, and executable join paths when given only a raw database and a natural-language investigative prompt. We apply a fixed, deterministic evaluation pipeline to two contrasting SQLite repositories: Android's SMS database with stable identifier propagation, and Snapchat's database with irregular schemas, ephemeral identifiers, and polymorphic relationships. Using expert-verified SQL ground truth, we evaluate (i) structural correctness of inferred relational links, (ii) execution coherence under multi-table reasoning, and (iii) robustness and failure modes of inferred structure when execution succeeds but relational interpretation diverges from expert ground truth. Evaluation is performed independently of semantic interpretation, with full queries and execution traces provided in the Appendix. Results show that structural inference remains reliable in regular schemas but degrades sharply as schema ambiguity increases, frequently producing structurally plausible yet incorrect joins that execute successfully. These findings clarify where schema-agnostic agentic reasoning can support forensic analysis, how its robustness degrades under realistic schema irregularities, and why additional verification remains essential before inferred relationships can be treated as reliable evidence.

---


### 26. [EXPL-FR: Explaining Face Recognition Models via Vision-Language Alignment](https://arxiv.org/abs/2608.21486)

**<font color=#1a73e8>作者：</font>** Guray Ozgur, Mustafa Efe Tamyapar, Naser Damer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep face recognition (FR) models reach near-saturated accuracy but remain opaque: a practitioner cannot ask which semantic attributes a similarity score relied upon. EXPL-FR answers this inside the FR model's own embedding space. A lightweight adapter aligns a vision-language model's (VLM) image encoder with the frozen FR space, trained on face images alone and never on text. Because the VLM's encoders share one space, the same adapter applies to the text encoder, turning 978 attribute prompts in 22 categories, also extendable, into FR-space anchors at no extra cost. We do not assume this transfer works: a face-verification protocol measures it, and an ablation changing only the adapter isolates its contribution. Not every concept survives, because an FR model earns its invariances by discarding the factors it must verify identities across. A label-free detectability measure compares each concept's separability in FR space against the VLM space, and the 100 most detectable form the model's readable semantic signature, which separates identities better than the full vocabulary. We cover four FR backbones and two VLM encoders, EXPL-FR needs no architecture access, and supports identity-level, per-image, and differential explanations. We benchmark attribute-level auditing under three supervision settings, human labels (current practice), VLM pseudo-labels, and our fully prompt-driven audit, against real verification behavior. With no labels, the prompt-driven audit ranks four FR models by their measured per-ethnicity RFW errors and ranks controlled attribute changes by their true verification cost.

---


### 27. [TASSO: TAsk-Specific Subspace Optimization for Continual Learning of Vision-Language Models](https://arxiv.org/abs/2608.21487)

**<font color=#1a73e8>作者：</font>** Chang Sun, Francesco Barbato, Matteo Caligiuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) exhibit strong zero-shot capabilities, making them an attractive solution for continual learning across diverse tasks. However, during continual adaptation, both catastrophic forgetting and zero-shot degradation occur, severely degrading performance. In this paper, we introduce TASSO, a new paradigm that efficiently preserves the latent space geometry while ensuring network plasticity. We achieve this with two complementary techniques: subspace learning and geometry-aware knowledge distillation. Specifically, we first learn a sequence of task-specific low-rank projectors, which we use to project the latent representations before optimizing cross-entropy. Secondly, we employ a geodesic-distance-based loss that distills knowledge from the previous-task model while effectively preserving the latent space geometry. These design choices not only avoid unnecessary parameter updates along the full embedding dimensions but also improve learning by focusing on task-specific manifolds. Moreover, the geometry-aware distillation provides strong regularization and significantly reduces both catastrophic forgetting and zero-shot degradation throughout the continual learning sequence. Experimental results with the CLIP vision language model in the multi-domain task incremental and class incremental learning benchmarks demonstrate clear improvements over state-of-the-art methods in mitigating forgetting and preserving zero-shot capabilities.

---


### 28. [Let Credit Follow Computation: Architecture-Aware Credit Transport for Large Language Model Reinforcement Learning](https://arxiv.org/abs/2608.21501)

**<font color=#1a73e8>作者：</font>** Qifan Shi, Zhaolu Kang, Chenghua Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Credit assignment in large-language-model reinforcement learning (LLM RL) can be separated into three objects: evidence about success, a transport operator that converts this evidence into token-level advantages, and an update geometry that turns advantages into policy changes. Recent work has greatly improved evidence, sampling, and update geometry, but the transport operator is usually architecture-agnostic. Fixed-discount GAE applies a stationary geometric kernel along token time; group-relative methods broadcast an outcome statistic across an entire response. Neither operator represents the trajectory-specific computation used by the Transformer policy itself. We introduce computation-conditioned credit transport (CCT), a general framework in which a detached statistic of the behavior policy's internal computation parameterizes the causal kernel that transports downstream value through a rollout. Our concrete algorithm, CompPO, maps native attention concentration to a bounded per-token retention gate, uses the gate in both the one-step bootstrap and a path-dependent generalized-advantage trace (Comp-GAE), and co-designs a transport-aligned critic (TAC) that reuses the actor's hidden states and routing information without a second same-scale Transformer. The task reward and clipped PPO policy objective remain unchanged; a constant gate recovers fixed-coefficient GAE. Across five Qwen3-4B seeds, CompPO reaches 61.4% final held-out accuracy (95% CI [60.8,62.0]) versus 53.8% [52.9,54.7] for tuned GRPO. Neither Comp-GAE with a standard critic (55.2%) nor TAC with a fixed gate (56.4%) matches the full model (interaction +2.4 [1.9,2.9]). Shuffle and position controls confirm trajectory-specific alignment; CompPO is stable in 10/12 PPO-grid runs versus 3/12. Frozen evaluation improves over GRPO by 4.3 and 3.9 greedy pass@1 macro points on Qwen3-4B and Llama-3.1-8B-Instruct.

---


### 29. [ChemDIRT: A Diversified Instruction, Representation, and Task Benchmark for Robust Chemistry-LLM Evaluation](https://arxiv.org/abs/2608.21504)

**<font color=#1a73e8>作者：</font>** Eric Inae, Tim Gunn, Chris Bond 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large language models (LLMs) has led to increasing interest in their application to scientific domains such as chemistry. However, existing chemistry benchmarks often provide only a narrow view of model capability, focusing on limited task sets while overlooking robustness to variations in problem formulation and chemical representation. As a result, reported performance may overestimate a model's true ability to reason consistently across realistic settings. To address this challenge, we introduce ChemDIRT (Diversified Instruction, Representation, and Task Benchmark), a comprehensive evaluation framework designed to assess the robustness of chemical reasoning in LLMs. ChemDIRT systematically measures model performance across variations in instructions and molecular representations while spanning eight categories of chemistry tasks. By evaluating both accuracy and consistency under these controlled perturbations, ChemDIRT provides a more reliable assessment of model reasoning capabilities than conventional single-format benchmarks. We benchmark a diverse set of open- and closed-source LLMs, revealing substantial prompt sensitivity, representation dependence, and uneven performance across task families.

---


### 30. [DamageScope: Vision-Language Retrieval at Scale for Disaster Damage Assessment from Satellite Imagery](https://arxiv.org/abs/2608.21529)

**<font color=#1a73e8>作者：</font>** Ravi K. Rajendran, Biplob Debnath, Murugan Sankaradas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Timely and accurate assessment of property damage is critical following natural disasters. Traditional on-site inspections are labor-intensive, costly, and often pose safety risks. Advances in satellite imagery and vision-language models (VLMs) enable scalable remote damage assessment; however, integrating VLMs into large-scale Earth observation pipelines presents challenges in computational efficiency, data organization, and information retrieval. To address these challenges, we present DamageScope, a retrieval-augmented framework that combines satellite imagery with Vision-Language Models (VLMs) and Large Language Models (LLMs) to automate property damage analysis. Built on a Retrieval-Augmented Generation (RAG) framework, DamageScope extracts structured visual representations from satellite imagery to support interactive natural language queries for damage assessment. To address scalability, we introduce a novel multi-vector embedding-based clustering algorithm that outperforms traditional single-vector embedding approaches while reducing indexing time by up to 14x. Furthermore, a dual-store data architecture minimizes LLM API calls, reducing both operational cost and response latency by up to approximately 3x. By effectively balancing scalability and operational efficiency, DamageScope provides a robust and practical solution for real-world damage assessment tasks.

---


### 31. [Beyond Sparse Weights: When Is Attention Compressible?](https://arxiv.org/abs/2608.21541)

**<font color=#1a73e8>作者：</font>** Chiwun Yang, Xiaoyu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV-cache compression is often justified by attention maps with a few large weights. This is incomplete: large weights may not contain most of the mass, omitted values can cancel, and preserving the attention output may not preserve the task. We separate these questions. Global score gaps -- not threshold counts -- determine how many tokens are needed to retain a target mass. For a realized row, the weighted sum of omitted values is the exact missing statistic. A controlled retrieval--aggregation model explains when truncation helps and when it hurts. These results motivate CertKV, a training-free compressor that reserves one tail-summary slot per head and allocates the rest by value dispersion. Under matched budgets, CertKV is top-two in seven of nine LongBench-v2 settings, remains in the leading compressed tier on 128K RULER, and realizes a ten-fold cache budget in a packed Llama prototype. Compressibility depends on the mass, values, future queries, and task -- not on a sparse-looking map alone.

---


### 32. [presto: Efficient, Training-free, and Open-world Object Placement via Imaginary Search](https://arxiv.org/abs/2608.21543)

**<font color=#1a73e8>作者：</font>** Weixuan Ding, Shang Liu, Hanyu Pei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object placement is critical in image composition, requiring spatially and semantically coherent positioning of objects within diverse scenes. Existing approaches typically rely on hand-crafted rules or supervised learning on limited datasets, which restricts their generalization and interpretability, especially in open-world scenarios involving novel objects and scenes. In this work, we reformulate open-world object placement as a heuristic search task guided by reasoning from a Multimodal Large Language Model (MLLM). We introduce \textsf{presto}, a zero-shot, training-free framework that operates within an imaginary action space to iteratively refine object position and scale. Our coarse-to-fine search strategy ensures fast convergence, and we evaluate two decision-making variants: Metric-guided Selection and MLLM-as-a-judge. Experiments across multiple benchmarks show that \textsf{presto}~achieves state-of-the-art performance, particularly in previously unseen, open-world settings. Human studies further reveal that the MLLM-as-a-judge variant produces more perceptually coherent placements than metric-driven approaches, highlighting a gap between standard evaluation metrics and human visual judgment.

---


### 33. [Forgotten in Weights, Recovered by Tools: Agentic Tool Unlearning for LLM Agents](https://arxiv.org/abs/2608.21544)

**<font color=#1a73e8>作者：</font>** Baicheng Chen, Zheyuan Liu, Jingyu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as tool-augmented agents, where responses can depend on tool calls and external observations rather than model parameters alone. This creates an evaluation mismatch for LLM unlearning: previous unlearning methods may suppress direct parametric recall, but an agent can still recover the same forget target through tools such as web search, retrieval, or database lookup. We identify this failure mode as tool-mediated recovery and study agentic tool unlearning, which aims to reduce both parametric recall and tool-mediated recovery while preserving normal tool use for retained knowledge. To address this challenge, we propose Agentic Tool Unlearning (ATU), a two-stage framework. The first stage applies parametric knowledge unlearning to suppress direct recall, while the second stage performs trajectory-level reinforcement learning in simulated tool-augmented environments to penalize target-seeking tool behavior and final-answer leakage. Experiments on RWKU and MUSE across different LLM architectures show that ATU achieves a better balance between target forgetting and retained utility, making unlearning more robust under tool-augmented agent deployment.

---


### 34. [Enhancing User Resilience Against AI-Augmented Phishing: A Two-Stage Framework for Detection and Personalized Training](https://arxiv.org/abs/2608.21547)

**<font color=#1a73e8>作者：</font>** Weihao Qu, Gurmeet Singh, Daniel Crawford 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid development of artificial intelligence, including agents and deepfake techniques, has accelerated phishing attacks and lowered the threshold for attackers. Modern phishing attacks now blend multiple tactics, including social engineering, URL spoofing, and AI deepfakes enabling adversaries to craft highly convincing messages that exploit human vulnerabilities and bypass traditional detection systems. At the same time, current security awareness education struggles to keep up with the speed, sophistication, and complexity of these evolving threats. To address this challenge, we propose a two-stage anti-phishing framework, CyberGLA, that combines technical defense and user-centered security education. In the Detection stage, we introduce EmailKnight, a spoof detection tool that performs multi-level email analysis. To enhance user awareness, the Training stage incorporates a large language model (LLM)-based security coach that dynamically selects personalized training modules based on the outcomes of the Detection stage. This dual purpose design philosophy enables effective protection against the evolving threats of modern email phishing attacks.

---


### 35. [Automating Multi-Hop RAG Evaluation via TRIAD: From Context Extraction to Validated Dataset Generation](https://arxiv.org/abs/2608.21558)

**<font color=#1a73e8>作者：</font>** Lorenz Brehme, Adam Jatowt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLMs and the adoption of RAG systems in industry have created a need for domain-specific question-answer datasets that can assess RAG performance on proprietary data. Existing datasets, such as HotpotQA, challenge current RAG systems on Wikipedia-based knowledge, but they cannot be transferred directly to domain-specific settings. A comprehensive evaluation of RAG system quality requires both multi-hop queries and unanswerable questions. This paper introduces TRIAD, a three-stage automated dataset generation approach. First, it generates question--answer (QA) pairs for the domain-specific knowledge base of a RAG system. Second, a validator checks each QA-pair in a feedback loop. Third, the QA pairs are extended with relevance-labeled context documents for downstream evaluation. We evaluate this approach against the established MuSiQue and HotpotQA datasets. The results show that the generated dataset exhibits similar performance trends across different RAG setups, while human validation indicates that the questions are suitable for evaluating a domain-specific RAG system. The code used to generate the dataset and all validation results are available in our GitHub repository(this https URL).

---


### 36. [Evidence-State Reliability Under Controlled Degradation: Parser-Validity Divergence in a Multi-Stage LLM Pipeline](https://arxiv.org/abs/2608.21559)

**<font color=#1a73e8>作者：</font>** Naimur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-stage LLM pipelines can remain structurally valid even when evidence available to downstream stages becomes incomplete, compressed, or conflicting. This paper introduces and operationalizes Evidence-State Reliability (ESR), an evaluation layer concerned with whether intermediate evidence remains sufficiently complete, grounded, internally consistent, and usable for a stage's assigned function. ESR is evaluated separately from parser validity, which measures structural conformance.
We evaluate the framework using GLM-5.2 on 60 sanitized base cases under four evidence conditions: clean, compressed-lossy, partial-dropout, and noisy-conflicting. Each condition was processed through decision, audit, and escalation stages. The design comprised 720 planned and ledgered calls, with 713 retained, sanitized execution rows.
Across nine matched degraded-minus-clean condition-stage comparisons, all operational stage-success estimates were negative, and all 95% bootstrap intervals remained below zero. All nine parser-validity point estimates were positive, although the three partial-dropout intervals included zero. Among parser-valid degraded audit outputs, degradation detection was 1.0 in each degraded condition, while false-assurance rates remained non-zero; among parser-valid degraded escalation outputs, recovery was 0.0 in every degraded condition.
The results show a bounded reliability-layer divergence in the evaluated pipeline: structural conformance can improve directionally while evidence-sensitive stage success deteriorates under the same controlled intervention. They also separate detection of degraded evidence from recovery. The conclusions are limited to the evaluated model configuration, pipeline design, selected sanitized cases, scoring procedure, and single scaled run.

---


### 37. [A Reproducible, License-Aware Distillation Recipe for CPUDeployable Safety Classification](https://arxiv.org/abs/2608.21570)

**<font color=#1a73e8>作者：</font>** Edson Rodrigues da Cruz Filho, Paulo Ricardo Ferreira Neves, Paulo Henrique Eleuterio Falsetti 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying a safety layer for large language models on commodity hardware is constrained by the guards available to do it: current open guard models hold between 1 and 9 billion parameters, are oriented toward the graphics processing unit, and answer in seconds per request on a central processing unit. This paper presents a reproducible, license-aware knowledge-distillation recipe addressing that constraint. A strong open guard labels a corpus of roughly 97,000 prompts, drawn from 24 public datasets, into seven safety categories aligned to a public hazard taxonomy, and a fleet of small students spanning lexical, shallow, encoder and generative architectures is trained to reproduce that signal. The corpus is partitioned at the license boundary, so that a deployable and a research model differ only in their training data and the cost of that restriction becomes measurable. Every model is scored against an independent gold benchmark of 6,361 rows over four slices, labeled apart from the teacher and including a slice of harmless prompts that makes over-defense measurable. The distilled students match the teachers on adversarial text within overlapping confidence intervals and reduce false alarms on harmless prompts, the smallest generative student reaching 3.8% against 4.8% for the 8-billion-parameter teacher, while the encoder classifies in roughly 24 ms per request on CPU. Per-class rebalancing is the only decisive ingredient of the recipe. No superiority over the distilled guards is claimed; on the clean reference slice they remain ahead.

---


### 38. [Data-Driven Dynamic Algorithm Dispatch with Large Language Models](https://arxiv.org/abs/2608.21584)

**<font color=#1a73e8>作者：</font>** Rushil Shah, Emmanuel Lujan, Rabab Alomairy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce a large language model (LLM)-driven approach for generating dynamic algorithmic dispatch heuristics in high-performance linear algebra. By combining prompt engineering with LLaMA 3 and a curated performance database, the model learns to synthesize selection heuristics that exploit structural patterns to identify fast algorithmic choices. A case study on LU factorization demonstrates the model's ability to replicate expert-designed strategies. This work, developed as part of the DARPA-MIT SmartSolve project, highlights the promise of LLMs for algorithmic discovery and the development of more adaptive, fast linear algebra software.

---


### 39. [Perturb the Thought, Not the Pixels: Latent-Space Rollout Diversification for Reinforcement Learning of Vision-Language Models](https://arxiv.org/abs/2608.21595)

**<font color=#1a73e8>作者：</font>** Michael Jerge, Joseph Pelczar, Justin Downes  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves the reasoning ability of vision-language models (VLMs), and diversifying the rollouts within each optimization group amplifies its gains. Existing approaches diversify through decoding temperature or pixel-space image distortion; we ask whether the perturbation belongs in the model's latent space instead. We introduce Noise-Contrastive GRPO (NC-GRPO), which injects scale-calibrated Gaussian noise into the last hidden layer of the prompt-encoding pass for half of each rollout group, branching those rollouts from a displaced departure state. Branches that reach the answer despite the displacement are reinforced over those derailed by it, converting sensitivity at the branch point into policy-gradient signal; the objective, reward, and inference protocol are untouched. On Qwen2.5-VL-7B trained on Geometry3K, NC-GRPO significantly improves out-of-domain mathematical reasoning over vanilla GRPO across five held-out benchmarks (pooled McNemar $p \le 0.001$) while also improving in-domain accuracy and hallucination robustness -- the latter an axis on which image-space noise regresses even while posting a larger OOD average on perception-heavy benchmarks. Mechanism ablations indicate that independent stochastic diversity, not noise budget or direction, is the active ingredient, and a noise-scale study exposes a dial between reasoning specialization and general capability. NC-GRPO is designed to be modality-agnostic and integrates into a standard RLVR pipeline as a ~50-line change to the inference engine.

---


### 40. [K-Bench: measuring model performance on real scientific agent requests](https://arxiv.org/abs/2608.21601)

**<font color=#1a73e8>作者：</font>** Aubrey Brueckner, Darshil Patel, Yuhuan He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks for scientific artificial intelligence are mostly written to be scored: multiple-choice questions, curated agent tasks with reference solutions, or simulators with a known generative structure. Real scientific requests arrive differently. They are underspecified, they carry attachments, and lack ground truth. We report K-Bench 01, an evaluation built from first-turn requests sampled from live user traffic on K-Dense Web and run end to end by nine frontier models in identical sandboxes, yielding 1,602 completed agent runs. Three blinded language-model judges scored every run against an eight-dimension rubric. On a rubric whose 8-anchor instructs judges that a domain scientist would accept the work with minor edits, no model clears the line under all three judges. gpt-5.6-sol has the highest pooled mean, 8.04, but its 95% interval [7.80, 8.23] spans the threshold, and two of the three judges rank claude-opus-5 first instead. We therefore report the ordering of systems as the reproducible quantity, the absolute level as an attribute of the instrument, and the top of the table as unresolved. Across all 39,934 scored judgments -- the eight dimension scores plus a holistic overall for each assessment, excluding not-applicable cells -- 47.6% fall below the 8-point threshold. Difficulty is not uniform across the rubric: scientific accuracy averages 6.22 against 7.33 for communication, on identical denominators and in the same direction within every one of the nine models. The single leading failure tag is overclaiming, on 31.4% of assessments. We argue that the informative quantity for scientific agents is not a leaderboard position but the joint distribution of what was delivered, what was claimed, and what artifacts were produced.

---


### 41. [Exploring Agentic Approaches for Data Issue Detection and Repair in AI-Assisted Visualization](https://arxiv.org/abs/2608.21602)

**<font color=#1a73e8>作者：</font>** Parimal Kashireddy, Anna Fariha, Mahmood Jasim  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI is increasingly lowering the barrier to data analysis and creating visualization scripts. However, a key obstacle in AI-assisted visualization is that certain data issues can lead to visualizations that are plausible, but misrepresent the underlying data. These \textit{visualization defects} are elusive and difficult to fix, particularly for non-experts who may not know what data issues cause them or how to guide AI systems to resolve them. We present findings of a preliminary empirical investigation of how commercial LLMs identify and repair defect-inducing data issues. Using a curated subset of the 911 emergency-call dataset with five injected data issues, we evaluated GPT-5, GPT-4o, GPT-4, and Claude Sonnet 4.6 under a three-stage prompting protocol, including zero-shot, guided issue-identification, and guided issue-repair. We executed this protocol under two conditions: single-agent and a multi-agent orchestration that separates data issue detection, review, repair planning, data repair, and repair quality assurance. We observed that across both conditions, LLMs identified and repaired single-field issues (e.g., missing values) but struggled to identify and repair temporal, geographic, and semantic issues. Based on these observations, we discuss design implications for agentic visualization systems, including explicit representation of data assumptions, selective human intervention for ambiguous decisions, and evidence-based repair.

---


### 42. [Can LLMs Truly Forget? Revealing Unlearning Gaps Through Adversarial Evaluation](https://arxiv.org/abs/2608.21606)

**<font color=#1a73e8>作者：</font>** Ayush Gupta, Hima Varshini Surisetty, Sreevidya Bollineni 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove the influence of targeted training data from a model while preserving its remaining capabilities, but evaluating whether such information has truly become inaccessible remains challenging. Existing benchmarks primarily assess unlearning under clean, non-adversarial queries, leaving open whether information that appears forgotten can still be recovered through strategic prompting. We address this gap through a unified evaluation of prompt-based and fine-tuning-based unlearning methods on TOFU using Llama-3.2-3B-Instruct, followed by an adversarial robustness evaluation of methods that perform strongly under standard metrics. We introduce Attack Success Rate (ASR), an LLM-as-judge metric that measures the fraction of adversarial responses whose leakage score exceeds $0.2$, and evaluate recovery across eight attack suites. Our results reveal a substantial gap between clean-query forgetting and adversarial robustness. Although several fine-tuning-based methods achieve Forget Quality above $0.91$, targeted information remains recoverable with ASRs between $72.8\%$ and $84.3\%$, close to the $87.5\%$ ASR of the unprotected base model. In contrast, clean multilingual reformulations yield only $2.95\%$ measured leakage. A manual audit further finds agreement between binary ASR decisions and human factual assessments in seven of ten cases, indicating that ASR provides a useful, though imperfect, signal of behavioral recoverability. These findings show that strong standard-metric performance alone is insufficient to establish robustness after unlearning and motivate adversarial stress-testing as a complementary component of unlearning evaluation.

---


### 43. [Semantic Compression Trees: Multi-Resolution Knowledge Retrieval via Hierarchical Semantic Residuals](https://arxiv.org/abs/2608.21610)

**<font color=#1a73e8>作者：</font>** Junaid Farooq  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation relies mostly on flat, fixed-granularity indexes: documents are cut into uniform chunks and retrieved by similarity, discarding the hierarchical structure of the source. We introduce Semantic Compression Trees (SCT), a hierarchical index in which each node stores only its semantic residual -- the information it adds beyond its parent -- and retrieval proceeds by progressive descent from the root, so that per-query cost is governed by tree depth rather than collection size.
We evaluate on QASPER (50 papers, 173 questions) under two protocols differing only in whether the benchmark supplies the relevant document, with bootstrap confidence intervals and paired significance tests throughout. The results are mixed and we report them as such. When the document is given, SCT with a zero-LLM extractive compressor matches dense retrieval on answer quality (0.274 vs. 0.277 F1, $p = 0.37$) using 30% fewer context tokens and no LLM calls to build the index, and residual storage beats storing full summaries at each node (0.274 vs. 0.205, $p < 0.001$). Increasing the collection fifty-fold multiplies flat retrieval's per-query scoring work by 48.9x and SCT's by 6.4x.
Progressive descent itself is not supported. Retrieving the same residuals without the tree performs identically when the document is given ($p = 0.27$), and descent is substantially worse when the system must select the document (0.122 vs. 0.165, $p < 0.001$). Routing accuracy localises the cause: descent selects the correct paper 20.2% of the time against 39.3% for flat retrieval, because that choice is made from the root residual, the most compressed node in the tree. We conclude that the residual representation is worth keeping and top-down routing is not.

---


### 44. [SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning](https://arxiv.org/abs/2608.21614)

**<font color=#1a73e8>作者：</font>** Yujie Zhang, Bin Gao, Tulika Mitra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) prompting improves LLM reasoning by decomposing complex problems into intermediate steps, but its sequential nature increases decoding latency and memory usage. Mixture-of-Experts (MoE) models scale capacity through sparse expert activation, yet their full expert weights often exceed GPU memory and require costly GPU-CPU transfers. Existing runtimes treat all tokens uniformly, overlooking a key structural property of CoT traces: consecutive reasoning stages exhibit coherent and predictable expert activation patterns. Ignoring this stage-level regularity leads to inefficient caching and unnecessary data movement. We propose SAEM, a stage-aware MoE inference runtime that detects reasoning stage boundaries and exploits stage-level activation coherence to guide expert placement. SAEM combines stage-aware caching, expert-aligned token repacking, and in-situ CPU execution to reduce data transfer and kernel fragmentation. On mathematical and scientific reasoning workloads, SAEM achieves an average 1.33x throughput improvement over the strongest state-of-the-art caching and offloading baselines under constrained GPU memory, rising to 1.54x when calibration data matches the workload, demonstrating the effectiveness of stage-aware, locality-driven MoE inference for CoT reasoning.

---


### 45. [Mitigating Database Leakage in RAG Systems with Keyword-Grounded Fact Substitution](https://arxiv.org/abs/2608.21656)

**<font color=#1a73e8>作者：</font>** Ziliang Zhang, Yubo Zhu, Wei Tong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm for combining large language models (LLMs) with external knowledge sources. However, RAG systems remain vulnerable to prompt injection attacks, which may mislead the retriever or generator to expose sensitive database contents. To address this issue, we propose KFS-RAG, a defense that mitigates information leakage by reformulating the retrieved context. Specifically, our method first identifies a small set of influential keywords from the retrieved context via an attention rollout plus a causal perturbation mechanism. These keywords are then used to guide an auxiliary LLM to generate a compact set of keyword-grounded facts from the retrieved passages. Finally, the original context is substituted with these curated facts, ensuring that the generator operates on sanitized evidence rather than the raw retrieved text. Experimental evaluations demonstrate that KFS-RAG significantly reduces the risk of database leakage under injection attacks while maintaining response accuracy and relevance. This work highlights a practical pathway toward building secure and trustworthy RAG systems.

---


### 46. [Measuring Activation Control in Large Language Models](https://arxiv.org/abs/2608.21664)

**<font color=#1a73e8>作者：</font>** Marek Mateusz Kowalski, Joshua Fonseca Rivera, Uzay Macar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safe deployment of increasingly capable models will likely come to rely on latent-space monitoring as a complement to behavioral evaluations, especially when evaluation-aware models exhibit scheming or deception. However, if models can also control their own activations, deception could extend into the latent space itself. With this in mind, we introduce the Activation Controllability Benchmark to quantify the extent to which models can modulate their residual stream via natural-language instruction. Across model families and capability levels, we find that most LLMs can control the direction and magnitude of their residual stream activations with some degree of temporal resolution, though performance varies considerably across models. In simple tasks, this level of control can evade activation-based monitoring methods (including linear probes, natural language autoencoders, activation oracles, and the Jacobian lens), albeit imperfectly. These results suggest that control over the activation space itself could become a confound for monitoring as introspective capabilities increase; therefore, we recommend that frontier labs and evaluators track activation controllability in future models.

---


### 47. [From Mastery Profile to Simulated Response: Stochastic Student Knowledge Graphs (SSKG) for Faithful LLM Student Simulation](https://arxiv.org/abs/2608.21668)

**<font color=#1a73e8>作者：</font>** Yuan An, Emily Wang, Benjamin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to simulate students at different mastery levels. These simulations can generate synthetic training data and stress-test tutoring systems. However, common prompt-based approaches leave the answer decision to the LLM, which tends to perform according to its built-in capabilities even when instructed to simulate a student with low mastery. As a result, these approaches may have difficulty distinguishing students with low and high levels of mastery. We demonstrate this limitation using 379 College Board-calibrated SAT Algebra items and five archetypal mastery profiles. Three LLMs from three vendors (Gemini 3.1 Flash Lite, Claude Haiku 4.5, and GPT-5.4-mini) achieve 96.8-100% accuracy across all profiles. To address this limitation, we introduce a method grounded in a Stochastic Student Knowledge Graph (SSKG). A curriculum knowledge graph (CKG) is extracted from an open algebra textbook, and each SAT solution is decomposed into a chain of required triples. The SSKG assigns a mastery probability to each triple, which is sampled to determine question correctness. An LLM then generates a first-person rationale consistent with the outcome. The simulation reduces accuracy to 44.1-85.2% across profiles and produces a clear monotone mastery gradient.

---


### 48. [SynEHR: Joint Modeling Inter-visit Temporal Evolution and Intra-visit Clinical Structure for Longitudinal EHR Synthesis](https://arxiv.org/abs/2608.21673)

**<font color=#1a73e8>作者：</font>** Ximiao Li, Lin Jiang, Rongchao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal electronic health records (EHRs) document patients' sequences of clinical visits over time, preserving the temporal evolution of disease progression and care delivery. However, real longitudinal EHRs are difficult to access because they contain large amounts of fine-grained, patient-specific information. Synthetic EHR generation therefore provides a valuable approach for preserving the statistical patterns and clinical structure of patient visit trajectories, enabling broader modeling and analysis when real records are limited. Although recent generative models have made progress in producing future visit sequences, they remain limited in explicitly integrating inter-visit irregular temporal evolution and intra-visit clinical event structures in EHRs, leading to clinically inconsistent and temporally unrealistic visit sequences. In this work, we propose SynEHR, a lightweight adaptive LLM-based framework for longitudinal EHR synthesis. There are two novel designs in SynEHR, i.e., a Temporal State Conditioning Module captures irregular temporal states across visits and a Temporal-Relational Adaptation Module combines these states with patient history to dynamically construct patient-specific relational representations. SynEHR then builds on a parameter-efficient LoRA-adapted language-model generator with next-visit generation capability to train the two modules for temporally and clinically informed generation. Extensive experiments on real-world EHR datasets across fidelity, privacy, and downstream utility evaluations demonstrate that SynEHR outperforms state-of-the-art models by generating more clinically coherent and temporally faithful longitudinal EHR data.

---


### 49. [Context as an Environment: Programmatic Context Management for Long-Horizon Agents](https://arxiv.org/abs/2608.21690)

**<font color=#1a73e8>作者：</font>** Yin Lin, Elaine Ang, Erkang Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly take on long-running tasks whose history grows far beyond a single model context window. Existing approaches compress earlier interactions or extract selected information into fixed memory representations, committing to what to preserve before future needs are known. We present Scroll, a context manager that treats each agent session as an executable Session Environment. The environment is backed by an append-only Event Log and a sandboxed, persistent Python kernel. The kernel maintains a typed namespace across model calls, allowing tool outputs, retrieved history, and derived state to be bound to variables rather than serialized into the prompt at each call. Model-written code searches, materializes, and transforms session state through exec; only explicitly printed projections enter the model's working view for the next call. Context management thus becomes a programming task that inherits the improving coding abilities of LLMs, while the Event Log preserves lossless historical ground truth. As the working view approaches its budget, stale spans are evicted but remain recoverable: an eviction index keeps compact landmarks tied to exact Event Log addresses, so that the agent navigates directly to evicted regions instead of searching the full log. With Qwen3.8-Max as the backbone, Scroll achieves 94.8% on LongMemEval_S; 73.1% on BEAM_10M, surpassing the best published memory system by 5.1 points; and 86.7% on LOCA_256K, exceeding the best published long-horizon agent by 37.4 points.

---


### 50. [Benchmarking Composable Compression Techniques in Mixture-of-Experts LLMs](https://arxiv.org/abs/2608.21693)

**<font color=#1a73e8>作者：</font>** Afsara Benazir, Chen Chen, Rongxiao Qu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) LLMs scale model capacity efficiently through sparse activation, but their large expert parameter footprint, routing imbalance, and long-context KV-cache growth make deployment difficult on commodity hardware. Practical deployment often requires stacking multiple compression techniques: expert pruning removes redundant experts, weight quantization lowers model memory footprint, and KV-cache compression reduces long-context memory pressure. However, these techniques are typically evaluated in isolation, leaving open how they interact when applied together in realistic deployment pipelines.
In this work, we present MoEXBench, a systematic benchmark for evaluating composable MoE compression as an end-to-end deployment workflow. MoEXBench studies 10 MoE models ranging from 30B to 235B total parameters across standard-attention, hybrid linear-attention, and sliding window attention architectures. It evaluates 20%-50% expert pruning rates, 1 to 16 bit weight-quantization schemes, and multiple KV-cache precision settings, applied both individually and in combination.
MoEXBench introduces an eight-module evaluation suite that jointly measures composable-compression quality, workload and architecture robustness, pruning/quantization/KV cache sensitivity, and deployment efficiency on commodity hardware. Our results reveal non-trivial interactions among compression methods: composable compression cannot be predicted from standalone techniques, compression rate alone does not reliably predict quality loss or runtime gain, expert pruning is the dominant degradation source, and average quality can hide workload and architecture-specific failures. By releasing normalized module scores, compressed artifacts, and reproducible scripts, MoEXBench enables practical accuracy-memory-latency comparison across MoE families and hardware backends.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-363](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
