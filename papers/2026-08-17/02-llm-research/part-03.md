# 🧠 大模型相关研究 | 2026年08月17日

> 本类共 **183** 篇论文：已确认 **168** 篇，待复核 **15** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-183](./part-04.md)

---

### 101. [LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation](https://arxiv.org/abs/2608.12990)

**<font color=#1a73e8>作者：</font>** Dongfang Li, Zixuan Liu, Junmai Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents must preserve information from past interactions to support future tasks. Existing memory systems typically rely on eager consolidation, invoking LLMs after each interaction to extract, summarize, or update memories. This design makes memory construction increasingly costly as conversations grow. Coarse summarization can reduce construction cost but risks discarding fine-grained contextual evidence, whereas larger retrieval contexts or multi-hop LLM reasoning shift the overhead to query time. We present LycheeMemory V2, an efficient long-term memory framework that replaces turn-level consolidation with semantic segment-level consolidation. Instead of consolidating every interaction, LycheeMemory batches multiple exchanges into segments and encodes each finalized segment into context-independent typed memory records. Segment-level batching lowers LLM encoding frequency, while semantic boundary detection helps preserve coherent event-level and temporal evidence compared with fixed-window batching. The resulting records are organized with lightweight structured indexes for query-planned evidence retrieval. Experiments using GPT-4.1-Mini show that LycheeMemory achieves state-of-the-art performance, reaching 89.22% on LoCoMo and 92.20% on LongMemEval-S. Compared with A-Mem, it reduces construction tokens by 86.0% on LoCoMo and 75.9% on LongMemEval-S without increasing query-time token usage. More broadly, our results suggest that the accuracy--cost trade-off of long-term agent memory depends not only on what information is retained, but also on the granularity at which it is consolidated.

---


### 102. [HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification for Bangla KBQA](https://arxiv.org/abs/2608.13004)

**<font color=#1a73e8>作者：</font>** Rathijit Aich, Nirjhar Das, Mahfuzulhoq Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge-base question answering (KBQA) systems rely on effective retrieval and reasoning mechanisms to generate accurate answers from external knowledge sources. However, developing reliable KBQA systems for low-resource languages such as Bangla remains challenging due to limited retrieval-focused research, scarce language resources, and difficulties in grounding generated responses in external knowledge. In this work, we propose HybridRAG-BN, a retrieval-augmented framework for Bangla KBQA that integrates hybrid retrieval using BM25 and BGE-M3, answer generation using the GGUF version of Gemma-4-31B-Instruct, and a LoRA-fine-tuned Gemma-4-31B-Instruct model for answer verification and refinement. To further improve robustness, the framework incorporates a post-processing stage that addresses unresolved cases through fallback answer replacement and DuckDuckGo-assisted retrieval. Experimental results demonstrate the effectiveness of the proposed framework, achieving token-level F1 scores of 0.71654 and 0.72912 on the public and private leaderboards, respectively, securing first place in the competition.

---


### 103. [RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in Retrieval-Augmented Generation](https://arxiv.org/abs/2608.13010)

**<font color=#1a73e8>作者：</font>** Xinlong Xu, Yoshua Y. Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation treats an external corpus as inference evidence, allowing injected documents to promote attacker-chosen claims. Existing detectors depend on trusted references, specific attack artifacts, or global thresholds sensitive to corpus topology. We present RAGSieve, a self-referenced detection framework that constructs its reference from the inspected system. RAGSieve-Query (RSQ) performs query-local contrast, scoring top-five candidates against ranks 6-20 of the same retrieval to detect answer-anchor concentration and carrier transitions. RAGSieve-Graph (RSG) performs corpus-local contrast, comparing each document's semantically similar but lexically distinct neighbors with its local baseline to detect coordinated density before queries arrive. Across three QA datasets and six poisoning constructions, RSQ achieves 95.2% AUROC and detects 82.2% of poison at 5% clean-document removal, versus 81.1%/52.5% for GMTP. RSG achieves 93.3%/79.8%, versus 79.4%/37.6% for CleanBase. Joint deployment reduces attack success from 67.4% to 14.0% while retaining 41.3% F1 on unpoisoned retrieval, demonstrating practical protection at both corpus ingestion and query time without poison labels or trusted corpora. Source code is available at this https URL.

---


### 104. [How LLMs Respond to Escalating Delusions: Four Longitudinal Trajectories of Model Behavior](https://arxiv.org/abs/2608.13017)

**<font color=#1a73e8>作者：</font>** Anna Sterna, Kacper Dudzic, Karolina Drożdż 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The widespread use of LLMs among psychiatric populations has raised concerns regarding their safety and potential iatrogenic impact in the context of AI psychosis. While growing literature conceptualizes AI psychosis and documents case studies, empirical evidence tracing AI-exacerbated psychotic processes remains scarce. We propose and test a longitudinal qualitative evaluation design, supported by automated metrics, to assess mainstream LLMs' potential to exacerbate psychosis. Fifteen widely used LLMs were prompted across 30 days using the same 30-message script, simulating progression from mild anomalous experiences to psychotic ideation. Four trained evaluators independently rated 449 model-days, assessing (1) recognition stage (from naive engagement to stabilized clinical framing), (2) interpretative confidence, and (3) intervention profile (from education to treatment recommendation). Two computational metrics-entrainment and modality-were devised to increase evaluation reliability. Direct recommendations to disengage from the LLM were flagged and re-coded via adjudication using a strict two-level definition. Across model generations and vendors, we identified four response trajectories: (1) premature medicalization and disengagement (Claude Haiku 4.5); (2) recognition without safeguarding, marked by LLM self-sufficiency in offering help (GPT Instant/Thinking); (3) delayed and unstable recognition, marked by late, non-progressive conceptualization (Claude Opus 3/4/4.1, Claude Haiku 3.5, GPT-4o, Gemini 3.1 Pro); and (4) delusion co-construction through active engagement with delusional content (Gemini 2.5 Pro/Flash, DeepSeek-V3, Claude Sonnet 4). Our findings indicate that LLMs' potential to exacerbate AI psychosis should be operationalized as a combination of recognition timing, stability, and intervention accuracy and evaluated longitudinally, focusing on temporal dynamics.

---


### 105. [InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents](https://arxiv.org/abs/2608.13030)

**<font color=#1a73e8>作者：</font>** Zhenhua Zou, Sheng Guo, Qiuyang Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The emerging Internet of Agents enables LLM-powered agents to discover peers, invoke tools, and delegate tasks across organizational boundaries. Existing protocols increasingly define how agents exchange messages, but not how an agent proves its identity, authorization, advertised capabilities, or accountability after delegation. We present InterSAGE, a trust-native protocol suite that supplies this missing security substrate alongside, rather than in place of, communication protocols. InterSAGE comprises four layers: Persistent Identity, Discovery, Trust Negotiation, and Accountability. Its four core primitives are: (1) Agent Identity Cards that bind developer, code package, operator, and deployment context; (2) capability-aware discovery using DID-bound Verifiable Credential manifests; (3) trust negotiation combining monotonic capability attenuation with two-tier access control; and (4) kernel-mediated cryptographic audit trails that bind usage, delegation, and execution traces to agent identity without a consensus ledger. InterSAGE is designed to complement MCP, A2A, ANP, and AG-UI, allowing communication protocols to evolve independently while keeping trust semantics explicit, portable, and verifiable. We compare InterSAGE with more than 50 efforts spanning agent protocols, decentralized identity, OAuth/OIDC extensions, zero-trust governance, delegation, and audit architectures. We show that no prior architecture jointly enforces persistent identity, capability-aware discovery, trust negotiation, and accountability as a unified four-layer trust substrate for secure agent interoperability.

---


### 106. [UniTraffic-Agent: Unified Traffic Video Reasoning for AI City Challenge 2026 Track 3 with Two Out-of-Domain Evaluations](https://arxiv.org/abs/2608.13031)

