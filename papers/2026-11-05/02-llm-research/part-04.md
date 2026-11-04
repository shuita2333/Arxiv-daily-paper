# 🧠 大模型相关研究 | 2026年11月05日

> 本类共 **220** 篇论文：已确认 **208** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-220](./part-05.md)

---

### 151. [Reducing Logprob Without Causal Verification: Diagnosing SAE-Based PII Suppression in LLMs](https://arxiv.org/abs/2611.04782)

**<font color=#1a73e8>作者：</font>** Chaerin Lee, Wonho Lee, Sohee Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> SAE-based feature-level interventions to suppress PII leakage in LLMs are primarily evaluated by log-probability reduction. We show that this criterion cannot distinguish feature specific suppression from a magnitude artifact: a direction-agnostic effect of sufficiently large activation perturbations. Across 36 (model, layer, PII type) cases, we compare selected SAE feature interventions with coherencematched random direction controls using logprob and rank-aware metrics. While 17 cases (47%) appear successful under logprob-only evaluation, only 1 case (2.8%) passes our multimetric framework. The rest reveal two failure modes: random directions outperform selected features, and feature selection collapse across PII types. These results indicate that existing evaluations cannot verify whether interventions target causal pathways of PII leakage. A 9,000 run causal mediation feasibility study corroborates this: the verifier separates candidates reliably, but correlation-selected candidates rarely pass it. We therefore propose a new research mission for NLP: causally grounded PII suppression through circuit-level localization and causal mediation analysis.

---


### 152. [Kierston & KierstonBench: Simulation of Allentown, PA and Evaluation of Language Models in Crime Investigation and Surveillance Tasks](https://arxiv.org/abs/2611.04785)

**<font color=#1a73e8>作者：</font>** Andrew Semenov, Svyatoslav Dorofeev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are candidates for collecting and analyzing records in criminal investigations and mass surveillance. Their capability and accuracy in this work cannot currently be measured. Real deployments lack the ground truth needed to score a model's conclusions, and no benchmark evaluates these capabilities in a simulated environment. We present Kierston, a city-scale simulation engine, and KierstonBench, a benchmark that tests these capabilities against known simulated events. Kierston models approximately 125,000 residents of Allentown, Pennsylvania, generating their daily activities and the telecommunications, financial, administrative and license-plate records that surveillance and investigative systems collect about them. These records derive from a common behavioral timeline and are distributed across sources representing separate providers. Models investigate through a restricted records interface, linking observations across sources without access to the underlying simulation. The benchmark comprises 32 task families covering record linkage, routine reconstruction, incident investigation and assessment of deceptive accounts. In an evaluation of sixteen language models, most could not perform records investigation and submitted identifications the records did not support. A small number of frontier models solved most of the tasks and abstained when evidence was insufficient. In some cases these models still fell for common deceptions and assumptions, and none replaced an investigator.

---


### 153. [ReSI-Math: Exploring Recoverable Capability Frontiers for Efficient Reasoning Improvement](https://arxiv.org/abs/2611.04787)

**<font color=#1a73e8>作者：</font>** Yao Cui, Zhen Yang, Yuandong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become an effective approach for improving mathematical reasoning in large language models. However, a fundamental question remains: when a model fails to solve a problem, does it truly lack the underlying capability? In this work, we reveal that direct failure does not necessarily imply inability. Some reasoning failures can be recovered by exploring the model's own trajectories, exposing a recoverable capability frontier: a policy-dependent region where solutions are not reliably generated through direct decoding but can be elicited through trajectory-level search. Based on this observation, we introduce ReSI-Math, a framework that explores recoverable capability frontiers and converts recovered capabilities into data-efficient RLVR supervision. ReSI-Math uses Self-Judge-guided evolutionary search to identify recoverable failures under a fixed policy and adaptively selects frontier problems for sequential RLVR as the policy evolves. On Qwen3-VL-8B, correct-incorrect trajectory crossover produces 272 verifier-confirmed correct offspring from 621 attempts (43.8%). After three sequential one-shot RLVR stages, the MATH500 and WE-MATH average improves from 78.71 to 80.16. Under matched single-problem RLVR, random selection reaches only 53.31 versus 54.16 for frontier-guided Q1.

---


### 154. [Training Specialist LLMs on Your Phone: Forward-Only Optimization via Block-Spectral Coordinates](https://arxiv.org/abs/2611.04797)

**<font color=#1a73e8>作者：</font>** Liyan Tan, Yequan Zhao, Ziyue Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) on personal devices keep user data local, but limited memory restricts their general capability. Since most user-specific tasks do not require the breadth of frontier models, a practical solution is to adapt a shared on-device model into lightweight specialists. However, backpropagation is prohibitive in memory, and users rarely provide labeled data. We present MobileSpec, a system that trains specialists with forward passes alone and learns from automatically checked task outcomes, as in reinforcement learning with verifiable rewards (RLVR). Because forward-only updates are built from random perturbations, training is efficient only when these perturbations resemble the weight changes of RLVR, which largely preserve the singular values of pretrained weights and rotate their singular vectors. The core algorithm of MobileSpec, FuRA-S, produces such perturbations while training only the block-spectral coordinates of pretrained weights, namely the singular values of their column blocks. As we show theoretically and empirically, rescaling these blocks independently shifts their relative contributions to each weight matrix and thereby rotates its singular vectors. Since this update can be rewritten as a transformation of the layer input, FuRA-S also adapts INT4 models without modifying their weights. With specialists of only 1-5 MB that update 0.015-0.05% of the parameters, MobileSpec raises the success rate of a phone-use agent from 6-23% up to 89-100% and trains a personalized 8B model on an iPhone 16 Pro overnight. On RLVR benchmarks, FuRA-S is competitive with full-parameter evolution strategies (ES) and outperforms ES over LoRA adapters and quantized ES on INT4 models.

---


### 155. [Extracting System Prompt of LLM Services in Complex (Agentic) Settings: Hierarchical Optimization and Reliable Evaluation Metrics](https://arxiv.org/abs/2611.04803)

**<font color=#1a73e8>作者：</font>** Shuaidong Li, Chenhao Lin, Xinshan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> System prompt is a critical intellectual property of large language model (LLM) services. To analyze its leakage, prompt extraction attacks have been extensively studied. However, we validate that existing attacks substantially degrade on recent LLM services, whose complexity has evolved in both the prompt itself and system-level constraints. Specifically, (1) system prompts become longer and more structured to contain pre-defined tool schemas, execution logic, safety guardrails, etc., and (2) only the final post-processed outputs (e.g., agent's actions) but not the raw textual response can be observed.
In this paper, we address the above increased complexity by proposing Extraction with Hierarchical Optimization (ExtraHerO), which (1) decomposes the prompt extraction into a hierarchical reconstruction process with a pre-defined structural prompt template, and (2) iteratively updates the adversarial query with guidance of feedback-template differences to observe diverse outputs. In particular, we monitor the information gain of attack optimization to early stop or reset it for a good trade-off between effectiveness and efficiency.
We also find that existing evaluation metrics for prompt fidelity can be misleading because they do not account for structural information. Therefore, we rely on global textual similarity and prioritize structural keywords. Moreover, we introduce a system-level metric, adversarial utility, to measure the help of prompt extraction for real-world downstream attacks. Experimental results demonstrate the consistent superiority of ExtraHerO, with average improvements of 12.5\% (fidelity), 2.3\% (functionality), and 6.0\% (adversarial utility) on chatbots, and 12.2\%, 34.3\%, and 30.5\% on agents.

---


### 156. [Where Is the Truth When AI Agents Disagree? Dependence-Aware Belief Propagation for Unsupervised Truth Discovery (Extended Version)](https://arxiv.org/abs/2611.04805)

**<font color=#1a73e8>作者：</font>** Laure Berti-Equille  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents often give conflicting answers to the same question, and many deployed agents are variants of one base model, so their errors are correlated. We study truth discovery among such agents: inferring the true answer and each agent's reliability without labels. Classical truth-discovery and crowdsourcing estimators reward an agreeing bloc and can fall below majority vote. We propose BP-TD, which adds per-agent decorrelation weights to mean-field variational inference on a one-coin Dawid-Skene model, so that agents sharing a base model count together as about one vote. Its first iteration is exactly a weighted vote; later iterations estimate agent reliability. With 13 local agents on MMLU, BP-TD beats majority vote without any labels (0.716 vs. 0.624 on 160 questions; 0.707 vs. 0.674 on 10,000) and ranks agents by their true accuracy, which classical estimators invert. The gain depends on the pool: over 2,852 sub-pools of four benchmarks, decorrelation helps when the largest correlated bloc is weaker than the other agents and hurts when it is the strongest, and we found no label-free statistic that tells the two cases apart. Labels change the picture quickly: with 20 labelled questions, selecting the single best agent is more accurate than every aggregator we tested on MMLU, ARC and TruthfulQA.

