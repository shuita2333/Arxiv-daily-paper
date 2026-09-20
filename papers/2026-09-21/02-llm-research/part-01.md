# 🧠 大模型相关研究 | 2026年09月21日

> 本类共 **176** 篇论文：已确认 **162** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-176](./part-04.md)

---

### 1. [Subliminal Prompting Beyond Static Geometry: Causal Depth and Multi-Token Confounds](https://arxiv.org/abs/2609.19149)

**<font color=#1a73e8>作者：</font>** Barath Velmurugan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Subliminal learning shows that language models can transmit a hidden trait through outputs that appear unrelated to it. One proposed explanation, token entanglement, links animal and number tokens through the model's output vocabulary. Yet existing measurements answer different questions: whether outputs co-vary, fixed output vectors align, an answer can be read from a hidden state, or that state causally controls the answer. We measure each separately in a fixed animal-number prompting protocol. From Llama-3.1-8B to 70B, fixed output-vector similarity predicts behavior less well: the paired mean correlation change is -0.080 (95% CI [-0.127, -0.035]). A fixed output-head readout shows no resolved change in normalized depth AUC. To test control, we copy the temporary answer-position state from one number prompt into another at five depths and measure which prompt the final animal score follows. Donor-control AUC rises from 0.254 to 0.540, a paired change of +0.286 (95% CI [+0.272, +0.300]), with increases for all 18 concepts. The contrast remains with exactly eight transformer blocks remaining, while specificity and identity controls remain small or exact. In two Qwen models, scoring every digit in sequence does not recover the positive one-token association. Per-token averaging instead creates a positive pooled association that disappears after controlling number width, revealing a length confound. Thus, fixed geometry, observational readability, causal timing, and multi-token measurement are distinct properties of this frozen prompting channel. They constrain token-level explanations but do not identify the mechanism of training-time trait transfer.

---


### 2. [Sampling Reveals Style: Unsupervised, Training-Free Discovery of Prompt-Conditional Stylistic Axes in LLM Activations](https://arxiv.org/abs/2609.19150)

**<font color=#1a73e8>作者：</font>** Ajit Mallavarapu, Ziwei Gu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) encode rich stylistic structure in their hidden activations, but discovering which stylistic dimensions are salient for a given prompt typically requires supervised contrastive data. We present a training-free, prompt-conditional alternative: we repeatedly sample completions of a single prompt at elevated temperature, apply Principal Component Analysis (PCA) to the pooled hidden activations, and label the resulting axes automatically from the pole generations. We validate the discovered axes against 245 human-elicited stylistic annotations in a two-phase study. On our strongest model (Qwen-3.5-4B-Instruct), the top two axes match spontaneously requested human dimensions with 72.8% precision and 43.6% macro-recall, and 75.6% of validity ratings judge the axes' polar generations accurate to their labels, with 90.9% adjacent inter-annotator agreement. Discoverability is strongly model-dependent: both Qwen models and Llama-3.2-3B expose human-salient axes, while DeepSeek-7B-Chat drops to 35.3% precision, its leading components dominated by structural rather than stylistic variance. Simple PCA over a model's own decoding variance is thus an effective, low-cost probe of stylistic structure in LLM representations, one that also exposes sharp cross-model differences in how that structure is organized.

---


### 3. [What Users Think of Generative AI: A Cross-Platform NLP Analysis of Trust and Friction in App Store Reviews](https://arxiv.org/abs/2609.19151)

**<font color=#1a73e8>作者：</font>** Md Jafrin Hossain, Umme Nusrat Jahan, Shouvaggo Sharif Shammo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) applications have achieved rapid consumer adoption, yet little large-scale research examines user-perceived quality, trust, and adoption barriers. We present one of the first cross-application analyses of app store reviews for six major GenAI applications (ChatGPT, Gemini, Microsoft Copilot, Claude, DeepSeek, and Perplexity), comprising 17,012 English-language reviews from Google Play and the Apple App Store. We combine BERTopic topic modeling with RoBERTa sentiment classification and evaluate cross-application differences using chi-square, Kruskal-Wallis, and multinomial logistic regression with Bonferroni correction. Both components are validated against human coding using a stratified sample of 300 reviews. Results show that negative sentiment concentrates in advertising (91%), authentication (89%), server reliability (83%), and subscription pricing (73%). Sentiment differs significantly across applications, with Claude exhibiting the highest negative sentiment (47.7%) alongside a strongly enthusiastic user base, indicating statistically significant polarization. These findings are robust despite unequal review counts across applications. As exploratory observations, a subset of DeepSeek reviews raised geopolitical and data privacy concerns related to its Chinese origin, while a proposed Trust Friction Score summarizes application-specific trust and usability barriers into interpretable dimensions. The study provides validated and actionable evidence on user trust, usability, and adoption barriers in consumer generative AI applications.

---


### 4. [FakeSpotter: A content and strategy agnostic Viral Misinformation Detection Tool](https://arxiv.org/abs/2609.19152)

**<font color=#1a73e8>作者：</font>** Giovanni Spitale, Federico Germani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Misinformation detection tools often rely on binary true and false classifications or models trained on historical examples, limiting their usefulness when novel misleading narratives emerge. Here, we present FakeSpotter, a content- and strategy-agnostic tool designed to estimate the viral misinformation risk of textual content by measuring structural fingerprints of misinformation rather than directly adjudicating truthfulness. FakeSpotter operationalizes a theory-driven framework across linguistic, narrative, logical, and critical-thinking dimensions, using repeated LLM assessments and domain-specific logistic regression classifiers for short and long texts. In a labelled corpus of 764 texts from social media and FakeNewsNet, FakeSpotter achieved macro F1 scores of 0.788 for short texts and 0.793 for long texts on a held-out test set. FakeSpotter's interpretive layer provides explainable outputs through feature-based scores, signal agreement, and a caution index, and can be used for social listening. These findings suggest that identifying the structural fingerprints of misinformation can support early, explainable, and human-supervised assessment of potentially viral misinformation.

---


### 5. [Neo-Classic: A Benchmark for Evaluating Linguistic-Aesthetic Reasoning in Classical Chinese Poetry](https://arxiv.org/abs/2609.19154)

**<font color=#1a73e8>作者：</font>** Han Zhang, Zihan Gu, Zhiyuan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) achieve high accuracy on established Classical Chinese Poetry benchmarks, it remains challenging to distinguish transferable Linguistic-Aesthetic Reasoning from reliance on familiar pre-training patterns. To address this issue, we introduce Neo-Classic, an evaluation benchmark that combines a constructionist Out-of-Sample (OOS) dataset with a suite of reverse understanding probes. Unlike traditional benchmarks that rely on verification or generation over historical corpora, Neo-Classic comprises strictly metrical poetry authored by contemporary experts, reducing the possibility of direct retrieval. We evaluate state-of-the-art models, including Qwen3-Max, Gemini-3-Pro, and DeepSeek-V3.2, across five behavioral probes designed to test hierarchical constraint satisfaction. Our results reveal two primary limitations. First, a performance gap of 20 to 50 percent emerges when models transition from historical to contemporary texts. Second, models exhibit substantial difficulties in discourse-level ordering tasks, with standard accuracy remaining low (0 to 13 percent). Although expert-level guidance improves the performance of reasoning-enhanced models to 36 percent, a notable gap with human experts persists. These findings suggest that while current LLMs capture local formal patterns, they struggle with global hierarchical planning required for robust Linguistic-Aesthetic Reasoning.

---


### 6. [Towards Proactive Detection of User-Side Implicit Conflicts in Human-LLM Dialogue](https://arxiv.org/abs/2609.19155)

**<font color=#1a73e8>作者：</font>** Jinqiang Wang, Tao Zhu, Huansheng Ning  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In Human-LLM dialogue, follow-up user utterances may implicitly conflict with earlier intents, leading the LLM to misinterpret user needs and generate inappropriate responses. A reliable dialogue system should proactively detect user-side conflicts before generating a response and seek clarification when necessary. However, prior work has largely focused on LLM-side conflicts, leaving user-side conflicts underexplored. To fill this gap, we construct UC-Bench, a human-annotated benchmark for evaluating user-side conflict detection. Preliminary experiments show that existing LLMs struggle with this task, especially when conflicts arise from implicit incompatibilities grounded in dialogue history. To improve lightweight LLMs with limited training data, we investigate data synthesis for user-side conflict detection. Existing synthesis methods do not explicitly model the implicit incompatibilities between historical and current user utterances, making it difficult to capture the evolution of conflicts and to generate reliably labeled implicit conflict samples. We propose SynUC, a constraint-guided synthesis method that represents user-side conflicts in a constraint space and uses the SPEAKING framework to guide traceable constraint transformations. Applying SynUC to WildChat, we construct UC-Data, a user-side conflict training set containing 2,487 samples. On UC-Bench, Qwen3.5-4B trained on UC-Data outperforms larger general-purpose LLMs such as Claude Opus 4.8, as well as the same backbone trained on data synthesized by existing methods.

