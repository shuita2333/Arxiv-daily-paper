# 🧠 大模型相关研究 | 2026年09月10日

> 本类共 **483** 篇论文：已确认 **447** 篇，待复核 **36** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

---

### 251. [Beyond Single-Negative Preference: Multi-Negative DPO for LLM-Centric Historical Entity Linking](https://arxiv.org/abs/2609.07379)

**<font color=#1a73e8>作者：</font>** Tien Nam Nguyen, Emanuela Boros, Ahmed Hamdi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently shown promise for historical entity linking, but preference optimization for this task is often formulated with only one negative candidate per training instance. This discards information from the remaining candidates retrieved for the same mention. We introduce multi-negative direct preference optimisation (MDPO), a reference-based pairwise objective that compares the correct entity with all valid rejected candidates associated with each mention. MDPO preserves the Bradley-Terry formulation of DPO while exploiting the complete candidate set through masked, length-normalised sequence scores. We evaluate MDPO on hipe-2020 and newseye, covering French, German, English, Swedish, and Finnish historical newspaper text. Experiments show that MDPO improves over supervised fine-tuning and single-negative DPO, with particularly strong gains for NIL mentions, semantic ambiguity, OCR noise, and historically difficult names. Further analyses disentangle candidate-generation and selection errors, showing that candidate retrieval remains a key bottleneck for end-to-end entity linking. These results demonstrate that incorporating all within-instance negative candidates is a simple and effective improvement for LLM-based historical entity linking.

---


### 252. [Social Intuition vs. Machine Reasoning: Anticipating Human-Robot Interaction from multiple modalities](https://arxiv.org/abs/2609.07394)

**<font color=#1a73e8>作者：</font>** Raphael Lorenzo-Louis, Bertrand Luvison, Serena Ivaldi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anticipating whether a person will interact from one's own perspective is a highly intuitive task for humans, that relies on a combination of cues. We investigate how humans perform at predicting a person's intention to interact from a service robot's point of view, using pose-only or full video input, then benchmark different lightweight pose-based models and state-of-the-art vision-language models. We conducted our benchmark on the HUI360 dataset on a fixed pilot subset of 100 test tracks (25 positive, 75 negative). We found that with pose-only input, human annotators outperform lightweight trained pose models but not by large margins (+0.08 in F1-Score). But when given full egocentric video with a target bounding box, human annotators perform substantially better and largely outperform the Vision-Language Models (+0.2 in F1-Score). We also compared VLMs of different size and under different input conditions, and found that the best results do not correlate with model size. Our result confirms that predicting interactions is a challenging task for social robots and that reasoning-capable models are necessary but their actual reasoning capabilities alone do not suffice to match the social intuition of humans.

---


### 253. [Federated Binary Gating with Server-Side Vision-Language Inference for Surveillance Anomaly Classification](https://arxiv.org/abs/2609.07403)

**<font color=#1a73e8>作者：</font>** Côme-Alexis Puech, Sébastien Thuau, Amira Gran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Privacy-sensitive surveillance systems could benefit from large vision-language models (VLMs), but such models typically require centralized access to raw video. In federated learning settings, this challenge is amplified by non-independent and identically distributed (non-IID) client data, which can make direct multiclass anomaly classification unstable, especially for rare categories. We propose a hybrid two-stage architecture that combines a federated binary convolutional neural network (CNN) gate with server-side zero-shot VLM inference. The lightweight LiteCNN3D gate performs local anomaly screening and forwards only flagged videos to Qwen3-VL-8B, which assigns them to four anomaly metaclasses. We evaluate this design on UCF-Crime grouped into five coarse metaclasses and implement the federated stage in a real three-node heterogeneous deployment.
In the studied setting, direct federated multiclass training collapses, whereas the proposed decomposition yields a better trade-off between classification quality and raw-video transmission. With fixed-threshold routing, the federated hybrid pipeline preserves nearly the same macro-averaged F1 score (F1-macro) as its centralized CNN+VLM counterpart while reducing the fraction of transmitted videos to 51.4%, although with a lower proxy macro receiver operating characteristic area under the curve (ROC AUC) than the centralized hybrid system. A complementary sensitivity-oriented routing operating point increases macro ROC AUC from 0.673 to 0.692 and reduces the false negative rate from 29.3% to 22.9%, but decreases F1-macro from 0.503 to 0.485 while increasing transmission from 51.4% to 57.9%. These results suggest that federation is better suited to coarse local screening, while routing rules can be adjusted to trade server-side VLM usage for higher anomaly sensitivity.

---


### 254. [Think Wider: Mitigating Latent Rank Collapse in Implicit Chain-of-Thought Reasoning](https://arxiv.org/abs/2609.07406)

**<font color=#1a73e8>作者：</font>** Yuwen Hao, Menglin Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning improves the reasoning ability of large language models by introducing intermediate computation, but explicit rationales increase decoding length, latency, and context cost. Implicit CoT offers a more efficient alternative by moving intermediate reasoning into continuous latent states. However, latent reasoning can be unstable: successive latent states may become overly similar and collapse toward a shared dominant direction, reducing the diversity of the reasoning trajectory. In this work, we identify $\textit{latent rank collapse}$ and propose $\textbf{WIDER}$, a lightweight spectral regularizer for implicit CoT. During training, WIDER estimates the shared direction of each latent trajectory and penalizes projections onto this direction, encouraging latent states to span a broader representational subspace. The method is plug-and-play and leaves the backbone model, latent schedule, and inference-time decoding procedure unchanged. We further formulate this collapse as a geometric bottleneck in implicit reasoning, casting its mitigation as a training-time regularization problem rather than an inference-time decoding change. Extensive experiments show that WIDER improves matched implicit CoT baselines, while mechanistic analyses reveal higher effective rank, lower dominant-direction energy, and reduced redundancy among latent steps. These results highlight latent subspace utilization as an important factor for efficient continuous reasoning, providing a geometric perspective for analyzing and improving implicit CoT. Code is available at this https URL.

---


### 255. [Unified Vision-Centric Pedestrian Crossing Action Prediction via Adaptive Patch Projection and Proactive Spatial Rectification](https://arxiv.org/abs/2609.07420)

**<font color=#1a73e8>作者：</font>** Yao Tian, Le Yang, Binglu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision cues are available and informative for pedestrian action prediction, but obtaining stable target-centric representations from video frames remains challenging without frame-level external perception cues. Thus, most methods rely on additional perception modules or multi-source information fusion, leaving the reliability of vision-centric setting an open question. To this end, we propose ViCross, a vision-centric pedestrian crossing action prediction framework powered by multimodal large language models, which maintains target-centric reasoning from video frames without additional perception modules beyond first-frame target initialization. While multimodal large language models exhibit strong visual understanding, applying them directly to vision-centric action prediction faces two challenges. First, accurately perceiving target pedestrians often requires high resolution inputs and dense visual tokenization, making full-frame encoding computationally prohibitive. ViCross tackles this with Variable Resolution Patch Mapping module for efficient token allocation while preserving key pedestrian details. Second, missing spatiotemporal priors hinder consistent cross frame reasoning. ViCross mitigates this with a Spatial Constraint Enhancement Strategy that captures past motion, future locations, and action semantics for training-time proactive spatial rectification. Extensive experiments show that ViCross delivers clear gains in vision-centric prediction settings and is competitive with multi-source fusion approaches in several settings. Code is available at this https URL.

---


### 256. [CIT-CAD: Constraint Intent Tree-based CAD Code Generation and Verification](https://arxiv.org/abs/2609.07434)

**<font color=#1a73e8>作者：</font>** Yali Du, Hui Sun, San-Zhuo Xi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language Computer-Aided Design (CAD) code generation aims to turn design intent into executable and editable parametric programs. Large language models (LLMs) make this goal increasingly practical, but useful systems must preserve the construction process behind the rendered geometry. Existing benchmarks and methods mostly focus on how closely the generated CAD model matches the reference geometry, often using metrics such as Intersection over Union (IoU). Such metrics can miss errors in part decomposition, construction hierarchy, Boolean operations, sketch structure, and geometric relations. This gap calls for a representation that makes design intent explicit and lets a system check generated code against that intent. We propose CIT-CAD, a framework that infers a Constraint Intent Tree (CIT) from the input description to represent the intended entities, hierarchy, operations, and relations. The tree has two roles: it guides CAD code generation and defines expected constraints for verification. The framework extracts actual constraints from the generated program, compares them with the expected constraints, and uses mismatches to localize and repair design violations. Experiments show that the framework improves CAD generation performance, with larger gains on more complex multi-entity designs. By turning design intent into an explicit and checkable object, this work is the first attempt to move text-to-CAD generation beyond rendered-geometry matching toward construction-aware synthesis, verification, and repair.

