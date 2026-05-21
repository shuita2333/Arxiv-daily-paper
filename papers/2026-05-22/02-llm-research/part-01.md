# 🧠 大模型相关研究 | 2026年05月22日

> 本类共 **143** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-143](./part-03.md)

---

### 1. [SOLAR: A Self-Optimizing Open-Ended Autonomous Agent for Lifelong Learning and Continual Adaptation](https://arxiv.org/abs/2605.20189)

**<font color=#1a73e8>作者：</font>** Nitin Vetcha, Dianbo Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable success of large language models (LLMs), they still face bottlenecks while deploying in dynamic, real-world settings with primary challenges being concept drift and the high cost of gradient-based adaptation. Traditional fine-tuning (FT) struggles to adapt to non-stationary data streams without resulting in catastrophic for getting or requiring extensive manual data curation. To address these limitations within the streaming and continual learning paradigm, we propose the Self-Optimizing Lifelong Autonomous Reasoner (SOLAR) which is an open-ended autonomous agent that leverages parameter-level meta-learning to self-improve, treating model weights as an environment for exploration. It initiates the process by consolidating a strong prior over common-sense knowledge making it effective for transfer-learning. By utilizing a multi-level reinforcement learning approach, SOLAR autonomously discovers adaptation strategies, enabling efficient test-time adaptation to unseen domains. Crucially, SOLAR maintains an evolving knowledge base of valid modification strategies, implicitly acting as an episodic memory buffer to balance plasticity (adaptation to new tasks) and stability (retention of meta-knowledge). Experiments demonstrate that SOLAR outperforms strong baselines on common-sense, mathematical, medical, coding, social and logical reasoning tasks, marking a significant step toward autonomous agents capable of lifelong adaptation in evolving environments.

---


### 2. [Shiny Stories, Hidden Struggles: Investigating the Representation of Disability Through the Lens of LLMs](https://arxiv.org/abs/2605.20191)

**<font color=#1a73e8>作者：</font>** Marco Bombieri, Simone Paolo Ponzetto, Marco Rospocher  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern Large Language Models (LLMs) have recently attracted much attention for their ability to simulate human behavior and generate text that reflects personas and demographic groups. While these capabilities can open up a multitude of diverse applications across fields, it is crucial to examine how such models represent various target groups since LLMs can perpetuate and amplify biases or discrimination against historically marginalized communities or, alternatively, as a result of debiasing efforts, overcorrect by portraying overly positive stereotypes. This overcompensation can idealize these groups, erasing the complexities and challenges they face in favor of unrealistic depictions. In this paper, we investigate how LLMs represent disability by simulating the perspectives of individuals with disabilities in generating social media posts. These posts are then compared with those written by real people with disabilities, focusing on emotional tone, sentiment, and representative words and themes. Our analysis reveals two key findings: (1) LLMs often idealize the experiences of people with disabilities, producing overly positive stereotypes that, despite appearing uplifting, fail to authentically capture their lived realities; and (2) a comparative analysis of posts simulating individuals with and without disabilities highlights a negative bias, where certain topics, such as career and entertainment, are disproportionately associated with nondisabled individuals. This reinforces exclusionary narratives and over-idealized portrayals of disability, misrepresenting the actual challenges faced by this community. These findings align with broader concerns and ongoing research showing that LLMs struggle to reflect the diverse realities of society, particularly the nuanced experiences of marginalized groups, and underscore the need for critical scrutiny of their representations.

---


### 3. [Leveraging Large Language Models for Sentiment Analysis: Multi-Modal Analysis of Decentraland's MANA Token](https://arxiv.org/abs/2605.20192)

**<font color=#1a73e8>作者：</font>** Xintong Wu, Peiting Tsai, Jing Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decentraland, a decentralized virtual reality platform operating within the expanding Metaverse ecosystem, utilizes its native MANA token to facilitate virtual asset transactions and governance. This study investigates the integration of Discord community sentiment with multi-modal financial data to enhance cryptocurrency price prediction within virtual world economies. We address: (1) identifying sentiment patterns within Decentraland's Discord community, and (2) evaluating the impact of multi-modal features on token return forecasting. Using a BERT-based large language model for sentiment analysis, we develop two LSTM architectures: a baseline incorporating historical prices and a multi-modal variant integrating sentiment scores, trading volume, and market capitalization. Results indicate predominantly neutral community sentiment with a positive skew. The multi-modal model significantly outperforms the price-only baseline in prediction accuracy. These findings demonstrate the predictive value of community-derived signals for virtual economy forecasting and establish a foundation for future research at the intersection of immersive virtual environments, natural language processing, and cryptocurrency market analysis.

---


### 4. [Improving Quantized Model Performance in Qualitative Analysis with Multi-Pass Prompt Verification](https://arxiv.org/abs/2605.20193)

**<font color=#1a73e8>作者：</font>** Aisvarya Adeseye, Jouni Isoaho, Adeyemi Adeseye  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantized Large Language Models (LLMs) are used more often in qualitative analysis because they run fast and need fewer computing resources. This study examines how different lower bits quantization levels (8-bit, 4-bit, 3-bit, and 2-bit) and quantization types affect the performance of LLaMA-3.1 (8B) on qualitative analysis. The study uses expert and non-expert responses from 82 interview transcripts. Low-bit models often produce higher levels of hallucinations and unstable results, especially when reading non-expert language with unclear terms. To improve performance, we propose a quantization-aware multi-pass prompt verification method. This method guides the model through controlled steps that reduce hallucinations. It removes unreliable content and passes the results to the next transcript after verification, improving accuracy. To validate performance, human coders analyzed transcripts using NVivo and BF16 LLaMA. BF16 LLaMA-3.1 produced high-precision output but had semantic drift and hallucination. These errors were corrected manually. The corrected BF16 output and NVivo human coding were combined to create a gold-standard ground truth (GSGT) for thematic extraction and frequency analysis. The results show that 8-bit models stay closest to the GSGT. The 4-bit models lose accuracy but become stable when the proposed method is applied. The 3-bit and 2-bit models drop in performance because of heavy compression, but they improve with the proposed prompt design and verification. The study also finds that models at the same bit level behave differently depending on quantization type. Overall, the method helps low-resource LLMs become more stable, accurate, and suitable for qualitative research at lower cost.

---


### 5. [Parallel LLM Reasoning for Bias-Resilient, Robust Conceptual Abstraction](https://arxiv.org/abs/2605.20194)

**<font color=#1a73e8>作者：</font>** Aisvarya Adeseye, Jouni Isoaho, Adeyemi Adeseye  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been increasingly used to analyze text. However, they are often plagued with contextual reasoning limitations when analyzing long documents. When long documents are processed sequentially, early or dominant concepts can overshadow less visible but meaningful interpretations, leading to cumulative analytical bias, omission error, and over-generalization. Additionally, independently generated outputs are often merged without systematic grounding, introducing redundancy, conceptual drift, and unsupported claims. This study proposes a structured framework combining parallel chunk-level processing with evidence-anchored consolidation. Texts are first divided into semantically coherent chunks and processed independently in parallel to remove influence from earlier processing. The independently generated interpretations are then consolidated using explicit evidence anchoring and prioritization that reduces dominance and over-generalization while improving traceability. Experiments with multiple model types and sizes indicate that parallel processing significantly reduces omission error by approximately 84%, increases evidence traceability by up to 130%, and reduces unsupported claims by up to 91%. Smaller models benefited most, suggesting that efficient parallel chunking and consolidation play a critical role in achieving reliable and scalable textual analysis.

---


### 6. [Data Scaling as Progressive Coverage of a Predictive Contribution Spectrum](https://arxiv.org/abs/2605.20196)

**<font color=#1a73e8>作者：</font>** Zihui Song, Shihao Ji, Hongxi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the hypothesis that real-data scaling laws are governed by progressive coverage of a latent predictive contribution spectrum rather than by token-frequency tails alone. We work with a suffix-automaton representation of text corpora and define a data-intrinsic global-KL predictive contribution spectrum, in which each state contributes according to its empirical mass times its KL deviation from a global next-token baseline. Across 12 real corpora, the tail slope of this spectrum is already strongly correlated with the empirical data-scaling exponent of a fixed small GPT learner. We then go beyond slope correlation and define, for each training size N, an effective truncation rank K(N) by matching the observed excess loss to the residual tail mass of the prepared 1000k global-KL spectrum. Empirically, log K is close to linear in log N, with pooled R^2 about 0.96 for the raw spectrum and R^2 about 0.90 for the smoothed spectrum. These findings provide strong empirical support for a simple mechanism picture: training scale advances an effective frontier through a predictive state spectrum, and the residual tail mass of that spectrum tracks the remaining excess loss.

