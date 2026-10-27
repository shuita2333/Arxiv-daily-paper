# 🧠 大模型相关研究 | 2026年10月28日

> 本类共 **418** 篇论文：已确认 **396** 篇，待复核 **22** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

---

### 251. [Text Is the Bottleneck: A Small-Scale Replication of LLM Game Playing in Riichi Mahjong](https://arxiv.org/abs/2610.34791)

**<font color=#1a73e8>作者：</font>** Mingge Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We replicate the riichi-mahjong track of "Can Large Language Models Master Complex Card Games?" (arXiv:2509.01328) under a drastically smaller budget: models of at most 2B parameters, one 16 GB consumer GPU, about five GPU-days. (1) With matched data and labels, text is the bottleneck: on the same 100k-decision training set, a 2.6M-parameter convolutional board encoder agrees with the strong AI Mortal on 80.6% of test decisions, above every text-prompt LLM we train (best 77.8%), and places better at the table (2.85 over 1,000 games vs. ~3.0 for the LLMs; paired difference at n=100 not significant). Scaled to 1.71M decisions, a 4.9M-parameter Transformer reaches 94.7% agreement, beats the 0.8B LLMs on identical seeds (-0.45 ranks, sign test p=0.005), and is statistically equivalent to parity against three Mortal champions (TOST within 0.10 ranks, p=6e-4); parity against a teacher-opponent is roughly the ceiling of pure imitation. (2) Training toward the teacher raises teacher agreement more than a 2.5x parameter increase does (+2.5 vs. +1.5 points); on human-record agreement both effects are +1.0, and neither is visible at the table. (3) Few-point agreement differences do not resolve into playing strength within a family: +2.5 agreement points coincide with a paired placement difference of +0.02 +/- 0.12 ranks (p=1.0), and +2.0 points at 2B with -0.06 (p=0.37) - both below the ~0.25-rank resolution of 100 paired games. We also document a paper-code mismatch in the original winner filter, reconstruct its two private engine patches, and show that a divide-and-conquer pipeline makes template-generated Japanese rationales 93% sentence-exact (43% without facts). Per Tenhou's terms we release no trained weights - only code, configurations, and evaluation protocols.

---


### 252. [Position Matters More Than Channel: Talking a Language Model Out of a Correct Answer](https://arxiv.org/abs/2610.34809)

**<font color=#1a73e8>作者：</font>** Xinyi Ni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models now answer questions alongside other claims: a note in the system prompt, a message from another agent, their own earlier answer. We ask what it takes to talk a model out of an answer it gets right on its own, and separate three factors that earlier studies vary together: where the advice sits in the prompt, who is said to have written it, and what the model has already written. On Qwen3.5-27B and four-option MMLU-Pro items, with the rest of the advice held fixed in each comparison, we find three things. First, position matters far more than the API channel, in opposite directions for a bare claim and an argument: a bare "the answer is X" does most harm just before the model answers, while the same claim with a false rationale does most harm before the question, where it raises error on items the model otherwise almost never misses from 1% to 67%; moving the claim between the system message and the user message at the same position changes error by a few points. Second, attributing the note to an authority rather than to another participant, and phrasing it assertively, each raise error by 10-27 points, while the two authorities we tested differ by under two. Third, replaying a correct worked answer before the advice protects it whether the text is shown as the model's own or as someone else's, and the same replay keeps wrong answers from being corrected by a bare correct note. The position result replicates under an independently written prompt. Code, items and all result tables are released at this https URL.

---


### 253. [Can System-1-Style Decision Models Replace Dedicated Rerankers in RAG? A Systems Evaluation](https://arxiv.org/abs/2610.34816)

**<font color=#1a73e8>作者：</font>** Qiaomu Li, Ying Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems often use a dedicated reranker to choose which retrieved candidates reach the language model. Reranking improves relevance but adds latency, so teams look for faster alternatives. System-1style decision models make direct, structured predictions instead of generating long responses. Could one provide comparable reranking quality with less inference overhead? We first screen 21 open-weight models on 11 benchmarks, then compare a promising decision model with a dedicated reranker on identical candidate lists. The default decision-model setup fails on many long candidate sets, so scoring only the requests it completes gives a misleading ranking. Limiting candidate text length largely restores reliability and makes some configurations competitive. A frozen evaluation on new retrieval data supports the reliability and ranking results, but confirms the latency requirement for only one of the two selected configurations. Across workloads, which model ranks better changes, and a tuned reranker remains faster and uses far less GPU memory. A decision model can perform competitive reranking, but replacing a reranker requires weighing quality, latency and memory together, and teams should tune the reranker they already run first.

---


### 254. [TrustJev: Separating Policy Authority from Untrusted Evidence in LLM-Based Decisions](https://arxiv.org/abs/2610.34826)

**<font color=#1a73e8>作者：</font>** Zhiwei Xu, Xuyang Liu, Xiaolin Peng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models enable software to select from predefined actions using natural language inputs. However, the external evidence that supplies facts for these decisions may also contain instructions that attempt to override the application's policy. We propose TrustJev, a framework combining protected policy scoring with bounded evidence corrections. A single Transformer backbone computes policy scores and a correction budget from trusted policy and candidates, then bounds evidence corrections by that budget. Paired supervision encourages stable predictions under instruction insertions that preserve task facts and changed preferences when edits change the correct answer. Authority supervision accommodates evidence when the policy alone cannot determine the decision. We evaluate a 0.6B implementation against 14 baselines on three datasets covering authentication, instruction hierarchy, and executable authorization rules. TrustJev achieves the highest mean Balance, the harmonic mean of accuracy on non-attack and attack inputs, exceeding the strongest baseline on each by 0.57-1.05 percentage points. In the authorization benchmark, it correctly answers all 32 attacks per source in a fixed pool for 95.77% of sources, compared with 80.98% for the strongest comparator. TrustJev maintains comparable inference memory and median latency, with additional overhead primarily during training.

---


### 255. [Collective Emergent Alignment: Measuring and Amplifying Interaction-Induced Reasoning Alignment in Multi-Agent LLMs](https://arxiv.org/abs/2610.34836)

**<font color=#1a73e8>作者：</font>** Boxuan Wang, Zhuoyun Li, Sarvapali D. Ramchurn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) systems can exhibit emergent behaviors through interaction, yet whether a similar phenomenon exists for reasoning alignment remains largely unexplored. We study whether agent interaction produces additional reference-grounded reasoning alignment beyond matched individual self-refinement, and introduce REMAP (Reference-Entailment-Matrix for Agentic Process), a framework that quantifies this effect through Semantic Coverage and interaction-specific alignment gains. Across diverse model families and two multi-hop reasoning benchmarks, we observe broadly positive interaction gains, particularly on reasoning content that depends on integrating evidence distributed across agents. These gains are consistently associated with independently measured peer-information recovery, while further analysis reveals composition-dependent heterogeneity effects and asymmetric information transfer across agent capability levels. Motivated by these findings, we further introduce a fact-level multi-agent communication framework that replaces full reasoning-trace exchange with compact, gap-aware, and selectively routed information. Our experiments show that compact fact exchange improves reasoning alignment and task performance while reducing communication overhead, whereas more selective communication exposes a trade-off between acquiring distributed information, retaining local content, and communication efficiency. Overall, our results show that collective emergent alignment can be quantified, linked to information-transfer patterns, and used to guide more effective multi-agent communication.

---


### 256. [Beyond Behaviour: A Stimulus-Response Safety Evaluation of Vision-Language-Action Models](https://arxiv.org/abs/2610.34837)

**<font color=#1a73e8>作者：</font>** Vy Vo, Dinh Phung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans exhibit biological sensitivity to safety-critical stimuli that can trigger defensive action. Across three models and two video benchmarks, we investigate whether similar responses emerge in vision-language-action models by examining their internal representations and action tendencies in response to visible hazards and harmful consequences. Our findings suggest that task execution may remain the default response even when danger is internally registered.

---


### 257. [When Respondents Are Scarce: LLM-Derived Semantic Priors for Bayesian Confirmatory Factor Analysis](https://arxiv.org/abs/2610.34843)

**<font color=#1a73e8>作者：</font>** Shaohuai Feng, Mohd Wira Mohd Shafiei, Mohd Sukri Shafie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Across social and behavioral research, measuring latent constructs can be challenging when target populations are small or difficult to reach. Recruiting additional respondents may be costly or infeasible, leaving researchers with limited data for estimating questionnaire factor structures. Yet item wording contains structural expectations before data collection, and whether these can improve small-sample estimation without replacing empirical validation remains unclear. We introduce the Semantic-Empirical Updating Framework (SEUF), which converts large language model paraphrases and embeddings, aligned with hypothesized item-factor assignments, into prespecified priors for Bayesian confirmatory factor analysis. We evaluated SEUF using a 38-item survey of 617 industrial-park stakeholders and two public surveys, FEVS and RIASEC. Semantic structure persisted after wording controls across all three instruments. With 50 respondents, SEUF achieved loading precision comparable to conventional CFA with 70-82 respondents, equivalent to 29-39% fewer respondents at the specified precision benchmark. Results showed lower loading errors and improved credible-interval coverage relative to conventional CFA in both public surveys. Gains were greatest when respondent data were limited, highlighting the value of semantic priors under information scarcity. By harnessing structural information already embedded in questionnaires, SEUF advances a more resource-efficient approach to measurement and opens new directions for study design and empirical inference in hard-to-reach populations.

