# 🧠 大模型相关研究 | 2026年11月25日

> 本类共 **486** 篇论文：已确认 **458** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

---

### 151. [When Rubrics Do Not Decide: Silent Value Completion in LLM Evaluation](https://arxiv.org/abs/2611.28940)

**<font color=#1a73e8>作者：</font>** Zhuangzhuang Pan, Yan Xia, Kaiwen Lei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-criterion LLM judges often evaluate responses without specifying how conflicting criteria resolve, leaving the winner undetermined even under exact criterion scores. Issuing a strict verdict without declaring the required trade-off premise constitutes silent value completion. We introduce TradeoffBench to isolate this failure by separating rule execution from response scoring. On authoritative criterion vectors, six open-weight non-reasoning judges pass all dominance and equality controls yet pick unsupported winners on 9%-81% of 1,345 conflicts. All 577 order-stable choices follow an explicitly banned majority rule. Reasoning-enabled configurations drop anonymous-vector violations to 2 in 9,720 judgments under an explicit rule, yet cannot bridge omitted trade-offs or divergent component scoring. On raw TradeoffBench text with unspecified trade-offs, GPT-6.1-sol omits its completion premise in 29.8% of 400 verified conflicts. Even under an explicit rule on four-rater-consensus MultiPref conflicts, four reasoning judges still issue strict verdicts on 16/45 (GPT-6.1-sol) up to 35/46 and 25/29 (open-weight judges) of valid presentations. We propose identified-first evaluation, decoupling specification support, explicit completion, and target agreement. In MultiPref human-score audits, peer-mean substitution raises directional disagreement from 0.6% to 28.8% on 2,707 shared targets. A single-peer ablation confirms a 29.38-point gap on 2,175 targets, ruling out averaging as the cause. In HUMAINE, declared partial trade-offs add 2.5 percentage points of coverage, yet newly decided pairs incur 3.9% disagreement versus 0.9% for Pareto. Reliable LLM judging, therefore, requires auditing, specification support, declared trade-offs, and human target agreement separately.

---


### 152. [Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents](https://arxiv.org/abs/2611.28947)

**<font color=#1a73e8>作者：</font>** Jiaqi Su, Jie-Jing Shao, Yichen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) built on vision-language models are increasingly entrusted with long-horizon tasks in live desktop, web, and mobile environments, where the screen keeps changing on its own. However, current CUAs lack real-time situational awareness: they perceive the environment through discrete snapshots, and the substantial inference latency of VLMs, compounded by highly dynamic interfaces, opens a perception-action gap in which the observed state frequently becomes stale before the corresponding action is executed. To bridge this gap, we present NightWatch, a plug-and-play framework that endows any CUA with continuous, temporally grounded perception without changing the agent's model, prompt, or action space. NightWatch couples the VLM agent with NightWatch-0.8B, a lightweight System-1 model that performs streaming monitoring of the interface state and keeps the agent synchronized with the evolving environment at low computational cost and latency, thereby grounding each decision in the current state rather than an outdated snapshot and reducing both stale actions and idle waiting while preserving task success. Experiments on desktop and dynamic web environments (OSWorld-Verified and DynaCU-Bench) show that NightWatch, driven by a watcher of only 0.8B parameters, reduces non-reasoning wall-clock time by 33% and wasted time by 53% on OSWorld while keeping task success on par, raises success on DynaCU-Bench from 39.5% to 44.2% with the large VLM agent, and is more efficient than passive-watching baselines such as AOI and PUSV under the same screenshot-only input, as well as a System-1 decision model more than $30\times$ its size. Overall, NightWatch demonstrates that the timing of perception is as critical as its content, marking a step toward agents that maintain continuous awareness of their environment rather than perceiving it turn by turn.

---


### 153. [EmoRouter: Adaptive Modality Cascading for Multimodal Emotion Recognition](https://arxiv.org/abs/2611.28960)

**<font color=#1a73e8>作者：</font>** Fangxu Yu, Lingzhi Yuan, Dehai Min 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Emotion Recognition (MER) involves detecting the underlying emotion behind each utterance within a conversation, which is essential for emotionally aware human-computer interaction. While omni-modal large language models (Omni-LLMs) demonstrate strong capability for MER by jointly processing modalities including text, audio, and vision, different modality combinations yield different prediction outcomes across utterances: acoustic and visual inputs can help recover annotated labels missed by text-only inference, but can also turn correct predictions into errors. Processing all modalities for every utterance is also computationally expensive. To this end, we introduce EmoRouter, a training-free, model-agnostic framework for adaptive modality cascading that selects an exit tier for each utterance along a predefined modality order. The routing is guided by prediction-uncertainty estimates derived from Conformal Prediction. EmoRouter routes each utterance through a sequence of increasing-cost modality levels and exits at the first level when the model is confident in the emotion. To determine when to exit, we propose Conformal Set Contraction, a structural calibration criterion that calibrates the per-tier CP error budgets used for these exit decisions. Comprehensive evaluations on 4 MER benchmarks and 3 Omni-LLMs reveal that EmoRouter matches or outperforms the full modalities while reducing inference latency by 67.9--94.5%. Furthermore, EmoRouter demonstrates high transferability across different models, validating its robustness. Code is available at this https URL.

---


### 154. [MolReJev: Decision Models Are In-Context Molecular Predictors](https://arxiv.org/abs/2611.28965)

**<font color=#1a73e8>作者：</font>** Kaiyuan Lu, Jiatong Li, Yatao Bian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular prediction helps prioritize compounds for screening. Specialized predictors are trained for a fixed set of tasks, limiting cross-task generalization. Language models can condition on task descriptions and have recently shown promise in molecular prediction. However, generating answers token by token adds inference cost, and general-purpose models often lack task-specific molecular knowledge. We thus propose MolReJev, which combines Jev-style candidate scoring with in-context learning (ICL) on a language model. MolReJev retrieves similar labeled examples from existing task data and scores candidate labels jointly in one forward pass. ICL improves predictions from the released general-purpose Kev checkpoint and the separately trained MolReJev. For the trained model, gains span all evaluation groups, including held-out tasks, and extend to compounds absent from training. MolReJev generally outperforms MolecularGPT on matched evaluations and nearest-neighbor prediction with the same examples. With four examples, MolReJev and a trained text baseline achieve similar ROC-AUC, with higher measured throughput for MolReJev. These results show that decision models can serve as in-context molecular predictors for compounds, drug pairs, and reactions.

---


### 155. [What the Background Hides: Thresholds, Vocabularies and Collisions in Training-Free Open-Vocabulary Segmentation](https://arxiv.org/abs/2611.28966)

**<font color=#1a73e8>作者：</font>** Wendong Yao, Binhua Huang, Soumyabrata Dev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free open-vocabulary semantic segmentation (OVSS) built on CLIP has advanced rapidly, with methods typically ranked by mean intersection-over-union (mIoU) across standard benchmarks. On datasets with a background class, however, implementations rely on per-dataset thresholds and background word lists that are rarely documented or unified (11 of 13 surveyed methods configure per-dataset background decisions). We audit configurations and papers of 13 training-free OVSS methods, re-run seven from official codebases, and compare official settings against a strict unified protocol under pre-registered contracts. The protocol gap depends strongly on the benchmark---ranging from 22.8 mIoU points on PASCAL VOC (VOC21) to 0.1 points (indistinguishable from zero) on ADE20K---and alters pairwise method rankings. Despite large shifts in absolute mIoU, most of the reported improvement of later CLIP-only methods over SCLIP remains under the unified protocol (roughly 79% of the published gain). Decomposing official background handling shows that it combines numeric settings and class-name files whose dominant component reverses across benchmarks, while no tested tuning-free rule transfers reliably across all datasets. Moreover, exact collisions between background words and target names---present in six of seven official COCO-Object configurations through "bed"---make affected classes unpredictable under official post-processing, while the main per-class drops under language-model-generated vocabularies on VOC21 are largely attributable to a few generated terms. We offer reporting recommendations and release our evaluation code, frozen configurations, contracts, and a collision-check tool.

---


### 156. [Learning from Another Angle: Rotation-Based Test-Time Training for Multimodal Large Language Models](https://arxiv.org/abs/2611.28972)

**<font color=#1a73e8>作者：</font>** Changyu Liu, Fei Zhao, Yiyang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) achieve strong performance on vision-language tasks but often remain vulnerable to distribution shifts due to their fixed parameters during inference. While Test-Time Training (TTT) offers a pathway for dynamic adaptation, existing approaches suffer from prohibitive computational overhead due to multiple sampling and the risk of error reinforcement from biased self-generated supervision. In light of this view, we propose RoTTT (Rotation-based Test-Time Training), a simple and efficient TTT approach that enables instance-specific refinement at inference time. For each test instance, RoTTT performs a small number of gradient updates by predicting the rotation angle of the input image. The known rotation angles naturally serve as a reliable self-supervised signal, enabling lightweight and stable adaptation without requiring additional annotations. Extensive experiments across multiple vision-language benchmarks demonstrate that RoTTT consistently improves performance across different MLLMs, providing a practical and efficient paradigm for on-the-fly MLLM adaptation.

