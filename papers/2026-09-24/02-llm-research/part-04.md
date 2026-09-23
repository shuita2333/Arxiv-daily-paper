# 🧠 大模型相关研究 | 2026年09月24日

> 本类共 **206** 篇论文：已确认 **192** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-206](./part-05.md)

---

### 151. [PACT: From Credit Assignment to Critic Alignment](https://arxiv.org/abs/2609.26355)

**<font color=#1a73e8>作者：</font>** Jiayan Fu, Hang Xu, Yong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a central component of large language model (LLM) post-training, yet token-level credit lacks a generally accepted mathematical definition, leaving its relationship to commonly used training signals unclear. We formulate three regularity conditions, namely Completeness, Prefix Consistency, and Neutrality, and prove that they uniquely determine token-level credit. This characterization provides a unified basis for explaining phenomena across existing algorithms and guides the development of an improved actor-critic training procedure. Through this lens, an ideal teacher in On-Policy Distillation (OPD) acts as an implicit critic, yielding an expected policy gradient proportional to that induced by token-level credit. Response-level REINFORCE Leave-One-Out (RLOO) signals match the expected policy-gradient contribution of token-level credit despite their coarser granularity. We further establish approximate credit sparsity under bounded outcome rewards and show how intermediate critic errors in Generalized Advantage Estimation (GAE) can become comparable to the underlying credit. These motivate Policy Aligned Critic Training (PACT), which adopts an Actor-then-Critic update order to apply importance sampling correction to critic training and better align the critic with the updated policy. In agentic mathematical reasoning, PACT achieves 72.87% average accuracy across four benchmarks, outperforming GRPO and PPO by 8.80 and 13.16 percentage points, respectively. On SWE-bench Verified, PACT achieves a pass rate of 67.4%, outperforming PPO, GRPO, and SAO by 2.4, 2.0, and 3.8 percentage points, respectively.

---


### 152. [TimeInteract: Towards Real-Time Interactive Intelligence for Streaming Time Series](https://arxiv.org/abs/2609.26389)

**<font color=#1a73e8>作者：</font>** Sheng Pan, Yongli Gu, Yiqing Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time series evolve continuously, with meaningful changes potentially emerging at any moment. However, existing time-series language models (TSLMs) remain inherently static. They either receive complete sequences for offline processing or alternate between streaming input and response generation, which prevents processing of new observations during interaction. We introduce a new regime, Time-Series Interaction: a model continuously perceives incoming time-series observations and user intent, autonomously decides when to remain silent or respond, and continues processing new observations during response generation. To realize this, we develop TimeInteract with three key designs: a dual-view streaming TS encoder that captures local variations and historical dynamics, a response control mechanism that learns when to trigger a response, and a decoupled streaming inference mechanism that separates control from response generation to avoid blocking subsequent observations. We further formulate a hierarchy of interaction capabilities, progressing from Understanding to Adaptivity. Based on this hierarchy, we construct StreamTSI-34K, a large-scale streaming TS interaction dataset with 34,588 episodes and 77,505 responses across synthetic and real-world time series in single- and multi-turn settings. Across all four interaction levels, TimeInteract consistently outperforms existing LLMs, VLMs, and TSLMs, with gains of up to 23.92 points on challenging tasks. It also improves response triggering while achieving near-zero stream stall and up to $2.15\times$ inference speedup.

---


### 153. [Combining Hierarchical Cognitive Process with Process Supervision for Interpretable Scene Safety Understanding](https://arxiv.org/abs/2609.26399)

**<font color=#1a73e8>作者：</font>** Zhiyun Jiang, Hanyong Wang, Binbin Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scene safety understanding plays a life-or-death role in situational awareness in various critical domains. Traditional methods that rely on learning direct mappings between scenes and safety levels often lack interpretability, limiting their reliability in critical applications. An effective approach to overcoming this challenge lies in interpreting human cognitive processes and equipping machine models with analogous cognitive capabilities. This work explores an effective way of integrating scene safety cognitive process modeling and process supervision. Specifically, we first construct a hierarchical cognitive safety structure, which motivates the development of a novel, high-quality scene safety understanding dataset based on multi-step reasoning with process labels. This dataset serves both as a benchmark and a resource to improve the safety reasoning capabilities of Large Language Models (LLMs), while also enabling a granular analysis of intermediate reasoning steps through information flow and saliency-based techniques. Building upon this foundation, we introduce a modular and flexible process supervision framework that reflects the hierarchical nature of human cognition. This framework leverages LLMs as the core architecture and incorporates Low-Rank Adaptation(LoRA) and Mixture-of-Experts (MoE) strategies to enable specialization and collaboration among expert modules, each tasked with specific sub-processes of the overall reasoning chain. Systematic experimental evaluations and analyses confirm that our framework exhibits superior interpretability and performance characteristics compared to traditional approaches.

---


### 154. [OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery](https://arxiv.org/abs/2609.26402)

**<font color=#1a73e8>作者：</font>** Thomas Egg, Harry Winston Sullivan, Ellad B. Tadmor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The discovery of novel inorganic materials drives technological breakthroughs in critical fields such as computing and energy storage. Generative AI has promised to accelerate the materials discovery pipeline, but state-of-the-art flow and diffusion models remain bottlenecked by the cost of proposing candidate materials. To address this, we introduce OMatG-flash, an all-atom flow map for inorganic crystal structure prediction (CSP) and de novo generation (DNG). OMatG-flash is a Pareto-optimal inference engine for materials, sampling candidate materials with an order of magnitude fewer inference steps and less wall-clock time than existing flow and diffusion models while demonstrating benchmark performance on par with the state-of-the-art. To enable post-training fine-tuning we apply Reinforce Adjoint Matching to flow maps, further improving match rates and RMSE on the unconditional CSP task. OMatG-flash showcases the potential of flow maps to accelerate generation of high-quality candidate inorganic materials and demonstrates a step forward in sample throughput necessary for data-hungry materials discovery workflows.

---


### 155. [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](https://arxiv.org/abs/2609.26425)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhao, Xiaobin Hu, Bo Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> KV cache memory has become a major deployment bottleneck for video generation and world models, which motivates low-bit quantization study for efficiency. Existing 2-bit KV cache quantization methods can achieve nearly lossless performance on video benchmarks such as VBench, however, we find that they still cause severe temporal flickering and visual degradation. Meanwhile, deeper investigates show that Key quantization produces smaller reconstruction errors than Value, but surprisingly leads to much larger output degradation. We trace this discrepancy to attention: small Key perturbations can change the attention logits, i.e., QK^\top, and shift the temporal-spatial tokens selected by Queries. These observations motivate us to explicitly preserve attention logits and temporal-spatial token selection during KV cache quantization to alleviate the visual degradation problem. To address this issue, we present QuantWM, a training-free and strictly causal 2-bit KV cache quantization framework. QuantWM introduces two complementary techniques to mitigate the attention shifts. Firstly, quantization-sensitivity-aware clustering (QSAC) jointly considers historical Query sensitivity and residual ranges to select INT2-friendly Key centroids, which reduces quantization errors in channels that are more critical to attention. In addition, principal-subspace attention compensation (PSAC) restores the remaining Key errors along the dominant Query subspace using low-rank projections, which provides a direct and efficient correction to stabilize attention logits. Extensive experiments on Causal-Forcing, LingBot-World-v2, HY-World 1.5, Matrix-Game-2 and Longcat-Video demonstrate that QuantWM significantly improves visual quality and temporal consistency, while outperforming existing methods across image and video quality metrics with up to 6.20x KV cache memory compression and limited additional overhead.

---


### 156. [How to Estimate Whether You Have Found Several Needles in a Haystack: Measuring Calibration in Multi-Label Text Classification](https://arxiv.org/abs/2609.26468)