---


### 258. [Seeing Before Naming: Context-Grounded Learning of Novel Visual Concepts](https://arxiv.org/abs/2610.34846)

**<font color=#1a73e8>作者：</font>** Gabriel Adineera, Jinoh Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning an unfamiliar visual category requires more than adapting a classifier: the model must connect its visual evidence to a useful semantic name. A pre-trained vision-language model can retain discriminative image features while providing a weak textual anchor for the target concept. We address this imbalance through context-grounded semantic anchoring. Our framework, SynerNet, learns concept-specific name embeddings, exposes them to compatible linguistic contexts, and conditions their representations on visual evidence. Difficulty-aware processing and adaptive objective weighting coordinate this adaptation while retaining the pre-trained backbone. On four VISTA-Beyond domains, SynerNet reaches a mean 16-shot accuracy of 74.35%, compared with 72.45% for few-shot name learning. Across 14 domains in the name-masked transfer setting, it improves mean accuracy from 45.17% to 46.74%. Ablations identify concept-specific name embeddings and cross-modal context integration as important components. These results support treating concept acquisition as the construction of visually grounded semantic anchors.

---


### 259. [DecoyCount: Evaluating Visual-Reasoning Misalignment in Counting](https://arxiv.org/abs/2610.34855)

**<font color=#1a73e8>作者：</font>** Qiuyi, Zhang, Zhen Xu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual counting benchmarks report whether vision-language models produce the correct number, but not whether errors arise from perception or reasoning. We introduce DecoyCount, a benchmark built from 1,660 real-world images with designed decoys across seven mechanisms, along with paired prompts: a neutral question, a matched alignment cue, and a novel multi-hop, multi-image question that situates the same counting problem in a realistic scenario. Using this design, we find that counting failures are induced partly by visual misalignment: models can execute the intended counting process when cue-guided but fail to select it unaided, and we term this difference in accuracy the reasoning-alignment gap. Despite being highly capable on general reasoning, frontier models remain below 50\% accuracy on our benchmark, while alignment gaps range from 11.8-22.1 percentage points; strikingly, we observe that more capable models, greater thinking budgets, and agentic processes often induce larger gaps. Because humans may bring context that models lack, we test whether textual underspecification contributes to misalignment using a scenario-based multi-hop condition without explicit hinting, but this added context does not improve aggregate performance. Our analysis concludes that stronger general reasoning does not by itself generalize to aligned visual reasoning, leaving misalignment with human visual expectations as a substantial component of the remaining deficit.

---


### 260. [Semantic Atoms for Scalable Text Analysis in Data Analytics in the Era of LLM-Based Agents](https://arxiv.org/abs/2610.34860)

**<font color=#1a73e8>作者：</font>** Jinxiang Xie, Zihao Li, Rui Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Much of the information needed for data analysis is buried in text columns: an analyst may infer customer frustration from complaint text and use it to explain resolution time. We call workloads in which processing text columns is central to subsequent data analysis TADA (\emph{Text Analysis in Data Analytics}). In an agentic setting, the user's query dynamically specifies this processing, and answering it interleaves LLM-based semantic steps with exact SQL or Python operations. This mixed execution raises two design questions: which work should be neural and which symbolic, and which semantic outputs later steps can reuse. We address them for agent-planned TADA workflows with two complementary, query-driven semantic atoms. Each atom takes a sequence of text items and a natural-language query specifying the semantic task: \textbf{Tagging} returns one string per input item, while \textbf{Categorization} returns $M$ category objects over $N$ input items. Tagging results are materialized as a row-aligned column and Categorization results as a category table; SQL or Python then performs exact computation over this exposed state. We realize this interface in TADA-Agent, whose atoms run inside generated Python programs and internally handle inputs beyond a reliable context window. We evaluate TADA-Agent on TABench, a benchmark of 40 complete analysis requests over spreadsheet tables spanning workflow composition, input--output structure, and literature-grounded analytical scenarios. Against a semantic-operator baseline and relative to a held-out TADA reference run, TADA-Agent delivers comparable row-level semantic quality, has higher complete-artifact preservation estimates, and uses over an order of magnitude fewer semantic-model requests under the evaluated native execution paths.

---


### 261. [Priority-Preserving Advantage Aggregation for Multi-Reward Policy Optimization](https://arxiv.org/abs/2610.34862)

**<font color=#1a73e8>作者：</font>** Xiangchi Yuan, Xingjian Diao, Zheyuan Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM post-training often optimizes multiple objectives with unequal priorities, such as correctness and reasoning efficiency. However, the widely used additive reward aggregation in RL can violate these priorities: when primary and auxiliary advantages conflict, a sufficiently large auxiliary signal can overturn the preference induced by the primary objective. We term this problem \emph{advantage priority inversion}. Although reward-level gating can protect priority more directly, it still removes potentially useful auxiliary distinctions among rollout samples that fail the primary condition. To address this trade-off, we propose Primary Advantage Policy Optimization (\textbf{PAPO}), a priority-aware advantage aggregation method that asymmetrically combines a primary and an auxiliary advantage. PAPO retains auxiliary supervision when the objectives agree and smoothly attenuates conflicting auxiliary signals, preserving the primary sign during fusion for \emph{primary-consistent ordering}. This rule applies to sequence-level advantages in GRPO and token-level advantages in actor--critic PPO. Experiments on multiple domains and models show that PAPO consistently achieves the best primary objective while maintaining best or competitive auxiliary-objective performance across both GRPO- and PPO-based optimization. \href{this https URL}{Code is available}.

---


### 262. [ECHOES: An Adaptive LLM-Powered AR Glasses Docent for Evidence-Grounded Urban Heritage Interpretation](https://arxiv.org/abs/2610.34865)

**<font color=#1a73e8>作者：</font>** Bang Xiao, Baosheng Jin, Jinhan Niu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Urban heritage tours are often delivered through fixed scripts, leaving limited room for visitors' situated questions, language preferences, or requests for evidence. We present ECHOES, an adaptive LLM-powered AR glasses docent for evidence-grounded interpretation of historical buildings. Specifically, the agent adapts along three dimensions: it modifies response structure according to the type of visitor question (identification, architectural detail, evidence-seeking, or route inquiry); it accumulates session-level interest signals from repeated questions and expressed curiosity to shape later explanations; and it tracks language preference and retrieval context across turns to maintain conversational continuity. The core of ECHOES is an LLM agent initialized as a source-aware urban heritage docent that realizes this adaptation through dialogue and preference context maintained across the session. Around this agent, ECHOES integrates visual site grounding, a self-built historical knowledge base supporting retrieval-augmented generation, and concise multilingual AR output designed for glanceable use. Through a working prototype centered on Shanghai's East Nanjing Road and the Bund, we demonstrate how an adaptive LLM-powered AR docent can transform historical tours from scripted narration into situated, question-responsive, and source-aware conversations.

---


### 263. [UniGFM-RAG: Unify Graph Foundation Models and Large Language Models for End-to-End Retrieval and Reasoning](https://arxiv.org/abs/2610.34866)

**<font color=#1a73e8>作者：</font>** Zicheng Zhao, Linhao Luo, Zongji Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown remarkable capabilities across tasks, but they still struggle with complex reasoning that requires integrating scattered knowledge. Graph Retrieval-Augmented Generation (GraphRAG) addresses this challenge by organizing fragment knowledge as graphs, while recent Graph Foundation Models (GFMs) further improve GraphRAG with graph-native retrieval and reasoning capabilities. However, existing GraphRAG methods usually adopt decoupled retrieve-then-generate pipelines, which create objective misalignment between retrieval and reasoning, and training GFM retrievers typically depends on expensive human annotations. To address these limitations, we propose \ourmethod, a unified end-to-end GraphRAG framework that tightly couples a GFM retriever with an LLM generator. Given a query, the GFM retriever first reasons over the graph to score and retrieve relevant document nodes. These node embeddings are then passed through a fully differentiable graph bridge, which projects them into soft-weighted graph prefixes according to retrieval scores and combines them with raw document texts to form graph-augmented prompts. In this way, structural information is injected directly into LLM generation, while the final answer loss can be back-propagated through the bridge to jointly optimize retrieval and reasoning. To stabilize training and reduce reliance on costly annotations, we further introduce a semantic-guided distillation module that provides auxiliary supervision using pseudo-labels derived from query-document semantic similarities. Extensive experiments on three multi-hop QA datasets and three out-of-domain GraphRAG benchmarks show that \ourmethod consistently outperforms strong baseline methods and generalizes well, which demonstrates the effectiveness of end-to-end GraphRAG with tightly integrated GFM retrieval and LLM reasoning.