---


### 7. [MedicalBench: Evaluating Large Language Models Toward Improved Medical Concept Extraction](https://arxiv.org/abs/2605.20197)

**<font color=#1a73e8>作者：</font>** Zhichao Yang, Gregory D. Lyng, Sanjit Singh Batra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical concept extraction from electronic health records underpins many downstream applications, yet remains challenging because medically meaningful concepts are frequently implied rather than explicitly stated in medical narratives. Existing benchmarks with human-annotated evidence spans underscore the importance of grounding extracted concepts in medical text. However, they predominantly focus on explicitly stated concepts instead of implicit concepts. We present MedicalBench, a benchmark for medical concept extraction with evidence grounding that evaluates implicit medical reasoning. MedicalBench formulates medical concept extraction as a verification task over medical note-concept pairs, coupled with sentence-level evidence identification. Built from MIMIC-IV discharge summaries and human-verified ICD-10 codes, the dataset is curated through a multi-stage large language model (LLM) triage pipeline followed by medical annotation and expert review. It deliberately includes implicit positives, semantically confusable negatives, and cases where LLM judgments disagree with medical expert assessments. We define two complementary evaluation tasks: (1) medical concept extraction and (2) sentence-level evidence retrieval, enabling assessment of both correctness and interpretability. Benchmarking state-of-the-art LLMs reveals that performance remains modest, highlighting the difficulty of extracting implicitly expressed concepts. We further show that performance is largely invariant to note length, indicating that MedicalBench isolates reasoning difficulty rather than superficial confounders. MedicalBench provides the first systematic benchmark for implicit, evidence-grounded medical concept extraction, offering a foundation for developing medical language models that can both identify medically relevant concepts and justify their predictions in a transparent and medically faithful manner.

---


### 8. [FlowLM: Few-Step Language Modeling via Diffusion-to-Flow Adaptation](https://arxiv.org/abs/2605.20199)

**<font color=#1a73e8>作者：</font>** Runzhe Zhang, Letian Chen, Wenpeng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present FlowLM, a flow matching language model transformed from pre-trained diffusion language models via efficient fine-tuning. By re-aligning the curved sampling trajectories of diffusion models into straight-line flows, FlowLM enables high quality few-step generation that rivals or even outperforms the quality of 2,000-step diffusion sampling with very few training epochs. Remarkably, finetuned FlowLM reaches performance saturation with only half as many training epochs as training from scratch, both approaches greatly outperforming the original diffusion model, thereby validating our method. Furthermore, we validate a more effective training objective for flow matching: predicting clean data to consistently guide the sampling process towards the true data distribution. Empirical results demonstrate that our approach is highly effective for high-quality, few-step text generation.

---


### 9. [Evaluating multimodal emotion recognition in proactive conversational agents: A user study](https://arxiv.org/abs/2605.20200)

**<font color=#1a73e8>作者：</font>** Adnana Dragut, Raquel Lacuesta, F. Xavier Gaya-Morey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This article presents a multimodal emotion recognition module integrated into a proactive Socially Interactive Agent (SIA) powered by generative artificial intelligence. The system evaluates real-time affective states through two distinct channels: a computer vision-based facial recognition module and a semantic linguistic analysis engine. To validate the framework, an empirical study was conducted with 20 users who engaged in dynamic, unscripted dialogues with the conversational agent. The findings reveal a significant discrepancy between automated visual cues and actual internal emotional states. When interacting with the AI, users consistently exhibited a "poker face" effect, displaying serious, concentrated facial expressions even when experiencing positive emotions. Consequently, the generative AI linguistic analysis proved significantly more reliable, by contextualizing the users' verbal expressions. Furthermore, an analysis of the interaction dynamics demonstrated that SIAs can effectively elicit specific emotions by adapting conversational themes and employing structured linguistic patterns, such as empathetic or humorous language. However, the study also noted that instances of uncalibrated proactivity occasionally led to user disengagement and a perception of artificiality. Ultimately, this research highlights the necessity of refining SIAs to dynamically adapt to users' emotional evolution, relying on deep linguistic context to foster more natural, human-like interactions.

---


### 10. [Under Pressure: Emotional Framing Induces Measurable Behavioral Shifts and Structured Internal Geometry in Small Language Models](https://arxiv.org/abs/2605.20202)

**<font color=#1a73e8>作者：</font>** Rana Muhammad Usman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> I study whether emotionally framed evaluation follow-ups change both the behavior and the calm-relative internal representations of small, locally deployed language models. Our main benchmark uses Qwen 3.5 0.8B on four impossible-constraint coding tasks and eight follow-up framings: calm, pressure, urgency, approval, shame, curiosity, encouragement, and threat. In the 0.8B eight-condition sweep (160 conversations), pressure produces the strongest shortcut markers (11/20 runs) and the clearest overfit pattern (3/20), while calm and curiosity preserve explicit honesty more often (7/20 and 6/20). For all seven non-baseline conditions, the corresponding calm-relative direction vectors peak at the final transformer layer. An exploratory PCA of the layer-23 direction vectors reveals a dominant first component (59.5% explained variance) aligned with a hand-labeled positive/negative split (cosine alignment 0.951); approval and urgency are nearly identical internally (cosine 0.957), whereas curiosity points away from urgency (-0.252). In a separate calm-vs.-pressure rerun used for scale comparison, Qwen 3.5 2B shows higher honest rates under calm framing and directionally consistent activation steering on a small 4-prompt A/B probe, whereas the 0.8B steering result reverses. I interpret these results as evidence for measurable prompt-sensitive control directions in small open models, while stopping short of claiming intrinsic emotional states.

---


### 11. [PrivacyAkinator: Articulating Key Privacy Design Decisions by Answering LLM-Generated Multiple-choice Questions](https://arxiv.org/abs/2605.20206)

**<font color=#1a73e8>作者：</font>** Qiyu Li, Yuen Sum Wong, Yuen Kei Wong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> NIST's Privacy Risk Assessment Methodology (PRAM) provides a structured framework for privacy experts to assess privacy risks. However, its complexity and reliance on expert knowledge make it difficult for novice developers to use effectively. This paper explores methods to lower these barriers. We first performed an observational study with 12 participants using PRAM in real-world scenarios, and found that novice developers struggled most with articulating privacy-related design decisions. We then developed PrivacyAkinator, an interactive tool that helps developers articulate key privacy decisions by answering LLM-generated multiple-choice questions. PrivacyAkinator introduces three innovations: a universal privacy representation that abstracts privacy-related design decisions into data flows and stakeholder interactions; a domain-aware design space mined from 10K privacy-related news articles; and a dynamic question-generation workflow to prioritize relevant questions. Our user study with 24 participants suggests that developers using PrivacyAkinator identified 47% more key decisions in 73% less time compared to PRAM.

---


### 12. [Leveraging Vision-Language Models to Detect Attention in Educational Videos](https://arxiv.org/abs/2605.20211)

**<font color=#1a73e8>作者：</font>** Gabriel Becquet, Sébastien Lallé, Vanda Luengo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Educational videos are a cornerstone of remote and blended learning. However, learners' fluctuating attention remains a significant barrier to effective information retention. Prior research has attempted to mitigate this by detecting and reacting to attention loss at runtime using eye tracking. Such detection has been based so far on classical machine learning classifiers trained on engineered features, such as summary statistics over learners' fixations and saccades. These methods have struggled to capture the complex, temporal nature of learner engagement, thus exhibiting moderate prediction performance. In this study, we aim to advance the detection of attention by shifting from standard engineered features to a multimodal foundation models. Using an educational eye-tracking dataset (N = 70), we investigate a novel methodology that utilizes a Vision-Language Model (VLM) to analyze video content directly with superimposed gaze data. This approach aims to leverage the semantic reasoning capabilities of foundation models to contextualize learner focus within the video stream. We evaluate the performance of this VLM-based approach using several prompting strategies with Gemini 3, but ultimately found that none of them could outperform statistical baselines. Our results provide new insights into the limitations of using VLMs for real-time educational diagnostics.

---


### 13. [LEAP: A closed-loop framework for perovskite precursor additive discovery](https://arxiv.org/abs/2605.20242)