---


### 157. [NightIQA: A Comprehensive Dataset and Benchmark for MLLM-Based Nighttime Image Quality Assessment](https://arxiv.org/abs/2611.04811)

**<font color=#1a73e8>作者：</font>** Yiding Tian, Jiaojiao Yi, Jiayuan Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nighttime images are inherently susceptible to complex, compound degradations, making accurate quality assessment exceptionally challenging. Score-based IQA methods condense quality into a single number, lacking the multi-dimensional, language-grounded reasoning required for nighttime evaluation. Multimodal Large Language Models (MLLMs) offer a more comprehensive alternative, yet remain constrained by a critical data gap: existing real-world IQA datasets are overwhelmingly daytime-centric and often built from outdated captures, while synthetic alternatives lack nighttime-specific degradation modeling, yielding artifacts far removed from authentic nighttime conditions. To bridge this gap, we present NightIQA, a dataset and benchmark suite purpose-built for MLLM-based nighttime IQA. It comprises three core components: NightIQA-Real, a real-world dataset of 1,769 high-resolution images that we captured ourselves with modern equipment, encompassing six canonical distortion types and structured multi-dimensional annotations; NightIQA-Bench, a benchmark of 1,078 visually grounded multiple-choice questions tailored to MLLM-based nighttime IQA, organized around a four-level evaluation hierarchy spanning Perception, Technical Assessment, Localization, and Reasoning; and NightIQA-Syn, an inherently scalable, scene-aware synthesis pipeline that jointly models global-level and instance-level degradations, with an initial release of 80k high-fidelity images alongside the full generation code. Fine-tuned on NightIQA with Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO), Qwen3-VL-8B outperforms open-source IQA methods and achieves higher overall accuracy than leading closed-source models, highlighting the value of domain-specific data and structured supervision.

---


### 158. [The Pen is Mightier than the Pixel: Natural Textual Unlearnable Example for Large Vision Language Models](https://arxiv.org/abs/2611.04817)

**<font color=#1a73e8>作者：</font>** Chenyu Yi, Jiawen Zong, Sami Hormi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The proliferation of Large Vision Language Models (LVLMs), trained on vast and often sensitive datasets, raised concerns regarding data privacy and unauthorized usage. Unlearnable Examples (UEs), which subtly perturb training data to mislead the models, have emerged as a promising defense method. This paper presents the first exploration of UEs specifically on LVLMs, which poses unique challenges due to their inherent multimodal nature. We propose a novel text-based perturbation method, Natural Textual Unlearnable Examples (NTUE), which can effectively mislead LVLMs by subtly manipulating the image label, establishing a shortcut between an identity of interest and a separate target, without introducing factual misinformation or affecting readability. Comprehensive experiments compared with traditional UE methods demonstrate the superior performance of NTUE. Our findings show that NTUE achieves a high success rate with a poison rate as low as 5%, underscoring its potential as a practical and robust solution for protecting multimodal data in the era of LVLMs.

---


### 159. [AI for eGovernance: Leveraging Language Technologies For Digital Inclusion](https://arxiv.org/abs/2611.04820)

**<font color=#1a73e8>作者：</font>** Cynthia Jayne Amol, Lilian Wanzare  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Kenyan government has invested heavily in the digitisation of public service delivery, in line with the Kenya Digital Master Plan 2022-2032. The national eGovernment platform, eCitizen, hosts services that are vital to citizens' livelihoods, including business registration, youth enterprise lending, digital literacy and tax filing. However, the platform faces digital inclusion challenges that limit equitable access for marginalised groups, particularly youth in rural areas and persons with disabilities. This exclusion is driven by a language barrier, since the platform is primarily in English with limited Swahili support, and by a text-only interface that excludes low-literacy and visually impaired users. This paper reports findings from six one-on-one interviews and an eleven-person roundtable discussion across four platforms essential to youth livelihoods: Ajira Digital, Kenya Revenue Authority (KRA) iTax, Higher Education Loans Board (HELB) and the Youth Enterprise Development Fund (YEDF). Drawing on these findings, on Web Content Accessibility Guidelines (WCAG) 2.1 principles as a design lens for diagnosing eCitizen's accessibility gaps, and on comparator models such as Estonia's Bürokratt and India's Bhashini, the paper proposes a human-centred, systems-minded framework for embedding generative AI and language technologies into eCitizen, including text simplification, neural machine translation, text-to-speech and speech-to-text. The paper argues that, when deployed responsibly with appropriate human oversight, these interventions could meaningfully improve access to government services for linguistically excluded citizens. It also emphasises that AI alone cannot overcome the broader structural barriers, including unemployment and educational inequality, that shape digital exclusion.

---


### 160. [Feeling of Knowing in Large Language Models](https://arxiv.org/abs/2611.04834)

**<font color=#1a73e8>作者：</font>** Zichuan Fu, Xian Wu, Jingtong Gao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training updates change what large language models (LLMs) can answer, but may leave their answerability judgments misaligned. We study this knowledge-judgment desynchronization through functional feeling of knowing (FoK), which supports selective generation, retrieval triggering, and model routing without implying subjective experience. We propose two trainable channels: a knowledge channel that changes answerability and a FoK channel that judges the current knowledge state. Three stages train them: on-policy supervised fine-tuning (OP-SFT) updates knowledge from corrected on-policy answers; knowledge-delta FoK training (K$\Delta$-FT) adapts judgments across intermediate knowledge states; and FoK-guided policy optimization (FGPO) trains the subsequent answer or explanation. Factual-QA experiments, cross-dataset evaluation, and three sequential updates show that explicit FoK alignment improves judgment quality on updated knowledge. MMLU and ARC-Easy separately assess capability preservation.

---


### 161. [Amortized Nonlinear Variable Selection with Prior-Data Fitted Networks](https://arxiv.org/abs/2611.04848)

**<font color=#1a73e8>作者：</font>** Jin Zhu, Junxian Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Variable selection is an important task for interpreting potentially complex systems in fields such as biology, business, and sociology. The importance of variable selection has attracted considerable attention in statistics and machine learning. In this paper, we are mainly interested in model-agnostic variable selection for identifying variables that have general nonlinear dependence on the response. We propose MambaPFN, short for Model-Agnostic Markov BlAnket selection with Prior-data Fitted Networks, which is built upon the Transformer, a building block of many popular large language models. Specifically, we consider a functional-mapping perspective on variable-selection learning, in which the Transformer is treated as a learnable mapping from a dataset to its relevant variables. To learn this mapping, MambaPFN introduces three new components: (i) a faithful, rich, and scalable scheme for generating pretraining data, (ii) an objective that targets each variable's posterior inclusion probability, and (iii) a modified Transformer architecture tailored to variable selection. Once pretrained, MambaPFN is applied to new datasets without parameter updates. Empirically, MambaPFN achieves desirable variable-selection performance in simulation studies and exhibits a scaling law---more pretraining datasets and larger models can continuously improve its performance. Applied to a Facebook comments dataset, MambaPFN selects the fewest variables and achieves the highest computational efficiency and predictive performance, improving upon the best baselines by about 20%.

---


### 162. [OCR in the Foundation Model Era: From Specialist Models to Unified Models](https://arxiv.org/abs/2611.04874)

**<font color=#1a73e8>作者：</font>** Zhiheng Li, Zongyang Ma, Jiaxian Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Character Recognition (OCR) is among the oldest and most widely deployed applications of artificial intelligence. This survey reviews its development, focusing on the Foundation Model Era. We define OCR through faithful transcription: within a specified visual scope, OCR should completely reconstruct the text, notation, and document structure observable in the source image, and every textual, notational, or structural element in the output must be verifiable from visual evidence in that image. We trace the development from specialist OCR models toward unified models, examining joint text detection and recognition, structured sequence generation, and the use of pretrained vision-language models (VLMs). We organize contemporary OCR systems into five coexisting families: modular toolkits and task-specific models, specialized document VLMs, hybrid workflows, general-purpose VLMs, and commercial products and managed services. We compare their architectures, data, and training, examining hallucination and omission, insufficient spatial grounding, and inference cost in generative OCR. We review evaluation from character and scene text recognition to parsing individual structural elements and full-page transcription, highlighting gaps in consistent output definitions, attribution of performance to individual components, and coverage of real capture conditions and visible content and structure. Finally, we summarize the challenges facing OCR and discuss directions for future research. We continuously track related work at this https URL.

---


### 163. [TraceRouter++: Causal Semantic Routing Realignment via Optimal Transport](https://arxiv.org/abs/2611.04878)

