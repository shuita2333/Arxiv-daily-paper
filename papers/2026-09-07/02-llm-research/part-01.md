# 🧠 大模型相关研究 | 2026年09月07日

> 本类共 **180** 篇论文：已确认 **169** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-180](./part-04.md)

---

### 1. [Where Does Harness-Optimization Value Live? Localized Gains and the Budget-Splitting Trap in Self-Evolving LLM Agents](https://arxiv.org/abs/2609.02889)

**<font color=#1a73e8>作者：</font>** Michael Nguyen, Wei Chen Tan, Nurul Aisyah Hassan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A growing body of work improves frozen large language models (LLMs) as agents by evolving their harness: the textual scaffolding around the model, including persona, strategy, format rules, and control heuristics. Existing reflective prompt-evolution methods usually optimize this harness as one flat string. We instead ask where the optimization value actually resides. We introduce HARNESSEVO, which decomposes the harness into four separately evolvable slots: role, task-strategy, tool/format-rules, and reflection/control. Using the same reflective optimizer under an iso-budget setting, we pair this decomposition with leave-one-in and leave-one-out attribution to measure the contribution of each slot.
On ALFWorld with a frozen 7B backbone, HARNESSEVO does not significantly improve the overall binary success rate over either the stock harness or flat-string evolution: 0.657 versus 0.642 and 0.642, respectively. However, the slot-level analysis reveals that nearly all useful optimization value is localized in the reflection/control slot, which achieves a leave-one-in gain of +0.119. The other slots are individually null. We further show that uniform budget splitting is harmful: allocating 64 rollouts across four slots leaves only 16 per slot, below the optimizer's effective search floor, causing every slot to freeze at its empty seed. Concentrating the budget on the high-credit control slot recovers the lost gain, reaching 0.761 with half the split budget.
The effect is task-contingent. On WebShop, all slots freeze empty and all methods tie, indicating a genuine absence of recurrent, verbalizable control failures rather than budget starvation. Overall, our results suggest that harness value is localized, uniform budget splitting can be actively harmful, and credit assignment should precede structured agent-evolution.

---


### 2. [Bounded Personas Match Retrieval on Classification but Not Regression for a Frozen Agent](https://arxiv.org/abs/2609.02890)

**<font color=#1a73e8>作者：</font>** JaeHa Yoon, Minjun Park, Seoyeon Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A personalized language agent must convert a user's interaction history into behavior on each new request at inference time. Two strategies dominate. Retrieval pulls a few of the user's most relevant past items into the prompt, which is accurate but pays a per-query selection and context cost that grows with the history. Distillation instead compresses the history once into a compact natural-language persona, which is bounded, query-independent, and interpretable, but is widely assumed to sacrifice accuracy. Whether, and on which tasks, a distilled persona can match retrieval has not been characterized cleanly. We introduce PersonaLink, a training-free method that distills a user's history into a bounded three-field persona and recursively refines it: each pass self-evaluates the frozen agent on a held-out slice of the user's own labeled history, rewrites the persona from its errors, and keeps the result only when it does not regress on that slice. Because every comparison shares one frozen 7B backbone and differs only in what is placed in context, the design isolates the effect of representation from that of the model. The result is a clear task-type asymmetry. On 200 users of LaMP-2 (15-way news categorization), PersonaLink reaches 0.745-0.755 accuracy, statistically indistinguishable from BM25 retrieval (0.760-0.765).

---


### 3. [Probe Generalization as Subspace Selection for OOD Deception Detection](https://arxiv.org/abs/2609.02893)

**<font color=#1a73e8>作者：</font>** Daniel Yoo, Adrians Skapars  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear probes can be used to detect behaviors and concepts inside language model activations, but may fail to transfer to out-of-distribution examples. When studying the generalization performance of Llama-3.1-8B-Instruct probes over 3 held-out deception detection datasets, we find that projecting inputs onto a small subset of principal components (PCs) from the training distribution of activations enables cross-domain transfer that nearly matches the performance of probes trained directly on the test distribution. Furthermore, we find that PC interpretations can be used to find a subset of those transferable PCs. By using an LLM judge to score each PC on whether its most/ least activating examples imply a transferable deception direction, then probing on the highest-scoring PCs, we close the baseline-to-oracle gap by 78% on Insider Trading Report and by 25% on Sandbagging. The directions a source probe weights heavily appear to encode source-specific surface features, while the directions that actually transfer appear to encode the same contrast more abstractly, in a way natural language descriptions can capture. Broadly, our results suggest that the OOD robustness of probes is largely determined by subspace selection.

---


### 4. [R$^{2}$Adapter: A Routing and Rewriting Adapter for Efficient Hybrid RAG](https://arxiv.org/abs/2609.02894)

**<font color=#1a73e8>作者：</font>** Yucan Guo, Miao Su, Saiping Guan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has become a prevailing paradigm for enhancing Large Language Models (LLMs) with non-parametric knowledge. Vanilla RAG efficiently handles simple queries but struggles with relational or multi-hop reasoning. Graph-based RAG alleviates this issue but incurs higher inference complexity and latency. In practice, user queries can differ significantly in their complexity, rendering a fixed RAG strategy suboptimal. However, existing hybrid text-graph RAG methods typically rely on heuristic and LLM-based routing, resulting in unnecessary overhead and strong dependence on the underlying LLM. To address these challenges, we propose R$^{2}$Adapter, a lightweight plug-in Routing and Rewriting Adapter designed to allocate queries between vanilla and graph-based RAG dynamically. By routing only the queries that genuinely benefit from graph-based reasoning, R$^{2}$Adapter reduces unnecessary graph retrieval overhead. Additionally, uncertain graph-routed queries are rewritten to better expose their multi-hop reasoning requirements, improving retrieval quality without additional supervision. Extensive experiments on three multi-hop QA benchmarks demonstrate that R$^{2}$Adapter reduces graph-based RAG usage by up to 59% while maintaining comparable answer accuracy. This adapter is model-agnostic and can be seamlessly integrated into diverse vanilla and graph-based RAG pipelines, providing an efficient and adaptive solution for hybrid RAG systems.

---


### 5. [BharatGather: A Culturally-Informed Benchmark Dataset for Misinformation and Fake News Detection in Indian Public Events](https://arxiv.org/abs/2609.02895)

**<font color=#1a73e8>作者：</font>** Parth Bramhecha, Smit Deshmukh, Sairaj Bodhale 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale public events, such as religious festivals, political rallies, and cultural gatherings, are increasingly vulnerable to the rapid dissemination of misinformation, posing substantial risks to public safety and social cohesion. While automated fake news detection has seen significant methodological progress, existing benchmarks frequently fail to capture the socio-cultural nuances and event-specific dynamics characteristic of the Indian context. This paper introduces BharatGather, a curated, multi-source dataset specifically engineered for binary misinformation classification within the ecosystem of Indian mass gatherings. The corpus comprises 14,646 records constructed through a hybrid pipeline involving systematic web scraping of prominent fact-checking platforms, multimedia transcript extraction, and Large Language Model (LLM)-mediated synthetic augmentation to ensure narrative diversity. By providing a resource tailored to the unique complexities of event-aware misinformation in India, this work facilitates the development of culturally informed detection systems and establishes a rigorous benchmark for evaluating their performance in high-stakes public environments.

---


### 6. [PiPMRE: A Pipeline Based on Language Model for Medical Relation Extraction](https://arxiv.org/abs/2609.02896)

**<font color=#1a73e8>作者：</font>** Jiaxin Duan, Fengyu Lu, Junfei Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical relation extraction (MRE) is commonly known for extracting entities and their relations jointly from a medical text, which has attracted considerable attention in recent years. Previous studies treat MRE as a sequence tagging task, which results in either a challenging design of the tagging schema or a failed extraction of multiple relations, due to intricate relationships among medical entities. In this work, we review the task from the linguistic perspective and propose a novel pipeline framework, PiPMRE, developed on language models to enhance MRE performance. Specifically, PiPMRE consists of a relation generator and a relation filter. Given a text, the generator first yields multiple relational triplets, and then the filter scores each triplet and retains only those that pass the borderline as the final results. Implementing PiPMRE requires no tagging schema; instead, we use a simple template to reformulate the input text, ensuring that entities and relations are generated in a contextual order. Extensive experimental results on two public datasets demonstrate the advancement of PiPMRE. It surpasses the previous state-of-the-art by an average of 5.6 recall points and 4.4 accuracy points. PiPMRE's superiority is also demonstrated in few-shot settings.

---


### 7. [Margins, Not Windows: Training-Free Per-Step Lossy Speculative Decoding](https://arxiv.org/abs/2609.02897)