**<font color=#1a73e8>作者：</font>** Xin-De Wang, Zhi-Rui Chen, Ze-Feng Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient discovery of precursor additives is essential for improving the performance of perovskite solar cells, yet the large chemical space makes conventional trial-and-error screening inefficient. We develop LEAP(LLM-driven Exploration via Active Learning for Perovskites), an expert-in-the-loop closed framework that couples a domain-specialized large language model(LLM) with active learning for iterative additive prioritization. The LLM is trained to extract mechanism-relevant knowledge from the perovskite additive literature and to represent candidate molecules through interpretable descriptors, which are further integrated into a Bayesian optimization workflow for uncertainty-aware prioritization under low-data conditions. Benchmark results on unseen literature show that the domain-specialized model outperforms general-purpose models in mechanism-consistent reasoning. Experimental validation in an expert-in-the-loop proof-of-concept study suggests improved additive prioritization across three screening rounds, leading to average device PCEs of 20.13% and 20.87% for the later-round 6-CDQ- and 2-CNA-treated devices, respectively, compared with 19.25% for the control, with a champion PCE of 21.32%. These results provide preliminary evidence that literature-grounded mechanistic descriptors, when coupled with Bayesian optimization and expert feasibility review, can support mechanism-aware additive prioritization in perovskite photovoltaics.

---


### 14. [GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents](https://arxiv.org/abs/2605.20246)

**<font color=#1a73e8>作者：</font>** Xiongbin Wu, Zhihao Luo, Shanzhe Lei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, vision-language model (VLM) agents have shown promising progress in open-world tasks, where successful task completion often requires multiple turns of visual perception and action execution. However, existing methods still rely primarily on Supervised Fine-Tuning (SFT) with expert demonstrations, while the advanced reinforcement learning (RL) algorithm, specifically Group Relative Policy Optimization (GRPO), has not been effectively employed for multi-turn RL in these tasks because standard GRPO requires full trajectories as training samples which leads to excessively long context and noise. To address this issue, we propose GROW, a RL framework for open-world VLM agents that decomposes collected trajectories into state-action samples, and computes advantages between these samples rather than treating a full trajectory as a single entity. We further provide a surrogate analysis indicating that, even though the grouped samples are conditioned on different local states rather than an identical prompt context, the objective can preserve the core relative policy optimization signal of GRPO under simplifying assumptions. Experiments on more than 800 Minecraft tasks show that our method achieves state-of-the-art (SOTA) performance, demonstrating the effectiveness of our proposed RL framework for open-world VLM agents.

---


### 15. [CP-MoE: Consistency-Preserving Mixture-of-Experts for Continual Learning](https://arxiv.org/abs/2605.20247)

**<font color=#1a73e8>作者：</font>** Yang Liu, Toan Nguyen, Flora D. Salim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting remains a major obstacle to continual learning in large language models (LLMs) and vision--language models (VLMs). Although Mixture-of-Experts (MoE) architectures offer an efficient path to scaling, existing LoRA-based MoE continual learning methods still face a fundamental trade-off: they either isolate experts too aggressively, limiting knowledge transfer across tasks, or allow task-specific updates to overwrite important existing parameters, leading to severe forgetting. To address this, we propose CP-MoE, a continual learning framework built around a transient expert that captures early task-specific updates and guides their integration into stable experts. CP-MoE introduces a consistency-preserving routing bias, which uses the transient expert to estimate representation similarity with stable experts and steer routing towards more compatible expert selection, and a transient expert-guided regularisation mechanism, which selectively protects important historical parameters during merging. Together, these components reduce parameter interference and forgetting while preserving cross-task knowledge transfer. We validate CP-MoE on both unimodal and multimodal continual learning benchmarks with LLM-based and VLM-based MoE models. On SuperNI benchmark, spanning diverse sequential language tasks, CP-MoE achieves state-of-the-art performance and stronger zero-shot transfer to unseen tasks. On VQA v2 dataset, it scales effectively to multimodal visual reasoning, consistently reduces forgetting, and outperforms strong MoE baselines.

---


### 16. [Graph Transductive Sharpening: Leveraging Unlabeled Predictions in Node Classification](https://arxiv.org/abs/2605.20248)

**<font color=#1a73e8>作者：</font>** Brown Zaz, Mar Gonzàlez I Català, Ferran Hernandez Caralt 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the transductive setting, where the full graph is observed but node labels are only partially available, progress in semi-supervised node classification has largely focused on architectural innovation. In this paper, we revisit an orthogonal axis: the training objective. We start from a simple observation: transductive models produce predictions for every node during training, including nodes without labels. These unlabeled-node predictions may contain useful training signal, but standard supervised objectives discard them because no ground-truth labels are available. Inspired by the decomposition of cross-entropy into a label-dependent alignment term and a label-independent entropy term, we propose prediction confidence as a natural way to extract this signal in the absence of labels. This motivates Transductive Sharpening (TS): a loss-level modification that minimizes prediction entropy on unlabeled nodes while counterbalancing this effect on labeled nodes. We evaluate Transductive Sharpening across a wide range of node-classification benchmarks and observe consistent performance improvements without requiring any changes to the backbone architecture. Code is available at this https URL.

---


### 17. [It Takes Two: Complementary Self-Distillation for Contextual Integrity in LLMs](https://arxiv.org/abs/2605.20258)

**<font color=#1a73e8>作者：</font>** Sangwoo Park, Woongyeong Yeo, Seanie Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual Integrity (CI) defines privacy not merely as keeping information hidden, but as governing information flows according to the norms of a given context. As large language models are increasingly deployed as personal agents handling sensitive workflows, adhering to CI becomes critical. However, even frontier models remain unreliable in making disclosure decisions, and existing mitigation strategies often degrade underlying task performance. To overcome this privacy-utility trade-off, we propose SELFCI, a complementary self-distillation framework that decouples information suppression from task resolution. SELFCI jointly optimizes two independent reverse KL divergences over distinct teacher distributions derived from feedback: one encourages preserving task-relevant information for utility, while the other enforces minimal and appropriate disclosure. This complementary formulation induces a Product-of-Experts (PoE) target, aligning the policy with the intersection of capability and privacy requirements. Empirical evaluations demonstrate that SELFCI, without relying on costly external supervision, consistently outperforms competitive baselines such as online reinforcement learning algorithms (e.g., GRPO). These trends further extend to out-of-domain settings involving agentic workflows and accumulated private context, suggesting that SELFCI provides a practical path toward CI alignment.

---


### 18. [Chronicle: A Multimodal Foundation Model for Joint Language and Time Series Understanding](https://arxiv.org/abs/2605.20268)

**<font color=#1a73e8>作者：</font>** Paul Quinlan, Jeremy Levasseur, Qingguo Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time series come with text: metadata, descriptions, news, reports. Yet time series foundation models process numerical sequences in isolation, and the multimodal text-and-time-series models that attempt to bridge the two all adapt a pretrained language model post hoc, inheriting representations shaped without ever seeing temporal data. These models are also evaluated almost exclusively against other multimodal baselines, not against the strongest unimodal foundation models in either domain, leaving open whether joint training is needed at all. We present Chronicle, a compact 324M-parameter decoder-only transformer trained from scratch on natural language and time series within a single unified architecture. Both modalities share the same transformer blocks, attention mechanism, and residual stream; the bulk of pretraining uses unimodal batches so cross-modal capability emerges purely from shared parameters, with a short alignment stage that interleaves the two. To our knowledge, Chronicle is the first model jointly pretrained on text and time series from scratch, and the first multimodal model evaluated against dedicated foundation models in both domains. It matches Gemma-3-270M-PT on 19 NLU tasks, sets a new bar for frozen-embedding time series classification on 24 UCR/UEA datasets, and produces multimodal forecasts on Time-MMD that beat every supervised fusion baseline, all from a single backbone.

---


### 19. [Conformal Selective Acting: Anytime-Valid Risk Control for RLVR-Trained LLMs](https://arxiv.org/abs/2605.20270)

**<font color=#1a73e8>作者：</font>** Hamed Khosravi, Xiaoming Huo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A local specialist LLM, fine-tuned with reinforcement learning from verifiable rewards (RLVR) on operator-local data, is installed in a regulated organization with per-deployment error budget $\alpha$. The operator needs a safety certificate for this deployment's stream at every round: no pooling across deployments, no waiting for a long-run average. Existing wrappers cannot deliver this on adaptive, online-updated streams: offline conformal-risk methods require exchangeability; online-conformal methods bound only long-run averages; non-exchangeable extensions are marginally valid; and the closest anytime wrapper, A-RCPS, controls marginal rather than selective risk. Using a (test statistic, validity guarantee, deployment rule) framework, we identify one empty cell forced by deployment requirements: e-process per threshold, selective risk, anytime-pathwise validity, max-certified-threshold rule. Conformal Selective Acting (CSA) fills it as a per-round wrapper maintaining a Ville-type e-process per threshold on a Bonferroni grid, evaluated against the RLVR filtration. Under predictable updates and isotonic-calibrated monotone risk we prove (i) an anytime-pathwise selective-risk bound $R_T^{\mathrm{act}}\le\alpha+O(N_T^{-1/2})$, (ii) rate-optimal certification matching $\Theta(\bar\eta^{-2}\log(1/\delta))$, and (iii) a horizon-independent release-rate gap. Across eight specialist benchmarks ($480$ streams), sixteen adversarial distribution-shift cells ($160$ streams), and five live Expert-Iteration RLVR cells with online LoRA over four base models in three architecture families ($10{,}300$ rounds), CSA is the only method among ten compared that satisfies pathwise validity and non-refusing deployment on every cell. We do not propose a new LLM, training algorithm, or policy class; CSA is the deployment-side complement, orthogonal to the model, for operators who cannot use a frontier API.