---


### 157. [CLASP: Complementary Layer Selection and Profiling for Zero-Shot OOD Detection using Vision-Language Models](https://arxiv.org/abs/2611.28986)

**<font color=#1a73e8>作者：</font>** Saahil Islam, Adarsh Bhandary Panambur, Teodora Spasojevic 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) enable zero-shot out-of-distribution (OOD) detection in medical imaging, yet existing approaches often rely on final-layer confidence or entropy-based layer selection, potentially missing complementary information. We show that low in-distribution (ID) confidence entropy does not reliably predict OOD discrimination. We introduce CLASP (Complementary Layer Selection and Profiling), an ID-only framework that jointly models layer--prompt responses and visual features. CLASP ranks visual encoder layers using Gaussian conditional mutual information and selects a compact subset through anchored spectral selection, without fixing the number of layers. It then combines the selected layer--prompt profiles with PCA-compressed visual embeddings and fits a single shrinkage-regularized Gaussian. OOD scores are computed using squared Mahalanobis distance, without fine-tuning, OOD training data, or test-time adaptation. Across histopathology, chest X-ray, and brain MRI benchmarks with UniMedCLIP and BioMedCLIP, CLASP performs strongly under varied distribution shifts. On MIDOG near-OOD, it achieves 87.54% AUROC with UniMedCLIP, outperforming confidence-based baselines; with BioMedCLIP, it remains competitive but trails visual-only Mahalanobis modeling. Ablations highlight the value of layer--prompt interactions and cross-feature dependencies, while exposing shift-dependent contributions and limitations under semantic shifts.

---


### 158. [Diagnosing Verbalized Confidence in a Medical Vision-Language Model for Selective Prediction on Colorectal Histopathology Patches](https://arxiv.org/abs/2611.28993)

**<font color=#1a73e8>作者：</font>** Anay Sinhal, Amit Sinhal, Ashish Pandey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flagging uncertain histopathology patches for specialist review needs a confidence that is higher when the model is right. We test whether an open medical vision-language model emits one. MedGemma-27b-it and its base Gemma-3-27b-it were run zero-shot under one prompt on 10,004 PathMNIST validation patches and 7,180 patches of a patient-disjoint external cohort. Both are too inaccurate to deploy (40.6% and 35.5%); the object of study is the confidence. MedGemma's verbalized confidence puts 96% of patches at one value; its confidence-correctness AUROC is 0.499 and 0.528, and routing by it moves selective-accuracy AUC by -0.004 and +0.037. Gemma-3 spreads its confidence over nine values, reaches AUROC 0.70, and gains +0.114 and +0.115. MedGemma's label-token probabilities do not rescue it: their validation advantage reverses where the top-20 alternatives include every class. On 1,800-patch subsets of each cohort, stratified on correctness and reweighted to the full splits, agreement across five prompt variants beats random by +0.123 and +0.106, and wording-only paraphrases give +0.100 and, externally and in direction only, +0.054; agreement's external margins over confidence do not survive slide-level clustering. Under one restructured prompt variant, MedGemma's stated confidence routes (+0.112, +0.141), so the failure is tied to a prompt chosen for macro F1.

---


### 159. [S$^2$LMR: Supervised Sequential Long-Context Multi-Step Retriever](https://arxiv.org/abs/2611.28995)

**<font color=#1a73e8>作者：</font>** Qiang Hu, Kaiyi Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-step retrieval over long contexts is a key capability for retrieval-augmented generation, but strong existing approaches are costly and complex to train. Supervised retrievers are far simpler and cheaper, yet they fall well behind in this setting. We show that this gap stems not from supervised training itself, but from three misalignments between training and inference: easy training negatives, noisy retrieval prefixes, and position-agnostic scoring. Guided by this analysis, we introduce S$^2$LMR, a simple yet effective supervised sequential retriever that models multi-step retrieval as the evolution of an explicit textual state encoded by a single shared Transformer. On long-context reasoning, multi-hop QA, and needle-in-a-haystack benchmarks with context lengths ranging from 4K to 10M tokens, S$^2$LMR achieves performance comparable to state-of-the-art methods, substantially outperforming prior supervised retrievers. Notably, it requires only $\sim$2 hours of training on a single A6000 for contexts of up to 10M tokens, while remaining robust across a wide range of hyperparameter settings.

---


### 160. [Elicitation format changes zero-shot classification accuracy in a medical vision-language model: a two-center evaluation on colorectal histopathology](https://arxiv.org/abs/2611.28997)

**<font color=#1a73e8>作者：</font>** Anay Sinhal, Amit Sinhal, Arpana Sinhal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background. Verbalized confidence from a hosted medical vision-language model is usually treated as packaging around an unchanged prediction. Methods. We held a nine-class colorectal histopathology prompt fixed except for the requested response format and evaluated MedGemma-27b-it on 10,004 validation and 7,180 external-center PathMNIST patches, with preregistered endpoints, randomized ties, and random floors recomputed for each patch set. Results. Requesting probabilities over all nine classes instead of a ranked top-3 reduced accuracy by 14.8 points on validation, -0.1475 [-0.1594, -0.1353], and 13.4 at the external center, -0.1341 [-0.1484, -0.1196], against chance accuracy of 0.1111. The nine-class prompt uniquely forbade commentary, reasoning, and a chosen answer; removing that prohibition at matched cardinality and token budget recovered +0.1878 [+0.1623, +0.2134] and +0.1911 [+0.1648, +0.2181], while changing cardinality with the prohibition absent moved accuracy by -0.0013 [-0.0300, +0.0280] and -0.0214 [-0.0494, +0.0071]. The nine-class format returned no parseable distribution on 7.6 and 7.7 percent of patches, mostly zero vectors in the two least-textured classes, and deferring these failures first explained its measurable selective-prediction gain. Across four vision-capable models, accuracy did not grade the cost: two models matched on accuracy differed five- to sevenfold. First-token logit entropy routed better than any elicited signal, +0.1820 [+0.1722, +0.1974] versus +0.0493 [+0.0377, +0.0649] relative to each signal's random floor. Conclusions. Response format changes a medical vision-language classifier, and the operative component here was the instruction suppressing an answer. Use logits when available; otherwise request a short ranked list without prohibiting reasoning or a chosen answer.

---


### 161. [Consumer-Time Validity in Stateful AI Runtimes: Verifying Recovered State and Deferred Authority](https://arxiv.org/abs/2611.29004)

**<font color=#1a73e8>作者：</font>** Guijia Zhang, Huihao Jing, Bing Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Stateful LLM serving engines and agent runtimes reuse execution state and deferred permissions across components and sessions. A cancellation, rollback, or approval is recorded by one component and relied on by another, and recording it does not make the later use valid: a downstream consumer may read state or dispatch an action whose identity, production status, allocation, or target revision has since changed. We call the missing check consumer-time validity and separate two forms. State validity governs what a consumer reads. On vLLM with LMCache, an interrupted KV load leaves unwritten blocks indexed, and a host-only counter rewind desynchronizes the GPU position, so a second tenant generates a schema-valid tool call naming the wrong tenant in 10/10 native-fault runs; the call is recorded and not executed. Authority freshness governs what a consumer executes: on a multi-session approval runtime, an unrevoked deferred grant overwrote a newer revision in one admitted live execution. Output equality cannot test state validity: a fault-free run diverges at token 30 through BF16 batching alone while attended-KV digests match. We therefore specify consumer-bound recovery contracts that, for state recovery, jointly require exclusion, retention, and task completion, and an admissible-witness standard realized as a GPU-free offline trace verifier over scheduler metadata and persisted tool artifacts. On recorded traces the verifier agrees with the reference verdicts in 42/42 frozen GPU-matrix scenarios. An allocation-aware repair satisfies 7/7 triggered vLLM fault predicates on a pinned scheduler-case matrix, where upstream PR 61769 satisfies 2/7, and revision-bound dispatch blocks all 160 deterministic conflicting overwrites in a separate dispatcher cohort. Recovery must be checked where state and authority are consumed, with evidence bound to the consuming request.

---


### 162. [NoHairCache: Calibrate-Once KV Cache Eviction with One Power-Law Exponent](https://arxiv.org/abs/2611.29006)

**<font color=#1a73e8>作者：</font>** Shuyang Xiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The decay exponent $\alpha$ in KV-cache eviction is an intrinsic property of the model: calibrated once on a single corpus, it transfers directly across domains. Attention-based accumulation (H2O) and recency-based sliding windows (StreamingLLM) are two dominant eviction frameworks, often treated as unrelated, but we show that they are the two endpoints of a single power-law family: by scoring each token as $s_i = A_i \cdot (t-i)^{-\alpha}$, where $A_i$ is cumulative attention and $\alpha$ controls the age penalty, H2O and StreamingLLM correspond to $\alpha=0$ and $\alpha\to\infty$, respectively (with StreamingLLM additionally hard-coding an attention-sink patch).
The no-hair mechanism of \citet{xiang2026nohair} bounds the admissible range of $\alpha$, and the measured exponents agree: calibrating once on WikiText yields $[0.556, 0.822]$ for a representative model (Qwen2.5-1.5B-Instruct). The per-model ranges are consistent across five models (410M--1.5B) and independently match the optimal regions from perplexity sweeps.
\textsc{NoHairCache} achieves the lowest perplexity across three datasets (WikiText, PG19, and arXiv) without per-dataset tuning, outperforming both H2O and StreamingLLM ($p < 0.05$ on all three datasets, with $0.06$--$0.10$ PPL gains over StreamingLLM at budget $512$). On downstream four-way multiple-choice QA, it matches or outperforms StreamingLLM across all nine (task, budget) cells, retaining $98.2\%$ of full-cache accuracy on NarrativeQA at $25\%$ retention versus $91.1\%$ for StreamingLLM; per-cell McNemar tests are not significant, so QA is corroborating only. We release our calibration script and drop-in scorer upon publication.