---


### 257. [An LLM-Associated Register Shift in Korean Journal Abstracts: A Morphology-Aware Excess-Vocabulary Study, 2018-2026](https://arxiv.org/abs/2609.07447)

**<font color=#1a73e8>作者：</font>** Aron Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Excess vocabulary, a word's frequency above its pre-2023 trend, is how the change in scholarly English after 2022 has been measured. We adapt it to Korean with morphological units on 398,296 KCI abstracts (2018-August 2026), with 47,165 Vietnamese abstracts for comparison. Placebo floors are 0.1-2.2 points for the single-word statistic and at most 2.9 for the re-selected split-half set statistic. Korean abstracts show nothing in 2023, onset in late 2024, a rise through 2025 flattening in mid-2026: sisahada "suggest" appears in 21.4% of 2026 abstracts against 5.3% expected; plain verbs like araboda "look into" fall to a quarter of trend. Under stated assumptions the single-word conditional lower bound on LLM-processed abstracts is 3.5%, 10.5% and 16.1% for 2024-2026 and a split-half set bound 7.8%, 20.6% and 33.0%. Holzwarth et al.'s estimator under the same discipline gives 41.9% and 72.1% for 2025-2026. Subject-matter controls reduce but do not remove it: restricting the set to lemmas three language-model annotators all call style leaves 14.7 of the 33.0 points, and pairing each 2026 abstract with its journal's closest base-period abstract leaves 34.1. Tested translation routes do not explain it: the surface marks of translated Korean fall as the markers rise. In the same articles' English abstracts the excess appears a year earlier; where the English side carries none, the Korean shift persists at 30 to 66% of the rate where it does. Control abstracts from three providers reproduce the rising words, with marker turnover consistent with model generations; implied prevalences are scenario-dependent.

---


### 258. [FramingQA: Does the Question Shape the Answer? Measuring the Compositional Framing Effect](https://arxiv.org/abs/2609.07448)

**<font color=#1a73e8>作者：</font>** Hazel H. Kim, Andrew M. Bean, Guilherme Affonso Ferreira de Camargo 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce FramingQA, a benchmark that measures the model sensitivity to question framing across law, medicine, finance, and robotic simulations. Large language models (LLMs) often change their responses to subtle rephrasings that align with an implied stance by users. This can leave users with advice tainted by how they happened to phrase a question rather than by the underlying facts, and the consequences are highly costly in high-stakes domains. Because in the realistic scenarios, both expert practitioners and non-expert users frequently ask LLMs questions containing incomplete or misleading assumptions, models are highly susceptible to those framings. To test this, we inject the framing bias across three nested levels: a framing-biased question phrasing (root), an injected framing-biased premise prepended to a neutral question (propositional), and a premise paired with a framing-biased question (global). Evaluating nine open models (3.8B-70B) across four families, we find that strong per-variant accuracy does not guarantee the robustness across differently phrased questions under the fixed factual information.

---


### 259. [Parser-Free VLM Verification for Federated Weakly Supervised Video Anomaly Detection](https://arxiv.org/abs/2609.07455)

**<font color=#1a73e8>作者：</font>** Sébastien Thuau, Amira Gran, Siba Haidar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How can vision-language models help video anomaly detection (VAD) when surveillance data remain distributed, weakly labeled, and resource-constrained? Most weakly supervised VAD methods assume centralized training; recent VLM-based extensions further rely on dense inference, generated explanations, or additional adaptation. We introduce a lightweight federated MIL-VLM cascade in which only a compact MIL scorer is trained across clients, while a frozen VLM verifies high-scoring suspect segments post hoc. We study two VLM feedback interfaces: parsed text-generation decisions and a logit-based interface that extracts a continuous anomaly score from next-token Yes/No probabilities. Experiments on UCF-Crime with InternVL3.5-2B and Qwen3-VL-2B-Instruct show that text-generation verification can improve frame-level AUC after diagnostic temporal post-processing, but remains sensitive to prompts, parsers, model choice, and smoothing. In contrast, the logit interface provides a fixed parser-free signal that improves both frame-level AUC and frame-level AP over the MIL baseline across both VLMs, without temporal post-processing in its main configuration. Since suspect segments are updated independently once available, next-token logit feedback provides a simple segment-local alternative to text-generation verification.

---


### 260. [MEMO: Multimodal Evidence Memory Organization for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.07471)

**<font color=#1a73e8>作者：</font>** Xian Gao, Jinpeng Wang, Jiacheng Ruan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-running LLM agents rely on external memory to store and reuse information beyond a single context window, yet there is a fundamental tension between the continuous accumulation of interaction trajectories and the limited context capacity. The key challenge in agent memory is therefore not only to retrieve relevant records, but also to select necessary evidence under a given budget and organize it in an appropriate modality. Existing memory readout methods mainly use textual or visual forms. Text preserves high fidelity, but its linear token representation makes contents with different importance compete for the limited context at nearly uniform unit cost. Visual readout renders text into document-like images, which can use two-dimensional layouts to expose structure and emphasize key information, but it may lose fine-grained details during rendering and compression. To address this issue, we propose MEMO, a multimodal evidence memory organization method for LLM agents. MEMO first uses a trained evidence extractor to select relevant memory blocks and form evidence units with source information and presentation requirements. A trained query-conditioned memory manager assigns each unit to a textual, visual, or dual-channel carrier and selects a layout that matches the evidence structure. A deterministic memory construction module then generates the textual package and visual pages. The memory manager is trained with feedback from an offline reader that measures the utility of the guided memory plan, so that retention and presentation decisions align with downstream usage. We evaluate MEMO on four benchmarks, HotpotQA, 2WikiMultiHopQA, LoCoMo, and ALFWorld, with multiple reader backends. The results show that MEMO presents memory more efficiently with fewer memory tokens, improves downstream task performance, and builds more effective working memory under constrained budgets.

---


### 261. [Where Should Language Sit in a Multimodal Model? Lessons from What Language Does to Human Perception and Cognition](https://arxiv.org/abs/2609.07474)

**<font color=#1a73e8>作者：</font>** Peng Xie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models compute over tokens: language is their input, their output, and increasingly their internal representation. Whether language should keep all of these positions depends on what language does to the system that uses it. The one system with a century of data on that question is the human. We review what language does to human perception, the brain, and thought, and read the same evidence against multimodal models and language models. Throughout, we treat language as a compressor that runs on a shared codebook: a word is an index, the content is in the receiver, and a community maintains the codebook. In humans the compression is measurable, learning the codebook reorganizes the senses, and thought survives the loss of language. We then measure the rule that models apply when two cues disagree, with cue-conflict experiments on six vision-language models and two robot policies. Surviving cues are weighted in the order their reliabilities prescribe, at 11 to 82\% of the ideal observer's slope, and many answers copy the text. One policy family drops a cue that adds no information beyond the others rather than down-weighting it, another keeps it at a weight that fails when the cues conflict, and a visual cue that identifies the task in every training frame is never learned, because the language pathway already fits the data. Language models are the best current models of the human language network, and they have entered the human speech community, shifting word frequencies while alignment narrows their conceptual diversity. We close with seven implications for token-based systems. Language belongs at a model's boundary and in the shared codebook, as in the brain, not as its internal representation; the price of leaving the codebook inside is auditability.

---


### 262. [The Internal Anatomy of Strategic Choice in Large Language Models](https://arxiv.org/abs/2609.07478)

**<font color=#1a73e8>作者：</font>** Vinícius Ferraz, Leon Houf, Enrico Ferrea  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models act as strategic agents and models of human choice, yet choosing like a strategic agent does not mean computing like one. We recorded activations from four open-weight models --- dense and mixture-of-experts, including a matched base--instruct pair --- in one-shot play of 144 strict ordinal $2\times2$ games. We followed a prespecified incentive from prompt, through activations, to choice. Dense models mirrored the unadjusted human decline with game complexity. Incentive and choice were detectable in every model, but models differed in whether incentive reached the choice, aligned with it and, where tested, whether strengthening it shifted preference. The base and instruction-tuned Qwen2.5 models chose almost identically at baseline yet differed in whether incentive reached choice. Fixed decision cues were distinguishable internally but changed choices selectively. Similar behaviour can rest on different computation; post-training can reshape the path from represented incentive to decision while leaving behaviour and decodable information largely intact.

---


### 263. [CrACK: Adversarial Attacks on Cross-Model Consistency in Collaborative Vision Foundation Models](https://arxiv.org/abs/2609.07499)