---


### 7. [Reflective Recovery: A Self-Supervised Method for Reasoning by Learning from Mistakes](https://arxiv.org/abs/2609.19156)

**<font color=#1a73e8>作者：</font>** Qirui Chen, Renjie Pi, Jiahui Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data-driven fine-tuning is widely adopted to enhance reasoning in Large Language Models (LLMs) due to its simplicity and efficiency. However, mainstream imitation learning methods that rely exclusively on perfect reasoning trajectories suffer from a Scaling Collapse: when the problem set is limited, increasing positive examples fails to yield continuous improvement. However, during inference, an LLM can not guarantee that every intermediate step is correct and is therefore prone to errors. Once such errors arise, the LLM often struggles to recover and may be further misled by the accumulation of previous mistakes. To address this, we propose Reflective Recovery, a simple yet effective self-supervised approach that transforms failed reasoning attempts into recovery training data. Specifically, we extract initial segments of failed trajectories, concatenate them with prompts, and use them to guide the LLM toward valid solutions. Because these segments from failed trajectories are likely to contain errors, this process teaches models to recognize and correct mistakes during reasoning, enabling recovery from erroneous states without relying on external critics or reward models. Evaluated on extensive benchmarks, Reflective Recovery significantly improves performance. On DeepSeek-R1-Distill-Qwen-7B, it boosts accuracy from 30.0% to 37.5% on AIME 2025 and from 37.6% to 47.8% on Minerva. More importantly, analyses demonstrate that it breaks the scaling collapse barrier and enables models to develop emergent self-correction behaviors, representing a paradigm shift from outcome-oriented memorization to process-oriented reflective reasoning.

---


### 8. [VisKG-LM: Compiling Knowledge Graphs into Visual Memory for Multiple-Choice Question Answering](https://arxiv.org/abs/2609.19158)

**<font color=#1a73e8>作者：</font>** Yixin Peng, Er Jin, Shiwei Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs are usually integrated into question answering by encoding a retrieved subgraph with a graph neural network and fusing it with the language model in the online inference path. The same subgraph is therefore re-encoded from scratch every time a pair is scored, across training epochs, seeds, and evaluation runs, even though the knowledge graph never changes. We ask whether the retrieved knowledge graphs can instead be compiled once, offline, and then accessed as read-only memory. VisKG-LM shows that it can, by decoupling graph encoding from language reasoning. It serializes each retrieved candidate-specific subgraph as Relation-Labeled Paths and renders the result as an image whose two-dimensional layout preserves the branching structure of the paths. Each image is encoded once, offline, and cached for reuse. At inference, the language model contextualizes the question and candidate from text alone, and only its final layer consults the cached visual memory, reading both its global layout and its local relational detail. The graph information thus enters only after the text has been understood. On the test sets of CommonsenseQA, OpenBookQA, and MedQA-USMLE, VisKG-LMimproves over GreaseLM by $1.2$, $0.8$, and $4.3$ points, respectively, while matching or surpassing GraphVis, a $7$B vision-language model, with only about $400$M online parameters. Against a matched text-only control that receives the identical Relation-Labeled Paths, it gains $4.2$, $6.5$, and $5.1$ points across the three benchmarks. These gains show that the complete visual-memory interface adds value beyond path textualization alone and support compiled visual memory as an alternative to online graph propagation.

---


### 9. [To Memories and Beyond: From Remembering to Knowing You across Long-Term Multimodal Personal Archives](https://arxiv.org/abs/2609.19167)

**<font color=#1a73e8>作者：</font>** Wenqi Zhou, Zhuorui Yu, Kaiao Wen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI systems evolve into personalized digital companions, a central capability is reasoning over a user's long-term personal history: not merely storing past events, but tracking longitudinal experiences and evolving preferences. Progress here is bottlenecked by evaluation, existing long-term memory benchmarks are largely synthetic and text-only, they overlook the visual records that anchor everyday human memory, lack the authentic and causally connected longitudinal data that real personalization demands, and consequently remain confined to shallow factual recall. We introduce ReaLMem (Real-world Long-term Multimodal Memory), the first benchmark built from authentic multi-year personal visual archives, paired with first-person subjective annotations. ReaLMem evaluates models across three cognitive tiers of increasing difficulty: factual recall, persona inference, and predictive personalization. We further propose ChronoProfiler, a temporal-weighting profiling module that computes temporal stability scores for user attributes and applies them as a salience prior, resolving conflicts among temporally inconsistent preferences and helping models compound multiple co-active preferences in complex personalized decisions. Extensive evaluation of frontier multimodal large language models (MLLMs) and memory systems on ReaLMem reveals predictive personalization as a consistent ceiling, exposes clear performance gaps and bottlenecks between MLLMs and memory systems, and shows that high-quality, temporally informed representations substantially improve personalization. Together, ReaLMem and ChronoProfiler provide an authentic testbed and a simple, effective mechanism for long-term personalization, laying a foundation for future research on lifelong AI companions.

---


### 10. [BioPhys-Bridge: A Benchmark for Interdisciplinary Scientific Reasoning in Physics-Grounded Biological Research](https://arxiv.org/abs/2609.19180)

**<font color=#1a73e8>作者：</font>** Qingyang Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models face unique challenges in analyzing interdisciplinary scientific research literature. In biophysics research, faithful answers require grounding observed data in source evidence, interpreting it through a quantitative physics model, and linking it to a biological mechanism. To address this challenge, we introduce BioPhys-Bridge, a novel benchmark dataset for evidence-grounded scientific reasoning over biophysical literature. Each case contains evidence blocks, stable evidence IDs, quantitative values, units, equations, assumptions, mechanisms, and next decisions as grounding targets for question answering (QA) and retrieval-augmented generation (RAG). The initial release contains 500 cases, 1,517 agent-facing tasks, and covers six biological domains and nine physical model families, including three sparse families reserved for future expansion. We enforce strict quality gates for all cases in schema, evidence-integrity, quantitative-grounding, source-license, duplicate, unit-normalization, with domain expert review and annotation for 81 cases. Preliminary evaluations show that DeepSeek-V4-Flash obtain the highest evidence-ID $F_1$ score (0.360), followed by Qwen3.7-Max (0.316) and GPT-4o-mini (0.294). BioPhys-Bridge is an interdisciplinary benchmark for evaluating attribution, faithfulness, hallucination reduction, and biological experiment design with complex, multi-step scientific reasoning. Future works will increase the size and complexity of the dataset and perform comprehensive evaluations. Code and data are available in the GitHub repository and on Hugging Face.

---


### 11. [What Do We Expect from LLMs? Mapping the Design of LLM Benchmarks](https://arxiv.org/abs/2609.19182)

**<font color=#1a73e8>作者：</font>** Chao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks are central to how progress in large language models (LLMs) is assessed and communicated. Yet model rankings alone reveal little about how evaluation requirements themselves are changing. The expanding variety of benchmarks offers another perspective: what researchers expect LLMs to do, and what they count as successful performance. We systematically map 14,767 papers introducing or updating evaluation resources from arXiv submissions between January 2022 and August 2026. Using staged screening and automated full-text coding, we examine changes in target systems and domains, evaluation materials and conditions, and scoring mechanisms. The collection shows growing emphasis on action, interaction, and professional applications, while established and newer design elements frequently coexist. Model participation also develops unevenly: LLM-based scoring grows within both agent and non-agent groups, whereas model-generated materials show no comparable sustained increase in recent cohorts. These findings illuminate how public research translates capability expectations into concrete tests and criteria for success. As AI participates in constructing tests, performing tasks, and judging responses, they also raise a question: does expanding evaluation provide more independent evidence, or risk reproducing the preferences and blind spots of its participating models?

---


### 12. [Message capacity and claim wording set the transition points of collective truth-finding in language-model networks](https://arxiv.org/abs/2609.19183)