**<font color=#1a73e8>作者：</font>** Sophie Henning, Georg Hofmann, Alexander Schulte 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A key factor in deciding whether to trust an automatic prediction is its confidence score, which should be calibrated to match the actual probability of the prediction being correct. Most confidence calibration metrics target binary or multi-class tasks, while multi-label calibration remains largely underexplored. Multi-label classification tasks, such as assigning medical codes to clinical notes or determining news topics, are usually dominated by a large number of negatives, i.e., labels that do not apply. We show that existing binning schemes to compute label-wise expected calibration error either underestimate the error, simply reflect label frequency, or suffer from many bins with very few instances. To achieve trustworthy label-wise calibration errors, we propose a new binning scheme that gives equal weight to positive and negative label assignments. Our empirical study demonstrates that in contrast to existing binning schemes, our new scheme results in meaningful estimates of calibration error in hierarchical and in extreme multi-label classification. We also show that calibrating confidence scores of large language models for multi-label predictions is an open challenge. Our detailed analysis lays the foundation for further research by providing a solid evaluation metric for measuring calibration in multi-label classification.

---


### 157. [Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies](https://arxiv.org/abs/2609.26481)

**<font color=#1a73e8>作者：</font>** Rasika Muralidharan, Haewoon Kwak, Jisun An  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Social norms cannot be identified from behavior alone: the same cooperative equilibrium may reflect shared expectations, strategic incentives, or simple imitation. Yet in multi-agent large language model systems, prior work largely treats behavioral convergence as evidence of norm emergence. In this work, we introduce an evaluation framework that measures agents' reported empirical and normative expectations in addition to behavioral convergence. Through controlled ablations, we test the effect of expectation elicitation and isolate two collective mechanisms central to theories of norm formation---social learning through interaction and social selection through network-based group formation. We further test the stability of these resulting dynamics under adversarial disruption across four LLM families. We find that eliciting expectations increases cooperative contributions, while social learning stabilizes behavior, and social selection reliably identifies cooperators but provides limited behavioral reinforcement. Following disruption, normative expectations and behavioral coordination recover differently. Together, these results show that similar cooperative outcomes can arise from different underlying social processes. By making expectations observable, our framework allows us to attribute each mechanism's contribution separately, offering designers of multi-agent systems a principled basis for selecting the social processes that sustain cooperation.

---


### 158. [From Token Importance to Conditional Removability: Rethinking Visual Token Pruning in Multimodal Large Language Models](https://arxiv.org/abs/2609.26484)

**<font color=#1a73e8>作者：</font>** Shengli He, Yongchao Liang, Roumeng He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free visual-token pruning often uses token importance, redundancy, or related selection criteria as proxies for safe removal. We show that these signals alone do not fully characterize removability, which is conditioned on both representation depth and the surrounding deletion set. Controlled interventions demonstrate that removing the same tokens at different depths produces substantially different downstream perturbations, while changing only the deletion context at a fixed depth alters candidate marginals and pruning-boundary decisions. These findings show that token importance alone cannot determine when a token is safely removable or how its removability changes under joint deletion. Motivated by this perspective, we propose CoRePrune, a training-free two-stage framework. Progressive Perturbation-Aware Visual Pruning refreshes deletion effects as visual representations evolve, while Set-Conditioned Refinement reevaluates candidate rescue benefits under the current deletion set after visual--text interaction. Across five multimodal large language model backbones covering standard images, high-resolution inputs, and video, CoRePrune preserves performance under aggressive token budgets. On Qwen3.5, with a final budget of 128 visual tokens, it retains 90.3% of dense-model performance while reducing aggregate prefill time by 51.0%.

---


### 159. [Spoken Language Models that Think Aloud](https://arxiv.org/abs/2609.26488)

**<font color=#1a73e8>作者：</font>** Junyi Ao, Kainan Peng, Mingbo Ma 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Chain-of-Thought (CoT) reasoning has improved the capability of language models, directly applying it to Spoken Language Models (SLMs) may introduce long silent intervals under the serial "think-then-speak" paradigm, disrupting real-time spoken interaction. To address this issue, we propose an asynchronous think-aloud framework for reasoning-based SLMs within the Thinker-Talker architecture. The framework maintains a primary reasoning stream for logical deduction and a lightweight think-aloud stream that generates short, task-grounded progress utterances conditioned on the user input and the evolving reasoning state. A dynamic balance strategy coordinates the two streams at runtime, triggering additional think-aloud speech to avoid silent gaps and canceling pending utterances when the final response becomes ready. Experiments on spoken reasoning and question-answering benchmarks show that our approach substantially reduces user-audible silence during reasoning while maintaining answer accuracy comparable to that of a serial "think-then-speak" baseline, demonstrating the potential of asynchronous think-aloud for responsive interaction in SLMs.

---


### 160. [Calibration as a First-Class Criterion in LLM Evaluation](https://arxiv.org/abs/2609.26489)

**<font color=#1a73e8>作者：</font>** Mario Sanz-Guerrero, Katharina von der Wense  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Calibration of language models -- the alignment between expressed or implicit confidence and empirical correctness -- is a well-studied subfield within NLP. Methods to measure it already exist. The problem is adoption: outside this subfield, NLP research regularly introduces new models, datasets, and benchmarks without checking whether the model's confidence scores are meaningful. We argue that this adoption gap is a major obstacle to trustworthy LLM evaluation. Miscalibration causes problems in two distinct areas: at deployment, where overconfident mistakes cause real harm, and inside the research pipeline, where methods like LLM-as-a-judge, synthetic data generation, and active learning rely on calibrated confidence without verifying it. Standard calibration metrics only require two inputs per example: a confidence score and a correctness judgment. Most benchmarks in use today already provide both, meaning calibration can be reported immediately. For open-ended generation, however, defining these two inputs is still an open challenge. We argue that each NLP subfield should pair its main performance metric with a calibration score and call for treating calibration as an essential property of every model rather than a niche topic.

---


### 161. [Semantically-Guided Domain Randomization for Industrial Object Detection in Low-Image-Budget Regimes](https://arxiv.org/abs/2609.26505)

**<font color=#1a73e8>作者：</font>** Jose Moises Araya-Martinez, Gautham Mohan, Jens Lambrecht  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retraining visual perception pipelines in High-Mix, Low-Volume (HMLV) automotive manufacturing must be carried out under tight annotation, energy, and time budgets, yet most Synthetic Data Generation (SDG) strategies still operate in the thousands of images. This work evaluates Semantically-Guided Domain Randomization (S-GDR), an annotation-free adaptation pipeline that couples Vision-Language Model (VLM)-based semantic captioning of a small unannotated real reference set with diffusion-based background synthesis (Stable Diffusion XL (SDXL) conditioned by ControlNet and IP-Adapter) and mask-based object composition. On an automotive multi-object detection benchmark and with a fixed budget of 200 synthetic training images, S-GDR reaches mAP50-95 = 0.739 on a real held-out test set, outperforming a domain-randomized render baseline (mAP50-95 = 0.697) as well as brightness filtering, perceptual hashing, CycleGAN style transfer, and unguided diffusion variants sharing the same 200-image budget. These initial observations position S-GDR as a promising annotation- free alternative for extreme data-scarcity regimes.

---


### 162. [Virtual Encoders in Multimodal Transformers](https://arxiv.org/abs/2609.26513)

**<font color=#1a73e8>作者：</font>** Katsuya Ogata, Yuta Nakashima  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal language models traditionally rely on dedicated perceptual encoders to construct task-usable representations. More integrated architectures have recently emerged, which instead expose the shared transformer to lightly projected patches, audio frames, or discrete visual tokens. Where does this encoding happen when such representations are not provided? We find that the transformer can internalize this missing computation, constructing task-usable perceptual representations within its own early-to-middle layers before the downstream language model. We call this computational structure a Virtual Encoder. Across linear probing, similarities to perceptual encoders, and causal analyses, we identify signatures of this structure in models that receive perceptual tokens without continuous encoder-derived features. These analyses also suggest that the boundary between perception and language processing need not coincide within an architectural module. Instead, encoder-like computation can emerge as a functional regime within a shared transformer, providing a new perspective for understanding where and how multimodal models process perception.

---


### 163. [A Semiotics-Aware Framework for Evaluating Fidelity and Coverage in Natural Language Generation](https://arxiv.org/abs/2609.26527)

