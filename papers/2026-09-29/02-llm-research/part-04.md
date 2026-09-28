# 🧠 大模型相关研究 | 2026年09月29日

> 本类共 **183** 篇论文：已确认 **174** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-183**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-183**

---

### 151. [Towards Mitigating Fabricated Consensus: The Active Provenance Gate for Multi-Agent Debate Synthesis](https://arxiv.org/abs/2609.31422)

**<font color=#1a73e8>作者：</font>** Jakub Masłowski, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model-based multi-agent debate (MAD) systems are being increasingly used as complex decision pipelines in distributed processes. However, their final synthesis phase still remains inadequately controlled. Even with detailed debate logs, summarizing models are prone to fabricating smoothly written debate consensus that is not grounded in the debate's history. To address this safety gap, this paper presents empirical research and studies if the introduction of active post-debate verification can mitigate the production of such factually unsupported summaries, while still providing valuable information. Furthermore, it is examined whether explicitly signalling divergence is preferable in the absence of a reliable compromise. The Active Provenance Gate (APG) is introduced as a post-debate verification layer that treats the source as a hard constraint, analysing the debate logs, auditing each claim, and applying self-correction. In crisis simulations, the self-healing mechanism more than doubles the average data Provenance Fidelity in difficult condition scenarios, before the strict gate blocks unsupported claims and generates divergence reports. In the human study, a vast majority of the users (over 75%) preferred a report explicitly stating failure in critical scenarios, despite most of them perceiving fabricated consensus from the baseline system as more fluent. Our main contribution is the transition of data origin tracing from passive logging to active conditional blocking before publication.

---


### 152. [Compress What You See, Not What You Say: Anchored Context Distillation for Latent-Observation Software Engineering Agents](https://arxiv.org/abs/2609.31430)

**<font color=#1a73e8>作者：</font>** Zhensheng Zou, Guoqing Wang, Dan Hao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool observations dominate the context of software-engineering agents, making long interaction histories costly to maintain. Existing context compression methods can discard information needed by later actions, while adapting agents to soft-token representations can compromise their original behavior. To reduce context while preserving action-critical information and agent behavior, we combine Latent Observations, Hard Actions (LOHA), a context layout that separates compressed history from text needed for exact reference, with Anchored Context Distillation (ACD), a training method that enables latent reading while constraining behavioral drift. LOHA compresses older tool observations into soft tokens while retaining the agent's own turns and the last K observations in text, providing compact access to historical information and exact access to recent content. To enable the agent to use this representation, ACD distills the base model's full-text predictions into the latent view while anchoring its behavior on plain-text inputs to the same base model. On SWE-bench Verified, K=3 reduces context per call by 43% for Qwen3-4B and 57% for SWE-Master-4B-RL, with resolve rates of 12.1% and 21.8% versus 14.5% and 27.5% for their uncompressed bases. A single-run recency sweep reaches 14.4% and 23.0% at K=8, with larger windows generally favoring task performance over compression. Under a 32K-token limit, Qwen3 with K=3 resolves 21.1% of a 199-instance subset versus 11.1% for the same adapted agent using full text. In concurrent single-GPU serving, it achieves 1.9 times that full-text agent's instance throughput.

---


### 153. [ViSTA: A Simple Bridge Extends Visual Alignment to Clinical Time-Series Understanding in Multimodal LLMs](https://arxiv.org/abs/2609.31448)

**<font color=#1a73e8>作者：</font>** Junyi Gao, Yu Shi, Pingzhao Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical prediction models estimate risk from patient measurements, while large language models support medical text understanding and question answering. Yet their language capabilities do not ensure accurate prediction from structured, high-dimensional clinical time series. Improving this ability would connect risk estimation with flexible questions about a patient's evolving condition. We introduce ViSTA, a compact adapter that incorporates irregular numerical measurements into a pretrained vision-language model's chart representations. It learns corrections to visual tokens while leaving all pretrained parameters unchanged. On MIMIC-IV, ViSTA has the highest mean scores among the compared adaptations on all four metrics for acute kidney injury and mortality prediction across models with 2-9 billion parameters. With 0.516 million trainable parameters, the 2-billion-parameter model reaches an area under the ROC curve of 0.7376 for acute kidney injury, compared with GPT-5.6 Sol's 0.7380 with text input and high reasoning effort. Training for temporal question answering yields 69.27% accuracy at 4 billion parameters with over 90% fewer trainable parameters than low-rank adaptation using charts or numerical text, at a 2.82-4.88 percentage-point accuracy gap. ViSTA extends pretrained language models to numerical prediction and temporal questions.

---


### 154. [From Reward Signal to Visual Utility: A Controlled Audit of Medical VLM Post-Training](https://arxiv.org/abs/2609.31450)

**<font color=#1a73e8>作者：</font>** Wang Jingxin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language model (VLM) post-training is commonly evaluated through answer accuracy. We examine how changes in accuracy and training objectives relate to image-conditioned decisions in a controlled Qwen2.5-VL-3B study on PMC-VQA. We compare supervised fine-tuning (SFT) with low-rank adaptation (LoRA) restricted to the language model, expanded multimodal adaptation scopes, standard answer-only Group Relative Policy Optimization (GRPO), and a counterfactual evidence objective. On 2,000 clean-test questions, language model LoRA SFT changes correct-image accuracy by +1.10 percentage points (95% paired bootstrap CI:-0.85 to +3.05), while visual-benefit events decrease by 2.40 points and image sensitivity decreases by 5.60 points. Paired records reveal 155 acquired and 203 lost visual-benefit events. Broader adaptation yields lower correct-image accuracy than language-model LoRA SFT. Standard GRPO produces mixed-reward groups and parameter updates, with an uncertain clean test accuracy change. A generation audit reveals that canonical option scores can follow a different token path from generated answers. With scores taken along the greedy generation path, the evidence target improves on the training set; its gains over standard GRPO remain inconsistent on validation data at matched training doses. Sample-level analyses trace how evidence scores, decision margins, and generated answers change during post-training. This empirical and measurement audit identifies gaps between optimization activity, target acquisition, and useful held-out visual behavior.