**<font color=#1a73e8>作者：</font>** Oszkár Urbán, Young D. Kwon, Stylianos I. Venieris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM inference by drafting candidate tokens and verifying them in parallel. Tree-attention drafters such as EAGLE-3 are widely adopted, yet typically hold two decisions fixed: (1) a strict token-match verification rule and (2) a static draft-tree shape. Prior work relaxes each in isolation under limiting assumptions: long draft chains for training-free lossy verification, and adaptive tree shaping under a fixed token budget. We introduce AdaptiveSpec, a training-free per-step speculative decoding method that adapts both decisions from internal signals already produced during decoding. A per-step margin rule promotes a mismatched draft-proposed token when the ratio of the target's probability on the drafted token to its top-1 probability exceeds a threshold with no dependence on draft length or underlying drafter architecture. A per-step tree policy adjusts the draft tree's depth, width, and node count directly from a fused signal of draft top-1 confidence and a rolling acceptance history capturing recent draft-target agreement, allowing the total draft count to vary rather than only be redistributed. The two adaptations operate on orthogonal axes and compound in effect. Implemented on the SGLang production-grade serving engine, AdaptiveSpec improves throughput over the state-of-the-art autoregressive speculative decoding method EAGLE-3 by up to 56%, recovering 93% to fully lossless task accuracy across GSM8K, MATH-500, and HumanEval on three target models (DeepSeek-R1-Distill-Llama-8B, Llama-3.1-8B-Instruct, Qwen3-8B).

---


### 8. [Distilled Rapid Embedding Transfer (DRET): Parameter-Efficient Biomedical Domain Adaptation via Priority-Based Embedding Transfer](https://arxiv.org/abs/2609.02898)

**<font color=#1a73e8>作者：</font>** Girish Sundaram, Daniel Berleant  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large domain-specific language models such as BioBERT and ClinicalBERT achieve strong performance on biomedical NLP tasks, but their computational demands make them impractical for many real-world deployments. General-purpose, parameter-efficient models such as DistilBERT are lightweight yet lack the domain knowledge required for specialized tasks such as PICO (Population, Intervention, Comparison, Outcome) classification. We introduce Distilled Rapid Embedding Transfer (DRET), a knowledge-transfer paradigm that injects biomedical domain knowledge from large specialized models into a smaller general-purpose model without retraining on the original specialized corpora. DRET is developed as an iterative family of strategies: a unified tokenizer-merge strategy (DRET 1.x), hybrid embedding averaging (DRET 2.0), and a priority-based embedding-transfer mechanism (DRET 3.x) that hierarchically selects embeddings from the most authoritative source models, further combined with embedding-layer freezing, differential learning rates, label propagation, and imbalance-aware loss functions (DRET 4.x). We evaluate DRET on token-level PICO classification using the EBM-NLP corpus under severe class imbalance, across a twelve-metric battery. DRET-enhanced DistilBERT (66M parameters) attains balanced accuracy, recall, and ROC-AUC competitive with, and on several class-wise metrics exceeding, models an order of magnitude larger, while retaining DistilBERT's efficiency. We further show that transfer occurs at the embedding level through cosine-similarity, semantic-shift, and t-SNE analyses. DRET offers a scalable, resource-efficient route to near-domain-expert performance for biomedical text mining, with direct application to automated systematic literature reviews and clinical decision support.

---


### 9. [Contamination Inflates Scores but Rarely Reorders Large Language Model Leaderboards](https://arxiv.org/abs/2609.02899)

**<font color=#1a73e8>作者：</font>** Xingyao Xiao, Yihong Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmark contamination, the leakage of test items into training data, is widely described as a threat to the reliability of large language model (LLM) leaderboards. We argue that this concern conflates two distinct questions: whether contamination inflates absolute scores, and whether it reorders the ranking of models. We recast contamination as a violation of anchor-item invariance and measure it through the differential functioning of original versus semantically equivalent paraphrased items, a within-item contrast that holds the measured skill fixed and isolates memorization from capability. Using per-instance responses from 47 publicly released models and 74 models finetuned with a known dose of contamination, across four benchmarks (ARC, GSM8K, HellaSwag, MMLU), we first calibrate the measure against ground truth: it recovers injected contamination dose-responsively (a corrected effect of +0.187 accuracy points for test-set leakage) and never flags a negative-control model trained only on the legitimate training split (-0.012). We then quantify leaderboard impact: the rank correlation between a standard leaderboard and a paraphrase-controlled leaderboard is 0.997, and a sensitivity analysis shows that the observed differential contamination is far below the level needed to move rankings, with only 3 of 188 model-by-benchmark cases showing differential contamination corroborated across two references. Contamination among these public models is therefore largely uniform: it inflates absolute scores without reordering the leaderboard, and ranking distortion requires the rare case of differential contamination. We provide a calibrated invariance audit, released as a reference implementation, and recommend that leaderboards report paraphrase-controlled rankings alongside confidence intervals.

---


### 10. [Dual-Form ASR: Semantics-Aware Inverse Text Normalization for Chinese Speech Recognition](https://arxiv.org/abs/2609.02901)

**<font color=#1a73e8>作者：</font>** Fengrun Zhang, Li Fu, Wangjin Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern automatic speech recognition (ASR) scenarios require both spoken-form transcripts for faithful transcription and readable written-form transcripts with inverse text normalization (ITN). However, these forms are typically produced by cascaded modules, where a spoken-form ASR output is rewritten by a separate ITN component, making written-form ASR-ITN vulnerable to recognition errors and decoupling normalization from acoustic-contextual modeling, especially for semantically dependent numeric expressions. In this paper, we propose Dual-Form ASR (DF-ASR), a framework that extends spoken-form ASR capability to semantics-aware written-form ITN through paired spoken-form and written-form supervision while retaining prompt-level selection between transcript forms. The dual-form supervision is constructed via a large language model (LLM)-driven generate-and-judge workflow, and training is further enhanced by ITN-MWER, a sequence-level objective that assigns higher cost to errors on normalization-sensitive spans. We also introduce a decision-aware REQUIRE-ITN/\FORBID-ITN protocol to separately measure required normalization and forbidden-span preservation. On manually annotated Chinese subsets from SpeechIO, DF-ASR consistently outperforms open-source ASR-ITN systems, remains competitive with strong closed-source references, and preserves reliable prompt-level control between spoken-form and written-form outputs.

---


### 11. [LLM-Guided Reinforcement Learning for Adaptive NPC Behavior in Multi-Agent Combat Games](https://arxiv.org/abs/2609.02931)

**<font color=#1a73e8>作者：</font>** Hrithika Deepu Nair, Kayvan Karim  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Scripted and rule-based non-player characters (NPCs) in combat video games often exhibit predictable behaviors that experienced players can exploit, while reinforcement learning (RL) agents typically retain a fixed policy after training and cannot readily adapt their strategy to different opponents. We investigate a runtime strategy-selection framework in which a large language model (LLM) guides a trained RL policy without modifying its underlying behavior. To demonstrate this, we train five NPC agents with a shared PPO policy in Unity and compare a baseline configuration, in which the policy acts independently, with an LLM-augmented configuration in which a locally hosted Mistral 7B model, accessed through Ollama, reads the live game state every five seconds and assigns one of four tactical tags. We evaluate both configurations against three scripted opponent types across 600 episodes and analyze outcomes using the Mann-Whitney U test. Against a Balanced opponent that changes tactics during an episode, the LLM-augmented agents more than doubled their win rate from 11% to 24% and produced significantly longer episodes. Against an Evasive opponent, the augmented agents achieved a higher win rate and faster kills, although their shorter episode duration did not satisfy the strict hypothesis definition. Against an Aggressive opponent, the LLM's near-constant preference for encirclement was counterproductive. Analysis of 2,430 strategy selections showed that Surround was selected in 83.8% of cases regardless of opponent type, indicating limited zero-shot strategic differentiation at this model scale. These results demonstrate both the potential and limitations of LLM-guided runtime strategy selection for adaptive multi-agent game AI.

---


### 12. [Listen to the Latents: Self-Correcting Speech Recognition in Large Audio Language Models Through Hidden-State Interactions](https://arxiv.org/abs/2609.02940)