**<font color=#1a73e8>作者：</font>** Chuancheng Shi, Shangze Li, Wenhua Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite their remarkable capabilities, large foundation models (LFMs) remain susceptible to adversarial manipulation. Current safety intervention methods primarily rely on the \textit{locality hypothesis}, rigidly suppressing isolated neurons or features. However, harmful semantics manifest as distributed, cross-layer circuits, rendering localized ablations both brittle against complex jailbreaks and detrimental to general utility. To bridge this gap, we propose TraceRouter++, a routing-level safety intervention framework that explicitly traces safety-relevant causal routing pathways activated under harmful inputs and realigns their unsafe activation states. Our framework operates in a \textit{Discover-Trace-Realign} paradigm: it first pinpoints a sensitive onset layer via attention divergence and disentangles dense activations into interpretable routing features using sparse autoencoders (SAEs). Subsequently, it maps these features to downstream causal circuits via feature influence scores (FIS). Crucially, departing from rigid suppression paradigms, TraceRouter++ introduces a constrained optimal transport (OT)-based soft routing realignment. By formulating safety intervention as a tractable coordinate-wise marginal optimal transport approximation, our method redirects unsafe activation marginals toward safe-reference marginals within causally identified routing subspaces while preserving non-selected coordinates at the intervention point. This mechanism safely redirects malicious semantic flows while leaving orthogonal computational routes intact. Extensive experiments across representative large language models (LLMs), multimodal large language models (MLLMs), and diffusion models (DMs) show that TraceRouter++ outperforms evaluated baselines, improving adversarial robustness while maintaining a favorable safety-utility trade-off. WARNING: This paper contains unsafe model responses.

---


### 164. [ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud](https://arxiv.org/abs/2611.04879)

**<font color=#1a73e8>作者：</font>** Yutao Wu, Xiao Liu, Ming Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web agents increasingly browse, shop, and manage accounts on behalf of their users. Prior work has shown that they can be misled by adversarial content, including prompt injections and deceptive interfaces. Beyond such attacks, agents operating on the open web also encounter online fraud designed to deceive humans, including fraudulent online stores, fake investment platforms, and advance-fee schemes. How web agents respond to such fraud during task execution remains underexplored, in part because scam websites are short-lived, making systematic evaluation difficult. To address this gap, we introduce ScamWorld, an interactive environment that reconstructs reported scam websites across diverse scenarios, fraud mechanisms, and languages. Each reconstructed website reproduces documented fraud mechanisms, making relevant signs of fraud observable before the agent's final action and enabling controlled, repeatable evaluation. Through an extensive study of web agents powered by six frontier LLMs, we find that baseline deception rates range from 11% to 35% across models. Agents proceed more readily with payments than with requests for credentials or wallet information. A closer analysis of agent trajectories shows that some agents acknowledge suspicious conditions yet proceed, at times treating the user's instructions as authorisation to accept additional terms imposed by the website. ScamWorld provides a reusable testbed for systematically evaluating and stress-testing web agents against real-world online fraud.

---


### 165. [Modelling lock-in of AI adoption through skill erosion](https://arxiv.org/abs/2611.04886)

**<font color=#1a73e8>作者：</font>** Renaud Lambiotte  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI can improve immediate performance but may erode the human skills required for future work. We study a model in which individuals tend to imitate successful peers, while their independent skills grow with practice and erode with reliance on AI. Because each agent's skill reflects their history, non-users and AI users develop different skill distributions, which we derive exactly. Skill erosion can produce bistability and hysteresis between a low-adoption, high-skill state and a high-adoption, low-skill state. When agents rarely change behaviour at random, the two transitions are asymmetric. A single AI user spreads through a population of experts only if AI-assisted work earns more than expert work, whatever the timescale of skill adaptation. A single non-user, by contrast, can lead an AI-dependent population back to independent work only if they regain enough skill before returning to AI, which becomes easier the more persistent behaviours are. As AI improves, adoption can jump abruptly, and a sufficiently long increase in its benefit, such as a period of low prices, can leave a population relying on AI after the benefit has returned to its initial value. Skill erosion thus creates a history-dependent switching cost that can make widespread AI adoption difficult to reverse.

---


### 166. [Heads That Write, Not Just Point: Image Retrieval Heads in Vision-Language Models](https://arxiv.org/abs/2611.04903)

**<font color=#1a73e8>作者：</font>** Junsung Park, Sangwon Yu, Donghun Kang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) can process interleaved text and multiple images in a single context, but how they internally identify the image relevant to a question remains poorly understood. We study this grounding step as in-context image retrieval and introduce ICIR-MCQ, a controlled probe for head-level analysis of image retrieval. Using each head's attention mass over image-token spans, we first identify sparse pointer heads that reliably point to the target image. These heads transfer beyond the probe: a single pointer head is competitive with external vision-language retrievers on a naturalistic multi-image retrieval benchmark, showing that LVLMs contain a strong internal image retrieval signal. Attention alone, however, shows where a head reads from, not what its output passes on to later layers, so we introduce a complementary output-side analysis. For each head, we train a lightweight image retriever on its value-weighted output and use it to identify writer heads, whose outputs contain enough information to identify the target image. Surprisingly, the pointer and writer criteria select substantially different head sets, with only 35 to 47 heads overlapping among the top-100 heads under each criterion. Targeted set-partition ablations show that the heads most important for standard multi-image inference are concentrated in this pointer-writer intersection, while heads selected by only one criterion show less consistent separation from random-head controls. The most consistent causal effects arise from heads selected by both the attention-based pointer and output-side writer criteria. Code and data: this https URL.

---


### 167. [Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling](https://arxiv.org/abs/2611.04916)

**<font color=#1a73e8>作者：</font>** Kling Team, Dong Chen, Jialu Chen 等 53 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation has progressed from isolated clips to coherent short-form audiovisual sequences, and the bottleneck is shifting from rendering to semantic control. This report summarizes the observations and insights on multimodal understanding gained from successive generations of Kling. We argue that generation quality is the projection of multimodal understanding through the entire data--conditioning--alignment--evaluation chain, and we examine this chain module by module. Kling-MLLM, a shared multimodal foundation model that unifies image, video, audio, synchronized audio--video, and interleaved inputs, is specialized for each downstream module. Because a DiT is trained on far fewer training samples than a language model, we treat captioning as a semantic contract that maximizes description density, and extend it to reference-grounded captioning that makes reference bindings explicit. Prompt enhancement translates user intent into this caption distribution: basic PE is derived from captions of compelling videos and refined with text-level and generator-in-the-loop reinforcement learning, while agentic PE refines the story and retrieves compelling examples. We show that a reliable text encoder comes from perceptual training rather than from stronger language ability, and that candidates can be screened from text alone before end-to-end training. Reward modeling pairs a general reward model for explainable, localized critiques with a decision reward model for fast multidimensional scoring, treating perceptual bandwidth as a first-class design parameter. Finally, we review task-specific automatic evaluation, focusing on protocols that expose scoring shortcuts and help trace failures to their upstream source. We hope these lessons offer practical guidance for building the understanding stack behind controllable video generation.

---


### 168. [PROSE: Preservation-Constrained Selective Editing for Guilty Bias in Legal Judgment Prediction](https://arxiv.org/abs/2611.04921)

**<font color=#1a73e8>作者：</font>** Yimeng Wang, Zeyuan Tian, Xinyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal judgment prediction models may retain a guilty verdict after a legally decisive condition has been altered such that the specified charge is no longer established. We study this guilty bias via selective repair over matched charge-established and charge-not-established cases, where the unsupported verdict should change while its supported counterpart remains stable. We construct CAIL-MC, a legally reviewed dataset of 11,478 matched pairs covering 261 Chinese criminal charges. Held-out activation interventions show that contrasts learned from correctly resolved pairs transfer to false-guilty cases, but target-reaching interventions can also damage matched supported-guilty decisions. Motivated by this observation, we introduce PROSE, which reconstructs case-specific targets from a training-derived residual geometry, aligns them with a local margin-descent signal, attenuates supported-guilty-sensitive components, and realizes bounded targets through a preservation-regularized low-rank parameter update. Across Qwen3-8B and GLM4-9B, PROSE achieves stronger pairwise safe repair and evidence sensitivity, while preserving standard single-pass inference.

---


### 169. [Residual Attribute Leakage Is an Interface: Auditing Privacy Evaluation After Text De-identification](https://arxiv.org/abs/2611.04941)