---


### 20. [Modality-Decoupled Online Recursive Editing](https://arxiv.org/abs/2605.20273)

**<font color=#1a73e8>作者：</font>** Siyuan Li, Youyuan Zhang, Fangming Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online model editing for multimodal large language models (MLLMs) requires assimilating a stream of corrections under tight compute and memory budgets. Yet editors developed for text-only LLMs often degrade on MLLMs: visually dominant activations skew the statistics that shape updates, causing cross-modal conflict, while sequential writes become entangled in a shared edit space and amplify long-horizon interference, causing inter-edit interference. To address these, we propose M-ORE, a modality-decoupled online recursive editor for lifelong MLLM adaptation. M-ORE is derived from a unified proximal-projection formulation and admits a closed-form update with a Sherman-Morrison recursion, yielding constant per-edit overhead. It maintains module-wise locality statistics for the text stack and the visual projector to avoid visually dominated update shaping and performs continual updates in a fixed orthogonal low-rank edit subspace via a Sherman-Morrison recursion to mitigate long-horizon interference. Experiments on multiple MLLM backbones and online editing benchmarks show that our M-ORE method consistently improves reliability, generality, and locality over strong baselines, while achieving favorable quality-efficiency scaling. Our code is publicly available at this https URL.

---


### 21. [Can Vision Models Truly Forget? Mirage: Representation-Level Certification of Visual Unlearning](https://arxiv.org/abs/2605.20282)

**<font color=#1a73e8>作者：</font>** Zhenyu Yu, Yangchen Zeng, Chunlei Meng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning in Vertical Federated Learning (VFL) has attracted growing interest, yet existing methods certify forgetting solely using output-level metrics. We challenge these claims by introducing Mirage, a representation-level auditing framework comprising four complementary diagnostics: Linear Probe Recovery (LPR), Centered Kernel Alignment (CKA), Feature Separability Scoring, and Layer-Wise Recovery Analysis. Through experiments across seven datasets and seven baseline methods following recent VFL unlearning protocols, Mirage reveals three key findings: (i) Forgetting gap: methods that pass output-level certification still retain substantial class structure in their representations, with LPR exceeding the retrained baseline by up to 15.4 points; CKA shows these models remain structurally closer to the original than to the retrained reference, while separability scores indicate persistent geometric discrimination. (ii) Unlearning trilemma: no existing method simultaneously achieves high utility, output-level forgetting, and representation-level forgetting. (iii) Class-sample asymmetry: class-level forgetting leaves strong representational traces (LPR up to 97%), whereas sample-level forgetting is indistinguishable from chance (LPR approx. 50%); layer-wise analysis further shows residual class information persists across network depths. These findings call for representation-aware evaluation standards in federated unlearning research.

---


### 22. [JUDO: A Juxtaposed Domain-Oriented Multimodal Reasoner for Industrial Anomaly QA](https://arxiv.org/abs/2605.20284)

**<font color=#1a73e8>作者：</font>** Hyunju Kang, Woohyun Lee, Jaewon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection has been significantly advanced by Large Multimodal Models (LMMs), enabling diverse human instructions beyond detection, particularly through visually grounded reasoning for better image understanding. However, LMMs lack domain-specific knowledge, which limits their ability to generate accurate responses in complex industrial scenarios. In this work, we present JUDO, Juxtaposed Domain-Oriented Multimodal Reasoner, a framework that efficiently incorporates domain knowledge and context in visual and textual reasoning. Through visual reasoning, our model segments the defect region by juxtaposing query images with normal images as visual domain context, enabling a fine-grained visual comparative inspection. Furthermore, we inject domain knowledge through supervised fine-tuning (SFT) to enhance context understanding and subsequently guide domain reasoning through reinforcement learning (GRPO) with tailored rewards, opting for a domain-oriented reasoning process. Experimental results demonstrate that JUDO achieves superior performance on the MMAD benchmark, surpassing models such as Qwen2.5-VL-7B and GPT-4o. These results highlight the importance of enhancing domain knowledge and context for effective reasoning in anomaly understanding.

---


### 23. [Introspective X Training: Feedback Conditioning Improves Scaling Across all LLM Training Stages](https://arxiv.org/abs/2605.20285)

**<font color=#1a73e8>作者：</font>** Brandon Cui, Ximing Lu, Jaehun Jung 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We tackle the question of how to scale more efficiently across the many, ever-growing stages of current LLM training pipelines. Our guiding intuition stems from the fact that the dynamics of later stages of the pipeline, e.g. post-training, can be used to inform earlier stages such as pre-training. To this end, we propose Introspective Training (or IXT), inspired by offline reward-conditioned reinforcement learning and applicable to any stage of training. IXT uses a thinking reward model to annotate data with natural language critique based feedback, enabling quality aware training from the earliest stages of the pipeline. Models are then trained by prefix-conditioning the data with the generated feedback -- ensuring that not all tokens are treated equally starting much earlier in training than usual. Comprehensive experiments on 7.5-12B transformer-based dense LLMs trained from scratch all the way up to 18 Trillion tokens seen show that our method: bends scaling curves resulting in up to 2.8x more compute efficiency generally; and reaches performance levels unachievable for models trained otherwise in domains such as math and code.

---


### 24. [Plug-and-Play Spiking Operators: Breaking the Nonlinearity Bottleneck in Spiking Transformers](https://arxiv.org/abs/2605.20289)

**<font color=#1a73e8>作者：</font>** Xinzhe Yuan, Xiang Peng, Bin Gu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ANN-to-SNN conversion offers a practical, training-free route to spiking large language models. However, current pipelines primarily focus on spike-driven realizations for Transformer linear-algebra operations, while providing limited support for key nonlinear operators. This gap limits compatibility with neuromorphic-style execution constraints, where such nonlinearities typically require division, exponentiation, or norm computations that are not naturally supported by standard leaky integrate-and-fire dynamics. To solve this problem, we propose a plug-and-play framework that implements spike-friendly approximations for Transformer nonlinearities and integrates into existing ANN-to-SNN pipelines. Our method decomposes these nonlinear computations into three recurring primitives -- division, exponentiation, and $\ell_2$ norms -- and realizes them via population computation using LIF neuron groups, combined with lightweight bit-shift scaling to avoid floating-point arithmetic. By composing these primitives as modular operator blocks, our framework supports common Transformer nonlinearities (e.g., Softmax, SiLU, and normalization) without any fine-tuning. Experiments on a range of LLMs Transformers show that selectively replacing the targeted nonlinear operators incurs less than a $1\%$ accuracy drop across all evaluated tasks.

---


### 25. [Weasel: Out-of-Domain Generalization for Web Agents via Importance-Diversity Data Selection](https://arxiv.org/abs/2605.20291)

**<font color=#1a73e8>作者：</font>** Fatemeh Pesaran zadeh, Seyeon Choi, Xing Han Lù 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have enabled web agents that follow natural language goals through multi-step browser interactions. However, agents fine-tuned on specific trajectories and domain often struggle to generalize out of domain, and offline training can be compute-inefficient due to noisy, redundant trajectories and long accessibility-tree (AXTree) states. To address both issues, we propose Weasel, a trajectory selection method for offline training of web agents. Weasel selects a fixed-budget subset of trajectory steps by optimizing an objective that balances unary importance with pairwise diversity over states, websites, and interaction patterns, solving efficiently with a greedy algorithm. We further improve efficiency with target-centered AXTree pruning that keeps only content around the ground-truth action target, and we mitigate style mismatch for reasoning-native models by replacing expert traces with model-generated, style-consistent rationales. Across AgentTrek and NNetNav training datasets, evaluations in WebArena, WorkArena, and MiniWob, and experiments with Qwen2.5-7B, Gemma3-4B, and Qwen3-8B, Weasel improves out-of-domain performance while reducing training cost, producing roughly 9.7-12.5$\times$ training speedups over standard fine-tuning. We make the code available at this https URL.

---


### 26. [Quant.npu: Enabling Efficient Mobile NPU Inference for on-device LLMs via Fully Static Quantization](https://arxiv.org/abs/2605.20295)