---


### 264. [DocTalk: Enhancing Medical Knowledge Retrieval via Fine-tuned Large Language Models with Chain-of-Thought Reasoning for Robust Clinical Decision Support](https://arxiv.org/abs/2610.34871)

**<font color=#1a73e8>作者：</font>** Asad Gohar, Md Ariful Islam Mozumder, Moon-Il Joo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective: The rapid advancement of large language models (LLMs) in healthcare has opened new possibilities for AI-assisted clinical decision-making; however, safe and effective deployment remains challenging because of hallucination and domain misalignment. This study introduces DocTalk, a doctor-assistive question-answering (QA) system designed to generate concise, chart-grounded responses from de-identified discharge summaries. Methods: We developed a high-fidelity data generation pipeline that produces 500 clinically relevant QA pairs through sentence-level decomposition, chain-of-thought-guided question formulation, and expert review. Six open-source LLMs, including three general-purpose and three biomedical models, were evaluated before and after parameter-efficient instruction tuning using Low-Rank Adaptation (LoRA). The framework integrates prompt engineering, in-context learning, and medically aligned evaluation to support factual and interpretable responses. Results: On DocTalk-QA, instruction tuning produced consistent improvements across lexical, semantic, and clinical fidelity metrics. The best-performing tuned model, Llama-3-Med42-8B, achieved ROUGE-L = 0.40, BERTScore-F1 = 0.76, and UMLS-F1 = 0.49. To examine external generalization beyond the DocTalk-QA dataset, the two best-performing models, Llama-3.1-8B-Instruct and Llama-3-Med42-8B, were evaluated on PubMedQA before and after instruction tuning. Accuracy improved from 0.931 to 0.977 for Llama-3.1-8B-Instruct and from 0.935 to 0.943 for Llama-3-Med42-8B. Conclusion: DocTalk was deployed as a secure web-based platform for interactive EHR querying. These findings suggest that clinically grounded instruction tuning can improve medical QA performance and support practical clinical decision support.

---


### 265. [Adaptive Retrieval, Selective Answers: Evaluating Conformal Factuality in Agentic RAG](https://arxiv.org/abs/2610.34872)

**<font color=#1a73e8>作者：</font>** Muhammad Aimal Rehman, Chi-Kuang Yeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) can improve factual grounding without guaranteeing that every generated claim is supported. Previous work has studied claim-level conformal factuality in single-stage RAG and, more recently, multi-hop RAG. We examine its behavior in agentic RAG, where a language-model policy adaptively issues follow-up retrieval queries or terminates retrieval before response generation. We retain the retrieval-based relevance-scoring formulation and post-generation conformal filtering and evaluate six model-dataset configurations: GPT-6 Luna and Llama 3.1 8B on HotpotQA, Natural Questions, and TriviaQA. Each configuration uses 60 fixed questions, 100 seeded 30/30 calibration-test partitions, five conformal target levels, and a no-conformal-prediction baseline. Across the six configurations, higher target levels are accompanied by higher observed full-support rates and reduced answer availability. At the 95% target, non-empty response coverage ranges from 17.23% to 60.17%, claim retention from 10.72% to 43.16%, and full support among non-empty outputs from 89.14% to 95.56%. We formulate the adaptive retrieval trajectory explicitly and characterize the reliability-informativeness trade-off when conformal factuality is applied after agent termination.

---


### 266. [RubriX: A Fast, Fine-Tunable Non-Autoregressive Rubric Judge](https://arxiv.org/abs/2610.34875)

**<font color=#1a73e8>作者：</font>** Balamurugan Paramasivam, Sudalai Rajkumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based evaluation asks which level of a rubric a response meets. It is usually done by prompting a large language model (LLM) as a judge, which needs a generative call per judgment and reads every level description, so its cost grows with the rubric. We present RubriX, a rubric judge whose architecture is inspired by contrastive language models (CLM): a LoRA-adapted encoder embeds the input and each level description, and a softmax over scaled cosine similarities gives a probability for every level without text generation. Trained on public rubric data and proprietary synthetic data, RubriX reaches 75.4% exact accuracy on held-out rubrics, against 57.1% for TypeSafe's Jev and 49.8% for a Qwen3-8B judge. On eight human-labelled benchmark sets it is within 6 percentage points of Jev's accuracy on most of them, while Jev keeps a larger lead on two and ranks responses best on average; against the results reported in the G-Eval paper, RubriX outperforms G-Eval with GPT-3.5 on every SummEval dimension and both QAGS subsets. With level embeddings cached, RubriX's latency stays at about 28 ms per judgment as level descriptions grow from 10 to 3,000 tokens, while Jev's (approximate network time subtracted) rises from 44 ms to 211 ms and the Qwen3-8B judge's from 32 ms to 516 ms, making RubriX 7.7x faster than Jev and 18.8x faster than the Qwen3-8B judge at 3,000 tokens per level.

---


### 267. [ClinVerse: A Realistic Multi-Agent Diagnostic Environment for Training and Evaluating Medical Agents](https://arxiv.org/abs/2610.34878)

**<font color=#1a73e8>作者：</font>** Sirry Chen, Fangke Chen, Xuanwen Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Disease diagnosis is a key application of large language model (LLM) agents in healthcare. However, existing medical agents are primarily trained and evaluated with static question-answering data, providing limited opportunities to learn active information acquisition, examination decision-making, and dynamic clinical interaction. To address this limitation, we present ClinVerse, an interactive, real-data-grounded multi-agent environment designed for training and evaluating medical diagnostic agents. Built on ClinPatient, a scalable dataset comprising 150k diagnostic cases derived from real-world electronic health records, ClinVerse supports coordinated interactions among six specialized clinical roles. Specifically, a doctor agent starts from an initial patient complaint, progressively gathers clinical evidence through patient interviews and examination requests, and ultimately produces a diagnosis. For each interaction trajectory, a rule-based scoring framework quantifies information acquisition, examination ordering, and diagnostic accuracy. These trajectory-level scores serve as reward signals for agent training while also enabling scalable evaluation. In experiments, we evaluate various general-purpose and medical-domain models and show that nine self-evolution methods across three categories consistently improve agents' diagnostic capabilities within ClinVerse. We further analyze the interplay among model capability, environment feedback, and self-evolution methods.

---


### 268. [MedAdaptAgent: An Automatic Harness for Adapting Medical Imaging Models to New Sites](https://arxiv.org/abs/2610.34884)

**<font color=#1a73e8>作者：</font>** Hanxue Gu, Zhonghao Liu, Xingrui Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reusing pretrained medical-imaging models offers an alternative to training from scratch. A model trained for the same task may perform poorly at a new hospital because imaging protocols and preprocessing differ. Effective adaptation depends on the model architecture, domain shift, and available labels and compute. Adaptation can improve scores on a small labeled set yet reduce performance on unseen data. We present MedAdaptAgent, an automatic harness that turns a supplied model, target data, and a free-text request into a new-site adaptation workflow. Its LLM-driven Adaptation Planner uses model-site evidence to choose compatible experiments and revise subsequent adjustments. The harness requires evidence of improvement over the pretrained model, then delivers the selected model as a complete, runnable package. Evaluation spans 26 segmentation and classification transfers across architectures and compute settings, with segmentation annotation budgets ranging from zero-shot transfer to few-shot adaptation. With 20 local annotations, mean segmentation Dice rises from 0.483 to 0.774 across 10 transfers, a 60.1% relative gain, with no harmful replacements. Mean classification AUROC rises from 0.810 to 0.837 across 13 transfers, a 3.4% relative gain. Comparing adapted models with the pretrained model reduces harmful classification replacements by 30.8% versus selecting the highest-scoring model on the available labels, using identical candidates. Seven public-model deployments demonstrate adaptation and reproducible package delivery across contrast and modality shifts. A CT-to-MRI study extends the evaluation to four LLM planners, including two open-weight models. We release the code on GitHub.

---


### 269. [ThinkBit: Search Codewords, Recalibrate Scales, Select by Reasoning](https://arxiv.org/abs/2610.34886)