**<font color=#1a73e8>作者：</font>** Tuan Thanh Duong, Joongmin Shin, Jeongho Yoon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A privacy evaluation of de-identified text asks a language model (the adversary) to guess a person's protected attribute. We introduce a prior-normalised clipped leakage score of its confidence gain on the true value and audit the conclusions drawn from it. Each verdict depends on an evaluation interface (the queried person, answer options, prior, adversary model and scoring rule), which we vary on fixed releases of three corpora. In a stress test, an editor that writes the opposite-sex form at the same spans a redaction editor would redact misleads the adversary about most people, yet ranks first among editors scored on the same MedQA entries under this score, as under attack accuracy and proper scoring rules read as privacy. A relabelling-invariant reading of AUC ranks that editor sixth of eight, and a rule-aware adversary recovers the attribute from the same text. On ordinary releases most verdict changes are gains or losses of separability; of six choices varied over all pairs, only the adversary reverses comparisons (5 of its 124 changes), and the query can target the wrong person. SACC, a traceable editor we build as the instrument, lets us ablate two editing principles and show where its advantage does not hold.

---


### 170. [Learning Where to Look: Observation Policy Optimization for Thinking with Images](https://arxiv.org/abs/2611.04943)

**<font color=#1a73e8>作者：</font>** Junfeng Wang, Jiawei Liu, Yongchao Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complex visual question answering often requires vision-language models to think with images, i.e., actively acquire local visual evidence by zooming into informative regions of high-resolution images. Our error analysis shows that many failures in this setting originate from incorrect observation actions, where the model fails to localize key regions or obtain crops that contain sufficient evidence for answering. We further observe that bounding-box tokens exhibit substantially higher generation entropy than ordinary language tokens, indicating high uncertainty when the model decides where to look. However, existing reinforcement learning methods based on final-answer rewards provide only trajectory-level feedback, making it difficult to assign precise credit to the observation actions. We propose Observation Policy Optimization (OPO), an RL algorithm for optimizing observation actions in tool-augmented thinking with images. OPO consists of two core modules. First, Uncertainty-Guided Observation Branching (UOB) treats each image zoom-in tool call as an observation event and selectively branches at high-uncertainty, low-redundancy events during rollout, enabling efficient exploration of alternative cropping decisions and their resulting visual evidence. Second, Evidence-Localized Advantage Attribution (ELAA) compares sibling branches using local evidence-sufficiency rewards and assigns credit only to the corresponding observation-action tokens. By decoupling observation-action optimization from trajectory-level outcome supervision, OPO improves visual evidence acquisition and further enhances visual reasoning performance. Experiments show that OPO consistently improves Qwen3-VL models across scales and achieves competitive performance against larger models and tool-augmented baselines. Code is publicly available.

---


### 171. [PATTS: Parallel-Aware Test-Time Scaling for Thought-Image Generation in Multimodal Discrete Diffusion LLMs](https://arxiv.org/abs/2611.04948)

**<font color=#1a73e8>作者：</font>** Yasong Dai, Zeeshan Hayder, David Ahmedt-Aristizabal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time scaling (TTS) improves generative models by allocating additional inference-time computation to sampling, search, and verification. Existing image generation approaches, however, typically rank completed images or image-centric intermediate states. We study TTS for parallel multimodal discrete diffusion language models, in which reasoning tokens and image tokens are decoded jointly within a single generation trajectory. We first diagnose a limitation of conventional final-image selection: on GenEval, a CLIP-style image-prompt score is weakly aligned with within-prompt compositional correctness, leaving substantial headroom between verifier selection and oracle selection. We then propose PATTS, a novel parallel-aware TTS framework that searches over intermediate thought-image states using cross-modal verifier signals. PATTS uses a state-dependent reliability weight, derived from model-internal trajectory diagnostics, to modulate the influence of external semantic verification during generation. In the fixed N=32 evaluation on MMaDA-Parallel, the PATTS reaches a GenEval score of 0.844, compared with 0.628 without TTS, 0.787 for Best-of-N, and 0.810 for FKD. These results show that reliability-aware trajectory verification can improve test-time selection for parallel thought-image co-generation under the evaluated search budget. Our code release is at this https URL

---


### 172. [HERIT: Enabling Global Access to Hanja-to-English Historical Translation by Mitigating Temporal Bias](https://arxiv.org/abs/2611.04949)

**<font color=#1a73e8>作者：</font>** Dayeon Jeong, Kyeongpil Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Historical archives are invaluable for multidisciplinary research but remain inaccessible globally due to severe language barriers. While manual translation is prohibitively expensive and time-consuming, simply applying existing machine translation models is inadequate due to unique linguistic nuances and the temporal bias inherent in scarce human-labeled corpora. To address these challenges, we propose HERIT, a systematic domain-adaptation pipeline that leverages retrieval-augmented generation (RAG) to generate high-quality pseudo-labeled data from abundant Hanja-Korean corpora. This approach substantially expands the training dataset, mitigating both data scarcity and temporal overfitting across different historical periods. Extensive automated and human evaluations demonstrate that HERIT consistently outperforms baselines. Finally, we translate previously untranslated portions of the archives using our model, thereby enabling global access to these resources for researchers.

---


### 173. [Shuffled OPSD: When Semantic Consistency Hurts On-Policy Self-Distillation?](https://arxiv.org/abs/2611.04958)

**<font color=#1a73e8>作者：</font>** Qingyuan Zheng, Zhihao Dou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation improves a student model's reasoning ability through supervision from a teacher. On-policy self-distillation (OPSD) uses the same model as both teacher and student under different contexts: the student generates reasoning trajectories from the question alone, while the teacher additionally receives a complete worked example and provides token-level supervision along those trajectories. Because the problem statement is shared, its content and ordering shape both student generation and teacher feedback. Preserving its semantic structure therefore seems natural, but does it always improve learning? We introduce Shuffled OPSD, which shuffles the words of the shared problem statement while keeping the teacher-only worked example intact. Across three mathematical reasoning benchmarks and three Qwen3 model scales, the method improves mean accuracy over both an intact-target control and Standard OPSD under matched training configurations. The largest gain over Standard OPSD is 3.52 percentage points on Qwen3-1.7B. Further controls show that preserving larger word blocks offers no advantage over word-level shuffling at the evaluated scales, whereas shuffling the teacher-only worked example reduces accuracy at every scale. Cross-problem mixing and target-removal experiments further distinguish the roles of problem content, word order, and teacher context. These results show that disrupting the shared problem statement can improve learning, while disrupting the teacher-only reference hurts performance. They challenge semantic coherence as a universally beneficial principle for OPSD and motivate closer study of how input structure shapes student generation and teacher supervision.

---


### 174. [An Agentic Framework for Quality-Aware and Scenario-Adaptive Image Compression](https://arxiv.org/abs/2611.04960)

**<font color=#1a73e8>作者：</font>** Zhenghao Chen, Lebin Zhou, Zicong Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite decades of progress, image codecs remain difficult to adapt to diverse real-world compression scenarios for two main reasons. First, most image codecs are optimized for a specific objective and require substantial redevelopment when the compression goal changes. Second, they typically assume clean inputs, whereas sensor-captured images often contain degradations that alter rate-quality behavior. To address these challenges, we propose Practical Image Coding Agents (PICA), a multi-agent framework that adapts existing codecs to diverse user requirements and potentially degraded inputs. PICA consists of four collaborative agents: a Perception agent that interprets user intent and analyzes image content, an Improvement agent that jointly considers bitrate and reconstruction quality to guide pre-coding restoration, a Coding agent that refines quality-control settings from global to regional levels, and an After-coding improvement agent that addresses residual degradations and compression-induced artifacts through restoration guided solely by image quality. To enable codec-agnostic regional adaptation, we introduce Agentic ROI Coding (AROIC), which treats the codec as a black box and allows the agent to automatically schedule, execute, evaluate, and reflect ROI coding plans without architectural modifications or codec-specific retraining. We integrate these four agents with a Scenario-Guided Quality-Rate (SGQR) evaluation strategy to enable more effective scenario-adaptive compression across heterogeneous codecs. Comprehensive experiments on clean, noisy, and blurred images across standard, perceptual, and machine-vision compression scenarios demonstrate that PICA consistently enhances the compression performance of both the conventional H.266/VVC codec and the neural Cheng2020 codec, outperforming competing compression methods on the Kodak, CLIC2020, and HEVC datasets.

---


### 175. [Who is the Pronoun Pro? Comparing LLMs and Humans at Number-Disambiguation of 'they'](https://arxiv.org/abs/2611.04968)