---


### 155. [Diagnosing the Sources of Compositional Failure in Vision-Language Models: A Controlled Analysis](https://arxiv.org/abs/2609.31456)

**<font color=#1a73e8>作者：</font>** Mona Gandhi, Cenk Merih Olcay, Kuan-Chieh Lo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) often struggle with compositional reasoning tasks, but the reasons for this underperformance remain unclear. A common hypothesis is that models struggle to integrate multiple components, leading to training interventions to improve compositional binding. However, this assumption has never been directly quantified. Existing benchmarks evaluate captions only in their composed form, making it impossible to separate the cost of joint reasoning from the cost of recognizing individual components under increasing load. We introduce COMPASS (COMPositional Analysis of SkillS), a controlled evaluation framework designed to isolate and measure the distinct factors underlying compositional failure. By comparing performance on composed captions with their decomposed counterparts , we directly quantify the cost of compositional integration across 87K image-caption pairs. Across multiple VLMs, this gap is real but partial, accounting for only part of the observed degradation. This motivates a finer-grained investigation into what additional factors govern model behavior. We analyze performance at the level of individual skills: object detection, attribute binding, and relation reasoning, using skill-targeted perturbations across 274K image-caption pairs. We find a consistent skill-specific pattern: each skill degrades primarily with the count of its own primitive type (self-load), while cross-load effects are predominantly positive, suggesting that primitives of different types provide useful grounding context. This pattern holds across standard contrastive encoders, explicitly trained compositional reasoning models, and non-contrastive architectures. These findings show that compositional degradation reflects multiple separable factors that cannot be reduced to joint reasoning alone.

---


### 156. [Segment-Level Agentic Topic Modeling for Improved Data Exploration and Resource Efficiency](https://arxiv.org/abs/2609.31460)

**<font color=#1a73e8>作者：</font>** Myeongjun Erik Jang, Antonios Georgiadis, Sae Young Moon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Topic modeling is an effective technique for discovering hidden themes within documents and is widely used in text mining and data analysis across a variety of industry sectors. Recently, large language model (LLM)-based topic models have been emerged that prompt LLMs to generate topics then assign the topics to documents, producing more natural and human-readable topics than conventional topic modeling algorithms. However, the nature of topic assignment process causes certain drawbacks, such as the incapability to produce topic distributions over a document, too broad or narrow topics, and high resource consumption, which increases with the number and length of of documents being assigned topics. These issues are particularly critical for industrial applications, which require high-quality, in-depth analysis and the processing of large volumes of documents. In this context, this paper introduces a framework called SeLATM, which addresses these concerns by employing segment-level topic generation and topic refinement through agentic feedback loops. Experimental results on various datasets demonstrate that SeLATM significantly reduces the LLM resources compared to methods based on topic assignment process, while maintaining superior performance.

---


### 157. [Game Arena: Strategic LLM Evaluation in Competitive Environments](https://arxiv.org/abs/2609.31473)

**<font color=#1a73e8>作者：</font>** Bovard Doerschuk-Tiberi, Yao Yan, Justin Chiu 等 62 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Kaggle Game Arena, an open and ever-expanding platform to evaluate large language models (LLMs) through competitive games. Different from static benchmarks, game arena enables models to play head-to-head matchups in structured environments where the gameplay strength naturally increases as models evolve, preventing performance saturation. This technical report details the infrastructure behind Game Arena and describes the three pilot game environments: Chess, Poker, and Werewolf. These environments span perfect information, imperfect information, and multiplayer game settings, enabling a systematic study of models' strategic planning, adaptation, and robustness under uncertainty. For each game, we provide a detailed description of the environment, evaluation metrics, and results from running full competitions across models. Through robust infrastructure and large-scale ground-truth based evaluation, Game Arena ensures reproducibility, transparency and generalizability to new games and variants over time.

---


### 158. ["AI is (not) the new...": A Diagnostic Analogy Framework for Generative AI's Cultural Impacts](https://arxiv.org/abs/2609.31482)

**<font color=#1a73e8>作者：</font>** Rida Qadri, Vinodkumar Prabhakaran, Remi Denton  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI is reshaping the cultural infrastructures through which knowledge is found, synthesized, and held accountable. To make sense of this shift, scholars and policymakers reach for historical analogies of technologies such as the printing press, steam power or electricity. But these comparisons are typically imprecise about which property of the technology carries the comparison, and imprecise analogies produce imprecise governance by designing interventions against the wrong property of the system. This paper offers a diagnostic framework for analyzing how generative AI can transform epistemic and cultural practice. This paper offers a diagnostic framework for analyzing how generative AI can transform epistemic and cultural practice. We decompose each intervention into three coordinates: the epistemic site at which a technology acts, the governing logic by which it organizes its object, and the technical mechanism through which the logic is instantiated. This framework allows us to distinguish between structural cultural consequences, which follow from the mechanism itself, from contingent ones, which remain open to design and institutional choice. Applying the framework to information discovery and knowledge synthesis, we show how the shift from indexicality to inference and from editorial authority to statistical consensus produces specific, traceable cultural effects and reveals governance levers that gestalt analogy obscures.

---


### 159. [Prompt Minimization: Reducing Input Redundancy Without Sacrificing Output Fidelity](https://arxiv.org/abs/2609.31505)