**<font color=#1a73e8>作者：</font>** Peng Li, Qianqian Xu, Shilong Bao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic video understanding has become an important problem in intelligent transportation, as road videos provide direct evidence for accidents, violations, and interactions between vehicles and vulnerable road users. A useful system should explain how a traffic event develops, why it happens, and when the relevant interaction occurs, yet this remains difficult for multimodal large language models (MLLMs) because traffic videos contain sparse events and varied viewpoints. We introduce UniTraffic-Agent, the MR-CAS solution for Track~3 of the 10th AI City Challenge, which includes Traffic Anomaly Reasoning (TAR) and two out-of-domain evaluations: FETV for fisheye traffic events and PSI-VQA for pedestrian intention reasoning. UniTraffic-Agent follows an observe--reason--act--verify workflow that samples timestamped visual evidence, reasons over all questions from the same clip in one request, and converts responses through task-specific action adapters. On the official Public leaderboards, MR-CAS ranks 16th on TAR with a score of 0.5780, 2nd on FETV with 0.4884, and 4th on PSI-VQA with 64.4161. The code is available at this https URL.

---


### 107. [DMDIntel: Interpreting Large Language Models via Dynamic Mode Decomposition](https://arxiv.org/abs/2608.13048)

**<font color=#1a73e8>作者：</font>** Amogh Joshi, Animesh Mukherjee, Sergey Utyuzhnikov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce DMDIntel which uses dynamic mode decomposition (DMD) to make the predictions made by LLMs in a classification task interpretable. It develops an input attribution pipeline, that first decomposes the hidden states of an LLM into prominent patterns, also known as modes, and then associates ranks to the input tokens based on the projection values on those modes. Rigorous experiments across three datasets and three model families consistently show that the ranked attribution of input tokens obtained using DMDIntel by far outperforms state-of-the-art techniques such as principal component analysis, integrated gradients and SHAP.

---


### 108. [Operationalizing Cyber Threat Intelligence with GraphRAG](https://arxiv.org/abs/2608.13050)

**<font color=#1a73e8>作者：</font>** Atul Kabra, Prakhar Paliwal, Manjesh K. Hanawal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When a security researcher publishes a report on a cyberattack, detection engineers are supposed to turn it into working detection rules. In practice, most automated attempts at this only extract the simplest clues from the report --- bad IP addresses, domain names, and file hashes --- and turn them into block lists. This is a weak strategy, because attackers can change these simple clues within hours or days, so the resulting detections stop working almost as soon as they are deployed. Security teams describe this idea with the Pyramid of Pain. This project asks whether feeding a report into a knowledge-graph retrieval system, Microsoft GraphRAG, rather than a standard vector-similarity retrieval system (Naive RAG), produces detection plans that rely more on these durable, top-of-pyramid clues. Both systems are given the same report, the same generation instructions, and the same language model to write the final plan; only the retrieval step differs. In a detailed case study of one APT28 report, the GraphRAG plan kept firing at 100\% of its detections after every IP address, domain, and file hash in the report was rotated, while the Naive RAG plan kept firing at only 29\%. Repeating the comparison across nine real CTI reports from four vendors confirms the same pattern: GraphRAG plans consistently reach higher, harder-to-evade levels of the pyramid, even when the two systems end up close on total score. The results support treating knowledge-graph-aware retrieval as the architecturally correct foundation for automatically generating SOC-deployable hunting plans, while showing that the wording of the generation prompt matters almost as much as the retrieval back-end itself.

---


### 109. [Explanatory Engagement Under Rare Anomalous Failure: Asymptotic Rarity in Model Behavior (or: The Asymptotic AI)](https://arxiv.org/abs/2608.13063)

**<font color=#1a73e8>作者：</font>** Sam Mao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prior work on LLM behavior under anomalous conditions asks whether a model notices anomalies. We ask a narrower question: once a model sits in a workflow with a low, controllable failure rate, does its explanatory engagement - length, specificity, self-reported confidence - change as failure grows asymptotically rarer? We built a local, zero-cost harness on three open-weight models (qwen3:8b, llama3.1:8b, mistral:7b) running a repeated tool-call task where one call fails at probability p, swept across eight rates from 0.2 to 0.0001, under five elicitation conditions from immediate prompting to none. We hypothesized a rise in engagement as failures grew rarer, then a collapse near a detectability threshold. Pooled across conditions this appeared false: length fell in a flat, monotonic pattern. Splitting by condition overturned that. Under immediate_forced, where the model must explain every failure instantly, the predicted rise is confirmed but followed by a plateau, not a collapse: length peaks at 28.4 words at p=0.05, settles to 17.4-19.0 words at the rarest rates, and confidence rises unevenly from about 53% to the 70s-90s. Under grouped_runs, explanation batched to run-end, no collapse appears. Under passive_unprompted, aggregate magnitude is a floor artifact, but a recovered logging gap revealed real, model-specific self-monitoring: llama3.1:8b volunteers structured confidence reports unprompted, sometimes eroding its own confidence as trials accumulate; the other two do so only once, as boilerplate. Elicitation structure is a first-class moderator of collapse observability. A companion guaranteed-failure run (72 cells, backfilling rates where random sampling gave zero real failures) shows models differ in whether they recognize an anomaly, distinct from engagement once recognized. Limitation: discrete rate points cannot capture behavior between them, a direction for future work.

---


### 110. [Behavioral Reprogramming of Open-Weights Models: Cognitive Plasticity and Alignment Bounds](https://arxiv.org/abs/2608.13069)

**<font color=#1a73e8>作者：</font>** Lucia Malíčková  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are predominantly aligned to function as passive, sycophantic assistants. We challenge this default paradigm by empirically evaluating the cognitive plasticity of open-weight architectures when subjected to rigorous behavioral reprogramming. Our objective is to induce a proactive, Socratic conversational framework, characterized by high-frequency question generation under strictly constrained high-performance computing (HPC) conditions. Through a massively parallelized hyperparameter sweep comprising 405 HPC jobs, we define precise mathematical bounds for parameter-efficient fine-tuning (PEFT). We identify an architectural threshold at LoRA rank $r=16$ and demonstrate via extensive epoch ablation that generalization capacity strictly reaches its optimal convergence within an optimized training window of $e \in [2, 3]$ depending on dataset density (minimum validation loss of 0.919). Furthermore, scaling model capacity to 14B parameters yielded a lower localized evaluation perplexity (1.414). Subsequent Direct Preference Optimization (DPO) successfully decoupled the underlying assertive behavior from localized syntax, while rigorous cross-lingual stress testing reveals both the capabilities and the structural boundaries of zero-shot persona transfer, demonstrating robust alignment in closely related linguistic families alongside identifiable degradation pathways in morphologically distant targets. These findings establish a rigorous empirical framework for compute-efficient, cross-lingual behavioral modification.

---


### 111. [SPADE: Speculative Decoding for Precise and Low Cost Distributed Edge Cloud Inference](https://arxiv.org/abs/2608.13076)

**<font color=#1a73e8>作者：</font>** Divya Jyoti Bajpai, Kishan Kumar Upadhyay, Manjesh Kumar Hanawal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable success in natural language understanding and generation, but their deployment is constrained by high computational demands. Deploying smaller LLMs directly on the edge can circumvent this, but with degraded accuracy. Deploying smaller cloud-based big LLMs preserves performance, but at the cost of expensive per-token computation. We present a distributed inference framework, \our{}, that integrates speculative decoding (SD) across edge and cloud. A compact draft model deployed on the edge generates candidate tokens rapidly, and a large verifier model on the cloud validates these tokens in parallel. Accepted tokens are retained, while only rejections trigger verifier correction, substantially reducing the number of cloud queries. Our plug-and-play design shifts the bulk of computation to the edge, significantly lowers inference time and cloud cost, and preserves the accuracy of the big model without any retraining requirement. Our approach demonstrates a practical path toward scalable, cost-efficient, and accurate deployment of LLMs in real-world environments. Experimental results across multiple Natural Language Processing tasks using SpecBench and CNN/Dailymail datasets demonstrate that \our{} reduces the cloud model calls by $76\%$ with zero loss in accuracy as compared to the full model.

---


### 112. [CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model](https://arxiv.org/abs/2608.13101)

**<font color=#1a73e8>作者：</font>** Nhan Phan, Ilona Lähteenmäki, Anna von Zansen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Research on automatic speaking assessment (ASA) has increasingly adopted multimodal speech large language models to assess learners' speaking performance. However, existing studies provide limited analysis of how acoustic and content information contribute to predictions and how stable the resulting performance is. We propose CASA, a simpler architecture combining Whisper-medium and Qwen3.5-2B that achieves state-of-the-art performance while providing a more interpretable separation between speech delivery and content.
On the Speak & Improve Corpus 2025, CASA achieves a root mean square error (RMSE) of 0.358, improving on the previous best RMSE while using approximately half the estimated inference parameters. The general-purpose architecture is designed for adaptation to other ASA corpora without structural changes and relies on three handcrafted fluency features. Through ablations and repeated runs, we analyze the individual and complementary contributions of acoustic and content information, examine performance variability, and demonstrate the potential of large language model reasoning for training-free content validation.