**<font color=#1a73e8>作者：</font>** Lorenzo Zangari, Davide Picca  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When two texts describe the same expression, standard metrics based on lexical overlap or whole-text similarity may fail to detect meaningful differences in how that expression is framed. We propose a framework to evaluate semiotic alignment between texts, where a semiotic profile encompasses both the contextual meaning and the discourse references made salient by a text. Our approach yields two scores, Semiotic Fidelity and Semiotic Coverage, estimating how much of one text's profile is supported by the other and how much of the other's profile it recovers. Experiments show that coverage is typically lower than fidelity, and that alignment between LLMs and human-curated data is highest at low sampling temperatures, while higher temperatures reduce this alignment.

---


### 164. [REFLEX with Jev for Efficient Selective Control in LLM Agents](https://arxiv.org/abs/2609.26532)

**<font color=#1a73e8>作者：</font>** Tiantong Wu, Wei Yang Bryan Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents often use generative models for bounded decisions, raising the question of when these decisions can be handled more efficiently without reducing task success. We study REFLEX, an agent architecture that uses Jev as a fast, typed decision layer and calls a strong LLM when confidence is low, or generation is required. On a frozen 100-task benchmark, REFLEX achieves 95% success with 72.7% fewer strong-model calls than a strong-only agent, with reductions persisting across three fallback families. Controlled interventions show that reliability depends on action-set size and near-valid alternatives near authorization boundaries. External BFCL and $\tau$-style evaluations reveal limited advantages over a cheap generative cascade when ordinary routing is already highly accurate. These findings identify when selective control with Jev can reduce computation and where its benefits are limited.

---


### 165. [Transcribe, Translate, and Optimize: Joint Reward Learning for Speech Translation](https://arxiv.org/abs/2609.26536)

**<font color=#1a73e8>作者：</font>** Yanghe Dong, Wanting Huang, Weiran Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In LLM-based speech translation, transcription-based chain-of-thought (CoT) suffers from a mismatch between reference transcripts used in supervised fine-tuning (SFT) and model-generated transcripts at inference. To address this, we propose joint recognition and translation fine-tuning via group relative policy optimization (GRPO). We score both transcripts and translations, with translation conditioned on model-generated transcripts, and compare three token advantage strategies. Using Qwen2.5-Omni-3B across four languages, we evaluate CoT against direct speech translation (Direct ST) under SFT and GRPO, training on CoVoST 2 and testing on CoVoST 2 and FLEURS. CoT GRPO outperforms Direct ST GRPO by 1.77 and 0.83 average BLEU points on CoVoST 2 and FLEURS. Compared to CoT SFT, GRPO boosts BLEU by 0.82 and 0.67 points and reduces word error rate (WER) by 8.8% and 7.2% relatively. These results highlight reinforcement fine-tuning as an effective method to mitigate the training-inference mismatch, jointly improving recognition and translation.

---


### 166. [A retrospective analysis on the use of LLMs to study infant syntax learning](https://arxiv.org/abs/2609.26539)

**<font color=#1a73e8>作者：</font>** Hélie Bazin, Anouk Barberousse, François Yvon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have increasingly been used to investigate how children acquire syntax at an early stage of development. This is notably the central scientific goal of the BabyLM challenge, a community-wide effort to develop models that achieve human-level syntactic performance while being trained on developmentally realistic corpora. In this paper, we reflect on the use of LLMs in the study of infant syntax learning by providing an epistemological assessment of several studies from this research program. We discuss how datasets are built, which models are implemented, how they are trained and syntactically evaluated. We observe significant assumptions in the methodology of BabyLM and related studies, thus mitigating their theoretical scope. We additionally observe that using developmentally-realistic corpora have limited effects on models performance on commonly-used benchmarks, which suggest important computational differences between LLMs and the infant syntax learner.

---


### 167. [JEV-as-a-Judge: Accept When Confident, Escalate When Unsure](https://arxiv.org/abs/2609.26550)

**<font color=#1a73e8>作者：</font>** Yubo Li, Yidi Miao, Ramayya Krishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge enables evaluation across diverse tasks, but inference cost and confidence reliability become critical at scale. We study whether a decision-only judge can provide an economical first pass and identify when stronger evaluation is needed. Comparing jev-as-a-judge with sixteen generative and reward-model judges, with blinded human adjudication, we find it within three percentage points of a state-of-the-art LLM judge, our strongest comparator, on ordinary preference and evidence-grounded factuality at 0.36% of the comparator's fee. Larger gaps arise when judgments require checking a derivation or resisting an elaborately written wrong answer. On several benchmarks, JEV's gap to this comparator is concentrated in low-confidence decisions. A frozen cascade that accepts confident verdicts and escalates uncertain ones retains 99% of the comparator's accuracy at lower cost.

---


### 168. [Rouxii: Exploiting Honeypots with Deception-Aware AI Pentesters](https://arxiv.org/abs/2609.26555)

**<font color=#1a73e8>作者：</font>** Arthur Cordeiro, Alberto Maria Mongardini, Emmanouil Vasilomanolakis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Honeypots are designed to deceive attackers, and recent work shows they can also derail autonomous LLM-based pentesters. These evaluations, however, largely consider attackers unaware of the deception they face. We study the opposite setting: an autonomous attacker explicitly equipped to recognize and act on honeypot fingerprints. We introduce Rouxii, an AI-driven penetration-testing framework that integrates counter-deception into reconnaissance and pivots from honeypot detection to exploitation. We evaluate matched vanilla and anti-deception Rouxii configurations across three reasoning models and eleven network setups over twelve cycles (1,544 attack reports). Between the matched cohorts, which differ only in the prompt, counter-deception raises correct honeypot identification from 19% to 97%, an effect strongest on OT services (11% to 97%), while false alarms on the real service stay at 0.7%. Deception-unaware baselines (PentestGPT, HackingBuddy) fail similarly, indicating the effect is not specific to our framework. Detection, moreover, is not the endpoint: through a white-box analysis of the honeypots themselves we show that a detected trap can be turned against its operator, demonstrating a denial-of-service that disables Conpot without tripping its liveness monitoring, and a corruption of the intelligence a GasPot instance reports. These findings show that deception effectiveness depends strongly on attacker knowledge, and that evaluations of honeypot resilience against AI attackers must account for adversaries that actively reason about and exploit the deception layer.

---


### 169. [Receptiveness, Not Sycophancy: Distinguishing Engagement from Deference in Language Models](https://arxiv.org/abs/2609.26579)

**<font color=#1a73e8>作者：</font>** Calvin Isley, Johann Gaebler, Max Lamparth 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A central concern with language models is sycophancy: their tendency to defer to users' views at the expense of independent substantive judgment. In parallel, work on social sycophancy has focused on behaviors such as validation and positivity that may signal inappropriate deference. Yet the markers of social sycophancy are also characteristic of conversational receptiveness, a construct from social psychology shown to improve interactions across disagreement. We argue that this overlap creates a construct-validity problem for social sycophancy evaluations. Using a popular moral-advice dataset, we find that responses classified as more socially sycophantic are also more receptive. Further, increasing the receptiveness of human-written responses---while preserving their substantive conclusions---causes them to be classified as more socially sycophantic. This tight coupling raises the possibility that social sycophancy evaluations inadvertently penalize desirable behavior. In a preregistered experiment comparing substantively equivalent responses, participants prefer the more receptive responses, expect users to be more likely to listen to them, and are more willing to seek advice from their authors. The same overall pattern persists even among participants who believe the original question asker is in the wrong. Finally, we introduce a simple approach that substantially increases receptiveness without increasing substantive deference, demonstrating that conversational receptiveness and substantive independence can be achieved together.

---


### 170. [Semantic Abstraction for Natural Language Inference: a Methodological Framework for Discovering and Compensating Semantic Knowledge and Reasoning Gaps in Large Language Models](https://arxiv.org/abs/2609.26610)