**<font color=#1a73e8>作者：</font>** Makoto Fukushima  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Whether human or large language model (LLM), an agent in a discussion reads only a few of the others' contributions, bounded by cognition, context, or cost. LLM collectives can settle on a wrong consensus even when a majority starts out correct; we ask how far that reading bound alone decides the outcome. We model the bound with one number, the message capacity, which sets how many of the others' messages an agent reads, and generate the communication network from it. Over 31,824 randomized queries, we found that an 8-billion-parameter model's judgment of a claim effectively reduces to a logistic function of a weighted sum of its inbox, the update rule of a stochastic binary neuron with divisively normalized weights. From these weights and the network's degree statistics alone, the wrong consensus should become unreachable from any start once agents read, on average, fewer than 6.4 of their 31 sources. In 1,414 episodes with assigned starts the prediction failed: the correct side won in fewer than 50% of episodes from every start, and in only 28-45% when 75% of agents started correct. The failure traces to the field, the threshold that a claim's wording sets for the agent's answer before any message is read: the experimental claims' fields lay below the calibration mean, and with each claim's own field the same weights reproduce the outcomes. Reversing the wording showed that the threshold follows what a claim asserts, not whether it is true. On a second 8B model the pipeline predicts claim-dependent bistability; transition points appeared where computed, and an eight-claim calibration matched in 15 of 16 conditions. At 70B the assertion bias is not detected. Thus a collective's fate is largely set by two single-agent measurements: the threshold a claim's wording sets, and the message capacity that sets the transition point.

---


### 13. [EvoSherlock: Towards Agentic Lifelong Evolution for Unseen Long-Tailed Security-Critical Events in Videos](https://arxiv.org/abs/2609.19201)

**<font color=#1a73e8>作者：</font>** Zixin Fan, Jiahong Lu, Changsheng Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing Security-oriented Video Understanding (SVU) systems assume a \emph{closed world}, \ie static category sets, abundant labels, and the premise that all event types are known upfront. Real-world security-critical events break these assumptions: they follow long-tailed distributions, new types emerge continuously, and critical security events may offer only a few samples. We formalize this gap as \textbf{Lifelong Evolving Task for Long-Tailed Security-Critical Events in Videos ({\boldmath$L^2$}-SCE)}, a new task that requires VLMs to continually classify and temporally localize newly emerging security-critical events from scarce samples without forgetting previously learned events. Furthermore, \task reveals two critical challenges: (1)~\textbf{Intra-Event Scarcity}, where extreme data scarcity may weaken both classification and temporal localization for new events, and (2)~\textbf{Inter-Event Interference}, where cross-event feature entanglement and representation drift may strengthen catastrophic forgetting. On this basis, we propose \textbf{\method}, a causal-enhanced approach orchestrated end-to-end by an \textbf{Agentic Controller} with self-reflective closed-loop control, which includes two core modules: the Intra-Event \textbf{C}ausal \textbf{V}ideo \textbf{G}eneration module (\textbf{CVG}) and the Inter-Event \textbf{C}ausal \textbf{D}ecoupling and \textbf{A}lignment module (\textbf{CDA}), to address the above two challenges, respectively. Especially, this paper constructs a \task dataset to simulate real-world incremental conditions. Extensive experiments on our benchmark demonstrate the advantages of \method over several advanced baselines. These justify the importance of the proposed \task and the effectiveness of \method in classifying and temporally localizing emerging security-critical events from scarce samples.

---


### 14. [Layer-wise Curriculum Learning for Efficient LLM Compression](https://arxiv.org/abs/2609.19213)

**<font color=#1a73e8>作者：</font>** Donggeon Lee, Dooyeon Na, Seungmin Oh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce layer-wise curriculum learning for efficient LLM compression. The proposed method facilitates the knowledge transfer from the teacher model to the student model, utilizing a curriculum learning approach that begins with easier optimization tasks and progressively tackles harder ones. In order to adopt the layer-wise learning in LLM compression, we partition the whole model into multiple segments consisting of layers, thereby enabling more computationally efficient knowledge transfer for LLMs. Based on our theoretical analysis of cumulative error phenomenon, layer-wise curriculum learning accelerates convergence while stabilizing the knowledge transfer process. In addition, we present a feature caching method with a multi-threading strategy to efficiently address feature misalignment across layers, maximizing GPU utilization. Consequently, our method exhibits advanced model compression performance, as well as high computational efficiency in terms of minimized memory usage and short training hours. Experiments on multiple datasets show that the proposed method achieves state-of-the-art performance while reducing GPU memory usage and training hours by more than 50\% on BERT and GPT-2. Moreover, it outperforms the other pruning methods on LLaMA-family and Qwen models under the same training hours, with a lower GPU memory footprint.

---


### 15. [PAPC: Platform Mediation for Privacy-Propagation Externalities in AI-Mediated Workflows](https://arxiv.org/abs/2609.19226)

**<font color=#1a73e8>作者：</font>** Tao Huang, Guosen Wu, Chen Hou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-mediated platforms coordinate work through LLM agents acting for different principals. In these workflows, privacy loss can be created before a final answer appears: a memory write, shared-workspace update, inter-agent message, or tool event may impose downstream exposure cost on another principal. We model this failure mode as a privacy-propagation externality, where the cost of a raw disclosure depends on topology and fanout as well as content. We present PAPC, a platform-mediated mechanism that intercepts information-moving events before they update shared state or external channels. PAPC combines policy, provenance, topology/fanout, privilege, and content signals to allow an event, release a policy-safe abstraction, quarantine raw content, block a transition, or narrow onward rights. The model explains why final-output control misses intermediate exposure costs and why high-fanout objects amplify propagation. Across retrieval-memory and multi-agent workflow benchmarks, PAPC preserves deterministic task completion and eliminates measured exact raw-value and external raw-value exposure. The results position event-level mediation as a platform-governance primitive for agent-mediated online work.

---


### 16. [Robust Conformal Intrusion Detection via Traffic-Aware Calibration and Attack-Orbit Invariance](https://arxiv.org/abs/2609.19241)

**<font color=#1a73e8>作者：</font>** Zhenpeng Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models fine-tuned for network intrusion detection emit single-point predictions without statistical validity guarantees. Conformal prediction supplies a finite-sample coverage guarantee, but a threshold calibrated on clean traffic fails once an adversary perturbs controllable network features. We demonstrate this failure across three intrusion detection benchmarks and propose traffic-aware conformal prediction, which calibrates on traffic drawn from the perturbation mechanism an attacker is expected to use and provably restores coverage whenever that mechanism is known and can be sampled. A stronger, adaptive attacker that queries the target model's own score can still degrade this matched-calibration guarantee. We address this second threat model by excluding attacker-controllable features and their deterministic descendants from the scored representation, and prove that this yields an exact, pathwise coverage guarantee rather than a probabilistic bound. Across three independently fine-tuned language model architectures, this representation remains completely unchanged under every evaluated attack attempt, at a quantified seven-to-fourteen-point cost in clean accuracy relative to the unrestricted feature set.

---


### 17. [Block Parallelism For Efficient Distributed Long-Context Diffusion Language Model Training](https://arxiv.org/abs/2609.19242)

**<font color=#1a73e8>作者：</font>** Tarun Suresh, Pranshu Chaturvedi, Hangoo Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block diffusion language models (BDLMs) combine autoregressive dependencies across blocks with parallel denoising within blocks, but long-context training is constrained by distributed attention communication and activation memory. Conventional context parallelism (CP) shards the combined clean-plus-corrupted sequence by position, communicating shared clean K/V together with block-specific corrupted K/V and their gradients. We observe that the BDLM objective separates over target blocks. We introduce block parallelism (BP), a new distributed parallelism dimension that assigns each corrupted-block computation to one rank. To scale BP to long contexts, we introduce context-sharded block parallelism (CSBP), which also shards the shared clean sequence across those ranks. CSBP keeps corrupted K/V and gradients local, avoids replicated clean prefixes, and preserves BDLM training semantics. On 16 H200 GPUs at 256K context, CSBP improves throughput over the best baseline by 1.18-1.45x for supervised fine-tuning and 1.27-1.33x for conversion of autoregressive models to BDLMs, while matching or reducing peak HBM. Full-model speedup reaches 1.61x at 512K. On eight H100 GPUs, CSBP accelerates DFlash2 speculative-decoder training by 2.48x at 512K and 7.59x at 1M. In matched 12-hour DiffusionGemma 26B-A4B SFT runs, CSBP achieves higher pass rates at every trained checkpoint on SWE-bench Verified and Terminal-Bench Lite. Code: this https URL

---


### 18. [Characterizing Web Search by Conversational LLM Agents: From Search Decisions and Strategies to Results and Responses](https://arxiv.org/abs/2609.19244)