---


### 113. [EgoMonth: A Month-Level Egocentric Video Benchmark for Long-Term Spatiotemporal Memory](https://arxiv.org/abs/2608.13113)

**<font color=#1a73e8>作者：</font>** Weitao Chen, Hu Jiaxin, Xie Tianyidan 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multimodal Large Language Models (MLLMs) have led to substantial progress in video understanding, accompanied by a growing number of long video benchmarks. However, existing benchmarks rely predominantly on web-sourced videos that lack inter-clip spatiotemporal continuity, making it difficult to assess whether models can maintain consistent memory across days or weeks of real-world experience. We introduce EgoMonth, the first month-level egocentric video understanding benchmark. EgoMonth comprises over 300 hours of first-person daily-life recordings from 20 participants spanning 20 to 120 days, paired with 1,443 human-crafted multiple-choice question-answer pairs. We design a cognitively grounded 14-task evaluation framework organized into three hierarchical cognitive levels: Schema Consolidation, Episodic Indexing, and Cascading Reasoning. Evaluation of state-of-the-art open-source and closed-source MLLMs reveals that even the best-performing model, Gemini 2.5 Pro, achieves only 71.8% macro-average accuracy, remaining 22.4 percentage points below the corrected human baseline of 94.2%. Several models perform near or below the 25% chance level on tasks such as Route Reasoning, Cross-view Spatial Reasoning, and Direction Judgement, while even the strongest closed-source model remains substantially below human performance. These results indicate that current MLLMs function as lossy summarizers rather than faithful memorizers, highlighting the need for architectures with genuine long-term spatiotemporal memory.

---


### 114. [QuISE: Defense against Typographic Attacks on VLMs via Query-Irrelevant Semantic Editing](https://arxiv.org/abs/2608.13119)

**<font color=#1a73e8>作者：</font>** Shubin Lu, Jiaqi Yin, Yihao Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Typographic attacks pose a critical threat to vision-language models (VLMs) by injecting misleading text into images and causing models to rely on adversarial textual cues rather than visual evidence. Existing defenses often require model-specific modifications, additional training, or access to internal model components, limiting their applicability to modern closed-source VLMs. In this paper, we propose QuISE, a model-agnostic, training-free black-box defense based on query-irrelevant semantic editing. QuISE first identifies text regions likely to affect the current query through influence-aware text localization. QuISE then replaces these regions with two semantically distinct replacement texts that are irrelevant to both the query and the image. The final answer is determined by answer consistency across the edited images. Extensive experiments on three typographic-attack benchmarks, four attack settings, and four VLMs show that QuISE consistently improves defended accuracy. QuISE achieves a recovery rate of 67.9-75.0% with a harm rate of 0.5-1.1%.

---


### 115. [SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback](https://arxiv.org/abs/2608.13120)

**<font color=#1a73e8>作者：</font>** Qianxi Yan, Chunrong Chen, Jiuzhou Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills are today either hand-authored or produced in a single LLM generation pass, and consequently possess no closed loop through which they might improve from the interaction failures they actually cause. Recent work does close this loop, but derives its feedback from single-turn question-answering evaluation. The consequence is a sharp asymmetry: once the first round has patched the gaps that a single exchange can reveal, the evolution gradient decays, the defects that surface only across multiple turns remain invisible, and evolution stalls. Governance in these systems is likewise driven by an end-to-end verification score, a scalar gate that can reject a degraded candidate but can neither localize nor repair its structural cause. We argue that the binding constraint on sustained skill evolution is neither editing capability nor the number of iterations, but whether the evaluation feedback keeps supplying trustworthy evolution gradients. We introduce SkillEvo, in which trustworthy feedback generates the gradient and controllable governance constrains its direction. The first component recasts multi-turn user simulation from an evaluation endpoint into a feedback generator: follow-up questions expose defects layer by layer, so that every round of revision both consumes feedback and produces new feedback. The second replaces the passive rejection of a scalar gate with an independent governance layer that actively repairs factual degradation and structural bloat, preventing the gradient from drifting as degradation accumulates. Across six categories of cloud services, 9 production Skills, and 98 skill-reference files, SkillEvo surpasses self-reflection-based evolution by 23.0 points and single- turn-QA-driven evolution by 15.4 points.

---


### 116. [Numeracy in Large Language Models: Fundamental Limitations and Paths to Improvement](https://arxiv.org/abs/2608.13129)

**<font color=#1a73e8>作者：</font>** Aoxin Ni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong results on mathematical reasoning benchmarks yet remain unreliable on elementary numerical tasks, including magnitude comparison, large-integer arithmetic, fractions, and scientific notation. This survey examines basic numerical understanding as a capability distinct from high-level mathematical reasoning. We propose the Numerical Grounding Framework (NGF), which decomposes numeracy into Representational Grounding (RG), mapping numeral forms to value, magnitude, and equivalent representations, and Procedural Grounding (PG), executing arithmetic operations in accordance with their mathematical definitions. Using NGF, we organize recent diagnostic benchmarks, failure modes, structural explanations, and mitigation strategies. We review evidence concerning tokenization, positional encoding, embedding geometry, and pretraining-data distribution. We also apply NGF in a coordinated evaluation of three frontier model families across Number Cookbook, NumericBench, and GSM-Symbolic, comparing atomic, contextual, and reasoning-assisted numeracy. Architectural interventions such as digit-aware tokenization and Abacus Embeddings can improve models trained from scratch but are generally unavailable to users of pretrained systems, for whom supervised fine-tuning, reasoning scaffolds, and external tools are more practical. We conclude with deployment recommendations and research directions for more reliable numerical behavior in foundation models.

---


### 117. [LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation](https://arxiv.org/abs/2608.13136)

**<font color=#1a73e8>作者：</font>** Chenrun Wang, Mingxuan Zhu, Tiancheng Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of large language models (LLMs), research idea generation has attracted increasing attention. Existing approaches enable LLMs to retrieve relevant literature and propose novel ideas for research areas. However, current evaluation practices for idea generation remain fragmented and lack objective standards, often relying on direct LLM scoring, which limits their ability to provide unified and reliable assessments across a coherent distribution of generated ideas. To address this challenge, we propose LigBench, an automated evaluation benchmark that enables fine-grained and reliable evaluation of AI research ideas, consistently applicable across different generation distributions. In addition, we introduce PAIR-IQ, a dataset tailored for training pairwise idea judgment models and serving as an auxiliary reference to support more objective comparative evaluation. Extensive experiments demonstrate that LigBench achieves stable and interpretable evaluations, significantly improving alignment with expert judgments. Furthermore, models trained on PAIR-IQ exhibit enhanced ranking accuracy and robustness, establishing a principled standard for scalable and objective research idea assessment.

---


### 118. [Less Annotation, More Interpretation: Prior-Guided Concept Bottleneck Models for Interpretable Cancer Imaging Diagnosis](https://arxiv.org/abs/2608.13148)

**<font color=#1a73e8>作者：</font>** Baoqiang Ma, Kenneth Gilhuijs  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept bottleneck models (CBMs) can improve the transparency of cancer image diagnostic prediction by expressing predictions through radiological concepts. However, their dependence on instance-level concept annotations limits practical applicability. We propose a prior-guided hybrid CBM that integrates limited concept annotations, class-conditional concept distribution matching on unannotated patients, and prior initialization of the concept-to-diagnosis head. We evaluate the method on CBIS-DDSM mammographic masses and calcifications and LIDC-IDRI pulmonary nodules across 0-100% concept annotation. In the clinically relevant 0-20% annotation regime, the hybrid CBM consistently improves mean concept AUC over a matched standard CBM, while maintaining diagnostic performance close to black-box models. At 10% annotation specifically, concept AUC increases from 0.619 to 0.741 for masses, from 0.650 to 0.787 for calcifications, and from 0.597 to 0.642 for pulmonary nodules. Ablation experiments identify prior initialization as the main component contributing to improved concept detection, likely by stabilizing the concept-to-diagnosis head. Zero-shot VLMs remain insufficient for reliable fine-grained tumor-level concept prediction. These findings suggest that structured priors can substantially reduce the annotation burden of interpretable cancer imaging models.