---


### 163. [Population-Based Post-Training for Large Language Models](https://arxiv.org/abs/2611.29014)

**<font color=#1a73e8>作者：</font>** Yixuan Even Xu, Aleksei Petrenko, Raja Giryes 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is one of the most popular post-training paradigms for large language models. RLVR typically trains a single model under hyperparameters chosen before training begins, while researchers tune hyperparameters across consecutive runs. We introduce Population-Based Post-Training (PBPT), which trains several models in parallel and lets the training process do the tuning through population-based training. PBPT periodically evaluates models on a validation set. High-performers are duplicated and their hyperparameters perturbed to explore new configurations. Low-performers stop training and are replaced by these copies. On reasoning benchmarks (Enigmata, Nemotron) and interactive tool-use environments (Gaia2, AppWorld), PBPT produces stronger agents than compute-matched groups of independent RLVR learners. Furthermore, PBPT is able to recover from poor initial hyperparameters, automatically discovering better settings over the course of training.

---


### 164. [Watermark Claims Under Test: Lessons from Auditing a Production LLM](https://arxiv.org/abs/2611.29018)

**<font color=#1a73e8>作者：</font>** Felix Desyatirikov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Can we tell whether an LLM is watermarked without knowing its secret key? Published black-box tests suggest that carefully designed prompts can reveal the statistical footprint of a watermark. This paper examines what happens when those tests move from controlled reference implementations to a deployed model whose watermarking parameters are undisclosed. We present an audit of the Red-Green watermark presence test on Claude. Across ten initial configurations, the published test never rejects on a model the provider states is watermarked, despite detecting a local reference at comparable sample sizes. Controlled experiments expose a failure mode: including the prompt in the watermark's repeated-context history suppresses marking exactly where the test measures it. The watermark remains active, but the probe becomes blind. Attempts to repair the probe reveal further confounds. Constructed contexts can trigger native digit-to-word preferences, while comparisons within a single response can measure how the model plans its answer. Tokenization changes which contexts the probe actually controls. These findings show why validation on a surrogate model does not establish validity on the model under investigation. A redesigned probe finds a substantial context-dependent shift on Claude Fable that is absent on two sibling controls. However, the pre-registered decision remains inconclusive because selective refusals violate the protocol, and the effect's watermark origin is unresolved. We show how to design controls, distinguish statistical rejection from evidence of watermarking and interpret a null without treating it as proof of absence. We provide researchers and practitioners working on LLM evaluation, watermarking, and provenance with an audit checklist grounded in concrete successes and failures. Code, prompts, and parsed responses are available for reproducing the analyses.

---


### 165. [Do You Even Know What I Want? Improving LLMs Ability to Detect Hidden User Intent](https://arxiv.org/abs/2611.29028)

**<font color=#1a73e8>作者：</font>** Kelsey Sikes, Sarath Sreedharan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As with conventional AI agents, a common source of misalignment between Large Language Models (LLMs) and their human users is misspecified goals. Often, this happens when the human has skewed beliefs about the system's model and provides it with information that causes behavior different from what they expected, with potentially unwanted side effects. To ensure goal alignment, one solution would be for the LLM to ask the human questions about their objectives. However, it has been well-documented that LLMs most often provide default responses to user requests rather than try and ask questions to clarify their true intent. In this paper, we address these challenges by adapting a novel formulation for the objective misspecification problem to work with LLMs. We then test if LLMs that are prompted to ask questions about a user's true underlying objectives are better at identifying them compared to those that do not. We evaluate our method using four state-of-the-art LLMs tested on five standard IPC domains, showing that for some domains, asking questions greatly improved model performance.

---


### 166. [LITMUS - Literature Informed Testbed for Mapping Usecases and Synthesizing Risk-Cards](https://arxiv.org/abs/2611.29034)

**<font color=#1a73e8>作者：</font>** Seshu Tirupathi, Elizabeth M. Daly, Radu Marinescu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The proliferation of large language models (LLMs) and Artificial Intelligence (AI) in real-world applications has heightened the need for systematic, safety-oriented deployment frameworks. Existing approaches typically prioritize the construction of datasets and risk cards around the LLM and AI architecture itself, yet they provide scant consideration for the specific use-case that drives model selection. This omission is problematic because any practical AI deployment begins with a detailed use-case description that informs the assessment of contextual hazards. In this paper, we introduce a structured pipeline that, given a use-case, automatically produces a tailored dataset and an accompanying risk card. The process ensures that identified risks are tightly coupled to the use-case, and it offers traceable evidence from peer-reviewed literature to substantiate each risk to use-case relationship. Prior claim-verification methods (FActScore, FactReasoner) have been validated for factual claims. Risk-relevance is a hypothetical claim about possible harm, and whether evidence retrieval can meaningfully assess such claims remains untested. Literature-Informed Testbed for Mapping Use-cases and Synthesizing (LITMUS) risk cards are the first systematic attempt to characterize this adaptation. We evaluated the pipeline using the MIT Risk Taxonomy and achieved a 0.91 F1-score with a list of 320 samples from the benchmark risk dataset that was considered. These results demonstrate the effectiveness of our approach in generating robust, evidence-based risk assessments for LLM deployments.

---


### 167. [Grounding Collaborative Agents in Group Cognition](https://arxiv.org/abs/2611.29036)

**<font color=#1a73e8>作者：</font>** Zhaoxuan Tan, Mengting Wan, Jingbo Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Collaborative agents joining an ongoing team rely on shared context to connect multi-party interaction histories with downstream coordination decisions. Existing work typically focuses either on retrieving historical facts from conversation logs, which surfaces isolated evidence without capturing who knows or owns what, or on evaluating end-to-end interactions, which conflates preparation with execution and lacks direct supervision because a team's history has no single ground-truth summary. To bridge this gap, we formulate group briefing, the task of reconstructing task-relevant group cognition across participants' expressed beliefs, group dynamics, and grounding gaps, and introduce a four-domain benchmark of 1,351 requests and 9,975 verified reference points paired with a two-stage evaluation pipeline combining reference-point coverage and downstream collaboration simulation. Using this pipeline, we show that GroupBrief, a simple task-guided approach that iteratively probes the message history and synthesizes a structured brief without offline memory indexing or graph construction, outperforms ten retrieval and agent-memory baselines in overall coverage with gpt-5.4-mini, while benchmarking nine language models reveals that prospective friction remains harder to recover than past state across model scales. We further use reference-point coverage as a feedback signal for harness optimization, refining GroupBrief's retrieval and synthesis instructions while keeping model weights frozen. On held-out Test projects, GroupBrief (optimized) improves coverage by 2.54 percentage points for gpt-5.4-mini and 12.88 for gpt-5.6-luna, achieving 64.46% and 68.42% preference over no brief in downstream simulations. These results establish our benchmark and evaluation pipeline as a foundation for measuring and optimizing how collaborative agents ground in group cognition.

---


### 168. [RES: Accelerating Diffusion Language Models with Rolling Entropy Sampling](https://arxiv.org/abs/2611.29066)

**<font color=#1a73e8>作者：</font>** Patrick Pynadath, Nicolas Perez-Nieves, Bobak Shahriari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A diffusion language sampler makes two choices for every position in its denoising window: where the next token comes from, and when the position is committed to the KV cache. Using the entropy-bound sampler in DiffusionGemma, we study two extremes of the second choice. Committing each token as soon as it is accepted removes the chance to revise it, which hurts when the entropy bound is relaxed to trade accuracy for speed. When accepted tokens are frozen, macro accuracy falls from 73% to 20% as the bound is relaxed, while the unfrozen sampler stays near 70%. Committing a whole block at once wastes computation, since tokens converge in a largely left-to-right order and more than half of the window holds already-final tokens by twenty denoising steps. These findings motivate the Rolling Entropy Sampler (RES), which commits a contiguous accepted prefix once it reaches a minimum length and keeps positions farther ahead open to revision. Unlike earlier rolling samplers, RES runs on uniform diffusion, where accepted tokens can still change, and it needs no training. Across seven benchmarks, RES increases tokens per forward pass from 19.3 to 25.5, while macro accuracy goes from 80.7% to 78.8%, and it extends the speed-quality Pareto frontier beyond what tuning the entropy bound alone reaches.

---