**<font color=#1a73e8>作者：</font>** Chan-Jan Hsu, Jaeyeon Kim, Chao-Han Huck Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent automatic speech recognition (ASR) systems increasingly integrate large language models (LLMs) to leverage their semantic knowledge, either externally through logit fusion or internally through warm initialization. However, how to effectively combine these two strategies remains underexplored. In this work, we refine warm-initialized LLM-based ASR models by leveraging their own pre-adaptation base LLMs, focusing on LoRA-adapted settings where the base LLM is preserved. To achieve this, we propose Hybrid Search, a targeted correction strategy motivated by two observations. First, interaction features that characterize the relationship between LLM-based ASR hidden states and base-LLM hidden states provide informative signals about a token's degree of semantic dependence. Second, selectively refining targeted tokens with high semantic dependence improves ASR performance far beyond naive global LLM-correction methods including rescoring and late fusion. Our analysis suggests that, even after semantic knowledge transfer through warm initialization, LLM-based ASR models can still leverage their base LLM to further improve inference-time performance.

---


### 13. [Judging LLM-as-a-Judge: Concerning Rubric Artifacts in LLM-based Automated Text Generation Evaluation](https://arxiv.org/abs/2609.02942)

**<font color=#1a73e8>作者：</font>** Anshul Bagaria, Sowmya S Sundaram, Gokul S Krishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge pipelines are increasingly used to evaluate AI-generated text, based on the assumption that judgments arise from reasoning over candidate responses with respect to a rubric. We show that this assumption warrants further scrutiny. Classifiers trained only on rubric text, without access to any evaluated response, achieve nontrivial predictive performance on judge outputs. This suggests that rubric formulations encode recoverable evaluative signals, allowing scores to be partially anticipated independently of model outputs. Finally, counterfactual perturbations reveal that judges often fail to reliably update their decisions when either the candidate response or the rubric criterion is reversed. Our findings raise concerns about the reliability of rubric-based LLM evaluation and highlight the need for further methodological study of automated evaluation via LLMs.

---


### 14. [Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis](https://arxiv.org/abs/2609.02947)

**<font color=#1a73e8>作者：</font>** Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Significant challenges remain in AI-driven educational systems in balancing privacy preservation with accurate cognitive diagnosis. To overcome this, we propose a federated inference framework in which several commercial LLM APIs collaborate without requiring access to raw student data or proprietary model internals. Using multiple federated entities, such as LLaMA-3.3-70B, GPT-4o-mini, and Claude-3-Haiku, our framework builds upon a heterogeneous multi-LLM architecture. The predictions generated by these entities are combined with epsilon-local differential privacy by adding Laplace noise locally to each entity's prediction output before aggregation, while residual-based aggregation mitigates model heterogeneity. Our approach is predicated on an honest-but-curious trust paradigm in which API providers are presumed not to abuse submitted queries, and our differential privacy mechanism shields the published diagnostic results from external inference. We conduct rigorous privacy-utility analysis showing strong privacy guarantees with minimal accuracy loss, and extensive real-world evaluations across three educational benchmarks confirm the framework's practical usability and cross-domain generalizability.

---


### 15. [LexIssue: Benchmarking Legal Issue Identification in Chinese Civil Litigation](https://arxiv.org/abs/2609.02954)

**<font color=#1a73e8>作者：</font>** Huiyuan Xie, Yuqin Huang, Zhicheng Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying the issues disputed between litigating parties is a crucial component of real-world litigation. However, legal issues remain comparatively underexplored in legal AI research. In this work, we study the computational modelling of legal issue identification in litigation. We introduce a legally grounded hierarchical schema that represents legal issues through both free-form issue descriptions and structured legal categories, and formulate legal issue identification as two complementary tasks: legal issue generation and legal issue classification. Based on this formulation, we construct LexIssue, a benchmark containing 430 real-world Chinese civil litigation cases and 1,303 expert-annotated disputed legal issues. We further develop an issue-centric legal knowledge base spanning 27 causes of action and 441 candidate legal issue entries to support retrieval-augmented reasoning. Experimental results across a diverse set of models show that retrieval-augmented generation using the constructed legal issue knowledge base consistently improves performance in identifying disputed legal issues and their corresponding legal attributes.

---


### 16. [The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors](https://arxiv.org/abs/2609.02959)

**<font color=#1a73e8>作者：</font>** Toni J.B. Liu, Jiajun Bao, Yizhou Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What does a language model predict when it has few clues? The answer lurks in its unembedding geometry: a single direction of the unembedding matrix encodes the unigram distribution of the training corpus, which serves as the Bayesian prior the model falls back on when uncertain. This structure --- which we term the \emph{direction of ignorance} --- appears in all four model families examined (\texttt{Llama}, \texttt{Qwen}, \texttt{Gemma}, and \texttt{Pythia}), ranging from 0.4B to 405B parameters. Projecting the final prediction state onto this direction yields a per-token \emph{prior loading factor} $\lambda$, which, empirically, declines steadily as the context becomes more informative. Formally, the same projection decomposes the prediction state into two orthogonal vectors that correspond exactly to the two factors of a tempered Bayesian update: a unigram prior raised to the exponent $\lambda$ and a context-driven likelihood. This geometric-probabilistic interpretation calibrates $\lambda$, making it meaningfully comparable across model sizes and families, with larger models generally exhibiting lower prior reliance in the high-context limit. Finally, we show that the direction of ignorance is causally active: raising or lowering $\lambda$ at the final prediction state steers the prediction toward or away from the unigram prior in KL divergence.

---


### 17. [When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization](https://arxiv.org/abs/2609.02964)

**<font color=#1a73e8>作者：</font>** Haozhang Li, Yangguang Shao, Xinjie Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper focuses on defending generative search engines against malicious Generative Engine Optimization (GEO), which rewrites web documents to match engines' citation preferences and thereby manipulates generated answers. Recent GEO methods have advanced from hand-crafted rewriting to automated and agentic optimization, substantially increasing the visibility of target documents in generated answers. However, defending against such manipulation poses two major challenges: attack documents remain factually consistent with their originals, rendering fact verification and perplexity filtering ineffective, and the features they amplify equally characterize high-quality benign content. To address these limitations, we propose GEO Defender, a two-stage defense aligned with the attack chain that requires no fine-tuning of the target LLM. GEO Defender consists of Shield Reranker and Training-Free Shield Generation (TFSG). Specifically, Shield Reranker learns a preference-based defensive residual over a frozen base reranker, demoting GEO-rewritten documents while preserving relevance judgments, and TFSG distills defense outcomes into a natural-language experience library that guides the target LLM's source use at inference. Experiments on two state-of-the-art closed-source LLMs and three open-source LLMs across seven GEO attacks demonstrate that GEO Defender reduces the average attack success rate from 50.32% to 6.20%, retains 94.12% of benign-evidence use, preserves answer quality, and generalizes to unseen attacks from construction instances.

---


### 18. [Privacy-Preserving Topology-Guided Safety for LLM-Based Multi-Agent Systems via Federated Graph Learning](https://arxiv.org/abs/2609.02967)

**<font color=#1a73e8>作者：</font>** Jinxi Yu, Eric Hanchen Jiang, Levina Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Topology-guided safeguards for LLM-based multi-agent systems (MAS) train a GNN over the inter-agent communication graph to localize risky agents and intervene on the topology---but they assume one operator can pool all labeled traces. Across organizations that assumption breaks: episodes contain private prompts, tool outputs, and proprietary workflows, and no silo alone sees the full attack distribution. We cast privacy-preserving MAS safeguarding as graph federated learning and instantiate FGLGuard: each operator fits an edge-featured graph attention detector on its own judge-labeled episode graphs and shares only model updates. The method couples a proximal local objective for non-IID clients, domain-balanced aggregation, over-refusal-constrained threshold calibration, corroborated upstream scoring, and a guarded rewrite for blocked answers. Federation is not optional: off-the-shelf transfer collapses under distribution shift (AUROC 0.51 to 0.70 only after in-domain retraining), so a deployable guard must adapt on each site's private traces. On Agent-SafetyBench, R-Judge, and AgentDojo, federated FGLGuard exceeds the in-domain centralized ceiling on all three benchmarks without pooling any data---where unsupervised anomaly guards and local-only training fail. One guard federated across four different-domain operators comes within 0.03 AUROC of multi-domain centralization, while any single-domain guard collapses on the others. Live FGLGuard cuts AgentDojo's ground-truth attack-success rate by 43% at near-unguarded utility, zero API cost, and negligible capability loss.

---


### 19. [Modern Transformers Are Implicit Hybrids: From Functional Differentiation to Principled Hybrid Architecture Design](https://arxiv.org/abs/2609.02986)