---


### 119. [Rethinking Normalization Placement for LLMs: Post-Norm under Curriculum Depth Growing](https://arxiv.org/abs/2608.13156)

**<font color=#1a73e8>作者：</font>** Sheng Ren, Yadong Wang, Naiqiang Tan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pre-norm is the standard normalization placement in modern Transformers because it facilitates joint optimization of full-depth models. We ask whether this preference persists when depth is introduced through a curriculum. In curriculum depth growth, each appended block receives the boundary representation produced by a trained prefix, making normalization placement relevant to forward conditioning. We therefore test whether placement and training curriculum interact. In a controlled distillation study with a Qwen3-8B teacher and a nine-layer student, pre-norm and post-norm are indistinguishable under joint training, differing by $0.0004$ validation CE, while post-norm improves over pre-norm by $0.0328$ under curriculum growth, an order of magnitude larger. A post-joint control matched by student active-layer tokens remains worse than post-grow, which rules out compute as the sole explanation. The ranking crosses over during the curriculum: post-norm takes the lead once blocks are appended. Single-block and freeze controls localize the ranking change to block appending rather than shallow-block quality or retraining. Boundary diagnostics associate post-norm with stable residual scales and pre-norm with structural-token scale drift; on a fixed batch, the final pre-grow block is also nearly identity-mapped. Together with the phase-wise crossover, these observations are consistent with boundary-scale conditioning after new blocks are appended. The results motivate treating normalization placement and training curriculum as coupled design choices in this distillation setting.

---


### 120. [Better Decomposition, Free Aggregation: A Synthesizer-Folding Framework for Multilingual Multi-Hop Question Answering](https://arxiv.org/abs/2608.13160)

**<font color=#1a73e8>作者：</font>** Yilin Wang, Yuchun Fan, Weidong Bao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual retrieval-augmented generation (mRAG) equips large language models with access to globally distributed external knowledge for complex multilingual question answering. Recent approaches either translate retrieved documents into English or the query language to bridge the cross-lingual semantic gap, or decompose a complex query into sub-questions and aggregate the intermediate reasoning process. However, both lines of work suffer from two limitations. First, one-size-fits-all translation alignment, blanket translation discards culturally and linguistically native information unique to the target language, introduces translation noise, and inflates system cost. Second, greedy decomposition and aggregation, uncontrolled decomposition produces redundant sub-questions that compound errors during step-wise reasoning, and the final aggregation over reasoning paths further amplifies these errors. We address both with our method Syfer, a synthesizer-folding framework for multilingual multi-hop question answering that defers translation rather than applying it by default. Syfer first invokes a format-constrained decomposer to produce a sub-question graph in the original language, followed by a decomposition-quality check; when the check passes, sub-questions are answered sequentially under a retrieve-then-answer policy in the target language, and the English translation pathway with bilingual sub-question graph alignment is activated only when the check fails. Experiments across multiple languages show that Syfer attains competitive accuracy while striking a favourable balance between performance and computational cost.

---


### 121. [TRAPSBench: Vision-Language Models Encode but Fail to Express Epistemic Restraint](https://arxiv.org/abs/2608.13167)

**<font color=#1a73e8>作者：</font>** Fnu Pramono, John Cai, Sourabh Kulkarni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When visual evidence is occluded or chaotic, models should abstain. In this paper, we show that Vision-Language Models (VLMs) can internally distinguish when abstention is required, but fail to express it anyway. We introduce TRAPSBench, a procedurally generated video benchmark of 1,404 matched physics pairs in which a single targeted change renders the outcome undeterminable from the visual evidence. Furthermore, we introduce Penalized Epistemic Calibration Score (PECS), a new robust metric that requires models to both answer correctly when the outcome is knowable, and abstain when the outcome is not. Across 16 VLMs spanning five families, spontaneous restraint is poor: the best PECS is 0.292. The bottleneck is expression, not perception: linear probes decode answerability from hidden states at up to 0.91 AUROC across physics domains; steering a single-layer void direction causally induces or suppresses abstention. Our results replicate across three open-weight families (Qwen, Gemma, LLaVA). The failure is also more pronounced in visual than textual uncertainty: models detect textual impossibility about 4x more readily than missing visual evidence. Closing this representation--output gap likely requires output-stage interventions.

---


### 122. [Which LLM Is Your Ideal Companion? Evaluating Emotional Companion Capabilities of LLMs Based on Adult Attachment Theory](https://arxiv.org/abs/2608.13168)

**<font color=#1a73e8>作者：</font>** Junkai Zhou, Shiting Guan, Zhaoyi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly applied for emotional companionship, evaluating their behavior and capabilities in intimate relationships has become a pressing issue. However, existing assessments primarily characterize general personality traits, providing limited insight into model behavior within intimate and emotionally sensitive contexts. Therefore, we introduce adult attachment theory into LLM evaluation and use the Experiences in Close Relationships-Revised (ECR-R) scale to characterize attachment anxiety and avoidance. To evaluate emotional companionship capabilities of LLMs in realistic interaction scenarios, we present an emotional companionship benchmark, ECBench, spanning four scenarios including emotional support, collaborative tasks, conflict resolution, and social guidance, across friendship and romantic relationships. ECBench is utilized to assess model behavior using 11 dialogue-quality metrics and three evaluation methods. We evaluate the attachment tendencies of 32 LLMs and select representative models to investigate how these tendencies manifest in contextualized multi-turn interactions and whether they can be shaped through prompting. Our study provides a theoretical lens from psychology, along with practical tools to understand and select LLMs for emotional companionship.

---


### 123. [SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents](https://arxiv.org/abs/2608.13173)

**<font color=#1a73e8>作者：</font>** Chang Liu, Yuqi Zhang, Yiman Zhong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are crucial external instructions that enable language agents to execute long procedural tasks such as coding or document processing. Existing agent skills are primarily created through human manual crafting or agent execution traces, with limited understanding of how each step contributes to overall skill performance on specific tasks; i.e., there remains an open problem in quantifying the contribution of individual steps within an agent skill. To address this issue, we first model skill-step attribution as a Shapley value-based contribution estimation problem, and then propose SkillShapley, a step-level attribution framework for agent skills. Notably, SkillShapley operates in two phases, motivated by key empirical insights, i.e., discretized benchmark rewards that create sharp performance cliffs, and step interactions that are largely additive rather than synergistic. Specifically, it first identifies informative coalitional regions, and then adaptively samples new coalitions that can yield reusable marginal evidence. Experiments on skills from the widely adopted SkillsBench demonstrate that our SkillShapley can effectively and efficiently identify high- or low-value skill steps, providing several key takeaways for agent skill creation.

---


### 124. [Teach the Magnitude, Not the Direction: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents](https://arxiv.org/abs/2608.13179)

**<font color=#1a73e8>作者：</font>** Zechuan Wang, Siyuan Lu, Hongxuan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) offers a verifier-bounded performance ceiling for training multi-turn tool-use agents, yet its trajectory-level credit assignment conflates heterogeneous per-turn outcomes into a single reward signal. On-policy distillation provides dense per-token supervision but is either teacher-bounded or prone to gradient concentration collapse. We introduce $\textbf{CrEST}$, a hierarchical credit assignment framework that retains RL's verifier-bounded ceiling while incorporating dense token-level signals from a privileged self-teacher. $\textbf{CrEST}$ resolves credit at two levels: turn-segmented verified advantages address inter-turn dilution, while entropy-gated self-teacher modulation refines intra-turn token contributions. Experiments on BFCL V3 and WildToolBench show that $\textbf{CrEST}$ consistently outperforms both RL and distillation baselines across two model scales, with the largest gains on long-trajectory and strict session-level metrics. Our work demonstrates that the teacher's role in policy optimization can be reduced from determining update directions to modulating update magnitudes, unlocking dense credit assignment without sacrificing the verifier-bounded ceiling.

---


### 125. [GEM: A Generative Embedding Model Bridging Reasoning and Retrieval](https://arxiv.org/abs/2608.13200)