**<font color=#1a73e8>作者：</font>** Marius F. R. Juston, Kevin A. Karim, Jonathan Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the growing capabilities of large language models (LLMs), prompt design remains largely heuristic and ad hoc. This project will explore $\textit{prompt minimization}$, the process of reducing prompts to their smallest, most information-dense form while preserving output fidelity. Practically, shorter prompts reduce computational overhead and inference latency, especially when large contexts, such as entire documents or codebases, are included unnecessarily. Further, longer prompts can damage LLM reasoning and accuracy. Theoretically, the existence of multiple prompts yielding equivalent outputs suggests a high degree of redundancy in the input space, raising fundamental questions about what information is essential to elicit specific model behaviors. We propose three variant frameworks to identify and evaluate minimal prompts and demonstrate that minimal prompts often produce outputs comparable to those of their longer counterparts. These findings suggest new directions for efficient prompt engineering and deepen our understanding of input compression in LLMs.

---


### 160. [Evaluating Cultural Awareness of LLMs for Haitian Creole](https://arxiv.org/abs/2609.31506)

**<font color=#1a73e8>作者：</font>** Christelle Clervilsson, Yanzhu Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit substantial performance disparities between high- and low-resource languages. Beyond lower task performance, they often fail to capture the cultural norms and values of underrepresented communities. In this work, we present the first systematic evaluation of cultural awareness in LLMs for Haitian Creole, a language spoken by millions but severely underrepresented in digital resources. We assess cultural awareness along four complementary dimensions---specificity, bias, diversity, and variation---using a benchmark of culturally salient prompts curated by native speakers in a text infilling setting. Our results reveal a clear gap between cultural awareness in Haitian Creole and higher-resource French, with Haitian performance being more uneven across domains and more affected by French linguistic interference. Story generation further reveals recurring portrayals of Haitian characters through hardship and resilience, showing that even positive characterizations can encode stereotypical narratives. Our code, benchmark, and evaluation framework are publicly available.

---


### 161. [SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery](https://arxiv.org/abs/2609.31507)

**<font color=#1a73e8>作者：</font>** Jiajun Jiang, Chunliang Hua, Zichun Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban uncrewed aerial vehicle (UAV) vision-language navigation (VLN) requires agents to follow instructions across extended urban spaces, inherently demanding long-term memory and geospatial grounding. However, scaling existing benchmarks remains difficult because of their reliance on costly reconstructed 3D assets, limiting geographic diversity and episode scale. To address this, we introduce SatNav, a scalable, long-horizon UAV VLN benchmark built from high-resolution satellite imagery. SatNav targets city-level navigation missions and uses satellite crops as approximations of UAV nadir views for visual observations. Through an automated cue-to-episode pipeline, SatNav constructs 118K episodes from 59 scenes across 18 cities, with an average trajectory length of 379 m. To stress-test long-horizon memory and geospatial reasoning, SatNav defines three task families: Boundary, Landmark, and Route, targeting loop progress tracking, landmark-based spatial grounding, and route following with counting cues. Benchmarking classical VLN agents and recent agents based on large vision-language models (LVLMs) on SatNav shows that city-scale navigation remains challenging. We further introduce SwiftVLN, a modular framework with switchable memory components, and conduct systematic memory-design ablations. Finally, satellite-to-UAV transfer experiments show that satellite-trained navigation models can operate on real-flight UAV observations, showing the practical relevance of SatNav. Our project page: this https URL

---


### 162. [Muslim: A Deployed Arabic Voice AI Platform for Grounded Islamic Knowledge](https://arxiv.org/abs/2609.31511)

**<font color=#1a73e8>作者：</font>** Yahya Mohamed Elnawasany  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Muslim, a production Arabic voice AI platform serving grounded, sourced Islamic knowledge to real users. Beyond a real-time voice pipeline (NeMo Arabic ASR, an OpenAI-compatible LLM endpoint, self-hosted TTS) and a deterministic multi-source retrieval layer routed across six Model Context Protocol servers, we report three things a research prototype typically lacks. First, a released family of fine-tuned Arabic Islamic model artifacts: an efficient tool-routing LLM (Muslim-6B-PRO, 5.94B parameters) and a Modern Standard Arabic TTS model (Fasih-TTS-V1) that ranks 5th of 17 overall and 2nd of 11 open-weight systems on the community-voted Arabic TTS Arena for MSA. Second, an account and metering layer - a free per-account turn allowance, capacity-aware refusal, and email verification deferred to the point it actually matters - that turns an open demo into an operable, abuse-resistant product. Third, a three-layer observability stack (liveness, error reporting, product analytics) built specifically around the system's characteristic failure mode: a GPU-bound agent host going silent while the web tier keeps serving normally. We report real, measured latency and accuracy figures (98.4% recitation-validation accuracy on 124 cases; end-to-end voice latency of 0.9-1.7s) and discuss the concrete engineering trade-offs and limitations of running an Islamic-knowledge voice product in production.

---


### 163. [Forensic Twins: Self-Supervised Residual Learning for AI-Generated Image Forensics](https://arxiv.org/abs/2609.31514)

**<font color=#1a73e8>作者：</font>** Javier Muñoz-Haro, Ruben Tolosana, Ruben Vera-Rodriguez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detectors of AI-generated images are typically trained using samples from all Generative AI architectures they must catch, and struggle as soon as a new architecture emerges. Recent approaches have explored self-supervised pre-training as an alternative solution, yet standard frameworks work against the forensic task, e.g., their augmentations overwrite the micro-statistics of image formation. This paper introduces Forensic Twins, a Self-Supervised Residual Learning (SSRL) framework whose pretext task suppresses macroscopic content availability. Each image is mapped through a frozen, off-the-shelf forensic residual extractor, from which two spatially disjoint crops are drawn. Sharing no pixel, the two views retain minimal semantic structure to align, leaving a redundancy-reduction objective with a predominant common signal: the stationary fingerprint of the image acquisition pipeline. Additionally, Forensic Twins is trained exclusively on real images; no AI-generated image is observed at any stage. Experiments show that Forensic Twins attributes AI generator sources with 56.61% accuracy, i.e., 6.13% above the previous state-of-the-art zero-shot method at 375x lower latency. We also demonstrate that fitting a Gaussian Mixture Model (GMM) offline using only the real image embeddings extracted from Forensic Twins turns it into a state-of-the-art zero-shot detector, reaching 97.99% AUC across 27 unseen AI generators, including GANs, diffusion models and commercial systems. Code, weights and exact splits will be made publicly available