**<font color=#1a73e8>作者：</font>** Mahsa Amani, Seungeon Lee, Abhisek Dash 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational LLM agents increasingly rely on Web search, yet the end-to-end lifecycle of agentic search remains poorly understood. We present the first study of Web search across four major conversational platforms (ChatGPT, Claude, Grok, and DeepSeek), combining real-world user interactions (invivo) with controlled experiments using the same platform's models by their APIs (invitro). We investigate the quality of agentic decisions to invoke Web search, their strategies to formulate queries, the potential domain preferences in the search results they receive, and the choices they make when transforming search results into grounded responses. We find that Web-search decisions vary substantially across platforms and models, while more frequent Web-search invocation does not necessarily yield better response quality. We further show that conversational agents employ different complex querying strategies and that platform specific search engines return search results from their preferred domains. Finally, although responses are largely grounded in search results, some claims rely on uncited search results, raising concerns about attribution and reliability. Our findings have important implications for the design of future AI agents and Web search tools optimized for conversational retrieval.

---


### 19. [Why Pretraining Fails to Share Cross-Lingual Knowledge](https://arxiv.org/abs/2609.19291)

**<font color=#1a73e8>作者：</font>** Adam Gaber, Uriel Dolev, Elisabeth Fittschen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have made remarkable progress in the processing and modeling of many languages. Yet, unlike human multilinguals, they exhibit surprisingly limited cross-lingual knowledge transfer. While this limitation is well documented, its origins during multilingual training remain unclear. We pretrain 360M- and 7B-parameter LLMs and show that poor cross-lingual knowledge generalization emerges during pretraining and persists under standard interventions. To isolate its cause, we employ a controlled bilingual pretraining setting using two copies of the same language, sharing identical text and token segmentation, but mapped to disjoint token spaces. We find that disjoint tokens alone are enough to induce knowledge compartmentalization, even between identical copies of the same language, establishing disjoint token spaces as a fundamental barrier to cross-lingual knowledge generalization. Guided by this understanding, we suggest mapping languages into a shared token space by simple word-wise translation and find it substantially improves cross-lingual knowledge generalization, recovering up to 12.6\% of native-language learning efficiency --- 14$\times$ the baseline.

---


### 20. ["I Know Where to Look," But Does the LLM? Charting the Gaps Between Clinical Expert Needs and Unstructured Data Abstraction Tools](https://arxiv.org/abs/2609.19318)

**<font color=#1a73e8>作者：</font>** Venkatesh Sivaraman, Rigney Turnham, George Bonano 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Clinical data abstraction, the process of distilling structured information from patient records, plays a key role in advancing knowledge about diseases such as cancer. Information extraction (IE) with large language models (LLMs) could accelerate this process, but it is unclear whether current frameworks effectively support clinical researchers without AI expertise. To address this, we co-designed an interactive LLM-based abstraction system called Libretto with seven cancer research teams, then evaluated the system's ability to help them answer real-world research questions. We found that while clinicians knew where and how to annotate complex concepts in patient notes, in twelve of fourteen tasks they faced barriers to replicating those intuitions with LLMs. Contextual note reliability judgments, difficulties in steering vibe-coded prompts, and inflexible evaluation strategies necessitated fundamental changes to the IE workflow. Our results highlight open problems for HCI research to bridge the gaps between AI data work tools and clinical users' needs.

---


### 21. [A frontend-backend architecture for tool calls in full-duplex speech models](https://arxiv.org/abs/2609.19334)

**<font color=#1a73e8>作者：</font>** Ke Hu, Slyne Deng, Chen Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech-to-speech (S2S) models provide natural, low-latency conversational interaction and would benefit from the ability to use external tools and complete voice-agent tasks. We propose a frontend-backend architecture where a duplex speech-to-text frontend learns to emit a delegation token and forwards streaming ASR transcripts to a text-based backend LLM for tool calls. Tool-call results from the backend are injected back into the frontend through a lightweight prefill-and-repeat mechanism and then synthesized using streaming TTS to the user. Our approach largely preserves regular duplex turn-taking, interruption handling, and low-latency interaction as it requires minimal modifications to the frontend model. In a single-turn tool-call evaluation, our system achieves 92-97% tool-call recall, competitive tool-call prediction performance, and 81.2% accuracy in rejecting irrelevant calls. When equipped with a larger backend (e.g., Qwen3-235B-A22B), our system achieves competitive results on Full-Duplex-Bench-V3 compared to open and closed source models, and significantly outperforms GPT-realtime-mini and Qwen3-Omni-30B-A3B-Instruct on EVA-Bench. These results demonstrate that backend delegation is an effective and modular approach for combining natural duplex speech interaction with strong agentic tool-call capabilities.

---


### 22. [Can Vision-Language Models Judge Olympic Diving? From Reasoning to Scores in Zero-Shot Action Quality Assessment](https://arxiv.org/abs/2609.19354)

**<font color=#1a73e8>作者：</font>** Henry O. Velesaca, David Freire-Obregon, Luigi Miranda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated action quality assessment (AQA) in Olympic sports remains a challenging task due to the complexity of human motion and the subjectivity inherent in expert judging. This work evaluates the capability of open-source Vision-Language Models (VLMs) to perform zero-shot action quality assessment on Olympic diving videos using the AQA-7 benchmark dataset. In this regard, a regression-based framework is pro-posed to leverage both the semantic reasoning and phase-level sub-scores generated by the VLMs, combining TF-IDF vectorization, dimensionality reduction, and ensemble learning to predict final competition scores. Experimental results show that standalone VLMs achieve moderate Spearman correlations below 0.32, while the proposed ensemble regression framework substantially improves performance in the reported evaluation, reaching a Spearman correlation of 0.67 with a four-model configuration. Textual reasoning features con-sistently outperformed raw numerical sub-scores, highlighting the richness of VLM-generated explanations for action quality analysis. These findings suggest that VLMs hold strong potential as assistive tools for explainable and semi-automated sports performance evaluation. The code is publicly available on GitHub this https URL diving judge vlm

---


### 23. [How to Guide Your Language Flow](https://arxiv.org/abs/2609.19356)

**<font color=#1a73e8>作者：</font>** Rohit Dilip, Tianrong Chen, Yuyang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a new method to guide flow matching models. Our approach, which we call probe guidance, uses the frozen internal states of an existing diffusion model to construct a guidance signal. This works using a similar principle as autoguidance, but eliminates the need for an additional forward pass at inference time and provides a reliable path to ensure that the weak and strong model share similar dynamics. We apply and benchmark this method on continuous diffusion language models, where probe guidance sets a new state-of-the-art performance on unconditional generation. When applied to a 1.7B diffusion language model, probe guidance consistently improves on multiple choice question answering benchmarks. Using our probes, we study the traditional autoguidance setting where the strong model is a weak checkpoint, and find that the weak model must come from a low-entropy region of training. These findings both provide a practical way to improve diffusion language models and shed light on the actual mechanism behind autoguidance, which is currently poorly understood.

---


### 24. [MAGS: Multi-agent Auto-formalization Guarantees Safety for Agentic Outputs](https://arxiv.org/abs/2609.19391)

**<font color=#1a73e8>作者：</font>** Albert Wu, Nicholas Roberts, Tzu-Heng Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM coding agents now generate complex programs at a scale that makes thorough human review increasingly difficult, raising the risk of safety and security failures. Common approaches, including fuzz testing, static analysis, and LLM-as-a-Verifier, can detect many failures but struggle to cover all possible edge cases. Formal verification addresses this by providing machine-checkable guarantees over specified properties, but traditionally demands substantial manual specification and proof engineering. We introduce a unified multi-agent framework, MAGS, that generates executable programs with formal safety guarantees, using Dafny as a verification-aware intermediate representation where safety properties can be mechanically checked. MAGS formalizes and freezes human-audited APIs and safety requirements, translates generated code into Dafny, repairs violations using verifier feedback, and compiles verified programs back into executable code. We evaluate MAGS on 100 CUDA kernels, 100 terminal scripts, and 20 robotic-arm tasks. Across all 220 examples, it achieves a 100% success rate in producing programs with non-trivial safety guarantees against frozen specifications. Independent safety and functional evaluations further show strong performance across all three domains, while revealing failures when the auto-formalized semantics do not fully capture the target behavior.

---


### 25. [Less Is More: Graph-free Multimodal RAG via Multi-signal Late Fusion](https://arxiv.org/abs/2609.19417)