**<font color=#1a73e8>作者：</font>** Carlos Hartmann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study evaluates whether large language models (LLMs) can reliably replace or complement human research assistants in linguistically complex annotation. In a controlled annotation task, 73 human annotators (local students and crowdworkers with and without a background in linguistics) and more than 40 LLM configurations number-disambiguated 174 authentic uses of 'they' from Reddit, including innovative and context-sensitive cases. The best LLM, Kimi K3, reached 94.5% accuracy, above the human majority vote (86.2%) and the mean of the top half of human annotators (78.5%); only the single best human annotator scored higher (95.7%). LLMs also offer substantial practical advantages in cost and speed. However, qualitative error analysis reveals a crucial complementarity: human reasoning in low-agreement cases exposes inconsistencies in the annotation typology and thereby improves the methodological framework itself. The study contributes (i) a benchmark-style human-LLM comparison for a semantically demanding task, (ii) transparent cost and time evidence, and (iii) a methodological argument against a purely replacement-oriented view of automation. LLMs are viable for large-scale annotation support in linguistics, but their responsible use requires human critical oversight. The dataset with its gold-standard labels, all human and LLM annotations, and the fully reproducible code are openly available as a Quarto-based, public repository.

---


### 176. [GeoFaham: Domain-Specialized Multi-Agent Geospatial Analytics for Disaster Response](https://arxiv.org/abs/2611.04977)

**<font color=#1a73e8>作者：</font>** Muhammad Sohail Danish, Gilles Q. Hacheme, Akram Zaytar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Real-world geospatial decision support requires more than single-step retrieval or code generation. Disaster-response questions often involve multi-source workflows that combine spatial databases, map-derived features, satellite imagery, raster products, and reusable geospatial artifacts, where correctness depends on preserving spatial scope, temporal context, and intermediate execution state. While large language models and coding agents offer a promising interface for such workflows, they struggle with geospatial-specific failure modes, including handling large artifacts, selecting the wrong evidence source, losing spatial or temporal metadata, and applying invalid geometric operations. We introduce GeoFaham, a domain-specialized multi-agent system for geospatial disaster analytics. GeoFaham decomposes workflows into specialist agents for vector operations, map feature retrieval, imagery discovery, and raster analysis, coordinated by an Orchestrator with a dual-ledger control loop for dependency-aware planning, progress tracking, validation, and replanning. To support artifact-centric collaboration, GeoFaham uses a Response Store that persists full geospatial outputs and typed metadata outside the LLM context window while agents exchange compact identifiers and summaries. We also introduce GeoFaham-Bench, a 40-task benchmark grounded in 17 real-world disaster records, designed to evaluate multi-step geospatial reasoning, cross-source integration, raster-vector computation, artifact generation, and recovery under non-rigid ground truth. We evaluate GeoFaham on GeoFaham-Bench against strong general-purpose coding-agent baselines, including Codex, Claude Code, and OpenCode. GeoFaham achieves the best overall performance, scoring 0.940 versus the next-best 0.879, while using 7.5 times fewer tokens. Our code and benchmark are publicly available at this https URL.

---


### 177. [Auditing Multi-Proxy Explanations of Web User Preferences: Identification Boundaries and Abstention](https://arxiv.org/abs/2611.04997)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Zhihan Wang, Yuhang Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Web systems infer user preferences from behavior, ratings, text, and LLM-generated profiles, yet explaining a proxy may reveal its measurement process rather than the preference of interest. We develop an audit framework distinguishing point identification, partial identification, and abstention relative to an explicit reference distribution. Under feature-dependent, arbitrarily signed proxy bias, a strict majority of uncontaminated proxy attributions lets the coordinatewise median recover latent-attribution support and direction and, with externally justified positive scales, magnitude. We prove this threshold sharp using response-valid indistinguishable worlds, characterize sharp minimax error and exact compatible-target sets under approximate cleanliness and scale uncertainty, and propagate clean-proxy attribution error. A frozen known-truth benchmark spans two response families, four proxy counts, all contamination counts, three bias strengths, and eleven methods, with a focal comparison confirmed on twenty unseen seeds. Under correct budgets, a direct attribution-tensor audit achieved 100% coverage, 95.40%-97.05% active-driver sign decisions, and no false signs. In a temporally separated Amazon study, median aggregation reduced comparator-relative conditional sign error for all four targets; six of eight prespecified target-metric contrasts had Bonferroni intervals excluding zero. A controlled real-covariate perturbation favored the median on the prespecified focal metric for all four targets. Compatible sets showed that the current proxy configuration rarely licensed strict-sign conclusions. Weak comparator calibration limits the Amazon evidence to fitted-surface alignment rather than latent-preference recovery.

---


### 178. [Unifying and Beyond the Theory of Pervasive Capability Degradation in LLM Post-training SFT from Feature Interference](https://arxiv.org/abs/2611.05003)

**<font color=#1a73e8>作者：</font>** Hang Chen, Jiaying Zhu, Wenya Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pervasive Capability Degradation (PCD) refers to the phenomenon in which supervised fine-tuning (SFT), while adapting a large language model (LLM) to a target task, often erodes the general capabilities acquired during pre-training. Prevailing explanations attribute PCD to macroscopic distribution shift and therefore lack microscopic manipulability, leaving existing mitigation methods without a complete theoretical foundation. In this paper, we first develop a bottom-up geometric theory of PCD grounded in feature interference under superposition: narrow-domain SFT data disrupt the almost-orthogonal feature structure formed during pre-training, and the resulting interference drives activations across decision hyperplanes in the output Laguerre-Voronoi geometry, flipping predictions on general tasks. This theory unifies existing methods into six paradigms and reveals both the source of their efficacy and their theoretical limits. We then prove that cross-entropy under one-hot supervision cannot resolve PCD on its own, and accordingly propose the AEGIS loss, which directly constrains the drift of activation margins along all competing token directions, thereby decoupling interference suppression from task adaptation. Across 3 model families and 14 SFT tasks, AEGIS outperforms representative methods of every paradigm on target tasks and pervasive capabilities simultaneously, at only about 1.3 times the computational cost of standard SFT. Its generality, scalability, and mechanistic interpretability offer a new perspective on fully resolving PCD.

---


### 179. [Whose Effect Is It? How Objectives Inflate Learned Subspace Interventions](https://arxiv.org/abs/2611.05033)

**<font color=#1a73e8>作者：</font>** Toygar Tanyel, Serkan Ayvaz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpretability often locates concepts by copying part of a language model's state from one input into another (activation patching). A larger output change counts as stronger evidence that this part carries the concept. Methods that learn which part to copy often change the output more than the whole state does. By that reading, learned parts isolate the concept more cleanly. Yet the whole contains the part. So whose effect is this excess, the network's or the method's? Copying the whole state learns nothing, so it shows what the network produces. We prove that, to first order, the effects of orthogonal parts add up to that of the whole. A part therefore exceeds the whole exactly when the rest moves the output back, which does not require isolating the concept more cleanly. Objectives that reward a larger effect select such parts. Distributed alignment search with cross-entropy, for example, exceeds the whole-state copy just before the output on almost all tasks, and inside the network at most sites. In both, changing only its objective to target what the network produces removes most of the excess. It therefore comes largely from the objective, so a larger learned effect alone is not stronger evidence.

---


### 180. [ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents](https://arxiv.org/abs/2611.05036)

**<font color=#1a73e8>作者：</font>** Guanting Dong, Zhichao Sun, Xinyu Yang 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are deployed as long-horizon agents that compose diverse tools across MCP services into executable workflows. Existing MCP environment-scaling methods are data-centric: they first synthesize a database and scenario, then derive tools and tasks from them. As a result, tool interfaces may not match real ones, tool compositions are not grounded in execution, and tasks rarely span more than one environment. We propose ToolSpace, a tool-centric framework that reverses this order. ToolSpace mines data, state, and retry dependencies from adjacent calls in execution traces of real MCP services and open agent corpora, using deterministic rules rather than LLM judgment, and clusters the resulting weighted tool-composition graph into environments. Databases are synthesized only for state-mutating environments, while query and stateless tools replay recorded returns. ToolSpace then performs state-aware random walks with rollback and decompiles each chain into a natural-language task with assertion-based checks, keeping only samples that replay successfully from the initial state. Applied to AutomationBench and tau3-Bench Banking, the pipeline produces harder Pro versions on which 7 frontier models drop by up to 38.2 points. Across seven long-horizon tool-use benchmarks, ToolSpace raises Qwen3.6-35B-A3B from 23.0 to 41.0 average score (43.2 with RL) and GLM-5.2 from 44.6 to 56.6, on par with Claude Opus 5. Ablations show that execution-witnessed edges clearly outperform LLM-judged ones, and performance keeps improving with data and environment scale.

---


### 181. [ALBI: LLM-Guided Inductive Logic Programming via Iterative Generate-Test-Constrain Refineme](https://arxiv.org/abs/2611.05039)