---


### 164. [Structured Reasoning Agentic Framework for Interpretable Critical View of Safety Assessment](https://arxiv.org/abs/2609.31524)

**<font color=#1a73e8>作者：</font>** Qing Xu, Yuxiang Luo, Zhen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical scene understanding is critical for computer-assisted intervention, yet laparoscopic cholecystectomy remains challenged by the complex anatomy of the hepatocystic triangle and the risk of bile duct injury. Existing methods for Critical View of Safety (CVS) assessment typically treat it as a holistic prediction task, mapping visual features directly to criterion-level labels. This black-box paradigm lacks explicit reasoning about anatomical relationships, limiting both interpretability and compositional generalization. To address this, we propose ReasonCVS, a structured reasoning agentic framework empowered by Vision-Language Models (VLMs) that decomposes CVS assessment into explicit, fine-grained anatomical verification. Specifically, we devise an Anatomical Scene Graph Abstraction (ASGA) that organizes anatomical entities and their spatial relationships into a structured representation. To operationalize this, we introduce a Rationale-Aware Reasoning Agent, powered by a Large Language Model (LLM) fine-tuned via rationale distillation. Functioning as a strict central decision-maker, it invokes VLM-driven Sub-criterion Verifier as a specialized perceptual tool to parse the graph and independently evaluate individual sub-criteria. Through calibrated soft reasoning, this agent synthesizes the tool-gathered distributed observations, yielding a final verdict alongside a traceable clinical rationale. Extensive experiments on the Endoscapes-CVS201 benchmark demonstrate that ReasonCVS achieves superior performance (68.1\% mAP) over state-of-the-art while providing interpretable, criterion-level explanations for reliable surgical assessment.

---


### 165. [FragToken: Amplifying LLM Inference Costs through Noncanonical Token Generation](https://arxiv.org/abs/2609.31552)

**<font color=#1a73e8>作者：</font>** Zihan Wang, Rui Zhang, Xinyuan Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) inference becomes increasingly expensive, resource-consumption attacks pose a growing threat to model providers. Existing attacks typically amplify cost by inducing abnormally long or repetitive outputs on attacker-controlled or triggered requests, making them easier to detect and limiting their deployment-wide impact when benign traffic dominates. In this work, we uncover a previously overlooked token-level attack surface arising from the many-to-one mapping from token sequences to decoded text. Although standard LLMs predominantly generate the canonical token sequences induced by their tokenizers, the same text can also be represented by substantially longer non-canonical sequences. This representational flexibility exposes a new avenue for resource-consumption attacks: an attacker can train the model to favor such sequences, systematically increasing the number of autoregressive decoding steps without a proportional increase in visible response length. However, we empirically find that directly maximizing token fragmentation substantially degrades model utility, producing conspicuous answer-quality failures that undermine attack stealthiness. To address this challenge, we propose FragToken, a training-time framework that combines source-model self-distillation, capacity-aware filtering and budgeting, and BPE-Aligned Merging to induce fragmented generation under ordinary prompts while largely preserving model utility. We evaluate FragToken on four LLMs across three benchmarks. Across the four models, FragToken achieves a three-benchmark average token inflation ratio (TIR) ranging from 1.99 to 2.46, while causing only minor degradation in model utility. Our work reveals a covert LLM supply-chain threat that increases inference cost without requiring large volumes of attack requests while largely preserving utility.

---


### 166. [Multi-agent Scaling Across Disjunctive and Compensatory Tasks](https://arxiv.org/abs/2609.31563)

**<font color=#1a73e8>作者：</font>** Carolina Fortuna, Blaz Bertalanic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems are often expected to improve as team size increases, yet the scaling behavior may depend on task structure. Our central contribution is to introduce Steiner's taxonomy of group tasks as a framework for analyzing multi-agent LLM scaling and focusing the analysis on disjunctive and compensatory tasks. We model independently sampled agents as conditionally independent given the item, which yields their large-team limits: plurality voting converges to the model's modal answer, and averaging converges to the model's item-level bias. Across selected representative benchmarks, 13 open-weight models, and teams of up to 30 agents, we find qualitatively different scaling behavior. On disjunctive tasks, the probability that at least one agent is correct grows by 5-20 points with team size, but plurality voting over agents that answer directly realises almost none of this potential, as the model predicts to within 0.5 points on average. Multi-round revision raises accuracy considerably, yet the gain is nearly the same with one peer as with 29. In contrast, scaling provides little benefit on Fermi estimation, despite its natural suitability for aggregation: item-level biases shared across the samples of a model account for about 87% of the squared error, so averaging reduces error by only about 6%. Combining model families helps on Fermi estimation but does not surpass the strongest member on disjunctive tasks. These results show that task structure, together with the mechanism combining member outputs, is a fundamental determinant of team scaling.

---


### 167. [DeepEdu-v1: Efficient and Scalable Agentic LLMs for Vietnamese Education](https://arxiv.org/abs/2609.31568)