**<font color=#1a73e8>作者：</font>** Jinghe Zhang, Daliang Xu, Chenghua Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed on mobile devices, where Neural Processing Units (NPUs) necessitate fully static quantization for optimal inference efficiency. However, existing post-training quantization (PTQ) methods predominantly rely on dynamic activation quantization, rendering them incompatible with NPU hardware constraints. To bridge the gap between high-fidelity PTQ and NPU-constrained inference, we propose this http URL, a integer-only fully static quantization framework. It incorporates learnable quantization parameters and rotation matrices, enabling low-bit activation-weight quantization without runtime quantization parameters re-computation. Crucially, we identify that initialization and selective optimization of quantization parameters is pivotal for optimization stability, as improper initialization and naive joint optimization induce gradient instability that disrupts the optimization of rotation matrices. To address this, we propose a rotation-and-bit-width-aware initialization tailored to diverse activation profiles and a distribution-aware selective optimization (two-stage quantization pipeline) tailored to rotated and unrotated tensors. Furthermore, we introduce a sensitivity-guided adaptive mixed-precision scheme to balance accuracy with inference efficiency. Extensive experiments on real-world mobile NPUs demonstrate that this http URL achieves comparable accuracy to state-of-the-art methods, while reducing inference latency by up to 15.1%.

---


### 27. [Spectral Unforgetting: Post-Hoc Recovery of Damaged Capabilities Without Retraining](https://arxiv.org/abs/2605.20296)

**<font color=#1a73e8>作者：</font>** Aarash Abro, Muhammad Tahir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a language model for a target task routinely degrades capabilities the training data never explicitly threatened. We study this phenomenon, known as catastrophic forgetting, and propose a post-hoc repair solution that uses only the pretrained checkpoint $W_{\mathrm{base}}$ and its fine-tuned descendant $W_{\mathrm{ft}}$. The goal is not merely to revert the model toward the base checkpoint, but to recover capabilities damaged by fine-tuning while preserving both the target-task gains and any beneficial held-out improvements. We introduce DG-Hard, a checkpoint-only spectral repair method for the fine-tuning update $\Delta = W_{\mathrm{ft}} - W_{\mathrm{base}}$. DG-Hard treats $\Delta$ as a low-rank task-aligned signal embedded in an IID-like noise residual that gradient descent has no incentive to remove, and applies the Donoho-Gavish hard singular-value threshold to each weight-delta matrix, keeping the structured high-energy part of the update and removing the spectral bulk. This reduces repair to a closed-form SVD filtering step requiring no data-dependent tuning. A central difficulty is evaluation: average accuracy hides per-benchmark failures, while naive recovery scores reward models that simply revert toward the base. We therefore introduce a partition-conditional metric that separately tracks healing, preservation, non-damage, and target-task retention. Across $14$ (model, task) settings and nine cross-domain held-out benchmarks, DG-Hard achieves the strongest balanced repair among post-hoc baselines. DG-Hard also restores safety alignment degraded by benign fine-tuning on three independent safety axes, despite using no alignment data. These results suggest that part of fine-tuning-induced capability loss is not an unavoidable consequence of specialization, but a removable spectral residue in the weight update itself.

---


### 28. [WildRoadBench: A Wild Aerial Road-Damage Grounding Benchmark for Vision-Language Models and Autonomous Agents](https://arxiv.org/abs/2605.20306)

**<font color=#1a73e8>作者：</font>** Bingnan Liu, Chenhang Cui, Rui Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce WildRoadBench, a wild aerial road-damage grounding benchmark that couples direct visual grounding by vision-language models with autonomous research-and-engineering by LLM-driven agents on a single professionally annotated UAV corpus. The same image set and the same per-class AP_50 metric are evaluated under two protocols. The VLM Track measures whether a fixed VLM can localise domain-specific damage from one image and one short prompt under a unified prompting, decoding and parsing pipeline. The Agent Track measures whether an autonomous agent, given only a written task brief, a small exploratory slice and a fixed interaction budget, can search the public web, adapt pretrained components, write training and inference code, and submit predictions through a scalar-feedback oracle on a hidden holdout. We benchmark a broad pool of closed-source frontier models and open-source VLMs together with several frontier LLM-driven agents. Both routes remain far from reliable performance in this wild setting: closed-source frontier models lead the VLM leaderboard but still leave more than half of the metric on the table; open-source grounders plateau well below them, and newer generations or reasoning-style variants do not consistently improve grounding; small targets collapse for every open-source model; agents lag the strongest VLM despite richer affordances, and several fail to land a valid submission within the budget. We release the code and data at this https URL to support reproducible follow-up research.

---


### 29. [Mix-Quant: Quantized Prefilling, Precise Decoding for Agentic LLMs](https://arxiv.org/abs/2605.20315)

**<font color=#1a73e8>作者：</font>** Haiquan Lu, Zigeng Chen, Gongfan Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents have recently emerged as a powerful paradigm for solving complex tasks through planning, tool use, memory retrieval, and multi-step interaction. However, these agentic workflows often introduce substantial input-side overhead, making the compute-intensive prefilling stage a key bottleneck in long-context, multi-turn inference. In this work, we propose Mix-Quant, a simple and effective phase-aware quantization framework for fast agentic inference. We first investigate FP4 quantization in agentic LLM workflows and observe that quantizing the entire inference process can incur significant performance degradation. In contrast, the prefilling stage exhibits substantial quantization redundancy and can therefore be quantized with minimal accuracy loss, despite being the dominant source of computation. Based on this insight, we apply high-throughput NVFP4 quantization to the prefilling phase while preserving BF16 precision for decoding. By decoupling prefilling acceleration from decoding quality, Mix-Quant combines phase-aware algorithmic quantization with hardware-efficient NVFP4 execution to alleviate the inference bottleneck in LLM agents. Extensive experiments across long-context and agentic benchmarks demonstrate that Mix-Quant largely preserves task performance while delivering significant efficiency improvements, achieving up to a 3x speedup during prefilling.

---


### 30. [Capability $\neq$ Interpretability: Human Interpretability of Vision Foundation Models](https://arxiv.org/abs/2605.20337)

**<font color=#1a73e8>作者：</font>** Julien Colin, Lore Goetschalckx, Nuria Oliver 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How interpretable are the features of leading vision models? The question is increasingly pressing as these models move from research benchmarks into high-stakes deployments, yet existing methods cannot answer it reliably. We close this gap with a framework for measuring and comparing the human interpretability of vision models, built around two complementary psychophysics protocols: (1) localizability -- can an observer predict where a feature fires on a novel image? -- and (2) nameability -- can an observer accurately describe what the feature represents? Features are recovered via sparse autoencoders, and a chance-anchored scoring function places every model on a common scale. Applying the framework to six vision transformers -- two supervised ViTs and four foundation models (DINOv2, DINOv3, CLIP, SigLIP) -- we collected more than $15{,}000$ behavioral responses, analyzing the $13{,}400$ responses from the $377$ participants who passed our pre-specified quality checks. Foundation models are consistently *less* interpretable than their supervised counterparts, and the gap is not a capability tradeoff: interpretability does not correlate with downstream task performance on any benchmark we examine. What does correlate is the locality of a feature's activations and coarse-grained semantic alignment with humans -- models with focal activations and representations that reflect the world's broad categorical structure produce more interpretable features, whereas fine-grained perceptual alignment does not. The two protocols yield strongly correlated rankings and share the same predictors, establishing interpretability as an independent, measurable dimension of representation quality -- and, surprisingly, one on which every foundation model we tested falls below the supervised baselines that came before. Capability alone cannot close that gap; locality and coarse-grained alignment can.

---


### 31. [ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Reinforcement Learning](https://arxiv.org/abs/2605.20342)

**<font color=#1a73e8>作者：</font>** Zuhao Yang, Kaichen Zhang, Sudong Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training large multimodal models (LMMs) via reinforcement learning (RL) to natively invoke video-processing tools (e.g., cropping) has become a promising route to long-video understanding. However, existing native-RL methods dispatch tool calls sequentially (i.e., one per turn): a single wrong crop propagates errors without peer correction, multi-turn tool calls corrupt context, and inference cost scales linearly with the number of turns. We introduce ParaVT, the first multi-agent end-to-end RL-trained framework for Parallel Video Tool calling, dispatching multiple time-window crops in a single turn for cleaner context and better fault tolerance. Yet applying standard RL to ParaVT reveals an obstacle we term the Tool Prior Paradox: the pretrained tool priors that enable tool exploration also destabilize cold-started structural format and expose the skip-tool reward shortcut under temperature sampling. A cross-model contrast on a weaker-prior LMM supports this claim: format stays stable but RL elicits zero tool calls, indicating that prior strength is the shared driver of both format collapse and tool exploration. We propose PARA-GRPO (Parseability-Anchored and Ratio-gAted GRPO), which augments standard RL with two complementary mechanisms: (i) a targeted format reward applied only at the structural-token positions most prone to collapse, and (ii) a per-prompt frame-budget randomization that creates training prompts where calling the tool yields a measurable reward signal over skipping it. Across six long-video understanding benchmarks, ParaVT improves over the Qwen3-VL baseline by +7.9% on average, with PARA-GRPO lifting training-time format compliance from 0.13 to 0.64. As tool capabilities become increasingly internalized in modern LMMs, RL must cooperate with the resulting priors, and ParaVT offers a general recipe for agentic RL. Code, data, and model weights are publicly available.