**<font color=#1a73e8>作者：</font>** Tithi Rakshit, Hongkuan Zhou, Lavdim Halilaj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph-based retrieval-augmented generation (RAG) is widely used for multimodal, cross-document question answering. However, building corpus-level graphs is expensive, slow to query, and difficult to maintain. We present TrioRAG, a graph-free multimodal framework that integrates evidence from three complementary signals: the question, the anchor image, and a VLM-enhanced query generated from both. Each signal retrieves independently over a shared multi-vector index of page text and page images, and the results are combined through late fusion. Further, we introduce AutoQA, a multimodal automotive benchmark whose questions are grounded in noisy, web-sourced images rather than clean document-sourced figures. Its questions require reasoning across manuals. We position it as a model-curated testbed rather than a human-validated gold standard. Across three benchmarks, TrioRAG matches or outperforms graph-based systems while reducing total cost and accelerating per-query inference by 1.6-2.3 times. By construction, AutoQA grounds its questions in out-of-corpus web images. In this setting image retrieval reaches only 19.3% document-level recall, while text-derived signals, especially the VLM-enhanced query, keep retrieval robust.

---


### 26. [Use and Effects of LLMs in Peer Review: A Randomized Experiment and Survey at ICML 2026](https://arxiv.org/abs/2609.19420)

**<font color=#1a73e8>作者：</font>** Sunnie S. Y. Kim, Wesley Hanwen Deng, Jennifer Wortman Vaughan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLMs are rapidly reshaping peer review, making it important to understand how reviewers use them in practice and how different LLM-use policies affect review outcomes. We investigate these questions through a randomized experiment and an anonymous post-survey at ICML 2026, a major machine learning conference involving over 24,000 papers and 17,000 reviewers. Reviewers were assigned to either a conservative policy prohibiting all LLM use or a permissive policy allowing limited assistance, with randomization among a subset of main-track papers and reviewers. Policy assignment had near-zero effects on final paper decisions, paper scores, and reviewer confidence, although reviews under the permissive policy were 5.5-7% longer. Post-survey responses (N=1,486) revealed diverse attitudes toward LLMs and substantial noncompliance: 22.5% of conservative-policy reviewers reported using an LLM despite the prohibition, and 36.5% of permissive-policy reviewers reported at least one explicitly disallowed use. We discuss implications for future peer-review policy and tool design.

---


### 27. [Closed-World Resolution Against Tool Hallucination in LLM Agents](https://arxiv.org/abs/2609.19425)

**<font color=#1a73e8>作者：</font>** Laxmipriya Ganesh Iyer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented large language model (LLM) agents fail in a way no tool-selection or tool-security method addresses: they call tools that do not exist and pass arguments no schema declares. Existing defenses either pick the right tool (selection) or constrain what an agent may do with real tools (gating), both of which presuppose the emitted call refers to a real tool at all. We show this is a structural blind spot: a hallucinated call is by construction not a decision any gate made, so no gate can reject it. This paper is primarily a measurement and benchmark study. We give a five-class taxonomy of tool hallucination (H1-H5) and, as a reference point, the Resolution Rung: a training-free, closed-world resolver (registry membership plus a signature check) whose interest is where it must sit, not what it computes. We prove hallucination defense must precede any causal gate, and characterize the one irreducible residue (borrowed arguments schema-indistinguishable from a valid call). Across ten hosted models under two invocation surfaces we measure 322 genuine hallucinations; fabricated-tool calls concentrate on the unconstrained raw-JSON surface (34 vs. 3), and model scale does not help (a 675B model matches a 7-8B one). We then extend to the Model Context Protocol, where merging several servers into one namespace creates hallucination surfaces a single registry cannot express (a second taxonomy, M1-M5); on the live MCP surface we measure 154 hallucinations, including from frontier models that were clean on the single-registry surface, because collisions and shadowing are structural to the merge. We release the versioned Hallucinated-Tools Benchmark (HTB) so any resolver is comparable across submissions.

---


### 28. [CARES: A Conversational AI System for Regulation-Grounded Safety Reporting in Construction Education](https://arxiv.org/abs/2609.19429)

**<font color=#1a73e8>作者：</font>** Fan Yang, Jiabin Wu, Yuan Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Construction safety reporting often relies on manual logs and static templates that provide limited feedback and leave daily activities disconnected from relevant regulations. This paper introduces CARES (Conversational AI Reporting for Enhanced Safety), a conversational AI system that integrates regulatory guidance into daily reporting to support construction safety education. CARES combines proactive multi-agent dialogue, retrieval-augmented generation (RAG), and automated report generation. The system guides users through reporting tasks, retrieves relevant regulatory passages using hybrid retrieval, and converts conversations into structured daily reports. Regulatory sources and the evolving report are displayed alongside the dialogue to support user review and correction. A preliminary evaluation involving 15 construction management students assessed retrieval quality, response faithfulness, and conversational relevance. CARES achieved an overall faithfulness score of 0.74 and an answer relevance score of 1.00, while initial retrieval ranking remained an area for improvement. These results provide preliminary evidence of the technical feasibility of regulation-grounded conversational reporting. The study highlights opportunities to integrate regulatory knowledge into routine documentation, with future work needed to evaluate effects on report quality, safety awareness, and learning outcomes.

---


### 29. [Bayesian Optimization with Rich Auxiliary Information via LLMs](https://arxiv.org/abs/2609.19437)

**<font color=#1a73e8>作者：</font>** Tejus Gupta, Efe Mert Karagözlü, Rohit Sonker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian Optimization (BO) is widely used for optimizing expensive black-box functions, yet many real-world optimization problems contain substantially richer information than function evaluations alone. Examples include training curves in hyperparameter optimization, expert notes and images in scientific experimentation, and prior knowledge about where optima may lie. We show that large language models (LLMs) can effectively leverage such rich auxiliary information to guide optimization. Motivated by these findings, we develop three methods for incorporating auxiliary information into BO using LLMs. Across hyperparameter optimization benchmarks and a real-world nuclear fusion optimization task, our methods consistently outperform both standard BO and existing LLM-based optimization approaches. Our results demonstrate the effectiveness of LLMs for leveraging rich auxiliary information in BO.

---


### 30. [Compositional Reasoning in Language Models under Reinforcement Learning Post-Training](https://arxiv.org/abs/2609.19465)

**<font color=#1a73e8>作者：</font>** Yu He, Yingxi Li, Yifei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compositional reasoning is critical for real-world problem solving: since training data is necessarily limited, models must generalize by composing learned skills in new ways. While post-training methods such as reinforcement learning (RL) have substantially improved the reasoning abilities of language models (LMs), their effects on compositional reasoning remain less well understood. We propose a dependency-graph framework to formalize compositional reasoning, yielding three levels of compositionality with increasing complexity. Empirically, we instantiate this framework with data-structure tasks, which provide deterministic reward computation and clear compositional structure. We find a consistent decomposed-to-composed asymmetry: decomposed-skill training does not reliably transfer to composed tasks, whereas composed-task training transfers more readily back to decomposed tasks. We provide theoretical explanation for this asymmetry, and further evaluate compositional generalization under length extrapolation, structural distribution shift, and transfer to tasks requiring unseen skills. Finally, we present a pilot study on real-world tool-calling benchmarks, showing preliminary evidence that the decomposed-to-composed asymmetry can extend to practical settings.

---


### 31. [Safety Beyond the Interface: Detecting Harm via Latent States in Large Language Models](https://arxiv.org/abs/2609.19472)

**<font color=#1a73e8>作者：</font>** Alizishaan Khatri, Chiquita Prabhu, Omkar Neogi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous systems increasingly rely on Large Language Models (LLMs) yet the safety infrastructure surrounding these models introduces latency and compute overhead. This limits utility in resource-constrained, time-critical deployments. Existing external guardrail models remain blind to the model's internal workings, creating a fundamental assurance gap. We ask: does the model already know when the content is harmful? We extract activations from LLaMA-3.1-8B and train lightweight MLP classifier probes (12.6M parameters) to detect harmful prompts. Evaluated on WildJailbreak, Beavertails, and AEGIS 2.0, our probes achieve F1 scores of 99%, 83%, and 84%, respectively competitive with 1000x larger guard models while cutting latency and compute costs.

---


### 32. [SCOUT: Sim-to-Real Text-Based Person Retrieval by Embedding-Space Prediction over Frozen Video Features](https://arxiv.org/abs/2609.19483)