**<font color=#1a73e8>作者：</font>** Quang Nguyen, Hieu Nguyen, Hien Hoang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI tutoring could markedly improve learning outcomes for students in developing regions such as Vietnam, yet the two obvious paths both fall short. Cloud assistants such as ChatGPT route sensitive student data to foreign servers---violating data-sovereignty laws such as Vietnam's Decree 53---and, pre-trained on Western-centric corpora, are not organized around the national textbook curriculum, so their knowledge of local content is unsystematic and frequently hallucinated. Self-hosting an open model keeps data on-premise but hits a two-fold wall: post-training quantization (AWQ, GPTQ) tames the static weight footprint, yet the dynamic KV cache and prefill latency of long tutoring contexts still cause out-of-memory failures and slow responses on consumer GPUs, while the model keeps hallucinating on region-specific material. We present DeepEdu-v1, an AI-tutoring system for Vietnamese education built on SCALE (Self-improving Context-Aware Learning Engine), a framework with two innovations. First, a long-context inference engine amortizes token selection from per-sub-chunk to per-cluster granularity; on long-context retrieval it issues x7.7 fewer retrieval calls than a state-of-the-art selective-attention baseline, cutting prefill latency (TTFT) by roughly 35% while matching or improving task accuracy. Second, a self-improving agentic layer continuously curates a verified playbook from past interactions instead of fine-tuning, a design intended to progressively reduce reliance on dominant-language priors as trustworthy local knowledge accumulates. In its deployed configuration, DeepEdu achieves a nearly x2 TTFT speedup over standard vLLM serving and lifts agentic accuracy from 70.0% to 79.5% on complex tasks, with the strongest per-track gains across financial-reasoning and interactive-agent benchmarks.

---


### 168. [Strategically Diverse Sampling for Self-Training](https://arxiv.org/abs/2609.31571)

**<font color=#1a73e8>作者：</font>** Alexander Gurung, Esmeralda S. Whitammer, Mirella Lapata  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many LLM training and inference methods, including RL and test-time scaling, depend on repeated sampling, but benefit only when the responses meaningfully differ. Self-training faces the same challenge: training data is typically constructed by sampling IID responses and filtering primarily for correctness, thereby overrepresenting strategies a model already favours. We investigate strategic diversity, or substantive variation among approaches to a problem, as an alternative principle for constructing self-training data. We generate strategically diverse data with two sampling methods: GROOT, a new method which constructs a hierarchical tree of approaches and samples distinct paths, and Verbalized Sampling (VS), adapted to produce an unstructured set of approaches. Across competitive programming and Next-Chapter Prediction domains, models trained on strategically sampled data outperform IID-trained counterparts on difficult tasks and provide strong initializations for RL and test-time scaling. Most strikingly, self-training on strategically diverse but incorrect traces from Qwen3-4B outperforms IID distillation from a 235B teacher. These results challenge prevailing assumptions about what makes useful self-training data and show that diversity of approaches can matter more than correctness or teacher scale.

---


### 169. [Configuration, Not Conscience: A Large-Scale Empirical Study of LLM System Prompts](https://arxiv.org/abs/2609.31575)

**<font color=#1a73e8>作者：</font>** Constantinos Patsakis, Vasilios Argyropoulos, Efthymios Alepis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Leaked system prompts are often treated as windows into the hidden values of commercial language models, yet their composition is rarely studied at scale. We analyze a merged corpus of 407 leaked, reconstructed, or officially published system prompts from 62 vendors across four community collections, identifying 29 near-duplicate clusters covering 66 files. Operational content rather than ethical statements dominates the corpus; a deliberately simple block-level classifier assigns roughly 58\% of classified words to tool/protocol and roughly 5\% to safety policy, while the strictest rule-lines guard tool use and file safety over harmful content by an 11:1 margin. Literal text transfer concentrates in a small set of cross-vendor pairs. Prompts also carry measurable maintenance debt, with version chains turning over thousands of words per release. The evidence supports treating leaked prompts as operational specifications, closer to configuration files than value statements, and treats reuse and prompt rot as engineering and supply-chain concerns. Because most documents are adversarial in origin and the detectors are deliberately simple, all magnitudes are directional; we audit the main classifier's error modes.

---


### 170. [AgentWorld: Benchmarking Long-Horizon Collaboration of Multi-agent LLMs](https://arxiv.org/abs/2609.31590)

**<font color=#1a73e8>作者：</font>** Raphael Shu, Yusen Zhang, Young Min Cho 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Existing multi-agent benchmarks primarily test in competitive settings, short-horizon interactions under 20 steps, or simply aggregate individual performance, failing to isolate and highlight genuine collaboration capabilities of LLM-based agents. We introduce AgentWorld, a benchmark of 100 human-annotated tasks (with 100 augmented variants) for evaluating long-horizon, multi-agent collaboration. Tasks span 50+ interaction rounds across a rich MMORPG sandbox and require 3-20 agents with asymmetric roles and abilities to coordinate through communication, joint planning, and resource sharing under a blackbox setting where each agent acts independently without access to others' internal states. To quantify collaboration effectiveness in addition to conventional binary task success, we propose Causal Collaboration Effectiveness (CCE), a graph-based metric that traces causal dependencies between agent actions and measures what fraction of a team's effort actually contributed to the outcome. Experiments with Gemini 3 Flash, Claude Haiku 4.5, GPT-5 Mini, and DeepSeek R1-70B show that even the best model achieves only 52.0% task success, with systematic failure modes including communication breakdowns, role confusion, and inability to maintain shared plans across rounds. AgentWorld is fully open-source.

---


### 171. [From Source Code to Network Profile: Automated and Traceable MUD Profile Generation for IoT Devices](https://arxiv.org/abs/2609.31594)

**<font color=#1a73e8>作者：</font>** Alessandro Lotto, Abdulla R. A. Almenhali, Savio Sciancalepore 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Manufacturer Usage Description (MUD) standard allows IoT manufacturers to define expected network behaviors in a MUD file. This file can be translated into enforceable access-control policies, restricting compromised devices to operate solely through manufacturer-defined communication patterns. However, practical adoption of MUD depends on profiles that are accurate, complete, and maintainable. Existing approaches use traffic-based automation but require device deployment and prolonged monitoring, capturing only behavior exercised during observation. Rare, failure-triggered, or configuration-dependent communications may remain absent, producing incomplete policies that disrupt legitimate operation and offer limited insight into the software components responsible for each rule. We present AutoMUD, a source-code-driven tool that generates traceable MUD profiles for IoT devices from their firmware and software source code. AutoMUD combines static and syntactic extraction, retrieval-grounded language-model reasoning, and deterministic validation and compilation to recover the communication behavior characterizing an IoT device and translate eligible endpoints into policy rules. By analyzing code-level evidence, AutoMUD exposes rarely exercised and conditional communication paths, links every generated rule to its source-level provenance, and preserves excluded findings with explicit reasons for review. Our evaluation on a Linux-based repository demonstrates that AutoMUD recovers complete communication behavior, consolidates validated behavior into semantic endpoint groups, and generates structurally valid MUD profiles. Through a controlled semantic fault-injection campaign, we demonstrate that AutoMUD enables analysts to detect, localize, explain, and correct propagated errors, recovering policies semantically identical to their clean counterparts.