**<font color=#1a73e8>作者：</font>** David Torres-Moreno, Jorge Hermosillo-Valadez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite their outstanding performance on many NLP tasks, LLMs face serious challenges related to semantic abstraction. In this study, we are interested in understanding how LLMs leverage abstract semantic knowledge in natural language inference (NLI), which requires sophisticated linguistic capabilities to interpret implicit meanings, contextual conceptual relationships, and semantic connections between words and phrases. To this end, we propose a methodological framework for constructing new semantic knowledge at a higher level of abstraction, which we define under the notions of semantic compatibility and incompatibility for NLI. In this framework, the meaning of the lexical-semantic relations between the premise and the hypothesis is reconfigured to achieve a more flexible semantic network that induces different reasoning paths in LLMs. These new pathways show a consistent pattern of responses that allows agreement on a single response. The results demonstrate that our proposal allows to discover and compensate for LLMs' semantic knowledge gaps in NLI, achieving significant improvements in accuracy, exceeding 10% for some models, and in particular for the non-entailment class. It is essential to note that LLMs need structured knowledge and not just more data to bridge reasoning gaps. Our hybrid approach directs attention to overlooked word relationships, allowing models to synthesize missing information. We believe that the future lies not in increasing model size, but in creating a semantic scafolding that mimics the flexibility of human thinking. Hopefully, our proposal will enable the development of more robust agents and interpretable reasoning, guiding AI toward reliable language understanding.

---


### 171. [Greedy Decoding Is Not Precision-Invariant: Cross-Precision Output Divergence in LLM Inference](https://arxiv.org/abs/2609.26621)

**<font color=#1a73e8>作者：</font>** Gaoyuan Du, Anam Nawaz Khan, Rex Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Greedy decoding from large language models is commonly treated as deterministic. We show it is not precision-invariant: the same model, prompt, and decoding algorithm produce different outputs in BF16 versus FP16 on identical hardware. Across our evaluations of six models (1.1B-7B parameters, four families; divergence additionally characterised at 12B) and three benchmarks, 49-100\% of prompts diverge; a single token flip often cascades into trajectory-level divergence. We develop an empirical error-propagation analysis and find that 22 layers of accumulated body error do not distinguish flipping from non-flipping steps; the outcome depends primarily on the top-two logit margin at the LM head relative to the directional perturbation between the top-two candidates. The analysis makes five testable predictions about intervention outcomes, including that applying more FP32 compute (broader scope) makes agreement worse. The experiments match all five predictions. The best-performing low-overhead intervention we evaluate, selective FP32 LM head recomputation, triggered only when the margin falls below a threshold, delivers +22-36 pp exact agreement on A10G (+12-21 pp on L4 and A100) at less than 4\% latency overhead in low-batch (batch size <=4) single-stream inference. We map the applicability boundary across six models and four batch sizes, and hypothesise that training-time precision stability is a determining factor. The method is a partial mitigation rather than a universal determinism guarantee: its benefit vanishes when body-originated error dominates, including at batch size >=8 and under end-to-end FP8 in our tests.

---


### 172. [PERSONAWEAVER: Controllable Diversity Beyond Conventional Archetypes in Procedural Character Generation](https://arxiv.org/abs/2609.26629)

**<font color=#1a73e8>作者：</font>** Maan Qraitem, Kate Saenko, Bryan A. Plummer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Procedural character generation aims to populate games, simulations, and other virtual worlds with diverse characters. Large language models (LLMs) offer a promising foundation for scaling this task. However, LLM-based procedural character generation remains at an early stage: existing methods either generate characters directly or adapt profiles retrieved from persona banks. As we show, both approaches produce behaviorally homogeneous populations: characters overwhelmingly agree with positive moral norms and respond to questions with helpful, assistant-like reactions. To mitigate this homogenization, we introduce PersonaWeaver, which disentangles world building from behavioral specification and models behavior through setting general, diverse, manually curated banks of moral positions and conversational reactions. This design allows us to test how far LLM(s) can be pushed beyond their default behavioral patterns across settings. Across ten realistic and fantastical settings and three LLM(s), PersonaWeaver produces broader moral and interactional response distributions than prior work. Its guidance also diversifies interpersonal language, response length, and sentiment. It also produces less archetypal combinations of world attributes. Code is available at this https URL.

---


### 173. [Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models](https://arxiv.org/abs/2609.26637)

**<font color=#1a73e8>作者：</font>** Xiaoyu Luo, Tao Ren, Wenrui Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid capability gains of frontier language models are widely attributed to improved reasoning abilities, yet this cannot be verified as raw CoT traces in closed-source systems are hidden. By registering a simple custom tool through a standard API feature, we induce frontier models to externalize intermediate reasoning. Because these traces may reflect post-hoc rationalization rather than genuine reasoning, we first evaluate against native CoT on open-source models and extend to closed-source frontier models including GPT-6 Astra. We find that the extracted reasoning matches native reasoning performance and substantially outperforms no-reasoning baselines, across competition mathematics, science, and code generation. We then characterize how frontier models structure their intermediate reasoning. Across token efficiency, reasoning-step types, and induced reasoning trees, we identify systematic differences in how models externalize, compress, and organize reasoning. We find that Astra exhibits token-efficient directed reasoning, selecting a correct trajectory earlier, while resolving elementary steps internally and externalizing only crucial reasoning. These findings provide a behavioral lens on frontier-model reasoning beyond benchmark scores.

---


### 174. [Diffusion Drafts, AR Verifies: Accelerating Document OCR with Self-Speculative Decoding](https://arxiv.org/abs/2609.26638)

**<font color=#1a73e8>作者：</font>** Dohyun Kim, Sungjun Han, Hyungguk Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive OCR vision-language models accurately convert document images into text and structured markup, but require one sequential decoding step per output token, limiting inference speed. Unlike open-ended text generation, OCR outputs are strongly grounded in the input image, making diffusion-based parallel generation promising. However, when several tokens are predicted in one diffusion step, each is predicted before the others are known. Committing them directly can therefore introduce errors. We therefore introduce GravityOCR, a parameter-shared AR-block-diffusion model jointly trained for parallel drafting and causal AR verification. Verifying drafts before commitment lets the model commit multiple output tokens per round without a separate drafting network. The causal AR path also enables GRPO with sequence- and structure-level OCR rewards, avoiding diffusion-trajectory likelihood estimation while updating the shared drafter parameters. On OmniDocBench v1.6, AR-path GRPO improves the Overall score from 94.92 to 95.16 without reducing diffusion drafting efficiency, while the final model remains close to the original GLM-OCR score of 95.48. In an SGLang serving deployment, GravityOCR commits an average of 9.7 output tokens per forward pass and achieves a $3.94\times$ decode-only speedup on region crops and a $1.32\times$ end-to-end page-processing speedup over AR decoding.

---


### 175. [MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward Reinforcement Learning](https://arxiv.org/abs/2609.26667)

**<font color=#1a73e8>作者：</font>** Kairui Yang, Ziheng Yi, Xunkai Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaboration topology shapes both the performance and execution cost of LLM-based multi-agent systems. Because tasks differ in complexity and required capabilities, recent approaches generate task-specific collaboration graphs that specify agent participation and information flow. However, representative topology generators use either individual agents or predefined groups throughout an organization, overlooking differing collaboration needs across subtasks. Our key insight is to select granularity locally for each functional role, combining fine-grained control with reusable collaboration patterns within one organization. Learning such organizations requires exploring a combinatorial construction space with limited intermediate feedback from final-answer rewards. Therefore, we propose MAGIC, a dense-reward reinforcement learning framework for mixed-granularity graph generation. Specifically, MAGIC constructs a mixed-granularity agent graph by sequentially selecting a functional role, instantiating it as a single agent or reusable group, and connecting it to existing units. We directly optimize the construction policy using returns from trajectories sampled under the current policy and use potential-based reward shaping to provide intermediate feedback from probe-based utility and structural signals while preserving the cumulative task reward. MAGIC outperforms state-of-the-art baselines across eight benchmarks and demonstrates strong inference efficiency in our efficiency study.

---


### 176. [Stepping into the Margins: How Readers Want AI to Generate Footnotes](https://arxiv.org/abs/2609.26673)