**<font color=#1a73e8>作者：</font>** Abdarahmane Traoré, Andy Couturier, Éric Hervet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-based person retrieval under a sim-to-real gap (synthetic training data, a real-image gallery) is usually tackled with costly fine-tuned cross-encoders. We ask whether a frozen-encoder system can compete. We present SCOUT, which casts cross-modal retrieval as prediction in embedding space. A trainable predictor maps the patch tokens of a frozen video encoder into the embedding space of a frozen text encoder under a bidirectional InfoNCE objective, and no encoder is fine-tuned in the base model. The video encoder is V-JEPA, the text encoder is EmbeddingGemma, and the predictor is initialized from a Qwen3.5-0.8B decoder. We make three findings. First, the best frozen text encoder is simply the one whose geometry best matches the video features. A training-free alignment score ranks three candidate text encoders in the same order as their retrieval accuracy on our held-out split (Spearman $\rho = 1.0$); a fourth, LLM-based encoder shows the rule is metric-dependent, holding for a neighborhood-overlap score ($\rho = 0.8$) but not for a linear probe ($\rho = -0.2$). Second, two precision-targeted levers, parameter-efficient ExPLoRA adaptation of the video encoder and a training-free attribute-decomposed reranker built on a vision-language model, improve the top-rank precision that otherwise limits the frozen system, adding 2.2 points of leaderboard R@1. Third, a local-versus-public calibration study explains which interventions transfer to the real domain. On AI City Challenge 2026 Track 4 the full retrieve-fuse-rerank system reaches 84.25 mAP@10 on the final leaderboard, while a single frozen model submitted alone reaches 60.63. Our trained components cost about 95 GPU-hours. CMP, the dataset authors' fine-tuned cross-encoder that trains for sixteen GPU-days, is one fusion member of the full system, not an alternative. Code and annotations: this https URL

---


### 33. [Sample Count Is Not Enough: Candidate-Generation Strategy Shapes the Energy and Performance of LLM Test-Time Scaling](https://arxiv.org/abs/2609.19499)

**<font color=#1a73e8>作者：</font>** Mobina Kashaniyan, Ali Jannesari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling can improve large language model reasoning by generating and combining multiple candidate responses. In sampling-based methods, the inference budget is often described by the number of generated candidates, N. However, N tells us how many candidates are generated, not how they are executed. The same candidate budget can be produced in one batched generation call or split across several sequential calls with smaller batch sizes. We first study the effect of increasing N on reasoning accuracy using Phi-3-mini and Qwen2.5-1.5B on 500 GSM8K prompts. As expected, increasing N from 1 to 8 improves accuracy by 8.4 percentage points for Phi-3-mini and 18.4 points for Qwen2.5-1.5B. However, accuracy alone does not show the systems cost of using a larger candidate budget. We therefore fix N = 8 and compare four generation schedules: 1x8, 2x4, 4x2, and 8x1, where axb denotes a generation calls with b candidates per call. We measure latency, throughput, GPU-hours, and gross GPU-device energy while keeping the total candidate count fixed. On A100 GPUs, eight serial calls use 4.64-4.86x as much gross GPU-device energy and have 5.77-6.12x the P95 latency of one batched call with eight candidates. The same pattern appears across three independently scheduled A100 nodes per model and in short-output SciQ/V100 experiments. These results show that candidate count alone is not enough to describe the systems cost of multi-candidate test-time scaling. When candidates are independent and memory allows it, fewer generation calls with larger batch sizes are more efficient. Evaluations should therefore report not only candidate count and accuracy, but also generation schedule and GPU-level systems metrics.

---


### 34. [For Your Eyes Only: Evaluating Coordination Between Isolated Language Model Instances](https://arxiv.org/abs/2609.19504)

**<font color=#1a73e8>作者：</font>** Alexander Shirnin, Aleksey Kudelya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As model-generated content is increasingly consumed by other model instances in automated workflows, a practically important question arises: can a model embed a signal in natural language that an independent instance of the same model can detect, relying only on shared pre-training and task instructions, without any shared memory or coordination-specific training? We introduce For Your Eyes Only, a cooperative signalling game designed to evaluate this directly. A Sender produces free-form descriptions for two words, one of which is a hidden target; an isolated Receiver must identify it. We evaluate seven contemporary models from four architectural families on 300 word pairs from established psycholinguistic corpora, using the Double-Pass Success Rate to control for output biases. We find that most models struggle to maintain coordination once they are required to avoid detectable signals, while one frontier model retains near-perfect performance even after such filtering. We further show that models can direct this capability toward deliberate misdirection, and that coordination is consistently weaker across architectures than within them.

---


### 35. [QVAC Genesis III: A Large-Scale, High-Quality Open Synthetic STEM Corpus for Efficient Language Model Pre-Training](https://arxiv.org/abs/2609.19513)

**<font color=#1a73e8>作者：</font>** Davide Vitabile, N. Ranjan, Akshay Nambiar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-quality pre-training data is a critical bottleneck for educational and STEM-specific language models targeting edge AI and on-device deployment where token budgets are tightly constrained. While major organizations train ever-larger models on private corpora, the open ecosystem lacks STEM-focused synthetic datasets that deliver high per-token learning value efficiently for small models. To address this gap, we introduce QVAC Genesis III, a 191.43B-token, STEM-focused multi-domain synthetic corpus covering 19 domains across several difficulty levels and different educational styles. QVAC Genesis III is built via a dual generation strategy that performs targeted teacher distillation using a weak edge-scale student model as signal: the student's failures are converted into corrective explanations, while its successes are expanded into contrastive option-level reasoning over all answer choices. We further introduce an LLM-as-a-parser evaluation protocol that extracts final answers from free-form outputs and tracks both accuracy and answer validity. To validate the effectiveness of our QVAC Genesis III data, we conduct controlled from-scratch ablations with 1.7B-parameter models, showing that models trained with QVAC Genesis III consistently outperform both models trained with the open-source synthetic corpus Cosmopedia-v2 and the publicly released Cosmo-1B model across ARC, GPQA Diamond, and MMLU STEM benchmarks, achieving up to +28.57% on ARC-E and +21.35% on ARC-C, while reaching a Valid Answer Rate of up to 99.45%.

---


### 36. [LLM-as-an-Improver: Turning Verification into Better Candidates](https://arxiv.org/abs/2609.19515)

**<font color=#1a73e8>作者：</font>** Akiyoshi Tomihari, Yuma Ichikawa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifier-based selection improves LLM performance by generating multiple candidate solutions and using a verifier to select the most promising one. However, existing methods typically treat verification only as a ranking step and discard its feedback once a fixed candidate pool has been evaluated. In this paper, we ask whether verification can also improve the candidate set itself. To this end, we introduce LLM-as-an-Improver and propose Verify--Repair--Reselect (VRR), which uses verification feedback to generate and reselect improved candidates. VRR retains the initial winner while conditionally generating three complementary alternatives: repaired versions of the winner and runner-up, and a solution based on a new approach. It filters invalid and duplicate candidates using only inference-time information and then reselects the final answer under the original evaluation criteria. Across diverse models and code-generation and reasoning benchmarks, VRR improves over fixed-pool verifier-based selection in many settings and can recover correct solutions even when all candidates in the initial pool are incorrect. These results highlight a broader role for LLMs as improvers: verification feedback can not only select among existing solutions but also construct stronger candidates beyond the initial pool.

---


### 37. [An Architecture for Long-Horizon Agents: Levels, Ticks and Cascaded Intelligence](https://arxiv.org/abs/2609.19519)

**<font color=#1a73e8>作者：</font>** Erik Nijkamp, Anurag Koul, Egor Pakhomov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents are increasingly asked to carry out work spanning days or weeks, such as an operations remediation or a research programme. Such a task outlives any context window, any process and any interval at which a person can attend. In this paper, we argue that a long-horizon agent must run continually without forgetting before it can learn continually. This ability lies in the harness around the model rather than in the model itself. We derive seven bottlenecks from the long-horizon setting and answer them with a hierarchical architecture of three parts: (i) levels indexed by time scale, each keeping a bounded file summarising the level below; (ii) a clocked tick as the unit of autonomous action; and (iii) cascaded intelligence, where work is escalated to a more capable model only after failing review. We report on a ten-day campaign in which an agent built on this architecture reproduced a published reinforcement-learning result with a human attending once a day, and show (1) the agent kept the thread across every context reset and session boundary of the campaign, (2) operating knowledge written early changed later behaviour with no change to model weights, and (3) where learned components would enter such a system. Overall, our experience suggests continual learning for these agents needs a substrate outliving every context and process, and the checks the harness already runs are where a learner belongs.

---


### 38. [A Unified Evaluation Framework for Trustworthy Large Language Models, Agentic AI, and Multimodal Systems](https://arxiv.org/abs/2609.19524)