---


### 172. [GraphWrit3R: End-to-End 3D Scene Graph Writing](https://arxiv.org/abs/2609.31595)

**<font color=#1a73e8>作者：</font>** Luka Milivojevic, Nikola Popovic, Sayan Deb Sarkar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene graphs provide a structured representation of complex environments by encoding objects, their semantic attributes, and the spatial and functional relationships between them. Current approaches for 3D scene graph generation suffer from several fundamental limitations. They rely on complex multi-stage pipelines with explicit intermediate representations, making systems fragile and prone to error propagation. They assume access to ground-truth object annotations during inference, which deviates from real-world scenarios. They depend on proprietary models, hindering open-source deployment, or incur prohibitively slow inference. We present GraphWrit3R, a simple end-to-end method that takes a 3D point cloud, Gaussian Splats, or a combination of both as input, and directly outputs a complete scene graph as a structured JSON script. The graph lists all objects, their semantic attributes, and the relationships between them, while avoiding all of the above mentioned limitations. The choice of multiple input modalities is purely for versatility, allowing a single set of weights to handle diverse scenarios. Point cloud inputs are encoded via Sonata and Gaussian Splat inputs via Chorus, with both modalities projected onto a shared voxel grid and fused through a novel per-voxel contrastive alignment loss before being decoded by a large language model. As a natural consequence of the LLM, GraphWrit3R also supports open-vocabulary querying. On the 3DSSG benchmark, our method achieves state-of-the-art performance on object class, predicate, and triplet recall, outperforming methods that rely on ground-truth object annotations during inference. We further provide qualitative results and analyze different input modality configurations, contrastive loss formulations, and token fusion strategies.

---


### 173. [New LoRA Skills Should Read but Never Write](https://arxiv.org/abs/2609.31600)

**<font color=#1a73e8>作者：</font>** Zeyan Li, Panqi Yang, Qirong Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adapters (LoRA) make it cheap to fine-tune a large language model once per task, but combining several independently trained adapters into one model remains difficult: merging the updates in weight space causes interference, retraining on all task data is expensive, and routing between separate adapters gives up the goal of a single combined model. We trace the difficulty to two choices that every composition method makes implicitly. A LoRA update admits infinitely many equivalent factorizations; the choice among them is invisible while an adapter serves alone, but it determines what a learned interaction between adapters can see. A coupling between an old skill and a new one can likewise point in either direction, and the direction decides whether the old skills keep computing what they computed before. We introduce READ (Read-only Expansion of Adapter Deltas), which fixes both choices: each adapter is rewritten into a balanced canonical form that preserves its update exactly, and the coupling grows in one direction only, so a new skill can read the input subspaces of old skills but cannot write into their output subspaces. The only trainable object at each append is the new skill's row of the coupling matrix, and the composed update folds into the base weights with no inference cost, routing, or task-specific rules. We evaluate READ across four benchmark suites and two model families, adding skills one at a time. Across several families, READ improves every suite average over the strongest published baselines built from the same adapters---by more than twenty points on SuperGLUE and more than seven points on the domain suite---and nearly all complete addition sequences end above every direct baseline. Factor coordinates and coupling direction, which a lone adapter never exposes, are what decide whether composed skills survive.

---


### 174. [Learning to Stop without Learning to Stop: Self-Supervised Confidence Training Improves Reasoning Efficiency](https://arxiv.org/abs/2609.31619)

**<font color=#1a73e8>作者：</font>** Parsa Hosseini, Akasha Tigalappanavara, Sumit Nawathe 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning models often generate very long reasoning traces, making inference computationally expensive. Existing approaches typically improve efficiency either through inference-time early-stopping mechanisms or by explicitly encouraging shorter reasoning during training, for example through reinforcement learning with length penalties. We show that substantial efficiency gains can instead emerge from a different kind of supervision: \textit{confidence}. Using a self-supervised procedure, we fine-tune reasoning models to predict their confidence in the answer at intermediate points along their own reasoning trajectories using only 600 training problems. Confidence is used only as a training target: the loss contains no objective for reasoning length, efficiency, or stopping. At inference, the fine-tuned models use the standard generation procedure, with no confidence elicitation or early-stopping mechanism. Despite this, self-supervised confidence fine-tuning makes reasoning more efficient, reducing generated tokens by up to 25\% at matched accuracy across Gemma, Qwen, Nemotron, and GPT-OSS models on mathematical, scientific, and coding reasoning benchmarks, with efficiency gains comparable to methods that explicitly optimize for shorter reasoning. Analysis of reasoning episodes further shows that confidence supervision largely preserves the base models' high-level reasoning composition rather than selectively suppressing particular behaviors. Our results suggest that efficient reasoning may emerge as a downstream consequence of learning metacognitive signals, without being directly optimized.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 175. [EviDETR: Preserving Query-Relevant Temporal Evidence for Moment Retrieval and Highlight Detection](https://arxiv.org/abs/2609.30724)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoran Sun, Yufan Li, Qichen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint video moment retrieval and highlight detection requires identifying query-relevant temporal segments while estimating clip-level saliency, yet DETR-style pipelines do not explicitly preserve query-relevant evidence throughout encoding, decoding, and cross-task prediction. We propose EviDETR, an evidence-preserving framework with three components. Semantic-aware Feature Reweighting (SFR) enhances query-relevant clip representations through saliency estimation and cross-modal interaction. A Temporal Top-2 Mixture-of-Experts (TTop2MoE) decoder performs query-adaptive refinement via sparse expert routing. MR-to-HD (MR2HD) fusion transfers span-level retrieval evidence to clip-level highlight prediction through confidence-weighted multi-scale aggregation. Using CLIP+SlowFast features, EviDETR achieves 69.29 R1@0.5, 54.77 R1@0.7, and 48.41 Avg. mAP for moment retrieval on QVHighlights, together with 41.83 HD-mAP and 68.33 HIT@1. Strong results on TACoS and Charades-STA further demonstrate cross-dataset transferability.