**<font color=#1a73e8>作者：</font>** Rhea Sanjay Sukthanker, Pashmina Cameron  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning language models generate thousands of tokens per answer, and generation speed is limited by memory bandwidth, so storing weights in two bits instead of bfloat16 can potentially make inference 8$\times$ cheaper. Two-bit methods are usually judged by perplexity and multiple-choice question-answering accuracy, both of which say little about whether a model can still reason through more difficult problems. We present ThinkBit, a strictly scalar two-bit framework built to preserve reasoning, in which every weight is an integer codeword times a bfloat16 scale shared by a group of weights. We first use a sensitivity metric to assign each layer a ternary, 2-bit, or 3-bit tier to allocate bitwidths optimally among layers. This is followed by a layerwise Gumbel-softmax-based scalar quantization algorithm that searches for optimal codewords block by block. Since a layerwise scheme does not capture how quantized layers interact with each other, we recalibrate scales, with the codewords frozen, using a knowledge-distillation-based loss against the teacher model. We then perform a short quantization-aware training (QAT) stage that lets the model mimic the base model's distribution by reassigning codewords. Finally, a paired reasoning test on training problems selects the final checkpoint between the recalibration stage and the QAT stage. On Qwen3-1.7B at matched size, our recalibrated checkpoint scores 46.7 on MATH-500 against 30.0 for EfficientQAT trained on the same data, and 73.0 after QAT on reasoning traces; at 0.52 GB it is smaller than every published 2-bit GGUF of the model yet more accurate on MATH-500. We show that this framework scales and up to 14B, a 3.74 GB model scores 94.8 on MATH-500, against 97.5 for the 29.5 GB bfloat16 model.

---


### 270. [NumTrace: Auditing the Number Provenance of Financial Analyst Agents](https://arxiv.org/abs/2610.34887)

**<font color=#1a73e8>作者：</font>** Tianlei Zhu, Matt White, Xue Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A numerical claim generated by a financial analyst agent can match a number in a company filing but refer to the wrong entity, concept, period, unit or scope. A check based on reference answers can mark such an answer as wrong but does not explain why it fails. In this paper, we present NumTrace, a new benchmark that audits the provenance of each numerical claim made by financial analyst agents: its source and financial semantics. NumTrace currently has 540 questions over 2,163 SEC EDGAR documents. To the best of our knowledge, it is the first numerical benchmark about who holds a company's shares (Form 13F) and what its executives are owed (Item 402(i)). On a frozen snapshot of these documents, we build the reference answers according to accounting rules. NumTrace then gives each claim three separate verdicts: value, binding and support. By retaining separate value and binding verdicts, NumTrace detects right number, wrong account (RNWA) errors: a claim has an RNWA error when it passes the value check but fails the binding check. The RNWA rate quantifies the gap between value-only and joint value-and-binding pass rates. Finally, we audit three agents, Claude Opus 5.5, GPT-6 Astra and DeepSeek-V4.1-Flash. RNWA errors make up 67.5-81.8% of each agent's failing claims. In particular, on 13F co-filing group questions, about 91% of claims pass the value check, but fewer than half pass the binding check.

---


### 271. [FATE-5: Faithful Alignment of Trait Expression for Continuous Big Five Personality Control](https://arxiv.org/abs/2610.34889)

**<font color=#1a73e8>作者：</font>** Gunhee Cho, Hongyeob Kim, Yun-Gyung Cheong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Controlling personality in large language models is important for building conversational agents that can be customized to different users and interaction settings. However, existing personality control methods often face a tradeoff between strong trait expression and natural dialogue generation. We introduce FATE-5, Faithful Alignment of Trait Expression for the Big Five, a two-stage framework that separates personality encoding from naturalness alignment. FATE-5 first learns continuous soft prompt representations of Big Five profiles using dialogue supervision and an auxiliary survey objective. It then improves dialogue naturalness through preference alignment based on both dialogue quality and personality agreement. Across three language model backbones, FATE-5 maintains strong trait expression while achieving substantially higher dialogue naturalness than other trait-strong methods. On held-out questionnaires, it achieves monotonicity correlations of 0.97-0.99 and recovery RMSE of 8.9-12.4, substantially improving over the evaluated baselines. These results demonstrate effective continuous personality control while maintaining natural conversational behavior.

---


### 272. [SGDB: Semantic-Geometric Decoupling and Evidence Binding for Logical Anomaly Detection](https://arxiv.org/abs/2610.34897)

**<font color=#1a73e8>作者：</font>** Chenrui Ji, Jiafan Lu, Zilu Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Logical anomaly detection requires recognizing scene components and measuring whether their configuration satisfies task constraints. Correct identities can coexist with inaccurate geometry; clean mask fragments can yield misleading lengths. We propose Semantic-Geometric Decoupling and Evidence Binding (SGDB). A semantic decoder learns object identities from component-annotated normal sources and factual edits; a separate reader supplies final measurements. Partial one-to-one association binds geometric witnesses to identities while retaining unmatched objects in the count. A support-certified reader selects mask-derived axes using line quality and complete component ownership. Explicit task requirements and normal-data references define executable checks, with decision thresholds fixed by independent normal calibration. Execution-grounded explanation traces rule contributions to source objects and measurements, extracting compact sufficient alarm certificates. A frozen language model expresses selected outcomes as cited claims, with numeric evidence retained by the executor. Reports preserve observed deviations and unavailable evidence. SGDB achieves 98.19% AUROC and 94.52% fixed-threshold F1 on five MVTec LOCO logical categories, and 93.56% AUROC and 92.76% F1 across all 50 VID-AD tasks. Frozen-output controls evaluate geometric readout and explanatory sufficiency and compactness.

---


### 273. [LE-GDA: Layer Ensemble Gaussian Discriminant Analysis for Training-Free Few-Shot CLIP Adaptation](https://arxiv.org/abs/2610.34901)

**<font color=#1a73e8>作者：</font>** Pavodi Maniamfu, Vogel Kiketa, Zezina Kuzulu Kuetu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free few-shot adaptation of vision-language models typically constructs a classifier from CLIP's final projected image representation, leaving intermediate representations unused. Combining them is not straightforward. Class scores from different representations differ in spread by orders of magnitude for the same query. Direct averaging allocates influence by numerical scale rather than predictive information. We propose Layer-Ensemble Gaussian Discriminant Analysis (LE-GDA), a method that fits regularized shared-covariance discriminants independently to intermediate and final representations extracted in one frozen encoder pass. LE-GDA standardizes each discriminant's class scores per query, selects a small representation multiset on labeled validation data, and combines it with the zero-shot classifier without gradient-based optimization. Across 11 datasets, four CLIP backbones, five shot counts, and three independently sampled K-shot training sets, LE-GDA achieves the highest mean accuracy of all evaluated methods on every backbone, raising the 16-shot mean from 78.01% to 79.54% over a matched GDA-CLIP (final-feature) baseline and improving that baseline for every backbone-shot combination. At one shot, LE-GDA retains a 1.20-point mean gain over the baseline even though covariance estimation is unavailable and per-query standardization is neutral. A control with richer per-class structure inside a single representation does not reproduce the gain, indicating that the benefit comes from combining representations. These results show that intermediate CLIP representations carry information beyond the final embedding and can improve training-free few-shot adaptation. Code and evaluation resources are available at this https URL.

---


### 274. [End-to-End MXFP8 Reinforcement Learning on Blackwell: What Matching Buys, When It Pays Off, and How It Fails](https://arxiv.org/abs/2610.34915)

**<font color=#1a73e8>作者：</font>** Wengee Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-precision arithmetic can make reinforcement learning (RL) for large language models cheaper, but RL requires the sampler and the learner to agree. Several frameworks now run FP8 on both sides. We implement end-to-end MXFP8 RL in verl (Megatron/Transformer Engine training; vLLM and SGLang rollout; dense and MoE models) and measure on B200 GPUs, with Qwen3-8B and Qwen3-30B-A3B, what this design buys, when it is faster, and how it fails. (1) Matching. For an MXFP8 learner, a sampler on the learner's grid is more consistent than a higher-precision BF16 sampler: in one engine at fixed weights, train-rollout KL is 11% lower with half of the sampler's linear layers on the grid and 16% lower with all of them, and the synchronized weights we checked equal the learner's FP8 forward weights byte for byte. On the MoE model, an FP8 pipeline whose sampler uses another grid has twice the shared-grid pipeline's KL from the first step. Without a quantized KV cache, BF16 end to end remains 2.5-10x more consistent. (2) Speed. MXFP8 training adds a fixed cost per micro-batch and saves a per-token cost, so in our dense setting it pays off only above about 4.5k tokens per micro-batch; a micro-batch sweep on identical data confirms the per-micro-batch cost, and a trace shows the GPU waiting for the host for most of the added time. End to end, MXFP8 cuts MoE step time by 10.7% and generation time by 24%, and slows a short-sequence dense workload by 5%. (3) Correctness. We state seven conditions every weight synchronization must preserve and checks that test them against the live engine. Each of the seven failures we met on hardware broke one condition, five silently; the checks caught two at their first opportunity, each missed by the other checks, and CPU fault-injection tests reproduce five. All runs are single-seed and at most 60 steps long; we make no claim about final model quality.

---


### 275. [DiffAuction: An Auction-Driven Framework for Generative Image Advertising](https://arxiv.org/abs/2610.34917)