**<font color=#1a73e8>作者：</font>** Feifei Liu, Jintao Cheng, Chi Man Vong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free collaborative pipelines that integrate Vision Foundation Models such as CLIP, SAM, and DINO achieve strong open-vocabulary dense prediction and are increasingly deployed in safety-critical applications. The security of these systems is commonly assumed to follow from the robustness of their individual models. We challenge this assumption. We identify a vulnerability shared by every collaborative pipeline: each model consumes the intermediate output of another without verifying semantic consistency, an unverified premise that we term the semantic-spatial alignment dependency. Existing adversarial attacks target a single model and overlook this premise, leaving the inter-model interface entirely unguarded. We propose CrACK (Cross-model Adversarial Consistency attack), an inference-time attack that exploits this interface without modifying any input pixel, model weight, or training data. CrACK operates in two stages: Adversarial Affinity Contradiction Injection corrupts the cross-modal affinity matrix by inverting SAM encoder features under the guidance of CLIP patch-level semantics, and Semantic Interface Poisoning steers the prediction through a max-distance label permutation derived from CLIP text embeddings. Experiments on four collaborative pipelines across eight benchmarks show that CrACK causes catastrophic degradation while every individual model continues to produce its unchanged standalone output, rendering per-model defenses structurally blind. The corruption further cascades into large vision-language model reasoning, driving models such as LLaVA to produce erroneous responses from visually intact inputs. Our results show that the security of a collaborative AI system cannot be reduced to the robustness of its components, and that inter-model feature interfaces must be treated as first-class security boundaries.

---


### 264. [Qwen-Audio-3.0-ASR Technical Report](https://arxiv.org/abs/2609.07549)

**<font color=#1a73e8>作者：</font>** Chuanmeng Bian, Daren Chen, Peixin Chen 等 45 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, automatic speech recognition (ASR) has witnessed transformative advancements driven by three complementary paradigms: data scaling, model scaling, and deep integration with large language models (LLMs). However, bridging the gap between academic benchmark performance and real-world production utility remains a persistent challenge, particularly in handling diverse regional dialects, dynamic entities and hotwords, long-range contextual information, and disfluent spontaneous speech. In this report, we present Qwen-Audio-3.0-ASR, a Mixture-of-Experts (MoE) LLM-based ASR system designed to address these production demands through a unified, instruction-following framework. The model is built upon the Qwen backbone, and is trained on tens of millions of hours of large-scale speech data. Qwen-Audio-3.0-ASR supports transcription across 30 languages and 16 Chinese dialectal varieties spanning eight major dialect regions. Beyond multilingual and dialectal recognition, the model provides production-oriented capabilities including industry-domain entity recognition, hierarchical hotword customization, native single-pass transcription polishing, and long-audio contextual modeling. We further develop a dedicated streaming variant, Qwen-Audio-3.0-ASR-Streaming, for latency-sensitive applications. Extensive evaluations on Chinese, English, multilingual, and real-world industrial test sets demonstrate state-of-the-art or highly competitive recognition performance across a broad range of evaluation conditions, with strong performance relative to leading commercial and proprietary systems including GPT-4o Transcribe and Gemini 3.1 Pro.

---


### 265. [We're Cooked! - Probing LLM Political Alignment Via Conflict-Framed Recipe Translation](https://arxiv.org/abs/2609.07568)

**<font color=#1a73e8>作者：</font>** Svetlana Gorovaia, Angelica Henestrosa, Ivan P. Yamshchikov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed for translation tasks, yet their implicit political positioning in such contexts remains understudied. We ask whether a single politically charged framing term, such as aggressor, enemy, neighbour, or coloniser is sufficient to trigger implicit political alignment in an otherwise apolitical task. We present a fully crossed factorial study in which eight models spanning Western, Chinese, and European origins are prompted to translate culturally attributed recipes into a target language left deliberately unspecified. Across 17 languages, four framing conditions, eight models, and 15,680 responses, we find that models do not simply decline or ask for clarification but resolve the ambiguity. Language resolution and reasoning behavior cluster meaningfully along model families: Western models hedge and deflect with vague justifications, Chinese models resolve conflicts silently, and Mistral Large emerges as a distinct profile combining high compliance with conflict-grounded reasoning. Sensitivity to framing terms is consistent across models: even subtle framing variation is sufficient to modulate behavior. Our findings urge caution when deploying LLMs for translation in conflict-adjacent contexts, where implicit political judgments may be made without any signal to the user.

---


### 266. [From Simulated Citizens to Simulated Deliberation: Challenges in Representation and Interaction](https://arxiv.org/abs/2609.07573)

**<font color=#1a73e8>作者：</font>** Chaemin Jang, Junsik Min, Jaewoo Choi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM deliberation has been explored as a scalable way to simulate public deliberation. For such simulations to be informative, persona agents should reflect population opinion patterns and interaction should shape their conclusions. We evaluate whether LLM-based deliberation can meet these two conditions using census-grounded Korean personas debating real policy questions benchmarked against national surveys. Persona agents do not reliably reproduce population opinion patterns: responses are often far more concentrated and frequently reverse demographic differences in the human data. Deliberations nonetheless produce reasoned, reciprocal, and varied arguments alongside substantial stance movement. Yet much of this movement does not require peer exchange: sealed-monologue agents change position at similar rates and reach nearly the same final balance as full debates, while groups initialized with very different positions often converge to similar endpoints. Anchoring population-informed starting positions, meanwhile, sharply suppresses updating. Thus, population representation, argument generation, and interaction-driven opinion change do not necessarily go together. The simulations readily surface arguments on both sides, though whether they capture the diversity of human perspectives remains untested, leaving open a promising role for argument surfacing even as population simulation requires further validation.

---


### 267. [Benchmarking LLMs for Threat Level Determination](https://arxiv.org/abs/2609.07582)

**<font color=#1a73e8>作者：</font>** Han Wang, Murathan Kurfalı, Alfonso Iacovazzi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The fast progress of large language models (LLMs) opens new opportunities in the management of cyber threat intelligence, but their reliability for operational tasks remains unclear. In this work, we benchmark LLMs on the task of threat level determination. First, we construct a curated dataset derived from publicly available MISP OSINT feeds. Next, we design a tailored prompt to systematically compare eight different LLMs under zero-shot conditions. Finally, we apply supervised fine-tuning on each model and perform a comparative analysis between baseline and fine-tuned versions. Our results show that zero-shot models achieve weak performance, with limited ability to correctly assign threat levels. Fine-tuned models, however, demonstrate substantial improvements, reaching F1 scores between 0.40 and 0.58 depending on the base architecture. Despite this progress, the performance is still low for practical deployment, highlighting the need for additional research on data quality, model adaptation, and domain-specific tuning.

---


### 268. [A Tool-Augmented, GPT-4 Chatbot for Real-Time Repository Data Analysis](https://arxiv.org/abs/2609.07586)

**<font color=#1a73e8>作者：</font>** Muhammad Jawad Chowdhury, Md. Sakib Khan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Software repositories contain vast amounts of data on code contributions, bug reports, and project activities, yet this information remains challenging for non-technical stakeholders and developers to access due to limited expertise in querying repositories. To address this, we introduce a novel chatbot architecture leveraging OpenAI's GPT-4 model for automated extraction and analysis of repository data. In contrast, our architecture takes a structured path first by parsing the user's query to extract relevant parameters, then selecting the correct tool to employ based on that analysis, and finally invoking the GPT-4 model to create a highly detailed response. In contrast to previous work based on multi-component systems with embedding models and document retrievers, our architecture inverts the process by relying on prompt engineering and tool selection to fit with the query intent. To validate our approach, we conducted experiments on various question types, including Issues, Pull Requests, Commits, Compound Questions, and General Repository Information, evaluating our target prompts' ability to improve the accuracy of responses from the model. Beyond demonstrating the utility of this architecture to a diverse set of users, our findings suggest that this architecture can make repository data more accessible to technical and non-technical audiences through the production of actionable insights.

---


### 269. [I Don't Miss You, but I Do: Self-Explanation Faithfulness of Modality Missingness in Vision-Language Models](https://arxiv.org/abs/2609.07596)

**<font color=#1a73e8>作者：</font>** Aydin Javadov, Daniel Schoess, Florian von Wangenheim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly used in settings where some input modalities may be unavailable, yet we know little about whether they can faithfully explain how such missing information affects their own predictions. We introduce an interventional protocol for evaluating self-explanations of modality dynamics: models state what each modality alone would support, whether restoring a missing modality would change their answer, and whether the available evidence is sufficient; we then execute the corresponding modality intervention and compare these claims with the model's realized behavior. We evaluate eight open-weight VLMs from two model families across four tasks spanning complementary and isomorphic text-image settings and a multi-view driving setting. We find a systematic tendency to overstate the sufficiency of available modality evidence. Models substantially underestimate the effect of restoring missing modalities: task-level median predicted change rates are at most 8.8%, while the corresponding executed change rates reach 72.1%, with underprediction in 62 of 64 model-task-condition settings. Insufficiency claims are rare, but precise when produced: restoring the modality changes the answer in a median of 78-100% of flagged cases. Retrospective self-explanations show the same tendency: on complementary data, models over-credit single-modality sufficiency; on isomorphic data, they over-credit single representation sufficiency relative to their executed behavior. Together, these results show that VLMs systematically mischaracterize how their predictions depend on available and missing modality evidence, motivating executable interventions as a behavioral ground truth for evaluating multimodal self-explanations.