**<font color=#1a73e8>作者：</font>** Shaina Raza, Ahmed Y. Radwan, Imran Liaquat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmark scores alone provide an incomplete basis for assessing the trustworthiness of modern artificial intelligence systems. Large language models (LLMs), agentic systems, and multimodal models (MLLMs) require different forms of assessment, yet their evaluation evidence must remain interpretable for development and oversight. We propose a unified framework that connects output-level, trajectory-level, and cross-modal assessment through eight trustworthiness dimensions: capability, robustness, safety, fairness, transparency, governance, oversight, and efficiency. The framework preserves system-specific metrics while mapping native measurements to common performance bands, accompanied by uncertainty estimates and traceable evidence. A meta-evaluation layer examines the validity, reliability, and reproducibility of the evaluation itself. Multidimensional profiles expose strengths and weaknesses, while safety-critical overrides prevent aggregate scores from masking critical failures. Mappings to governance frameworks, international standards, and European Union regulatory requirements connect technical assessment with oversight needs. The framework provides a structured basis for assessing both system performance and the credibility of the evidence supporting it, with empirical validation across deployment contexts remaining an essential next step.

---


### 39. [Self Improvement via Fast Tree-search](https://arxiv.org/abs/2609.19526)

**<font color=#1a73e8>作者：</font>** Xinghong Fu, Aravinth Kulanthaivelu, Yutaro Yamada  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents can recursively modify their own implementations, forming a loop of self-improvement. While prior work shows this can boost performance on coding benchmarks, existing approaches are costly and compute-intensive. We introduce a simple, sample-efficient self-improvement framework that significantly improves coding performance under strict budget constraints. We identify evaluation of candidate self-modifications as the main runtime bottleneck since prior approaches estimate their effectiveness by re-running a subset of benchmark tasks with the modified agent, which is time-consuming. We introduce Recursive Self Improvement via Fast Tree-search (SIFT), which augments these downstream task evaluations with an LLM-as-a-judge signal that performs pairwise comparisons between candidate patches, where the win-loss record is aggregated with a regularized Bradley-Terry model, and the resulting strength scores drive rank-based parent sampling inside a lightweight disaggregated tree search. Expensive downstream task evaluations are reserved only for the most promising nodes. Using a fully disaggregated tree search pipeline, the judge scores provide intermediate signal to guide exploration on promising candidate patches without being bottlenecked by slow evaluation runs. SIFT outperforms existing tree-search based self-evolution frameworks on the full Polyglot benchmark with significantly lower resource requirements in terms of CPU hours, wall clock time, and API cost.

---


### 40. [When Hiring Becomes Agent-Mediated: Evaluating Access and Recurrence in Two-Agent Résumé Screening](https://arxiv.org/abs/2609.19530)

**<font color=#1a73e8>作者：</font>** Jian Gao, Hang Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hiring is bilateral: employers assess fit, while candidates present and defend evidence of their qualifications. Yet résumé screening, the first gate, is commonly automated as a static, one-call judgment over a résumé-job pair. We study a two-agent alternative in which employer-side and candidate-side agents represent these roles, exchange evidence, and update their judgments before deciding who advances. We compare procedures on 600 constructed résumé-job pairs using GPT-5.5 and Claude Opus 4.7. Two-agent screening advances more applications (33.3% to 39.3% for GPT-5.5; 34.0% to 35.5% for Opus 4.7). Across three runs on the common 191-pair borderline pool, pass-instance rates rise from 4.5% to 26.2% and from 6.5% to 16.1%, respectively. This is not a uniform relaxation: two-agent screening rejects applications one-call advances, changing decisions in both directions. At similar pass volumes, the procedures advance different applications, and no one-call threshold recovers applications consistently selected by two-agent screening. Among discovery-selected cases re-executed in fresh runs, two-agent-only selections recur less often than shared selections, clearly under GPT-5.5 and less certainly under Opus 4.7, while a separate one-call follow-up shows no comparable decline. As hiring becomes agent-mediated on both sides, the screening procedure, not only the model behind it, shapes who reaches human review and how reliably that access recurs.

---


### 41. [Agentic AI Networking for Heterogeneous Unmanned Aerial Systems in Low-Altitude Wireless Networks](https://arxiv.org/abs/2609.19538)

**<font color=#1a73e8>作者：</font>** Nguyen Duc Minh Quang, Chang Liu, Shuangyang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low-altitude wireless networks (LAWNs) are emerging as a key infrastructure for heterogeneous unmanned aerial systems that support concurrent services within a shared three-dimensional airspace. Their coexistence creates strong coupling among mobility, connectivity, and shared network resources, while heterogeneous services impose distinct and time-varying requirements. These interactions naturally form a dynamic non-cooperative game in which both operating conditions and coordination objectives evolve over time. Conventional optimization and learning-based controllers typically rely on predefined objectives, limiting their ability to adapt autonomously to changing service requirements and resource priorities. To address this challenge, we propose a hierarchical hybrid large language model (LLM)- multi-agent reinforcement learning (MARL) architecture organized as a dual-loop structure. Specifically, an outer adaptation loop employs LLM-assisted game orchestration to interpret service requirements and operator intent, and reconfigure objectives and resource priorities, while an inner loop executes decentralized, parameter-conditioned MARL policies under the configured game. A logistics-monitoring case study illustrates how the proposed framework facilitates coordinated coexistence among heterogeneous services, adapting to evolving operating conditions without retraining the underlying MARL policies. Finally, we discuss key challenges and research directions toward scalable, trustworthy, and adaptive agentic LAWNs.

---


### 42. [From Parameters to Behaviors: A Survey of Model Fusion for Large Language Models](https://arxiv.org/abs/2609.19553)

**<font color=#1a73e8>作者：</font>** Shuo Cai, Yanggan Gu, Zihao Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model fusion integrates the capabilities from source models into a single target model. As of June 2026, Hugging Face hosts more than 2M models. This growing pool provides a rich base for model reuse and capability integration. Yet existing surveys often cover only separate parts of this space, and they do not provide a unified definition or a systematic taxonomy. This survey defines model fusion and organizes prior work into three levels: parameter-level, representation-level, and behavior-level fusion. We also review related metrics, benchmarks, and applications, summarize current challenges, and identify future directions. Our goal is to provide a clear map of this area and support future work on model fusion. A comprehensive list of papers about model fusion is available at this https URL.

---


### 43. [Learning from Success and Failure: Acquiring Adaptive Dialogue Strategies for Social Robots](https://arxiv.org/abs/2609.19570)

**<font color=#1a73e8>作者：</font>** Sanae Yamashita, Yuki Okafuji  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traditional dialogue systems for social robots require both dialogue strategies and user attribute recognition, each demanding specialized expertise. However, data collection is costly in real-world deployments, and the resulting datasets often include many failure cases. In this study, we aim to automate the acquisition of dialogue strategies by leveraging both successful and failed interactions using a vision-language model (VLM) and a large language model (LLM). We propose an architecture in which user attributes, recognized by the VLM, along with dialogue history, are fed into the LLM to generate dialogue strategies tailored to specific user attributes. We extracted dialogue strategies from an interaction dataset collected through a field experiment and evaluated their effectiveness. The results demonstrate that explicitly representing failure strategies complements success strategies and improves performance. Our findings highlight a practical pipeline for constructing and maintaining an interpretable strategy repository from in-the-wild deployment logs by recycling abundant failure interactions as reusable constraints, ultimately reducing the development cost of social robots.

---


### 44. [CliniCIRCA: A Modular LLM Framework for Constructing Longitudinal Mental Health Patient Journeys from Raw EHR Narratives](https://arxiv.org/abs/2609.19585)

**<font color=#1a73e8>作者：</font>** Aiwei Ivy Zhang, Nimra Ishfaq, Mohit Chandra 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In mental health care, reasoning over patient journeys is a key task for clinicians. Yet these journeys, encompassing a longitudinal progression of biological, psychological, and social events, are often spread across disparate unstructured text narratives, making temporal recovery challenging. We present CliniCIRCA, a multi-stage LLM framework for Calendar-anchored, Imprecision-aware Reconstruction of Clinical Annals. To our knowledge, CliniCIRCA is the first to temporally classify clinical events across unstructured discharge summaries without event-level timestamps. From 14,882 MIMIC-III mental health admissions, we first construct a benchmark of 52 discharge summaries on which CliniCIRCA produces 15,891 temporally tagged events. After correcting 629 errors based on a clinician-in-the-loop evaluation, we produce verified gold-standard labels. Finally, the corrected timelines drive a temporally grounded summarization stage that compresses each source 1.52 times into a date-grouped chronological record. We then scale the framework to generate 1,000 silver-standard timelines and evaluate them as training data. Compared with zero- and few-shot prompting, instruction tuning generally improves five open-weight models on event extraction, temporal tagging, and summarization across silver and clinician-verified evaluations.