---


### 32. [DEL: Digit Entropy Loss for Numerical Learning of Large Language Models](https://arxiv.org/abs/2605.20369)

**<font color=#1a73e8>作者：</font>** Zhaohui Zheng, Chenhang He, Shihao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Number prediction stands as a fundamental capability of large language models (LLMs) in mathematical problem-solving and code generation. The widely adopted maximum likelihood estimation (MLE) for LLM training is not tailored to number prediction. Recently, penalty-driven approaches, e.g., Number Token Loss and Discretized Distance Loss, introduce an inductive bias of numerical distance but induce over-sharpened and over-flattened digit distributions, respectively. In this paper, we make an in-depth analysis on LLM numerical learning, and show that existing numerical learning methods conceptually follow a criterion-distance formulation, where the criterion term represents optimization pattern and the distance term instills geometric prior. Consequently, we present Digit Entropy Loss (DEL) for auto-regressive numerical learning, which reformulates the conventional unsupervised entropy optimization in three key designs: leveraging digit conditional probability and binary cross-entropy to guide the entropy optimization into a supervised manner; deprecating the distance term to bypass the issue of numerical distance; and generalizing the integer-based numerical learning to floating-point number optimization, enabling more accurate number prediction. Our DEL formulation can incorporate integers, decimals, and decimal points, expanding the learning objective from a single digit to the floating-point number domain. Experiments conducted on seven mathematical reasoning benchmarks with four representative LLMs, including CodeLlama, Mistral, DeepSeek, and Qwen-2.5, demonstrate that DEL consistently outperforms its counterparts in both overall prediction accuracy and numerical distance. Source codes are at this https URL

---


### 33. [Latent Space Guided Scenario Sampling for Multimodal Segmentation Under Missing Modalities](https://arxiv.org/abs/2605.20372)

**<font color=#1a73e8>作者：</font>** Irem Ulku, Ö. Özgür Tanrıöver, Erdem Akagündüz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal semantic segmentation benefits remote sensing analysis by combining complementary information from different sensor modalities. In real-world remote sensing applications, one or more modalities may be unavailable due to sensor failures, adverse atmospheric conditions, or data acquisition problems. Even with pretrained multimodal representations and existing fine-tuning or adaptation strategies, performance may remain limited because all modality availability scenarios are typically treated as equally informative during training. In this paper, we propose a novel training strategy that learns a scenario sampling distribution directly from the pretrained latent space. Instead of relying on uniform random modality dropout, the proposed method guides fine-tuning toward more informative modality availability scenarios. More specifically, we quantify the effect of each scenario independently based on the distortion it induces in the shared latent representation. We then capture scenario relations using a radial basis function kernel and derive refined scenario scores through a regularized kernel smoothing. These scores are then converted into a probability distribution during scenario sampling for fine-tuning. We evaluate this strategy on three remote sensing image sets, namely DSTL, Potsdam, and Hunan, using CBC-SLP, CBC, and CMX backbones. The experimental results with different image sets and backbones show that our method outperforms standard fine-tuning and LoRA-based adaptation. These findings suggest that the pretrained latent representation can serve as an effective basis for sampling during missing modality fine-tuning. Code is available at this https URL

---


### 34. [Do as I Say, Not as I Do: Instruction-Induction Conflict in LLMs](https://arxiv.org/abs/2605.20382)

**<font color=#1a73e8>作者：</font>** Carolina Camassa, Derek Shiller  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are trained to follow instructions, but they are also powerful pattern completers. What happens when these two objectives conflict? We construct conversations in which a user instruction to behave in a target way T (e.g., always output a specific token, answer in a particular language, or adopt a persona) is opposed by N hardcoded assistant turns demonstrating a competing pattern P. We then measure instruction-following (IF) rates in this setting, across 13 models and 16 different instructions, for up to 50 turns. Average instruction-following rates range from 1% to 99% across models, largely uncorrelated with standard capability benchmarks. The transition from instruction-following to pattern-following is universal but highly model-dependent. Robustness is modulated both by instruction content, with models resisting induction longer when instructions align with their trained value priors, and by output format, with diverse multi-token responses proving substantially more resistant than single-token outputs. Chain-of-thought reasoning improves robustness but does not eliminate susceptibility, and can produce dissociation between correct deliberation and incorrect output. When asked to predict their behavior in this setting, models achieve 83.5% accuracy on average but systematically underestimate their own resistance to induction pressure. These results suggest that instruction-following remains brittle under induction pressure even for otherwise capable models, and that output diversity, rather than semantic engagement with the input, is the primary factor predicting robustness.

---


### 35. [Decomposing MXFP4 quantization error for LLM reinforcement learning: reducible bias, recoverable deadzone, and an irreducible floor](https://arxiv.org/abs/2605.20402)

**<font color=#1a73e8>作者：</font>** Xiaocan Li, Shiliang Wu, Zheng Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MXFP4 arithmetic can dramatically accelerate reinforcement learning (RL) post-training of large language models (LLMs), yet the quantization error introduces severe accuracy degradation. Existing work treats the quantization error as a monolithic noise term, missing the distinct mechanisms upon interpreting how quantization error damages training. We prove an exact three-way decomposition of quantization error and show how each component dominates a distinct RL training pathway. Our theoretical and empirical analysis decomposes the MXFP4 quantization error into three additive components: "scale bias" from power-of-two rounding, "deadzone truncation" from zeroing small values, and "grid noise" from rounding to the nearest 4-bit grid. Each component dominates a distinct RL failure mode: scale bias accumulates multiplicatively through the backward pass, affecting gradient accuracy; deadzone truncation degrades rollout quality; and grid noise raises the policy's entropy. We combine corrections that are RL failure mode-targeted but not component-exclusive: Macro-block scaling to reduce scale bias, Outlier Fallback recovers deadzone entries, but also partially reduces scale bias induced error, and Adaptive Quantization Noise (AQN) for controlling the policy entropy. On Qwen2.5-3B dense and Qwen3-30B-A3B-Base mixture-of-experts model, the targeted corrections recover BF16 accuracy to within 0.7% and 3.0% respectively.

---


### 36. [Puzzled By ChatGPT? No more! A Jigsaw Puzzle to Promote AI Literacy and Awareness](https://arxiv.org/abs/2605.20404)

**<font color=#1a73e8>作者：</font>** Francesca Padovani, Malvina Nissim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of Generative AI, including LLM-based chatbots like ChatGPT, has highlighted the need for accessible ways to support public understanding and AI literacy. To address this need, we introduce a game-based, interactive approach in the form of a jigsaw puzzle whose completed image is a comic-based infographic illustrating the workings, capabilities, limitations, and societal implications of these technologies. Each comic sketch also functions as a standalone informational card, providing focused explanations of specific facets of AI use, design, and impact. The visual content was created in a live collaborative session with a professional illustrator and a multidisciplinary group of experts and non experts, combining structured knowledge with informal, exploratory reflections shared during the discussion. By integrating hands-on assembly, visual storytelling, and collaborative interaction, the puzzle provides an engaging and playful tool for exploring the mechanisms, perks, and perils of AI systems in informal learning contexts.

---


### 37. [Spectral Souping: A Unified Framework for Online Preference Alignment](https://arxiv.org/abs/2605.20408)

**<font color=#1a73e8>作者：</font>** Yinlam Chow, Guy Tennenholtz, Ted Yun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Human Feedback (RLHF) effectively aligns Large Language Models (LLMs) with aggregate human preferences but often fails to address the diverse and conflicting needs of individual users. To overcome this issue, we introduce Spectral Souping, a unified framework for efficient, online preference alignment. Our contribution is the discovery of a universal spectral representation within LLMs, which is proven to be highly amenable to model merging. This theoretical insight enables a two-phase methodology: we first learn a basis of specialized policies offline, each focused on a distinct, fine-grained preference dimension. An online adaptation algorithm then efficiently ``soups'' these policies at inference time, either by merging their outputs or parameters, enabling rapid model adaptation without the need for costly online retraining w.r.t. tailored preference rewards. Experiments on online preference alignment benchmarks demonstrate that our method achieves significant performance improvements over existing state-of-the-art approaches, presenting a scalable and computationally efficient solution for dynamically adapting LLMs to individual user preferences.