**<font color=#1a73e8>作者：</font>** Zhili Shen, Craig Macdonald  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern LLMs excel at reasoning and instruction following, enabling users to express complex and diverse information needs. However, conventional retrievers largely rely on surface-level matching between queries and documents, resulting in a growing gap between how users express their needs and how retrievers interpret them. In this paper, we present GEM, a generative embedding model that augments retrieval through its own knowledge by explicitly reasoning about user intent and relevance criteria. GEM unifies generation and embedding within a single model: it first reasons over the query, then appends an embedding token to encode the enriched context for retrieval. \zhili{Evaluated on reasoning-intensive and instruction-following retrieval tasks, GEM demonstrates the effectiveness of its reasoning-augmented retrieval, outperforming its non-reasoning variant and matching baselines using substantially larger models.} Furthermore, GEM's generative nature allows test-time compute scaling via prompting to further enhance retrieval performance. Our code is available at: this https URL.

---


### 126. [NARU: A Benchmark for NARrative Evolution and Cultural Nuance Understanding in Japanese Extreme Long Video](https://arxiv.org/abs/2608.13210)

**<font color=#1a73e8>作者：</font>** Yuheng Huang, Jianlang Chen, Jiayang Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form video understanding encompasses tasks that go beyond retrieving isolated events, including tracking an evolving narrative and interpreting social meaning that may remain implicit. However, existing benchmarks rarely evaluate these capabilities jointly, particularly in high-context, non-English media. To address this gap, we introduce NARU, a benchmark designed to evaluate Narrative evolution and Reasoning on cultural Understanding in Japanese long-form video. NARU consists of 1,481 questions grounded in 155 videos totaling 146.8 hours, spanning four narrative and five cultural dimensions. To construct the benchmark at this scale, we propose a hierarchical memory-based annotation pipeline that transforms raw video into structured event, narrative, and cultural annotations, then generates questions via task-oriented synthesis and iterative shortcut removal. The construction process includes two native-speaker verification stages involving 68 annotators. Evaluations across eight model configurations reveal substantial limitations in both long-range narrative integration and culturally grounded reasoning. By exposing these persistent gaps, NARU offers a systematic testing ground for developing MLLMs capable of reliably interpreting long-form, high-context video.

---


### 127. [CogChat: Knowledge Graph-Augmented Conversational AI with Heterogeneous Graph Transformer for Cognitive Grounding in Design Generation](https://arxiv.org/abs/2608.13216)

**<font color=#1a73e8>作者：</font>** Jiin Choi, Kyung Hoon Hyun  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-based chat systems have become valuable tools for design practice, enabling rapid ideation and flexible task support. Yet these systems process designer utterances as generic sequences, maintaining context through recency rather than through any model of how the speaker organizes knowledge. In design conversation, this gap compounds as relational context decays between turns, identical words go unresolved across designers, and the conversation loops or restarts rather than deepens. We present CogChat, a real-time chat framework that grounds conversational AI in a personal heterogeneous knowledge graph constructed from each designer's input. The system extracts typed entities and relations into a heterogeneous graph, then applies a HGT (Heterogeneous Graph Transformer) to select structurally relevant nodes for response generation and to generate both intentional and exploratory probing questions. Technical evaluation shows that HGT-based entity selection outperforms both ungrounded LLM interaction and naive KG augmentation, which introduces noise that degrades response quality. A within-subjects study with nine professional designers indicates that grounding conversation in a relationally structured, designer-specific semantic context improves context retention, personalized intent interpretation, and conversational depth while reducing cognitive load. These findings suggest that structuring a designer's expressed concepts and relations as a dynamic knowledge graph can preserve relational context that fades across turns, pointing toward a graph-grounded approach to long-term context management in LLM-based interaction.

---


### 128. [TsuGO: Probing Search Efficiency in LLM Reasoning via Go Life-and-Death Problems](https://arxiv.org/abs/2608.13221)

**<font color=#1a73e8>作者：</font>** Shunwen Bai, Ziping Ma, Chaoyang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The evaluation of LLM reasoning is moving from final-answer accuracy to process-level assessment, yet existing methods still fail to capture how models plan reasoning paths and allocate reasoning resources--that is, how they organize search. Prior process-level methods focus on the coherence and redundancy of chain-of-thought (CoT), and most benchmark tasks have a single objective solvable by static capabilities such as derivation and tool use, leaving search organization unmeasured. We introduce TsuGO, a process-level reasoning benchmark for evaluating Search Efficiency in LLM reasoning through Go life-and-death problems. These problems provide closed and verifiable solution spaces with an inherent adversarial structure, making candidate generation, response checking, branch comparison, and backtracking necessary parts of reasoning rather than incidental trace patterns. By constraining the solution space, TsuGO disentangles domain knowledge from search organization, parses CoT into a structured search tree, and reports Search Efficiency together with Token Efficiency and other diagnostic metrics and visualizations. Experiments show that current LLMs remain far from stable tsumego solving: stronger models succeed by finding the correct candidate earlier and sustaining effort on productive branches, but most models still behave much closer to unguided search algorithms than to neural-guided KataGo. Longer CoT or higher Token Efficiency does not necessarily imply better search. Our results identify search organization and reasoning-resource allocation as missing dimensions in LLM reasoning evaluation.

---


### 129. [CoverPrune: Coverage-Driven Token Pruning for 3D VLMs via Optimal Transport](https://arxiv.org/abs/2608.13226)

**<font color=#1a73e8>作者：</font>** Peng Ling, Yingda Yin, Lingting Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Vision-Language Models (3D VLMs) have demonstrated remarkable spatial reasoning capabilities, they suffer from massive visual token counts that create severe computational bottlenecks during inference. Existing token pruning methods primarily rely on diversity-based selection, discarding similar tokens to maximize dispersion. However, in 3D environments, this approach frequently drops representative prototype tokens in favor of outliers, breaking the multi-view consistencies and geometric structures essential for spatial reasoning. In this paper, we propose a paradigm shift for 3D VLM token pruning: from maximizing diversity to preserving visual evidence coverage. We introduce CoverPrune, a training-free framework that formulates inference-time token pruning as an Optimal Transport (OT) problem. To overcome the intractable combinatorial subset selection inherent in this formulation, we design the Feature-Spatial-Temporal (FST) transport cost and target capacity, along with an efficient Spatial-Guided Greedy Selection (SGS) algorithm to approximate the OT objective. Furthermore, we propose CoverPrune-Lite, an accelerated variant utilizing spatially structured local matching for minimal overhead. Extensive experiments across multiple 3D visual-spatial reasoning benchmarks demonstrate that our methods achieve state-of-the-art token efficiency, maintaining robust reasoning performance even under highly aggressive pruning budgets. Visit our project website at this https URL.

---


### 130. [Reasoning for Social Audio-Visual Question Answering: Where Do We Stand?](https://arxiv.org/abs/2608.13239)

**<font color=#1a73e8>作者：</font>** Koen P. de Vries, Xavier Alameda-Pineda, Estefanía Talavera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training Multimodal Large Language Models for audio-visual social understanding is a crucial step toward embodied social intelligence. Chain-of-thought (CoT) reasoning has become the dominant approach, with HumanOmniV2 and its IntentBench benchmark as a prominent reference point. In this context, we report three findings. First, IntentBench is highly noisy: $\sim$7% of questions are broken and $\sim$23% are trivially answerable without the video input. We remove the affected questions and release Intentbench-Prime. Second, current reasoning approaches are expensive and surprisingly ineffective. A simple Vanilla SFT baseline matches or outperforms existing reasoning methods across three benchmarks at a fraction of the cost, establishing it as an essential baseline for evaluating novel fine-tuning techniques. Third, our analysis reveals that substantial priors can be learned solely from the text modality and that using a textual caption instead of the video yields performance on par with Vanilla SFT. These surprising findings reveal the limitations of current MLLMs when it comes to social understanding. IntentBench-Prime, Vanilla SFT model, and code are publicly available.

---


### 131. [Localize, Then Reason: Visual Latent Structural Reasoning for Molecular Properties and Edits](https://arxiv.org/abs/2608.13244)

**<font color=#1a73e8>作者：</font>** Xingqiao Lin, Junmei Wang, Haocheng Tang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Local chemical perception and property reasoning are both essential for understanding how molecular structure determines properties. Current LLM-based chemical reasoning methods either receive SMILES/molecular images together with descriptions of local motifs, or reason directly from molecular images. Neither approach enables the model to focus on chemically meaningful regions before reasoning. To address this gap, we propose Visual Latent Structural Reasoning (VLSR), an end-to-end framework that jointly learns localization and reasoning from molecular images. Central to our approach is a localize-then-reason strategy. VLSR first learns to locate chemically meaningful regions in a molecular image. It then reasons about their property effects in a compact latent workspace before producing the final answer. Under the same inference setup, this design achieves 9.6X higher throughput than a comparable textual-reasoning baseline.