---


### 176. [Learning Polarization Image Restoration with General Restoration Priors](https://arxiv.org/abs/2609.30728)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chenggong Li, Jinhao Liu, Caiyun Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Polarization imaging captures distinctive surface and geometric cues that benefit a wide range of vision tasks. However, real-world polarization acquisition is often affected by multiple coupled degradations, making image restoration essential for practical polarization vision. Existing methods are largely tailored to specific degradations and remain constrained by the limited scale and quality of polarization data. To address these limitations, we develop an all-in-one polarization restoration framework for diverse and composite degradations. We first study the impact of different polarization representations on restoration performance and identify the normalized Stokes representation as an effective choice for separating intensity and polarization information. Accordingly, we devise a dual-branch architecture that separates intensity and polarization modeling. To overcome the limitations of polarization-specific training, the intensity branch leverages pretrained general restoration priors and a mixture-of-experts extension for composite degradations, while its restoration knowledge is adaptively distilled into the symmetric polarization branch via a cross-domain feature transform. In addition, we establish a composite-degradation polarization benchmark to support all-in-one restoration research. Extensive experiments on public datasets and our proposed benchmark demonstrate the effectiveness of the proposed method.

---


### 177. [EXAONE Demand 1.0: A Time Series Foundation Model for Demand Forecasting](https://arxiv.org/abs/2609.30880)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Sangjun Han, Jun Seo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) are pretrained on series from diverse domains, where demand series make up only a small fraction. Demand data has properties that such corpora rarely contain: Short histories, frequent zeros, censoring by stock-outs, and exogenous events that the series does not record. To this end, we propose EXAONE Demand, built on 1) a demand-specific corpus and 2) a demand-aware adapter. For the corpus, we assemble 11.3M series and 48.4B observations from 73 sources, and a synthetic generator supplies the behaviour that open demand data under-represents. For the adapter, we attach low-rank branches to a frozen general-domain backbone, one for each of the four demand classes (smooth, intermittent, erratic, and lumpy), and a router that reads eight scale-free statistics of the input series decides how much each branch contributes. We build EXAONE Demand in two versions, one trained on real-world and synthetic demand together and one trained on the synthetic corpus alone. On 22 held-out datasets, both versions outperform 36 TSFMs, and real-world demand adds a gain over synthetic data alone.

---


### 178. [Aurora-X: Built for Extreme Time Series Forecasting](https://arxiv.org/abs/2609.31038)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xingjian Wu, Chenjuan Guo, Xiangfei Qiu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) enable cross-domain forecasting, but their development as general-purpose forecasters remains constrained by underexplored training potential and limited architectural versatility. To address these challenges, we introduce Aurora-X, a billion-scale TSFM with a progressive curriculum and a unified architecture. We first use channel-independent pretraining to learn temporal patterns, then introduce cross-variable dependencies, varied context and horizon lengths, and future covariates if available during midtraining. Variable-resolution post-training further enables an adjustable temporal span per token at inference. With fixed model weights, this supports longer histories under a fixed token budget or fewer tokens for the same history, enabling test-time scaling. With a versatile architecture, Aurora-X supports cross-variable modeling, covariate conditioning, and parallel decoding of future patches for probabilistic forecasting. These are supported by a novel pattern-guided mixture-of-experts that expands model capacity through sparse activation and uses shallow patch similarities to constrain deep-layer routing, guiding expert specialization across heterogeneous time series. Furthermore, we propose an implicit quantile network head that predicts arbitrary quantiles to characterize predictive distributions, enhancing probabilistic forecasting flexibility. Comprehensive experiments on GIFT-Eval, TIME, FEV-Bench, TFB, and DAG-Bench demonstrate state-of-the-art forecasting performance against pretrained TSFMs and task-specific supervised models.

---


### 179. [Neural State Prediction: Obstructing Shortcut Learning in EEG Foundation Models](https://arxiv.org/abs/2609.31167)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kieren Yu, Ziyang Liu, Chang Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> EEG foundation models increasingly use masked prediction to learn from unlabeled recordings, but optimizing this objective does not ensure transferable neural representations. A central challenge is that stable positional cues and local correlations can make masked regions predictable without integrating distributed neural context. To reduce this reliance on low-information prediction paths, we introduce Neural State Prediction (NSP), a latent-predictive framework that constrains both the prediction target and the available context. NSP uses a Target Encoder updated by an exponential moving average (EMA) to define latent supervision. Identity residualization removes additive effects associated with channel identity and relative time from the targets, while topology-separated context excludes their immediate spatial and temporal neighborhood from the visible input. We pretrain NSP on 2.2 million EEG segments from TUEG and evaluate it across 30 downstream datasets spanning clinical diagnosis, sleep staging, emotion recognition, motor imagery, event-related potentials, cognitive-state decoding, and language retrieval. Under full-parameter multi-task fine-tuning on EEG-FM-Bench, NSP achieves 63.94 macro balanced accuracy across 14 datasets, exceeding the strongest evaluated baseline by 2.35 percentage points. Controlled component ablations assess the contribution of each mechanism, while matched context controls and held-out interventions characterize the role of context geometry, signal content, and positional information. Jointly designing latent targets and their context offers a promising direction for EEG foundation models that learn from distributed signal structure.