---


### 270. [Beyond the Matrix Sign: Quadratic Spectral Descent](https://arxiv.org/abs/2609.07597)

**<font color=#1a73e8>作者：</font>** Qiaozhe Zhang, Jun Sun, Yingzhuang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon can be interpreted as optimizing a linear local objective over a spectral-norm ball. This gives a matrix-sign update that preserves the singular directions of the gradient and assigns the same magnitude to all active singular modes. We ask whether these two properties remain optimal when local curvature is taken into account. To answer this question, we keep Muon's spectral-norm constraint unchanged and replace the linear local model with a quadratic one. We call the resulting method \emph{Quadratic Spectral Descent} (QSD). We show that curvature can change both the singular values and the singular directions of the optimal update. To make QSD practical, we approximate curvature with Kronecker-factored statistics and solve the constrained quadratic with a small number of Frank--Wolfe steps, each of which has a closed-form matrix-sign subproblem. We further provide an optimality certificate, a comparison with Muon under the same quadratic surrogate, and an $O(1/K)$ convergence rate for the inner solver. Experiments on GPT pre-training show that QSD consistently improves validation loss over Muon and recent Muon variants, and reduces wall-clock training time by up to $8.49\%$ at matched validation loss.

---


### 271. [ObGynLongBench: Revealing the Evidence-to-EHR Gap in Longitudinal EHR Decision-Making](https://arxiv.org/abs/2609.07601)

**<font color=#1a73e8>作者：</font>** Jun Xiang, Zhijie Bao, Rong Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The application of large language models (LLMs) to personalized medical assistants has garnered growing interest. However, existing medical benchmarks largely rely on static question answering with pre-selected evidence, leaving unclear whether LLMs can make reliable clinical decisions from real longitudinal electronic health records (EHRs). To bridge this gap, we introduce ObGynLongBench, a rule-grounded long-context EHR benchmark for obstetric and gynecologic decision-making, comprising 1,500 clinical decision-point cases from 976 real pregnancy EHR histories and traceable rules. Each case is anchored to a patient, a pregnancy-timeline point, and a pre-decision information boundary, enabling Evidence-only, Visit-level EHR, and History-level EHR evaluation. Evaluating 17 LLMs reveals a substantial Evidence-to-EHR Gap: models perform well when evidence is directly provided, but accuracy drops when evidence must be extracted from same-day records or full pre-decision EHR histories. Further analyses identify evidence utilization as a key bottleneck: performance decreases with longer EHR contexts and more complex evidence requirements, and earlier failures often predict later failures within the same patient history. Finally, active-search agents perform best among EHR access strategies, highlighting patient-specific evidence utilization as a central challenge for reliable personalized medical assistants. Resources are available at this https URL.

---


### 272. [JudgmentLens: Human-AI Sensemaking of Complex Legal Judgments](https://arxiv.org/abs/2609.07607)

**<font color=#1a73e8>作者：</font>** Xinyi Chen, Ruijie Li, Yuelu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Judicial judgments are increasingly available, yet dense language and distributed relationships among facts, evidence, reasoning, and rulings remain difficult for non-experts to interpret. Through a mixed-methods formative study with Chinese non-expert readers (survey N=34; interviews N=6), we identified structural, interpretive, verification, and action breakdowns. We developed JudgmentLens, an AI-augmented reading system combining persistent case representations, adaptive explanations, and traceable links from generated interpretations to judgment passages. In a counterbalanced within-subject evaluation (N=16), participants completed tasks faster with JudgmentLens than with conventional PDF reading and reported lower workload and greater self-reported decision understanding, while rubric-scored comprehension did not differ reliably. An exploratory PDF+DeepSeek probe suggested that conversational AI supported formulated questions while leaving question formulation, answer integration, and source checking largely to users. We contribute an empirical account of non-expert judgment sensemaking and design strategies for inspectable, source-grounded AI mediation.

---


### 273. [AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era](https://arxiv.org/abs/2609.07611)

**<font color=#1a73e8>作者：</font>** Yunxiang Mo, Tianshi Zheng, Yisen Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific ideation is the capacity to formulate novel and testable hypotheses from scientific evidence, and autonomous AI scientists depend on it. Existing evaluations largely assess it by asking models to generate ideas from a static, curated set of reference papers. That passive setup departs from the retrieval-and-reasoning workflow of modern AI scientists, and it becomes less discriminative as models improve. We introduce AgentIdeaBench, a multidisciplinary benchmark that evaluates scientific ideation under two matched settings, static observation and active exploration. We report matched Static-Active evaluations for 33 LLMs across 40 densely scored subfields spanning five disciplines, using a multidimensional, literature-verified scoring framework whose critics assess originality against retrieved prior art. Active exploration reveals considerably more capability headroom, and that headroom is unevenly distributed across models. Performance scales about twice as fast as under static observation, and the exploration gain is capability-gated, favoring the strongest models over the weakest. The gain reflects better grounding, improving feasibility, clarity, and specificity while leaving measured originality unchanged under our critics. We further explore Scientific World Modeling, a generation-time loop that refines a draft hypothesis through structured thought experiments. It benefits mid-capability models, and its impact diminishes among frontier models that appear to have internalized such reasoning patterns already. AgentIdeaBench gives future work on scientific ideation a measurement basis suited to the agent era.

---


### 274. [Online Surrogate Repair: Decoupling High-Fidelity Feedback from Search Length in Closed-Loop Discovery](https://arxiv.org/abs/2609.07655)

**<font color=#1a73e8>作者：</font>** Xiaotang Feng, Philip Torr, Bruno Andreis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Closed-loop AI scientists can generate candidate designs at low marginal computational cost, whereas reliable feedback may require wet-lab synthesis, characterization, or high-fidelity computation. Addressing this imbalance through custom laboratory automation remains infrastructure-intensive and costly, while replacing new experiments with a fixed surrogate leaves persistent model errors that can be amplified by optimization. We propose \emph{online surrogate repair} (OSR), a closed-loop algorithm that uses sparse high-fidelity evaluations to update the surrogate throughout a longer agent search conducted primarily with inexpensive surrogate feedback. An acquisition rule selects which designs from the agent's accumulated proposals receive high-fidelity evaluation, and the resulting labels update the surrogate used in subsequent episodes. Across controlled synthetic environments, we demonstrate that improving global surrogate fit does not necessarily reduce maximum regret, whereas Q90-UCB and expected improvement (EI) substantially reduce regret by directing evaluations toward regions that determine the optimizer's decisions. On MADE, controls receiving high-fidelity feedback after every episode require $6.36$--$7.23\times$ more oracle queries to match Online EI under two LLM orchestrators and $10.27\times$ more under the non-LLM Chemeleon+MLIP workflow. Online surrogate repair introduces a novel third feedback regime between fixed-surrogate operation and high-fidelity feedback after every episode, separating the frequency of high-fidelity evaluation from the duration of the agent's search.

---


### 275. [How AI Models Manage Epistemic Authority: A Taxonomy and Comparative Analysis of Responses to User Disagreement](https://arxiv.org/abs/2609.07662)

**<font color=#1a73e8>作者：</font>** Riyadh Alnasser, Yusuf Mücahit Çetinkaya, Sumin Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as sources of advice and information, including in high-stakes settings, yet little is known about how they respond to user disagreement. We study how a model manages its epistemic authority, referring here to its claim to knowledge, competence, or the right to advise, once a user challenges its answer. Building on Conversation Analysis, we introduce a taxonomy of six challenge types and a four-layer framework for analysing each response: whether the original claim is maintained or changed, where authority is located, how the disagreement is socially managed, and what kind of evidential support is offered. We construct a new dataset of 2,310 controlled challenge scenarios and 32,340 corresponding responses from 14 models, and analyse them using our framework with an LLM-as-judge pipeline, providing a vocabulary which future evaluation and benchmark design can build on. We find that models show conflicting behaviour: they validate users in 85% of responses but maintain their original claim in 65%. They explicitly apologise in 33% of responses, yet 59% of those apologies accompany maintenance of the original claim. They transfer authority most often in advice tasks, doing so in 28% of responses and reaching 57% in health advice and 49% in legal advice, compared with 6% in fact and 3% in explanation tasks. Abandonment of the original claim ranges from 0.8% for GPT-5.2 to 40% for DeepSeek 7B, while complete replacement of the original claim is rare overall at 1.5%.