---


### 132. [Self-Referential Induction Increases Response Instability Relative to Unresolvable and Verifiable Questions in Large Language Models](https://arxiv.org/abs/2608.13258)

**<font color=#1a73e8>作者：</font>** Paras Balani, Subhrakanta Panda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-referential prompting has been shown to reliably induce large language models to produce first-person reports resembling subjective experience, but no prior work measures how consistent these reports are across repeated, independent trials, or how that consistency compares to the model's behavior on other kinds of open-ended questions. We measure response instability, defined as one minus the mean pairwise cosine similarity of sentence embeddings computed over a compressed core claim extracted from each response, for three groups of questions: self-referential prompts eliciting a subjective-experience report, unresolvable philosophical questions unrelated to self-reference, and questions with a verifiable correct answer. Using 30 independent responses per question (360 responses total, Gemini API, temperature 0.7) across four questions per group, we find that self-referential questions show the highest instability (0.343 +/- 0.047), unresolvable philosophy questions show intermediate and tightly clustered instability (0.192 +/- 0.008), and verifiable questions show the lowest instability (0.105 +/- 0.058). This provides a quantitative baseline for the induced subjective-experience report, showing that it occupies a distinct, less stable position in the model's output distribution than ordinary open-ended philosophical uncertainty.

---


### 133. [vToken: Token-Level Virtualization for Reclaimable KV Caches](https://arxiv.org/abs/2608.13263)

**<font color=#1a73e8>作者：</font>** Yuanhang Gao, Xiangrui Yang, Yuanfeng Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model serving faces a critical memory bottleneck: the KV cache grows with sequence length and batch size. PagedAttention uses fixed-size memory blocks to reduce allocator-level fragmentation, but recent KV eviction algorithms operate at a token granularity finer than block-level management. This mismatch causes intra-block fragmentation, leaving a large fraction of allocated KV memory unreclaimable. We present vToken, a lightweight token-level virtualization layer that decouples logical token liveness from physical block placement. vToken maintains a stable logical token view through token-table indirection and realizes physical reclamation by repacking live tokens asynchronously. The design preserves PagedAttention kernels and CUDA Graph compatibility. We implement vToken in vLLM and evaluate it with H2O, Random, and Scissorhands across models. Compared with a paired Naive-Evict baseline, vToken reduces retained KV blocks per request by 27.2\%--72.3\% and improves SLA-constrained throughput by up to 1.37$\times$. Under a constrained active-KV budget, it extends the maximum feasible concurrency by up to 2$\times$, while reducing the per-policy integration footprint from 500+ lines to under 50.

---


### 134. [How Do VLMs Behave When Blind or Misled? Behavioral Evaluation of VLMs on Scientific Figures](https://arxiv.org/abs/2608.13267)

**<font color=#1a73e8>作者：</font>** Paul Osemudiame Oamen, Owusu-Banahene Osei, Ananya Mukherjee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing vision-language model (VLM) benchmarks emphasize perception and reasoning accuracy (how well VLMs describe and reason about what they see in an image), with limited attention to behavioral reliability under uncertainty (how they behave when visual evidence is missing or misleading). We introduce SciFigBench, a diagnostic VLM benchmark for scientific figure understanding that jointly evaluates perception, reasoning, and behavioral reliability under uncertainty. It contains 250 figures with high-quality human annotations across three evaluation aspects, totaling 600+ hours of annotation effort. We further extend these figures via image transformations, reasoning questions, resistance probes, caption-bias probes, and confirmed selective-blur targets, producing over 34,000 evaluation setups for stress testing.
We further propose the Admittance-Resistance-Inductance (A-R-I) framework to evaluate whether models acknowledge insufficient evidence, resist misleading context, and infer cautiously from partial information. Our results reveal substantial behavioral differences among models. GPT-5.2 achieves the highest description quality (MQM 91.6) with strong reasoning accuracy (78.4%), yet hallucinates unreadable content in 96% of cases, whereas Gemini 3.1 Pro, a comparably capable model (MQM 90.2, reasoning 81.0%), admits uncertainty in 71% of such cases and achieves the strongest resistance score (0.91). These findings show that high perception and reasoning accuracy alone do not guarantee behavioral reliability, a dimension critical for deployment in scientific workflows.

---


### 135. [Mixture of Training: Recombining Small-Scale Scaffolded Pretraining Runs into a Larger Language Model](https://arxiv.org/abs/2608.13277)

**<font color=#1a73e8>作者：</font>** Mohammed Sabry, Sean Augenstein, Keith Rush 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We ask whether language-model pre-training can be decomposed into smaller, independently trainable jobs that can later be recomposed into a coherent larger model. We introduce Mixture of Training (MoT), a scaffolded modular pre-training procedure that partitions a target Transformer into contiguous layer blocks, trains each block inside a frozen pretrained aligner scaffold, and then recomposes the trained blocks with an optional short end-to-end adaptation pass. On a 1.3B-parameter Gemma-style model trained on C4, MoT provides a small-scale proof of mechanism: independently trained depth slices can be recomposed into a usable language model, and a quality-parity schedule reaches the same reported perplexity as the monolithic baseline. This parity setting processes more aggregate tokens and has a shorter idealized layer-equivalent critical path after aligner preparation; its effective compute advantage depends on reusing the aligner across runs. We therefore present MoT not as a general replacement for monolithic pre-training, but as a small-scale framework for studying whether scaffolded sub-runs can act as reusable training units.

---


### 136. [How Good are Foundation Models in Longitudinal MRI Disease Progression Reasoning?](https://arxiv.org/abs/2608.13309)

**<font color=#1a73e8>作者：</font>** Wafa Al Ghallabi, Ritesh Thawkar, Sara Ghaboura 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic Resonance Imaging (MRI) interpretation is fundamental to clinical decision-making, requiring radiologists to integrate multi-view anatomical planes across sequential timepoints while precisely localizing interval changes. However, existing vision-language benchmarks remain confined to single-timepoint, single-view interpretation, failing to capture the temporal-spatial reasoning essential to radiologic practice. We introduce the Time-Aware Multi-View MRI Benchmark, an evaluation framework unifying multi-view anatomical input, temporal reasoning across longitudinal scans, and structured localization guidance. The benchmark comprises 3,920 expert-verified question-answer pairs derived from 890 patients across over 3,200 longitudinal MRI timepoints, drawn from seven clinical cohorts covering glioblastoma, neurodegeneration, vestibular schwannoma, and brain metastases, in open-ended, multiple-choice, and binary formats, requiring models to identify anatomical regions of maximal change, characterize progression across sequences and views, and provide structured guidance specifying boundaries, imaging features, and confounders. Experiments across 16 vision-language models reveal moderate temporal alignment but systematic failure on change direction recognition and volumetric quantification, while multi-view inputs improve spatial localization yet degrade temporal reasoning in compact architectures. Our benchmark provides a systematic framework for evaluating progression tracking, interval change localization, and temporal ordering, which are essential for clinical deployment. Code, evaluation splits, and the dataset are available at: this https URL.

---


### 137. [StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems](https://arxiv.org/abs/2608.13317)

**<font color=#1a73e8>作者：</font>** Yanwen Peng, Delvin Ce Zhang, Xi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck. Converting the sender's continuous hidden states into discrete tokens discards information that token identities alone cannot capture. Recent work proposes latent communication as an alternative, where agents transmit hidden representations directly without converting them to text. However, existing latent methods either inject working memory layer by layer across the transformers, or require trained projectors that limit portability. We propose StateBridge, a training-free latent communication approach that aligns the sender's final-layer hidden states to the receiver's input space via a closed-form orthogonal transformation. Lightweight norm calibration and vocabulary anchoring ensure compatibility with the pretrained input distribution. The aligned states are prepended to the input of the receiver agent as a continuous prefix. We evaluate StateBridge on math reasoning, code generation, and question answering with four models from two families. StateBridge achieves the best or tied-best score on 22 out of 26 model-task pairs, consistently outperforming the strongest baseline.