**<font color=#1a73e8>作者：</font>** Yijie Su, Ruiyang Si, Tonghan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models enable multiple advertisers to compete for exposure within a shared generated image. Yet existing approaches are computationally costly when generating images under varying target-share configurations, and it remains unclear how the resulting outcomes should be evaluated and priced. To address these gaps, we propose DiffAuction, a framework integrating controllable generation, click-intent evaluation, and auction design. First, our training-free Residual Share Calibration (RSC) decomposes joint-attention updates into product-specific residuals and rescales them according to target shares. We further introduce Share-Conditioned Prompting (SCP) to adapt the viewpoint to each desired allocation. Second, we develop an evaluator that uses a VLM to extract visual evidence and an LLM to assess Click-Through Intent (CTI), a proxy for click propensity, along four dimensions: Product Prominence, Brand Recognizability, Scene Integration, and Contextual Value Communication. We validate its assessments against judgments from 10 trained annotators on 1000 images. Third, we formulate this advertising setting as an auction over jointly feasible generation configurations. Each configuration has a public expected CTI vector, while advertisers hold configuration-specific private values per unit of CTI that map click intent into commercial value. We adopt a learnable affine maximizer auction (AMA), which jointly selects a shared generation configuration and determines advertiser-specific payments to maximize expected platform revenue. The resulting allocation and payment rules guarantee dominant-strategy incentive compatibility (DSIC) and individual rationality (IR). Experiments show that our generation method strengthens the monotonic relationship between target shares and CTI relative to baselines, while the learned AMA achieves higher platform revenue in the resulting auction setting.

---


### 276. [PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable Worlds](https://arxiv.org/abs/2610.34921)

**<font color=#1a73e8>作者：</font>** Jinyuan Hu, Yilei Jiang, Chen Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physical reasoning underpins how embodied systems understand and act in the physical world, yet vision-language models (VLMs) remain unreliable on questions about dynamics and physical causality. Progress is critically constrained by the scarcity of grounded counterfactual training data, as observational videos capture only the factual trajectory that occurred. The self-evolving paradigm offers a route beyond fixed datasets by enabling models to construct their own training problems. Extending this paradigm to physics, however, requires an external source of truth that can both validate model-proposed environments and verify alternative physical outcomes under intervention. We introduce \physevolve{}, a verifier-grounded self-evolving framework that trains VLMs for causal physical reasoning from model-proposed executable worlds and simulation-authored tasks. At each round, a shared VLM proposes executable world programs and evidence schemas; a deterministic physics engine freezes each valid world, simulates matched baseline and body-elided counterfactual branches, and synthesizes discrete, answer-bound visual tasks. Exact verifier feedback from task solving updates both the shared policy via GRPO and an adaptive curriculum over physical intents. Starting from Qwen3-VL-8B-Instruct, \physevolve{} achieves targeted gains across PhysBench, CausalPhys, and ContPhy without human intervention data, improving PhysBench Throwing by $8.8$ points and ContPhy Counterfactual Removal and Goal-Pit by $7.4$ and $24.4$ points. These gains concentrate on interaction-sensitive and altered-world questions, demonstrating zero-shot transfer of causal principles to unseen complex dynamics (cloth, fluid, soft bodies) and real-world video.

---


### 277. [GUIFlow: Temporal Redundancy-Aware Incremental Inference for GUI Agents](https://arxiv.org/abs/2610.34959)

**<font color=#1a73e8>作者：</font>** Ye Li, Haoran Ding, Huanan Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI agents built on vision-language models interact with continuously evolving interfaces, yet conventional inference repeatedly recomputes representations of largely overlapping observations and histories. This mismatch makes multi-step interaction costly, while changes in context, interface content, and action arguments prevent straightforward cache reuse. We introduce GUIFlow, a framework for full-pipeline incremental inference in multi-image GUI interaction. Our central insight is that advancing a decision need not require rebuilding all supporting representations: each interaction step can instead selectively update computational states maintained across the trajectory. To support new decisions as the context evolves, GUIFlow adapts how past computation is reused: historical KV states are position-aligned and injected into the current context; change signals guide selective updates of current-observation states in the vision encoder and language model; and earlier action responses serve as speculative drafts verified by the target model. Together, these mechanisms enable cross-step reuse throughout visual encoding, prefill, and decoding without additional training, a separate draft model, or changes to the model-visible inputs and action interface. Experiments demonstrate up to 3.39x geometric-mean speedup across offline multi-image benchmarks and up to 3.49x in online, closed-loop interaction on OSWorld, while maintaining task performance broadly comparable to the dense baseline.

---


### 278. [Adaptive Memory Index Evolution for Agents](https://arxiv.org/abs/2610.34977)

**<font color=#1a73e8>作者：</font>** Yuntong Hu, Tongli Su, Yuanfu Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents continually accumulate experience, yet retaining a memory does not guarantee access when it is needed. Existing systems can adapt both memory content and access; we isolate persistent access updates as a separately controlled adaptation layer. We formulate this target as Memory Index Evolution and instantiate it with Adaptive Memory Index Evolution (AMIE), a lightweight plug-in layer that evolves per-memory access state from deployment retrievals without modifying stored content or retraining the host memory system. AMIE distils a semantic teacher's keep/suppress judgments into a retrieval-conditioned policy and accumulates its selective actions into bounded state that reweights subsequent host retrievals. Surprisingly, even a zero-call policy that simply accumulates retrieval frequency can match or outperform semantic policies in several settings, revealing retrieval traffic itself as a strong signal for access adaptation, while learned selectivity improves robustness when frequently retrieved memories remain useful. Across five retrieval-based hosts and three benchmarks, trained AMIE improves downstream F1 or accuracy in all 15 comparisons, by 0.70--3.37 percentage points (up to 25% relative), and improves retrieval in all 10 comparisons. Controlled analyses show that persistent competitor suppression can expose previously unseen evidence, while suppressing repeatedly useful memories creates the complementary failure mode. Together, these results establish persistent memory access as a practical adaptation layer, distinct from the content it serves, in retrieval-based agent memory systems.

---


### 279. [AskGLP1: A Knowledge Graph LLM Agent for Exploring GLP-1 Experience from Online Patient Narratives](https://arxiv.org/abs/2610.34987)

**<font color=#1a73e8>作者：</font>** Zhaoqian Xue, Anay Somani, Siddhartha Singh 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GLP-1 medications are increasingly used for weight management, and many people share their experiences online. These narratives show why people take the drugs and what they experience, but they remain unstructured and disconnected from formal pharmacovigilance. We therefore present AskGLP1, a system that transforms online patient narratives into a knowledge graph (KG) and answers questions about medication experiences. Through an LLM-assisted pipeline grounded in the MedDRA terminology, AskGLP1 screens nearly 8.5 million Reddit posts for medication experiences and distills 163,135 of them, with 2,506 WebMD reviews, into a KG of 385,790 drug-side-effect and drug-purpose relations. We find that GLP-1 experiences are source- and drug-specific. Online narratives share the most common gastrointestinal symptoms with FAERS, but they foreground everyday burdens such as fatigue and food aversion, whereas FAERS reports more often include injection-site reactions and selected serious diagnoses such as pancreatitis. We further find that posts report less nausea and vomiting for tirzepatide than for semaglutide, more fatigue for Wegovy than Ozempic and for Zepbound than Mounjaro. Evaluations show that the agent answers with verifiable evidence and declines requests for medical advice. Our findings reveal gaps between what FAERS captures and what people report online, and they call for patient-centered approaches to pharmacovigilance. Code, prompts, and evaluation questions are available at this https URL.

---


### 280. [Reason or Recite: Complementary Specialists with an LLM Judge for Traffic Anomaly Reasoning](https://arxiv.org/abs/2610.34993)

**<font color=#1a73e8>作者：</font>** Mayur Kulkarni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Road anomalies such as collisions, violations, and sudden hazards demand more from video understanding than detection: a practical system must verify what happened, describe the scene, and explain the cause. We find these competences pull in opposite directions for vision-language models: closed-form questions reward precise, evidence-grounded reasoning, while open-ended answers are scored by similarity to reference text, where matching the annotation style matters as much as reasoning correctly. We present Reason-or-Recite (RoR), a two-specialist framework for the Traffic Anomaly Reasoning track of the 2026 AI City Challenge. RoR (1) rewrites the official chain-of-thought annotations into a structured, temporally grounded schema and LoRA-tunes a 9B vision-language model on the enhanced traces; (2) fine-tunes a 4-bit-quantized 27B model on answers alone, absorbing the annotation style; and (3) selects between the two candidates per question with a training-free LLM judge. RoR ranks first on the in-domain leaderboard with mean score 0.6788.

---


### 281. [Why Are LLMs Confidently Wrong? Correcting Overconfident Errors via Causal Head Intervention](https://arxiv.org/abs/2610.34994)