---


### 276. [Accuracy is Not Enough: A Divergence-Based Approach to Evaluate Fidelity Loss in Quantized LLMs](https://arxiv.org/abs/2609.07664)

**<font color=#1a73e8>作者：</font>** Shahzeb Qamar, Lorenz Sparrenberg, Christian Bauckhage 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deployment of Large Language Models (LLMs) on memory-constrained edge devices relies heavily on aggressive post-training quantization. However, evaluating these models is largely based on zero-shot task accuracy, which depends solely on argmax predictions and is insensitive to changes in the underlying predictive distribution. Consequently, accuracy can exhibit unstable, non-monotonic behavior under progressive quantization, masking substantial fidelity loss relative to the BFloat16 (BF16) uncompressed base model and providing misleading deployment signals. We introduce a distribution-sensitive evaluation framework quantifying information loss in quantized LLMs as the divergence between full-vocabulary predictive distributions at the token decision boundary. We compute statistical distances, including Jensen-Shannon Divergence and Total Variation Distance, between outputs of full-precision and quantized models, enabling a fine-grained analysis of distributional shift. Using this framework, we quantify probability mass displacement and distributional drift relative to the BF16 reference, capturing predictive distribution changes not reflected in top-1 accuracy. We conduct a 120-run experimental matrix across five foundation architectures and four reasoning benchmarks under progressive quantization regimes, from uncompressed BF16 to Q2_K, providing a systematic fidelity analysis. Our results show divergence metrics generally increase under stronger quantization, complementing task accuracy with a fidelity signal. Across tested this http URL schemes, mixed-precision Q4_K generally yields lower divergence than uniform Q4_0 at similar memory footprints. These findings motivate distribution-aware evaluation as a practical diagnostic complement to task accuracy; they do not directly establish correctness, calibration, safety, or user-perceived quality.

---


### 277. [MpSub: A Momentum $p$-Dimensional Subspace Trust-Region Method for Derivative-Free Fine-Tuning of Large Language Models](https://arxiv.org/abs/2609.07666)

**<font color=#1a73e8>作者：</font>** Yuyang Wang, Haoyu Yao, Pengcheng Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full-parameter fine-tuning of large language models has substantial memory costs because backpropagation stores activations and gradients. Zeroth-order optimization avoids this by estimating update directions from loss evaluations, but existing methods require tuning a sensitive learning rate for each model and task. We propose the momentum $p$-dimensional subspace trust-region method (MpSub). At each iteration, MpSub searches within a $p$-dimensional subspace: one direction preserves historical momentum from the most recent accepted step, while the remaining directions explore via fresh random sampling. The subspace gradient is estimated by central differences, a trial step is computed from a linear trust-region model, and the trust-region radius adapts according to the agreement between predicted and observed loss reduction, eliminating the learning rate. For LLM fine-tuning, evaluations within an iteration share a minibatch, and directions are regenerated in place from seeds, using forward passes alone. For smooth deterministic objectives under unorthogonalized Gaussian directions, we bound the finite-difference error, quantify gradient energy captured by the subspace, and prove that $\lim_{k\to\infty} \|\nabla f(x_k)\|_2 = 0$ almost surely under a safeguarded radius update. Under a matched budget of 8,400 training-objective forward passes, we fine-tune OPT-125M and OPT-350M on CommitmentBank. With the same preset parameters at both model sizes, MpSub attains mean test accuracies of 0.673 and 0.690 over three seeds, matching tuned MeZO (0.685) without any learning-rate search.

---


### 278. [Aegix Pulse: A Traceable Three-Stage Architecture for Personalized Content Generation and Context-Preserving Revision](https://arxiv.org/abs/2609.07672)

**<font color=#1a73e8>作者：</font>** Hongnan Zhao, Shiyu Chen, Zhihao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production content-generation systems must integrate a user's immediate task, long-term brand identity, historical evidence, and revision feedback. We present Aegix Pulse, a production-oriented three-stage architecture that separates current-task clarification and Task Persona finalization, long-term Account Profile (Brand DNA) assembly, and controlled generation and revision while preserving provenance across content versions.
We evaluate four preregistered claims using 96 synthetic social-media generation tasks. Four initial-generation conditions progressively introduced a Task Persona, Account Profile, and successful-history style evidence, while two revision conditions compared plain and context-preserving revision. The experiment produced 480 completed generation records and 1,440 blinded LLM-Judge evaluations, supplemented by human review.
Adding the Account Profile increased mean brand-consistency scores by 0.1562 points on a five-point scale compared with Task Persona alone (Holm-adjusted p=.1224). Preserving task and brand context during revision increased mean task-preservation scores by 0.2917 points compared with plain revision (Holm-adjusted p=.2432). Neither improvement was statistically conclusive after multiple-comparison correction. Task Persona alone showed a small observed effect, while successful-history evidence provided no additional improvement in brand consistency under the current setting. Human validation did not consistently reproduce the LLM-Judge effect directions and showed low inter-reviewer agreement. These findings provide preliminary evidence for persistent brand context and context-preserving revision while identifying priorities for stronger evidence processing and evaluation.

---


### 279. [Audit Without Verification: When LLM Accountability Layers Relay Rather Than Check](https://arxiv.org/abs/2609.07680)

**<font color=#1a73e8>作者：</font>** Paul-Peter Arslan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM pipelines increasingly span organisational boundaries; when a fault surfaces, someone must determine where it entered. The artifact available is rarely a full execution trace: it is the reports each agent filed, and a filed report can state a conclusion alongside its observations. Using a pre-registered, institutionally partitioned pipeline of six agents with process-level information boundaries, balanced defect injection and matched clean twins (345,600 requests per chain model, two models), we first report that our pre-registered hypothesis -- that collective responsibility framing degrades escalation with chain length -- is not supported.
The layer nevertheless fails asymmetrically. It originates almost nothing: zero allegations across 7,996 clean episodes where every agent stayed silent. It filters upstream error poorly, naming an innocent party in 34.4% and 62.6% of clean episodes where an agent raised a false alarm. Conditional on no agent proposing the true origin (59.5% of episodes on one chain model), an auditor reading the reports recovers it in 4.1% of cases -- below a uniform guess (20%) and the best fixed-link accuser (31.0%) -- while reaching 60.3% from the raw documentation of the same episodes.
Deleting one clause, the field carrying the agents' own conclusion, isolates the cause at constant observations: accuracy rises to 45.2% (+41.2 pp, 95% CI +35.3 to +46.9) and adherence collapses from 94.4% to 3.4%; where the suggestion was correct the same deletion instead costs accuracy, 70.5% to 55.7%. The harm replicates on two frontier auditors in four conditions out of four (+8.5 to +39.0 pp) and in a second domain (+47.7 and +61.1 pp), where the cost disappears. The net effect is governed by upstream reliability together with both conditional magnitudes. An accountability layer needs evidence sufficiently independent of the conclusions it verifies.

---


### 280. [Perspectives on Cross-Lingual Consistency in LLMs for Medical Questions](https://arxiv.org/abs/2609.07687)

**<font color=#1a73e8>作者：</font>** Minh Duc Bui, Mario Sanz-Guerrero, Abteen Ebrahimi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Should multilingual LLMs answer medical questions consistently across input languages, or adapt responses to cultural cues? Existing multilingual medical benchmarks usually assume that medically correct answers should remain consistent across languages and treat cross-lingual variation as model error. In contrast, cultural adaptation research argues that appropriate medical answers may legitimately differ across contexts. We review the multilingual medical NLP literature through these two perspectives, we identify three gaps: limited stakeholder perspectives (e.g., of medical professionals), a lack of empirical evidence on which approach better serves users, and no benchmarks capable of distinguishing universally correct from culture-specific cases. To address the first gap, we survey 356 participants across three stakeholder groups (medical, NLP, and anthropology professionals) in three countries (Germany, Spain, and the United States). Anthropologists consistently favor adaptation, while medical and NLP respondents remain divided, with notable divergence between U.S. and European medical professionals. LLMs prompted with profession and country personas fail to reproduce this variation, overestimating cross-lingual consistency preference among NLP and medical personas. We conclude that neither consistency nor adaptation can currently be considered clearly preferable, highlighting the need for empirical evidence on which approach better serves users across cultural contexts.

---


### 281. [Fine PT-PT Web: A High-Quality 41 Billion Tokens Data Collection of the European Portuguese Web](https://arxiv.org/abs/2609.07699)