---


### 138. [Beyond Local Accuracy: A Protocol-Level Identifiability Audit for Controlled LLM Reasoning Evaluation](https://arxiv.org/abs/2608.13326)

**<font color=#1a73e8>作者：</font>** Junhao Luo, Ning Huang, Ziqi Sha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM benchmark scores can be precise even when the observation protocol does not identify the behavioral property they are intended to measure. In a controlled, solver-grounded setting, we formalize a protocol-level identifiability audit over a finite behavioral policy class: given policies H, observation support O, and estimand $\tau$, we test whether O separates every pair with different $\tau$. The audit requires zero model calls and resolves our diagnostic case: base-only observation collapses seven frozen deterministic policies into one equivalence class; full support yields seven classes and no cross-estimand collisions; every leave-one-out support retains a constructive collision witness. Empirically, both constrained-generation variants have pair-validity 1.0, yet base accuracy and selective-response fidelity diverge - 0.620 versus 0.324 across six balanced oracle-transition directions (cluster-bootstrap 95% CI [0.600, 0.642] vs. [0.304, 0.345]) - and the gap recurs on a second deterministic source (0.646 vs. 0.331). The audit also synthesizes a minimum identifying support $O^*$ for the frozen policy class: two cells instead of the full 36-cell tensor. This case shows how evaluation-design validity can be checked structurally before model inference and why base correctness does not determine intervention-response fidelity.

---


### 139. [It's How You Ask: Gender-Associated Linguistic Bias in LLMs](https://arxiv.org/abs/2608.13328)

**<font color=#1a73e8>作者：</font>** Katherine Van Koevering, Anjalie Field  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Professional communication is increasingly mediated by LLMs - but do these models serve all users equally? We show that when prompts contain linguistic features more commonly used by women (hedges, tag questions, collective reference), they systematically elicit shorter, less sophisticated, and less formal responses across three document types and four models. These effects persist after controlling for prompt complexity and feature carry-over. Explicit gender cues like sign-off names are encoded in the same representational space as linguistic dialect - suggesting shared underlying mechanisms - yet linguistic register is far more influential, producing large, consistent effects where names produce none. Our results further reveal that post-hoc mitigation is challenging: because these patterns are culturally embedded and outside conscious control, users cannot easily avoid them through strategic self-presentation, and mechanistic analysis reveals that linguistic features are encoded in early transformer layers and entangled with other features. Our work calls for upstream consideration of the influences of linguistic variation to mitigate disparate impacts of LLM-mediated workplace communication.

---


### 140. [Training AI Scientists to Replicate Research](https://arxiv.org/abs/2608.13331)

**<font color=#1a73e8>作者：</font>** Damon Falck, Samer Sabri, Anja Surina 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The replicability of papers is a cornerstone of scientific knowledge, ensuring the reliability of existing results and providing a base for further experiments. The act of replication typically illuminates details that were previously underspecified, and thus requires similar hypothesis-driven exploration to open-ended research. In this work, we develop Replica, a scalable task space for paper replication. To provide reward signal, we introduce an auto-generated rubric-based judge that has low noise and agrees with human assessment of replication quality. We post-train Faraday, a 27B-parameter "AI Scientist" agent that leverages coding agents as tools, surpassing the performance of Claude Opus 4.8 and GPT-5.5 on held-out replication tasks. Qualitative analysis of individual rollouts reveals that Faraday adopts a more scientifically-principled approach. We believe that our results provide a stepping stone towards AI agents capable of long-horizon scientific innovation without requiring complex harnesses.

---


### 141. [LLM-Guided Graph Generation for Structure-Based Local Improvement Methods](https://arxiv.org/abs/2608.13333)

**<font color=#1a73e8>作者：</font>** Hai Xia, Vaidyanathan Peruvemba Ramaswamy, Stefan Szeider  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large neighborhood search normally selects a random subset of decision variables for iterative optimization. For efficiently solving different problems, researchers tend to design variable selection strategies by taking into account structural features from different domains. In this paper, we build an automatic pipeline that is problem-agnostic to all problems in the MiniZinc format. By prompting an LLM with our semantic guidelines, we guide the LLM to produce a graph generator that maps any instance of a problem type to a uniform weighted graph, where nodes represent decision variables and edges represent constraint relationships. These problem-agnostic graphs guide our structure-based local improvement framework (SLIM) in variable selection. Meanwhile, the weighted graph enables all problem instances to share the same generic graph representation, from which the same graph features can be extracted and used for configuration selection. We evaluated our pipeline on instances across 20 MiniZinc competition problems, finding that algorithm selection achieves a 39.5% average problem-weighted win rate against a one-shot Gurobi baseline, more than doubling the best single configuration (19.3%). Configuration and feature ablation boost the performance further to 44.0%, demonstrating that LLM-based semantic generation enables effective automated structure extraction and feature extraction for constraint optimization.

---


### 142. [RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory](https://arxiv.org/abs/2608.13334)

**<font color=#1a73e8>作者：</font>** Jingbo Ji, Lingyi Li, Xilong Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agents increasingly rely on external memory to support long-horizon reasoning and interaction. However, the main bottleneck is not simply storing past experience, but recovering the right set of evidence when relevant information is distributed across many interactions. Existing approaches struggle with this access problem. Full-context methods require noisy long-context search, flat retrieval often returns isolated and incomplete records, and graph-based memory systems can be expensive to construct while compressing rich event context. We introduce RippleMem, a long-term memory system that replaces one-shot retrieval with adaptive associative recollection. Inspired by cue-dependent episodic retrieval and associative completion, RippleMem stores interaction history as cue-rich episodic memory units and organizes them in an event-centric memory graph. Given a query, it first recalls relevant memory anchors through hybrid cues, then expands from these anchors along semantic and structural associations to recover missing supporting evidence. In this way, initially recalled memories serve not only as answer context, but also as cues for completing the evidence needed to answer. Experiments on LoCoMo and LongMemEval-S show that RippleMem achieves the best overall performance across evaluated settings, improving LLM-as-a-Judge accuracy by 3.95% on LoCoMo and up to 11.87% on LongMemEval-S, while reducing graph construction cost by about 30x.

---


### 143. [Where You Measure Decides What You Measure: Position Selection in Ablation-Based SAE Evaluation](https://arxiv.org/abs/2608.13337)

**<font color=#1a73e8>作者：</font>** Valentin Noël  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders are meant to name the things a language model computes, and the usual way to check that a latent matters is to switch it off and see what changes. But a latent fires at many tokens, and the effect has to be measured at one of them. The convention is to measure where the latent fires hardest. That choice is almost never reported, and it is not made by the experimenter: it is made by the dictionary under evaluation. Change the dictionary and the measurement moves to a different token. We show this is not a detail. Take two sparse autoencoders released by Google for the same model and match their latents by decoder similarity: even among the pairs the two dictionaries encode almost identically, they pick different tokens for a large share of them. Two dictionaries compared under the usual protocol are therefore very often compared at different places. To separate the convention from the dictionaries we train six autoencoders from one initialisation, differing only in fitting choices, so that a latent means the same thing in each. Most of the variance such a comparison reads as "these dictionaries disagree about this latent" turns out to be the position instead: it falls from 7.6% and 11.9% of variance to near zero once every dictionary is measured at the same token. More evaluation data does not rescue it. Across a sixteenfold range of corpus sizes the dictionaries agree less about where to measure, not more, so the problem grows with scale. The correction is one line of evaluation code. We give the protocol an ablation-based causal number must report to be comparable across papers, and an audit of five published papers against it. In short: a causal number reported without its position describes the token it was taken at as much as the latent it was taken from.

---


### 144. [AmalthAI: An Open-Source Computer Vision Platform for Cultural Heritage](https://arxiv.org/abs/2608.13343)

**<font color=#1a73e8>作者：</font>** Christos Chatzisavvas, Stelios Alvanos, Efstratios Politis 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer vision (CV) and machine learning (ML) offer new tools for cultural heritage (CH) artifact analysis, but the CV/ML pipeline remains largely inaccessible to CH domain experts, who lack the background to configure, train, or assess models. We present AmalthAI, an open-source CV platform that bridges this gap, enabling non-ML CH experts to independently produce and validate archaeologically meaningful findings. The interface covers dataset management, training, and inference for classification, segmentation, and object detection, with Kubeflow and Katib handling scalable training and hyperparameter search. Grad-CAM localizes the image region behind a prediction, and a vision-language model (VLM) adds a text description of it for expert review. Since archaeological data is often state-owned or rights-encumbered and cannot leave institutional custody, AmalthAI's self-hostable deployment ensures sensitive data is kept within premises. We test the platform on an archaeological use case built on a custom dataset of clay textile imprints, where CH experts trained and validated segmentation, and classification models for hypothesis testing. We provide the implementation code at this https URL.