**<font color=#1a73e8>作者：</font>** Piper Vasicek, Courtni Byun, Kevin Seppi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Footnotes can be powerful tools to aid understanding, providing information that augments the reading experience. However, static footnotes cannot address every reader question. Current reading tools allow readers to view curated footnotes, allow personal and social annotation, and link dictionaries to reading material. Many other existing tools and natural language processing (NLP) techniques--such as generative AI, summarization and translation--could be used to address any reader question. However, no one has yet explored which of these features readers actually want. To bridge this gap, we conducted thirteen semi-structured interviews with readers from various backgrounds, followed by a thematic analysis of their responses. We develop themes describing the types of footnotes readers prefer and how to determine the quality of footnotes--specifically focusing on what sources of information a system considers, what the footnotes contain, and how the footnotes are presented to the reader.

---


### 177. [Decoding the Legalese: A Scalable and Quantitative Framework for Analyzing Corporate Privacy Policies](https://arxiv.org/abs/2609.26680)

**<font color=#1a73e8>作者：</font>** Jiaming Tang, Chenlan Wang, Mingyan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Even though privacy policies are the primary mechanism organizations use to disclose how they collect, process, and share personal data, they are difficult for average users to interpret, perhaps by design, due to their verbosity and dense legal language. Importantly, there is a lack of standardized metrics that characterize key qualities of a privacy policy beyond regulatory requirements. Recent advances in large language models (LLMs) make it feasible to automatically structure and analyze these documents at scale. In this study, we develop and evaluate an end-to-end, LLM-enabled system that converts raw privacy policies into fine-grained structured representations and a set of quantitative measures. Our pipeline applies a detailed taxonomy to extract specific data elements and governing practices, capturing relational links that connect each practice to the data elements it references. We apply our framework to a diverse corpus of 10,000 website privacy policies, yielding, to the best of our knowledge, the most comprehensive dataset of its kind to date. Building on our structured representations, we introduce the first standardized and repeatable quantitative metrics for evaluating privacy policies along four dimensions: completeness, transparency, commitment to user protection, and emphasis on business-driven data practices. This allows us to compare policies within and across industry sectors, and to assess the tension between user protection and business interests.

---


### 178. [From Alignment to Access Control: A Framework for GenAI Policy Enforcement](https://arxiv.org/abs/2609.26682)

**<font color=#1a73e8>作者：</font>** Nathalie Baracaldo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) applications have flourished enabling users to chat with large language models, and to create agents to act on their behalf for a variety of tasks. The pace of development of capabilities in this field is incredibly fast with security and safety taking a back seat. Unfortunately, the slower pace at which security and safety mechanisms have evolved has led to real incidents. Policy enables the definition of desirable behavior of applications, and for that reason, it is a cornerstone of making systems secure and compliant. Policy however means different things to different practitioners creating confusion and siloed solutions that are not adequate for compliance. This paper takes a tour of the good, the bad and the ugly when it comes to policy enforcement in GenAI applications. We propose a methodology to systematically analyze and dissect existing approaches to define and enforce policy found in the wild. Based on this principled analysis, we provide recommendations and call for action for the community to address.
This paper is a companion extension of USENIX Security 2026 Enigma talk titled "From Alignment to Access Control: A Unified View of GenAI Policy Enforcement" by the author Nathalie Baracaldo.

---


### 179. [Detecting GPT-Assisted Writing Using Interpretable Stylometric Features](https://arxiv.org/abs/2609.26687)

**<font color=#1a73e8>作者：</font>** Rajesh Kumar, Nabeel Siddiqui, Alexander Fuchsberger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Distinguishing GPT-assisted from independently authored student writing has become a critical challenge in academia. This paper evaluates the discriminative capability of interpretable stylometric features extracted solely from submitted text. Using data from 90 participants who wrote both independently and with ChatGPT assistance, we evaluate eight machine learning classifiers while keeping data from the same participant together during validation. On the held-out test set, Random Forest achieved an ROC-AUC of 0.87 and an F1-score of 0.84, with False Positive and False Negative rates of 22.2% and 11.1%, respectively. SHAP analysis shows that lexical and grammatical characteristics drive the resulting predictions. The findings suggest that transparent, text-intrinsic features provide measurable signal for detecting GPT-assisted writing.

---


### 180. [Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local Tool-Use Evaluation](https://arxiv.org/abs/2609.26693)

**<font color=#1a73e8>作者：</font>** Lijuan Tang, Yuemeng Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A coding agent must emit a valid tool call--a parseable invocation of a tool in the provided schema--before the harness can execute its chosen action. We study how local serving stacks affect this protocol step and show that measured outcomes can depend on the serving layer rather than model behavior alone. In Ollama, the default tools= request is gated per model by a static template flag: some models are accepted and return calls as text, some return native tool_calls, while Phi-3 and Gemma-3 are rejected before inference. In our harness, rejection and retry exhaustion are not preserved as structured failure metadata, so downstream analysis can misclassify them as model non-calls and naively report 0% fidelity. Adding a text tool list while retaining the native channel recovers much of the measured fidelity for accepted models, whereas a uniform text protocol reduces fidelity for Llama-3.2, which has native tool-call support. Cross-stack probes on Ollama, this http URL, vLLM, and SGLang show different handling of the same request. Constrained decoding removes parse failures but can induce non-termination, and turn-pooled versus per-instance estimates differ by up to about 55 points. We conclude with a checklist for treating serving behavior as part of the evaluation protocol.

---


### 181. [Beyond Repeated Sampling: Learning Search Policies for LLM Reasoning](https://arxiv.org/abs/2609.26704)

**<font color=#1a73e8>作者：</font>** Ismail Labiad, Matthieu Kowalski, Marc Schoenauer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly tackle hard reasoning problems by spending more test-time compute, yet the dominant strategy remains naive repeated sampling: draw many independent solutions and hope one is correct. Because such sampling explores only through local decoding noise, it tends to produce many near duplicate attempts rather than genuinely different ideas. We ask whether exploration can instead be steered at a semantic level, by first sampling problem specific concepts, hints, or strategies and then conditioning answer generation on them. We refine this into a simple, more exploratory procedure that emits many diverse concepts in a single trajectory, and evaluate it on hard problems where repeated sampling struggles. We then go a step further and make concept generation trainable: a small concept generator is optimized with reinforcement learning so that its concepts maximize the downstream success of a larger, frozen answer generator. On hard mathematical reasoning problems, the trained concept generator substantially improves the answer generator's pass@k over naive repeated sampling at the same answer generation allocation, surpasses concepts drawn from much larger untuned models, and transfers to answer generators it was never trained against, including a model from a different family. A small model can thus be trained into an effective, reusable search policy for a much larger one.

---


### 182. [Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning](https://arxiv.org/abs/2609.26708)

**<font color=#1a73e8>作者：</font>** Yuanteng Chen, Zhilei Liu, Peisong Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization-aware distillation (QAD) restores much of the short-form question-answering performance lost to sub-3-bit quantization, yet leaves mathematical and code reasoning substantially impaired. Long generations often degenerate into repetitive loops, exhausting the decoding budget without completing a solution. We trace this gap to quantization-amplified exposure bias: QAD trains on fixed corpus prefixes, while quantization-induced deviations compound along the model's own autoregressive trajectories. To address this mismatch, we introduce an on-policy distillation (OPD) stage that places teacher supervision where the quantized model actually goes. Starting from a QAD checkpoint, the student generates through the quantized forward path used at deployment and receives feedback from a frozen full-precision teacher on its own prefixes, combining dense token-level guidance with task-verifier rewards. Across four models at 2.79 and 1.88 effective bits, OPD raises average BF16 performance retention from 35% to 70% on MATH-500 and from 66% to 91% on HumanEval while preserving short-form performance, with reasoning gains substantially exceeding those of continued teacher-forced QAD in matched-budget comparisons. By coupling QAD's stable low-bit initialization with OPD's on-policy reasoning recovery, our framework provides a comprehensive sub-3-bit solution that preserves broad capabilities while restoring long-form reasoning.

---


### 183. [The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence](https://arxiv.org/abs/2609.26718)