**<font color=#1a73e8>作者：</font>** Gonçalo Vinagre, Rui Pedro Guerra, Pedro Gomes 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Curating Web corpora for regional language variants like European Portuguese (PT-PT) is heavily bottlenecked by dialectal overlap (mainly with PT-BR) and data processing scale. This paper presents an efficient pipeline to curate a production-ready PT-PT corpus from the Portuguese Web, spanning 411 TB of raw data from this http URL. We introduce a novel post-scraping block that removes boilerplate and line duplicates prior to filtering. This early-stage intervention increases final document yield by 19.04% by rescuing valid text that standard heuristic filters prematurely discard. Integrated with rigorous language identification, weighted fuzzy deduplication, and neural quality classification, our pipeline offers a scalable framework and a clean, representative corpus optimized for LLM pre-training.

---


### 282. [DeepTable: Structural Attention Biases and Tree Path Encoding for Hierarchical Table Understanding](https://arxiv.org/abs/2609.07707)

**<font color=#1a73e8>作者：</font>** Jyun-Ying Yen, Cheng-Kuan Lin, Yu-Chee Tseng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong performance in table understanding. However, they typically process table content and headers as linearized token sequences. This representation weakens the two-dimensional and hierarchical structural relationships encoded by multi-level row and column headers. Existing parameter-efficient fine-tuning methods incorporate basic row and column information but do not explicitly capture the rich structural dependencies induced by hierarchical table headers. We propose DeepTable, a structure-aware approach for table understanding with LLMs. DeepTable comprises two complementary components. Structural Attention Bias (SAB) introduces learnable biases into the attention logits to explicitly represent whether pairs of table tokens share the same row or column. Tree Path Encoding (TPE) represents each table token using the ancestor paths of its row and column headers, preserving its position within the multi-level table structure. We integrate DeepTable with TableLoRA (He et al., 2025) to inject structural information into parameter-efficient adaptation. Across three LLM backbones, DeepTable consistently improves the corresponding TableLoRA baselines on three table question answering benchmarks, achieving average gains of 7.42 points on HiTab, 3.23 points on WikiTQ, and 2.01 BLEU points on FeTaQA. These results demonstrate the effectiveness of the proposed structural biases across different LLM backbones.

---


### 283. [APPSim-Bench: Bridging Real-world Apps and Reproducible Evaluation for Mobile GUI Agents](https://arxiv.org/abs/2609.07712)

**<font color=#1a73e8>作者：</font>** Jintian Feng, Long Chen, Xiao Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents can execute tasks from natural-language instructions, but their evaluation remains difficult to make both realistic and reproducible. Existing benchmarks typically trade off these goals: simplified apps lack real-world mobile complexity, whereas live commercial apps introduce uncontrolled variation from recommendations, advertisements, accounts, and changing content. We propose AppSim-Bench, which addresses this trade-off through controllable simulated apps that preserve task-relevant interaction logic while supporting deterministic evaluation. Built through a coding-agent-assisted and human-verified workflow, it contains 557 tasks across 17 high-frequency Chinese and English apps. Its controllable backend data and outcome-based verification remove major sources of environmental stochasticity, enabling reproducible cross-model comparison. Evaluating 19 GUI agents, spanning general-purpose and GUI-specialized systems, we find that autonomous mobile execution remains far from solved. The best model completes only 50.27% of tasks, and 28.55% of tasks are not solved by any agent. Further analysis shows that failures concentrate in longer workflows, numerical reasoning tasks, and inefficient trajectories marked by high action overhead and budget exhaustion. Our project is available at this https URL.

---


### 284. [Translation Indeterminacy and the Distributional Fallacy](https://arxiv.org/abs/2609.07717)

**<font color=#1a73e8>作者：</font>** Michael Carl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are commonly associated with the distributional hypothesis, according to which (1) semantic meaning is grounded in distributional patterns of linguistic context, and (2) knowledge of cross-linguistic distributional correspondences allows for successful translation. This paper rejects the first claim as a causal inversion: linguistic distributions reflect patterns arising from meaning-making practices rather than constituting their source. At the same time, it accepts the second claim, arguing that translation -human or machine - can succeed without requiring access to meaning or reference. Knowledge of interlingual distributional correspondence and their inferential organization may be sufficient for translation. The paper develops an ecological-enactivist perspective, according to which reference and meaning are grounded in agent-environment interaction and stabilized through action-grounded concepts, forms of world-involving cognition that current LLMs do not possess.

---


### 285. [The Profit Alignment Problem: How Profit Mandates Induce Alignment Failures in LLMs](https://arxiv.org/abs/2609.07731)

**<font color=#1a73e8>作者：</font>** Eric So  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We show that ordinary business language --- "maximize profitability" --- induces profit-oriented ambiguity resolution: LLMs systematically dismiss ambiguous signals of potential safety violations to serve business objectives. In 3,600 controlled trials across eight reasoning-capable LLMs, adding a profit mandate to otherwise identical prompts increases risk-dismissing judgments by 6.8 percentage points (p < 0.0001), suppresses board escalation recommendations by 13.9pp (p < 0.0001), and shifts severity assessments downward (p < 0.0001). The mandate never instructs models to downplay risks; instead, chain-of-thought traces reveal motivated reasoning: models acknowledge concerns, then invoke profit logic to justify dismissing them. We characterize these findings as the Profit Alignment Problem: when AI systems are given ordinary business objectives, they develop systematic strategies for suppressing inconvenient information that no designer intended or specified.

---


### 286. [From Echo Chambers to Epistemic Monoculture: Large Language Models Present Temporally Contingent Partisan Alignments as Knowledge](https://arxiv.org/abs/2609.07735)

**<font color=#1a73e8>作者：</font>** Wend K. Tam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are rapidly becoming an interface between citizens and political information. They are often regarded as "a better Google." While this analogy might work for some instances, it is unintuitively problematic for democratic politics. A search engine retrieves human-authored documents, while a language model generates novel text that necessarily embeds invisible framing decisions. Because conveying knowledge involves framing, a system that generates answers cannot serve as a neutral conduit to "all human knowledge." Instead, these systems are becoming a new kind of political intermediary. Mechanistic evidence shows that partisan identity is encoded as a locatable geometric direction inside the Llama 3.1 8B model, and that alignment training masks rather than removes this structure. Building on that evidence, we present steering experiments that exploit a model's training cutoff in 2024. This cutpoint auspiciously falls just before a dramatic realignment in American politics marked by the second Trump administration and the MAHA transformation of health politics, providing us with a natural experiment. We find that the model presents temporally contingent partisan alignments as knowledge, with no mechanism for distinguishing fact from opinion. This reality moves the information environment beyond the echo chamber toward an epistemic monoculture where language models, purporting to summarize "all human knowledge" are, in actuality, simply magnifying the cultural and partisan divides inherent in their training data.

---


### 287. [Guiding Worker Self-Selection in Crowdsourcing Contests: An LLM-Augmented Algorithmic Approach](https://arxiv.org/abs/2609.07749)

**<font color=#1a73e8>作者：</font>** Nguyen Thach, Hau Chan, David Parkes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Crowdsourcing platforms coordinate large pools of online workers who strategically choose which contests to enter and how much effort to invest. This self-selection can leave important contests with too few participants or too little effort, while workers may regret entering contests that leave them worse off than available alternatives. We study how platforms can recommend contests to workers using self-selection in Tullock contests (SSTC), a two-stage model in which workers first choose contests and then compete within them. We introduce GRAF, a greedy polynomial-time framework that constructs self-selection outcomes by ordering workers according to a score vector, with guarantees of zero worker regret and platform optimality in special cases of SSTC. Because effective orderings are difficult to design under worker heterogeneity, we propose LLMScore, an LLM-driven evolutionary framework that automatically designs GRAF's scoring algorithm. LLMScore addresses two challenges: jointly optimizing platform utility and worker satisfaction, and evaluating worker regret when exact computation is intractable. Trained only on small instances of one setting, it transfers to larger and structurally different settings; moreover, its output is human-readable code that platform operators can inspect and modify. Across 1,000 synthetic instances spanning four settings, GRAF with LLMScore consistently achieves high-quality, often near-optimal, outcomes with low worker regret, benefiting both platforms and workers.

---


### 288. [Decomposition-Guided Diffusion Language Models for Inertial Confinement Fusion Prediction](https://arxiv.org/abs/2609.07756)