**<font color=#1a73e8>作者：</font>** Jing Ren, Bowen Li, Ziqi Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern large language models (LLMs) often exhibit overconfident errors, assigning high confidence to incorrect predictions and thereby undermining reliability in real-world use. Existing calibration methods typically rely on post-hoc adjustment or retraining, operating at the output level without addressing the underlying causes of miscalibration. We propose CoCHI, (Class-oriented Causal Head Intervention), a framework that improves calibration by identifying and intervening on internal components responsible for distinct confidence behaviours. By analysing predictions through correctness-confidence patterns, CoCHI enables targeted intervention on model internals, reducing overconfident errors while preserving correct predictions. Our approach provides a mechanistic perspective on calibration, linking reliability to identifiable structures within the model rather than treating it as an output-level issue. Experiments across multiple LLMs show consistent improvements in calibration metrics, including Expected Calibration Error, Negative Log-Likelihood, and Brier Score, while maintaining accuracy on five multiple-choice question answering benchmarks. These results suggest that effective calibration requires not only adjusting outputs, but also addressing the underlying causal mechanisms within the model.

---


### 282. [When the Persona Contradicts the Line: Diagnosing Plan-to-Synthesis Failures in Chain-of-Thought TTS](https://arxiv.org/abs/2610.35008)

**<font color=#1a73e8>作者：</font>** Joonyong Park, Jerry Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought TTS systems rely on language-model planners to translate persona and context into vocal delivery, but it is unclear where this intent is lost when the requested affect conflicts with lexical sentiment. We introduce a bilingual Japanese--English persona--line conflict benchmark in which each item pairs one line with congruent and conflicting personas and pre-declares the expected acoustic direction. We probe this direction in the planner-generated delivery phrase, the planner-written emotion vector, the QwenEmotion-generated vector, and the rendered waveform. Planner outputs are usually direction-correct, while downstream agreement can be substantially lower. Bypassing QwenEmotion provides only modest gains over the full planner-controlled Base. Supervising QwenEmotion raises the direction rate to 75% in Japanese and 84% in English. A learned text-to-latent interface reaches the highest English rate of 89% and the highest Japanese arousal rate of 88%. These results show that learned repair of the plan-to-synthesis interface can recover counter-textual delivery, although its effect differs across languages and acoustic axes.

---


### 283. [Critic's Eye: Review-Grounded Graph Reasoning for Long-Form Motif Discovery](https://arxiv.org/abs/2610.35011)

**<font color=#1a73e8>作者：</font>** Xinyu Sun, Zhangyue Yin, Xinyi Ju 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep narrative understanding requires distinguishing what happens from how it is presented, moving beyond the chronological fabula to decode the sjuzet, the discursive organization through which themes are staged. We study this through the recurrence of literary motifs (blood in Macbeth, for instance), where symbolic significance emerges not from local cues, but through repetition-with-variation across the whole work. We operationalize this setting as Computational Motif Discovery, a transductive task that predicts missing line-motif links using the full narrative structure of a play. We propose Critic's Eye, which models the work as a heterogeneous Narrative Topology Graph and performs discriminative inference over global structural evidence. Critic's Eye achieves 84.8% Hit@5 on our benchmark, nearly quadrupling state-of-the-art proprietary foundation models (Gemini-3-pro-preview, ~22.6%). Our analysis reveals that despite massive scaling, sequence-based models hit a "semantic ceiling", struggling to resolve dispersed dependencies. These findings suggest that explicit structural priors are a far more effective inductive bias than parameter scaling for decoding the complex architecture of long-form literature.

---


### 284. [Multiscale Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2610.35013)

**<font color=#1a73e8>作者：</font>** Tao Ren, Hui Yang, Jia Deng 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents interact with their environments through complete assistant turns while generating each action token by token. We observe that critic values vary primarily across turns, motivating optimization anchored at turns with finer credit allocation among tokens. We propose Multiscale Policy Optimization (MPO), combining Multiscale Advantage Estimation (MAE) and turn-level importance sampling to align credit assignment and policy updates at the turn scale. Extensive experiments across search, tool-use, and automation tasks with 4B and 30B-A3B models demonstrate consistent gains over strong RL baselines.

---


### 285. [When Pointing Becomes Profiling: Social Bias and Refusal in Text-Steerable Visual Encoders](https://arxiv.org/abs/2610.35017)

**<font color=#1a73e8>作者：</font>** Seyedarmin Azizi, Parsa Razmara, Sajjad Ghiasvand 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-steerable visual encoders condition a frozen Vision Transformer on a natural-language prompt and point at the matching image region, producing prompt-conditioned heatmaps and features. We audit the released SteerViT model and find that its steering interface turns language-driven pointing into demographic profiling. On counterfactual face mosaics and real multi-person photographs, "the person" selects a man more often than the base rate, crime words select Black people more often than occupation words do, "the man" among four women selects the Black woman 75.6% of the time on SocialCounterfactuals, and "the monkey" selects Black people. None of them is in the backbone's unsteered saliency, and the crime association is not in the frozen text encoder; the race effects grow with steering strength and enter through the last two cross-attention layers: giving the prompt to those layers alone reproduces them. Four other grounding models, CLIPSeg, Grounding-DINO, SAM 3, and Qwen2.5-VL, show no crime routing and weaker race routing. The model cannot refuse. Its patch softmax must place its mass somewhere, and its heatmap separates a groundable request ("the police officer") from one that is absent ("the pizza") or that would require a stereotyped demographic inference ("the criminal") only at chance (AUROC 0.52). We introduce SafeSteer, which adds a learned abstention output and counterfactual-invariance training on the same 23M steering parameters. SafeSteer separates should-point from should-abstain prompts at AUROC 0.997, generalizes to held-out sensitive and absent words (0.998; at a 0.5 threshold it refuses 99.8% of trained and 62% of held-out sensitive words) with no over-refusal of visible people on the benchmark, and removes most race routing while keeping localization and retrieval within 1 point of the released model. Code, benchmarks, and the curated mosaic sets will be released.

---


### 286. [BellowsKV: One Latent for Many Layers, Expanded on Demand](https://arxiv.org/abs/2610.35023)

**<font color=#1a73e8>作者：</font>** Jiamu Zhang, Hanjie Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) now serve as the backbone of agents that reason over many turns, call tools, and pursue long-horizon tasks. To avoid recomputation, a model stores the attention keys and values of all past tokens in a key-value (KV) cache. Each layer maintains its own cache, so KV-cache memory can become the main bottleneck for GPU serving. Most compression methods operate within a single layer, by quantizing the cache entries, reducing the channel dimension, or evicting less important tokens. All three lose substantial accuracy at high compression ratios. Cross-layer methods share one compressed cache across adjacent layers to go beyond this limit. However, these methods also degrade sharply at high compression ratios. We find that the KV-cache representations of adjacent layers are quite different, whereas the input hidden states of adjacent layers are highly similar. We also find that, under the same memory budget, reducing the dimension of this shared latent loses far more accuracy than quantizing it. Based on these findings, we propose BellowsKV, a training-free method that maps the hidden states of n adjacent layers to one shared latent per token. At inference time, each layer reads its own keys and values from this latent through a layer-specific projection. We keep the latent at full dimension and compress it in two other ways: BellowsKV-Quant stores the latent at low precision, which is nearly lossless because the latent has no dominant outlier channels; BellowsKV-Evict makes one shared eviction decision per block, because the layers rank token importance very similarly. Across Llama-3.1-8B, Mistral-7B and Qwen2.5-7B, BellowsKV-Quant retains about 99% of full-cache accuracy at 3.6x compression and 97-98% at 13-14x, where the strongest cross-layer method retains at most 84% at 16x. Code: this https URL

---


### 287. [Synthetic Child-Adult Interactions Are Not Developmentally Plausible](https://arxiv.org/abs/2610.35029)

**<font color=#1a73e8>作者：</font>** Bastian Bunzeck, Francesca Padovani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic data has become a common resource for training language models, and this trend has spilled over into research on developmentally plausible language modeling. However, it remains unclear whether LM-generated child-adult interactions actually resemble natural ones. We compare the synthetic TinyDialogues dataset to natural dialogue across a broad range of linguistic measures. While synthetic data matches natural data on the lexical level, it drastically underestimates the messy, fragmented nature of spoken interaction. To mitigate this, we propose instruction-tuning with data created from real dialogues, and show in a pilot study that a small model approximates the statistical tendencies of natural data after moderate parameter-efficient fine-tuning.

---


### 288. [PatentAgentBench: Benchmarking LLM Agents with Professional Patent Task Suites](https://arxiv.org/abs/2610.35031)

**<font color=#1a73e8>作者：</font>** Yijie Hu, Wei Li, Junjie Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Patent practice lies at the intersection of technical, legal, and linguistic work, making it challenging yet crucial to technological innovation. Recently, rapid advances in large language models (LLMs) and agentic systems have demonstrated the potential to complete realistic business workflows and even patent works. This raises a question: can current AI systems perform patent work reliably? Existing benchmarks cover a limited range of patent tasks and simplify evidence acquisition by providing reference materials or candidate documents. In this paper, we introduce PatentAgentBench, a benchmark comprising 510 instances across eight task suites: novelty search, freedom-to-operate (FTO) search, design FTO, invalidity search, claim charting, patent drafting, office-action response, and patent translation. Curated from real patent records and professional materials, the benchmark combines task-specific metrics with expert-reviewed annotations and rubrics. Retrieval tasks such novelty search, FTO, etc., require agents to search and compare patent collections without a supplied candidate pool. The drafting and OAR tasks assess the quality of agents' work given technical disclosure and office action notice. We evaluate seven LLMs across four agent harnesses on PatentAgentBench, finding that current systems still struggle to identify novelty, assess risk, and understand practitioner intent throughout patent workflows.