**<font color=#1a73e8>作者：</font>** Xiaoyu Yang, Jie Lu, Wei Duan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLMs focus on retrieving distant evidence from extensive context, yet existing work has largely focused on overcoming distance alone. In this work, we identify the Proximity Trap, insufficient attention to distant evidence often arises less from distance itself than from cumulative competition with abundant, task-irrelevant proximal background. To address the Proximity Trap, we introduce LYRA (Long-context heavY-tailed Relevance Alignment), a t-distributed directional matching mechanism that reshapes the context retrieval distribution, directing more attention mass toward task-relevant evidence, while preserving the relative positional information encoded. Extensive experiments on LongBench-v2, RULER, and LongBench demonstrate consistent improvements across context lengths and task categories. We further introduce ProxBench, a multi-level fine-grained benchmark for evaluating distant evidence utilization under increasing proximal background interference. Project page: this https URL

---


### 184. [Does AI Save Time on Product Design? A Randomized Controlled Experiment of AI Prompt-to-Design Workflows](https://arxiv.org/abs/2609.26725)

**<font color=#1a73e8>作者：</font>** Remy Stewart, Olabode Anise, Andrew Hogan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI tools for digital product design now offer prompt-to-design capabilities, allowing designers and their non-designer colleagues to create prototypes through conversational workflows with large language models (LLMs). While these tools promise time savings, experimental evidence in product design remains limited compared with evidence from software engineering. We conducted a randomized controlled trial with 50 product designers and 50 product managers to evaluate prospective time savings from leveraging Figma Make in design work. Participants attempted three standardized design tasks with or without access to Figma Make. Among participants who completed the study tasks, access to Figma Make was associated with approximately 20% shorter completion times, with larger gains among product managers. Our findings suggest that prompt-to-design tools may enable product managers to further contribute to design work, while the benefits for professional designers may be task dependent.

---


### 185. [Evaluating the Semantic-to-Geometric Gap in Adversarial Defenses Against Vision-Language Model-Based Plagiarism](https://arxiv.org/abs/2609.26733)

**<font color=#1a73e8>作者：</font>** Christopher Burger, Christina Trotter, Joseph Carlisle 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapidly advancing capabilities of vision-language models (VLMs) present a systemic challenge to academic integrity. VLMs now allow students to bypass meaningful engagement by capturing and submitting graphical problems as singular images, a practice we define as trivial plagiarism. To provide educators with actionable data on VLM limitations, we investigate the efficacy of heuristic adversarial image transformations designed to degrade model performance while remaining human-interpretable. Through a two-phase evaluation of introductory assessments, we manually assess baseline VLM performance on circuit diagrams, followed by an automated large-scale evaluation of topological structures (logic gates) and coordinate geometry (Karnaugh maps). We find that while highly capable VLMs can exhibit appreciable robustness, all models suffer vulnerability to adversarial perturbations. We conclude that while visual perturbations act as a viable near-term stopgap, long-term assessment security requires educators to reapproach assessment design given continually increasing VLM performance.

---


### 186. [EquivSVA: A Formally Verified Dataset of Behavioral Assertions Across Equivalent RTL Implementations](https://arxiv.org/abs/2609.26751)

**<font color=#1a73e8>作者：</font>** FNU Aditi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to generate SystemVerilog Assertions from natural-language specifica- tions and register-transfer-level designs. Existing datasets and benchmarks support important goals such as large- scale training, formal evaluation, specification-to-assertion generation, and mutation-based testing. A complemen- tary need is to study whether a generated assertion cap- tures externally observable behavior or depends on inci- dental details of one RTL implementation. We present EquivSVA, a formally verified dataset organized around behavior families. Each family contains four structurally distinct RTL implementations of the same externally ob- servable behavior, shared interface-level gold properties, three controlled mutants, and formal-validation evidence. EquivSVA contains 120 behavior families across 12 cat- egories, 480 reference RTL implementations, 914 gold properties, and 360 mutants. Every final family passes a fixed 17-job validation suite covering RTL equivalence, gold-property proofs, property reachability, mutant dis- tinguishability, and gold-property checks on mutants. We also provide fixed family-safe train, development, and test splits. As a small demonstration of the analyses en- abled by the dataset, we evaluate the publicly released, Apache-2.0-licensed Qwen2.5-Coder-7B-Instruct model on the held-out test split. Of 293 interface-only generated properties, 93 are formally sound, and the number of sound properties varies across equivalent implementations for 14 of 24 test families. These results illustrate how behavior-family organization can support controlled stud- ies of assertion-generation robustness without requiring changes in intended functionality. The dataset, generators, validation scripts, and case-study artifacts are publicly released at this https URL.

---


### 187. [Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents](https://arxiv.org/abs/2609.26760)

**<font color=#1a73e8>作者：</font>** Laizhen Li, Jiarui Li, Juanjuan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. We study whether task feedback can instead turn recurring control into reusable executable code, while reserving LLM calls for task-specific semantic reasoning. We introduce Growing Harness, a failure-guided training paradigm that learns the agent harness itself from a strategy-free scaffold that exposes fixed model and tool interfaces but encodes no task-solving controller. Function-level execution traces localize each failure to a bounded code surface, an optimizer repairs a window of failures jointly, and a success-first held-out gate rolls back repair sequences that harm prior capability. Accepted edits accumulate in one shared harness, allowing its control structure to emerge from task feedback. Across BrowseComp-Plus and WebArena-Verified with three deployment models from 4B to 120B parameters, Growing Harness achieves the highest mean success in five of six benchmark-model settings and trails the best mean by 0.7 pp. in the sixth. Relative to a Tool-Calling agent, it reduces LLM calls by 76.0-91.8% and deployed-agent inference cost by 74.4-98.6%. On WebArena-Verified, its success remains 44.7-45.3% across model scales, whereas Tool-Calling falls to 6.7% with the 4B model. Ablations show that trace-local edits, joint repair, and gate-based rollback each improve final success. These results show that persistent program growth can move recurring control out of model context and into low-cost code, yielding reusable specialist agents that remain effective with smaller deployment models.

---


### 188. [CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents](https://arxiv.org/abs/2609.26779)

**<font color=#1a73e8>作者：</font>** Trang Nguyen, Eulrang Cho, Bingqing Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents often work on complex problems that require millions of tokens of context, which necessitates compacting across sessions due to limited context windows. We develop CliffCompaction, an autocompaction technique that reduces cost by up to 50% under a bounded context while maintaining or improving performance on Terminal-Bench and achieving new levels of efficiency for test-time scaling and state-of-the-art results on KernelBench. The per-rollout savings of CliffCompaction make the performance--cost trade-off of test-time scaling more efficient, adding over 10 percentage points on Terminal-Bench for less than the cost of two full-context runs. Under parallel test-time scaling, CliffCompaction lets Kimi K2.6 match Opus 4.7, and exceed Opus 4.6 and GPT-5.3 Codex at lower cost. The key to CliffCompaction's effectiveness is that it keeps compacted information faithful by only truncating or dropping content, never rephrasing or rewriting it. We never compact a compaction---each pass operates only on original content, and prior compacted output is discarded, preventing context drift from accumulating. These properties sustain continual learning over sessions exceeding a million tokens: on KernelBench, CliffCompaction reaches CUDA kernel speedups of $2.23\times$ after 200 steps and $3.58\times$ after 400 steps, surpassing specialized search algorithms and trained agents despite being a general-purpose compaction technique. We open-source a scaffold-agnostic API-proxy implementation of CliffCompaction usable with Claude Code, Codex and other harnesses.

---


### 189. [SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue](https://arxiv.org/abs/2609.26780)