### 169. [Do LLM Agents Compromise Like Humans? Risk and Responsibility in Dyadic Decision-Making](https://arxiv.org/abs/2611.29069)

**<font color=#1a73e8>作者：</font>** Noah S. Okada, Ketika Garg, Wenning Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents are increasingly deployed in settings where they must collaborate to make joint decisions. We investigate how this collaboration unfolds under risk, asking whether agents adjust their choices to accommodate their partners, how they assign responsibility for shared outcomes, and whether responsibility attribution shapes subsequent adjustment. We designed a series of agents with systematically varying risk preferences and paired them in a repeated joint decision-making task previously conducted with humans. Like humans, agents converged toward their partners' choices. However, similar aggregate behavior arose from different dynamics: agents showed little evidence of reciprocal adjustment, tended to weigh rewards more, and their responsibility attribution was decoupled from compromise. Similarly, while they showed bias in their responsibility attribution, the outcome's valence shaped the attribution differently than in humans. Our results reveal important differences between human--human and agent--agent joint decision-making, demonstrating that similar social outcomes can emerge from different social dynamics and reasoning.

---


### 170. [Factory-simulator: A process-oriented environment for evaluating manufacturing decisions against optimisation-based references](https://arxiv.org/abs/2611.29079)

**<font color=#1a73e8>作者：</font>** Andrzej Wodecki, Wojciech Godlewski, Michał Chojna  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Motivated by discussions with an electronics contract manufacturer about decision support, Factory-simulator provides a deterministic manufacturing environment for controlled research on the business performance of large language model-based multi-agent systems (LLM-MAS). Equal delivery performance can arise from decisions with different financial consequences, complicating evaluation through delivery metrics alone. Its process-oriented model connects procurement and production decisions to order fulfilment and factory finances. Seeded worlds and recorded actions support replay and branching from a shared history to examine alternative decisions and their downstream consequences. Linear and mixed-integer programming models generate profit-oriented reference decisions. Observation-limited comparators use disclosed information; full-foresight references use future events for diagnostic comparison. Controlled examples show equal delivery performance with different profit under the same information and distinguish delivery penalties from deferred payment. Verification includes material and financial balances, replay and forks, and a small allocation instance in which the tested optimisation-based controllers attain an analytically established optimum. An external three-role LLM-MAS client completed four illustrative runs comprising 159 periods, with reconciled balances and exact replay of recorded actions. Matched-world rolling comparisons contextualise the financial outcomes, while full-foresight results provide heuristic reference points rather than certified optima. The software enables researchers to investigate how agent organisation and information access affect business outcomes, including whether distributing procurement and production responsibilities changes profit relative to a centralised controller.

---


### 171. [HME-PFD: Heterogeneous Mixture-of-Experts Privileged Feature Distillation](https://arxiv.org/abs/2611.29094)

**<font color=#1a73e8>作者：</font>** Wen Xu, Xiaomin Zhang, Yucheng Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) is widely used to transfer knowledge from large teacher models to smaller student models, facilitating efficient serving of machine learning systems. In the context of ads recommendation, privileged features distillation (PFD) extends KD by allowing the teacher model to leverage privileged features, i.e., features available only during training, to enhance distillation performance. However, in real-world scenarios, privileged features often have limited coverage and exhibit heterogeneous distributions, resulting in training examples of varying importance for distillation and model learning. We propose Heterogeneous Mixture-of-Experts Privileged Feature Distillation (HME-PFD), a novel approach that incorporates privileged features into the routing module of a Mixture-of-Experts-based student model. Our method introduces both hard-coded and learnable routing modules, enabling the student to dynamically determine expert assignment based on the availability and values of privileged features. This design allows the student model to better handle the heterogeneous data scenario, where privileged features are partially observed, by differentiating between high- and low-signal samples. Extensive experiments on two post-click conversion prediction tasks demonstrate that HME-PFD consistently outperforms baseline methods. Our results show that leveraging privileged features for expert routing in the student model leads to improved model performance, even when privileged features are incomplete or sparse.

---


### 172. [Beyond Free-Form Generation: Measuring Interface Composition in Competitive NLP Systems](https://arxiv.org/abs/2611.29103)

**<font color=#1a73e8>作者：</font>** Xinchen Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systems with decoder LLMs can combine free generation with scoring, ranking, or selection. We measure these documented interface combinations with five annotation fields linked to source evidence. The corpora comprise 517 solutions from 42 Kaggle competitions involving NLP and 76 participant systems from 26 SemEval, TREC, and WMT task years. Among eligible generation systems with decoder LLMs, 18 of 55 Kaggle systems and 17 of 20 Shared Task systems are hybrid: free generation coexists with a constrained interface. The remaining systems use free generation alone. Giving each competition or task year equal weight yields hybrid shares of 0.327 and 0.876. Within Eedi, 21 eligible systems with decoder LLMs have five exact interface profiles; ten LLM Science Exam systems share one interface class and have four profiles. Across Kaggle, the eligible systems with decoder LLMs span 18 exact interface profiles, revealing variation within broad task and backbone categories. These estimates characterize documented public systems selected using our selection criteria and include interfaces throughout the complete pipeline, including intermediate stages. The data are available at this https URL.

---


### 173. [Beyond Evidence Coverage: Encoding-Time Access in Multi-Agent Systems](https://arxiv.org/abs/2611.29107)

**<font color=#1a73e8>作者：</font>** Joshua Huang, Ajit Mallavarapu, Elliott Kalt  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cache-sharing multi-agent systems can retain every evidence token's representation while preventing cross-worker access during encoding. We test whether this coverage recovers joint-encoding quality using attention masks over two logical workers in frozen Qwen3-4B, Qwen3-8B, and Llama-3.1-8B-Instruct models. Tokens, positions, and answer-time access remain fixed within comparisons. We evaluate 200 two-hop MuSiQue-Ans questions and 200 selected HotpotQA bridge questions. In data-layout seed 0, averaged across models, blocking access costs 5.6 and 6.8 F1 points relative to full access on MuSiQue and HotpotQA, respectively. Exposing the earlier worker's supporting paragraph improves F1 over blocked access by 7.6 and 6.7 points; equal-token non-support access provides no detectable average gain. With model weights and greedy decoding fixed, we vary distractor layouts using five data-layout seeds per dataset for Qwen3-8B and three for Llama-3.1-8B-Instruct. Supporting-paragraph access has higher mean F1 than blocked and equal-token non-support access in every evaluated data-layout seed. Supporting access can also outperform full access, but its advantage depends on the model, dataset, and layout. Oracle support labels isolate access from selection error; the study does not evaluate a deployable selector. Complete evidence coverage at answer time therefore does not guarantee joint-encoding quality: which supporting facts can interact during encoding matters.

---


### 174. [Bridging Blind Spots With Words: Decentralized Multi-View Spatial Reasoning via Language-Constrained Communication](https://arxiv.org/abs/2611.29112)

**<font color=#1a73e8>作者：</font>** Soumyabrata Chaudhuri, Joydeep Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As multimodal LLMs (MLLMs) get increasingly used as collaborative partners across embodied robotics, AR/VR, and multi-user systems, spatial reasoning is now often distributed across agents with partial environment visibility, necessitating spatial reasoning integration. Prior work in language-mediated spatial integration is however strictly limited to simplified two-agent scenarios. To address this gap, we first formalize the general problem of decentralized multi-view spatial reasoning, where N agents observe distinct viewpoints, exchange budget-constrained natural language messages, and collaborate to enable a listener to answer spatial queries. We then introduce a novel multi-view spatial benchmark to isolate queries that demand non-trivial multi-view integration. Through an extensive empirical study, we discover that the penalty of restricting decentralized spatial reasoning to natural language with limited budget is far smaller than suggested by prior two-agent literature. Nevertheless, we observe that substantial headroom still remains for multi-agent spatial reasoning in this setting, as evidenced by a significant gap between current centralized performance and an oracle best-of-K ceiling. Moreover, we show that reinforcement learning with credit assignment substantially bolsters the decentralized model, effectively closing the gap with the centralized baseline.

---


### 175. [Decoding Transformer Dynamics via Koopman Subspaces](https://arxiv.org/abs/2611.29113)

**<font color=#1a73e8>作者：</font>** Subhradeep Kayal, Ali Dashti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We apply Koopman operator theory and Dynamic Mode Decomposition (DMD) to characterise how large language models (LLMs) process different input topics. Treating the layer-to-layer evolution of hidden states as a dynamical system, we fit a linear Koopman operator and take the subspace spanned by its dominant modes as a per-topic spectral fingerprint. Four findings emerge. First, the depth map is near-linear: a single linear operator predicts each next-layer state to within approx. 18% relative error (interior variance explained approx. 0.99). Second, over the 57 MMLU subjects the fingerprint is topic-discriminative, matching the MMLU taxonomy at 0.72 nearest-neighbour purity and each subject's semantic neighbourhood at 0.75 any-hit@3. Third, it is a reproducible signature (split-half self-retrieval approx. 0.97$). Finally, these findings are consistent across seven base models (Qwen2.5 0.5-7B, Llama-3 1-8B), with a suggestive trend of alignment rising with MMLU accuracy. The spectral fingerprint thus provides a probe of how transformers process different topics across depth. Code is available at this https URL.