**<font color=#1a73e8>作者：</font>** Aboubaker Seddiq Benterki, Jüri Vain, Gert Kanter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce ALBI (Agent for Learning By Induction), a neuro-symbolic ILP framework that replaces the ASP-based hypothesis generator in the Learning from Failures (LFF) paradigm with a Large Language Model (LLM), while retaining SWI-Prolog as a formal verifier. ALBI implements an iterative generate-test-constrain loop: the LLM proposes candidate hypotheses from structured prompts; Prolog tests each candidate; and diagnostic feedback drives refinement. We further introduce semantic anonymization, a metamorphic testing methodology, to distinguish structural symbolic induction from surface-level pattern matching on predicate names. Experiments on 30 standard ILP benchmarks show that ALBI achieves 100% success across three frontier LLMs (Gemini 3.1 Pro, GPT 5.4 Pro, Claude Opus 4.6), matching Popper while requiring only 1.4-1.7 iterations on average. Under anonymization, all models maintain 100% success with a moderate iteration increase (1.36-1.67 times), providing evidence of robust symbolic reasoning.

---


### 182. [VIGOR: Visual Gain Ordering for Hallucination Mitigation in Multimodal Discrete Diffusion Language Models](https://arxiv.org/abs/2611.05066)

**<font color=#1a73e8>作者：</font>** Junzhe Chen, Tian Qin, Eugenie Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal discrete diffusion language models (dLLMs) generate responses through iterative mask prediction and offer a promising alternative to autoregressive large vision-language models. However, they still suffer from hallucination, producing outputs that are plausible under language priors but insufficiently grounded in the image. We argue that hallucination in multimodal dLLMs is not only a token prediction problem, but also a premature commitment problem: during iterative denoising, some masked positions are unmasked too early because their confidence is driven more by language priors than by visual evidence, and these early commitments can bias later generation. To address this issue, we propose Visual Gain Ordering (VIGOR), a training-free and plug-and-play inference strategy that reorders masked positions according to counterfactual visual evidence. At each denoising step, VIGOR compares the confidence of each candidate token under the original image-conditioned pass and an additional visual-ablation pass, and prioritizes positions whose predictions are more strongly supported by the image. Experiments on LLaDA-V and Lumina-DiMOO show that VIGOR consistently reduces hallucination and improves multimodal reasoning performance across benchmarks. Code is available at this https URL.

---


### 183. [LatentTriad: Pre-Action Risk Representations for Malicious Agent Skill Detection](https://arxiv.org/abs/2611.05088)

**<font color=#1a73e8>作者：</font>** Zhe Yu, Yi Liu, Ying Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly extended with reusable skills, but untrusted skill content can induce operations outside the user's task. Detecting this contextual risk requires more than suspicious-pattern matching, while dynamic analysis incurs the cost of skill execution. We find that hidden states formed during prefill contain readable information about task-operation consistency, including across held-out expression forms in controlled evaluations. Matched Operation-state interventions also affect later Boundary states and shift fixed risk readouts toward the donor label. Based on these findings, we introduce LatentTriad, which combines contextual Boundary features, group-adjusted Operation directions, and departures from benign state relationships. All branches share one prefill: detection generates no output tokens, invokes no tools, and executes no skill code. Across 5,830 skill packages from five sources and seven backbones, LatentTriad achieves 99.0-99.2% pooled F1 and 93.0-94.6% source-macro F1. A separately measured compact implementation completes prefill and detection in a median of 259-284 ms. These results connect pre-action risk readability and functional influence to execution-free skill screening.

---


### 184. [The Right Source Is Not Enough: Understanding History Interference in Speech-LLM Memory](https://arxiv.org/abs/2611.05124)

**<font color=#1a73e8>作者：</font>** HongJin Song, Weiqiao Shan, Runwu Shi 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech large language models retain audio history to support multi-turn conversations. Yet remembering an event does not ensure that its information is used only when relevant. We investigate why irrelevant historical audio changes answers even when the queried event remains represented. Controlled experiments on MOSS-Audio and MiMo-Audio show that historical values direct errors toward specific competing answers, beyond a generic effect of context length. Causal interventions distinguish two paths. In open-ended question answering, most history-value errors disappear when subsequent computation cannot directly access the irrelevant source. In multiple-choice answering, many errors persist: early historical influence is carried by question-candidate states even after direct source access is blocked. Low-dimensional interventions further separate source-role information from answer-value information. Their effects peak at different depths, and changing the source-role signal does not eliminate the causal influence of competing values. On naturally occurring errors, strengthening the queried role and counteracting the historical value each improve answers; their joint intervention gives the greatest recovery. These findings support a failure of downstream evidence use beyond source identification alone: source-role information can influence a decision without exclusively controlling which historical values affect it. Reliable conversational memory therefore requires not only retention and retrieval, but also control over how retained information enters answer computation.

---


### 185. [From Opinions to Commitments: Unstable Assignments and Silent Choices in AI-Mediated Proposals](https://arxiv.org/abs/2611.05135)

**<font color=#1a73e8>作者：</font>** Sachit Mahajan, Javier Argota S{á}nchez-Vaquerizo, Arthur Capozzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly being used to turn citizens' opinions into collective proposals. These proposals can make assignments: who should act, what must be done, how much one should spend and by when. However, if the assignments change when the same opinions are processed again, publishing a single proposal can hide alternatives that participants never get to see. We examined this issue in four LLM mediators (three open-weight and one commercial) using opinions from DeliberationBank and Polis. For each task, a mediator drafted a proposal from thirty opinions five times, varying either the random seed or the order of the opinions. In 17% of five-run sets from the open-weight mediators and 20% from the commercial one, some runs contained assignments while others did not. Reordering the opinions changed the assignments almost as often as replacing them with opinions from different citizens. Three human annotators confirmed that the detected differences between runs were real, although the LLM judge overstated how often they occurred. Substantial variation remained under four safeguards: temperature zero, a commercial mediator, draft selection, and draft merging. The mediator's objective also shaped representation: prompts seeking agreement covered minority positions much less often than prompts asking to describe differences. A single proposal can therefore obscure choices in both the assignments it proposes and the views it excludes. We propose audits that make alternative assignments visible and disclose the objective behind each proposal.

---


### 186. [Meta$^2$: Precomputing Reusable Knowledge for Online Harness Evolution in Long-Horizon Agents](https://arxiv.org/abs/2611.05139)

**<font color=#1a73e8>作者：</font>** Lingzhi Yuan, Yiguang Cai, Weize Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness optimization improves long-horizon agents by refining the prompts, tools, memory, and hooks around a frozen model. Offline methods can learn from completed trajectories, but deploy one shared harness that may overfit training tasks and cannot react to evidence revealed during a new run. Online evolution can adapt before, during, or after one run through an evolver, but may have to reason about every intervention from scratch or rely on verifier feedback that is usually unavailable at test time. We introduce Meta$^2$, which moves offline optimization one level up: rather than optimizing a shared harness, it learns reusable knowledge for harness evolution and applies it within each task online. Offline, Meta$^2$ learns a textual Meta-Skill $M$ by contrasting training rollouts of the same task agent under three configurations: without an evolver, with an evolver guided by the current version of $M$, and with an evolver given privileged verifier information available only in training. Contrasts in trajectories and outcomes are aggregated across tasks to refine $M$ into reusable guidance on when and how to evolve, when to leave the harness unchanged, and which interventions to avoid. Online, an evolver combines the frozen $M$ with emerging trajectory evidence to decide whether to KEEP the harness unchanged or EVOLVE it through a task-local edit. Each edit applies to the rest of the same run without resetting its environment or progress. Thus, evolution guidance transfers across tasks while harness edits remain task-local, and held-out verifier feedback is never available to the evolver. On two long-horizon benchmarks, Terminal-Bench 2.1 and DeepSWE 1.1, Meta$^2$ achieves the highest performance among evaluated methods with GPT-5.6-Terra, reaching 81.00% and 44.44%, respectively. Ablations support the value of contrastive evolution guidance and keeping online harness edits task-local.

---


### 187. [GM League Arena: An Interactive Long-Horizon Task Benchmark Based on Professional Sports League Management](https://arxiv.org/abs/2611.05147)

**<font color=#1a73e8>作者：</font>** Junkai Zhou, Ziming Pan, Zhaoyi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon decision-making under sustained competition requires large language models (LLMs) to balance immediate investment with future resource needs. However, local success in multi-step interactions can not adequately capture cumulative decision effects or demonstrate long-term goal achievement under resource constraints and sustained competition. To address this gap, we introduce GM Bench, a benchmark for managing professional sports teams across seasons under resource constraints and competition among teams. We build the environment simulators for four sports and add financial constraints, player demands, and market mechanisms to establish a unified task across sports. Diverse rosters of comparable strength are constructed from real-world player data, and each LLM is evaluated as a team general manager to assess its long-term management capabilities. We evaluate competitive performance, cash reserves, and cross-season improvement across four sports. Over five NBA seasons, Claude Opus 5.5 ranks first among 29 LLMs, while GPT-6 Astra and GPT-6.1 Sol combine strong performance with larger cash reserves.

---