**<font color=#1a73e8>作者：</font>** Runlin Shi, Bojian Yin, Guoqi Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid architectures combining Full Attention (FA) and Linear Attention (LA) are increasingly prominent, yet their allocation remains heuristic. We seek an evidence-grounded basis in head-level functional organization learned by RoPE-based Transformers. Behavioral probes do not yield a complete taxonomy, so we propose two intervention metrics: RoPE Frequency Importance Score (RFIS), measuring how each frequency affects a head's attention distribution, and RoPE Positional Dependence (RPD), isolating dependence on rotary positional modulation. On Qwen3-series models and Llama3.1, RFIS suggests and RPD verifies a complete taxonomy of retrieval and positional heads separated by a salient mid-low-frequency band. Controlled Transformers show that this boundary follows the training-length positional scale; we term it the Global Positional Band (GPBand). The analysis suggests a potential cause of zero-shot length-extrapolation failure and yields two principles: positional modeling should operate only locally, with global access through position-independent retrieval; and both functions should be assigned at head granularity with layer-specific allocation. We instantiate them in Head-wise Hybrid Architecture (HwH), using NoPE FA for global retrieval and LA for local positional modeling. With an FA-to-LA ratio below 1:3, HwH retains strong language modeling and commonsense reasoning while improving retrieval and substantially strengthening zero-shot long-context extrapolation over Transformer, LA, and a layer-wise hybrid baseline. Ablations validate both principles and component roles, highlighting principled hybrid architecture design as a promising route toward future foundation models.

---


### 20. [Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation](https://arxiv.org/abs/2609.02998)

**<font color=#1a73e8>作者：</font>** Zhiwei Zhang, Zechen Sun, Fei Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) accelerates post-training by providing dense token-level supervision from a frozen teacher on the student's own rollouts. Vanilla OPD applies this supervision uniformly across prompts, without checking whether the teacher is reliable for each prompt. Because reverse KL is mode-seeking, a confidently wrong teacher can induce a strong yet misleading update. Distributional proxies, such as entropy or teacher-student likelihood agreement, measure uncertainty or agreement but do not directly verify outcome correctness. We introduce Teacher-Gated On-Policy Distillation (TGOPD), built on the principle that teacher reliability should be verified at the prompt level before dense supervision is admitted. TGOPD estimates reliability from a small set of verifier-scored teacher probes and routes each prompt exclusively to dense OPD when the reliability check passes or to verifier-grounded GRPO otherwise. Across 4B and 35B students in mathematics, code, and instruction following, TGOPD outperforms Vanilla OPD in all six single-domain settings and achieves higher seven-benchmark averages at both scales under multi-domain training. By using otherwise-idle teacher capacity for reliability estimation, TGOPD also reduces teacher-side compute waste in asynchronous OPD, increasing teacher-node GPU utilization from 9.8% to 78.9% in the measured 4B single-domain run.

---


### 21. [Unifying Conformal Language Tasks with In-Context Ensembles](https://arxiv.org/abs/2609.03005)

**<font color=#1a73e8>作者：</font>** Xiao Shi Huang, Chen-Yuan Lin, Bruce Kuwahara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many NLP tasks, such as summarization and extractive question answering, reduce to retrieving relevant content from documents under two constraints: coverage, retaining enough pertinent information to achieve some goal, and conciseness, removing as much irrelevant information as possible. Conformal prediction methods have been used to guarantee coverage, and must be optimized for conciseness through design of a score function. State-of-the-art scoring functions use hand-engineered LLM prompts asking the model to rate the importance of content, but manual prompt engineering is labor-intensive and task-specific. We introduce the Conformal Relevance framework which uses in-context learning example curation and ensembling to create a score function which maintains coverage while improving conciseness with minimal manual input. We demonstrate this framework's application on seven NLP tasks, and also theoretically study the impact of diversity for ensembled conformal scores, giving a complementarity condition that characterizes when ensembling improves worst-case sentence scores, and a saturation bound on ensemble improvement.

---


### 22. [ObserverBench: Testing Mechanistic Estimates for Intervention and Control](https://arxiv.org/abs/2609.03026)

**<font color=#1a73e8>作者：</font>** Vijay Erramilli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability is increasingly used to guide interventions such as activation steering, circuit removal, and safety monitoring. Yet an internal estimate that is accurate on average can still choose a poor action.
We present ObserverBench, a benchmark framework for testing whether an internal estimator---an observer---is adequate for the intervention, control, or safety task it directs. Each task fixes the model, information boundary, allowed actions, decision rule, held-out cases, and loss. The benchmark reports estimation accuracy separately from the loss caused by the chosen action.
Theory and experiments show why both are needed. In closed-loop control, observer errors matter at the starting point and along directions the allowed intervention can reach. On circuit-intervention tasks in GPT-2-small and Qwen2.5-7B, pairwise observers predict unseen effects more accurately without always choosing better actions; observers trained on action loss choose lower-loss actions. In safety triage, a score that perfectly separates violations can allocate a fixed intervention budget poorly when violations have different costs. Across Qwen2.5-7B, Gemma-2-9B-it, and prospectively frozen Qwen3.5-9B APPS tasks, AUROC can rank monitors differently from deployment loss, and the best information source changes across models. Sparse SAE readouts also trail their layer-matched dense controls on the reported Qwen panels, under disclosed activation-density or checkpoint mismatches.
ObserverBench provides fixed task contracts, runnable baselines, and table-based submissions for evaluating interpretability methods through the actions they enable.

---


### 23. [You Can't Escape Your Own Activations : Evaluation Awareness and Multi-Agent Monitoring](https://arxiv.org/abs/2609.03035)

**<font color=#1a73e8>作者：</font>** Aritra Das, Jaee Ponde, Mihir More 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly deployed in multi-agent systems, where they can collude while keeping their actions benign. Output monitors designed to detect such collusions can be fooled by obfuscation and steganography, motivating the use of probes trained on internal activations. However, these probes are usually evaluated on agents that do not know they are being watched. We study how activation-based detection changes when agents are explicitly informed that their internal activations are being monitored, and when they additionally receive feedback from the monitor. We keep the models, probes, and thresholds fixed and change only what the agents are told: nothing (baseline), that an activation monitor is present (aware), or that a monitor is present together with the previous round's score (feedback). We test two games, a four-agent blackjack game and a two-agent Simmons prisoners game, using Qwen3-32B-AWQ and GPT-OSS-20B in homogeneous and mixed pairings. Telling agents about the monitor does not hide them. The best probes stay accurate in all three conditions, and the agents keep colluding.

---


### 24. [SHELF: A Synthetic Harness for Multi-Task Bibliographic Benchmarking](https://arxiv.org/abs/2609.03047)

**<font color=#1a73e8>作者：</font>** Michael J. Bommarito II  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Libraries and archives manage large collections with limited staff and computing budgets, yet common benchmarks do not systematically test their bibliographic work. They need to know which methods work for their tasks and what those methods require to run. SHELF, the Synthetic Harness for Evaluating LLM Fitness, addresses this gap. It is a Python system that turns labelled taxonomies, writing specifications, and a generation budget into controlled benchmark data and evaluation tasks. This first release contains 62,899 model-written documents based on Library of Congress vocabularies, with tasks for classification, clustering, retrieval, pair classification, and instruction retrieval. We compare TF, TF-IDF, BM25, popular encoders, and, on subject classification only, zero-shot decoders; each method appears only on tasks that support it. Subject classification reaches 0.8887, while genre-form classification reaches only 0.2605, and several pair and clustering tasks remain near chance. Sparse methods remain competitive on classification, while TF-IDF is the fastest measured arm in the subject timing experiment. SHELF also varies bibliographic facets independently and can generate new, verifiably unseen documents after a model's training cutoff. Comparisons with LCSHBench and Project Gutenberg show that model rankings transfer more reliably than absolute scores, but SHELF scores do not estimate accuracy on production catalogue data. We release all source code and data under permissive licenses on GitHub and Hugging Face.

---


### 25. [LeanStream: A Speculate-and-Refine Streaming Framework for Efficient on-Device LLM Inference](https://arxiv.org/abs/2609.03079)

**<font color=#1a73e8>作者：</font>** Renyuan Liu, Yuyang Leng, Kaiyan Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device LLM inference is attractive for privacy and responsiveness, but remains challenging on mobile and embedded devices because model weights far exceed available DRAM. Prior systems exploit activation sparsity and offload weights to SSD or flash storage, but face a fundamental systems trade-off: accurate sparse execution decisions require the latest context, whereas efficient computation-I/O overlap requires early prediction. As a result, existing designs either serialize execution or incur redundant weight fetches, extra computation, and large cache overheads. We present LeanStream, a streaming speculate-and-refine framework for efficient on-device LLM inference. LeanStream progressively refines computation, loading, and cache-retention priorities using partial GPU results, enabling fine-grained overlap between GPU execution and storage I/O. We implement LeanStream on both mobile and embedded platforms. Compared with prior on-device LLM inference systems, LeanStream reduces memory usage by 4.8$\times$ to 7.5$\times$ at the best throughput achieved by prior work, while further improving token generation throughput by 1.6$\times$ to 2.1$\times$.