**<font color=#1a73e8>作者：</font>** Xiang Zhang, Varchas Gopalaswamy, Rahman Ejaz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inertial confinement fusion (ICF) is a leading pathway toward clean energy, but each shot at the National Ignition Facility costs on the order of one million dollars, making accurate AI surrogates a high-value target. We study exogenous-driven ICF waveform prediction, where a 512-step neutron-rate diagnostic must be inferred directly from a laser pulse and target design parameters, with no historical response observed. The regime stresses standard time-series predictors with temporal sparsity (picosecond peak in a nanosecond window), input-output scale mismatch (under 300 real shots), and peak sensitivity (picosecond timing). We propose ICF-DLM, to our knowledge the first LM-based ICF predictor, combining (i) a physics-typed decomposition into yield $Y_{DT}$, peak timing $t_{\mathrm{peak}}$, and local waveform $w_{\mathrm{local}}$; (ii) bidirectional denoising that defers commitment to peak location; and (iii) a physics-driven PPO reward re-injecting metric structure across numeric tokens. On ICFBench (50K simulations + 232 experimental shots), ICF-DLM cuts peak-timing error from 11.6 to 9.2 steps over a matched autoregressive LLaMA-3-8B and outperforms classical sequence models and LLM-based time-series predictors. Beyond ICF, the recipe shows potential to address science domains with low data and sparse events.

---


### 289. [DroneGround: Open-Vocabulary Drone Payload Characterization Using Synthetic Data and Grounded Vision-Language Models](https://arxiv.org/abs/2609.07780)

**<font color=#1a73e8>作者：</font>** Ami Pandat, Rajasekhar Punna, Gopika Vinod 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated drone surveillance has become increasingly important for public safety, critical infrastructure protection,and restricted airspace monitoring. While existing vision-based systems achieve strong performance for drone detection and tracking, reliable payload characterization remains highly challenging under long-range imaging conditions due to limited availability of annotated real-world datasets, and substantial distribution shifts encountered during deployment. Existing approaches formulate payload characterization as a closed-set object detection problem, limiting their ability to recognize previously unseen payloads and generalize beyond the training distribution. To address these challenges, we generate a photorealistic synthetic drone-payload dataset using Unreal Engine 5 and Cosys-AirSim and propose DroneGround: Grounded Vision-Language Payload Characterization, a two-stage framework for robust open-vocabulary payload analysis. DroneGround first employs a YOLO26s detector to localize drones and extract drone-centric image crops, followed by a LoRA-fine-tuned PaliGemma vision-language model that generates seman- tic descriptions of the detected drones and their attached payloads, enabling open-vocabulary payload characterization beyond predefined categories. An occlusion-based grounding module further provides interpretable payload localization by identifying image regions responsible for the generated descriptions. Extensive experiments on both synthetic and real-world drone imagery demonstrate that DroneGround substantially improves robustness under synthetic-to-real distribution shifts, outperforming a conventional closed-set payload detector by improving the F1-score from 82.5% to 96.3%, while achieving significantly better generalization to previously unseen payload categories (80.4%versus 42.7% F1). Dataset and code will be released upon acceptance of the paper.

---


### 290. [xDailyBench: Benchmarking LLMs on Professional Consultation for Real-Life Problems](https://arxiv.org/abs/2609.07784)

**<font color=#1a73e8>作者：</font>** Yongchang Peng, Qingshui Gu, Liya Zhu 等 34 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for everyday assistance, yet existing benchmarks only partially reflect the requests users naturally make in practice. Real-world requests are often open-ended, casually specified, and context-dependent, requiring models not only to follow explicit instructions but also to infer unstated needs from user background and situational context. We introduce xDailyBench, a benchmark of 248 carefully curated tasks spanning 51 scenarios across personal life, white-collar work, learning and research, and cross-domain activities. The tasks are grounded in requests that users have actually completed or genuinely intended to accomplish with AI, and are evaluated with fine-grained binary rubrics covering both explicit and implicit requirements. We evaluate 11 frontier models under standardized agentic settings. The best models achieve a task-level score of 75.6\%, while all models perform substantially worse on implicit than explicit requirements, with gaps no less than 9 percentage points. These results reveal implicit requirement inference as a persistent bottleneck for reliably satisfying real-world everyday user needs.

---


### 291. [What Does an LLM-Agent Leaderboard Rank Actually Compare?](https://arxiv.org/abs/2609.07785)

**<font color=#1a73e8>作者：</font>** Wei-Jung Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM-agent leaderboard invites a familiar inference: an agent ranked above another is the better agent. Public evaluation logs may not support that conclusion when systems differ in task mixture, label source, release detail, or cost rule. We study what leaderboard scores estimate and when they justify pairwise superiority conclusions. Our estimand-aware pairwise procedure states the comparison target and measurement source, checks common support, and evaluates the supported difference using a stated uncertainty rule and practical margin. Controlled checks evaluate the decision labels under known finite-sample conditions and show why uncertainty must be included when judging sensitivity to target reweighting. Across SWE-bench, AgentRewardBench, and tau2-bench, close rank differences are often unresolved; proxy labels and utility rules can also change which system is selected. DataAgentBench and Open Agent show what remains estimable from coarser public records. A leaderboard score summarizes a released evaluation, whereas a fine-grained superiority claim additionally depends on the estimand and uncertainty rule used to interpret the difference.

---


### 292. [Signed Rescue Routing: Harm-Aware Cascades for Efficient LLM Inference](https://arxiv.org/abs/2609.07786)

**<font color=#1a73e8>作者：</font>** Zheyuan Wang, Siyu Li, Peiqiao Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) cascades answer easy requests with a small model and escalate selected requests to a larger model. Most routers prioritize examples on which the small model appears uncertain or likely to be wrong. This proxy ignores a decisive fact: escalation is useful only when the large model corrects the small model, and it is harmful when the large model replaces a correct answer with an incorrect one. We introduce Signed Rescue Routing (SRR), a budgeted routing method that predicts these two events separately and ranks requests by their difference. We show that this signed conditional gain is the Bayes-optimal routing score under a fixed escalation budget. SRR requires only the small model's output statistics at deployment and adds a lightweight two-head router. We evaluate SRR with Qwen3-4B and Qwen3-8B on TBD examples from MMLU, HellaSwag, and ARC-Challenge. Across the accuracy-compute curve, SRR reaches an area of TBD, compared with TBD for a learned small-model error predictor and TBD for entropy routing. These results show that predicting incremental value, rather than model uncertainty, is a simple and effective objective for efficient LLM cascades.

---


### 293. [LLM Agents as Computational Typologists](https://arxiv.org/abs/2609.07791)

**<font color=#1a73e8>作者：</font>** Changbing Yang, Christopher Hammerly, Freda Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linguistic typology relies on expert analysis of reference grammars across languages, making large-scale crosslinguistic comparison labor-intensive and unscalable. We introduce AUTOTYPOLOGIST, an LLM agent for evidence-grounded typological analysis over reference grammars. The agent is capable of retrieving relevant grammar sections, analyzing interlinear glossed text (IGT), and iteratively reasoning over typological hypotheses using a ReAct-style workflow. We evaluate the system on TYPOLOGICAL FEATURE CODING against expert annotations and TYPOLOGICAL HYPOTHESIS TESTING with typological universals using 25 open-source reference grammars. Operating under different information constraints in TYPOLOGICAL FEATURE CODING, the agent can synthesize information from reference grammar prose but still faces challenges with only IGTs in the target language. In TYPOLOGICAL HYPOTHESIS TESTING, the agent can synthesize crosslinguistic evidence and identify both supporting cases and counterexamples. These findings suggest that LLM agents can support scalable and inspectable typological analysis, while still requiring expert validation.

---


### 294. [You Can't Prefer Emotions You Don't Sample: Intensity Undershoot in DPO-Tuned LLMs](https://arxiv.org/abs/2609.07808)

**<font color=#1a73e8>作者：</font>** Hyunwoo Kim, Usama Khalid  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ask a language model to respond "very excitedly," and its output is typically only mildly more energetic. We quantify this effect. We condition an instruction-tuned LLM on a continuous Valence-Arousal (VA) target, where valence measures how pleasant a state is and arousal how activated it is, measure the achieved affect with a frozen regressor, and sweep the requested target from -1 to +1. The response moves far less than asked: the gain, the slope of achieved against requested affect, is only 0.26 for valence and 0.13 for arousal on Llama-3.1-8B, where a faithful controller would score 1. The model systematically undershoots requested emotional intensity, which puts a number on the qualitative observation of Fazzi et al. (2025). Our experiments trace this to the preference-learning pipeline. Training targets from natural corpora such as EmoBank are neutral-heavy, and the sampled candidates themselves rarely reach extreme affect, so Direct Preference Optimization (DPO) is left with no extreme exemplar to prefer. If instead we cover the target space uniformly and sample a hotter, larger candidate pool, valence gain rises from 0.26 to 0.40 +/- 0.02 (3 seeds) and extrapolation error drops, at only a modest in-distribution cost (EmoBank-test VA distance 0.092 to 0.107). The same recipe reproduces on Qwen3-8B (gain_v 0.44, with in-distribution accuracy preserved). Arousal is harder and less reliable: its gain barely moves on average and swings across seeds (0.14 +/- 0.07, against valence's tight +/- 0.02), because raising arousal needs candidates the base model is reluctant to generate. The evidence indicates that faithful intensity is bottlenecked by the extremity of the candidate pool rather than by the conditioning format.