---


### 45. [Form Over Content In Gradient-Based Data Attribution Methods](https://arxiv.org/abs/2609.19589)

**<font color=#1a73e8>作者：</font>** Sunwoo Kim, Seokwon Jung, Sohyung Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data attribution methods using gradient similarity are widely used to analyze and select training data for large language models, but what gradient similarity actually measures is debated. Some interpret it as identifying task-relevant skills, while other work reports that surface form is the main factor. We resolve this debate for supervised fine-tuning examples by varying task and answer format independently. Specifically, we render benchmarks in different answer formats, such that datasets can share a task without a format or a format without a task. We find that gradient alignment follows the answer format, as benchmark pairs sharing an answer format align strongly (disattenuated cosine near 0.4), while same benchmarks rendered with different answer format classes show no alignment (near 0.0). We demonstrate that this ordering holds from the earliest pretraining checkpoints through post-training, and across model scales and families. We then analyze the released selections of LESS, a gradient-based data selection method for instruction tuning, and find that each target's selections over-represent the target's own answer format. Hence, we demonstrate that gradient-based attribution methods track format similarity more than task semantics, meaning that such methods, as well as the semantic interpretation of the gradient, should be tested on data where answer format and task vary independently for greater robustness and reliability.

---


### 46. [Chain-of-Thought Entropy as a Reliability Signal: A Preregistered Reproduction](https://arxiv.org/abs/2609.19606)

**<font color=#1a73e8>作者：</font>** Theodore O. Cochran  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This empirical study is an independent reproduction of the dissociation Zhao reported in 2026. The shape of a large language model's chain-of-thought entropy trajectory predicts whether the final answer is correct, while the magnitude of its total entropy drop does not. The dissociation merits reproduction because the magnitude half rests on a single 300-problem run with one model at one seed, while the shape half was reported at full scale on both benchmarks and on a second model family. Registered at OSF before any confirmatory run, the reproduction crosses the complete GSM8K and MATH-500 benchmark test sets with four open-weight models including one reasoning-distilled model of a kind the original did not test. The shape signal replicates. The magnitude signal divides by setting. On the anchor model the accuracy gap between monotone and non-monotone chains is +9.6 percentage points on GSM8K and +27.5 on MATH-500, while the rank correlation of the total entropy drop with correctness is -0.018 on GSM8K and +0.414 on MATH-500. On the reasoning-distilled model the binary form of the shape signal fires on about one chain in a hundred, too few to estimate the registered contrast, while the graded violation count remains predictive there. In an exploratory comparison the final-step entropy alone outperforms the binary shape flag in all eight model-by-benchmark cells by ROC area, and in six or seven by the risk-coverage area the original reports, depending on an integration range the original does not state. The study contributes a reproduction of the shape signal at full test-set scale under seven documented protocol differences, a map of the settings where the magnitude signal holds and fails, and measurements of four protocol dependencies the original does not report.

---


### 47. [Semantic Layer Induction from Raw Telemetry via Hierarchical LLM and RAG Abstraction](https://arxiv.org/abs/2609.19615)

**<font color=#1a73e8>作者：</font>** Yuanzhe Jia, Ali Anaissi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern applications generate massive volumes of raw telemetry data, but translating those noisy, heterogeneous event streams into actionable business insights remains a fundamental challenge. Data engineers and analysts expend substantial effort reconciling semantic discrepancies, hand-crafting parsing logics, and maintaining fragile mappings between raw data and business KPIs. In this paper, we present an end-to-end framework that fully automates the construction of a business semantic layer from application raw logs. Our approach introduces a two-stage semantic abstraction: first, high-level business features are identified via LLM inference augmented with domain-specific industry knowledge; second, fine-grained business nodes are derived through a structured pipeline comprising data refinement, hybrid retrieval, multi-stage filtering, semantic clustering, and canonical naming. Evaluation on production-scale telemetry demonstrates that our system improves human-assessed semantic quality from 50 to 80+ on a 100-point scale, reduces maintenance effort by 80%, filters out 74% of noise, and achieves 0.87 Cohen's kappa via an integrated LLM-as-Judge evaluation, enabling continuous, scalable quality assurance. Overall, our work distinguishes itself from prior work by addressing the novel problem of business semantic layer induction from raw telemetry, operating without labeled training data or manual rule engineering.

---


### 48. [The Complexity Kink: A Prompt-Side Structural Complexity Index for Code-Generation Reliability](https://arxiv.org/abs/2609.19616)

**<font color=#1a73e8>作者：</font>** Michael Hernandez, Tian Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complexity measured from generated code is failure-dependent: a difficult prompt can yield a short failing program and be assigned low output complexity. We introduce a six-dimension prompt-side structural-complexity index scored before generation and kept separate from correctness. We select 5,000 Python prompts across six bands of a preliminary single-rater rubric. Four out-of-panel LLM raters rescore the locked prompts, giving 19,997 score rows; composite inter-rater reliability is ICC = 0.872 on the 4,998 prompts with all four ratings. We evaluate 21 models per prompt, yielding 105,000 generations. In the unadjusted mean-pooled analysis, pass rate has a nonmonotone breakpoint at composite 13.75, with 79.9% at or below and 87.6% above. This is not a universal failure cutoff. Task-type fixed effects shift the breakpoint to 10.75 and cut the regime gap from 7.6 to 2.1 points. A construction-frame control shifts it to 8.50 with a raw gap of -3.5 points, and neither frame alone reproduces the pooled +7.6-point change. Model-specific fits include 16 upward and five downward changes. A 365-prompt audit-clean extension matches the original five-model estimates at bins 15 and 16 but adds only 14 prompts above bin 16. Among zero-pass generations with computable Lizard complexity, 28.5% pair a prompt composite above 8 with output complexity at most 10. Human agreement is moderate and rater-dependent on a disagreement-enriched calibration set; paraphrase and cross-language rescoring preserve score ordering. Overidentification tests reject the joint restrictions on the six dimensions, so we treat the composite as an index and make no causal interpretation of the 2SLS estimates. The contribution is a pre-generation measurement framework and a bounded observational analysis of reliability regimes.

---


### 49. [DataCanvas-EDU: An Agentic Framework for Instructor-Guided Synthetic Data Generation in Business Analytics Education](https://arxiv.org/abs/2609.19617)

**<font color=#1a73e8>作者：</font>** Bang An, Maria Hamdani, Joseph Fox  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Business analytics education requires diverse datasets to support different learning objectives, student backgrounds, and analytical tasks. Real-world data can be difficult to obtain and offer limited flexibility for adapting a case to a particular course. Even when suitable data are available, instructors must investigate the patterns, verify the results, and prepare assignments and reference solutions, requiring substantial time and effort. The use of large language models (LLMs) introduces an additional concern about training data contamination. Widely used public datasets often have extensive tutorials and worked analyses that models may have encountered during training. Students may therefore receive explanations drawn from existing analyses without practicing how to investigate unfamiliar data in collaboration with AI. This paper presents DataCanvas-EDU, an agentic framework for instructor-guided synthetic data generation in business analytics education. Instructors specify teaching goals and intended patterns through conversation, while an AI agent writes generation code, checks the resulting data, and prepares assignments, reference analyses, and rubrics. Four phases, Plan, Create, Verify / Test Analysis, and Evaluate, organize the process and support instructor review and revision. The framework is intended to simplify case preparation while creating opportunities for students to investigate newly designed patterns with AI. We illustrate the approach with WindowDash, a food delivery case containing 15,000 orders and nine designed patterns. DataCanvas-EDU is packaged as a reusable AI Agent Skill for compatible agent environments, with the package and installation instructions available at this https URL

---


### 50. [Scientific Image Quality Assessment via Multi-modal Retrieval-Augmented Generation](https://arxiv.org/abs/2609.19634)

**<font color=#1a73e8>作者：</font>** Yinuo Zhang, Bingshuo Liu, Zhiying Tu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a Retrieval-Augmented Generation (RAG) framework for scientific image quality assessment, designed to simultaneously address both the understanding track (SIQA-U) and the scoring track (SIQA-S) of the SIQA challenge. We construct a multimodal index that integrates textual semantics with fine-grained visual features, and develop a multi-route retrieval and fusion mechanism to provide large language models with highly relevant reference cases, thereby enhancing their capability to evaluate complex scientific images. Experimental results demonstrate that the proposed framework effectively aligns with the judgment criteria of human experts. Ultimately, our method achieves 1st place in the SIQA-U track of the SIQA challenge at the ICME 2026 Grand Challenges.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-176](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