**<font color=#1a73e8>作者：</font>** Haobo Zheng, Tan Tang, Yan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals perceive one another, what information is shared by the group, and how states change over time. Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed across members, groups, and time. Together, these issues reveal two core bottlenecks: message attribution and relational understanding in multi-party dialogue, and state reconstruction from interleaved histories. To address both, we propose $\textbf{SpeakerMem-R1}$: its dual-track memory stores speaker-labeled verbatim messages and derived states organized into person-level and group-level views, then combines evidence from both tracks by entity, event, and time at query time. To reduce attribution and update errors during structured memory construction while enabling local deployment, we train Writer-R1 with SpeakerLevenshtein and speaker-conditioned GRPO. On GroupMemBench, SocialMemBench, and EverMemBench, SpeakerMem-R1 achieves binary accuracies of 47.9%, 69.2%, and 61.9%, respectively. On the publicly reported EverMemBench leaderboard from EverMind-AI, we achieves 62.33%, the best reported result among the latest state-of-the-art frameworks. It also achieves 70.85% on all 1,986 LoCoMo questions, which we use as a two-person long-term conversation boundary test. In a controlled evaluation of 305 questions, RL raises the SFT Writer's mean accuracy from 57.38% to 68.20%. We report both binary accuracy and token-F1, and ablations show that the verbatim and structured tracks, as well as person-level and group-level views, are complementary under the standardized evaluation interface.

---


### 190. [Agensh: Scaling Organizational Intelligence to 1,024 Agents](https://arxiv.org/abs/2609.26781)

**<font color=#1a73e8>作者：</font>** Zhihao Zhan, Ting Song, Li Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A multi-agent system can reduce latency on complex tasks by executing work concurrently. Several pioneering harness frameworks support multi-agent systems. However, the scalability of current multi-agent harnesses is often constrained by a central orchestrator's capacity to allocate tasks and coordinate workers. To address this limitation, we introduce Agensh, a scalable self-organized multi-agent harness without a central orchestrator: concurrent workers execute a multi-agent cooperation loop, continuously gathering context, claiming and self-assigning sub-tasks, taking action and sharing findings, verifying results, and merging progress in an asynchronous manner. The loop is supported by the agentic organization infrastructure comprising three components: a shared workspace holds proposed, ongoing, and completed work; a message interface lets workers communicate; and shared context retains reusable findings and work intentions. To test the scalability of Agensh, we evaluate it on the five hardest ProgramBench tasks with GPT-5.6-sol (high). Scaling from 1 to 128 agents raises the mean final test-pass rate from 19.31% to 28.78%, an approximately 49% relative improvement. Larger organizations reach comparable test-pass rates earlier. On pandoc, scaling from 1 to 1,024 agents raises the final test-pass rate from 33.89% to 55.06%. Worker trajectories further show that different forms of self-organized cooperation gradually emerges and standardizes as the organization grows. These results reveal the number of agents as a new scaling dimension for multi-agent organizations to expand the frontier of general intelligence, offering a practical solution for complex tasks under hard latency constraints or time budgets.

---


### 191. [HARMONY: Hierarchical Agentic Reasoning for MONocular Image-to-Scene Synthesis](https://arxiv.org/abs/2609.26793)

**<font color=#1a73e8>作者：</font>** Shufan Sun, Chen Wang, Enxin Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional 3D scene reconstruction has recently been explored from two directions: agentic reasoning that provides semantic understanding of spatial relationships but lacks precise alignment with input images; and visual geometry foundation models that predict dense point maps from input images but the reconstruction quality is limited. Therefore, recovering a complete 3D scene from a single monocular image with accurate inter-object relationships and high-fidelity reconstruction quality remains challenging. In this paper, we present HARMONY, a hierarchical chain-of-thought framework that leverages both agentic reasoning and visual geometry foundation. Given an image of an indoor scene, starting from an empty 3D floorplan, HARMONY first calibrates the camera against the reference image to establish a semantically-grounded spatial frame, then uses agentic VLM reasoning to recover the 3D room layout and an initial placement order. It then places the objects in a hierarchical order, from wall-mounted elements, free-standing furniture, to dependent decorations on top of furniture. We also use depth-first traversal for furniture so each placement conditions on previously resolved structure and a reflective feedback loop to avoid error accumulation. After each object placement by VLM, we use the point cloud estimations to perform geometry-based refinement so that the rendered image aligns better with the input. HARMONY can produce 3D scenes that are semantically consistent and perceptually aligned with the reference image, extending single-image compositional reconstruction to complex indoor scene images. Experiments on synthetic and real-world images demonstrate that HARMONY outperforms the evaluated reconstruction baselines, while qualitative comparisons with GPT-6 Astra suggest more faithful object arrangements and better preservation of scene details.

---


### 192. [Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs](https://arxiv.org/abs/2609.26796)

**<font color=#1a73e8>作者：</font>** Quan Nguyen-Tri, Mukul Ranjan, Zhiqiang Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive LLMs by enabling non-autoregressive text generation. However, their practical deployment remains limited by inefficient inference, largely due to the absence of effective Key-Value (KV) caching and scalable parallel decoding mechanisms. Existing acceleration methods typically study KV caching and parallel decoding in isolation, overlooking the I/O bottlenecks that arise when cache reuse and parallel token verification are jointly applied. In this work, we introduce $\textbf{Flash-dLLM}$, a training-free inference acceleration framework for fast and memory-efficient dLLMs. Flash-dLLM first identifies GPU memory I/O as a dominant bottleneck in KV-cache-enabled dLLM inference and addresses it with an I/O-aware fused KV-cache kernel that reduces redundant memory movement. Building on this optimized cache mechanism, Flash-dLLM further proposes an efficient KV-cache-driven draft-and-verify decoding strategy, where the dLLM itself serves as both drafter and verifier without requiring an auxiliary model. This unified design enables faster decoding while preserving generation quality and improving scalability to longer sequences and larger batch size. Extensive experiments on mathematical reasoning and code-generation benchmarks demonstrate that Flash-dLLM consistently outperforms existing state-of-the-art dLLM acceleration methods in both inference speed and memory efficiency. In particular, it achieves $5.1\times$ and $11.0\times$ speedups over prior strongest baseline Elastic-Cache on GSM8K and HumanEval, respectively.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 193. [Efficient Iterative Retrieval with Heterogeneous Batching](https://arxiv.org/abs/2609.25405)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dohyun Park, Hubertus Franke, Daniel G. Waddington 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern information retrieval increasingly employs both embedding and generative models to handle complex queries. However, current serving systems suffer from low throughput and poor GPU utilization because they execute these models in isolation. Coarse-grained partitioning, such as dedicating GPUs to specific tasks, fails to adapt to dynamic workloads and creates computational "bubbles". To address these, we present Orthrus, a serving system that performs heterogeneous batching within a unified inference loop. The primary challenge lies in unifying embedding and generation workloads with conflicting computational patterns while optimizing batch composition for high performance. Orthrus addresses these challenges through chunked embedding with incremental pooling and by adjusting batch composition in a workload-aware manner. Evaluation on four A100 GPUs shows that, relative to baseline deployments, Orthrus achieves 1.28$\times$--4.52$\times$ higher throughput on controlled workloads and up to 55.8% lower end-to-end p99 latency on an iterative-RAG benchmark. We release our code at this https URL .

---


### 194. [RAG-NAROK: Retrieval-Aware Knowledge Corpus Poisoning in RAG with Source-specific Refutation](https://arxiv.org/abs/2609.25469)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Abdullahil Kafi, Alvi Ataur Khalil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval augmented generation (RAG) systems have emerged as the dominant architecture for grounding large language model (LLM) outputs in verifiable external knowledge, yet their structural reliance on a dynamic retrieval pipeline introduces a largely unexplored class of adversarial vulnerability. Existing knowledge-base poisoning attacks are fundamentally static. Adversarial documents are pre-computed and injected without any awareness of what the victim system will actually retrieve for a given query, leaving the attack blind to the competitive documentary landscape that surrounds its payload in the generator's context window. Unlike traditional static poisoning attacks that are blind to the retrieved context, we introduce RAG-NAROK (Retrieval-Anchored Generation Negation And Response Quality Collapse), a RAG attack framework that adapts to the query text. RAG-NAROK exploits the transparency inherent in RAG pipeline to first extract the legitimate source identities, then generate Anchor-Specific Refutation documents that explicitly name and devalue retrieved sources while leveraging recency and authority biases to steer the text generation toward a target answer. Our results demonstrate that RAG-NAROK significantly outperforms static baselines across diverse domains, revealing a fundamental tension between RAG transparency and AI security.