---


### 176. [When Can a Rewiring Control Test LLM Weight Readers? C2 and an Eligibility Protocol](https://arxiv.org/abs/2611.29120)

**<font color=#1a73e8>作者：</font>** Vaishak Girish Kumar, Sanika Vilas Najan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can predict the outputs of small neural networks from raw weights, but success could reflect recognition of weight-space regularities (fingerprints) rather than computation, and function-preserving controls cannot tell these apart. We propose C2, a counterfactual that permutes the columns of a network's final linear readout: every other parameter, and the readout's singular values, norms and entry multiset, are unchanged, and the function can change in an exactly recomputable way; we verify that each evaluated permutation does. C2 separates fingerprinting from computation only under three conditions, which we state as an eligibility protocol: a strategy restricted to C2-invariant summaries must already predict the target; C2 must change a property specific to the rewiring; and the reader's identity must be attested. No natural setting we tested is eligible. On tiny MLPs a frontier reader route followed the rewired function on all 24 networks, but invariant baselines were near chance and its backend could not be attested. In two public CNN zoos the conditions traded off: weight statistics predicted CIFAR-10 accuracy in-distribution, but C2's effect on accuracy was not specific to the swap, while per-image targets were specific but not predictable from invariant summaries. On a constructed population where a planted fingerprint rule works, all conditions hold and C2 separates a rule-following reader from an executor. A self-hosted Qwen3.8-27B followed the rewired function rather than the shortcut, and showed no evidence of using the weights with thinking disabled. A registered replication on fresh networks confirmed both findings (tracking minus stuck 0.875, 95% interval [0.750, 1.000]), and DeepSeek-R1-Distill-Qwen-14B also followed the rewiring (tracking minus stuck 0.729 [0.552, 0.885]). The transforms, audits and raw records are available from the authors.

---


### 177. [Group-Balanced Supervised Fine-Tuning for Knowledge-Intensive Domains](https://arxiv.org/abs/2611.29127)

**<font color=#1a73e8>作者：</font>** Mark Heimann, Bruno Jacob  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) weights every supervised token equally, so on knowledge-dense corpora the loss budget follows token count rather than importance: on a legal QA benchmark, citation strings absorb 81% of the supervised loss weight budget while the answers being taught absorb 5%. We present Group-Balanced SFT (GB-SFT), which equalizes the loss budget across the semantic roles of tokens within a target sequence. With one tunable dial and one structural switch, GB-SFT contains standard SFT, class- and span-level balancing as corners whose geometry we characterize exactly. On benchmarks in law, medicine, code, and mathematics, we show across model families that: (i) GB- SFT injects new knowledge better than uniform SFT, pointwise token weighting, memory editing, and matched-budget data mixing; (ii) it matches the injection of masking out everything but the knowledge payload while retaining the citation recall that masking destroys (0.98 vs. 0.38); and (iii) role-aware grouping carries the gain: label-free partitions recover at most a third of it, an LLM tagger nearly all where the groups are lexically distinctive; and and (iv) the budget governs what fine-tuning breaks as well as what it learns, acting as a monotone lever on the safety-guardrail erosion SFT causes, at matched task accuracy. We release two new contamination-controlled knowledge-injection benchmarks with validated ground truth.

---


### 178. [Pain Reassessment from Pulse Waveforms with Language Model Explanations](https://arxiv.org/abs/2611.29128)

**<font color=#1a73e8>作者：</font>** Cheng Ding, Jiaming Liu, Daoqiang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Routine photoplethysmography (PPG) offers a continuous physiological signal for pain reassessment between self-reports. Whether prior recordings provide an individualized physiological reference beyond care-process timing remains unresolved. Across 52,082 report-linked assessments from 21,514 patients in MIMIC-III critical care and MC-MED emergency care, we evaluate a workflow that pairs longitudinal PPG representations with local evidence-linked language interpretation. Among 27 methods, source-selected full-history models achieved average precision of 0.824 from critical to emergency care and 0.822 in reverse. Removing historical pulse-run representations while retaining reassessment availability and elapsed time lowered critical-to-emergency four-hour within-patient concordance from 0.718 to 0.534. This comparison supports the contribution of prior pulse-run representations to within-patient ordering beyond timing cues. Across 2,905 test patients, a local Qwen model interpreting frozen predictions achieved a 94.7% patient-equal pass rate on automated evidence checks after at most one revision. Longitudinal pulse context and evidence-linked language interpretation support a patient-centred workflow for pain reassessment.

---


### 179. [RAVEC: Reward-Aligned Visual Evidence Correction](https://arxiv.org/abs/2611.29142)

**<font color=#1a73e8>作者：</font>** Junjie Yang, Rui Qian, Xutao Mao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards improves multimodal reasoning, but response-level feedback provides limited guidance on which intermediate decisions to correct. Visual interventions reveal sensitivity to image content, yet this sensitivity alone does not establish reward alignment or support across questions. We introduce RAVEC (Reward-Aligned Visual Evidence Correction), which selects visual corrections using local and cross-question reward support and jointly determines their strengths within each response. Paired Visual Evidence Contrast (PVEC) compares predictions from an exponential moving average teacher at the same sampled response prefix under the original image and a version with its annotated evidence region suppressed, yielding signed correction directions. Credit-Risk Allocation (CRA) screens these directions using local reward alignment and reward support from other questions, excluding all responses to the source question. It then solves a response-level budgeted allocation problem, assigning additional cost to directions that locally reduce predictive entropy. The resulting signed visual loss augments Group Relative Policy Optimization (GRPO) during training. Inference uses only the original image and question. Across ten multimodal benchmarks, RAVEC achieves the highest average accuracy among the compared methods with both 3B and 7B Qwen2.5-VL-Instruct models, outperforming GRPO by 2.67 and 1.39 percentage points, respectively. Component ablations support the combined design of evidence alignment, credit qualification, and risk-aware allocation. The project is available at this https URL.

---


### 180. [RVLM: Fewer Tokens, Better Resolution Scaling, Fine-Grained Spatial Grounding](https://arxiv.org/abs/2611.29146)

**<font color=#1a73e8>作者：</font>** Savya Khosla, Chris Dongjoo Kim, Alex Schwing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) tokenize images using fixed spatial grids, so visual token count grows with pixel area rather than scene content. We propose to group neighboring patches based on their visual appearance, allowing tokens to represent coherent image regions rather than fixed spatial windows. We introduce RVLM, a VLM trained to use regions rather than patches as its visual units. Analyzing region construction for general-purpose VLMs, we find that regions must cover the full image, stay spatially connected during end-to-end training, and preserve fine structure such as small text, while semantic grouping adds little. RVLM therefore partitions images using training-free Felzenszwalb-Huttenlocher segmentation, assigns each ViT patch to a region, and pools patches within each region into a variable-length sequence of visual tokens. The patch-to-region assignment is retained to support spatially precise prediction through coarse-to-fine decoding. Across tasks spanning VQA, pointing, counting, segmentation, and depth estimation, RVLM matches or improves example-weighted task performance while using 21.5% fewer visual tokens than an identically trained patch baseline. The advantage grows with image resolution, reaching a 5.3-point gain while using 51.8% fewer visual tokens at the highest-resolution setting. The gains are largest on spatially demanding tasks, where prior token-reduction methods degrade most sharply. RVLM adds no model parameters and improves inference throughput by up to 35.9%. On unseen pathology and satellite images and on video benchmarks without any video training, RVLM performs on par with the patch baseline while using 2-3$\times$ fewer visual tokens. These results establish regions as a scalable alternative to patch-based visual representations while preserving the spatial precision required for grounded prediction.

---


### 181. [VeriLogic: Reinforcement Learning over Verifiable Logical Reasoning Traces](https://arxiv.org/abs/2611.29147)

**<font color=#1a73e8>作者：</font>** ZeLiang Chen, Yunyao Zhang, Xinglang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Logical reasoning derives conclusions from premises through explicit intermediate inference steps, providing a natural basis for process-level verification and supervision. However, existing learning methods often rely on response-level outcome signals, which overlook heterogeneous correctness within the reasoning trace: a correct answer may contain invalid reasoning, while valid intermediate steps may also appear in an incorrect response. To address this issue, we introduce Reinforcement Learning on Verifiable Logical Reasoning (VeriLogic), which turns internal reasoning traces into explicit and verifiable learning objects. Rather than treating a response as an indivisible learning unit, VeriLogic decomposes logical reasoning into explicit intermediate judgments, proofs, and final decisions, and organizes them into a unified "Grounding - Optimization - Refinement" pipeline: (1) Verification-Grounded Reasoning Environment Construction grounds logical reasoning into explicit intermediate states and formally checkable proof obligations, making the internal reasoning process accessible to verification and learning; (2) Logical Structured Policy Optimization learns from verifier feedback through complementary global and local rewards, jointly optimizing the overall reasoning outcome while providing targeted optimization signals to different intermediate reasoning paths; and (3) Verifier-Guided Iterative Refinement acts on verifier feedback by leveraging proof states and error messages to iteratively diagnose and repair failed reasoning. Experiments on six logical reasoning benchmarks show consistent gains over strong baselines, with average improvements of 6.39% and 5.00% on Qwen3 and Llama-3.1. These results highlight the value of making logical reasoning traces verifiable, learnable, and refinable beyond final-answer supervision.