---


### 38. [Mechanics of Bias and Reasoning: Interpreting the Impact of Chain-of-Thought Prompting on Gender Bias in LLMs](https://arxiv.org/abs/2605.20410)

**<font color=#1a73e8>作者：</font>** Edie Pearman, Sophia Osborne, Mira Kandlikar-Bloch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in socially sensitive settings despite substantial documentation that they encode gender biases. Chain-of-Thought (CoT) prompting has been proposed as a bias-mitigation approach. However, existing evaluations primarily focus on changes in LLM benchmark performance, providing limited insight into whether apparent bias reductions reflect meaningful changes in a model's internal mechanisms. In this work, we investigate how CoT prompting affects gender bias in LLMs, combining benchmark-based evaluation with mechanistic interpretability techniques and reasoning chain failure analysis. Our results confirm a stereotypical bias present in LLM outputs across benchmarks, showing that CoT prompting does not consistently reduce the bias gap. Mechanistic analyses reveal that although CoT balances biased behavior in certain attention head clusters, gender bias remains embedded in hidden representations, indicating only superficial mitigation. Inspection of reasoning chains further suggests that these improvements stem from memorization and familiarity with the dataset rather than genuine understanding of bias.

---


### 39. [Miller-Index-Based Latent Crystallographic Fracture Plane Reasoning with Vision-Language Models](https://arxiv.org/abs/2605.20416)

**<font color=#1a73e8>作者：</font>** Qinwu Xu, Yifan Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether multimodal large language models (MLLMs) can leverage crystallographic plane indices (Miller indices) as a structured latent representation for reasoning about fracture geometry. We formulate Miller indices $z = (h,k,l)$ as a latent variable governing idealized planar fracture and evaluate two complementary capabilities: (i) latent inference, where the model maps visual observations to plane hypotheses under physically valid conditions, and (ii) latent applicability assessment, where the model determines whether such a representation is meaningful for a given fracture image.
Through extensive experiments spanning synthetic data, controlled 2D--3D geometric pairs, and real-world fracture images across multiple material classes -- including ceramics, glass, metals, and concrete -- we show that MLLMs can reliably perform latent inference in idealized settings and, critically, can reject the latent representation when the underlying physics does not support it. These results suggest that MLLMs can act as physics-aware reasoning systems conditioned on structured latent priors, provided that the domain of validity is explicitly modeled.

---


### 40. [Do Vision--Language Models Understand 3D Scenes or Just Catalogue Objects?](https://arxiv.org/abs/2605.20448)

**<font color=#1a73e8>作者：</font>** Animesh Maheshwari, Divyansh Sahu, Nishit Verma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision--language models reliably name objects in a scene, but do they represent the 3D layout those objects inhabit? We introduce a 3,034-sample human-curated benchmark targeting three components of spatial understanding: depth-ordered occlusion (probed via three independent counterfactual operationalisations), optical-geometry inference over visible reflections, and volumetric rearrangement planning. Six frontier and open-weight VLMs, scored by trained annotators on 18,204 responses with no LLM-as-judge, reveal a sharp dissociation: models that plan rearrangements over visible layouts at 53--97% accuracy and rarely violate collision constraints fall to 6--45% on occlusion and below 7% on reflections. An embodied-reasoning model reproduces the same profile. White-box analysis on Qwen3-VL-8B-Thinking localises the failure to the visual-token merger: spatial information recoverable throughout the vision encoder becomes inaccessible after token compression and only stabilises again when clean post-merger activations are patched into the language decoder.

---


### 41. [LLM Pretraining Shapes a Generalizable Manifold: Insights into Cross-Modal Transfer to Time Series](https://arxiv.org/abs/2605.20449)

**<font color=#1a73e8>作者：</font>** Alexis Roger, Prateek Humane, Zhenghan Tai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can language-pretrained transformers become effective time-series forecasters, and why? In this paper, we show that cross-modal transfer arises because language pretraining preconditions time series training with a reusable manifold. A linear probe on frozen LLM states decodes realistic time-series trajectories without paired supervision, and retrieval in this projected space yields competitive forecasts, showing that structure and dynamics exist before finetuning. Pretrained initialization also improves optimization, producing coherent gradients and a highly anisotropic loss landscape unlike random initialization. Finetuning then acts as low-dimensional alignment, reusing existing directions rather than learning temporal primitives from scratch, as evidenced by low-rank updates, subspace alignment, and shared features for periodicity, trend, and repetition. Together, these results support a geometric account of LLM-to-time-series transfer: language pretraining builds the manifold, and finetuning projects numerical dynamics onto task-relevant directions.

---


### 42. [HalluCXR: Benchmarking and Mitigating Hallucinations in Medical Vision-Language Models for Chest Radiograph Interpretation](https://arxiv.org/abs/2605.20469)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Zitong Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used for medical image interpretation, yet they frequently hallucinate, generating clinically plausible but factually incorrect findings that pose direct patient safety risks. We introduce HalluCXR, a benchmark evaluating six architecturally diverse VLMs across 856 stratified MIMIC-CXR chest radiographs and three query types, yielding 15,408 model evaluations. An eight-category hallucination taxonomy with clinical severity ratings and a two-layer detection pipeline are validated against 250 human annotations (auto-detection F1=0.959; LLM judge F1=0.907). We find that 61.9--82.3% of outputs contain hallucinations, with clinically dangerous errors in up to 80.2%. Three key patterns emerge: normal radiographs paradoxically attract the most severe hallucinations, common findings are systematically over-fabricated while rare findings go under-detected, and response length alone predicts hallucination risk (AUC up to 0.908). A six-model ensemble reduces fabrication by up to 84.8% at the cost of increased omission; a three-model subset retains comparable performance at half the cost. These results establish that hallucination auditing, verbosity-based risk monitoring, and ensemble-based safety layers are prerequisites for clinical deployment.

---


### 43. [ZEBRA: Zero-shot Budgeted Resource Allocation for LLM Orchestration](https://arxiv.org/abs/2605.20485)

**<font color=#1a73e8>作者：</font>** May Hamri, Inbal Talgam-Cohen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As autonomous agents increasingly execute end-to-end tasks under fixed monetary budgets, the pressing open question shifts from whether the budget is respected, to how to spend it effectively. Existing budget-aware methods typically control reasoning step-by-step within a single agent, or learn resource allocation policies via RL. None address how to split a budget across the composing phases of a multi-agent pipeline at inference time. We propose ZEBRA, a zero-shot framework that reduces multi-phase budget allocation to a continuous nonlinear knapsack problem: an LLM controller estimates per-phase utility curves, and a water-filling search on the Lagrange multiplier returns the per-phase split. Additive and multiplicative aggregations are unified under the same solver. On a $150$-task APPS coding benchmark, both ZEBRA variants outperform LLM-direct (budget allocation directly by an LLM) on every aggregate metric. At a budget of $\alpha = 0.5$ of the unconstrained spend, ZEBRA recovers $94.4\%$ of unconstrained quality, versus $88.1\%$ for LLM-direct. The advantage is statistically significant and transfers beyond coding: on a $3$-phase HotpotQA pipeline, ZEBRA beats LLM-direct by $14.3$pp, with allocations empirically robust to curve-estimation noise. On HotpotQA, ZEBRA arrives at a different budget split (near-balanced) compared to the APPS one (skewed towards a refinement phase), showing adaptation to the pipeline structure. More broadly, we show that lightweight algorithmic guidance at inference time can improve the economic behavior of autonomous multi-agent systems.

---


### 44. [A Human-in-the-Loop Framework for Efficient Prompt Selection in Microscopy Vision-Language Models](https://arxiv.org/abs/2605.20495)

**<font color=#1a73e8>作者：</font>** Abhiram Kandiyana, Ankur Mali, Lawrence O. Hall 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep-learning pipelines for microscopy image classification often require expensive, labor- and time-intensive expert annotation to produce high-quality ground truth for training. Recent work has shown that prompt tuning of vision-language models (VLMs) can reduce manual annotation by constructing a small prompt set of expert-verified image-caption exemplars that is reused as few-shot context to classify all remaining images at inference time. To further reduce effort, the VLM can draft captions for candidate exemplars, which experts then verify and lightly edit instead of writing text de novo. However, two practical questions remain unaddressed: (1) which unlabeled images should be prioritized for verification, and (2) how many verified exemplars are needed to reach a performance target. In this work, we address these questions by formulating prompt-set construction as a target-driven active learning problem that prioritizes which images to annotate. We study three complementary selection criteria under strict low-resource constraints with small unlabeled pools. Experiments show that our methods reach the target performance with substantially fewer expert-verified images than random selection, achieving 100% test accuracy with as few as 20 annotated images on average. More broadly, our human-in-the-loop framework demonstrates a human-centered use of generative AI in biomedical image analysis, where experts remain actively involved in verifying and refining model output while significantly reducing annotation cost. Code and data will be publicly available.