---


### 195. [A JEPA Recipe for Tabular Foundation Models](https://arxiv.org/abs/2609.25541)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mingyu Jeon, Suwan Cho, Jae Young Suh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models learn to predict cell values in context, whereas world-model self-supervision asks for prediction in representation space (LeCun, 2022; Assran et al., 2023). On a tabular foundation-model prior, the latent term of a joint-embedding predictive architecture (JEPA) collapsed in our earlier runs and took the encoder with it to a constant map. We report a recipe under which the latent term survives to convergence beside the value objective: the value head reads the encoder field rather than the predictor, and the target is an exponential moving average (EMA) difference. To bound its cost against the value-only arm, both arms train until a plateau rule stops them, with no fixed step budget. A fixed horizon had confounded a slowdown with a ceiling, since the value-only arm was still improving well past the usual budget. At convergence, in one run per arm, the JEPA arm trails the value-only arm across 147 real datasets, 32:70 wins to losses on classification (29:63 with one entry per dataset name) and 8:24 on regression, the margin small on classification and wider on regression, and the count leans the same way in each stratum and each benchmark. The JEPA arm (jepa) needs 1.42 times as many steps as the value-only arm (ds), and 1.66 times its wall-clock, to reach its plateau.

---


### 196. [RootQuantV2: Adapting a Vision Foundation Model for Root-Trait Regression from Minirhizotron Imagery](https://arxiv.org/abs/2609.25567)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kinjalk Parth, Sebastian Varela, Andrew D. B. Leakey  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A lack of high-throughput phenotyping solutions for root traits in field-grown crops has severely constrained understanding and improvement of below-ground traits and processes. Minirhizotrons are the standard non-destructive root-phenotyping method in field environments. Computer vision solutions are needed to allow automated trait estimation at scale, but training data is scarce and human annotations are often inaccessible because they reside in proprietary software that only exports per-image scalar totals of root length and surface area. Nevertheless, large numeric archives of these root traits already exist. RootQuant showed that the traits can be predicted directly from the whole image by regression, thus removing manually traced masks from the pipeline; RootQuantV2 takes that idea further by replacing RootQuant's CNN backbone with a self-supervised ViT. We adapt a frozen DINOv3 ViT-L/16 with a hybrid parameter-efficient scheme. Training only 11.9M parameters (3.78% of the model), RootQuantV2 achieves length and area $R^2$ of 0.950 and 0.930, respectively, while lowering length/area RMSE by 24.3%/20.7% over RootQuant. RootQuantV2 thus repurposes legacy numeric archives for high-throughput, automated root trait estimation.

---


### 197. [C2FXNet: Coarse-to-Fine Scene Expert for Unified Object Detection across Adverse Weather](https://arxiv.org/abs/2609.25693)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianle Fang, Zhenbing Liu, Chong Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection in adverse weather remains challenging because severe degradations weaken visual quality and disrupt semantic feature representations across diverse scenes. Existing methods usually rely on condition-specific designs, which limits their ability to generalize within a unified detector. In this paper, we propose a Coarse-to-Fine Scene Expert Network (C2FXNet) that achieves unified detection through hierarchical scene guidance. Specifically, C2FXNet introduces a dual-level guidance mechanism consisting of a Multi-step Reasoning Router (MRR), which performs GRU-based recurrent scene reasoning over compressed multi-scale visual cues and frozen coarse scene prototypes, and a Fine Scene Refinement (FSR) module, which uses image-specific semantic cues to modulate high-level features for local variation handling. Furthermore, a Scene-aware Mixture-of-Experts (SMoE) dynamically combines scene-specific experts under the joint guidance of MRR and FSR. By coupling coarse scene reasoning with fine-grained semantic refinement, C2FXNet enables robust multi-scene detection without scene-specific training. Extensive experiments on RTTS, ExDark, and our newly constructed Adverse Weather Dataset (AWD) demonstrate that C2FXNet consistently outperforms state-of-the-art methods across foggy, dark, and clear conditions, reaching 63.70%, 71.14%, and 54.19% mAP on RTTS, ExDark, and AWD, respectively. The source code will be released at this https URL.

---


### 198. [Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models](https://arxiv.org/abs/2609.25788)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Panagiotis Michael, Moysis Symeonides, Demetris Trihinas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Foundation Models (TSFMs) promise a paradigm shift toward zero-shot forecasting by eliminating task-specific training. However, existing works often overlook trade-offs between predictive accuracy and probabilistic calibration. This paper presents a benchmark study of six TSFMs evaluated on energy, traffic, and financial datasets. We contrast their performance against statistical baselines and a supervised DL model. The study reveals that while TSFMs outperform statistical methods and supervised models, they are subject to a fundamental trade-off between point accuracy and probabilistic reliability. Specifically, xLSTM architectures provide robust probabilistic calibration across horizons. In contrast, patch-based transformers offer competitive accuracy but face calibration issues at long horizons, while transformer-based models exhibit context saturation points for optimal zero-shot reasoning. These findings offer evidence-based guidance for balancing generalization and uncertainty quantification in real-world deployments.

---


### 199. [In-Context Guidance: Learning Inter-Task Synergies via Numerical Foundational Models for Few-Shot Multitask Optimization](https://arxiv.org/abs/2609.25836)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tingyang Wei, Haofeng Wu, Jiao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task optimization (MTO) addresses a set of optimization tasks simultaneously, often suffering from inaccurate inter-task relationship estimation under limited evaluation budgets, leading to negative transfer. This paper introduces In-Context Guidance Multitask Optimization (ICG-MTO), a novel framework that leverages numerical foundational models to improve inter-task coupling estimation in few-shot scenarios. Unlike conventional methods that rely solely on scarce observed data, ICG-MTO employs a frozen foundational model to infer auxiliary guidance through in-context learning. The framework operates through three stages: constructing an algorithm-specific in-context query from evaluated solutions, using the foundational model to infer a guidance signal characterizing predictive relationships among tasks, and translating this signal into algorithm-specific guidance for maximum-a-posteriori coupling estimation. This approach provides regularization during the early, data-scarce stages of optimization and gradually relinquishes control as task-specific observations accumulate. We instantiate the framework in multitask Bayesian optimization as ICG-MTBO, using directional fitness-class queries to guide inter-task coupling estimation, and further instantiate it in MFEA-II using decision-space-overlap queries to guide random mating probability estimation. Experiments across synthetic benchmarks and a real-world robot arm control problem, together with evaluations under different acquisition functions and evolutionary multitasking, demonstrate the effectiveness and generality of ICG-MTO for few-shot multitask optimization.

---


### 200. [Delving into Asymmetric Information Dynamics for High-Fidelity Virtual Try-On](https://arxiv.org/abs/2609.25881)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zishu Qin, Zhiyu Jin, Pipei Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual try-on (VTON) requires precise pixel-level fidelity, yet mainstream Diffusion Transformers (DiTs) often suffer from texture degradation and structural drift. We identify symmetric interactions in standard joint-attention mechanisms as a source of these failures. Although such interactions support semantic flexibility in general-purpose editing, they allow stochastic noise to corrupt deterministic garment features in VTON. We analyze this problem through asymmetric information dynamics and introduce two diagnostic indicators: Conditional Attention Entropy (CAE) for feature unbiasedness and Injected Information Flux (IIF) for injection effectiveness. Our analysis suggests that symmetric bidirectional attention can corrupt conditional features and attenuate the conditional signal. To address these limitations, we propose RealFit, a framework that combines Unidirectional Information Flow (UIF) with Decoupled Timestep Modulation (DTM). UIF isolates the garment condition from stochastic noise to preserve garment identity, while DTM optimizes the modulation scale to maintain a strong conditional signal. The resulting time-invariant condition branch enables a conditional KV cache that reduces inference time by approximately 75%. RealFit offers a principled approach to conditional generation with state-of-the-art fidelity and efficiency.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-206](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