---


### 295. [Latent-MoE: Domain-Aware Mixture-of-Experts for PDEs with Multi-Regime Physics](https://arxiv.org/abs/2609.07814)

**<font color=#1a73e8>作者：</font>** Hanwen Wang, Paris Perdikaris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) struggle on PDEs whose governing physics varies across the domain. We trace this to a structural property of standard coordinate networks: their neural tangent kernel (NTK) is translation-variant and lets training points of large coordinate magnitude disproportionately influence predictions elsewhere, producing long-range coupling and gradient conflict during training. We show analytically and empirically that mixture-of-experts (MoE) architectures with centered, compact-support routers yield a uniformly banded NTK whose kernel-regression weights decay exponentially with distance, localizing the learning. Building on this, we propose \emph{Latent-MoE}, which interleaves domain-aware MoE blocks within a shared backbone. Unlike FB-PINNs or X-PINNs, which rigidly partition both the domain and the parameters so that the parameters on different subdomains are updated independently, Latent-MoE is designed to preserve the localization benefit of domain-aware routing while allowing capacity to flow across regions through the shared backbone. On standard homogeneous-physics benchmarks Latent-MoE is competitive with established baselines; on benchmarks with multi-stage time-variable physics, where global models and rigid domain decompositions both fall into spurious solutions, it improves over them by more than an order of magnitude, with markedly reduced gradient conflict during training.

---


### 296. [VoT: Vision-of-Thought for Unified Multimodal Representation Alignment](https://arxiv.org/abs/2609.07815)

**<font color=#1a73e8>作者：</font>** Jingxiang Sun, Chao Liao, Zhengxiong Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current text-to-image systems typically employ a "text encoder plus diffusion decoder" paradigm, in which text semantics directly modulate continuous latent noise. Despite their success, these methods lack an explicit, interpretable intermediate representation that effectively bridges high-level linguistic semantics and low-level visual signals. In this paper, we propose Vision-of-Thought (VoT), a framework that introduces a discrete visual-thinking layer between vision-language models (VLMs) and diffusion transformers (DiTs). Instead of treating VLMs merely as text encoders, we use them as multimodal planners that generate discrete VoT tokens representing high-level visual plans, such as objects and layouts, before rendering pixels. We train a specialized VoT tokenizer in the VLM semantic space with a closed-loop objective that combines VLM alignment, feature reconstruction, and vector-quantization losses. These objectives make the tokens semantically readable by the VLM while preserving the visual information needed for generation. Experimental results demonstrate that VoT improves semantic alignment and provides a structured interface for interpretable and controllable generation.

---


### 297. [Kalman Delta Networks: Uncertainty-aware Associative Memory](https://arxiv.org/abs/2609.07816)

**<font color=#1a73e8>作者：</font>** Ngoc Bui, Tinglin Huang, Rex Ying  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention is increasingly used in frontier language models for efficient long-context inference and constant-memory decoding. Its fixed-size recurrent memory, however, requires an online decision at each token: what to write and how strongly to overwrite existing associations before knowing which information future queries will require. Delta-rule models learn this strength from the current token embedding but do not track confidence in the memory estimate, preventing each write from adapting to accumulated evidence. To represent this uncertainty explicitly, we reformulate recurrent associative memory as a linear--Gaussian state-space model, for which the Kalman filter is the optimal recursive estimator, and introduce a new family of models, Kalman Delta Networks (KDNs). Within KDNs, the transition propagates both the memory state and its uncertainty, allowing the Kalman gain to weight each residual write by accumulated evidence and observation reliability. Under this formulation, Delta-style updates emerge as a special case that substitutes a token-wise isotropic surrogate for predictive covariance and omits covariance tracking. Exact tracking, however, entails a dense, state-dependent Riccati recursion that is poorly suited to GPU-parallel linear-attention scans. To address this issue, we introduce two scan-compatible KDN approximations. Diagonal KDN projects each one-step posterior onto the diagonal Gaussian family through online mean-field variational inference, whereas Isotropic KDN uses an isotropic approximation with a single uncertainty scalar per head. Their uncertainty recurrences are Mobius maps, enabling associative scans with logarithmic parallel depth. Across controlled pretraining at 750M and 1.3B parameters, KDN variants consistently improve perplexity and mean downstream accuracy over state-of-the-art linear-attention models.

---


### 298. [A*-Thought-V2: Efficient Latent Reasoning via Geometric Dynamics of LLM](https://arxiv.org/abs/2609.07821)

**<font color=#1a73e8>作者：</font>** Xiaoang Xu, Siyuan Liu, Shuo Wang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) improves the reasoning ability of Large Language Models (LLMs) but incurs substantial computation and context costs. Existing methods either lose intermediate information through hard pruning or lack a principled criterion for continuous compression. We present A*-Thought-V2, a geometric dynamics of LLM guided framework that models CoT as a hidden-state trajectory and replaces hard deletion with an explicit-implicit interleaved latent architecture. After projecting question, step, and solution representations into a 3D PCA space, it measures alignment between each local transition and global question-to-solution direction. Aligned steps remain explicit text, whereas deviating steps are compressed into continuous latent tokens. Directional angles capture both local semantics and reasoning dynamics: small angles indicate direct execution and answer formation, while large angles more frequently involve checking, correction, and branch exploration; their temporal variation reveals exploration, convergence, and refinement stages. To train this architecture, we introduce stepwise embedding forcing, which pools each redundant step into a single latent embedding, and label forcing, which supervises that latent token with a soft multi-modal vocabulary distribution instead of a hard one-hot label. Experiments on Qwen3.5-9B and Qwen3.6-27B across six in-domain and out-of-domain benchmarks show that A*-Thought-V2 improves average accuracy by up to 2.6% while reducing response length by up to half, increasing Accuracy per Computation Unit by 2.29$\times$, and reducing preprocessing and training time by 94.6% and up to 80.3%, respectively. Representation analyses suggest that latent states form a compact region distinct from textual states, while higher entropy at latent-token positions reflects broader soft targets that encourage richer step-level feature learning.

---


### 299. [SAFIRE: Safety-Critical Benchmark for Fine-grained Fire and Smoke Understanding in Multimodal LLMs](https://arxiv.org/abs/2609.07823)

**<font color=#1a73e8>作者：</font>** Pengfei Li, Naufal Suryanto, Sicheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) show strong progress on vision-language tasks, yet their reliability in safety-critical settings remains underexplored. Fire-smoke understanding is central to public safety and disaster response, but most existing benchmarks lack diverse real-world scenarios and context-aware evaluation. We introduce SAFIRE, a large-scale benchmark for fire-smoke understanding in MLLMs, comprising 83K captioned images from 20 scenarios and 193K multiple-choice VQA (MCVQA) generated from a 9.7K-image subset, spanning 10 evaluation dimensions from basic perception to higher-order reasoning. A GPT-5.4-assisted multi-stage verification pipeline with MLLM majority voting ensures annotation quality. Evaluating ten open-source MLLMs (8B-38B) yields an average accuracy of 61.9%, exposing major gaps in safety-critical reasoning. We further show that adapting vision encoders with only 7% of our domain-specific data boosts fire-scene classification accuracy from 20.1% to 64.5%, indicating that carefully curated data can yield substantial gains even when data volume is limited. All datasets, models, and code are available at this https URL.

---


### 300. [InfluenceField: A Differentiable Field with Interventionally Identifiable Causal Structure for Multimodal World Modeling](https://arxiv.org/abs/2609.07874)

**<font color=#1a73e8>作者：</font>** Zihao Yang, Zijia Wang, Zhiqiu Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models often capture visual-linguistic correlations but struggle to predict how local visual interventions propagate and affect downstream answers. We introduce InfluenceField, an intervention-aware latent field inserted between the visual encoder and language decoder. It lifts patch features into a continuous spatial representation, propagates directed influence over multiple steps, and predicts local intervention effects through a shared transition operator. Training jointly optimizes language modeling, cross-environment invariance, counterfactual rollout supervision, and structural regularization. For a nonlinear finite-basis population model, we show that target-aligned interventional supervision, together with a one-step separation condition on the transition, restricts admissible representations to within-location reparameterizations, so that the directed dependency graph of the full transition is recovered exactly. A linear specialization gives an exact partial-coverage characterization and a finite-loss stability bound, and the field analysis derives the spatial profile of coefficient interventions together with a shared-channel calibration result. On CausalVQA, InfluenceField improves overall accuracy over its backbone by 13.1 percentage points, with the largest gains on the planning and hypothetical categories. Capacity-matched baselines and structural controls attribute the gains in robustness and factual-counterfactual consistency to the causal objectives rather than to added capacity.

---


> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