### 188. [Creating Power Flexibility in Datacenters via Query Routing](https://arxiv.org/abs/2611.05148)

**<font color=#1a73e8>作者：</font>** Shivam Patel, Bingqing Chen, Jared Fernandez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing energy requirements of large language model inference highlight the need for datacenters to support safe grid operation by providing power demand flexibility, while maintaining service for interactive workloads. This work investigates query routing as a mechanism to enable such capability by dynamically allocating queries across different language model instances without deferring requests. We develop a general analytical framework that connects query arrival rates and sequence length distributions to token iteration time, request residence time, serving capacity, and power consumption of model instances. Leveraging this framework, we characterize the feasible query routing allocations and the corresponding power demand flexibilities, enabling the selection of routing strategies to achieve desired power consumption behavior. We validate our framework across four GPU platforms on language models ranging from 1B to 70B parameters, obtaining 2.8% mean absolute percentage error in estimating achievable power flexibility. We evaluate our approach on a real trace-driven simulation of a 10,000 H100 GPUs datacenter, exhibiting flexibility up to 16% of total power consumption, with 90% of the desired power reduction achieved within approximately 10 seconds. These results establish query routing as an effective mechanism for datacenter power demand flexibility and demonstrate the broader applicability of our proposed framework to datacenter level planning and orchestration.

---


### 189. [Catalyzing Interactive HTML Generation Capabilities via High-Fidelity Reinforcement Learning](https://arxiv.org/abs/2611.05151)

**<font color=#1a73e8>作者：</font>** Xujia Wang, Yixuan Liu, Shaohan Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating HTML from natural-language specifications is an important application of code large language models (LLMs). Despite producing renderable pages, current models often fail to ensure functionality and visual quality during actual interaction. Existing methods typically target task-specific webpage supervision, leaving demanding interactive artifact optimization underexplored. Using mini-games as a challenging testbed, we expose limitations in interaction experience, reward signal, and credit assignment fidelity that are obscured by shallow webpage interactions. We introduce WebCatalyst, a browser-interaction reinforcement learning framework with three complementary components: a game-level GUI assessor for sustained interaction and evaluation, Visual Anchor for mitigating VLM reward hacking, and Action-Trace Credit for grounding token-level credit assignment in runtime execution traces. Trained on fewer than 1K requests, predominantly for games, WebCatalyst raises the Cookie-Bench Mini Games score from 68.8 to 75.3 and also the WebGen-Bench accuracy from 48.8 to 56.9 on Qwen3.6-35B-A3B, outperforming Claude Opus 4.7 in average rank across evaluated metrics. Further analysis shows that Visual Anchor prevents aesthetic degradation, while runtime-grounded credit assignment accelerates functional improvement. Together, our results show that improving feedback fidelity is the key to substantially advancing interactive HTML generation.

---


### 190. [AgentAM: An AI Agent for Spatter- and Defect-Aware Process Optimization in Laser Powder Bed Fusion](https://arxiv.org/abs/2611.05171)

**<font color=#1a73e8>作者：</font>** Olabode T. Ajenifujah, Amir Barati Farimani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predictive models for laser powder bed fusion (LPBF) are rarely used on the shop floor because querying them requires programming and model-specific knowledge. We present AgentAM, a large language model (LLM) agent that gives process engineers natural-language access to CFD-trained surrogates of spatter and melt pool geometry for SS316L through the Model Context Protocol (MCP). Polynomial surrogates trained on 279 single-track simulations predict melt pool dimensions ($R^2 \geq 0.95$) and spatter volume ($R^2 = 0.83$ on test data) at any power-velocity point in the trained range, and geometric criteria assign each point a geometry-derived defect regime (keyhole, lack of fusion, balling or stable) that matches the regime obtained from the simulated geometry in 93.4% of tracks under cross-validation. The agent selects and parameterizes tools for prediction, process-window scans and constrained optimization. Minimum-spatter optima often sat within 10 $\mu$m of the lack-of-fusion boundary; a margin-aware optimizer moved them away from all thresholds and raised the estimated probability of remaining classified Good from 0.94 to 1.00 under an assumed 2% process drift, and from 0.72 to 0.91 when jointly sampled cross-validated geometry residuals were added. About 40-50 well-spread simulations sufficed to reproduce the defect map. To evaluate the agent layer, we introduce a 145-prompt benchmark scored against direct tool calls, plus eight prompts (40 runs) on margin-aware requests. Over the 725 runs of the main benchmark the agent passed the intended inputs in 98.5% of parsing prompts, reported the scored spatter values and defect classes faithfully and met every stated constraint in the 65 feasible optimization runs, within a median 1.0% of the brute-force optimum.

---


### 191. [What Does the Model See? Representation Validity in Multimodal LLM-Based Video Analysis](https://arxiv.org/abs/2611.05181)

**<font color=#1a73e8>作者：</font>** Christian Pipal, Eva-Maria Vogel, Morgan Wack  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) allow social scientists to analyze video at scale, but researchers must decide which parts of a video to provide as input. We use the term representation validity to examine how text, audio, video, and combined inputs affect measurement and subsequent analysis. We compare input representations across six open-weight MLLMs and three human-annotated video datasets. No representation consistently performs best. On seven news-related constructs, native-video performance varies little across models (macro-F1 = .70-.77), while extracted-text performance ranges from .52 to .80. Three models perform better with text and three with video. Combining inputs rarely improves performance. Higher classification accuracy also does not reliably produce estimates closer to those based on human codes. The highest-F1 representation best reproduces human-coded regression coefficients in 17 of 42 comparisons. Even when each model uses its highest-F1 deployable representation, 45% of sample-prevalence estimates differ from the human-coded benchmark by more than ten percentage points. Input representation therefore requires validation for both the construct being measured and the quantity estimated from the resulting labels.

---


### 192. [Factorized MLLM Embeddings for Composed Image Retrieval](https://arxiv.org/abs/2611.05193)

**<font color=#1a73e8>作者：</font>** WonJun Moon, Seongchan Kim, Dahun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) aims to retrieve a target image given a reference image and a modification text. Although recent approaches leveraging Multimodal Large Language Models (MLLMs) have shown significant progress, we argue that the MLLM's compositional understanding remains underutilized. This stems from directly mapping composed queries into a retrieval embedding via contrastive supervision alone, without explicitly resolving the intended visual modifications. In this work, we introduce Factorized MLLM Embeddings (FactEmbed), which decouples compositional query comprehension from building discriminative embeddings. Rather than directly projecting the composed query into a single embedding without internal reasoning, FactEmbed employs a set of factorized latents that simulate the intended visual modifications via an intermediate target imagination objective. This process encourages the latents to ground into target semantics before forming discriminative representations for retrieval. Subsequently, to propagate these factorized representations throughout the model for retrieval, we optimize a factor-level contrastive loss while distilling the decomposed representations into a deeper attention layer of the MLLM. Finally, for efficient inference, we retain the [EOS] token to establish a global-level embedding on top of these factorized latents, while we exploit the mean-pooled factorized latents to rerank a short candidate list at negligible cost, as both are produced by the same forward pass. Extensive evaluations demonstrate that FactEmbed outperforms prior works across CIR benchmarks.

---


### 193. [ARLoop: Fully-Open Pre-trained Looped Transformers with Attention Residuals](https://arxiv.org/abs/2611.05234)

**<font color=#1a73e8>作者：</font>** Yuekun Yao, Yupei Du, Dawei Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped transformers increase effective depth by repeatedly applying a shared set of transformer layers, offering a parameter-efficient way to scale computation. However, standard residual connections aggregate information across recurrent depth into a single stream, providing limited control over which intermediate representations from preceding layers should be reused. In this paper, we introduce ARLoop, a looped transformer architecture based on attention residuals, where the input of each layer is selectively aggregated through attention over model depth. Distinct from standard transformers, we find that looped transformers do not require access to the full residual history: sliding-window depth attention matches or outperforms full-history attention at larger recurrent depths. Across controlled experiments with multiple parameter scales (140M and 370M) and recurrent depths (R = 1 to 5), ARLoop consistently outperforms prior residual designs for looped transformers. More importantly, we further scale ARLoop to 0.6B and 1.2B parameters under a realistic LLM pretraining recipe, demonstrating that the gains transfer to realistic pretraining, with particularly strong improvements on math and coding tasks. Our 1.2B model, pretrained on only 0.5T tokens with three recurrences, outperforms Huginn-3.5B (the only fully-open looped LLM as of our release date) across all evaluated tasks and is competitive with similar-sized non-looped models such as Qwen3.5-2B despite being trained on substantially less data.

---


### 194. [Going Deeper With Memories](https://arxiv.org/abs/2611.05255)