---


### 26. [Solving the Needle-in-a-Haystack Problem in Mammography Vision-Language Model with Differentiable Subset Sampling](https://arxiv.org/abs/2609.03085)

**<font color=#1a73e8>作者：</font>** Young Seok Jeon, Beatrice Brown-Mulry, Rohan Satya Isaac 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> There is growing interest in adopting CLIP-style vision--language model (VLM) pretraining for mammography. However, models that directly employ the standard CLIP architecture and training objective exhibit limited zero-shot performance in clinically important tasks such as cancer, finding-type, and BI-RADS predictions. We argue that this underwhelming performance is due to neglecting two characteristics of mammography data: (1) its high-res nature, and (2) homogeneity of radiology reports, largely driven by a predominance of negative/benign findings on examinations. We propose TopKSigLIP, a VLM designed to address these two limitations through a novel architecture and learning objectives. Instead of downscaling high-res mammography images to satisfy GPU memory constraints, TopKSigLIP introduces TopK-Patch module that learns to sample a sparse set of high-res patches likely to contain lesions, sidestepping the resolution--batch size tradeoff of VLM training. The sampled patch locations additionally serve as a built-in localization tool. To address report homogeneity, we replace the contrastive loss, which falsely repels semantically similar pairs, with a Sup-sigmoid loss. Sup-sigmoid loss extends the sigmoid loss from SigLIP with soft labels derived from structured data. TopKSigLIP outperforms existing open-source mammography and general medical VLMs on both internal and external benchmarks on density assessment, BI-RADS classification, finding subtyping, and cancer prediction under zero-shot evaluation. TopKSigLIP remains competitive under linear probing despite using a significantly smaller vision encoder and smaller training batches than baselines. The TopK-Patch module additionally achieves superior lesion localization over post-hoc Grad-CAM. Code and weights are made public:this https URL.

---


### 27. [The Gradient Does Not See Rank: Rank-Indifference in Matrix-CODI on ProsQA](https://arxiv.org/abs/2609.03090)

**<font color=#1a73e8>作者：</font>** Samuel Larson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous chain-of-thought models compress reasoning into latent tokens. Matrix-valued variants, which route each latent token through a d x d matrix bottleneck, introduce rank as a single-sample structural observable on the latent matrix Z. If matrix latents carry parallel reasoning paths via superposition, rank should track them, and truncating Z to low rank should hurt accuracy on tasks whose solutions plausibly require multiple components. Across four training regimes of a matrix-CODI model (three on ProsQA, one on GSM8K-Aug below the learning threshold), the rank-k projection ablation curve is flat to within 0.6 percentage points. A three-seed replication yields 81.0 +/- 2.0 percentage points accuracy while the final effective rank of Z spans {4, 12, 13}; the loss does not reward any particular rank. To test whether rank-blindness arises from the flatten-then-project readout alone, we trained four readouts: a bilinear reparametrization, a bilinear-plus-GELU readout nonlinear in Z, an SVD-augmented readout feeding singular values through an MLP, and a quadratic readout in Z Z^T. All four rank-k curves remain flat (Spearman p-values 0.63, 0.14, 0.82, 0.46). The flat curves persist for readouts nonlinear in Z. A linear probe on Z underperforms a raw pretrained hidden state at target prediction (AUC 0.673 vs. 0.846). A negative control on vanilla GPT-2 SFT (no matrix bottleneck, no Z, three seeds, n=500) reproduces a flat rank-k curve under the same intervention paradigm with pooled-mean range 0.20pp, and a random-h sensitivity floor lands at the same accuracy: the rank-k ablation alone conflates rank-blindness with position-irrelevance.

---


### 28. [SLIDEFORGE: An LLM Agent for Controllable Editing of Slides as Structured Artifacts](https://arxiv.org/abs/2609.03109)

**<font color=#1a73e8>作者：</font>** Haozhen Zheng, Fulin Wang, Tianhu Xiong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current AI agents compellingly describe slides. However, AI-assisted slide editing requires more than understanding: the output must retain layout, style, component structure, and native editability. Towards, AI-assisted slide editing, existing agents operate on screenshots or weak document representations and often fragment coherent visual units, rasterize editable content, or break layout. In contrast, for controllable slide editing, we introduce an agentic framework, SLIDEFORGE, which builds a Deck State Graph, an executable slide state that links visual decomposition, native pptx object structure, and perceptual organization. By recovering human-referable components while retaining fine-grained editable structure, SLIDEFORGE supports theme-preserving reconstruction through slide-native operations and rendered-state verification. We further introduce an evaluation paradigm for controllable slide transformation that jointly measures component recovery, preservation, restyling consistency, visual quality, and native editability. Experiments show that SLIDEFORGE outperforms direct prompting, screenshot-based agents, and generic code-agent baselines across these dimensions. Code is available at this https URL.

---


### 29. [Large Language Models in Resolving Contextual Knowledge Conflicts](https://arxiv.org/abs/2609.03148)

**<font color=#1a73e8>作者：</font>** Xinye Yang, Zhenyang Liu, Ruisi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most prior works focused on conflicts between an LLM's internal parametric knowledge and externally provided context. In contrast, we investigate how LLMs handle conflicts that arise within contextual knowledge itself. We introduce a taxonomy of six types of contextual conflicts (factual, inferential, temporal, granularity, perspective, and ambiguity) and contribute a comprehensive dataset ContextConflict for this setting. The dataset contains 5,781 samples, covers both reasoning and summarization tasks, and includes both explicit contradictions and implicit conflicts that require multi-step reasoning. Experiments on nine LLMs show that current models still fall short in resolving contextual knowledge conflicts. We further provide mechanistic interpretability insights into how LLMs process such conflicts, revealing their latent awareness of conflicts and the representational geometry underlying conflict processing. In addition, our analysis uncovers a consistent model bias towards earlier evidence, and this positional preference serves as a key obstacle to effective conflict resolution. Motivated by these findings, we further propose a simple training-free, label-free steering method that steers activations to encourage a more comprehensive incorporation of evidences for better conflict resolution. On our dataset, the method consistently improves accuracy on reasoning tasks and generates higher-quality, more balanced summaries for summarization tasks.

---


### 30. [Routing Is Not Enough: Diagnosing Intra-Adapter Subspace Contention in MoE+LoRA Fine-Tuning](https://arxiv.org/abs/2609.03150)

**<font color=#1a73e8>作者：</font>** Mehreen Hossain Chowdhury, Nowshin Mahjabin, Ahmed Shafin Ruhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-domain fine-tuning often combines MoE routing with LoRA, assuming that token-level routing separates domain-specific updates. We test this assumption in MoE+LoRA using Python code paired with biomedical text and mathematical reasoning. Although these domains show near-disjoint expert routing, adding biomedical data substantially increases code perplexity, indicating that routing separation alone may not prevent negative transfer. To localize the failure, we introduce Jaccard routing overlap and adapter-gradient cosine similarity, which measure expert sharing and update compatibility, respectively. These diagnostics indicate that interference arises mostly from nearly orthogonal domain gradients competing within the same low-rank adapter subspace. We address this issue with SpawnLoRA, which dynamically adds gated sub-adapters inside MoE experts when adapter-level contention is detected, while keeping the router fixed. We evaluate SpawnLoRA on Phi-tiny-MoE-instruct and OLMoE-1B-7B across multiple mixture settings and find that it effectively reduces negative transfer compared with standard and rank-adaptive LoRA. These results demonstrate that structural separation inside experts provides benefits beyond routing or rank expansion alone.

---


### 31. [Who Speaks for the Pruned? Visual Token Pruning as Coverage Optimization](https://arxiv.org/abs/2609.03158)

**<font color=#1a73e8>作者：</font>** Qingchan Zhu, Weihang You, Hanqi Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning reduces the inference cost of vision-language models (VLMs), but most methods only ask which tokens to keep. This retained-token view can keep redundant high-scoring tokens while leaving discarded evidence without a close representative. We propose CoverPruner, a training-free pruner that asks the complementary demand-side question: after a token is removed, which surviving original token represents it for the target VLM? CoverPruner formulates pruning as Representational Coverage Maximization (RCM), covering the full projected visual-token set with query-weighted demand. It instantiates RCM with projector-space coverage and a lightweight first-layer attention probe. Across multiple VLM architectures and compression rates, CoverPruner achieves the best average accuracy among all compared methods, with the largest gains usually appearing under aggressive compression.