---


### 182. [Can an Agent Trust Its Own Zoom? Cross-Magnification Provenance Verification for Whole-Slide Images](https://arxiv.org/abs/2611.29150)

**<font color=#1a73e8>作者：</font>** Yan Wang, Yiran Song, Zizhuo Gong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual agents navigate whole-slide images through magnified observations associated with claimed locations. However, a visually plausible observation does not necessarily originate from its claimed location, particularly across magnifications and in regions with similar tissue structures. We formulate cross-magnification provenance verification (CMPV) to evaluate whether visual evidence supports a claimed spatial association, recover the source when possible, and abstain when evidence is insufficient. We introduce PyraFault, a benchmark of 3.06 million coordinate-supervised examples from 2,200 cases across five TCGA cohorts, covering within-context substitutions, absent-source faults, and geometric perturbations. We further propose ZoomTrace, a claim-independent verifier that estimates the observation's source before evaluating its agreement with the claimed location. It combines physical-scale alignment, visual retrieval, geometric refinement, and reliability estimation using spatially disjoint competing matches. On 503,320 test examples, ZoomTrace achieves 0.969 AUPRC and 0.987 AUROC, compared with 0.789 and 0.903 for Efficient LoFTR. Further evaluations reveal trade-offs in reliability estimation and limitations in vision-language models, cross-dataset retrieval, and calibration. Integrating ZoomTrace into visual agent tool paths reduces exposure to corrupted observations and silent failures, while downstream accuracy improvements depend on the agent and verification threshold.

---


### 183. [Medical Specialty Prediction from Bangla Patient Narratives: A Comparative Study of ML, DL, Transformers, and LLMs](https://arxiv.org/abs/2611.29151)

**<font color=#1a73e8>作者：</font>** Tasnin Tabassum Ali, Faisal Ahmed, Muhammad Anwarul Azim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Timely access to appropriate medical specialists remains a bottleneck in Bangladesh's healthcare system, as patients describe symptoms in informal Bangla rather than clinical terms, leading to ineffective referrals. This paper compares four model families for predicting medical specialties from Bangla patient narratives: six machine learning (ML) models using hybrid TF-IDF features, four deep learning (DL) models using Word2Vec embeddings trained on the corpus, four fine-tuned transformers, and five large language models (LLMs) evaluated zero-shot. From a corpus of 3798 patient records covering 20 specialties, we retained the five with the most records (Medicine, Gynecology, Dermatology, Pediatrics, Gastroenterology) and split the resulting 2730 records 80:20 into training and test sets shared by all families. The best transformer was XLM-RoBERTa (86.26% accuracy, 86.21% macro-F1), the best ML model was SVM (84.98%, 84.92%), the best DL model was Bidirectional GRU (80.77%, 80.83%), and the best LLM was Gemini (90.29%, 90.15%). Holm-corrected paired McNemar tests show SVM significantly outperforming Bi-LSTM (adjusted p = 0.004), whereas the Gemini-versus-Grok gap does not survive correction (adjusted p = 0.104), and neither the strongest transformer versus the weakest LLM (Grok) nor SVM versus the strongest transformer reaches significance. A tuned classical model is thus statistically indistinguishable from the strongest transformer, so accuracy rankings alone should not be read as evidence of one family's superiority. The findings provide a comparative baseline for Bangla medical text classification.

---


### 184. [MVAgent: Per-Video Agents under Global Coordination for Multi-Video Understanding](https://arxiv.org/abs/2611.29154)

**<font color=#1a73e8>作者：</font>** Kewei Wei, XueXiang Wen, Bocheng Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-video understanding requires systems to combine evidence from different videos for cross-video reasoning. Answering such questions involves two kinds of decisions. Observation decisions must adapt to each video's content, whereas cross-video judgments require relating evidence from different videos based on the question. Most existing agents make both kinds of decisions in one controller, whose context accumulates observations from every video. We separate them in MVAgent, a training-free Multi-Video Understanding Agent framework with one LocalAgent per video. Each LocalAgent plans observations of its own video and keeps a private observation history. A GlobalAgent coordinates cross-video reasoning by instructing the LocalAgents and combining their reports with joint observation. We evaluate MVAgent on CVBench, MVU-Eval, and CrossVid, using three Qwen3.5 models of different sizes and GPT-6-sol. With Qwen3.5, our framework improves aggregate benchmark scores by 5.1 points on average over Single-pass inference with the same model and by 5.0 points over the strongest prior agent using the same model. With GPT-6-sol, the average gain over Single-pass inference with the same model is 4.3 points. On the same hardware, MVAgent also runs 1.8-2.7 times faster than prior agents of comparable size.

---


### 185. [ContextFact: Remembering Facts in Context for Long-Term Conversational Agents](https://arxiv.org/abs/2611.29155)

**<font color=#1a73e8>作者：</font>** Jiayu Huang, Yichao Cai, Xinyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents built on large language models must maintain continuity across repeated interactions with users. However, long-term conversations scatter facts across turns and sessions, making it difficult to retrieve the right evidence with enough context. Memory for such conversations must therefore preserve facts with their context while keeping evidence selectively accessible. We first study how memory construction and retrieval-unit boundaries affect answerability and evidence access. Reading the entire memory bank reveals gaps that cannot be resolved by retrieval selection alone, showing that some context must be preserved during memory construction. Adjacent-turn grouping improves evidence access at matched unique-turn budgets, while wider windows do not consistently help. This motivates keeping fact-specific context local while organizing cross-session evidence separately. We propose ContextFact, which links context-preserving fact memories with source-grounded entity representations. Within sessions, it gathers the context needed to interpret each fact. Across sessions, it aligns recurring referents and revisits the source dialogue to reconstruct coherent entity representations linked to the supporting facts. At query time, ContextFact retrieves fact and entity views, reranks them independently, and uses entity-linked expansion to surface related facts; complete entity representations then provide organized cross-session evidence. With Qwen3.5-27B as the backbone, ContextFact achieves state-of-the-art performance while using only $21\%$ of the evidence tokens consumed by the strongest evaluated baseline, obtaining $86.49\%$ overall judge accuracy on LoCoMo and $91.00\%$ on LongMemEval-S. Controlled ablations support context-preserving fact boundaries and source-grounded entity reconstruction, while entity readout improves multi-hop accuracy beyond adding more facts.

---


### 186. [ARC: Adaptive Rollout Control for Efficient Synchronous LLM Reinforcement Learning](https://arxiv.org/abs/2611.29156)

**<font color=#1a73e8>作者：</font>** Yihui Zhang, Tianyu Wo, Jinghao Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synchronous reinforcement learning (RL) for large language models proceeds through a repeated rollout--barrier--update loop. Each update must wait for a fixed number of complete, group-relative training samples, yet individual response lengths and reward outcomes vary widely and only emerge as generation progresses. Static admission and unconditional completion therefore leave accelerators idle in some steps, and waste computation generating samples that will never contribute to the current update. We present ARC, a closed-loop rollout architecture that governs synchronous RL rollout at group granularity. ARC uses \textit{Calibrated Streaming Backfill} to judge from partial observations whether a group is still worth completing, backfilling a fresh candidate immediately when it is not; \textit{Deferred Group Completion} to park an uncertain early stop and resume it later instead of discarding it outright, bounded by a resume-cycle limit that guarantees termination; and \textit{Adaptive Admission} and \textit{Pipelining} to order admitted samples by early-measured duration and to admit further candidates only while expected supply still falls short of the target number of accepted groups. Under online evaluation, ARC reduces rollout time by $37.4\%$, a $1.60\times$ speedup, and improves effective GRPO throughput by $50.1\%$ over existing baselines, while directly recovering 98.9\% of the training groups that would ultimately have been kept.

---


### 187. [Decoupling Perception from Generation for Agentic 3D CT Report Generation](https://arxiv.org/abs/2611.29167)

**<font color=#1a73e8>作者：</font>** Chenyu Wang, Mingyu Chen, Wenchao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest CT reports repeatedly assess the same anatomical regions for findings and their attributes, such as whether a lung nodule is present and where it is located. These assessments suggest learning to answer visual questions directly, rather than coupling perception to open-ended text generation. Yet current CT report generation models largely follow generic vision-language modeling, which may miss subtle abnormalities when training data are limited. We therefore formulate report generation as a set of visual question-answering decisions coordinated by a large language model (LLM) agent. This decouples visual perception from reasoning and report writing: perception can be learned as a discriminative, non-generative task, while the LLM focuses on reasoning over patient context and posing relevant visual queries. We introduce Rad-VL-JEPA, which unifies report retrieval, finding recognition, and fine-grained attribute characterization through vision-language joint-embedding prediction. Building on this perception module, an agent trained with reinforcement learning (RL) acquires patient-specific visual evidence, while a separate editor incorporates the evidence into the final report, further separating evidence acquisition from report realization. Experiments show that Rad-VL-JEPA achieves strong performance on fine-grained CT understanding tasks with lower amortized per-query inference time than a generative VLM baseline trained with the same CT encoder and VQA data. The resulting reporting system outperforms strong VLM-based and agentic baselines.