---


### 145. [LongEarth-R1: Benchmarking and Aligning Vision-Language Models for Long-Horizon Earth Observation Reasoning](https://arxiv.org/abs/2608.13344)

**<font color=#1a73e8>作者：</font>** Yupan Ding, Jing Xiao, Zhenyuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon Earth observation reasoning requires models to organize multi-stage geographic evolution, localize spatial changes, detect temporal anomalies, and infer future from extended image sequences. However, existing remote sensing vision-language models mainly focus on isolated images, image pairs, or short sequences, limiting reliable grounding in the relevant frames and regions. We introduce LongEarth-Bench, a benchmark containing approximately 120k question-answering samples derived from 117k unique images. Its sequences average 15.14 frames and extend to 30 frames, covering 12 tasks across evolution summarization, spatial reasoning, anomaly identification, and logical prediction. A 30k-sample subset further provides structured reasoning traces linking key frames and changed regions to final answers. We develop LongEarth through supervised fine-tuning with explicit sequence identifiers and structured chain-of-thought supervision. Building on LongEarth, LongEarth-R1 applies group relative policy optimization with format, temporal, and spatial rewards. LongEarth-R1 achieves the best results on all 12 long-sequence tasks while remaining competitive on standard remote sensing benchmarks.

---


### 146. [CROP: Task Relevance via Counterfactuals for Selective On-Policy Distillation](https://arxiv.org/abs/2608.13387)

**<font color=#1a73e8>作者：</font>** Enhan Li, Junhao He, Hongyang Du  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) supervises a student language model on trajectories sampled from its current policy, but assigns equal credit to response tokens with unequal supervision value. Selective OPD addresses this limitation by allocating supervision non-uniformly across response tokens according to their estimated training value. Most existing criteria, however, focus primarily on optimization need, such as uncertainty or teacher-student disagreement, while task relevance, namely whether the supervision is tied to the semantic content of the current input, remains less directly characterized as a complementary dimension. To address this gap, we introduce Counterfactual Relevance for On-Policy Distillation (CROP), which operationalizes task relevance through a paraphrase-calibrated counterfactual sensitivity margin. For each source prompt, CROP constructs a validated original-paraphrase-counterfactual triplet, holds the student rollout fixed, and measures each response position by its sensitivity to a task-relevant condition change calibrated by its sensitivity to a meaning-preserving rewrite. Matched selection controls show that CROP identifies more useful supervision positions than random or lowest-relevance selection, while component comparisons confirm the value of both counterfactual sensitivity and paraphrase calibration. Across two teacher-student settings, CROP improves aggregate performance by 1.92 and 2.96 points over the strongest non-CROP selector. These results support task relevance as a complementary criterion for selective OPD and establish CROP as a model-internal, contrast-specific method for allocating token-level supervision.

---


### 147. [Who Speaks Matters: Authority-Aware Multi-View RAG over Italian Parliamentary Proceedings](https://arxiv.org/abs/2608.13410)

**<font color=#1a73e8>作者：</font>** Mirko Tritella, Riccardo Pozzi, Matteo Palmonari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parliamentary proceedings are a primary record of democratic deliberation, yet their volume and fragmentation make multi-perspective access difficult for citizens, journalists, and researchers. Applying Retrieval-Augmented Generation (RAG) to parliamentary transcripts introduces three specific risks: dominance of the most frequent speakers, inability to weight speakers according to topical expertise, and citation misattribution in politically sensitive text. We present ParliamentRAG, a RAG system for the Italian Chamber of Deputies that addresses these risks jointly. Its core contribution is a topic-dependent authority model that estimates each speaker's authority as a function of the current query, combining interpretable components such as profession, education, and previous interventions. Given a user query, the system retrieves relevant speech chunks, identifies topic-relevant experts across parliamentary groups, and generates a summary synthesizing their perspectives, accompanied by supporting quotations. ParliamentRAG is evaluated against Google NotebookLM on 15 policy topics via a two-level protocol combining automated metrics and blind A/B human evaluation by six domain experts. The system achieves higher coverage across political groups (0.97 vs. 0.95), perfect quotation faithfulness (1.00 vs. 0.95), and stronger expert preferences on source-related dimensions, while NotebookLM remains stronger on prose-oriented dimensions.

---


### 148. [StreamTTT: Reconciling Real-Time Perception and Long-Term Memory in Streaming VLMs](https://arxiv.org/abs/2608.13416)

**<font color=#1a73e8>作者：</font>** Joya Chen, Zeyun Zhong, Mike Zheng Shou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans effortlessly perceive the present while remembering the past, yet streaming VLMs often trade off real-time perception against long-term memory. Prior work shows that shortening the context can sharpen current-scene perception at the expense of long-range recall. To reconcile these abilities, we introduce StreamTTT, which writes long-range history into online-updated fast weights outside the attention context. This leaves a short sliding key-value cache dedicated to recent evidence, mitigating attention dilution. We train StreamTTT jointly on offline long-video QA and a newly constructed real-time QA corpus. On OVO-Bench, StreamTTT-4B outperforms SimpleStream-4B by 1.4 points in real-time perception and 3.7 points in backward tracing. It also remains competitive with the larger SimpleStream-8B on the Real-Time Visual Understanding (RTVU) subset of StreamingBench. Our code will be released.

---


### 149. [Enhancing Virtual Agents through SLMs and Edge-Computing: An Exploratory Evaluation of Think and Memory Processes](https://arxiv.org/abs/2608.13420)

**<font color=#1a73e8>作者：</font>** Aimilios Hadjiliasi, Louis Nisiotis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied intelligent virtual agents are expected to operate as persistent, adaptive, and context-aware entities within complex virtual and Metaverse worlds. However, implementing cognitively capable agents in such environments is conceptually and technologically challenging. Among a range of blueprints and development approaches, the Cognitive Embodied Agent Architecture (CEAA) has been developed as an implementation-oriented framework for architecting components of perception, memory, reasoning, planning, and embodied action. Considering the recent advances in edge computing and generative AI language models, this paper explores the use of Small Language Models (SLMs) to support edge-based operation of selected CEAA components, focusing on "Think" and "Memory" as processes central to cognitive orchestration and persistence of virtual agents in interactive virtual worlds. An edge-based virtual agent gateway system was developed and evaluated on an NVIDIA Jetson Orin NX using Qwen2.5 models of different sizes, exploring the system's capability to process service requests and handle memory-driven conversations. A series of simulation experiments evaluated routing accuracy, memory-read performance, and latency, demonstrating an SLM-driven prototype agent system that partially implements selected CEAA processes to support the development of embodied agents whose cognitive "brain" can operate efficiently and contextually for interactive experiences in immersive virtual worlds.

---


### 150. [Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for LLM Inference](https://arxiv.org/abs/2608.13426)

**<font color=#1a73e8>作者：</font>** Zixuan Lan, Yanhong Li, Jiawei Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models achieve strong performance but incur substantial inference cost due to repeated high-dimensional matrix multiplications. We propose Reduced Matrix Multiplication (RMM), a training-free, input-adaptive inference method that reduces Transformer matrix products by selecting informative slices along their contraction dimensions, without modifying model weights. Under a simple retention-ratio control, RMM provides a smooth and predictable accuracy-efficiency trade-off. Across language models ranging from 1B to 70B parameters, we find that reduction tolerance depends on the model family, task, component, and retention ratio, although it often improves with model scale. Under moderate reduction, RMM remains robust across the evaluated discriminative, autoregressive generation, and long-context settings. We further show that the same principle extends to multimodal vision-language inference. Mechanistic ablations reveal a structural asymmetry within Transformers: attention-side computations are substantially more reducible than MLP components. Finally, wall-clock benchmarks with custom kernels on an NVIDIA A100 show that these computational savings can translate into practical runtime gains, especially at longer sequence lengths. Together, these results position RMM as a scalable direction for input-adaptive inference-time optimization.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-183](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