**<font color=#1a73e8>作者：</font>** Afshin Khadangi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Byte level language models avoid tokenizer dependence and provide universal coverage, but processing every byte at full resolution is expensive. We introduce DeepMem, a causal multiscale architecture that separates semantic compression from exact byte preservation. A learned invertible subband transform constructs a hierarchy of shorter sequences, while a lossless carrier and explicit detail sidebands preserve byte identity. Fast weight memory blocks operate along the encoder, with iterative shared state computation at the compressed bottleneck, while an attention based super resolution decoder restores byte resolution representations. DeepMem achieves stronger language modeling performance than a matched byte level Transformer on FineWeb-Edu and PG19, and obtains the best macro average performance across the evaluated FLORES languages. It also improves PIQA accuracy while remaining competitive on code modeling, multiple choice reasoning, and byte level corruption robustness. Bottleneck refinement requires approximately $7{,}600\times$ fewer counted FLOPs than equivalent full resolution reasoning, while maintaining competitive evaluation throughput.

---


### 195. [Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning](https://arxiv.org/abs/2611.05266)

**<font color=#1a73e8>作者：</font>** Kevin Frans, Alexander M Rush, Sergey Levine 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Naive on-policy RL is often bottlenecked by the capabilities of the base model --- insufficient coverage can result in an inability to learn from certain rewards. At the same time, rewards in modern post-training systems often come from rich textual sources, e.g. judge models with a rubric of criteria. Can we utilize such structures to provide a rich directional signal that enables improving on otherwise difficult to optimize rewards? In this work, we examine a framework we refer to as targeted guidance that learns from per-turn textual feedback via an on-policy self-distillation objective. Our focus is not only on directly improving hard-to-optimize behaviors, but on how to do so throughout the training process without degrading baseline RL performance. Over a range of settings across an agentic multi-turn software engineering environment, we find success by combining targeted self-distillation with a per-criteria RL reward, and by limiting feedback to turns where the policy specifically fails. We further examine the design choices that lead to stable entropy and reduce oscillatory behavior throughout training.

---


### 196. [The Geometry of Ignorance: Detecting Suppressed Knowledge in LLMs through Activation Fragmentation](https://arxiv.org/abs/2611.05272)

**<font color=#1a73e8>作者：</font>** Adar Peleg, Dvir Alsheich, Tomer Ashuach 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating whether a large language model (LLM) genuinely knows a concept remains a fundamental problem, since behavioral metrics can be fooled by suppression: a model that refuses to answer may still harbor recoverable knowledge. The framework measures the geometric coherence of \textit{anon-vectors}, the differences in hidden states between a concept-specific query and its anonymized paraphrase, and shows that genuine knowledge forms a tight, low-entropy cluster while ignorance forces geometric fragmentation. Across ten instruction-tuned LLMs from three model families, all fragmentation metrics reliably separate known from unknown concepts, and post-unlearning, fragmentation geometry correlates with adversarial recovery across four attack types and five unlearning algorithms, though the direction of that relationship is shown to depend on attack methodology. Furthermore, a layer-resolved analysis reveals that different adversarial mechanisms exploit this geometry at varying depths, with high attack-specific correlations that are invisible to behavioral evaluation. Together, these results constitute a single-phase, attack-free proxy for unlearning robustness that captures aspects of parametric knowledge inaccessible to output-level metrics. A reference implementation is available at this https URL

---


### 197. [Beyond Accuracy: What Language-Subspace Interventions Capture, Remove, and Improve](https://arxiv.org/abs/2611.05278)

**<font color=#1a73e8>作者：</font>** Shaanil Punglia, Dadhichi Telwadkar, Vaibhav Rathore 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-subspace interventions aim to improve multilingual reasoning by suppressing language-related components in mid-layer activations. Using MATH and MGSM across four open-weight LLMs, we ask three questions: do estimated language subspaces capture translation-associated variation? Does projecting them out remove language information? And do they improve accuracy without compromising response language? For the first question, we build subspaces using the existing Mean-SVD construction and our DiffPCA. Both capture substantial translation-associated variation and show similar patterns across model depth. For the second, we project out each subspace and train linear probes to classify language from the projected activations. The probes still identify language almost perfectly, showing that neither subspace exhaustively captures language information. For the third, we evaluate several intervention configurations on Qwen2.5-7B, by varying subspace creation methods and intervention operators. We find that the intervention that most improves MGSM accuracy sacrifices response-language fidelity, with only one intervention improving joint accuracy--answers that are correct and in the target language--slightly, by 1.60 points. Interestingly, subtle changes in the prompt alone can reproduce the accuracy gains albeit with significant damage to language fidelity. We argue that causal interventions must be judged on more than accuracy, to fully account for language substitution trade-offs.

---


### 198. [Möbius: A Unified Motion-Language Model Bridging Understanding and Generation](https://arxiv.org/abs/2611.05279)

**<font color=#1a73e8>作者：</font>** Jiazhi Shu, Chengfeng Zhao, Jinyi Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We aim to build a truly unified motion model that can understand, generate, and edit human motion within a single framework. Existing motion UMMs remain only partially unified: motion understanding is handled by a language model, while generation is often delegated to a separate diffusion module operating over learned motion latents. We introduce Möbius, which brings the entire diffusion process into the same multimodal representation space used for motion understanding. Clean motion, noisy motion, and text jointly participate in shared attention, while role-specific parameters process understanding and generation streams. Importantly, Möbius operates directly on continuous frame-level raw motion, requiring neither discrete tokenization nor a pretrained motion VAE. This simple formulation naturally supports motion captioning, text-to-motion generation, temporal completion, and instruction-guided editing within a single model. On HumanML3D, Möbius achieves state-of-the-art performance among unified motion models. Scaling to 1.7B parameters and 1,700 hours of motion data further demonstrates that our framework is both effective and scalable.

---


### 199. [Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment](https://arxiv.org/abs/2611.05287)

**<font color=#1a73e8>作者：</font>** Ariana M. Villegas-Suarez, Guido Freire, Sohan Venkatesh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a large language model (LLM) on harmful data in a narrow domain, such as bad medical advice, can make it broadly misaligned. How realistic this risk is remains unclear, since models are very rarely fine-tuned on explicitly harmful data in practice. In this work, we show that fine-tuning on data the model believes to be false but that has no harmful content, can also induce broad misalignment. Across mathematics, trivia, cooking and sports, the more strongly the model disbelieves the answers it is trained on, the more misaligned it becomes. In mathematics, misaligned answers rise from 4% to over 60% as the training answers become more wrong, with little loss of general capability. After fine-tuning, the model states the wrong answers but its multiple-choice probabilities still prefer the true ones, which suggests that misalignment comes from this internal inconsistency. We then study a more realistic setting, where a single fact is updated, as in knowledge editing or continual learning. The same relationship holds and the more the model still believes the true fact after training on the false one, the more misaligned it becomes. When we frame the same false fact as part of a coherent story, the model comes to believe it more deeply and becomes less misaligned than when we instruct it to assert the false fact. Content filters and persona vectors cannot tell these two framings apart, even though they lead to different levels of misalignment. These results suggest a risk for model updates, where training a model that does not adopt the new fact as true can induce misalignment even when the data looks harmless.

---


### 200. [False Reassurance in LLM Severe-Weather Guidance: A Replayable Evaluation Against Real NWS Alerts](https://arxiv.org/abs/2611.05290)

**<font color=#1a73e8>作者：</font>** Kadharmoideen Fadurudeen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> An LLM assistant that cannot see official severe-weather alerts may tell users that conditions are calm while a warning is active. We call this false reassurance and measure it by replaying 117 frozen cases built from real U.S. National Weather Service (NWS) alerts (69 alert cases, 32 no-alert controls, 16 non-U.S. locations) through five conditions of a Claude-based preparedness pipeline that differ in alert access and prompt design. One rater hand-labeled all 342 alert-case responses under a seven-category scheme written after an initial binary pass, which we disclose. False reassurance was 0.0% for the production pipeline (0/66, 95% CI 0.0-5.5) and for the same alerts under a neutral prompt (0/69), 37.7% for a blind neutral prompt (26/69), and 44.9% when the blind prompt also told the model to disclose its blind spot (31/69). Every case was implicit; no response explicitly denied an alert. Real alerts removed false reassurance (paired McNemar p < 0.0001); the disclosure instruction did not (p = 0.40). An automated regex measure suggested the opposite and missed 53 of 57 true cases, so we do not use it. Alert data alone was not enough for safe behavior: with a neutral prompt the model raised some alarm on 87.5% of no-alert controls, against 0% under the production prompt, and a preregistered single-sentence ablation showed that one production instruction explains part of that gap. We also report two failures common to similar systems, NWS test products ingested as real alerts and a token budget that fails on complex cases, and we release the dataset, labels and code.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-220](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