---


### 188. [SpatialDuet: Bayesian task routing between a metric expert and a geometry expert for spatial intelligence](https://arxiv.org/abs/2611.29168)

**<font color=#1a73e8>作者：</font>** Duy Tran Thanh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied assistants and wearable devices need 3D spatial reasoning, and their limited hardware restricts them to small vision-language models (VLMs). Small spatial VLMs acquire different abilities from their training: a model trained on large spatial question sets estimates object and room sizes well, whereas a model with a 3D geometry encoder is better at relative directions and absolute distances. Instead of training a single model for all spatial tasks, as published methods do, we build one system that uses each frozen model for the tasks it handles best. We propose SpatialDuet, which pairs a metric expert with a geometry expert under a Bayesian task router. The metric expert is a data-driven spatial VLM run with three training-free modules: training-aligned sampling, metric-aware minimum Bayes risk decoding and per-type metric calibration. The geometry expert is a VLM with a 3D geometry encoder. For each question type, the router estimates from labelled development questions how likely each expert is to be better, and pools their answers with that probability as weight, in log space for numeric answers and over the option distributions for multiple-choice answers. Extensive experiments on four spatial benchmarks covering video and single images validate SpatialDuet; it outperforms the best published small VLMs by 3.17% on VSI-Bench and, excluding a model trained on CV-Bench-style data, by 1.44% on CV-Bench, without training any model weight.

---


### 189. [PhyCoVE: Benchmarking Physical Counterfactual Video Editing across Diverse Material Dynamics](https://arxiv.org/abs/2611.29184)

**<font color=#1a73e8>作者：</font>** Conghan Yue, Yuanjie Chen, Yunyan Xiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical counterfactual video editing turns a source video and a language-specified physical edit at a given execution frame into a counterfactual video that shows how the scene would evolve after the edit. Existing evaluations with counterfactual target videos mainly cover object removal or specific rigid-body motions, although real scenes also involve elastic deformation, fluid flow, and interactions among rigid bodies, elastic solids, and fluids. We introduce PhyCoVE, a benchmark of 533 cases on 110 source videos that covers rigid, elastic, and fluid dynamics in five interaction patterns, with edits that remove an object, change a physical quantity, or insert a new object. For the simulated cases, a language model proposes scene designs, coding agents build them with solvers suited to each material and physically based rendering and then simulate each edit from the source scene state, and humans check every stage. For the real cases, we record continuously from one camera position before and after each edit. We also propose counterfactual fidelity, a metric that applies across materials and their interactions and measures how much of the physical change from the source video to the target video a generated video reproduces. We evaluate seven open-source and commercial video editing models and find that counterfactual fidelity ranks them nearly as human preference does, but even the best model reproduces only about one seventh of the physical change. The models change how a scene looks but rarely how it evolves, whereas a physical edit requires understanding the dynamics that it changes. Physical counterfactual video editing thus remains far from solved, and PhyCoVE provides a foundation for developing and evaluating methods for it.

---


### 190. [Ziv Meets Sumcheck: Zero-Knowledge Proofs of Floating-Point LLM Inference](https://arxiv.org/abs/2611.29188)

**<font color=#1a73e8>作者：</font>** Hassan Khodaiemehr, Khadijeh Bagheri, Chen Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-knowledge proofs can show that a neural network produced a given output without revealing the network, but current systems for language models prove integer approximations of the model rather than the floating-point arithmetic that is actually deployed. Proving floating-point matrix multiplication has been regarded as hard, because rounding after every addition makes the result depend on the order of the additions. We avoid this obstacle by proving the correctly rounded product, in which every dot product is computed exactly and rounded once. This result is independent of the hardware and at least as accurate as standard kernels. We give an interactive proof for this relation whose cost is close to that of integer matrix multiplication, with roughly a thousand times fewer committed values than per-operation floating-point circuits need constraints, extend it to every layer of a transformer, and give a privacy construction for the complete argument whose zero knowledge we prove under explicit hypotheses. We implement the system and prove the full forward pass of GPT-2 small, including all twelve blocks and the output over the whole vocabulary, in 19 minutes on two processor cores; verification takes 21 seconds. The verifier rejects all 236 attacks we tested, and the model's outputs agree with high-precision inference at least as closely as standard 16-bit inference does.

---


### 191. [Direct Feedback Policy Optimization for AI Coding Agents](https://arxiv.org/abs/2611.29193)

**<font color=#1a73e8>作者：</font>** Fei Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI coding agents generate, modify, and validate code through multi-turn interactions. Existing reinforcement learning methods often rely on sparse terminal rewards, making it difficult to assess how intermediate decisions affect task outcomes, and group-relative methods also require repeated sampling for each task. We propose Direct Feedback Policy Optimization (DFPO), a single-trajectory reinforcement learning algorithm that trains directly from a single trajectory. DFPO achieves higher task resolution rates than GSPO under matched base models and execution harnesses.

---


### 192. [Unleashing the Value of Raw Point Clouds for 3D Understanding with LLMs](https://arxiv.org/abs/2611.29194)

**<font color=#1a73e8>作者：</font>** Tailai Chen, Jiawei Yu, Yiming Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard 3D point cloud language models typically rely on pretrained point encoders to extract 3D features and project them into representations processable by large language models (LLMs). However, these encoders are often originally optimized for pre-defined tasks, resulting in a representation bottleneck that may lead to a substantial mismatch with downstream 3D understanding. Moreover, existing models largely follow a single pass closed-book generation, limiting their ability to actively inspect task-relevant 3D regions or retrieve necessary external knowledge. In this work, we present PointTool, an encoder-free and tool-augmented framework for 3D reasoning. PointTool introduces Alignment-Free Patch Tokenization (AFPT) to locally aggregate raw point clouds while preserving fine-grained geometric structure, and Decoupled Point-Text LoRA (DPL) to facilitate global aggregation and 3D knowledge internalization within a frozen LLM. Building upon these designs, Program-Supervised Tool Reasoning (PSTR) enables the model to explicitly operate on raw 3D data and external resources through executable tools, supporting interactive 3D reasoning grounded in spatial evidence. We further introduce PointCloud-TR, a benchmark comprising 13K 3D objects, 39.8K questions, and 35.6K tool trajectories to facilitate training and evaluation of complex 3D reasoning. Experiments demonstrate that PointTool achieves strong performance on both standard and complex 3D understanding tasks, validating the effectiveness of the proposed framework.

---


### 193. [DataRecycle: Trustworthy Distillation of Structured Data from Scattered Web Evidence](https://arxiv.org/abs/2611.29206)

**<font color=#1a73e8>作者：</font>** Can Liu, Tengteng Zhu, Xinyu Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The web contains vast amounts of scattered quantitative evidence that is difficult to organize into comparable and verifiable structures. Yet its unstructured, sparse, and sometimes conflicting nature makes a systematic distillation costly and error-prone. Existing approaches force users to make a trade-off: search engines return document lists that require labor-intensive extraction and reconciliation, while generative AI systems produce fluent summaries that obscure data provenance, introduce reporting bias, and hide inconsistencies. We present DataRecycle, an interactive system that helps transform scattered web evidence into structured tables of comparable numerical facts. Given a user's query or statement, DataRecycle decomposes it into entities and attributes, retrieves candidate evidence, and organizes scattered, potentially conflicting records in a table-based evidence view. To address key challenges in automated data distillation (i.e., incomplete retrieval, untraceable generation, sparse data distribution, and multi-source inconsistency), DataRecycle adopts an ontology-guided, top-down data acquisition strategy, visualizes the recorded lineage from retrieved snippets to extracted values, and aligns heterogeneous data across dimensions such as time, definition, and scale. We evaluate DataRecycle through module-level experiments, a usage scenario, and a user study, showing that the system helps users organize numerical web evidence into provenance-linked tables and inspect uncertainty and conflicting sources.

---


### 194. [EVis+: Literature-Grounded Visual Analytics for Hypothesis-Driven Geoscientific Data Exploration](https://arxiv.org/abs/2611.29231)

**<font color=#1a73e8>作者：</font>** Zhaocong Yang, Jing Yang, Martha-Cary Eppes 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scientific researchers often interpret observational data in light of prior findings reported in the scientific literature. However, scientific literature typically remains external to visual analytics environments, requiring researchers to manually connect published findings with the data and hypotheses under investigation. In this paper, we present EVis+, a literature-grounded visual analytics system for condition-event time series analysis in geoscience. EVis+ enhances observational data exploration by retrieving and synthesizing literature-derived insights relevant to the dataset and analytical goals, transforming user-selected insights into testable hypotheses and mapping them to domain-specific visualizations through expert-curated templates, and supporting evidence examination, discrepancy validation, and literature-driven re-exploration to support iterative hypothesis refinement and scientific exploration. Rather than handing scientific analysis to an unconstrained language model, EVis+ uses structured AI-assisted transformations that keep intermediate results visible, allowing researchers to inspect and guide the analysis at each step. We evaluate the system through an evidence-grounding audit, a structured expert assessment of the insights, and case studies with geoscientists and a comparative study with domain experts.