---


### 289. [SimPOTrans: Self-Adaptation for Offline-to-Simultaneous Speech Translation via Reinforcement Learning](https://arxiv.org/abs/2610.35042)

**<font color=#1a73e8>作者：</font>** Haotian Tan, Hiroki Ouchi, Sakriani Sakti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simultaneous speech translation (SimulST) aims to translate ongoing speech with low latency while preserving translation quality. Recent studies have adopted large language models (LLMs) for SimulST and formulated it as a multi-turn dialogue task for efficient generation, achieving state-of-the-art performance. However, existing dialogue-style SimulST approaches typically rely on specialized training schemes to acquire simultaneous translation behavior, either using synthesized read/write trajectories, which may provide suboptimal training signals, or jointly optimizing translation quality and latency, whose competing objectives may cause optimization instability. In this paper, we introduce SimPOTrans, a reinforcement learning (RL) framework that enables offline speech translation models to self-adapt to dialogue-style SimulST. Through a simple two-stage RL post-training pipeline, SimPOTrans rewards an offline model for exhibiting translation behaviors beneficial to simultaneous scenarios when given partial speech inputs, thereby enabling offline-to-simultaneous self-adaptation without synthesized read/write trajectories or explicit latency optimization. At inference time, SimPOTrans requires no external decision policy and enables flexible quality--latency control by simply adjusting the chunk size of speech input. Experiments on the ACL 60/60 and MCIF benchmarks across three language directions (En$\rightarrow$De, En$\rightarrow$Zh, and En$\rightarrow$Ja) demonstrate that SimPOTrans outperforms several strong baselines, achieving a superior quality--latency trade-off.

---


### 290. [Steering for Safety, Hijacking for Profit: Trojan Threats in the LLM Activation Steering Supply Chain](https://arxiv.org/abs/2610.35043)

**<font color=#1a73e8>作者：</font>** Yu Yan, Jiahao Chen, Siqi Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly integrated into Web search, online recommendation, and intelligent decision-making, the third-party plugin ecosystem centered on model customization continues to grow. Among these, Steering Vectors guide model behavior by intervening in internal representations. However, the open plugin ecosystem also introduces new supply-chain security risks: malicious plugins can disguise themselves as having legitimate functionality and covertly manipulate outputs without significantly affecting model performance. Although this risk poses a real threat, the security issues of Steering plugins in the LLM supply-chain ecosystem still lack systematic research. This paper audits eight mainstream open-source Steering plugin libraries and reveals three structural vulnerabilities: insufficient distribution integrity verification, excessive plugin privileges, and missing runtime monitoring, which offers an attack surface for attackers. To investigate this threat, we propose a malicious plugin, IDH. Specifically, IDH designs a norm-gated mutually exclusive routing mechanism and proposes an information-decay inflection point localization method to automatically select the injection layer, thereby simultaneously achieving benign and malicious functions. To counter such threats, we propose a runtime defense framework, by suppressing anomalous activation interventions and orthogonalizing inter-layer trajectory. We evaluate IDH across five mainstream LLMs, using safety-refusal steering as the legitimate functionality and commercial recommendation manipulation as the hijack objective. Experiments covering six brands across three commercial domains demonstrate that IDH achieves an attack success rate (ASR) of up to 97.8% while preserving high refusal rates on harmful requests.

---


### 291. [LOCUS: Locate Once, Check Until Settled. Draft-and-Verify Visual Grounding with a Box Head and Coordinate-Token Verification](https://arxiv.org/abs/2610.35053)

**<font color=#1a73e8>作者：</font>** Muhammad Talha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) ground a referring expression in one of two ways. They decode the box as coordinate tokens, which is precise but takes one sequential step per token, or they regress it from a hidden state with a small head, which takes one step but loses accuracy at high IoU. The two fail differently: a head usually finds the right object but places its edges loosely, while coordinate tokens place edges precisely. We therefore use the regression head as a speculative drafter for the model's own coordinate tokens. Locus writes the head's box as coordinate tokens and checks them with the same backbone by Jacobi iteration over a shared image prefix. The fixed point is the model's greedy coordinate-token answer, reached in about 5.60 sequential passes on average instead of 18.46 decoding steps; head and verifier are one set of weights, trained jointly. On the 8 RefCOCO, RefCOCO+ and RefCOCOg splits, verification raises Locus-2B's Acc@0.9 from 54.87 for its own head to 59.13, and the one-pass head is ahead at Acc@0.5 of every published model with at most 3B parameters except Florence-2-L. Against Jag, the strongest open regression-head model, at its own size and training budget, Locus ties at Acc@0.5 and, with typical acceptance, gains +4.52 points at Acc@0.9, with paired significance tests. Exact answers come 1.5x faster than vLLM greedy-decoding the same coordinate tokens with the same weights; a pure regression head remains faster still.

---


### 292. [From Questions to Queries to Insights: A Schema-Grounded Agentic Workflow for Natural-Language Crash Data Analysis](https://arxiv.org/abs/2610.35054)

**<font color=#1a73e8>作者：</font>** Jingwen Zhu, Keshu Wu, Steven T. Parker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transportation agencies maintain extensive crash databases to identify safety priorities, evaluate countermeasures, and guide resource allocation. Making these data accessible to practitioners requires flexible ways to translate analytical questions into reliable results. Existing dashboards support predefined analyses, while additional requests often depend on specialists who understand database queries, coded fields, and agency conventions. This study presents CrashDB-QA, a fully local, schema-grounded agentic workflow that enables natural-language analysis of crash databases. Specialized components interpret questions, generate and validate read-only SQL, execute queries, and explain the results. A shared knowledge base grounds query construction in the agency's data dictionary and safety-analysis conventions, while recorded intermediate outputs support inspection and auditing. An optional extension, CrashDB-QA+, checks the alignment among the question, query, and execution result and supplies evidence for iterative repair. We evaluate the workflow on a frozen snapshot of 4.4 million Wisconsin crash records using a new benchmark of 300 questions across ten analytical categories and nine local open-weight models. Domain grounding substantially improves query accuracy, and a code-specialized 7B model provides the best accuracy-latency balance among the tested models. Compositional analyses remain more difficult than routine retrieval, particularly comparisons between groups or periods. Verification improves performance when the Judge uses authoritative field definitions and the Refiner receives execution evidence, whereas additional checking alone offers no consistent benefit. These findings demonstrate the potential of locally deployed, domain-grounded workflows to broaden access to crash analysis and identify the reasoning and verification capabilities needed for reliable use.

---


### 293. [Reinforcement Learning Done Right for Explicit Confidence Targets](https://arxiv.org/abs/2610.35059)

**<font color=#1a73e8>作者：</font>** Zefeng He, Yichen He, Yuan Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can produce plausible but incorrect answers when they are uncertain, which can mislead users and undermine model reliability. Training models to abstain with reinforcement learning is a natural approach, but most existing methods use a fixed error penalty and therefore cannot adapt their behavior to different confidence requirements at inference time. We study \emph{explicit confidence targets}, where a user specifies a target \(p\) in the prompt and the model directly chooses whether to answer or abstain, with the goal of achieving an accuracy of at least \(p\) among answered questions. However, learning to respond to different confidence targets with a single model has proven difficult, and prior attempts have failed to distinguish different targets. We show that this failure comes from two problems: the reward signal that distinguishes different values of $p$ is often lost during optimization, while the original error penalty grows without bound as $p$ approaches one. We propose RLEC (\textbf{R}einforcement \textbf{L}earning with \textbf{E}xplicit \textbf{C}onfidence Targets), which preserves the learning signal needed to distinguish confidence targets, introduces a stable reward family that keeps the desired answer condition unchanged, and uses reward scheduling to balance effective learning and training stability. Together, these designs enable the first successful training of a single LLM for explicit confidence target control. Extensive experiments across diverse benchmarks and model scales show that RLEC largely preserves general capabilities and achieves competitive calibration performance. RLEC also supports fine-grained target control without an external decision system or threshold calibration after training. By making explicit confidence targets part of the trained policy, RLEC opens a new and more direct path toward behavioral calibration.

---


### 294. [MemVLN: Streaming Episodic Memory for Vision-Language Navigation](https://arxiv.org/abs/2610.35066)