---


### 180. [Self-Supervised Representation Learning: From Spectral Foundation Models to Auroral Emission Spectra](https://arxiv.org/abs/2609.31206)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Matthieu Le Lain, Gaël Cessateur, Sébastien Lefèvre  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auroral spectrographs such as the Auroral Spectrograph In Skibotn (ASIS) record hundreds of thousands of emission spectra, but only a few hundred can be labelled by an expert. To exploit the rest, we pretrain a 1D Vision Transformer with a masked autoencoder on 223,000 unlabelled spectra. Without labels, its representation recovers the emission-line intensity ratios that physicists use to diagnose the precipitating particles (R^2 0.91 vs. 0.77 for an untrained control) and, under one linear probe, classifies as well as 13 features designed by experts. Fine-tuned, the model outperforms the previous supervised auroral classifier on its own benchmark (macro-AP 88.5 vs. 77.8), reaches 0.870 mAP, and exceeds the same architecture trained from scratch by +0.159 with 10% of the labels; attribution shows that it uses both N2+ bands. Could an existing pretrained model replace it? Two astronomical spectral foundation models and a time-series model transfer according to their spectral window: SpectraFM, trained in the infrared, falls below the untrained control, whereas SpecFormer, trained in the optical, approaches in-domain pretraining without reaching it.

---


### 181. [PIA: A Personal Intelligence Agent Turning Health Conversations into Records and Records into Understanding](https://arxiv.org/abs/2609.31255)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jeonghun Yoon, Dongchan Kim, Hongyeon Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose agent memory summarizes conversations: it extracts salient snippets, embeds them, and retrieves the top-k into the prompt. A health agent cannot run on summaries: a dose becomes a sentence, "since last week" is resolved at the model's discretion, and a three-month glucose trend cannot be answered by text similarity. We present PIA, a personal intelligence agent deployed alongside a consumer health agent. PIA receives the agent's natural-language requests, decides for itself whether and how to write or read, and turns conversations into typed clinical records and records into a synthesized understanding of the user. Its memory harness consists of four controls -- extraction, memory, retrieval, and understanding -- each a domain-agnostic mechanism with a pluggable health module: schema, medical alias dictionary, knowledge graph, and temporal rules. We show how the same query receives a different answer as the memory injected into the response context deepens from one-dimensional recall, to a two-dimensional health snapshot, to a three-dimensional trajectory with causality, and report lessons from operation: self-reported health data are missing not at random, question phrasing governs the quality of synthesized understanding, and nearly a third of candidate causal links are structural noise that rules alone remove.

---


### 182. [KneePreM: Towards 3D Knee MRI Foundation Models via Large-Scale Unlabeled Pretraining and Label-Efficient Fine-Tuning](https://arxiv.org/abs/2609.31461)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xinxin Wang, Liam Hazan, Jing Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Large volumes of unlabeled knee MRI scans are available across repositories but remain insufficiently leveraged. We developed KneePreM, a knee-specific 3D self-supervised model, and evaluated transfer and label efficiency for classification and segmentation. Methods: A 3D U-Net masked autoencoder was pretrained on 19,011 unlabeled Osteoarthritis Initiative (OAI) MRI series from 4,791 participants. Downstream fine-tuning used full and reduced training sets for fastMRI+ two-label classification (1,172 examinations), Arthroscopic Partial Meniscectomy (APM) eight-target classification (1,716 examinations), SKM-TEA segmentation (155 examinations), and APM segmentation (25 examinations). Baselines were random initialization and SuPreM. Deployment workflow was implemented with a Model Context Protocol interface. Evaluation metrics included balanced accuracy, F1 score, ROC AUC, PR AUC, and Dice score. Statistical analysis used bootstrap confidence intervals and paired bootstrap tests for classification and Wilcoxon signed-rank tests for segmentation. Results: KneePreM achieved higher full-data macro ROC AUC than both baselines for fastMRI+ and APM (all p < .001). For fastMRI+ classification, KneePreM achieved a ROC AUC of 0.722 using 50% of the training data, exceeding both full-data baselines. In APM classification, KneePreM reached a ROC AUC of 0.740 with 70% of the data, matching the full-data random baseline and outperforming SuPreM. For SKM-TEA segmentation, its 70%-data Dice of 0.838 exceeded the full-data random baseline (0.835) and both same-budget comparators. In APM segmentation, its 75%-data Dice of 0.746 exceeded the full-data random baseline (0.731) and both same-budget comparators. Conclusion: KneePreM improves transfer performance and label efficiency across knee MRI classification and segmentation tasks, particularly when labeled training data are limited.

---


### 183. [User Model Extraction via Belief Self-Distillation](https://arxiv.org/abs/2609.31603)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ali Holmov, Yiran Huang, Kirill Bykov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) implicitly infer attributes of their users and adapt their behavior accordingly, yet these beliefs remain difficult to inspect and causally manipulate. We introduce Belief Self-Distillation (BSD), a unified read-write framework that bridges linear and causal probing by learning a compact user representation that can be both decoded and written back into the model. The frozen LLM acts as its own teacher, distilling beliefs from natural conversations without external annotations. Unlike conventional probing, BSD isolates not only information present in activations, but a state whose causal role can be directly tested. Across multiple model families, BSD faithfully recovers user beliefs and enables substantially stronger interventions than matched hidden-state steering. Crucially, we find that refusal depends not only on the request, but on the model's inferred user intent: changing this belief alters refusal while holding the request fixed. We further uncover a striking cross-model regularity: independently trained LLMs converge on a shared geometry for representing their users. Together, these results reveal implicit user models as readable and causally writable internal states with direct implications for AI safety, shaping how models condition safety decisions on whom they believe they are interacting with.

---


> [!TIP]
> 当前位于：**151-183**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-183**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