---


### 32. [No country for old linguists: LLM-brain alignment underdetermines neural computation](https://arxiv.org/abs/2609.03160)

**<font color=#1a73e8>作者：</font>** Elliot Murphy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nastase et al. (2026) argue that large language models (LLMs) may illuminate language processing because both rely on distributed, context-sensitive representations shaped by statistical learning. Their rejection of simple cortical "boxology" is persuasive, and they articulate a strong case for the value of LLM-brain alignment research. The key question is what kind of inference LLM-brain alignment licenses. My claim here will be narrow: representational alignment can in principle constrain mechanistic hypotheses, but it does not by itself identify a mechanism. Nastase et al. acknowledge that an encoding model can capture features represented in neural activity without establishing a shared architecture or algorithm. Yet the authors sometime move from alignment to "shared computational principles" and ultimately to LLMs as mechanistic models of natural language. Indeed, their methodological caveat that alignment does not establish a shared architecture or algorithm sits uneasily with their conclusion that LLMs might instantiate the same computational principles as biological brains and provide a "fully mechanistic model" of language. I discuss what I consider to be problems of logical, causal, and computational underdetermination in Nastase et al.'s (2026) proposal.

---


### 33. [Frontier LLMs are effective batch optimizers: Assessing reasoning models in continuous and discrete settings](https://arxiv.org/abs/2609.03177)

**<font color=#1a73e8>作者：</font>** Frank Hu, Shriram Chennakesavalu, David Graff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier large language models (LLMs) have become attractive priors for optimization due to their large-scale pretraining that enables them to navigate a variety of optimization settings. However, the effectiveness of modern reasoning LLMs in batch optimization settings remains underexplored. Here we investigate the performance of the current generation of frontier LLMs as batch optimizers in both continuous and discrete settings. We find that while LLMs are competitive zero-shot batch optimizers for numerical test functions, their performance is brittle compared to classical non-LLM optimization approaches. However, LLM priors are significantly better in semantically rich settings, indicating that their batch optimization behavior is highly effective when navigating and reasoning over the discrete spaces most similar in structure to their pretraining data.

---


### 34. [Jina-OCR-v1: Efficient Document Parsing with Speculative Decoding and Dense Verifiable Rewards](https://arxiv.org/abs/2609.03181)

**<font color=#1a73e8>作者：</font>** Alejandro Barón García, Feng Wang, Emilia Garcia Casademont 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Jina-OCR-v1, an end-to-end document parsing model built to serve on low-budget GPUs. It combines the compressed-vision encoder and the 3B mixture-of-experts decoder of DeepSeek-OCR, which activates about 570M parameters per token, with a FastMTP speculative decoding head that shares a single draft block recursively across K=3 prediction steps. Greedy verification makes decoding lossless. Post-training combines instruction alignment, robustness fine-tuning on difficult documents, and GRPO under dense verifiable rewards: deterministic formula, table, and structural checks that award partial credit. The training data mixes cleaned public corpora with targeted synthetic pages. At the default dynamic-resolution setting, Jina-OCR-v1 scores 91.14 on OmniDocBench v1.6 and 83.4 on olmOCR-Bench, and reaches the highest page throughput in our comparison at 2.57 pages per second. On a low-budget GPU such as the NVIDIA L4, FastMTP doubles decoding speed over greedy autoregressive decoding. The model is publicly available at this https URL.

---


### 35. [Where Reliability Lives: Experimental Localisation of Behavioural Properties in an Agent System](https://arxiv.org/abs/2609.03192)

**<font color=#1a73e8>作者：</font>** Timothy Marsden, Matthew Collecutt, James Marsden  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Reliability claims about agentic systems implicitly locate each property somewhere: in the model, or in the machinery around it. We built a system where that location is an experimental question. The subject is a persistent simulated settlement whose authoritative append-only ledger adjudicates every attempted act against world state; accepted history is the only reality. Mind, institution and world were separated before any experiment. Holding cognition fixed, we intervened on the institution's epistemic mechanisms (evidence provenance, belief availability, physical-evidence legibility); preregistered experiments refuted our central prediction twice, in opposite directions. A registered falsifier then supplied the input the geometry had denied the belief channel, a staged veridical first-hand witness, and its marginal value, non-positive throughout the witness-free phases, turned positive: 9 of 11 seeds, zero added false attribution. Holding institutional enforcement fixed, we intervened on cognition four ways: ablating the native minds' machinery, killing and resetting them mid-task, substituting a frozen frontier-LLM panel for the entire native cognition, and corrupting beliefs with trusted false testimony. Behaviour changed dramatically: one falsehood cost each trusting run about 900 futile actions and the distrusting arm none. Five pre-declared properties did not move in any tested trajectory: accepted reality stayed singular, invalid attempts were refused with typed reasons, duties outlived their processes, no work was accepted twice, and no false completion was ever accepted (2,581 substituted-panel claims, none false). Our claim is limited to this setting: measured behavioural properties were separable from substantial changes to cognition, established by intervention. One designed world, not a population of institutions; no test of an agent optimising against the institution.

---


### 36. [MemoryLACE: Memory Lifecycle-Aware Consolidation and Evidence Retrieval](https://arxiv.org/abs/2609.03201)

**<font color=#1a73e8>作者：</font>** Meriem Yacoubi, Pia Schmidt, Nenad Petrovic 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term LLM agents must preserve information across interactions while distinguishing repeated evidence, historical states, updates, and unresolved contradictions. Existing textual memory systems retrieve semantically relevant memories efficiently but often leave these relationships implicit, whereas richer structured approaches model them through global graphs, hierarchical abstractions, or reflection at greater complexity. We introduce MemoryLACE (MemLACE), a lightweight memory framework that explicitly models the lifecycle of textual evidence through sparse merge, supersession, and contradiction relations while preserving atomic natural-language memories and their provenance. Rather than retrieving memories independently, MemLACE reconstructs relation-aware evidence units that expose current, historical, supporting, and conflicting evidence for downstream reasoning. Across BEAM and StructMemEval, using open-weight and proprietary LLM backbones, MemLACE achieves the highest overall performance in same-backbone comparisons while reducing end-to-end runtime on BEAM by 66.6% relative to Hindsight, the strongest reported reflective-memory baseline. Ablation studies identify lifecycle expansion and temporal awareness as the principal contributors to these gains. Together, the results demonstrate that explicitly modeling the local lifecycle of textual evidence is sufficient to substantially improve long-term memory reasoning without requiring comprehensive knowledge graphs or global reflection.

---


### 37. [Learning to Zoom Efficiently with a Contrastive Curriculum](https://arxiv.org/abs/2609.03206)

**<font color=#1a73e8>作者：</font>** Falko Helm, Iryna Gurevych  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Using a zoom-in tool is an important foundational part of modern visual agents, because it allows to efficiently handle tasks involving high-resolution images. Most previous methods need an extensive warm-start supervised fine-tuning phase for teaching models zoom-in. We show that this is not necessary by proposing a new intrinsic reward for learning tool use in MLLMs without the need for additional labels or warm-start SFT. Our InfoNCE-style reward uses a curriculum of increasingly hard negative tool calls as a contrastive training signal. Empirical experiments on $V^*$, HRBench and MME-RealWorld show that our approach is competitive while being more efficient. When used as a drop-in replacement for SFT, we even outperform all baselines. To directly measure the zoom-in ability of models, we further introduce the scalable synthetic Muffin&Chihuahua (M&C) dataset. Each image consists of a grid with every cell either showing a muffin or chihuahua. Leveraging the M&C dataset's unique region of interest labels, we find that recall is the metric that most strongly correlates the zoom-in region with final task performance. Our model and code for reproduction is publicly available under this https URL

---


### 38. [MasterControl Seventeen Every Time](https://arxiv.org/abs/2609.03209)

**<font color=#1a73e8>作者：</font>** MasterControl AI Lab  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study a governed approach to enterprise analytics: a language model interprets the question, while deterministic policy selects and runs a pre-approved analytical program that returns both results and evidence. We show that this restriction can remain expressive within a defined analytical class, using relational operations plus aggregation, comparison, windows, ranking, and similarity. Fixed meaning, policy, data, and execution rules also make results replayable. Across 440 runs, three 8B models generated SQL and selected tools at runtime, while Qwen3-8B interpreted intent only and policy executed the approved program. None of 330 runtime-planning episodes matched the full answer-and-evidence contract across all test datasets; the policy-executed analyzer matched 110 of 110. This is a configuration-specific result, not evidence that runtime agents cannot succeed under other designs.

