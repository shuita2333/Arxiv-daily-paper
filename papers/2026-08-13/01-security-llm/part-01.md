# 🔐 大模型安全相关研究 | 2026年08月13日

> 本类共 **6** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Withholding the Completing Chunk: Deterministic Pair-Completion Guardrails for Streaming LLM Output](https://arxiv.org/abs/2608.10279)

**<font color=#1a73e8>作者：</font>** Christopher M. Frost  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Streaming language-model output creates a release-timing problem: complete-response moderation acts after streamed text has escaped, whereas repeated semantic classification of partial text can be costly and unstable. We study a narrow deterministic construction in which each committed danger signature is the conjunction of two lexical predicates. The guard scans the accumulated prefix before every release and withholds the first chunk that makes both predicates observable. Across four signature families, eight chunk sizes, and 32 mechanism trials, streaming decisions matched the buffered scanner and withheld every pair-completing chunk; eight single-predicate controls passed. In a separate 512-trial strategy comparison, full-prefix scanning and complete buffering detected all configured pairs, a 512-character window detected 96/128, and chunk-local scanning detected 38/128. Fixed pairs flagged 0/338 human-derived safe responses and detected 0/394 jury-labelled unsafe responses, confirming narrow rather than general harm coverage. A calibrated official Llama Guard 3 1B baseline classified 310/338 safe responses as safe and 202/394 unsafe responses as unsafe. Repeated-prefix scanner time on 16,384-character responses ranged from 13.261 ms to 829.640 ms across tested chunk sizes. Pair completion is therefore an exact release-boundary backstop for a small fixed policy, not a substitute for semantic moderation.

---


### 2. [SafeCap: Improving LVLM Safety with Image Captioning Reinforcement Learning](https://arxiv.org/abs/2608.10513)

**<font color=#1a73e8>作者：</font>** Caoyuan Ma, Wenpu Liu, Weichu Xie 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) remain vulnerable to jailbreak attacks that exploit visual inputs to bypass safety alignment inherited from their language backbones. We propose SafeCap, a reinforcement-learning framework that aligns LVLMs through learned self-captioning. SafeCap trains a policy model to first generate a safety-relevant image caption and then produce a final answer; the caption is further optimized by whether it enables a frozen LLM to reach a safety-aligned decision. This caption-mediated objective encourages the policy to expose visual cues relevant to safe response generation rather than relying solely on direct refusal supervision. Across five multimodal safety benchmarks and six vision-utility benchmarks, SafeCap substantially improves aggregate safety performance under its intended DirectCap protocol, with gains of 3.7-19.0 points in safety average across four model settings while maintaining comparable or improved vision utility. Under controlled comparisons on matched backbones and data, SafeCap outperforms safety SFT, DPO, and SafeGRPO, demonstrating the effectiveness of caption-mediated reinforcement learning for multimodal safety alignment.

---


### 3. [ProbGuard: Calibrated Safety Risk Estimation from LLM Output Distributions](https://arxiv.org/abs/2608.10621)

**<font color=#1a73e8>作者：</font>** Xinzhe Huang, Biwu Yao, Kedong Xiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent research on Large Language Model (LLM) safety has widely adopted guardrails to identify unsafe LLM outputs. Existing guardrails typically formulate safety assessment as a deterministic classification task, mapping a discrete token sequence to a discrete safety label. However, this paradigm has two limitations: First, safety assessment is inherently an uncertain problem, particularly during the early generation state. Second, relying solely on discrete token sequences discards the rich probabilistic information embedded in the LLM output distribution. To address these limitations, we propose the first completely probabilistic architecture-agnostic guardrail \textsc{ProbGuard} to leverage the LLM early output distributional signals for estimating and calibrating the safety probability, thereby enabling early stopping of unsafe ongoing outputs. Specifically, given an LLM's generated prefix distribution, we formulate the safety risk as the unsafe probability of its continued generation dynamics and estimate this risk by Monte-Carlo sampling. Through post-training on the distributional signals and calibrated safety risk, \textsc{ProbGuard} achieves the best calibration performance across all nine model--dataset combination settings, reducing the average Brier score and ECE by 79.6\% and 71.9\%, respectively, over the best baseline. \textsc{ProbGuard} further limits the attack success rate to at most 1\% across six representative jailbreak attacks after observing the LLM early output distributions from only the first ten decoding steps.

---


### 4. [REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems](https://arxiv.org/abs/2608.10669)

**<font color=#1a73e8>作者：</font>** Zixing Chen, Xingyuan Liu, Jie Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents combine language-based reasoning with external tools to perform complex tasks. Adversarial inputs can exploit interactions between the agent and its environment, causing the agent to violate safety policies during execution. Yet existing evaluations often reduce agent safety to a single attack success rate (ASR), collapsing exposure, execution, observation, and adjudication and potentially conflating actual violations with evidence visibility. We introduce REDAgentBench, an executable framework for autonomous red-teaming and faithful measurement. It derives attacks from explicit safety constraints and associated agent-system vulnerabilities, runs them in isolated service sandboxes, and verifies harmful effects from service receipts and final-state changes. The benchmark contains 1,661 cases across five service surfaces. Across six models and three agent harnesses, macro-average ASR is 65.69%; reported ASR varies with harness and evidence view, while evaluation-context disclosure changes execution behavior. In a state-grounded diagnostic cohort, almost one in five confirmed violations with resolved action anchors occurs after the agent states the relevant constraint or risk, revealing a Recognition--Execution Gap. Finally, a training-free policy reminder reduces confirmed violations by more than 70 percentage points in matched replay. These findings show that executable evaluation can improve safety measurement and identify actionable intervention points.

---


### 5. [SafeCA: Safe Cross-Attention Localization and Regulation for Text-to-Video Jailbreak Defense](https://arxiv.org/abs/2608.10933)

**<font color=#1a73e8>作者：</font>** Siyuan Liang, Yupeng Qiu, Junfeng Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Video (T2V) generative models are vulnerable to jailbreak attacks in real-world deployment, leading them to produce harmful or inappropriate content. Existing defense approaches mainly rely on input filtering or reconstruction, which not only incur high computational latency but also tend to distort semantics. To address these issues, we experimentally and systematically analyze the differences between clean and jailbreak samples in the cross-attention feature space, revealing for the first time a cumulative separation effect and a progressively increasing trend of linear separability between the two during the diffusion process. Based on this insight, we propose SafeCA, a feature-level defense mechanism for safe cross-attention localization and regularization. Firstly, we identify key defensive regions and values through attention stability analysis using cross-attention features collected from clean prompts within a single inference. Secondly, SafeCA mitigates anomalous activations via attention masking with energy normalization and introduces a lightweight semantic-space adapter to redirect abnormal semantic flows. Furthermore, we detect and suppress potentially malicious tokens by back-propagating feature anomaly signals to the input cue words, thereby enhancing the deployability of the defense in commercial models. Experimental results show that SafeCA reduces the jailbreak success rate by about 20% on mainstream T2V models, adds almost no inference overhead (+0.1s), and maintains good text-video semantic consistency. Overall, SafeCA provides an architecture-level, deployable protection paradigm for T2V generation models.

---


### 6. [Once Poisoned, Arbitrarily Controlled: A Programmable Backdoor in VLMs](https://arxiv.org/abs/2608.10959)

**<font color=#1a73e8>作者：</font>** Tao Lin, Gaojie Jin, Zongxin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing vision-language model (VLM) backdoors are usually treated as static vulnerabilities: one-to-one and N-to-N attacks bind one or more triggers to a finite set of targets before victim training. This assumption substantially underestimates the threat. We show that a single poisoning phase can implant a programmable backdoor into a VLM, allowing an attacker to choose previously unseen target-caption semantics at inference time and synthesize corresponding stealthy triggers on demand. Unlike fixed-mapping attacks, the proposed any-to-any caption-control paradigm decouples post-training target selection from poisoning, enabling dynamic control of target captions without retraining the VLM. Our method has two components. First, a heuristic poisoning strategy exposes the model to diverse trigger-caption pairs, encouraging it to learn a general trigger-as-instruction rule rather than memorize a specific backdoor pattern. Second, a feature-space trigger steganography method maps any attacker-specified target caption to a stealthy visual trigger, implemented as either a norm-controlled perturbation or a non-semantic patch. Once inserted into arbitrary images, these triggers cause the poisoned VLM to generate outputs semantically aligned with the chosen target caption, even when the target was unseen during poisoning. Extensive experiments show that our attack achieves high any-to-any caption-control success rates, preserves clean model utility, and remains effective under several classical backdoor defenses.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