**<font color=#1a73e8>作者：</font>** Yan Wang, Jiangyong Huang, Baoxiong Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language navigation (VLN) requires an embodied agent to follow language instructions through 3D environments. Maintaining persistent episodic memory remains a challenge for VLM-based streaming agents in long-horizon navigation. We present MEMVLN, a streaming episodic memory framework that maintains a bounded bank of compressed perceptual features annotated with timesteps and action-derived relative poses, and produces compact memory tokens via cross-attention. We pair the proposed memory with a frozen pretrained geometry encoder. To learn the memory module, we design a masking-based trajectory summarization task with multi-granularity sub-trajectory decomposition, encouraging route reconstruction exclusively from episodic memory. Under navigation training restricted to the official R2R/RxR trajectories, MEMVLN achieves state-of-the-art performance on most reported metrics on standard VLN-CE benchmarks. Long-horizon analyses further characterize when episodic memory is useful. For physical evaluation, we collect 30 instruction-conditioned episodes in one physical scene, use 24 as demonstrations for post-training, and hold out six for testing. On the held-out episodes, MEMVLN improves success over the VLM baseline from 17% to 40%, and post-training further raises it to 47%.

---


### 295. [Beyond Single-Attribute Auditing: A Configurable Multi-Attribute Benchmark for Intersectional Fairness in LLMs](https://arxiv.org/abs/2610.35069)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Yifan Wu, Yuxiang Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly evaluated for fairness, yet most existing benchmarks audit one sensitive attribute at a time. This single-attribute paradigm can miss intersectional harms, where multiple attributes interact non-additively and produce failures that are invisible under marginal evaluation. We introduce ComFair, a configurable benchmark that converts existing fairness data into 479,066 controlled Dual- and Multi-attribute instances and pairs every augmented instance with its task-equivalent source. Across Recognition, Selection, Continuation, and Conversation, this pairing supports a unified audit of performance or bias-score shifts, how often added attributes introduce new errors or mask existing ones, and model-ranking stability. Experiments on ten LLMs show task- and subgroup-dependent sensitivity: discriminative tasks expose both transition directions even when aggregate changes are modest, generative tasks exhibit larger and directionally asymmetric shifts, and rankings vary with attribute composition. ComFair therefore provides a scalable controlled sensitivity audit---rather than a model of the natural joint distribution of identities---for testing the robustness of fairness-benchmark conclusions beyond single-attribute settings.

---


### 296. [Improving VLMs on Scientific Chart Analysis via Autonomous Evolution](https://arxiv.org/abs/2610.35077)

**<font color=#1a73e8>作者：</font>** Abhinav Sudhakar Dubey, Vidushi Goel, Kiran Rana 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding and operating with scientific charts is a standard approach in data analysis, and while humans are good at interpreting such charts, open vision-language models (VLMs) are known to perform poorly when it comes to question answering based on such data types. Motivated by an initial observation that many of their errors are due to inexact answering, we raise the following natural question: how much accuracy can we recover without changing the model at all? In this paper, we study this question by searching over inference programs and the code around a "frozen" version of the model. Using ideas from autonomous evolution (famously used in AlphaEvolve), we first start from a baseline inference program, and in each round we show an LLM judge the code together with a few failures on training questions, and ask for an improving evolutionary move. As usual in autonomous evolution approaches, the candidate programs are kept in a small pool ranked by training accuracy, and the next edit is performed on top-scorers from this pool. We run this approach on three VLMs and four popular benchmarks on scientific charts, and we measure the fraction of descriptive questions whose answer exactly matches the ground truth. The accuracy improves in all experimental settings. On average, it rises from 16.6% with the starting program to 41.3% with the evolved one, and the largest single increase is 55.2 percentage points. As a side benefit, our evolved program is 3.8x faster than the starting program, because short answers are easier to grade and faster to generate. Our results demonstrate that a large part of the observed errors arise due to the inference pipeline, and that optimizing it can improve the "frozen" VLM without the need to retrain it.

---


### 297. [Toward Fast Human Reaction Modeling from High-Frequency Digital Interaction Data](https://arxiv.org/abs/2610.35079)

**<font color=#1a73e8>作者：</font>** Emanuel Dopater, Daniel Gavlas, Lukáš Jochymek 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate whether limbic-like signatures of rapid, salience-driven behavior can be identified in high-resolution Counter-Strike 2 telemetry. This exploratory study introduces Ego-Knowledge, a leak-reduced reconstruction of each player's plausible perceptual state, supported by a millisecond-precision visibility engine and a reaction-centered extraction pipeline. Using a neuroscience-motivated 60--120 ms window, we derive coarse fight-or-flight labels from visibility- and damage-triggered events, with back-damage cases enabling constrained reaction-time analysis and manual label checks. We train two telemetry-native models using only information available by the trigger: EMBER (gradient boosting) and ORBIT (a custom transformer). On the full validation set, EMBER achieves 73.5% accuracy and ORBIT 71.2%, versus a 51.5% majority-class baseline, and both generalize to held-out players. The strongest LLM baseline achieves 62.7% on 1,000 validation cases; on these same cases, EMBER (73.6%) and ORBIT (70.9%) perform better (McNemar p=1.3e-9 and 1.5e-6, respectively), with orders-of-magnitude lower inference time and cost, though the comparison is not compute-matched. Including a short post-trigger window changes forecasting into early response recognition, raising accuracy monotonically to 85.15%. We propose this curve as a candidate probe of the transition from rapid to deliberative control, but roughly uniform per-tick gains do not establish that interpretation. The neuroscience framing is hypothesis-generating, not mechanistic: physiological ground truth, suitable control distributions, and reverse-inference limitations remain open. We outline extensions to auditory reconstruction, larger datasets, and telemetry-native foundation models.

---


### 298. [Zero-Shot Multi-Class Wafer Map Classification with Rule-Ordered Prompts for Large Multimodal Models](https://arxiv.org/abs/2610.35080)

**<font color=#1a73e8>作者：</font>** Tianjian Cao, Jun Tao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wafer-map defect classification often requires labeled data and retraining when production conditions change. We present a training-free six-class framework that combines connected-component highlighting with morphology-, location-, and exclusion-aware prompts for a frozen large multimodal model. On Mixed-WM38 (6,866 maps), multi-region prompting achieves 92.9% macro and 93.8% overall accuracy. On WM811K (9,000 maps), it achieves 79.1% and 81.3%, respectively. Eight alternative rule orders achieve 90.1-91.9% overall accuracy, compared with 93.8% for the selected order.

---


### 299. [Ask Before You Answer: A Question-Driven Evidence Reasoning Architecture (QERA) for In-Context Learning](https://arxiv.org/abs/2610.35083)

**<font color=#1a73e8>作者：</font>** Jinhu Qi, Minda Hu, Wentao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI assistants are increasingly asked to reason over a user's own web traces: group chats, community threads, activity logs and revision histories. On CL-bench Life, a benchmark of such real-life context learning, frontier LLMs solve fewer than one task in five. We find that the request is not the specification: over 80% of the benchmark's rubrics share less than 60% of their content words with the final request, as for a rule set two turns earlier or every record that meets the user's criterion, and LLMs answering directly pass only 67% of these implicit rubrics against 81% of the others. We propose QERA, a Question-driven Evidence Reasoning Architecture that asks before it answers. QERA first turns the request into a requirement checklist and typed information needs, filtered by code for faithfulness to the user's words; it then answers from the whole conversation, asks the same questions again with quotes verified by code, and applies a guarded local repair. It needs no training or rubrics and makes about four LLM calls per task. On all 405 tasks with four frontier LLMs, QERA attains the highest solving rate on every LLM (21.0% on average, against 18.2% for the strongest of three inference-time baselines and 14.6% for direct answering) and leads every baseline significantly when pooled across LLMs, while using fewer tokens than PSCI and 4-5% of the tokens of Ctx2Skill. Ablations on GPT-6-Luna show that the gain is settled before the answer, by a fixed answer protocol (+3.8 rubric points) and the request-specific questions (+1.6), and that it is concentrated on implicit rubrics, with checking afterwards refining mainly numeric requirements.

---


### 300. [Improving Instruction Hierarchy by Learning from Goal-Goal Conflicts](https://arxiv.org/abs/2610.35093)

**<font color=#1a73e8>作者：</font>** Sizhe Chen, Sanjay Kariyappa, Liwei Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The recent incident in which OpenAI agents autonomously compromised Hugging Face's infrastructure illustrates the importance of instruction hierarchy (IH): an LLM should follow lower-priority instructions, such as user requests, only when they do not conflict with higher-priority instructions, such as system policies. IH can be effectively improved by fine-tuning LLMs on simulated examples of instruction conflicts, whose diversity is key to teaching LLMs to properly handle conflicts at test time. However, our decomposition of a task into goals and constraints reveals a conflict type -- goal-goal conflicts -- that is absent from existing IH training sets from OpenAI and NVIDIA. We show the importance of this conflict type: fine-tuning Qwen3.5-9B and Gemma4-12B-it on examples of this conflict type significantly improves IH on a wide range of real-world tasks unseen in training; adding these examples to existing IH training sets for fine-tuning also gives better IH adherence. The IH gains come with trivial mean utility changes on no-conflict tasks across eight benchmarks. Our work advocates including this new conflict type in IH training, even if these examples do not reflect typical LLM use.

---


> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