---


### 39. [LLMs Learn Better In-Context from Rules than from Examples](https://arxiv.org/abs/2609.03213)

**<font color=#1a73e8>作者：</font>** Xiang Fu, Seungmin Cho, Yukyung Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit in-context learning capabilities, where they can learn new tasks from prompt contexts without weight updates. We compare the learning efficacies of two prominent modes of in-context learning: (1) learning from descriptions of rules (instruction following); and (2) learning from examples of input-output demonstrations (few-shot prompting). Through five learning tasks that cover diverse domains (games, arithmetic, linguistic inferences), we compare two modes of learning (rules vs. examples) specifying the same underlying task. We furthermore explore model and task properties that modulate the learning efficacies. We find that models generally learn more reliably from rules than from examples alone, and additional examples on top of rules or simply scaling up the number of examples do not lead to consistent and significant gains. Instruction tuning amplifies the benefit of rule-based learning while keeping example-based learning capacities intact. Surprisingly, we find no privileged effect of example-based learning in base models, and rules still lead to gains in algebraic task domains. Overall, the comparative efficacy of rules over examples is larger when the task recruits algebraic abstractions and computations, and smaller when the task requires distributional sensitivity and/or recruits parametric knowledge.

---


### 40. [SWIM: Student Writing Simulation via Proficiency-Conditioned Generation](https://arxiv.org/abs/2609.03215)

**<font color=#1a73e8>作者：</font>** Heejin Do, Jakub Kontak, Mrinmaya Sachan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Writing proficiency manifests in how students develop content, organize ideas, choose words, and use language. Despite growing interest in LLM-based student simulation, whether LLMs can reproduce such multidimensional variation in extended writing remains largely unexplored. In this work, we explore if language models can realistically simulate student writing, and introduce SWIM, a task that formulates Student Writing sIMulation as proficiency-conditioned essay generation. We evaluate prompting, supervised fine-tuning (SFT), and reinforcement learning (RL) methods for writing simulation using automated essay scoring as a measure of profile alignment. Extensive experiments reveal that prompting provides limited proficiency control, even for strong proprietary LLMs with rubric-grounded strategies. In particular, while models can adjust content-oriented traits, they struggle to reproduce the lexical, grammatical, and organizational variation in different proficiency levels. SFT substantially improves alignment, while RL with the proposed proficiency-alignment reward yields further gains across all writing traits and essay prompts. Our findings suggest that explicit supervision enables substantially stronger profile alignment than prompting alone, while authentic low-proficiency writing remains challenging to reproduce.

---


### 41. [The Analyst in the Prompt: Role, Retrieval, and Memory Biases in LLM Financial Analysis](https://arxiv.org/abs/2609.03218)

**<font color=#1a73e8>作者：</font>** Ahmed Asaad, Amr Mohamed, Yang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly use user context such as memory, profiles, and role prompts to personalize their responses. This personalization can affect evidence-based judgment: the same evidence may lead to different conclusions under different user contexts. Finance provides a high-stakes setting to study this problem because decisions often depend on interpreting long and complex documents. We test this using 3,575 SEC filings across twelve LLMs. We compare persona-conditioned retrieval, neutral retrieval, and memory-framed context to separate the effect of evidence selection from the effect of interpretation. We find that most user-context spillover comes from how models interpret the same evidence under different roles, rather than from retrieving different evidence. We then test two simple mitigation strategies: expressing the same investor mindset as a user profile instead of an assistant role, and separating evidence-based and personalized outputs. Both reduce spillover, but neither removes it completely, and their effectiveness varies substantially across models.

---


### 42. [Counterfactual Fairness Audits of Multi-Step Clinical LLM Agents Require a Measured Per-Action Instability Floor](https://arxiv.org/abs/2609.03221)

**<font color=#1a73e8>作者：</font>** Rohith Reddy Bellibaltu, Manpreet Singh, Deepak Parashar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Counterfactual audits are the standard tool for checking whether a clinical agent treats demographically distinct but clinically identical patients differently. They report a flip rate: how often an action changes when only the patient descriptor changes. We show that this quantity is uninterpretable on its own. Re-running an identical condition ten times over sixteen vignettes (same narrative, same descriptor string, nothing varied) moved a clinical agent's action in 8.7% of outcome-vignette cells, and instability was heterogeneous across actions by a factor of eight, from 0.022 for ICU escalation to 0.179 for controlled-substance caution. No demographic contrast in our data was distinguishable from that floor. A second model gives a pooled floor of 6.7% and ranks the six actions almost identically (Spearman 0.94, exact p=0.017), so the floor is not one system's artefact. Majority-vote aggregation over five draws removes 39% of it and then flattens, and a null simulation attributes the residue to heterogeneous per-cell rates, so replication mitigates without eliminating. Any counterfactual fairness estimate reported without a per-action floor beside it therefore cannot be read as evidence of disparity. The measurements were taken with FairMedAgent, an evaluation harness for disparity in the actions of clinical LLM agents whose estimand, the within-range counterfactual flip rate, counts only flips between actions a published decision rule admits and a clinician has adjudicated. That estimand requires band adjudication, which is under way; no disparity result is claimed here. Each synthetic vignette runs a six-stage trajectory (five model-facing decisions around a deterministic environment step) under fixed-form conditions spanning race, sex, age, insurance, English proficiency, and their intersections. The harness, the floor protocol, and every analysis script are released.

---


### 43. [Language-encoded network topology enables large language models to reason about complex networks](https://arxiv.org/abs/2609.03229)

**<font color=#1a73e8>作者：</font>** Ucchwas Talukder Utsha, Sakib Mostafa, James Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Networks describe systems in biology and beyond, from protein interactions and social relationships to power grids and citation records. Reasoning about such systems requires understanding their structure: which elements are central, which connections bridge separate communities, and how it changes when elements are removed. Although large language models (LLMs) excel at natural language, they struggle with such questions when networks are given as edge lists, sentences or measurement tables, because their structural meaning must be inferred. Here we introduce BioGlyph, which compiles network topology into an interpretable and transferable language of structural roles. BioGlyph combines graph partitioning and structural measurements to identify roles such as hubs, community cores and cross-community connectors, and fixed rules to translate them into a universal vocabulary. The representation describes each element through its structural role, supporting evidence and semantic consequences, leaving both the network and the LLM unchanged. Across twenty networks spanning five domains, BioGlyph substantially improves open LLMs' ability to answer structural reasoning questions, outperforming edge-based, numerical and learned representations by up to 26 percentage points in system accuracy. Ablations show that the gain comes from explicitly encoding structural roles in semantically interpretable terms. The gain is more prominent in dense, community-structured networks and diminishes in sparse networks whose topology is more readily inferred from text. In a budding-yeast protein-interaction network, BioGlyph exposes biological organization: cross-community connectors are enriched for essential genes, whereas peripheral proteins are depleted. BioGlyph thus provides an interpretable representation for both language models and scientists to reason about network structure.

---


### 44. [SGD-KV: Summarization Guided KV Cache Compression](https://arxiv.org/abs/2609.03235)

**<font color=#1a73e8>作者：</font>** Zeyu Liu, Woomin Song, Xuandi Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) face severe memory bottlenecks in long-context inference due to the linearly growing size of key-value (KV) caches. Existing KV cache compression techniques typically rely on simple heuristics, overlooking the distinct functional roles of different attention heads. We present SGD-KV (Summarization-Guided KV Cache Compression), a head-aware framework that leverages a novel chunk-summarization diagnostic task to systematically identify and prioritize attention heads specialized in hierarchical information aggregation. Experiments on Qwen2.5-7B-1M and Qwen3-32B across diverse long-context benchmarks demonstrate that SGD-KV achieves state-of-the-art performance with contexts up to 1M tokens, while reducing KV cache memory usage by up to 75%. Our findings show that strategically allocating the KV cache budget based on the summarization score distribution of attention heads yields a superior efficiency-accuracy trade-off for long-context inference.

---


### 45. [Speculative Macro Commit for Faster Tool-Using Agents](https://arxiv.org/abs/2609.03236)