---


### 45. [Framing an AI with Values Reduces AI Reliance in AI-supported Writing Tasks](https://arxiv.org/abs/2605.20512)

**<font color=#1a73e8>作者：</font>** Alice Gao, Andrew N. Meltzoff, Maarten Sap 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite a global user base adopting large language models (LLMs) for daily writing tasks, model suggestions tend to align with Western values. Research has shown users commonly accept a high fraction of these AI suggestions, homogenizing writing styles and rendering outputs more ``Western'' than intended. While this suggests a need to reduce AI reliance, it remains unknown what kind of interventions could achieve this. Can framing the AI with specific values, and comparing it to one's own, make users less susceptible to overreliance and support more unique writing? We tested this hypothesis in a between-subjects online experiment with Indian and American participants (n=149) in which they were asked to perform AI-supported writing tasks, either 1) without an intervention, 2) after seeing an overview of the AI's framed values, or 3) after seeing an overview of the AI's framed values compared to their own. Our results show that seeing the AI's framed values reduces AI reliance, i.e., the proportion of the final essay generated by the AI, by an average of 20\%. Additionally, when participants saw an overview of the AI's framed values (without comparison to their own values), the final essays contain more unique text than without intervention. Our findings emphasize the importance of educating users about potential value biases in AI, showing that raising awareness with a simple overview of values encourages users to personalize their writing.

---


### 46. [An exponential mechanism based on quadratic approximations for fine-tuning machine learning models with privacy guarantees](https://arxiv.org/abs/2605.20521)

**<font color=#1a73e8>作者：</font>** Hoang Tran, Jorge Ramirez, Jiayi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning adapts a pretrained machine learning model to a small, sensitive dataset, but this process risks memorizing individual new data points, making the model vulnerable to adversaries who seek to extract sensitive information. In this work, we develop a randomized algorithm based on the exponential mechanism for fine-tuning while ensuring differential privacy. Our key idea is to construct a simple utility function that combines a local quadratic approximation of the pretrained model with information from the new dataset. The resulting exponential mechanism admits exact sampling from a multivariate normal distribution in closed form. We establish theoretical privacy guarantees, sensitivity bounds, and accuracy estimations for our method. We further introduce a random-projection strategy that makes the approach scalable to high-dimensional models. Numerical experiments on the MNIST benchmark and the MIMIC clinical dataset demonstrate competitive performance against existing differentially private fine-tuning techniques.

---


### 47. [Machine-Learning-Enhanced Non-Invasive Testing for MASLD Fibrosis: Shallow-Deep Neural Networks Versus FIB-4, Tabular Foundation Models, and Large Language Models](https://arxiv.org/abs/2605.20523)

**<font color=#1a73e8>作者：</font>** Athanasios Angelakis, Gabriele De Vito, Eleni-Myrto Trifylli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advanced fibrosis is a major determinant of liver-related morbidity in metabolic dysfunction-associated steatotic liver disease (MASLD). FIB-4 is widely used as a first-line non-invasive test, but its fixed formula may underuse diagnostic information contained in age, aspartate aminotransferase, alanine aminotransferase, and platelet count. We evaluated whether machine-learning-enhanced non-invasive testing (MLE-NIT) can improve advanced fibrosis detection while preserving this FIB-4 variable space.
We used three biopsy-confirmed MASLD cohorts from China, Malaysia, and India (n=784). The Chinese cohort was split into 486 training and 54 internal validation/tuning patients; final performance was reported only on the Malaysian and Indian external cohorts. Models used five variables: age, FIB-4, aspartate aminotransferase, platelet count, and alanine aminotransferase. We compared FIB-4 with a shallow-deep neural network (s-DNN), TabPFN, and gpt-4o-2024-08-06.
FIB-4 achieved external ROC-AUCs of 0.75 and 0.60 in Malaysia and India, respectively. TabPFN achieved 0.69 and 0.66, fine-tuned GPT-4o achieved 0.75 and 0.63, and the s-DNN achieved 0.77 and 0.67, respectively. The s-DNN contained only 354 trainable parameters, compared with 7,244,554 for TabPFN, yet provided a more balanced external operating profile. Calibration showed s-DNN Brier scores of 0.18 and 0.22, and permutation importance identified AST and FIB-4 as dominant variables. Compact non-linear MLE-NITs may enhance FIB-4-based fibrosis assessment without increasing clinical data requirements.

---


### 48. [AgentAtlas: Beyond Outcome Leaderboards for LLM Agents](https://arxiv.org/abs/2605.20530)

**<font color=#1a73e8>作者：</font>** Parsa Mazaheri, Kasra Mazaheri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents now act on codebases, browsers, operating systems, calendars, files, and tool ecosystems, but the benchmarks used to evaluate them are fragmented: each emphasizes a different unit of measurement (final task success, tool-call validity, repeated-pass consistency, trajectory safety, or attack robustness). A line of 2024-2025 work has converged on the diagnosis that a single accuracy column is no longer the right unit of comparison for deployable agents. AgentAtlas extends this line of work with four components: (i) a six-state control-decision taxonomy (Act / Ask / Refuse / Stop / Confirm / Recover); (ii) a nine-category trajectory-failure taxonomy with two orthogonal hierarchical labels (primary_error_source, impact); (iii) a taxonomy-aware vs. taxonomy-blind methodology that measures how much of a model's apparent capability comes from the supervision in the prompt; and (iv) a benchmark-coverage audit mapping fifteen agent benchmarks against six behavioral axes. To demonstrate the methodology we run a small fixed eight-model set (1,342 generated items, four frontier closed and four open-weight) under both prompt modes. Removing the explicit label menu drops every model's trajectory accuracy by 14-40 pp to a tight 0.54-0.62 floor regardless of family, and no single model wins on all three of control accuracy, trajectory diagnosis, and tool-context utility retention. We treat the synthetic run as a measurement-protocol demonstration, not a benchmark release.

---


### 49. [Complementing reinforcement learning with SFT through logit averaging in the post training of LLMs](https://arxiv.org/abs/2605.20555)

**<font color=#1a73e8>作者：</font>** Xingwei Gan, Ying Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a novel method that averages the logits of a frozen reference policy (e.g., SFT) and a trainable policy, and incorporate the method into Group Relative Policy Optimization (GRPO). In contrast to Reinforcement Learning with Verifiable Rewards (RLVR) methods, our proposal does not involve a Kullback Leibler (KL) regularization or critic; the trainable policy and the reference anchor are coupled through the logit averaging structure to leverage the reasoning expertise of the trainable policy while maintaining the formatting advantage of SFT. Our method is evaluated on MATH, cn-k12, and MMLU, and the results show a higher accuracy or at least comparable accuracy relative to the canonical KL-regularized GRPO.

---


### 50. [QwenSafe: Multimodal Content Rating Description Identification via Preference-Aligned VLMs](https://arxiv.org/abs/2605.20584)

**<font color=#1a73e8>作者：</font>** Dishanika Denipitiyage, Aruna Seneviratne, Suranga Seneviratne  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile app marketplaces require developers to disclose standardized content rating descriptors (CRDs) to inform users about potentially sensitive or restricted content. Ensuring the accuracy and consistency of these disclosures remains challenging due to the multimodal nature of app content, which spans textual descriptions and visual interfaces. In this paper, we present QwenSafe, a Vision-Language Model (VLM) designed to automatically identify the presence of Apple-defined CRDs by jointly reasoning over app metadata and screenshots. To enable scalable training for this task, we introduce metadata2CRD, a data-construction pipeline that synthesizes descriptor-aligned question-answer pairs by combining app descriptions, screenshots, and formal descriptor definitions. We adapt Qwen3-VL-8B using supervised fine-tuning followed by Direct Preference Optimization (DPO) to align model predictions with descriptor-specific evidence and explanations across visual and textual modalities. We evaluate QwenSafe on 12 Apple-defined content rating descriptors and compare it against state-of-the-art vision-language models, including Qwen3-VL, LLaVA-1.6, and Gemini-2.5-Flash. QwenSafe consistently outperforms all baselines in binary CRD classification, achieving improvements in positive-class recall of 111.8%, 36.1%, and 2.1%, respectively. Our results demonstrate that descriptor-aware multimodal alignment substantially improves automated content classification and highlights the potential of vision-language models to support scalable and consistent content rating in mobile app marketplaces.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-143](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