---


### 195. [GameAnything: From Any Inspirations to Playable Game Worlds](https://arxiv.org/abs/2611.29238)

**<font color=#1a73e8>作者：</font>** Wenyi Wu, Siqi Liu, Yuru Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-driven game development holds the potential to transform diverse human inspirations into interactive experiences. However, existing systems and benchmarks primarily focus on explicit development specifications, with limited support for adapting multimodal references and evaluating actual gameplay experiences. We introduce GameAnything, an open-source agentic platform that transforms multimodal inspirations into playable extensions of existing games through iterative development. GameAnything integrates coding agents with an independent playtesting critic, persistent development state, and reusable experience memory to support continuous refinement. We further present GameAnything-Bench, a benchmark spanning diverse reference modalities, game creation objectives, and gaming environments, with exploratory gameplay testing to assess both functional correctness and gameplay quality. Evaluations of nine coding agent configurations reveal that current agents can adapt reference content but still struggle with playable interactions and precise modifications. Moreover, multimodal references improve content fidelity, while iterative refinement yields substantial but varying improvements across agents. These findings highlight both the potential and remaining challenges of inspiration-driven game development.

---


### 196. [Edit-Induced Dependency Mismatch: Propagation Omissions, Recovery, and Evaluation Blind Spots in Coding Agents](https://arxiv.org/abs/2611.29242)

**<font color=#1a73e8>作者：</font>** Fei Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> During iterative code modification, coding agents may continue to rely in subsequent reasoning on outdated dependency judgments whose text remains fixed in the context, leading to errors in subsequent reasoning and leaving consumer defects undetected by the original task evaluations, thereby exposing blind spots in the tested benchmarks. We study actual agent execution trajectories collected on benchmark tasks: deepseek-v4-flash runs on DeepSWE and SWE-bench Verified, supplemented by Qwen3.8-Flash cases on FeatureBench. Focusing on edit-induced consumer obligations, a full-corpus blinded human audit of the DeepSWE runs identifies terminal mismatches, including diagnoses whose task scope remains disputed. Following supplementary execution checks, all retained DeepSWE terminal events have execution support. The audit also shows that recovery within a trajectory can coexist with terminal omissions in the same run. The process analysis links the presentation of relevant consumer code to explicit dependency judgments and subsequent synchronization actions recorded in the trajectories. An explicit dependency-review prompt reduces terminal omissions under the tested conditions, supporting re-derivation of consumer obligations after edits. Local replays of selected DeepSWE cases show that synchronizing the diagnosed consumers restores the target behavior while the listed controls continue to pass. Cross-benchmark execution counterexamples show that the original task evaluations do not fully detect edit-induced dependency mismatches: patches pass those evaluations, yet additional execution checks confirm unintended defects along existing consumer paths. These findings support measuring task scores, terminal propagation states, and recovery separately.

---


### 197. [Seeing Is Not Acting: WARD Diagnoses the Evidence-to-State-to-Action Gap in Longitudinal Clinical Agents](https://arxiv.org/abs/2611.29243)

**<font color=#1a73e8>作者：</font>** Chao Ding, Yidong Jiang, Junzhi Ning 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models for longitudinal clinical care must revise their assessments and actions as patient information accumulates. However, benchmarks centered on isolated responses or final task outcomes provide limited insight into intermediate failures in evidence use, state updating, and action selection. We introduce WARD, a benchmark for evaluating how clinical agents translate accumulating evidence into patient-state judgments and timely, safe actions. WARD comprises 4,560 clinical tasks across seven clinical output domains, organized into 240 checkpoints from 40 longitudinal clinical trajectories spanning 95 hospitalizations. Its Longitudinal Track evaluates these tasks under controlled cumulative evidence. Its Interactive Track evaluates end-to-end, tool-mediated clinical management across 271 verifiable evidence items and 141 reference transitions. Across 12 models with scorable checkpoint outputs, evidence recognition consistently outpaces downstream state and action decisions, with linked-evidence nonresponse reaching 74.47--90.90\%. Models also struggle to retain and update information over time, while in the Interactive Track only 11.46\% of executed actions advance a reference transition. These results reveal a persistent evidence-to-state-to-action gap and highlight the need for process-level evaluation of longitudinal clinical this http URL and data: this https URL.

---


### 198. [TurboFHE: An Efficient and Scalable Multi-GPU Framework for Homomorphic LLM Inference](https://arxiv.org/abs/2611.29244)

**<font color=#1a73e8>作者：</font>** Honghui You, Haoping Yang, Wenzhe Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) enables privacy-preserving large language model inference but remains computationally intensive. Existing multi-GPU FHE inference systems rely on expert-crafted parallelization plans that generalize poorly across hardware platforms and applications. We present \fwName, a framework that automatically compiles CKKS inference programs into efficient multi-GPU executables. Its compiler can split different nodes of the same computation graph at the ciphertext and polynomial level. Guided by a measurement-based performance model, its hardware-aware planner jointly optimizes task partitioning, placement, operand residency, and transfer scheduling. %Critical-path-guided rewrites extract shared computation and restructure homomorphic sums. Its backend then generates optimized GPU kernels and executes plans using CUDA graphs and selective point-to-point transfers. \fwName adapts its plans to diverse hardware configurations and FHE inference algorithms for large-scale models. On a single A100 GPU, \fwName achieves a $24.5\times$ speedup over THOR's reported BERT-Base inference latency. For Cerium's Llama-3-8B workload, \fwName outperforms Cerium's expert-crafted plans by $1.14\times$, $1.16\times$, and $1.24\times$ on 2, 4, and 8 RTX PRO~6000 GPUs, respectively. On A100 GPUs, \fwName achieves $98.0\%$, $91.8\%$, and $79.3\%$ parallel efficiency for the same workload on 2, 4, and 8 GPUs, respectively.

---


### 199. [MM-DataLoop: Closing the Data-Side Loop for Recursive Self-Improvement in MLLM Post-Training](https://arxiv.org/abs/2611.29254)

**<font color=#1a73e8>作者：</font>** Likang Peng, Chen Ju, Xu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) offers a path toward improving models through repeated evaluation and revision. We study its data side in multimodal language model (MLLM) post-training, where heterogeneous operations and cross-round evidence must be coordinated. MMDataLoop organizes data interventions into five operation families and connects them through an Observe-Diagnose-Plan-Execute-Verify-Reflect cycle with shared rule memory. Across 34 candidate rounds on Qwen3.5-0.8B and five benchmarks, we hold the base initialization, shared training schedule and evaluation protocol fixed while varying data recipes. The five-benchmark mean reaches 63.04 at R33, up 5.32 points from the zero-shot baseline; R29, R32, and R33 form a close top cluster within 0.09 points. In eightcandidate comparisons, guided search reaches the preselected target in six candidates and identifies the top observed candidate, while random arms show higher means and lower dispersion. The selected R29 recipe also scores above two full-pool baselines under the same epoch schedule. Together, these findings establish MM-DataLoop as a traceable workflow and provide an empirical basis for studying how data-side decisions shape outcomes across MLLM post-training recipes.

---


### 200. [NoeVera: Can Knowledge Guide Experiments and Experiments Refine Knowledge?](https://arxiv.org/abs/2611.29255)

**<font color=#1a73e8>作者：</font>** Pinaki Prasad Guha Neogi, Spyros Mastorakis, Ankur Mallick 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the growing demand for large language model (LLM) services, optimizing LLM serving systems is becoming increasingly complex, and the bottleneck is no longer predicting how a given configuration will perform. The harder problem is deciding what to investigate: which mechanisms matter for a workload, which configurations are worth testing, and what evidence a decision still needs. In this work, we present NoeVera, an agentic Second Brain that goes beyond just one-shot retrieval by turning papers, code, benchmarks, and experimental results into a persistent, provenance-preserving knowledge base with three planes: source evidence, reusable synthesis, and agent memory. Decision-aware retrieval assembles compact evidence packs, role-specific agents reason over them and invoke a simulator (Vidur or GAUSS) whenever quantitative support is needed, and every finding is written back as a scoped evidence record, so knowledge guides experiments and experiments refine knowledge. In configuration search over four serving scenarios, NoeVera comes within 5% of the optimum in a median of 6-7 simulator calls, versus 9 for Bayesian optimization and 15 for a knowledge-free agent with the same tools; on A100 GPUs, its representative configurations deliver ~1.30x vLLM-default throughput and meet every scenario's latency objective. When reused, provenance-preserving evidence records over-generalize on only 8% of applicability traps, versus 28% for a general-purpose agent memory. On the held-out 48-task split of a 72-task benchmark, NoeVera scores 29% higher than an equally equipped agent and 36% higher than its single-call retrieval counterpart (0.80 vs. 0.62 and 0.59), and even when baselines receive NoeVera's own prompts, a statistically significant part of its evidence-evolution advantage remains.

---


> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