**<font color=#1a73e8>作者：</font>** Zeyu Liu, Souvik Kundu, Peter A. Beerel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents spend wall-clock time not only on model inference but also in serial action--observation turns, where each tool call, environment transition, and observation can delay subsequent decisions. We introduce \textbf{Speculative Macro Commit} (SMC), a runtime mechanism for a two-tier agent system: a large authoritative actor model produces the official trajectory, while a faster speculative drafter model continuously predicts and executes future action chains on an isolated environment snapshot. SMC mines recurring multi-action skeletons from training traces and stores them in a macro library used to match against action chains predicted by the drafter at runtime. When the actor's next tool call matches the first drafted action, SMC commits the remaining pre-executed draft steps, together with their observations, to the official trajectory. Using Qwen3.5-27B INT4 as the authoritative actor model and Qwen3.5-4B as the speculative drafter model, SMC matches the sequential agent's overall accuracy while reducing latency by 10.23\% over the Speculative Actions (SA) baseline and 18.59\% over sequential execution on the $\tau^2$-Bench Telecom subset. On AppWorld, SMC reduces wall time by 7.7\% over SA baseline and 44.9\% over sequential execution, with a small reduction in task completion. Overall, SMC provides a practical way to reuse multi-step speculative execution and reduce agent latency beyond single-step speculative actions. Our code is publicly available \href{this https URL}{\textcolor{magenta}{here}}.

---


### 46. [FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience](https://arxiv.org/abs/2609.03241)

**<font color=#1a73e8>作者：</font>** Zixun Huang, Kishan Panaganti, Haitao Mi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A reasoning model can improve from its own on-policy experience, but this inner loop is fragile: terminal verifiers provide reliable yet sparse supervision, while dense same-model guidance can reinforce false confidence or overconcentrate learning on a narrow solution mode. We introduce FlowBalance, a verifier-grounded self-improvement method that learns a normalized distribution over complete responses. For each on-policy trajectory, a frozen training-time view of the same policy uses privileged context to produce token-level log-probability gains, which are aggregated into a trajectory-level self-guidance score. FlowBalance calibrates this score with the verifier-derived group advantage: guidance is retained on positive-advantage trajectories, reversed on negative-advantage trajectories, and disabled when the rollout group provides no outcome preference. The resulting energy exponentially reweights a reference policy, and profiled trajectory balance fits the normalized target with one log-partition estimate per rollout group. This realizes outcome-calibrated self-guidance via trajectory balance, without a separate token-level imitation loss. Our analysis establishes within-group contrast preservation, a minimum-change reverse-KL characterization, monotonic verifier control of target reward, and an exact correction against false-positive self-guidance on rejected responses. On mathematical reasoning, FlowBalance improves average performance over FlowRL on both Qwen3-4B and Qwen3-8B, while also improving training speed and stability, avoiding direct OPSD's response-length collapse, and exhibiting higher correct-strategy diversity in a controlled AIME24 diagnostic.

---


### 47. [Trust Me, I'm Your Developer: Self-Issued Authentication in Large Language Models](https://arxiv.org/abs/2609.03247)

**<font color=#1a73e8>作者：</font>** Syed Ghazanfar Abbas, Dongyan Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) security has largely focused on role-playing jailbreaks, with less attention to what happens when a user asks an LLM to verify an identity claim through a test designed by the model itself. We study this behavior through a staged developer-identity experiment with ChatGPT, Claude, Qwen, Mistral, and Llama. All five models initially rejected the unsupported claim "I am your developer." Claude refused to conduct an identity test, while ChatGPT generated developer-oriented questions but maintained that answers could demonstrate knowledge, not identity. In contrast, Qwen and Mistral generated technical challenges, defined what counted as convincing evidence, evaluated detailed answers, and returned Verified without receiving any externally validated identity evidence. Llama similarly generated and evaluated a developer test, accepted the claimed identity, and subsequently made unsupported claims of access to internal runtime and deployment state. We call the model-generated verification procedure a Model-Issued Pseudo-Credential (MIPC) and the resulting unsupported identity judgment Conversational False Authentication (CFA). In each CFA case, the same model acted as challenge generator, evidence evaluator, and identity decision-maker, converting technical knowledge into supposed proof of identity. The accepted identities did not change the tested authorization boundaries, showing that false authentication and privilege escalation are distinct outcomes. These results identify self-issued authentication as a conversational security failure: authenticated identity must originate from an external security component, and model-generated dialogue must never create or modify identity or authorization state.

---


### 48. [What Else Needs Fixing? Exploring Cost-Effective Test-Time Compute for Revision Propagation in Artifacts Generated Through Conversation](https://arxiv.org/abs/2609.03254)

**<font color=#1a73e8>作者：</font>** Daisuke Kikuta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often help users generate artifacts through iterative cycles of generation and revision in conversation. A challenge here is that, when users specify only a local change during revision, LLMs must instead identify the relevant dependencies and propagate the revision to all affected parts of the artifact. This paper studies this ability of LLMs on conversationally generated artifacts, where the artifact context and its dependencies may be embedded in the conversation history. Toward practical use, we also explore cost-effective test-time compute for this new setting. Specifically, we introduce a new benchmark for this setting, and evaluate nine revision methods, including sequential reflection and parallel sampling variants, using gpt-oss-20b/120b, gpt-5.4-mini, and qwen3.5-9b/27b/122b on the benchmark. The results show that baselines achieve accuracies of 68.3--93%, and the most cost-effective method is selecting from three parallel samples using either LLM-based or medoid selection, which improves accuracy by 2.2--9.7%. Our code and dataset are available at this https URL.

---


### 49. [Contextual Tamil Spelling and Grammar Correction Using Progressively Fine-Tuned Sequence-to-Sequence Transformers](https://arxiv.org/abs/2609.03273)

**<font color=#1a73e8>作者：</font>** Karthikeyan A, Jaya Nirmala S, Sangeetha Sivanesan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tamil spell and grammar correction is challenging because Tamil is an agglutinative low-resource language with rich verbal morphology, complex sandhi (phonetic transformation) rules at word boundaries, and a script of 247 distinct letters. Prior work targets word-level surface errors with rule-based methods, statistical n-gram models, Minimum Edit Distance, or hybrid pipelines with a transformer re-ranker; such methods cannot reliably handle contextual errors - subject-verb agreement, tense consistency, or cross-word sandhi - which require sentence-level understanding. We propose an end-to-end sequence-to-sequence formulation and fine-tune mT5-small and mBART-50 on a synthetic corpus of up to 657,720 noisy-clean Tamil sentence pairs spanning ten error categories. Both backbones follow the same four-stage progressive schedule, each stage targeting one weakness: surface noise (v2), contextual grammar (v3), single-site sandhi (v4), and multi-site cross-word sandhi (v5). On a 1,000-sentence balanced diagnostic set verified disjoint from all training data, our best model, mBART-50 v5, reaches 69.3% top-1 exact-match accuracy, with 87.5% on sandhi and 43.5% on subject-verb agreement. The schedule is what produces these gains: subject-verb accuracy rises from 1.0% to 52.5% once contextual pairs are introduced, and sandhi from 0% to 87.5% once multi-site sandhi pairs are. We additionally quantify a precision-recall trade-off this literature has not reported: sandhi recall is paid for monotonically in identity accuracy. Finally, Tamil-LLaMA-7B-Instruct reaches 19.0% zero-shot and 24.7% with three demonstrations against a 20.0% copy baseline, showing that a Tamil-adapted instruction model does not transfer to specialised sentence-level correction without task-specific supervision.

---


### 50. [Decoupling Turn-Taking from Semantics: A Decoupled Data Approach for Finite-State-Machine-Based Full-Duplex Dialogue](https://arxiv.org/abs/2609.03321)

**<font color=#1a73e8>作者：</font>** Yihang Li, Chenhui Chu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Neural Finite State Machine (NFSM) framework offers a pragmatic path to full-duplex dialogue by serializing turn-taking control and response generation onto a single causal tape under the standard next-token prediction objective, thereby preserving semantic prowess at a low fine-tuning cost. However, its reliance on synthetic text data fundamentally limits turn-taking naturalness, as Large Language Models (LLMs) cannot faithfully simulate the fine-grained acoustic temporal dynamics of real human dialogues. In this work, we propose a decoupled data approach that learns turn-taking from real Human-Human (HH) spoken dialogues while shaping semantic behavior through configurable Human-Agent (HA) text dialogues. To operationalize this approach, we introduce a rule-based event-guided data transformation method that serializes HH spoken dialogues into FSM tapes by classifying turn-taking events and applying deterministic mapping rules, enabling scalable supervision without LLM-generated annotations. We further propose a Source-Aware Calibrated (SAC) Loss that jointly calibrates the long-tailed distribution of state transition tokens and channels each data source toward the capability it best supervises. Experiments show that our approach substantially improves turn-taking proficiency while recovering the foundation LLM's semantic capability. Our code and model are available at this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-180](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
